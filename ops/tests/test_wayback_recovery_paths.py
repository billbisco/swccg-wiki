"""Worker-level availability failures and old accepted-canary restarts."""
import io
import json
import sys
import tempfile
import time
import unittest
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W
from wayback_control import Control, Paused

URL = "https://example.org/recovery.png"


class Response(io.BytesIO):
    status = 200
    headers = {}

    def __init__(self, data):
        super().__init__(json.dumps(data).encode())


class RecoveryPaths(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.directory = self.repo / "control"
        (self.repo / W.QUEUE).parent.mkdir(parents=True)
        (self.repo / W.QUEUE).write_text(URL + "\nhttps://example.org/second.png\n")
        patches = [
            patch.object(W, "control_directory", lambda _: self.directory),
            patch.object(W, "reset_to_origin"),
            patch.object(W, "commit_and_push", side_effect=lambda repo, paths, msg, redo: bool(redo())),
            patch.object(W, "wiki_snapshot_wayback_paths", return_value=set()),
            patch.object(W, "AUTH", "LOW offline:fixture"),
            patch.object(W.time, "sleep"),
            patch.object(W.urllib.request, "urlopen", side_effect=AssertionError("external network forbidden")),
        ]
        for p in patches:
            p.start(); self.addCleanup(p.stop)

    def seed_accepted_probe(self, age_seconds, legacy_state=False):
        started = time.time() - age_seconds
        entry = {"status": "pending", "job_id": "accepted-before-offline", "tries": 1,
                 "last": datetime.fromtimestamp(started, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        (self.repo / W.DONE).write_text(json.dumps({URL:entry}))
        with Control(self.directory, W.AUTH) as c:
            c.state.update(mode="half_open", probe_url=URL, next_attempt=0,
                           last_submission_attempt_at=datetime.fromtimestamp(started, timezone.utc).isoformat())
            if not legacy_state:
                c.state["probe_started_at"] = started
            c.save()
        return entry

    def saved(self):
        return json.loads((self.repo / W.DONE).read_text())

    def state(self):
        return json.loads((self.directory / "control.json").read_text())

    def test_availability_429_pauses_worker_and_subsequent_timer_without_another_save(self):
        calls = []

        def response(req, **kwargs):
            calls.append(req.full_url)
            if req.full_url == "https://web.archive.org/save":
                return Response({"message":"same snapshot had been made"})
            if req.full_url.startswith("https://archive.org/wayback/available?"):
                raise urllib.error.HTTPError(req.full_url,429,"limited",{"Retry-After":"7200"},None)
            self.fail("unexpected request")

        with patch.object(W.urllib.request, "urlopen", side_effect=response), patch.object(W, "save_anon") as anonymous:
            W.run(self.repo,5)
            W.run(self.repo,5)
        self.assertEqual(2,len(calls))
        self.assertEqual(1,calls.count("https://web.archive.org/save"))
        anonymous.assert_not_called()
        self.assertEqual("open",self.state()["mode"])
        self.assertGreater(self.state()["next_attempt"]-time.time(),7190)
        self.assertFalse((self.repo/W.DONE).exists())

    def test_availability_provider_and_transport_errors_are_not_swallowed(self):
        for suffix,error in [
            ("http",urllib.error.HTTPError("https://archive.org/wayback/available",520,"unavailable",{},None)),
            ("transport",urllib.error.URLError("offline fixture")),
        ]:
            with self.subTest(suffix=suffix), Control(self.repo/suffix,W.AUTH) as c:
                with patch.object(W,"ACTIVE_CONTROL",c), patch.object(W.urllib.request,"urlopen",side_effect=error):
                    with self.assertRaises(Paused):W.latest_capture(URL)
                self.assertEqual("open",c.state["mode"])

    def test_anonymous_save401_persists_repair_and_never_repeats_on_next_timer(self):
        address="https://web.archive.org/save/"+URL
        error=urllib.error.HTTPError(address,401,"rejected",{},None)
        with patch.object(W,"AUTH",None), patch.object(W.OPENER,"open",side_effect=error) as request:
            W.run(self.repo,5);W.run(self.repo,5)
        self.assertEqual(1,request.call_count)
        self.assertEqual("auth_blocked",self.state()["mode"])
        self.assertFalse((self.repo/W.DONE).exists())

    def test_three_hour_probe_is_polled_once_per_worker_restart_without_duplicate_submission(self):
        original=self.seed_accepted_probe(3*3600,legacy_state=True)
        with patch.object(W,"spn2_status",return_value={"status":"pending"}) as status, patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5);W.run(self.repo,5)
        self.assertEqual(2,status.call_count)
        status.assert_called_with("accepted-before-offline")
        submit.assert_not_called()
        self.assertEqual(original,self.saved()[URL])
        self.assertEqual("half_open",self.state()["mode"])
        self.assertIsNotNone(self.state().get("probe_started_at"))

    def test_twenty_five_hour_probe_gets_one_reconciliation_then_explicit_owned_repair(self):
        original=self.seed_accepted_probe(25*3600)
        with patch.object(W,"spn2_status",return_value={"status":"pending"}) as status, patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5);W.run(self.repo,5)
        status.assert_called_once_with("accepted-before-offline")
        submit.assert_not_called()
        self.assertEqual(original,self.saved()[URL])
        self.assertEqual("probe_blocked",self.state()["mode"])
        self.assertEqual(URL,self.state()["probe_url"])
        repair=json.loads((self.directory/"repair.json").read_text())
        self.assertEqual(407,repair["repair_issue"])
        self.assertIn("24hours",repair["reason"])

    def test_old_completed_probe_is_verified_instead_of_expiring_or_resubmitting(self):
        self.seed_accepted_probe(25*3600)
        def verify(url,entry):entry.update(status="verified",verify={"method":"fixture-checked"})
        result={"status":"success","timestamp":"20261114120000","original_url":URL}
        with patch.object(W,"spn2_status",return_value=result) as status, patch.object(W,"capture_ok",return_value=True), patch.object(W,"try_verify",side_effect=verify), patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        status.assert_called_once_with("accepted-before-offline")
        submit.assert_not_called()
        self.assertEqual("verified",self.saved()[URL]["status"])
        self.assertEqual("accepted-before-offline",self.saved()[URL]["job_id"])
        self.assertEqual("healthy",self.state()["mode"])

    def test_expired_unknown_job_enters_repair_without_losing_accepted_id(self):
        self.seed_accepted_probe(25*3600)
        result={"status":"error","status_ext":"unknown-or-expired-job"}
        with patch.object(W,"spn2_status",return_value=result), patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        submit.assert_not_called()
        self.assertEqual("probe_blocked",self.state()["mode"])
        self.assertEqual("accepted-before-offline",self.saved()[URL]["job_id"])

    def test_independently_verified_receipt_can_release_probe_repair_without_resetting_control(self):
        self.seed_accepted_probe(25*3600)
        with patch.object(W,"spn2_status",return_value={"status":"pending"}):W.run(self.repo,5)
        done=self.saved();done[URL].update(status="verified",capture="independently-checked")
        (self.repo/W.DONE).write_text(json.dumps(done));(self.repo/W.QUEUE).write_text(URL+"\n")
        with patch.object(W,"spn2_status") as status, patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        status.assert_not_called();submit.assert_not_called()
        self.assertEqual("healthy",self.state()["mode"])

    def test_provider_pause_during_probe_poll_retains_accepted_identity_for_recovery(self):
        original=self.seed_accepted_probe(3*3600)
        error=urllib.error.URLError("offline fixture")
        with patch.object(W,"spn2_status",side_effect=error), patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        submit.assert_not_called()
        self.assertEqual(original,self.saved()[URL])
        self.assertEqual("open",self.state()["mode"])
        self.assertEqual(URL,self.state()["probe_url"])
        with Control(self.directory,W.AUTH) as c:
            c.state["next_attempt"]=0;c.save()
        with patch.object(W,"spn2_status",return_value={"status":"pending"}) as status, patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        status.assert_called_once_with("accepted-before-offline")
        submit.assert_not_called()

    def test_missing_canary_receipt_enters_repair_without_a_parallel_replacement(self):
        self.seed_accepted_probe(3*3600)
        (self.repo/W.DONE).write_text("{}")
        with patch.object(W,"spn2_status") as status, patch.object(W,"spn2_submit") as submit:
            W.run(self.repo,5)
        status.assert_not_called();submit.assert_not_called()
        self.assertEqual("probe_blocked",self.state()["mode"])


if __name__=="__main__":unittest.main()
