"""Offline safety boundaries for the existing owner's exact native cohort."""
import copy
from contextlib import ExitStack
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "ops"), str(ROOT / "tools"), str(ROOT / "tests")]
import wayback_worker as W
from test_preservation_native import XML, source_for
from test_preservation_registration import fixture
from preservation_registry import register, SERVER_OWNER
from preservation_suppression import suppress_objects, suppressed_url


class NativeCaptureScopeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.registry = self.root / "control" / "registry"
        self.control = MagicMock()
        self.control.directory = self.root / "control"
        self.control.state = {}
        self.control.restore_updates.return_value = {}
        self.control.may_submit.return_value = True
        self.control.SUBMISSION_GAP = 10
        self.requests = []
        self.ids = set()
        self.urls = set()

    def add_native(self, number=1, ready=True):
        source = source_for(XML + (b" " * number))
        source["primary_url"] = "https://forum.starwarsccg.org/download/file.php?id=" + str(number)
        source["provenance_equivalence"]["primary_url"] = source["primary_url"]
        request = fixture(ready=ready)
        subject = dict(kind="source_snapshot", title=source["primary_url"],
                       original_version_url=source["primary_url"],
                       content_sha256=source["sha256"], bytes=source["bytes"])
        request.update(subject=subject, source=source)
        receipt = request["backup_receipt"]
        receipt["subject"] = copy.deepcopy(subject)
        receipt["verification"].update(restored_sha256=source["sha256"], restored_bytes=source["bytes"])
        registered = register(self.registry, request)
        self.requests.append(request)
        self.ids.add(registered["object_id"])
        self.urls.add(source["url"])
        self.approve()
        return registered["object_id"], source["url"]

    def approve(self, keys=None):
        self.registry.mkdir(parents=True, exist_ok=True)
        (self.registry / "approved-objects.json").write_text(json.dumps(dict(
            schema_version=1, owner=SERVER_OWNER, approval_scope={"ticket": 994},
            object_ids=sorted(self.ids if keys is None else keys))), encoding="utf-8")

    def test_default_none_does_not_read_registry(self):
        with patch.object(W, "iter_records", side_effect=AssertionError("default must not read cohort")):
            self.assertIsNone(W.native_capture_scope(self.control, None))

    def test_exact_one_and_six_ready_approved_records(self):
        self.add_native()
        self.assertEqual(self.urls, W.native_capture_scope(self.control, self.ids))
        for number in range(2, 7):
            self.add_native(number)
        self.assertEqual(self.urls, W.native_capture_scope(self.control, self.ids))
        self.control.state["probe_url"] = sorted(self.urls)[0]
        self.assertEqual(self.urls, W.native_capture_scope(self.control, self.ids))

    def test_empty_seven_malformed_and_string_rejected(self):
        for keys in ([], ["a" * 64] * 0, {str(i) * 64 for i in range(7)}, ["not-an-id"], "a" * 64):
            with self.subTest(keys=keys), self.assertRaises((ValueError, PermissionError)):
                W.native_capture_scope(self.control, keys)

    def test_approval_and_actual_record_are_required(self):
        self.add_native()
        self.approve([])
        with self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, self.ids)
        missing = {"f" * 64}
        self.approve(missing)
        with self.assertRaises(ValueError):
            W.native_capture_scope(self.control, missing)

    def test_unready_and_withdrawn_records_rejected(self):
        self.add_native(ready=False)
        with self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, self.ids)
        key, _ = self.add_native(2)
        suppress_objects(self.registry, {key}, owner=SERVER_OWNER,
                         reason="fixture withdrawal", approval_scope={"ticket": 994})
        with self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, {key})

    def test_cancelled_payload_cannot_return_through_new_native_mirror_alias(self):
        source = source_for(XML + b" ")
        primary = source["primary_url"]
        old = fixture(ready=True)
        subject = dict(kind="source_snapshot", title=primary,
                       original_version_url=primary, content_sha256=source["sha256"],
                       bytes=source["bytes"])
        old.update(subject=subject, source=dict(url=primary, sha256=source["sha256"],
                   bytes=source["bytes"], checked_evidence=source["checked_evidence"]))
        old["backup_receipt"]["subject"] = copy.deepcopy(subject)
        old["backup_receipt"]["verification"].update(
            restored_sha256=source["sha256"], restored_bytes=source["bytes"])
        original = register(self.registry, old)
        suppress_objects(self.registry, {original["object_id"]}, owner=SERVER_OWNER,
                         reason="fixture exact payload withdrawal", approval_scope={"ticket": 994})
        key, mirror = self.add_native()
        self.assertNotEqual(original["object_id"], key)
        self.assertEqual(old["source"]["sha256"], self.requests[-1]["source"]["sha256"])
        self.assertTrue(self.requests[-1]["readiness"]["ready"])
        self.assertIsNotNone(suppressed_url(self.registry, primary))
        self.assertIsNone(suppressed_url(self.registry, mirror))
        before = copy.deepcopy(self.control.state)
        with self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, {key})
        manager = MagicMock()
        manager.__enter__.return_value = self.control
        with patch.object(W, "Control", return_value=manager), patch.object(W, "AUTH", "fixture-auth"), \
                patch.object(W, "_run") as runner, patch.object(W, "_json") as provider:
            with self.assertRaises(PermissionError):
                W.run(self.root, 2, native_object_ids={key})
        self.control.begin.assert_not_called()
        runner.assert_not_called()
        provider.assert_not_called()
        self.assertEqual(before, self.control.state)

    def test_ordinary_image_registration_is_not_native(self):
        result = register(self.registry, fixture())
        keys = {result["object_id"]}
        self.approve(keys)
        with self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, keys)

    def test_malformed_native_proof_and_duplicate_target_cannot_expand_scope(self):
        key, _ = self.add_native()
        broken = copy.deepcopy(self.requests[0])
        broken["source"]["provenance_equivalence"]["mirror_sha256"] = "f" * 64
        with patch.object(W, "iter_records", return_value=[{"request": broken}]), \
                self.assertRaises(PermissionError):
            W.native_capture_scope(self.control, {key})
        missing_key = "e" * 64
        self.approve({key, missing_key})
        duplicate = [{"request": self.requests[0]}, {"request": self.requests[0]}]
        with patch.object(W, "iter_records", return_value=duplicate), self.assertRaises(ValueError):
            W.native_capture_scope(self.control, {key, missing_key})

    def test_bounded_run_requires_existing_credentials_before_begin(self):
        self.add_native()
        manager = MagicMock()
        manager.__enter__.return_value = self.control
        with patch.object(W, "Control", return_value=manager), patch.object(W, "AUTH", None), \
                patch.object(W, "_run") as runner:
            with self.assertRaises(PermissionError):
                W.run(self.root, 2, native_object_ids=self.ids)
        self.control.begin.assert_not_called()
        runner.assert_not_called()

    def test_outside_accepted_probe_blocks_before_begin_or_provider(self):
        self.add_native()
        self.control.state = {"probe_url": "https://example.org/existing-accepted-probe", "probe_job_id": "fixture"}
        before = copy.deepcopy(self.control.state)
        with self.assertRaises(W.Paused):
            W.native_capture_scope(self.control, self.ids)
        manager = MagicMock()
        manager.__enter__.return_value = self.control
        with patch.object(W, "Control", return_value=manager), patch.object(W, "AUTH", "fixture-auth"), \
                patch.object(W, "_run") as runner, patch.object(W, "_json") as provider:
            W.run(self.root, 2, native_object_ids=self.ids)
        self.control.begin.assert_not_called()
        runner.assert_not_called()
        provider.assert_not_called()
        self.assertEqual(before, self.control.state)

    def test_mixed_inbox_applies_only_selected_and_retains_original(self):
        _, selected = self.add_native()
        unrelated = "https://example.org/unrelated"
        inbox = self.control.directory / "verify-inbox"
        inbox.mkdir(parents=True)
        def entry(url):
            return {"capture": "https://web.archive.org/web/20260101000000/" + url,
                    "status": "pending", "last": W.iso(W.now())}
        done = {u: entry(u) for u in (selected, unrelated)}
        original_unrelated = copy.deepcopy(done[unrelated])
        receipts = {u: dict(e, status="verified", verify={"matches": True}) for u, e in done.items()}
        mixed = inbox / "mixed.json"
        mixed.write_text(json.dumps({"schema": 1, "updates": receipts}), encoding="utf-8")
        raw = mixed.read_bytes()
        only_other = inbox / "unrelated.json"
        only_other.write_text(json.dumps({"schema": 1, "updates": {unrelated: receipts[unrelated]}}), encoding="utf-8")
        other_raw = only_other.read_bytes()
        changed = {}
        self.assertEqual(1, W.apply_verify_inbox(self.control, done, changed, allowed_urls=self.urls))
        self.assertEqual("verified", done[selected]["status"])
        self.assertEqual(original_unrelated, done[unrelated])
        self.assertEqual({selected}, set(changed))
        self.assertEqual(raw, mixed.read_bytes())
        self.assertEqual(other_raw, only_other.read_bytes())

    def exercise_run(self, bounded=True):
        for number in range(1, 7):
            self.add_native(number)
        selected = sorted(self.urls)
        outside = {"https://example.org/" + status: dict(status=status,
                   capture="https://web.archive.org/web/20260101000000/https://example.org/" + status,
                   last=W.iso(W.now()), tries=1, job_id="fixture")
                   for status in ("pending", "ok", "verified", "failed")}
        done = copy.deepcopy(outside)
        queue = selected + list(outside) + ["https://example.org/new"]
        q = self.root / W.QUEUE
        q.parent.mkdir(parents=True)
        q.write_text("\n".join(queue), encoding="utf-8")
        qraw = q.read_bytes()
        adapter = MagicMock()
        adapter.prepare.return_value = {"ledger_updates": {}}
        def submit(url, *_):
            self.assertIn(url, self.urls if bounded else set(queue))
            return {"recent": "https://web.archive.org/web/20260101000000/" + url}
        mocks = {}
        with ExitStack() as stack:
            for name, value in {"reset_to_origin": None, "apply_verify_inbox": 0,
                "reconcile_recovery_probe": None, "registry_recovered": None,
                "registry_repair": None, "try_verify": True, "confirm": False,
                "verify_entry": True, "recheck_replay_only": None,
                "prune_legacy_snapshots": None, "persist_changes": None}.items():
                mocks[name] = stack.enter_context(patch.object(W, name, return_value=value))
            stack.enter_context(patch.object(W, "load", return_value=(queue, done)))
            stack.enter_context(patch.object(W, "OwnerAdapter", return_value=adapter))
            stack.enter_context(patch.object(W, "submit_capture", side_effect=submit))
            sleep = stack.enter_context(patch.object(W.time, "sleep"))
            stack.enter_context(patch.object(W, "MAX_SUBMITS_PER_RUN", 99))
            stack.enter_context(patch.object(W, "GAP_S", 1))
            stack.enter_context(patch.object(W, "AUTH", "fixture-auth"))
            stack.enter_context(patch.object(W, "_raw_get", side_effect=AssertionError("no real GET")))
            stack.enter_context(patch.object(W, "_json", side_effect=AssertionError("no real POST")))
            W._run(self.root, 10, self.control, native_object_ids=self.ids if bounded else None)
        self.assertEqual(qraw, q.read_bytes())
        for url, entry in outside.items():
            self.assertEqual(entry, done[url])
        return mocks, sleep, done, outside

    def test_bounded_all_walks_exclude_unrelated_and_never_prune(self):
        mocks, sleep, done, outside = self.exercise_run()
        mocks["confirm"].assert_not_called()
        mocks["prune_legacy_snapshots"].assert_not_called()
        self.assertTrue(all(call.args[0] in self.urls for call in mocks["verify_entry"].call_args_list))
        rechecked = mocks["recheck_replay_only"].call_args.args[0]
        self.assertEqual(self.urls, set(rechecked))
        persisted_changes = mocks["persist_changes"].call_args.args[2]
        self.assertTrue(set(persisted_changes) <= self.urls)
        self.assertEqual(6, sum(call.args == (60,) for call in sleep.call_args_list))
        self.assertEqual(self.urls, mocks["apply_verify_inbox"].call_args.kwargs["allowed_urls"])

    def test_default_mode_retains_ordinary_walks_and_prune(self):
        mocks, sleep, done, outside = self.exercise_run(bounded=False)
        self.assertTrue(mocks["confirm"].called)
        mocks["prune_legacy_snapshots"].assert_called_once()
        self.assertIn("https://example.org/verified", mocks["recheck_replay_only"].call_args.args[0])
        self.assertIsNone(mocks["apply_verify_inbox"].call_args.kwargs["allowed_urls"])
        self.assertTrue(any(call.args == (1,) for call in sleep.call_args_list))


if __name__ == "__main__":
    unittest.main()
