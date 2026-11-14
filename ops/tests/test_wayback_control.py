"""Deterministic recovery, restart and exclusive-owner regressions; no live saves."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W
from wayback_control import Busy, Control, Paused, retry_seconds

URL = "https://example.org/source.png"


class Circuit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.clock = 1_800_000_000.0

    def controller(self, credential="LOW fixture:secret"):
        return Control(self.root / "control", credential, lambda: self.clock)

    def test_auth_rejection_survives_restart_without_retry_or_anonymous_escape(self):
        with self.controller() as c:
            c.begin()
            with self.assertRaises(Paused): c.authentication_failed()
        for credential in ["LOW fixture:secret", None]:
            with self.controller(credential) as restarted:
                with self.assertRaises(Paused): restarted.begin()
                self.assertEqual("auth_blocked", restarted.state["mode"])
        with self.controller("LOW changed:new-secret") as repaired:
            repaired.begin()
            self.assertEqual("half_open", repaired.state["mode"])
            repaired.submitting(URL)
            self.assertFalse(repaired.may_submit("https://example.org/other.png"))

    def test_cooldown_and_failures_survive_restart_and_timer_boundaries(self):
        with self.controller() as c:
            with self.assertRaises(Paused): c.provider_failed(520)
            first = c.state["next_attempt"]
        self.clock += 60
        with self.controller() as c:
            with self.assertRaises(Paused): c.begin()
            self.assertEqual(first, c.state["next_attempt"])
        self.clock = first
        with self.controller() as c:
            c.begin()
            with self.assertRaises(Paused): c.provider_failed(520)
            self.assertEqual(self.clock + 1800, c.state["next_attempt"])

    def test_retry_after_seconds_and_http_date_are_not_shortened(self):
        with self.controller() as c:
            with self.assertRaises(Paused): c.provider_failed(429, "7200")
            self.assertEqual(self.clock + 7200, c.state["next_attempt"])
        date = datetime.fromtimestamp(self.clock + 4000, timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.assertEqual(4000, retry_seconds(date, self.clock))
        for invalid in ["", None, "junk", "-1"]:
            self.assertEqual(0, retry_seconds(invalid, self.clock))

    def test_circuit_closes_only_after_verified_canary_not_a_job_or_http_success(self):
        with self.controller() as c:
            with self.assertRaises(Paused): c.provider_failed(503)
            self.clock = c.state["next_attempt"]
            c.begin(); c.submitting(URL)
            for status in ["pending", "ok"]:
                c.reconcile({URL:{"status":status}}, set())
                self.assertEqual("half_open", c.state["mode"])
                self.assertFalse(c.may_submit("another"))
            c.reconcile({URL:{"status":"verified"}}, set())
            self.assertEqual("healthy", c.state["mode"])
            self.clock += Control.SUBMISSION_GAP
            self.assertTrue(c.may_submit("another"))
            self.assertEqual(0, c.state["failure_count"])

    def test_recovery_probe_and_pending_job_are_retained_across_restart(self):
        with self.controller() as c:
            with self.assertRaises(Paused): c.provider_failed(429)
            self.clock = c.state["next_attempt"]
            c.begin(); c.submitting(URL)
        self.clock += Control.SUBMISSION_GAP
        with self.controller() as restarted:
            restarted.begin()
            self.assertFalse(restarted.may_submit("another"))
            self.assertEqual(URL, restarted.state["probe_url"])

    def test_unverified_canary_cannot_certify_recovery_or_immediately_retry(self):
        with self.controller() as c:
            c.state["mode"]="half_open"; c.submitting(URL)
            c.reconcile({URL:{"status":"unverified"}}, set())
            self.assertEqual("half_open", c.state["mode"])
            self.assertGreater(c.state["next_attempt"], self.clock)
        with self.controller() as restarted:
            with self.assertRaises(Paused): restarted.begin()

    def test_lock_excludes_a_separate_process_and_releases_on_exit(self):
        with self.controller() as c:
            code="from wayback_control import Control,Busy;from pathlib import Path;import sys\ntry:\n with Control(Path(sys.argv[1]),None): sys.exit(9)\nexcept Busy: sys.exit(0)"
            env={**os.environ,"PYTHONPATH":str(Path(W.__file__).parent)}
            p=subprocess.run([sys.executable,"-c",code,str(c.directory)],env=env,capture_output=True,timeout=10)
            self.assertEqual(0,p.returncode,p.stderr)
        with self.controller() as next_owner:
            next_owner.begin()

    def test_process_crash_releases_lock_and_keeps_acknowledged_job_journal(self):
        code="from wayback_control import Control;from pathlib import Path;import os,sys\nwith Control(Path(sys.argv[1]),None) as c:\n c.checkpoint({'https://example.org/source.png':{'status':'pending','job_id':'before-crash'}},{})\n os._exit(0)"
        env={**os.environ,"PYTHONPATH":str(Path(W.__file__).parent)}
        p=subprocess.run([sys.executable,"-c",code,str(self.root/'control')],env=env,capture_output=True,timeout=10)
        self.assertEqual(0,p.returncode,p.stderr)
        with self.controller() as c:
            c.begin();done={};c.restore_updates(done)
            self.assertEqual('before-crash',done[URL]['job_id'])

    def test_corrupt_state_fails_closed_instead_of_forgetting_the_pause(self):
        folder=self.root/'control';folder.mkdir();(folder/'control.json').write_text('{bad')
        with self.assertRaises(ValueError):
            with self.controller(): self.fail("corrupt state admitted a run")
        self.assertEqual('{bad',(folder/'control.json').read_text())

    def test_nonfinite_cooldown_cannot_silently_disable_the_gate(self):
        folder=self.root/'control';folder.mkdir()
        (folder/'control.json').write_text('{"schema":1,"mode":"open","failure_count":1,"next_attempt":NaN}')
        with self.assertRaises(ValueError):
            with self.controller():self.fail('nonfinite cooldown admitted')

    def test_corrupt_repair_record_never_prevents_the_auth_pause(self):
        with self.controller() as c:
            (c.directory/'repair.json').write_text('{bad')
            with self.assertRaises(Paused):c.authentication_failed()
            self.assertEqual('auth_blocked',c.state['mode'])
            self.assertFalse(c.may_submit(URL))
        with self.controller() as c:
            with self.assertRaises(Paused):c.begin()

    def test_submission_spacing_survives_a_process_restart(self):
        with self.controller() as c:c.begin();c.submitting(URL)
        with self.controller() as c:
            with self.assertRaises(Paused):c.begin()
        self.clock+=Control.SUBMISSION_GAP
        with self.controller() as c:c.begin();self.assertTrue(c.may_submit(URL))

    def test_acknowledged_pending_job_is_restored_without_losing_its_identity(self):
        pending={URL:{'status':'pending','job_id':'acknowledged','tries':1}}
        with self.controller() as c:c.checkpoint(pending,{})
        with self.controller() as c:
            done={};restored=c.restore_updates(done)
            self.assertEqual(pending,done);self.assertEqual(pending,restored)
            self.assertEqual('acknowledged',done[URL]['job_id'])
            c.ledger_saved();self.assertFalse((c.directory/'pending-updates.json').exists())

    def test_pending_journal_cannot_overwrite_a_different_newer_verified_receipt(self):
        with self.controller() as c:
            c.checkpoint({URL:{'status':'pending','job_id':'old'}},{})
            newer={URL:{'status':'verified','capture':'different-newer-receipt'}}
            with self.assertRaises(ValueError):c.restore_updates(newer)
            self.assertEqual('verified',newer[URL]['status'])
            self.assertTrue((c.directory/'pending-updates.json').exists())

    def test_health_reports_real_progress_and_never_credential_material(self):
        with self.controller() as c:
            c.begin();c.reconcile({URL:{"status":"pending","last":"2026-11-14T00:00:00Z"}},set())
            health=c.health({URL:{"status":"pending","last":"2026-11-14T00:00:00Z"}},"completed")
            self.assertIsNone(health['last_verified_progress_at'])
            self.assertFalse(health['process_success_is_capture_success'])
            c.reconcile({URL:{"status":"verified"}},set())
            health=c.health({URL:{"status":"verified"}},"completed")
            self.assertIsNotNone(health['last_verified_progress_at'])
            text=json.dumps(health)
            self.assertNotIn('secret',text);self.assertNotIn(c.credential,text)

    def test_repair_record_deduplicates_the_same_unresolved_incident(self):
        with self.controller() as c:
            with self.assertRaises(Paused):c.provider_failed(520)
            first=json.loads((c.directory/'repair.json').read_text())
            self.clock=c.state['next_attempt'];c.begin()
            with self.assertRaises(Paused):c.provider_failed(520)
            second=json.loads((c.directory/'repair.json').read_text())
            self.assertEqual(first['incident_id'],second['incident_id'])
            self.assertEqual(first['first_seen_at'],second['first_seen_at'])
            self.assertEqual(2,second['occurrences'])


class WorkerIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.repo=Path(self.tmp.name);(self.repo/W.QUEUE).parent.mkdir(parents=True)
        (self.repo/W.QUEUE).write_text(URL+'\n')
        self.patches=[patch.object(W,'control_directory',lambda _:self.repo/'control'),
                      patch.object(W,'reset_to_origin'),patch.object(W,'commit_and_push',side_effect=lambda repo,paths,msg,redo:bool(redo())),
                      patch.object(W,'wiki_snapshot_wayback_paths',return_value=set()),
                      patch.object(W.urllib.request,'urlopen',side_effect=AssertionError('live network forbidden')),
                      patch.object(W,'AUTH','LOW fixture:secret')]
        for p in self.patches:p.start();self.addCleanup(p.stop)

    def test_two_timer_runs_make_one_rejected_auth_request_and_zero_fallbacks(self):
        err=urllib.error.HTTPError('https://web.archive.org/save',401,'rejected',{},None)
        with patch.object(W,'spn2_submit',side_effect=err) as auth,patch.object(W,'save_anon') as anonymous:
            W.run(self.repo,5);W.run(self.repo,5)
            self.assertEqual(1,auth.call_count);anonymous.assert_not_called()
            self.assertFalse((self.repo/W.DONE).exists())
            health=json.loads((self.repo/'control/health.json').read_text())
            self.assertEqual('auth_blocked',health['mode'])

    def test_provider_pause_preserves_partial_jobs_and_existing_verified_rows(self):
        old='https://example.org/old.png'
        original={old:{'status':'verified','capture':'unchanged','tries':2,'last':'2026-11-01T00:00:00Z'}}
        (self.repo/W.DONE).write_text(json.dumps(original))
        def process(repo,minutes,control):
            control.done[URL]={'status':'pending','job_id':'accepted-before-outage','tries':1,'last':'2026-11-14T00:00:00Z'}
            control.provider_failed(503,'3600')
        with patch.object(W,'_run',side_effect=process):W.run(self.repo,1)
        result=json.loads((self.repo/W.DONE).read_text())
        self.assertEqual(original[old],result[old]);self.assertEqual('accepted-before-outage',result[URL]['job_id'])
        self.assertNotEqual('verified',result[URL]['status'])

    def test_interruption_retains_job_ack_for_next_run_even_without_git_push(self):
        def process(repo,minutes,control):
            control.done[URL]={'status':'pending','job_id':'interrupted-ack','tries':1}
            raise KeyboardInterrupt()
        with patch.object(W,'_run',side_effect=process):
            with self.assertRaises(KeyboardInterrupt):W.run(self.repo,5)
        with Control(self.repo/'control',W.AUTH) as c:
            done={};c.restore_updates(done)
            self.assertEqual('interrupted-ack',done[URL]['job_id'])

    def test_retry_after_from_real_http_error_reaches_the_persistent_gate(self):
        error=urllib.error.HTTPError('https://web.archive.org/save',429,'limited',{'Retry-After':'7200'},None)
        with Control(self.repo/'control',W.AUTH) as c,patch.object(W,'ACTIVE_CONTROL',None):
            with patch.object(W,'ACTIVE_CONTROL',c),patch.object(W.urllib.request,'urlopen',side_effect=error):
                with self.assertRaises(Paused):W.spn2_submit(URL)
            self.assertGreaterEqual(c.state['next_attempt']-c.clock(),7199)

    def test_source_host_throttle_does_not_open_archive_provider_circuit(self):
        with Control(self.repo/'control',W.AUTH) as c,patch.object(W,'ACTIVE_CONTROL',None):
            with patch.object(W,'ACTIVE_CONTROL',c):W.archive_response(URL,429,{'Retry-After':'3600'})
            self.assertEqual('healthy',c.state['mode'])

    def test_corrupt_control_does_not_contact_git_or_archive(self):
        (self.repo/'control').mkdir();(self.repo/'control/control.json').write_text('{}')
        with patch.object(W,'_run') as process:
            with self.assertRaises(ValueError):W.run(self.repo,1)
            process.assert_not_called()

    def test_concurrent_ledger_additions_are_preserved_when_saving_our_job(self):
        peer='https://example.org/peer.png'
        current={peer:{'status':'verified','capture':'peer-checked'}}
        (self.repo/W.DONE).write_text(json.dumps(current))
        ours={URL:{'status':'pending','job_id':'ours'}}
        W.persist_changes(self.repo,dict(ours),ours,{})
        saved=json.loads((self.repo/W.DONE).read_text())
        self.assertEqual(current[peer],saved[peer]);self.assertEqual(ours[URL],saved[URL])

    def test_ledger_write_occurs_only_inside_the_git_callback(self):
        original={URL:{'status':'pending','job_id':'old'}}
        (self.repo/W.DONE).write_text(json.dumps(original))
        replacement={URL:{'status':'verified','capture':'checked'}}
        def locked_commit(repo,paths,msg,redo):
            self.assertEqual(original,json.loads((repo/W.DONE).read_text()))
            redo()
            self.assertEqual(replacement,json.loads((repo/W.DONE).read_text()))
            return True
        with patch.object(W,'commit_and_push',side_effect=locked_commit):
            W.persist_changes(self.repo,dict(replacement),replacement,original)

    def test_old_git_helper_cannot_silently_discard_unwritten_updates(self):
        ours={URL:{'status':'pending','job_id':'ack'}}
        with patch.object(W,'commit_and_push',return_value=False):
            with self.assertRaises(RuntimeError):W.persist_changes(self.repo,dict(ours),ours,{})
        self.assertFalse((self.repo/W.DONE).exists())

    def test_conflicting_newer_ledger_receipt_is_never_overwritten(self):
        current={URL:{'status':'verified','capture':'newer'}}
        (self.repo/W.DONE).write_text(json.dumps(current))
        old={URL:{'status':'pending','job_id':'ours'}}
        with self.assertRaises(RuntimeError):W.persist_changes(self.repo,dict(old),old,{})
        self.assertEqual(current,json.loads((self.repo/W.DONE).read_text()))


if __name__=='__main__':unittest.main()
