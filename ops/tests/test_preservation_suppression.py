"""Withdrawn bytes cannot be restaged or submitted; unrelated jobs remain usable."""
import copy
import hashlib
import io
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "ops"), str(ROOT / "tools"), str(ROOT / "tests")]
from test_preservation_registration import fixture
from preservation_registry import SERVER_OWNER, export_records, register
from preservation_suppression import suppress_objects, suppressed_source, suppressed_url
from preservation_owner import OwnerAdapter
import wayback_worker as worker


class SuppressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.registry = self.root / "control" / "registry"

    def add(self, title="File:withdrawn.jpg", url=None, payload=None):
        q = fixture(title=title)
        if url:
            q["subject"]["original_version_url"] = url
            q["source"]["url"] = url
        if payload:
            digest = hashlib.sha256(payload).hexdigest()
            q["subject"].update(content_sha256=digest, bytes=len(payload))
            q["source"].update(sha256=digest, bytes=len(payload))
            q["backup_receipt"]["verification"].update(restored_sha256=digest,
                                                       restored_bytes=len(payload))
        q["backup_receipt"]["subject"] = copy.deepcopy(q["subject"])
        receipt = register(self.registry, q)
        return q, receipt

    def suppress(self, ids):
        return suppress_objects(self.registry, set(ids), owner=SERVER_OWNER,
                                reason="User explicitly withdrew these exact bytes",
                                approval_scope={"ticket": 994, "exact_scope_checked": True})

    def test_two_objects_share_one_cancelled_payload_without_deleting_requests(self):
        a, ar = self.add()
        b, br = self.add(title="File:second-version.jpg",
                         url="https://wiki.swccg.com/images/exact-other-copy.jpg")
        result = self.suppress([ar["object_id"], br["object_id"]])
        self.assertEqual(1, len(result["payloads"]))
        self.assertEqual(0, result["capture_submissions"])
        self.assertEqual(2, len(list((self.registry / "requests").rglob("*.json"))))
        rows = export_records(self.registry, object_ids={ar["object_id"], br["object_id"]})["objects"]
        self.assertEqual({"cancelled"}, {x["state"] for x in rows})
        self.assertFalse(any(x["submitted"] for x in rows))
        for q in (a, b):
            self.assertIsNotNone(suppressed_source(self.registry, q["source"]))
            self.assertIsNotNone(suppressed_url(self.registry, q["source"]["url"]))
        self.assertEqual(result, self.suppress([ar["object_id"], br["object_id"]]))

    def test_exact_scope_does_not_cancel_another_payload_or_url(self):
        a, ar = self.add()
        b, br = self.add(title="File:approved.jpg", url="https://wiki.swccg.com/images/approved.jpg",
                         payload=b"different approved native bytes")
        self.suppress([ar["object_id"]])
        self.assertIsNone(suppressed_source(self.registry, b["source"]))
        self.assertIsNone(suppressed_url(self.registry, b["source"]["url"]))
        row = export_records(self.registry, object_ids={br["object_id"]})["objects"][0]
        self.assertEqual("ready", row["state"])
        self.assertEqual(a["source"]["url"], a["subject"]["original_version_url"])

    def test_invalid_identity_or_missing_approval_writes_nothing(self):
        _, ar = self.add()
        with self.assertRaises(PermissionError):
            suppress_objects(self.registry, {ar["object_id"]}, owner="client",
                             reason="not allowed", approval_scope={"ticket": 994})
        with self.assertRaises(ValueError):
            self.suppress({"a" * 64})
        self.assertFalse((self.registry / "suppressed-payloads").exists())

    def test_owner_will_not_restore_fetch_or_queue_suppressed_payload(self):
        q, ar = self.add()
        self.suppress([ar["object_id"]])
        lock = io.BytesIO(b"owner test lock")
        self.addCleanup(lock.close)
        control = SimpleNamespace(directory=self.root / "control", state={"mode": "healthy"},
                                  lock=lock, done={})
        w = SimpleNamespace(ACTIVE_CONTROL=control, snapshot_root=lambda: self.root / "public")
        adapter = OwnerAdapter(w, self.root, control, {ar["object_id"]},
                               work=self.root / "work",
                               readback=lambda *a, **k: self.fail("withdrawn payload restore"))
        self.assertEqual(0, adapter.prepare(time.monotonic() + 300)["prepared"])
        self.assertFalse(adapter._check_public(q["source"]))
        with self.assertRaises(PermissionError):
            adapter._enqueue(q["source"]["url"])

    def test_last_submission_guard_blocks_existing_legacy_queue_url(self):
        q, ar = self.add()
        self.suppress([ar["object_id"]])
        control = SimpleNamespace(directory=self.root / "control")
        with patch.object(worker, "ACTIVE_CONTROL", control), \
                patch.object(worker, "spn2_submit") as submit, \
                patch.object(worker, "save_anon") as anon:
            with self.assertRaises(PermissionError):
                worker.submit_capture(q["source"]["url"], None, {"authenticated": True})
            submit.assert_not_called()
            anon.assert_not_called()

    def test_corrupt_url_pointer_fails_closed_without_guessing_another_payload(self):
        q, ar = self.add()
        self.suppress([ar["object_id"]])
        key = hashlib.sha256(q["source"]["url"].encode()).hexdigest()
        pointer = self.registry / "suppressed-urls" / (key + ".json")
        pointer.write_text(json.dumps({"url": "https://example.org/unrelated", "payload_sha256": "a" * 64}))
        with self.assertRaises(ValueError):
            suppressed_url(self.registry, q["source"]["url"])
