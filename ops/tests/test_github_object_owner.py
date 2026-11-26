"""GitHub commit/blob pages verified by git object, not HTML bytes (#1377)."""
import hashlib
import io
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
from test_preservation_registration import fixture
from preservation_contracts import validate_source_representation
from preservation_github import (GITHUB_REPRESENTATION, check_public, parse_github_page, raw_url,
                                 validate_github_object)
from preservation_registry import SERVER_OWNER, export_records, object_state, register
from preservation_owner import OwnerAdapter
from preservation_owner_receipts import load_event

COMMIT = "022435b7929e4de26dafbcb1de2ec1d6d04d2153"
OTHER = "ab7441976d996222d5b7235219576492a00bd1e2"
FILE = b"GIF89a exact holotable image"
FILE_SHA = hashlib.sha256(FILE).hexdigest()
PATH = "Images-HT/starwars/ResetDS-Dark/large/fanfare.gif"


def commit_source(ref=COMMIT):
    return {"url": "https://github.com/swccgpc/holotable/commit/" + ref,
            "representation": GITHUB_REPRESENTATION,
            "github_object": {"owner": "swccgpc", "repo": "holotable", "kind": "commit",
                              "ref": ref, "path": None, "commit": COMMIT}}


def blob_source(ref="022435b"):
    return {"url": "https://github.com/swccgpc/holotable/blob/%s/%s" % (ref, PATH),
            "representation": GITHUB_REPRESENTATION,
            "github_object": {"owner": "swccgpc", "repo": "holotable", "kind": "blob", "ref": ref,
                              "path": PATH, "commit": COMMIT, "file_sha256": FILE_SHA,
                              "file_bytes": len(FILE)}}


def page(commit=COMMIT, extra=b""):
    body = b'<html><script>{"oid":"' + commit.encode() + b'"}</script>' + extra + b"</html>"
    return {"status": 200, "sha256": hashlib.sha256(body).hexdigest(), "size": len(body), "body": body}


class ContractTests(unittest.TestCase):
    def test_commit_and_blob_bindings_validate(self):
        for source in (commit_source(), commit_source("022435b"), blob_source(), blob_source(COMMIT)):
            with self.subTest(url=source["url"]):
                self.assertEqual([], validate_github_object(source))
                self.assertEqual([], validate_source_representation(source))

    def test_only_pinned_commit_or_blob_pages_parse(self):
        for url in ("https://github.com/swccgpc/holotable",
                    "https://github.com/swccgpc/holotable/blob/master/" + PATH,
                    "https://github.com/swccgpc/holotable/commits/master/" + PATH,
                    "https://github.com/swccgpc/holotable/commit/022435",
                    "https://github.com/swccgpc/holotable/commit/" + COMMIT + "?diff=split",
                    "https://github.com/swccgpc/holotable/commit/" + COMMIT + "#x",
                    "https://github.com/swccgpc/holotable/commit/" + COMMIT + "/x",
                    "https://github.com/swccgpc/holotable/blob/" + COMMIT,
                    "https://github.com/swccgpc/holotable/blob/" + COMMIT + "/a/../b.gif",
                    "http://github.com/swccgpc/holotable/commit/" + COMMIT,
                    "https://raw.githubusercontent.com/swccgpc/holotable/" + COMMIT + "/" + PATH):
            with self.subTest(url=url):
                self.assertIsNone(parse_github_page(url))

    def test_bindings_must_match_url_and_full_commit(self):
        cases = []
        source = commit_source("022435b"); source["github_object"]["commit"] = OTHER; cases.append(source)
        source = commit_source(); source["github_object"]["commit"] = "022435b"; cases.append(source)
        source = commit_source(); source["github_object"]["repo"] = "other"; cases.append(source)
        source = commit_source(); source["github_object"]["file_sha256"] = FILE_SHA; cases.append(source)
        source = commit_source(); source["primary_url"] = "https://example.org/"; cases.append(source)
        source = blob_source(); source["github_object"].pop("file_sha256"); cases.append(source)
        source = blob_source(); source["github_object"]["path"] = "other.gif"; cases.append(source)
        source = blob_source(); source["github_object"]["extra"] = 1; cases.append(source)
        source = blob_source(); source.pop("github_object"); cases.append(source)
        for source in cases:
            with self.subTest(source=source):
                self.assertTrue(validate_source_representation(source))

    def test_commit_check_needs_200_page_naming_the_full_commit(self):
        source = commit_source("022435b")
        self.assertTrue(check_public(lambda url: page(), source)["matches"])
        self.assertFalse(check_public(lambda url: page(OTHER), source)["matches"])
        self.assertFalse(check_public(lambda url: dict(page(), status=502), source)["matches"])

    def test_blob_check_reads_raw_file_at_full_commit_and_cited_ref(self):
        source = blob_source()
        seen = []
        good = {"status": 200, "sha256": FILE_SHA, "size": len(FILE)}
        def fetch(url):
            seen.append(url)
            return good
        self.assertTrue(check_public(fetch, source)["matches"])
        self.assertEqual([raw_url(source), raw_url(source, "022435b")], seen)
        self.assertTrue(seen[0].startswith("https://raw.githubusercontent.com/swccgpc/holotable/" + COMMIT + "/"))
        def changed(url):
            return good if COMMIT in url else {"status": 200, "sha256": "0" * 64, "size": len(FILE)}
        self.assertFalse(check_public(changed, source)["matches"])


class OwnerTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.lock = io.BytesIO(b"owner test fixture")
        self.control = SimpleNamespace(directory=self.root / "control", state={"mode": "healthy"},
                                       lock=self.lock, done={})
        self.calls, self.commits, self.responses = [], [], {}
        def fetch(url):
            self.calls.append(url)
            return self.responses.get(url, {"status": 404, "sha256": "", "size": 0, "body": b""})
        def commit(repo, paths, message, redo):
            self.commits.append(redo())
        self.worker = SimpleNamespace(ACTIVE_CONTROL=self.control, QUEUE="ops/queue.txt", fetch=fetch,
                                      commit_and_push=commit, snapshot_root=lambda: self.root / "public",
                                      snapshot_file=lambda url: None,
                                      capture_parts=lambda url: ("20261114000000", url.split("/20261114000000/", 1)[1]),
                                      id_url=lambda url: url.replace("/20261114000000/", "/20261114000000id_/"),
                                      strict_check=lambda url: (True, "ok"), VERIFY_GAP_S=0)
        self.registry = self.control.directory / "registry"
        self.allowed = set()

    def add(self, source, *, ready=True):
        request = fixture(title="File:gh.gif", ready=ready)
        request["owner"] = SERVER_OWNER
        # The page backup shares the fixture's backed-up payload hash/size.
        request["source"] = dict(source, sha256=request["subject"]["content_sha256"],
                                 bytes=request["subject"]["bytes"],
                                 checked_evidence=request["source"]["checked_evidence"])
        result = register(self.registry, request)
        self.allowed.add(result["object_id"])
        return request

    def adapter(self, **kwargs):
        return OwnerAdapter(self.worker, self.repo, self.control, self.allowed, work=self.root / "work",
                            observe_max=10, **kwargs)

    def queue(self):
        path = self.repo / "ops/queue.txt"
        return path.read_text().split() if path.exists() else []

    def test_commit_page_with_new_html_bytes_is_queued(self):
        request = self.add(commit_source("022435b"))
        self.assertEqual("ready", object_state(request))
        fresh = page(extra=b"fresh csrf token")
        self.assertNotEqual(request["source"]["sha256"], fresh["sha256"])
        self.responses[request["source"]["url"]] = fresh
        result = self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual(1, result["prepared"])
        self.assertEqual([request["source"]["url"]], self.queue())
        self.assertEqual("queued", load_event(self.registry, request["source"])["state"])

    def test_commit_page_naming_another_commit_is_never_queued(self):
        request = self.add(commit_source("022435b"))
        self.responses[request["source"]["url"]] = page(OTHER)
        self.assertEqual(0, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([], self.commits)
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])

    def test_blob_is_checked_by_raw_file_and_queues_the_page(self):
        request = self.add(blob_source())
        good = {"status": 200, "sha256": FILE_SHA, "size": len(FILE), "body": FILE}
        self.responses[raw_url(request["source"])] = good
        self.responses[raw_url(request["source"], "022435b")] = good
        self.assertEqual(1, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([request["source"]["url"]], self.queue())
        self.assertNotIn(request["source"]["url"], self.calls)

    def test_blob_with_different_raw_file_is_never_queued(self):
        request = self.add(blob_source(COMMIT))
        self.responses[raw_url(request["source"])] = {"status": 200, "sha256": "0" * 64, "size": len(FILE)}
        self.assertEqual(0, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        self.assertEqual([], self.queue())
        self.assertEqual("needs_attention", load_event(self.registry, request["source"])["state"])

    def test_awaiting_stage_github_object_is_advanced_by_the_owner_check(self):
        request = self.add(commit_source(), ready=False)
        self.assertEqual("awaiting_stage", object_state(request))
        self.responses[request["source"]["url"]] = page()
        self.assertEqual(1, self.adapter().prepare(time.monotonic() + 300)["prepared"])
        row = export_records(self.registry)["objects"][0]
        self.assertTrue(row["readiness"]["ready"])
        self.assertEqual(COMMIT, row["source"]["github_object"]["commit"])

    def capture(self, request, replay):
        capture = "https://web.archive.org/web/20261114000000/" + request["source"]["url"]
        self.responses[self.worker.id_url(capture)] = replay
        self.control.done[request["source"]["url"]] = {"status": "verified", "capture": capture}
        return capture

    def test_capture_replay_naming_the_commit_is_verified(self):
        request = self.add(commit_source("022435b"))
        self.capture(request, page(extra=b"archived render"))
        self.adapter().finish(time.monotonic() + 300)
        event = load_event(self.registry, request["source"])
        self.assertEqual("verified", event["state"])
        self.assertEqual("github_commit_oid", event["verification"]["method"])
        self.assertEqual(COMMIT, event["verification"]["commit"])

    def test_capture_replay_without_the_commit_is_not_verified(self):
        request = self.add(commit_source())
        self.capture(request, page(OTHER))
        self.adapter().finish(time.monotonic() + 300)
        self.assertNotEqual("verified", (load_event(self.registry, request["source"]) or {}).get("state"))

    def test_existing_capture_is_verified_during_prepare_without_a_resave(self):
        request = self.add(commit_source())
        self.responses[request["source"]["url"]] = page()
        self.capture(request, page(extra=b"older render"))
        self.adapter().prepare(time.monotonic() + 300)
        self.assertEqual([], self.queue())
        self.assertEqual("verified", load_event(self.registry, request["source"])["state"])


if __name__ == "__main__":
    unittest.main()
