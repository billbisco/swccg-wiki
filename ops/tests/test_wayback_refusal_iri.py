"""#1375: refused connections end a step cleanly; non-ASCII URLs never crash a run."""
import hashlib
import io
import json
import sys
import tempfile
import time
import unittest
import urllib.error
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
import wayback_worker as W  # noqa: E402
from wayback_control import Control, Paused  # noqa: E402
from preservation_owner import OwnerAdapter  # noqa: E402

REFUSED = lambda: urllib.error.URLError(ConnectionRefusedError(111, "Connection refused"))  # noqa: E731
URL = "https://swccg.com/wiki/File:2025_World_Championship_player_4_October_1407.jpg"
IRI = "https://example.org/images/Bjørn_Sørensen.jpg"
WIRE = "https://example.org/images/Bj%C3%B8rn_S%C3%B8rensen.jpg"


def refused_verify_retry():
    try:
        raise REFUSED()
    except urllib.error.URLError as error:
        try:
            raise W.VerifyRetry(f"URLError: {error}", side="capture") from error
        except W.VerifyRetry as wrapped:
            return wrapped


class WorkerRun(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        (self.repo / "ops/wayback").mkdir(parents=True)
        (self.repo / W.QUEUE).write_text("")
        (self.repo / W.DONE).write_text("{}")
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        for name in ("reset_to_origin", "recheck_replay_only", "prune_verified_snapshots"):
            self.stack.enter_context(patch.object(W, name))
        self.stack.enter_context(patch.object(W, "control_directory", return_value=self.repo / "control"))
        self.stack.enter_context(patch.object(W, "AUTH", "LOW fixture:offline"))
        self.stack.enter_context(patch.object(W.time, "sleep"))
        self.stack.enter_context(patch.object(W.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")))
        self.stack.enter_context(patch.object(W, "commit_and_push", side_effect=lambda r, p, m, redo: redo()))
        self.adapter = Mock()
        self.adapter.prepare.return_value = {"ledger_updates": {}}
        self.adapter.protected_snapshot_urls.return_value = set()
        self.stack.enter_context(patch.object(W, "OwnerAdapter", return_value=self.adapter))
        self.stack.enter_context(patch.object(W, "load_allowed_objects", return_value=set()))

    def state(self):
        return json.loads((self.repo / "control" / "control.json").read_text())

    def health(self):
        return json.loads((self.repo / "control" / "health.json").read_text())

    def test_refused_verify_in_owner_finish_returns_and_records_cooldown(self):
        self.adapter.finish.side_effect = refused_verify_retry()
        before = time.time()
        W.run(self.repo, 1)  # the 26 Nov journal: VerifyRetry escaped here and exited 1
        state = self.state()
        self.assertEqual("network_refused", state["provider_event"])
        self.assertGreaterEqual(state["next_attempt"], before + Control.MIN_PAUSE - 1)
        self.assertEqual("paused", self.health()["outcome"])
        self.assertFalse((self.repo / "control" / "registry-repair.json").exists())
        self.assertIsNone(W.ACTIVE_CONTROL)

    def test_refusal_escaping_the_run_saves_ledger_and_exits_cleanly(self):
        url = "https://example.org/a.png"
        entry = {"status": "verified", "capture": "https://web.archive.org/web/20261120000000/" + url,
                 "tries": 1, "last": "2026-11-20T00:00:00Z"}
        def boom(control, done, changed, deadline):
            done[url] = entry
            raise refused_verify_retry()
        self.stack.enter_context(patch.object(W, "reconcile_recovery_probe", side_effect=boom))
        W.run(self.repo, 1)
        self.assertEqual(entry, json.loads((self.repo / W.DONE).read_text())[url])
        self.assertFalse((self.repo / "control" / "pending-updates.json").exists())
        self.assertEqual("network_refused", self.state()["provider_event"])
        self.assertEqual("paused", self.health()["outcome"])

    def test_timeout_escaping_the_run_defers_without_cooldown(self):
        self.stack.enter_context(patch.object(W, "reconcile_recovery_probe",
                                              side_effect=W.VerifyRetry("TimeoutError: timed out", side="capture")))
        W.run(self.repo, 1)
        self.assertNotEqual("network_refused", self.state().get("provider_event"))
        self.assertEqual("paused", self.health()["outcome"])

    def test_refused_verify_during_run_defers_item_and_keeps_going(self):
        url = "https://example.org/b.png"
        cap = "https://web.archive.org/web/20261120000000/" + url
        (self.repo / W.DONE).write_text(json.dumps({url: {"status": "ok", "capture": cap, "tries": 1,
                                                          "last": "2026-11-20T00:00:00Z"}}))
        self.stack.enter_context(patch.object(W, "strict_check", side_effect=refused_verify_retry()))
        W.run(self.repo, 5)
        row = json.loads((self.repo / W.DONE).read_text())[url]
        self.assertEqual("ok", row["status"])
        self.assertEqual("manpc", row["verify"]["defer"])
        self.assertEqual("completed", self.health()["outcome"])

    def test_bad_row_in_backlog_is_marked_and_the_run_completes(self):
        bad, good = "https://example.org/bad.png", "https://example.org/good.png"
        rows = {u: {"status": "ok", "capture": "https://web.archive.org/web/20261120000000/" + u,
                    "tries": 1, "last": t} for u, t in ((bad, "2026-11-21T00:00:00Z"), (good, "2026-11-20T00:00:00Z"))}
        (self.repo / W.DONE).write_text(json.dumps(rows))
        seen = []
        def verify_entry(url, e, get=None):
            seen.append(url)
            if url == bad:
                raise KeyError("unexpected fixture shape")
            e["status"] = "verified"
            return True
        self.stack.enter_context(patch.object(W, "verify_entry", side_effect=verify_entry))
        W.run(self.repo, 5)
        saved = json.loads((self.repo / W.DONE).read_text())
        self.assertEqual([bad, good], seen)
        self.assertEqual("verified", saved[good]["status"])
        self.assertIn("KeyError", saved[bad]["verify"]["error"])
        self.assertEqual(1, saved[bad]["verify_tries"])


class OwnerObserve(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.lock = io.BytesIO(b"fixture")
        self.waits = []
        def capacity_wait(reason, retry_after=None):
            self.waits.append(reason)
            raise Paused("account capacity unavailable; bounded wait")
        self.control = SimpleNamespace(directory=Path(self.temp.name), state={"mode": "healthy"},
                                       lock=self.lock, done={}, capacity_wait=capacity_wait)
        self.calls = []
        self.worker = SimpleNamespace(
            ACTIVE_CONTROL=self.control, VerifyRetry=W.VerifyRetry, provider_refused=W.provider_refused,
            capture_parts=W.capture_parts, id_url=W.id_url,
            fetch=lambda url: self.calls.append(url) or {"status": 200, "sha256": "x", "size": 1})
        self.adapter = OwnerAdapter(self.worker, Path(self.temp.name), self.control, set(), work=Path(self.temp.name))
        self.source = {"url": "https://example.org/c.png", "sha256": "x", "bytes": 1}
        self.entries = [{"request": {"source": self.source}}]
        self.legacy = {"status": "ok", "capture": "https://web.archive.org/web/20261120000000/https://example.org/c.png"}

    def test_refusal_records_cooldown_and_stops_replay_requests(self):
        self.worker.strict_check = Mock(side_effect=refused_verify_retry())
        with self.assertRaises(Paused):
            self.adapter._observe(self.entries, self.legacy, time.monotonic() + 300)
        self.assertEqual(["network_refused"], self.waits)
        self.assertEqual("pending", self.adapter._observe(self.entries, self.legacy, time.monotonic() + 300))
        self.worker.strict_check.assert_called_once()
        self.assertEqual([], self.calls)

    def test_timeout_defers_without_cooldown(self):
        self.worker.strict_check = Mock(return_value=(True, "ok"))
        self.worker.fetch = Mock(side_effect=W.VerifyRetry("TimeoutError: timed out"))
        self.assertEqual("pending", self.adapter._observe(self.entries, self.legacy, time.monotonic() + 300))
        self.assertEqual([], self.waits)
        self.assertTrue(self.adapter.replay_deferred)

    def test_other_errors_still_raise(self):
        self.worker.strict_check = Mock(side_effect=KeyError("fixture"))
        with self.assertRaises(KeyError):
            self.adapter._observe(self.entries, self.legacy, time.monotonic() + 300)


class FakeResponse(io.BytesIO):
    def __init__(self, body=b"", status=200, headers=None):
        super().__init__(body)
        self.status = status
        self.headers = headers or {}

    def geturl(self):
        return ""


class NonAsciiUrls(unittest.TestCase):
    def test_wire_url_percent_encodes_only_what_ascii_cannot_carry(self):
        self.assertEqual(WIRE, W.wire_url(IRI))
        self.assertEqual("https://web.archive.org/web/20261120000000id_/" + WIRE,
                         W.wire_url("https://web.archive.org/web/20261120000000id_/" + IRI))
        plain = "https://swccg.com/wiki/File:A%20b.jpg?x=1&y=%C3%B8#f"
        self.assertEqual(plain, W.wire_url(plain))
        self.assertEqual("https://example.org/a%20b?q=%C3%B8", W.wire_url("https://example.org/a b?q=ø"))
        self.assertEqual("https://" + "bjørn".encode("idna").decode() + ".example/x",
                         W.wire_url("https://bjørn.example/x"))

    def test_request_helpers_send_ascii(self):
        seen = []
        def urlopen(req, timeout=None):
            seen.append(req.full_url)
            req.full_url.encode("ascii")
            return FakeResponse(b"body")
        def opener(req, timeout=None):
            seen.append(req.full_url)
            return FakeResponse(b"body")
        cap = "https://web.archive.org/web/20261120000000/" + IRI
        with patch.object(W.urllib.request, "urlopen", side_effect=urlopen), \
             patch.object(W.OPENER, "open", side_effect=opener):
            self.assertTrue(W.capture_ok(cap))
            self.assertEqual(200, W.fetch(IRI)["status"])
            self.assertEqual(200, W._raw_get(W.id_url(cap))[0])
        self.assertTrue(all(u.isascii() for u in seen))
        self.assertTrue(all("Bj%C3%B8rn" in u for u in seen))

    def test_run_with_non_ascii_queue_url_keeps_ledger_key_and_never_crashes(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        repo = Path(temp.name)
        (repo / "ops/wayback").mkdir(parents=True)
        (repo / W.QUEUE).write_text(IRI + "\n", encoding="utf-8")
        (repo / W.DONE).write_text("{}")
        body = b"\x89PNG fixture bytes"
        ts = "20261126000000"
        wire = []
        def urlopen(req, timeout=None):
            url = req.full_url
            url.encode("ascii")  # what http.client does with the request line
            wire.append(url)
            return FakeResponse(body)
        def opener(req, timeout=None):
            url = req.full_url
            url.encode("ascii")
            wire.append(url)
            if url.startswith(W.CDX_API):
                return FakeResponse(json.dumps([["timestamp", "statuscode", "mimetype"],
                                                [ts, "200", "image/png"]]).encode())
            return FakeResponse(body)
        posted = []
        with ExitStack() as stack:
            for name in ("reset_to_origin", "prune_verified_snapshots"):
                stack.enter_context(patch.object(W, name))
            stack.enter_context(patch.object(W, "control_directory", return_value=repo / "control"))
            stack.enter_context(patch.object(W, "AUTH", "LOW fixture:offline"))
            stack.enter_context(patch.object(W, "GAP_S", 0))
            stack.enter_context(patch.object(W.time, "sleep"))
            stack.enter_context(patch.object(W, "commit_and_push", side_effect=lambda r, p, m, redo: redo()))
            # test_wayback_worker replaces W.strict_check at import; use the
            # same wire helpers the real one uses (replay id_ GET + CDX rows).
            def strict(capture):
                ts, original = W.capture_parts(capture)
                return W._raw_get(W.id_url(capture))[0] == 200 and bool(W.cdx_rows(original, ts)), "ok"
            stack.enter_context(patch.object(W, "strict_check", strict))
            stack.enter_context(patch.object(W.urllib.request, "urlopen", side_effect=urlopen))
            stack.enter_context(patch.object(W.OPENER, "open", side_effect=opener))
            stack.enter_context(patch.object(W, "ensure_capacity"))
            stack.enter_context(patch.object(W, "spn2_submit", side_effect=lambda url, force=False: posted.append(url) or {"job_id": "spn2-fixture"}))
            stack.enter_context(patch.object(W, "spn2_status", return_value={"status": "success", "timestamp": ts, "original_url": IRI}))
            stack.enter_context(patch.object(W, "OwnerAdapter", return_value=Mock(prepare=Mock(return_value={"ledger_updates": {}}),
                                                                               protected_snapshot_urls=Mock(return_value=set()))))
            stack.enter_context(patch.object(W, "load_allowed_objects", return_value=set()))
            W.run(repo, 2)
        done = json.loads((repo / W.DONE).read_text(encoding="utf-8"))
        self.assertEqual([IRI], list(done))  # the key stays exactly as queued
        self.assertEqual([IRI], posted)
        self.assertIn(done[IRI]["status"], {"verified", "ok"})
        self.assertTrue(wire and all(u.isascii() for u in wire))

    def test_unsendable_url_in_verify_counts_against_the_row_only(self):
        e = {"status": "ok", "capture": "https://web.archive.org/web/20261120000000/" + IRI}
        with patch.object(W, "verify", side_effect=UnicodeEncodeError("ascii", IRI, 23, 24, "ordinal not in range(128)")):
            self.assertTrue(W.verify_entry(IRI, e))
        self.assertEqual("ok", e["status"])
        self.assertEqual(1, e["verify_tries"])
        self.assertIn("UnicodeEncodeError", e["verify"]["error"])


if __name__ == "__main__":
    unittest.main()
