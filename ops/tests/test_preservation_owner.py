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
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
from test_preservation_registration import fixture
import test_preservation_registration as contract_fixtures
from preservation_contracts import registration_object_id, source_backup_subject
from preservation_registry import (register, records, export_records, advance_readiness, SERVER_OWNER)
from preservation_owner import OwnerAdapter, load_allowed_objects
from preservation_owner_receipts import load_event, store_event
from wayback_control import Paused


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
                                      strict_check=lambda url: (True, "ok"), VERIFY_GAP_S=0)
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

    def test_provider_pause_during_prepare_propagates_without_more_work(self):
        request, _ = self.add()
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.control.done[request["source"]["url"]] = {"status": "verified", "capture": capture}
        def pause(url):
            self.control.state["mode"] = "open"
            raise Paused("fixture provider cooldown")
        self.worker.strict_check = pause
        with self.assertRaises(Paused):
            self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual([], self.commits)
        self.assertIsNone(load_event(self.registry, request["source"]))

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

    def test_approved_client_continuation_owner_uses_the_same_capture_owner(self):
        request = fixture(title="File:approved-client.png")
        request["owner"] = "MemoryCoreChatGPT / Story309 continuation"
        registered = register(self.registry, request)
        self.allowed.add(registered["object_id"])
        self.responses[request["source"]["url"]] = {"status": 200, "sha256": request["source"]["sha256"], "size": request["source"]["bytes"]}
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(1, result["prepared"])
        self.assertEqual(1, len(self.commits))
        self.assertEqual(request["owner"], records(self.registry)[0]["request"]["owner"])
        self.assertIs(self.control, self.worker.ACTIVE_CONTROL)

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

    def test_stage_budget_ignores_preexisting_snapshot_tree_when_batch_fits(self):
        stage = self.worker.snapshot_root()
        stage.mkdir(parents=True, exist_ok=True)
        legacy = stage / "legacy.html"
        with legacy.open("wb") as stream:
            stream.truncate(32 * 1024 ** 2 + 1)
        original = legacy.stat()
        request, _ = self.add(ready=False, snapshot=True)
        def restore(subject, storage, *, restore_to):
            restore_to.write_bytes(self.payload)
        result = self.adapter(readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(1, result["prepared"])
        self.assertEqual(original.st_mtime_ns, legacy.stat().st_mtime_ns)
        self.assertEqual(self.payload, self.worker.snapshot_file(request["source"]["url"]).read_bytes())

    def test_stage_budget_caps_cumulative_bytes_in_one_batch(self):
        r1, _ = self.add(title="File:batch-one.png", ready=False, snapshot=True)
        payload2 = b"second exact snapshot byte"
        sha2 = hashlib.sha256(payload2).hexdigest()
        r2_req = fixture(title="File:batch-two.png", ready=False)
        r2_req["owner"] = SERVER_OWNER
        s2 = copy.deepcopy(r1["source"])
        s2["url"] = "https://swccg.com/snapshots/pc/batch-two.html"
        s2["primary_url"] = "https://www.starwarsccg.org/batch-two/"
        s2["sha256"] = sha2
        s2["bytes"] = len(payload2)
        s2["provenance_equivalence"]["primary_url"] = s2["primary_url"]
        s2["provenance_equivalence"]["snapshot_url"] = s2["url"]
        s2["provenance_equivalence"]["snapshot_html_sha256"] = sha2
        r2_req["source"] = s2
        b2 = copy.deepcopy(r1["source_backup_receipt"])
        b2["subject"] = source_backup_subject(s2)
        b2["verification"]["restored_sha256"] = sha2
        b2["verification"]["restored_bytes"] = len(payload2)
        r2_req["source_backup_receipt"] = b2
        res2 = register(self.registry, r2_req)
        self.allowed.add(res2["object_id"])
        self.responses[s2["url"]] = {"status": 200, "sha256": sha2, "size": len(payload2)}
        restores = []
        payloads = {r1["source"]["sha256"]: self.payload, sha2: payload2}
        def restore(subject, storage, *, restore_to):
            restores.append(subject)
            restore_to.write_bytes(payloads[subject["content_sha256"]])
        budget = len(self.payload) + 10
        first = self.adapter(stage_budget=budget, limit=2, readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(1, first["prepared"])
        self.assertEqual(1, len(restores))
        second = self.adapter(stage_budget=budget, limit=2, readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(1, second["prepared"])
        self.assertEqual(2, len(restores))

    def test_only_approved_snapshot_targets_are_protected_from_legacy_cleanup(self):
        approved, _ = self.add(ready=False, snapshot=True)
        self.add(title="File:original.png")
        unknown = fixture(title="File:unapproved-snapshot.png", ready=False)
        unknown["source"] = dict(approved["source"], url="https://swccg.com/snapshots/pc/unknown.html")
        unknown["source_backup_receipt"] = dict(approved["source_backup_receipt"])
        unknown["source_backup_receipt"]["subject"] = source_backup_subject(unknown["source"])
        register(self.registry, unknown)
        self.assertEqual({approved["source"]["url"]}, self.adapter().protected_snapshot_urls())

    def test_default_work_refuses_unmounted_volume_before_restore(self):
        self.add(ready=False, snapshot=True)
        adapter = OwnerAdapter(self.worker, self.repo, self.control, self.allowed,
                               readback=lambda *a, **k: self.fail("unmounted restore"))
        with patch("preservation_owner.os.path.ismount", return_value=False):
            result = adapter.prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertIn("refusing root-disk fallback", result["observations"][0]["reason"])
        self.assertEqual([], self.commits)

    def test_private_restore_is_removed_when_provider_pauses(self):
        request, _ = self.add(ready=False, snapshot=True)
        def restore(subject, storage, *, restore_to):
            restore_to.write_bytes(self.payload)
            self.control.state["mode"] = "auth_blocked"
        result = self.adapter(readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertFalse((self.root / "work" / (request["source"]["sha256"] + ".restored")).exists())
        self.assertFalse(self.worker.snapshot_file(request["source"]["url"]).exists())

    def test_private_restore_is_removed_when_deadline_expires(self):
        request, _ = self.add(ready=False, snapshot=True)
        late = [False]
        def restore(subject, storage, *, restore_to):
            restore_to.write_bytes(self.payload)
            late[0] = True
        with patch("preservation_owner.time.monotonic", side_effect=lambda: 950 if late[0] else 0):
            result = self.adapter(readback=restore).prepare(1000)
        self.assertEqual(0, result["prepared"])
        self.assertFalse((self.root / "work" / (request["source"]["sha256"] + ".restored")).exists())
        self.assertFalse(self.worker.snapshot_file(request["source"]["url"]).exists())

    def test_failed_readback_removes_partial_private_restore(self):
        request, _ = self.add(ready=False, snapshot=True)
        def restore(subject, storage, *, restore_to):
            restore_to.write_bytes(b"incomplete")
            raise ValueError("injected independent restore failure")
        result = self.adapter(readback=restore).prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertFalse((self.root / "work" / (request["source"]["sha256"] + ".restored")).exists())
        self.assertEqual([], self.commits)

    def test_public_payload_mismatch_is_durable_and_never_queued(self):
        request, _ = self.add()
        self.responses[request["source"]["url"]]["sha256"] = "0" * 64
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(0, result["prepared"])
        self.assertEqual([], self.commits)
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])

    def test_missing_checked_evidence_cannot_be_promoted_by_public_bytes_alone(self):
        request = fixture(title="File:missing-evidence.png", ready=False)
        request["source"].pop("checked_evidence")
        registered = register(self.registry, request)
        self.allowed.add(registered["object_id"])
        self.responses[request["source"]["url"]] = {"status": 200, "sha256": request["source"]["sha256"], "size": request["source"]["bytes"]}
        self.assertEqual(0, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([], self.commits)
        self.assertEqual("needs_attention", export_records(self.registry)["objects"][0]["state"])

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

    def queued_epoch(self):
        request, _ = self.add()
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.responses[self.worker.id_url(capture)] = {"status": 200, "sha256": "0" * 64, "size": len(self.payload)}
        previous = {"status": "verified", "capture": capture}
        self.control.done[request["source"]["url"]] = previous.copy()
        delta = self.adapter().prepare(time.monotonic() + 300)["ledger_updates"]
        return request, previous, delta

    def test_restart_replays_queued_version_delta_before_worker_checkpoint(self):
        request, previous, expected = self.queued_epoch()
        # Simulate process death after durable owner event, before returning or
        # checkpointing the delta into the worker's URL ledger.
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(expected, result["ledger_updates"])
        self.assertEqual(previous, self.control.done[request["source"]["url"]])
        self.assertTrue(result["ledger_updates"][request["source"]["url"]]["recapture"])
        self.assertEqual([request["source"]["url"]], (self.repo / self.worker.QUEUE).read_text().splitlines())

    def test_queued_epoch_does_not_reset_an_accepted_job_after_restart(self):
        request, _, _ = self.queued_epoch()
        accepted = {"status": "pending", "job_id": "actually-accepted", "tries": 3}
        self.control.done[request["source"]["url"]] = accepted.copy()
        self.assertEqual({}, self.adapter().prepare(time.monotonic() + 300)["ledger_updates"])
        self.assertEqual(accepted, self.control.done[request["source"]["url"]])

    def test_queued_epoch_does_not_reset_already_applied_retry_budget(self):
        request, _, delta = self.queued_epoch()
        applied = dict(delta[request["source"]["url"]], tries=3)
        self.control.done[request["source"]["url"]] = applied.copy()
        self.assertEqual({}, self.adapter().prepare(time.monotonic() + 300)["ledger_updates"])
        self.assertEqual(applied, self.control.done[request["source"]["url"]])

    def test_replayed_epoch_rechecks_public_payload_before_replacing_old_ledger(self):
        request, previous, _ = self.queued_epoch()
        self.responses[request["source"]["url"]]["sha256"] = "1" * 64
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual({}, result["ledger_updates"])
        self.assertEqual(previous, self.control.done[request["source"]["url"]])
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])

    def test_applied_epoch_with_wrong_capture_becomes_owned_repair_not_retry_reset(self):
        request, previous, delta = self.queued_epoch()
        applied = dict(delta[request["source"]["url"]], status="verified", capture=previous["capture"], tries=3, job_id="accepted-epoch-job")
        self.control.done[request["source"]["url"]] = applied.copy()
        self.adapter().finish(time.monotonic() + 300)
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])
        exported = export_records(self.registry)["objects"][0]
        self.assertTrue(exported["submitted"])
        self.assertEqual("accepted-epoch-job", exported["owner_job_receipt"]["accepted_job_id"])
        self.assertEqual({}, self.adapter().prepare(time.monotonic() + 300)["ledger_updates"])
        self.assertEqual(applied, self.control.done[request["source"]["url"]])

    def test_new_queue_recent_old_capture_gets_one_checked_version_epoch(self):
        request, _ = self.add()
        self.adapter().prepare(time.monotonic() + 300)
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.responses[self.worker.id_url(capture)] = {"status": 200, "sha256": "0" * 64, "size": len(self.payload)}
        previous = {"status": "verified", "capture": capture, "tries": 1}
        self.control.done[request["source"]["url"]] = previous.copy()
        self.adapter().finish(time.monotonic() + 300)
        self.assertEqual("capture_check_pending", load_event(self.registry, request["source"])["state"])
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertTrue(result["ledger_updates"][request["source"]["url"]]["recapture"])
        self.assertEqual(previous, self.control.done[request["source"]["url"]])

    def test_corrupt_unapproved_record_does_not_block_the_approved_cohort(self):
        self.add()
        unknown = fixture(title="File:other-client.png")
        result = register(self.registry, unknown)
        path = self.registry / result["record"]
        path.write_bytes(b"broken unrelated metadata")
        self.assertEqual(1, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual(set(), self.adapter().protected_snapshot_urls())
        self.assertEqual(b"broken unrelated metadata", path.read_bytes())

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


    # --- #1375: batched queue appends and separate promotion / finish limits ---
    def add_distinct(self, i):
        payload = b"distinct exact payload %d" % i
        sha = hashlib.sha256(payload).hexdigest()
        request = fixture(title=f"File:p{i}.png")
        request["owner"] = SERVER_OWNER
        url = f"https://wiki.swccg.com/images/p{i}.png"
        for subject in (request["subject"], request["backup_receipt"]["subject"]):
            subject.update(original_version_url=url, content_sha256=sha, bytes=len(payload))
        request["backup_receipt"]["storage"]["path"] = "preservation/objects/" + sha + ".bin"
        request["backup_receipt"]["verification"].update(restored_sha256=sha, restored_bytes=len(payload))
        request["source"].update(url=url, sha256=sha, bytes=len(payload))
        request["readiness"]["stage_bytes"] = len(payload)
        result = register(self.registry, request)
        self.allowed.add(result["object_id"])
        self.responses[url] = {"status": 200, "sha256": sha, "size": len(payload)}
        return request

    def test_batched_enqueue_makes_one_push_for_many_urls_and_keeps_order(self):
        requests = [self.add_distinct(i) for i in range(5)]
        queue = self.repo / self.worker.QUEUE
        queue.parent.mkdir(parents=True)
        queue.write_text("https://example.org/older\n" + requests[2]["source"]["url"] + "\n", encoding="utf-8")
        result = self.adapter(limit=10).prepare(time.monotonic() + 300)
        self.assertEqual(5, result["prepared"])
        self.assertEqual(1, len(self.commits))
        lines = queue.read_text().splitlines()
        self.assertEqual(["https://example.org/older", requests[2]["source"]["url"]], lines[:2])
        self.assertEqual(6, len(lines))
        self.assertEqual(len(lines), len(set(lines)))
        self.assertEqual(sorted(r["source"]["url"] for r in requests), sorted(lines[1:]))
        for request in requests:
            self.assertEqual("queued", load_event(self.registry, request["source"])["state"])

    def test_failed_batch_push_stores_no_queued_events_and_rewinds_cursor(self):
        requests = [self.add_distinct(i) for i in range(3)]
        def reject(repo, paths, message, redo):
            redo()
            raise RuntimeError("push rejected")
        self.worker.commit_and_push = reject
        with patch("builtins.print"), self.assertRaisesRegex(RuntimeError, "push rejected"):
            self.adapter(limit=10).prepare(time.monotonic() + 300)
        for request in requests:
            self.assertIsNone(load_event(self.registry, request["source"]))
        cursor = json.loads((self.registry / "owner-prepare-cursor.json").read_text())
        self.assertEqual("", cursor["after"])
        # Next run with a working push queues all of them.
        self.worker.commit_and_push = lambda repo, paths, message, redo: self.commits.append(redo())
        self.assertEqual(3, self.adapter(limit=10).prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual(1, len(self.commits))

    def test_promotion_limit_and_time_budget_bound_prepare(self):
        for i in range(5):
            self.add_distinct(i)
        self.assertEqual(2, self.adapter(limit=2).prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual(1, len(self.commits))
        self.assertEqual(0, self.adapter(limit=10, prepare_seconds=-1).prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual(0, self.adapter(limit=0).prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual(1, len(self.commits))

    def test_finish_uses_its_own_limit(self):
        for i in range(4):
            request = self.add_distinct(i)
            url = request["source"]["url"]
            self.control.done[url] = {"status": "ok", "capture": "https://web.archive.org/web/20261114000000/" + url}
        self.assertEqual(1, self.adapter(limit=0, finish_limit=1).finish(time.monotonic() + 300))
        self.assertEqual(3, self.adapter(limit=200, finish_limit=3).finish(time.monotonic() + 300))
        self.assertEqual(2, self.adapter(limit=2).finish(time.monotonic() + 300))

    # --- #1375 review: archive.org observations share a paced per-run budget ---
    def captured(self, i):
        request = self.add_distinct(i)
        url = request["source"]["url"]
        self.control.done[url] = {"status": "ok", "capture": "https://web.archive.org/web/20261114000000/" + url}
        return request

    def count_checks(self):
        checks = []
        self.worker.strict_check = lambda url: checks.append(url) or (True, "ok")
        return checks

    def test_observation_budget_bounds_prepare_and_finish_while_fresh_jobs_fill_the_cap(self):
        for i in range(12):
            self.captured(i)
        fresh = [self.add_distinct(100 + i) for i in range(5)]
        checks = self.count_checks()
        adapter = self.adapter(limit=5, finish_limit=6, observe_max=3)
        result = adapter.prepare(time.monotonic() + 300)
        self.assertEqual(3, len(checks))
        self.assertEqual(3, result["archive_observations"])
        self.assertGreater(result["observe_skipped"], 0)
        # Every fresh, never-captured job was still promoted (cap 5).
        self.assertEqual(5, result["prepared"])
        for request in fresh:
            self.assertEqual("queued", load_event(self.registry, request["source"])["state"])
        # finish() shares the spent budget: no archive.org request at all.
        self.assertEqual(0, adapter.finish(time.monotonic() + 300))
        self.assertEqual(3, len(checks))

    def test_finish_uses_what_prepare_left(self):
        for i in range(6):
            self.captured(i)
        checks = self.count_checks()
        adapter = self.adapter(limit=0, finish_limit=6, observe_max=4)
        adapter.prepare(time.monotonic() + 300)
        self.assertEqual(4, adapter.finish(time.monotonic() + 300))
        self.assertEqual(4, len(checks))

    def test_observations_keep_the_verify_gap(self):
        for i in range(3):
            self.captured(i)
        self.count_checks()
        self.worker.VERIFY_GAP_S = 4
        sleeps = []
        with patch("preservation_owner.time.sleep", side_effect=sleeps.append):
            self.adapter(limit=0, finish_limit=3, observe_max=10).finish(time.monotonic() + 300)
        self.assertEqual(2, len(sleeps))
        self.assertTrue(all(3.9 < s <= 4 for s in sleeps), sleeps)

    def test_default_observation_budget_comes_from_env(self):
        with patch.dict("os.environ", {"WAYBACK_OWNER_OBSERVE_MAX": "2"}):
            self.assertEqual(2, self.adapter().observe_left)
        with patch.dict("os.environ", {"WAYBACK_OWNER_OBSERVE_MAX": ""}):
            self.assertEqual(10, self.adapter().observe_left)

    def test_shared_cooldown_means_no_observation(self):
        for i in range(3):
            self.captured(i)
        checks = self.count_checks()
        self.control.state["next_attempt"] = time.time() + 600
        self.adapter(limit=5, finish_limit=5, observe_max=10).prepare(time.monotonic() + 300)
        self.adapter(limit=5, finish_limit=5, observe_max=10).finish(time.monotonic() + 300)
        self.assertEqual([], checks)

    def throttle_control(self):
        waits = []
        def capacity_wait(reason, retry_after=None):
            waits.append(reason)
            raise Paused("account capacity unavailable; bounded wait")
        self.control.capacity_wait = capacity_wait
        return waits

    def test_replay_or_cdx_429_records_cooldown_and_stops_archive_calls(self):
        import wayback_worker as W
        for i in range(4):
            self.captured(i)
        waits = self.throttle_control()
        self.worker.VerifyRetry = W.VerifyRetry
        calls = []
        def throttled(url):
            calls.append(url)
            raise W.VerifyRetry("CDX HTTP 429", side="capture")
        self.worker.strict_check = throttled
        adapter = self.adapter(limit=5, finish_limit=5, observe_max=10)
        with self.assertRaises(Paused):
            adapter.prepare(time.monotonic() + 300)
        self.assertEqual(["replay_throttled"], waits)
        self.assertTrue(adapter.replay_deferred)
        # finish() makes no further archive.org request and does not raise.
        adapter.finish(time.monotonic() + 300)
        self.assertEqual(1, len(calls))

    def test_id_fetch_429_records_cooldown(self):
        for i in range(2):
            request = self.captured(i)
            url = request["source"]["url"]
            self.responses[url.replace("https://", "https://web.archive.org/web/20261114000000id_/https://", 1)] = \
                {"status": 429, "sha256": "", "size": 0}
        self.worker.id_url = lambda capture: capture.replace("/20261114000000/", "/20261114000000id_/")
        waits = self.throttle_control()
        checks = self.count_checks()
        adapter = self.adapter(limit=0, finish_limit=5, observe_max=10)
        self.assertEqual(0, adapter.finish(time.monotonic() + 300))
        self.assertEqual(["replay_throttled"], waits)
        self.assertEqual(1, len(checks))


if __name__ == "__main__":
    unittest.main()
