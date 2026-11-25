import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
from test_preservation_registration import fixture
from preservation_registry import register, atomic_json, SERVER_OWNER
from preservation_owner_receipts import store_event
import preservation_policy as policy


class PolicyTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.registry = Path(tmp.name) / "registry"

    def add(self, title, *, ready=True, ticket=410, reason=None, generation=0):
        request = fixture(title=title, ready=ready)
        if ticket is None:
            request["approval_scope"] = {"publication_ticket": 386}
        else:
            request["approval_scope"]["ticket"] = ticket
        if reason:
            request["readiness"]["reason"] = reason
        request["generation"] = generation
        return register(self.registry, request)["object_id"], request

    def test_ticket_number_forms(self):
        self.assertEqual(policy.ticket_number(1359), 1359)
        self.assertEqual(policy.ticket_number("#382"), 382)
        self.assertEqual(policy.ticket_number("1310"), 1310)
        self.assertEqual(policy.ticket_number("https://github.com/swccg-guild/work/issues/1359"), 1359)
        for bad in (None, True, 0, -3, "", "n/a", "PR 12", "https://github.com/other/repo/issues/5"):
            self.assertIsNone(policy.ticket_number(bad), bad)

    def test_ready_with_ticket_is_approved_others_stay_out(self):
        good, _ = self.add("File:good.png", ticket=1310)
        url_ticket, _ = self.add("File:url.png", ticket="https://github.com/swccg-guild/work/issues/1246")
        none, _ = self.add("File:none.png", ticket=None)
        unready, _ = self.add("File:unready.png", ready=False)
        held, _ = self.add("File:held.png", ready=False, reason=policy.HOLD_MARK + "; do not submit")
        explicit, _ = self.add("File:explicit.png", ticket=611)
        result = policy.apply(self.registry, {explicit}, seconds_left=3600, now=1000.0)
        log = policy.load_log(self.registry)
        self.assertEqual(set(log), {good, url_ticket})
        self.assertEqual(log[good]["ticket"], 1310)
        self.assertEqual(log[url_ticket]["ticket"], 1246)
        self.assertEqual(result["new"], 2)
        self.assertEqual(result["new_by_ticket"], {1310: 1, 1246: 1})
        self.assertEqual(result["window"], {good, url_ticket})
        self.assertNotIn(explicit, result["window"])
        flagged = json.loads((self.registry / policy.FLAGGED_NAME).read_text())
        self.assertEqual(flagged["no_ticket"], 1)
        self.assertEqual(flagged["no_ticket_object_ids"], [none])
        self.assertEqual(flagged["counts"]["held"], 1)
        self.assertEqual(flagged["counts"]["not-ready"], 1)
        self.assertNotIn(held, log)
        self.assertNotIn(unready, log)
        # approved-objects.json is never written by the policy.
        self.assertFalse((self.registry / "approved-objects.json").exists())

    def test_log_is_append_only_and_scan_is_hourly(self):
        first, _ = self.add("File:first.png")
        policy.apply(self.registry, set(), seconds_left=3600, now=1000.0)
        before = (self.registry / policy.LOG_NAME).read_text()
        second, _ = self.add("File:second.png")
        r = policy.apply(self.registry, set(), seconds_left=3600, now=1000.0 + 60)
        self.assertFalse(r["scanned"])
        self.assertEqual(r["window"], {first})
        r = policy.apply(self.registry, set(), seconds_left=3600, now=1000.0 + policy.SCAN_INTERVAL_S)
        self.assertTrue(r["scanned"])
        after = (self.registry / policy.LOG_NAME).read_text()
        self.assertTrue(after.startswith(before))
        self.assertEqual(r["window"], {first, second})
        # No scan near the end of a run.
        third, _ = self.add("File:third.png")
        r = policy.apply(self.registry, set(), seconds_left=60, now=1000.0 + 3 * policy.SCAN_INTERVAL_S)
        self.assertFalse(r["scanned"])
        self.assertNotIn(third, r["window"])

    def test_window_drops_verified_held_later_and_respects_cap(self):
        a, req_a = self.add("File:a.png")
        b, _ = self.add("File:b.png")
        c, _ = self.add("File:c.png")
        policy.apply(self.registry, set(), seconds_left=3600, now=1000.0)
        # A later held observation of b takes it out of the window.
        self.add("File:b.png", ready=False, reason=policy.HOLD_MARK, generation=1)
        # A verified owner event takes a payload out (all fixtures share one payload here,
        # so check with a cap instead and a fresh registry for the verified case).
        r = policy.window(self.registry, policy.load_log(self.registry), set(), cap=1)
        self.assertEqual(len(r), 1)
        r = policy.window(self.registry, policy.load_log(self.registry), set(), cap=10)
        self.assertEqual(r, {a, c})
        store_event(self.registry, {"schema_version": 1, "job_id": "payload:" + req_a["source"]["sha256"],
                                    "source_sha256": req_a["source"]["sha256"],
                                    "source_bytes": req_a["source"]["bytes"],
                                    "approved_object_ids": [a], "state": "verified",
                                    "reason": "test", "owner": SERVER_OWNER})
        r = policy.window(self.registry, policy.load_log(self.registry), set(), cap=10)
        self.assertEqual(r, set())  # shared payload verified
        r = policy.apply(self.registry, set(), seconds_left=3600, now=1000.0 + 10)
        self.assertEqual(r["cap"], policy.MAX_ALLOWED)

    def test_worker_hook_falls_back_on_error(self):
        import wayback_worker as worker
        control = SimpleNamespace(directory=self.registry.parent)
        a, _ = self.add("File:hook.png")
        out = io.StringIO()
        with mock.patch("sys.stdout", out):
            got = worker.ticket_policy_window(control, set(), worker.time.monotonic() + 3600)
        self.assertEqual(got, {a})
        self.assertIn("policy-approval: scanned=True new=1 tickets=#410:1", out.getvalue())
        with mock.patch.object(policy, "apply", side_effect=RuntimeError("x")), mock.patch("sys.stdout", io.StringIO()):
            self.assertEqual(worker.ticket_policy_window(control, set(), worker.time.monotonic() + 3600), set())


if __name__ == "__main__":
    unittest.main()
