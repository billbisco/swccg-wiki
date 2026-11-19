"""Native maintenance never becomes a second saver or an HTML approximation."""
import copy
import hashlib
import io
import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "ops"), str(ROOT / "tools"), str(ROOT / "tests")]
from test_preservation_native import XML, source_for
from test_preservation_registration import fixture
from preservation_registry import register, export_records, SERVER_OWNER
from preservation_owner import OwnerAdapter
from preservation_suppression import suppress_objects
from preservation_stage_native import stage_native_objects
import wayback_worker as W


class NativeStagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.registry = self.root / "control" / "registry"
        self.payload = XML
        self.request = fixture(ready=False)
        source = source_for(self.payload)
        subject = {"kind": "source_snapshot", "title": source["primary_url"],
                   "original_version_url": source["primary_url"],
                   "content_sha256": source["sha256"], "bytes": len(self.payload)}
        self.request.update(subject=subject, source=source)
        self.request["backup_receipt"]["subject"] = copy.deepcopy(subject)
        self.request["backup_receipt"]["verification"].update(
            restored_sha256=source["sha256"], restored_bytes=len(self.payload))
        self.registered = register(self.registry, self.request)
        self.allowed = {self.registered["object_id"]}
        self.lock = io.BytesIO(b"existing actual owner fixture")
        self.addCleanup(self.lock.close)
        self.control = SimpleNamespace(directory=self.root / "control", lock=self.lock,
                                       state={"mode": "open", "next_attempt": 9999999999}, done={})
        self.calls, self.restores, self.commits = [], [], []
        self.public = self.root / "public"
        self.status, self.ctype, self.override_body = 200, "text/plain", None
        def raw_get(url, limit):
            self.calls.append(url)
            self.assertEqual(source["url"], url)
            body = self.override_body if self.override_body is not None else self.payload
            return self.status, {"Content-Type": self.ctype}, body[:limit]
        def commit(*args):
            self.commits.append(args)
        self.worker = SimpleNamespace(ACTIVE_CONTROL=self.control, _raw_get=raw_get,
            snapshot_root=lambda: self.public, QUEUE="queue.txt", commit_and_push=commit,
            snapshot_file=lambda url: self.public / url.split("/snapshots/", 1)[1])
        self.restore_result = copy.deepcopy(self.request["backup_receipt"])
        def readback(subject, storage, *, restore_to):
            self.restores.append(subject)
            restore_to.write_bytes(self.payload)
            return copy.deepcopy(self.restore_result)
        self.readback = readback

    def adapter(self, **kw):
        return OwnerAdapter(self.worker, self.root, self.control, self.allowed,
                            work=self.root / "private", readback=self.readback, **kw)

    def test_stage_only_preserves_provider_pause_and_never_queues(self):
        for mode in ("open", "half_open", "auth_blocked", "probe_blocked"):
            self.control.state["mode"] = mode
            before = copy.deepcopy(self.control.state)
            result = self.adapter().stage_native_only(time.monotonic() + 300)
            self.assertEqual(1, result["staged"])
            self.assertEqual(0, result["capture_submissions"])
            self.assertEqual(0, result["queue_appends"])
            self.assertEqual(before, self.control.state)
            self.assertTrue(result["results"][0]["public_readback"]["matches"])
        self.assertEqual(1, len(self.restores))
        self.assertEqual([], self.commits)
        row = export_records(self.registry, object_ids=self.allowed)["objects"][0]
        self.assertEqual("ready", row["state"])
        self.assertFalse(row["submitted"])
        self.assertEqual(self.payload, self.worker.snapshot_file(row["source"]["url"]).read_bytes())

    def test_default_prepare_still_does_nothing_while_paused(self):
        self.assertEqual(0, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([], self.restores)
        self.assertEqual([], self.calls)

    def test_native_restore_requires_real_receipt_and_cleans_private_copy(self):
        self.restore_result = None
        with self.assertRaisesRegex(ValueError, "independent restore receipt"):
            self.adapter().stage_native_only(time.monotonic() + 300)
        self.assertFalse(self.worker.snapshot_file(self.request["source"]["url"]).exists())
        self.assertFalse(any((self.root / "private").glob("*.restored")))

    def test_public_wrong_bytes_html_mime_or_redirect_cannot_advance(self):
        for status, ctype, body in ((200, "text/plain", b"different"),
                                    (200, "text/html", self.payload),
                                    (302, "text/plain", b"")):
            self.status, self.ctype, self.override_body = status, ctype, body
            result = self.adapter().stage_native_only(time.monotonic() + 300)
            self.assertEqual(0, result["staged"])
            self.assertFalse(result["results"][0]["public_readback"]["redirects_followed"])
            self.assertEqual("awaiting_stage", export_records(self.registry, object_ids=self.allowed)["objects"][0]["state"])
        self.assertEqual([], self.commits)

    def test_budget_and_fifty_GiB_floor_precede_private_restore(self):
        self.assertEqual(0, self.adapter(stage_budget=1).stage_native_only(time.monotonic() + 300)["staged"])
        with patch("preservation_owner.shutil.disk_usage", return_value=SimpleNamespace(free=49 * 1024 ** 3)):
            self.assertEqual(0, self.adapter().stage_native_only(time.monotonic() + 300)["staged"])
        self.assertEqual([], self.restores)

    def test_maintenance_rejects_non_native_cohort_before_restore(self):
        old = fixture(ready=False)
        r = register(self.registry, old)
        self.allowed = {r["object_id"]}
        with self.assertRaisesRegex(ValueError, "another representation"):
            self.adapter().stage_native_only(time.monotonic() + 300)
        self.assertEqual([], self.restores)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO fixture requires POSIX")
    def test_existing_fifo_is_rejected_before_generic_payload_hash_read(self):
        target = self.worker.snapshot_file(self.request["source"]["url"])
        target.parent.mkdir(parents=True)
        os.mkfifo(target)
        with patch("preservation_owner.payload_hashes", side_effect=AssertionError("FIFO generic read must never run")):
            with self.assertRaises(ValueError):
                self.adapter().stage_native_only(time.monotonic() + 300)
        self.assertEqual([], self.restores)
        self.assertEqual([], self.calls)

    def test_existing_or_broken_native_symlink_is_rejected_before_hashing(self):
        target = self.worker.snapshot_file(self.request["source"]["url"])
        target.parent.mkdir(parents=True)
        other = target.parent / "other.txt"
        for existing in (False, True):
            if existing:
                other.write_bytes(self.payload)
            try:
                target.symlink_to(other)
            except OSError as error:
                if os.name == "nt" and getattr(error, "winerror", None) == 1314:
                    self.skipTest("Windows runner cannot create symlink fixtures")
                raise
            with patch("preservation_owner.payload_hashes", side_effect=AssertionError("symlink generic read must never run")):
                with self.assertRaisesRegex(ValueError, "symlink"):
                    self.adapter().stage_native_only(time.monotonic() + 300)
            target.unlink()
        self.assertEqual([], self.restores)
        self.assertEqual([], self.calls)

    def test_withdrawn_native_cannot_be_staged(self):
        suppress_objects(self.registry, self.allowed, owner=SERVER_OWNER,
                         reason="explicit fixture withdrawal", approval_scope={"ticket": 994})
        self.assertEqual(0, self.adapter().stage_native_only(time.monotonic() + 300)["staged"])
        self.assertEqual([], self.restores)

    def allowance(self, adapter):
        inventory = adapter._stage_inventory()
        source = self.request["source"]
        return {"schema_version": 1, "approval_scope": {"ticket": 994, "explicit_one_shot": True},
                "legacy_baseline": {key: inventory[key] for key in ("files", "bytes")},
                "new_bytes_limit": source["bytes"],
                "objects": {self.registered["object_id"]: {"sha256": source["sha256"],
                    "bytes": source["bytes"], "url": source["url"]}}}

    def test_legacy_over_budget_still_blocks_normal_prepare_but_exact_allowance_works(self):
        self.public.mkdir()
        legacy = self.public / "legacy.html"
        with legacy.open("wb") as stream:
            stream.truncate(32 * 1024 ** 2 + 1)
        original = legacy.stat()
        self.control.state["mode"] = "healthy"
        adapter = self.adapter()
        self.assertEqual(0, adapter.prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([], self.restores)
        self.control.state["mode"] = "open"
        result = adapter.stage_native_only(time.monotonic() + 300,
                                           maintenance_allowance=self.allowance(adapter))
        self.assertEqual(1, result["staged"])
        self.assertEqual(len(self.payload), result["new_stage_bytes"])
        self.assertEqual(32 * 1024 ** 2, result["global_stage_budget"])
        self.assertTrue(result["preexisting_staging_metadata_unchanged"])
        self.assertEqual(original.st_mtime_ns, legacy.stat().st_mtime_ns)
        self.assertEqual([], self.commits)

    def test_allowance_rejects_extra_object_overcap_or_wrong_baseline_before_writes(self):
        adapter = self.adapter()
        good = self.allowance(adapter)
        for key, value in (("new_bytes_limit", len(self.payload) + 1),
                           ("new_bytes_limit", 33 * 1024 ** 2),
                           ("legacy_baseline", {"files": 1, "bytes": 999}),
                           ("objects", {**good["objects"], "f" * 64: next(iter(good["objects"].values()))})):
            bad = copy.deepcopy(good)
            bad[key] = value
            with self.subTest(key=key, value=value):
                with self.assertRaisesRegex(ValueError, "exact frozen"):
                    adapter.stage_native_only(time.monotonic() + 300, maintenance_allowance=bad)
        self.assertEqual([], self.restores)
        self.assertFalse(self.public.exists())

    def test_native_xml_replay_requires_exact_hash_and_length(self):
        url = self.request["source"]["url"]
        capture = "https://web.archive.org/web/20261119000000/" + url
        def response(raw):
            return {"status": 200, "ctype": "application/xml", "body": raw,
                    "sha256": hashlib.sha256(raw).hexdigest(), "size": len(raw)}
        source = response(self.payload)
        changed = response(self.payload.replace(b' title=', b'  title='))
        with patch.object(W, "strict_check", return_value=(True, "ok")):
            status, info = W.verify(url, capture, get=lambda u: source if u == url else changed)
            self.assertEqual("unverified", status)
            self.assertEqual("sha256", info["method"])
            wrong_length = dict(source, size=source["size"] + 1)
            self.assertEqual("unverified", W.verify(url, capture, get=lambda u: source if u == url else wrong_length)[0])

    def test_operator_maintenance_uses_real_existing_lock_without_control_write(self):
        root = self.registry.parent
        state = {"schema": 1, "mode": "open", "failure_count": 2,
                 "next_attempt": 9999999999, "probe_url": None}
        (root / "control.json").write_text(json.dumps(state))
        (self.registry / "approved-objects.json").write_text(json.dumps(
            {"schema_version": 1, "owner": SERVER_OWNER, "approval_scope": {"ticket": 994},
             "object_ids": sorted(self.allowed)}))
        before = (root / "control.json").read_bytes()
        test = self
        class Adapter:
            def __init__(self, worker, repository, control, object_ids, **kw):
                test.assertIs(worker.ACTIVE_CONTROL, control)
                test.assertFalse(control.lock.closed)
                test.assertEqual(test.allowed, object_ids)
            def stage_native_only(self, deadline):
                return {"staged": 1, "capture_submissions": 0, "queue_appends": 0}
        with patch.object(W, "control_directory", return_value=root), \
                patch.object(W, "ACTIVE_CONTROL", None), \
                patch("preservation_stage_native.OwnerAdapter", Adapter):
            result = stage_native_objects(self.root, self.allowed)
            self.assertEqual(1, result["staged"])
            self.assertIsNone(W.ACTIVE_CONTROL)
        self.assertEqual(before, (root / "control.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
