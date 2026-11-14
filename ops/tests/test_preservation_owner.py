import copy
import hashlib
import io
import json
import sys
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
from test_preservation_registration import fixture
import test_preservation_registration as contract_fixtures
from preservation_contracts import registration_object_id, source_backup_subject
from preservation_registry import (register, records, export_records, advance_readiness, SERVER_OWNER)
from preservation_owner import OwnerAdapter, load_allowed_objects
from preservation_owner_receipts import load_event, store_event


class OwnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.lock = io.BytesIO(b"owner test fixture")
        self.addCleanup(self.lock.close)
        self.control = SimpleNamespace(directory=self.root / "control", state={"mode": "healthy"}, lock=self.lock, done={})
        self.calls, self.commits = [], []
        self.responses = {}
        def fetch(url):
            self.calls.append(url)
            return self.responses.get(url, {"status": 404, "sha256": "", "size": 0})
        def commit(repo, paths, message, redo):
            self.commits.append(redo())
        stage = self.root / "public"
        self.worker = SimpleNamespace(ACTIVE_CONTROL=self.control, QUEUE="ops/queue.txt", fetch=fetch,
                                      commit_and_push=commit, snapshot_root=lambda: stage,
                                      snapshot_file=lambda url: stage / url.split("/snapshots/", 1)[1] if "/snapshots/" in url else None,
                                      capture_parts=lambda url: ("20261114000000", url.split("/20261114000000/", 1)[1]),
                                      id_url=lambda url: url.replace("/20261114000000/", "/20261114000000id_/"),
                                      strict_check=lambda url: (True, "ok"))
        self.registry = self.control.directory / "registry"
        self.allowed = set()
        self.payload = b"exact original image bytes"

    def add(self, *, title="File:one.png", ready=True, snapshot=False):
        request = fixture(title=title, ready=ready)
        request["owner"] = SERVER_OWNER
        if snapshot:
            request["source"] = contract_fixtures.BackupContractTests().snapshot_source()
            subject = source_backup_subject(request["source"])
            backup = copy.deepcopy(request["backup_receipt"])
            backup["subject"] = subject
            request["source_backup_receipt"] = backup
        result = register(self.registry, request)
        self.allowed.add(result["object_id"])
        self.responses[request["source"]["url"]] = {"status": 200, "sha256": request["source"]["sha256"], "size": request["source"]["bytes"]}
        return request, result

    def adapter(self, **kwargs):
        return OwnerAdapter(self.worker, self.repo, self.control, self.allowed,
                            work=self.root / "work", **kwargs)

    def test_paused_modes_never_stage_fetch_or_queue(self):
        self.add(ready=False, snapshot=True)
        for mode in ("auth_blocked", "open", "half_open", "probe_blocked"):
            self.control.state["mode"] = mode
            result = self.adapter(readback=lambda *a, **k: self.fail("paused restore")).prepare(time.monotonic() + 300)
            self.assertEqual(0, result["prepared"])
        self.assertEqual([], self.calls)
        self.assertEqual([], self.commits)

    def test_adapter_requires_actual_active_owner_context(self):
        self.worker.ACTIVE_CONTROL = None
        with self.assertRaises(PermissionError):
            self.adapter()

    def test_unknown_global_registrations_remain_untouched_and_queue_order_is_preserved(self):
        request, result = self.add()
        unknown = fixture(title="File:unknown.png")
        unknown["owner"] = SERVER_OWNER
        register(self.registry, unknown)
        queue = self.repo / self.worker.QUEUE
        queue.parent.mkdir(parents=True)
        queue.write_text("# existing queue\nhttps://example.org/older\n", encoding="utf-8")
        self.assertEqual(1, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual("# existing queue\nhttps://example.org/older\n" + request["source"]["url"] + "\n", queue.read_text())
        rows = export_records(self.registry)["objects"]
        self.assertEqual(1, sum(row["state"] == "queued" for row in rows))
        self.assertTrue(all(not row["submitted"] for row in rows))

    def test_shared_payload_preserves_all_approved_version_mappings_without_duplicate_queue(self):
        self.add()
        self.add(title="File:two.png")
        self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(1, len(self.commits))
        rows = export_records(self.registry)["objects"]
        self.assertEqual(2, len(rows))
        self.assertTrue(all(row["state"] == "queued" for row in rows))

    def test_checked_snapshot_restores_exact_bytes_then_advances_generation(self):
        request, _ = self.add(ready=False, snapshot=True)
        calls = []
        def restore(subject, storage, *, restore_to):
            calls.append(subject)
            restore_to.write_bytes(self.payload)
        result = self.adapter(readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(1, result["prepared"])
        self.assertEqual(source_backup_subject(request["source"]), calls[0])
        self.assertEqual(self.payload, self.worker.snapshot_file(request["source"]["url"]).read_bytes())
        row = export_records(self.registry)["objects"][0]
        self.assertEqual(1, row["generation"])
        self.assertEqual("queued", row["state"])

    def test_stage_budget_does_not_restore_or_queue_private_snapshot(self):
        self.add(ready=False, snapshot=True)
        result = self.adapter(stage_budget=1, readback=lambda *a, **k: self.fail("overbudget restore")).prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertEqual("awaiting_stage", export_records(self.registry)["objects"][0]["state"])

    def test_public_payload_mismatch_is_durable_and_never_queued(self):
        request, _ = self.add()
        self.responses[request["source"]["url"]]["sha256"] = "0" * 64
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertEqual([], self.commits)
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])

    def test_accepted_job_is_reported_while_auth_paused_without_network(self):
        request, _ = self.add()
        self.control.done[request["source"]["url"]] = {"status": "pending", "job_id": "actual-spn-job-123"}
        self.control.state["mode"] = "auth_blocked"
        self.adapter().finish(time.monotonic() + 300)
        self.assertEqual([], self.calls)
        row = export_records(self.registry)["objects"][0]
        self.assertEqual("submitted", row["state"])
        self.assertEqual("actual-spn-job-123", row["owner_job_receipt"]["accepted_job_id"])

    def test_verified_requires_strict_capture_and_exact_raw_payload(self):
        request, _ = self.add()
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.responses[self.worker.id_url(capture)] = self.responses[request["source"]["url"]]
        self.control.done[request["source"]["url"]] = {"status": "verified", "capture": capture}
        self.adapter().finish(time.monotonic() + 300)
        row = export_records(self.registry)["objects"][0]
        self.assertEqual("verified", row["state"])
        self.assertEqual(request["source"]["url"], row["capture_original_url"])

    def test_wrong_historical_payload_never_becomes_new_version_verified(self):
        request, _ = self.add()
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.responses[self.worker.id_url(capture)] = {"status": 200, "sha256": "0" * 64, "size": len(self.payload)}
        previous = {"status": "verified", "capture": capture}
        self.control.done[request["source"]["url"]] = previous.copy()
        outcome = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(previous, self.control.done[request["source"]["url"]])
        event = load_event(self.registry, request["source"])
        self.assertEqual("queued", event["state"])
        self.assertEqual(previous, event["superseded_worker_receipt"])
        self.assertEqual(request["source"]["sha256"], outcome["ledger_updates"][request["source"]["url"]]["registered_payload_sha256"])
        self.assertEqual(1, len(self.commits))

    def test_readiness_compare_and_swap_preserves_newer_observation(self):
        request, _ = self.add(ready=False)
        old = records(self.registry)[0]
        advance_readiness(self.registry, old, {"ready": True, "reason": "first owner check", "stage_bytes": 0}, owner=SERVER_OWNER)
        with self.assertRaisesRegex(ValueError, "advanced"):
            advance_readiness(self.registry, old, {"ready": True, "reason": "stale overwrite", "stage_bytes": 0}, owner=SERVER_OWNER)
        self.assertEqual("first owner check", records(self.registry)[0]["request"]["readiness"]["reason"])

    def test_concurrent_readiness_observations_have_one_cas_winner(self):
        self.add(ready=False)
        old = records(self.registry)[0]
        def attempt(number):
            try:
                return advance_readiness(self.registry, old, {"ready": True, "reason": f"owner {number}", "stage_bytes": 0}, owner=SERVER_OWNER)["state"]
            except ValueError:
                return "stale"
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(attempt, (1, 2)))
        self.assertEqual(1, results.count("ready"))
        self.assertEqual(1, results.count("stale"))
        self.assertEqual(1, records(self.registry)[0]["request"]["generation"])

    def test_owner_approval_does_not_derive_from_all_registered_objects(self):
        self.add()
        self.assertEqual(set(), load_allowed_objects(self.registry))
        from preservation_registry import atomic_json
        atomic_json(self.registry / "approved-objects.json",
                    {"schema_version": 1, "owner": SERVER_OWNER, "approval_scope": {"ticket": 410},
                     "object_ids": list(self.allowed)})
        self.assertEqual(self.allowed, load_allowed_objects(self.registry))

    def test_queued_receipt_pointer_tampering_is_rejected(self):
        request, _ = self.add()
        self.adapter().prepare(time.monotonic() + 300)
        pointer = self.registry / "owner-jobs" / (request["source"]["sha256"] + ".json")
        value = json.loads(pointer.read_text())
        value["event"] = "../../another.json"
        pointer.write_text(json.dumps(value), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "escapes"):
            export_records(self.registry)


if __name__ == "__main__":
    unittest.main()
