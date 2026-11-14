"""Existing-owner integration only: all providers, staging and Git are offline."""
import json
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W
from wayback_control import Control, Paused

URL = "https://swccg.com/snapshots/fixture.html"
ALIAS = "http://www.swccg.com/snapshots/fixture.html?old=1"


class OwnerHook(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        (self.repo / "ops/wayback").mkdir(parents=True)
        (self.repo / W.QUEUE).write_text("")
        (self.repo / W.DONE).write_text("{}")
        self.real_prune = W.prune_verified_snapshots
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        for name in ("reset_to_origin", "recheck_replay_only", "prune_verified_snapshots"):
            self.stack.enter_context(patch.object(W, name))
        self.stack.enter_context(patch.object(W, "control_directory", return_value=self.repo / "control"))
        self.stack.enter_context(patch.object(W, "AUTH", "LOW fixture:offline"))
        self.stack.enter_context(patch.object(W.time, "sleep"))
        self.stack.enter_context(patch.object(W, "fetch", side_effect=AssertionError("provider forbidden")))
        self.stack.enter_context(patch.object(W.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")))
        self.adapter = Mock()
        self.adapter.prepare.return_value = {"ledger_updates": {}}
        self.adapter.protected_snapshot_urls.return_value = set()
        self.factory = self.stack.enter_context(patch.object(W, "OwnerAdapter", return_value=self.adapter))
        self.allowed = self.stack.enter_context(patch.object(W, "load_allowed_objects", return_value=set()))
        self.stack.enter_context(patch.object(W, "commit_and_push", side_effect=lambda r,p,m,redo: redo()))

    def test_active_owner_recovery_prepare_checkpoint_reload_then_submit(self):
        events = []
        original_checkpoint = Control.checkpoint
        def checkpoint(c, done, baseline):
            events.append("checkpoint")
            return original_checkpoint(c, done, baseline)
        self.stack.enter_context(patch.object(Control, "checkpoint", checkpoint))
        self.stack.enter_context(patch.object(W, "reconcile_recovery_probe", side_effect=lambda *a: events.append("recovery")))
        old = {"status": "failed", "last": W.iso(W.now()), "tries": 6}
        delta = {"status": "retry", "last": "2000-01-01T00:00:00Z", "tries": 0}
        (self.repo / W.DONE).write_text(json.dumps({URL: old}))
        def prepare(deadline):
            self.assertIs(W.ACTIVE_CONTROL, self.factory.call_args.args[2])
            self.assertFalse(W.ACTIVE_CONTROL.lock.closed)
            events.append("prepare")
            (self.repo / W.QUEUE).write_text(URL + "\n")
            # Mimic a shared Git reset with a conflicting old ledger on disk.
            (self.repo / W.DONE).write_text(json.dumps({URL: old}))
            return {"ledger_updates": {URL: delta}}
        self.adapter.prepare.side_effect = prepare
        def submit(url, entry, session):
            events.append("submit")
            self.assertEqual(entry, delta)
            journal = json.loads((W.ACTIVE_CONTROL.directory / "pending-updates.json").read_text())
            self.assertEqual(journal["updates"][URL], delta)
            raise Paused("offline fixture pause")
        self.stack.enter_context(patch.object(W, "submit_capture", side_effect=submit))
        W.run(self.repo, 3)
        self.assertLess(events.index("recovery"), events.index("prepare"))
        self.assertLess(events.index("prepare"), events.index("checkpoint"))
        self.assertLess(events.index("checkpoint"), events.index("submit"))
        self.adapter.finish.assert_called_once()

    def test_prepare_error_keeps_legacy_accepted_job_and_finish_but_skips_pruning(self):
        self.adapter.prepare.side_effect = ValueError("private bad metadata")
        (self.repo / W.QUEUE).write_text(URL + "\n")
        self.stack.enter_context(patch.object(W, "submit_capture", return_value={"job_id": "legacy-accepted"}))
        self.stack.enter_context(patch.object(W, "confirm", return_value=False))
        # End polling after one check without pausing the whole run.
        def confirm(url, entry):
            entry["status"] = "failed"
            return True
        self.stack.enter_context(patch.object(W, "confirm", side_effect=confirm))
        def finish(deadline):
            self.assertEqual(W.ACTIVE_CONTROL.done[URL]["job_id"], "legacy-accepted")
            self.assertFalse(W.ACTIVE_CONTROL.lock.closed)
        self.adapter.finish.side_effect = finish
        W.run(self.repo, 3)
        self.adapter.finish.assert_called_once()
        W.prune_verified_snapshots.assert_not_called()
        repair = json.loads((W.control_directory(self.repo) / "registry-repair.json").read_text())
        self.assertEqual(repair["phase"], "prepare")
        self.assertEqual(repair["status"], "open")
        self.assertNotIn("private bad", json.dumps(repair))

    def test_successful_phase_resolves_its_existing_repair(self):
        directory = self.repo / "control"
        directory.mkdir()
        control = SimpleNamespace(directory=directory)
        W.registry_repair(control, "prepare", ValueError("fixture"))
        W.registry_recovered(control, "finish")
        self.assertEqual(json.loads((directory / "registry-repair.json").read_text())["status"], "open")
        W.registry_recovered(control, "prepare")
        self.assertEqual(json.loads((directory / "registry-repair.json").read_text())["status"], "resolved")

    def test_registry_epoch_markers_and_tries_survive_all_submission_outcomes(self):
        markers = {"registered_payload_sha256": "a" * 64, "registry_job_id": "b" * 64,
                   "previous_capture": "https://web.archive.org/web/20200101000000/" + URL,
                   "recapture": True}
        cases = {"recent": {"recent": markers["previous_capture"]},
                 "accepted": {"job_id": "actual-accepted-id"},
                 "anonymous": {"anonymous_capture": markers["previous_capture"]},
                 "error": ValueError("offline fixture")}
        for name, result in cases.items():
            with self.subTest(outcome=name), \
                 patch.object(W, "control_directory", return_value=self.repo / name), \
                 patch.object(W, "try_verify"), patch.object(W, "verify_entry", return_value=False), \
                 patch.object(W, "confirm", side_effect=lambda url, entry: entry.update(status="failed") or True), \
                 patch.object(W, "submit_capture", side_effect=result if isinstance(result, Exception) else None,
                              return_value=result):
                old = dict(markers, status="retry", last="2000-01-01T00:00:00Z", tries=2)
                (self.repo / W.DONE).write_text(json.dumps({URL: old}))
                (self.repo / W.QUEUE).write_text(URL + "\n")
                W.run(self.repo, 3)
                entry = json.loads((self.repo / W.DONE).read_text())[URL]
                self.assertEqual({key: entry[key] for key in markers}, markers)
                self.assertEqual(entry["tries"], 3)

    def test_auth_blocked_does_zero_adapter_provider_queue_work(self):
        directory = W.control_directory(self.repo)
        with Control(directory, W.AUTH) as control:
            with self.assertRaises(Paused): control.authentication_failed()
        with patch.object(W, "_run") as run:
            W.run(self.repo, 3)
        run.assert_not_called()
        self.factory.assert_not_called()
        self.allowed.assert_not_called()
        self.adapter.finish.assert_not_called()

    def test_prepare_pause_is_preserved_and_finished_inside_owner(self):
        self.adapter.prepare.side_effect = Paused("prepare fixture pause")
        def finish(deadline):
            self.assertIsNotNone(W.ACTIVE_CONTROL)
            self.assertFalse(W.ACTIVE_CONTROL.lock.closed)
        self.adapter.finish.side_effect = finish
        W.run(self.repo, 1)
        self.adapter.finish.assert_called_once()
        self.assertIsNone(W.ACTIVE_CONTROL)

    def test_finish_sees_real_accepted_job_on_pause(self):
        (self.repo / W.QUEUE).write_text(URL + "\n")
        self.stack.enter_context(patch.object(W, "submit_capture", return_value={"job_id": "actual-accepted-id"}))
        self.stack.enter_context(patch.object(W, "confirm", side_effect=Paused("provider pause")))
        def finish(deadline):
            self.assertEqual(W.ACTIVE_CONTROL.done[URL]["job_id"], "actual-accepted-id")
            self.assertFalse(W.ACTIVE_CONTROL.lock.closed)
        self.adapter.finish.side_effect = finish
        W.run(self.repo, 3)
        self.adapter.finish.assert_called_once()

    def test_finish_failure_preserves_primary_failure_and_journal(self):
        primary = RuntimeError("primary fixture failure")
        def prepare(deadline):
            W.ACTIVE_CONTROL.done[URL] = {"status": "pending", "job_id": "actual-accepted-id"}
            raise primary
        self.stack.enter_context(patch.object(W, "pending_confirm_urls", side_effect=primary))
        (self.repo / W.QUEUE).write_text(URL + "\n")
        self.adapter.prepare.side_effect = prepare
        self.adapter.finish.side_effect = ValueError("private secret must not be recorded")
        with self.assertRaises(RuntimeError) as raised: W.run(self.repo, 1)
        self.assertIs(raised.exception, primary)
        directory = W.control_directory(self.repo)
        self.assertIn("actual-accepted-id", (directory / "pending-updates.json").read_text())
        repair = json.loads((directory / "registry-repair.json").read_text())
        self.assertEqual({k: repair[k] for k in ("schema", "status", "repair_issue", "phase", "error_type")},
                         {"schema": 1, "status": "open", "repair_issue": 410, "phase": "finish", "error_type": "ValueError"})
        self.assertNotIn("private secret", json.dumps(repair))
        self.assertIsNone(W.ACTIVE_CONTROL)

    def test_finish_failure_preserves_pause_and_reports_repair(self):
        self.adapter.prepare.side_effect = Paused("original pause")
        self.adapter.finish.side_effect = RuntimeError("sensitive detail")
        W.run(self.repo, 1)
        health = json.loads((W.control_directory(self.repo) / "health.json").read_text())
        self.assertEqual(health["outcome"], "paused")
        self.assertTrue((W.control_directory(self.repo) / "registry-repair.json").exists())

    def test_finish_failure_on_completed_run_is_failure(self):
        self.adapter.finish.side_effect = ValueError("finish fixture")
        with self.assertRaises(ValueError): W.run(self.repo, 1)
        health = json.loads((W.control_directory(self.repo) / "health.json").read_text())
        self.assertEqual(health["outcome"], "failed")

    def test_exact_approved_snapshot_and_legacy_alias_are_excluded(self):
        self.adapter.protected_snapshot_urls.return_value = {URL}
        entry = {"status": "verified", "capture": "old historical body"}
        unrelated = "https://swccg.com/snapshots/other.html"
        done = {URL: entry, ALIAS: entry, unrelated: entry}
        W.prune_legacy_snapshots(SimpleNamespace(registry_adapter=self.adapter, directory=self.repo), done)
        candidates = W.prune_verified_snapshots.call_args.args[0]
        self.assertEqual(set(candidates), {unrelated})
        self.assertIs(candidates[unrelated], entry)
        self.assertEqual(len(done), 3)

    def test_old_verified_cited_alias_cannot_delete_new_approved_payload(self):
        root = self.repo / "snapshots"
        root.mkdir()
        staged = root / "fixture.html"
        staged.write_text("newly staged approved payload")
        self.adapter.protected_snapshot_urls.return_value = {URL}
        # Use the real pruning path; any fetch would trip the offline guard.
        with patch.dict(W.os.environ, {"SWCCG_SNAPSHOT_ROOT": str(root)}), \
             patch.object(W, "prune_verified_snapshots", self.real_prune), \
             patch.object(W, "wiki_snapshot_wayback_paths", return_value={"fixture.html"}):
            W.prune_legacy_snapshots(SimpleNamespace(registry_adapter=self.adapter, directory=self.repo),
                                    {ALIAS: {"status": "verified", "capture": "https://web.archive.org/web/20200101000000/" + ALIAS}})
        self.assertEqual(staged.read_text(), "newly staged approved payload")

    def test_empty_unapproved_cohort_preserves_legacy_candidates(self):
        done = {URL: {"status": "verified"}}
        W.prune_legacy_snapshots(SimpleNamespace(registry_adapter=self.adapter, directory=self.repo), done)
        self.assertEqual(W.prune_verified_snapshots.call_args.args[0], done)

    def test_inventory_failure_skips_all_deletions_and_records_repair(self):
        self.adapter.protected_snapshot_urls.side_effect = ValueError("secret metadata")
        directory = self.repo / "control"
        directory.mkdir()
        W.prune_legacy_snapshots(SimpleNamespace(registry_adapter=self.adapter, directory=directory), {URL: {"status": "verified"}})
        W.prune_verified_snapshots.assert_not_called()
        repair = json.loads((directory / "registry-repair.json").read_text())
        self.assertEqual(repair["phase"], "prune-inventory")
        self.assertNotIn("secret", json.dumps(repair))


if __name__ == "__main__": unittest.main()
