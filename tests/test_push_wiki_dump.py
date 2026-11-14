"""Real-Git regression tests; all repositories and remotes are local fixtures."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import push_wiki_dump as sync


class PushWikiDumpTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / "remote.git"
        subprocess.run(["git", "init", "--bare", "--initial-branch=main", str(self.remote)], check=True, capture_output=True)
        self.worker = self.clone("worker")
        self.write(self.worker, "pages/A.wiki", "original\n")
        self.write(self.worker, "pages/INDEX.tsv", "A\tpages/A.wiki\n")
        self.write(self.worker, "README.md", "original\n")
        self.commit(self.worker, "seed")
        self.run_git(self.worker, "push", "origin", "HEAD:main")
        self.peer = self.clone("peer")

    def clone(self, name):
        repo = self.root / name
        subprocess.run(["git", "-c", "core.autocrlf=false", "clone", str(self.remote), str(repo)], check=True, capture_output=True)
        self.run_git(repo, "config", "user.name", "fixture")
        self.run_git(repo, "config", "user.email", "fixture@example.invalid")
        self.run_git(repo, "config", "core.autocrlf", "false")
        return repo

    def run_git(self, repo, *args):
        result = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def write(self, repo, rel, content):
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    def commit(self, repo, message):
        self.run_git(repo, "add", ".")
        self.run_git(repo, "commit", "-m", message)

    def remote_text(self, path):
        return self.run_git(self.peer, "--git-dir", str(self.remote), "show", "main:" + path)

    def peer_push(self, path="README.md", content="peer change\n"):
        self.write(self.peer, path, content)
        self.commit(self.peer, "peer")
        self.run_git(self.peer, "push", "origin", "HEAD:main")

    def test_no_change_makes_no_commit_or_push(self):
        before = self.run_git(self.worker, "rev-parse", "HEAD")
        result = sync.push_dump(self.worker, retry_seconds=0)
        self.assertFalse(result["changed"])
        self.assertEqual(before, self.run_git(self.worker, "rev-parse", "HEAD"))

    def test_rebases_dump_over_existing_peer_commit_and_keeps_new_page(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        self.write(self.worker, "pages/New.wiki", "new page\n")
        self.peer_push()
        result = sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(result["push_attempts"], 1)
        self.assertEqual(self.remote_text("README.md"), "peer change")
        self.assertEqual(self.remote_text("pages/A.wiki"), "dump")
        self.assertEqual(self.remote_text("pages/New.wiki"), "new page")

    def test_race_between_fetch_and_push_retries_without_losing_peer(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        original = sync.git
        pushed = 0

        def race(repo, *args):
            nonlocal pushed
            if args[0] == "push":
                pushed += 1
                if pushed == 1:
                    self.peer_push("pages/Peer.wiki", "peer page\n")
            return original(repo, *args)

        with patch.object(sync, "git", side_effect=race):
            result = sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(result["push_attempts"], 2)
        self.assertEqual(self.remote_text("pages/Peer.wiki"), "peer page")
        self.assertEqual(self.remote_text("pages/A.wiki"), "dump")

    def test_same_page_conflict_refreshes_live_text_and_keeps_peer_history(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        self.peer_push("pages/A.wiki", "newer peer page\n")
        peer_commit = self.run_git(self.peer, "rev-parse", "HEAD")
        with patch.object(sync, "live_page", return_value="current live page\n") as live:
            result = sync.push_dump(self.worker, retry_seconds=0)
        live.assert_called_once_with("A")
        self.assertEqual(self.remote_text("pages/A.wiki"), "current live page")
        self.run_git(self.worker, "merge-base", "--is-ancestor", peer_commit, result["published_commit"])
        self.assertFalse((self.worker / ".git/rebase-merge").exists())

    def test_same_page_conflict_can_become_no_change_after_live_refresh(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        self.peer_push("pages/A.wiki", "newer peer page\n")
        with patch.object(sync, "live_page", return_value="newer peer page\n"):
            sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/A.wiki"), "newer peer page")
        self.assertFalse((self.worker / ".git/rebase-merge").exists())

    def test_failed_live_refresh_aborts_without_overwriting_either_copy(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        self.peer_push("pages/A.wiki", "newer peer page\n")
        with patch.object(sync, "live_page", side_effect=sync.SyncError("live source unavailable")):
            with self.assertRaisesRegex(sync.SyncError, "live source unavailable"):
                sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/A.wiki"), "newer peer page")
        self.assertEqual((self.worker / "pages/A.wiki").read_text(), "dump\n")
        self.assertFalse((self.worker / ".git/rebase-merge").exists())

    def test_index_conflict_preserves_both_concurrent_additions(self):
        self.write(self.worker, "pages/INDEX.tsv", "A\tpages/A.wiki\nDump\tpages/Dump.wiki\n")
        self.write(self.worker, "pages/Dump.wiki", "dump addition\n")
        self.write(self.peer, "pages/Peer.wiki", "peer addition\n")
        self.peer_push("pages/INDEX.tsv", "A\tpages/A.wiki\nPeer\tpages/Peer.wiki\n")
        sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/INDEX.tsv"), "A\tpages/A.wiki\nDump\tpages/Dump.wiki\nPeer\tpages/Peer.wiki")
        self.assertEqual(self.remote_text("pages/Peer.wiki"), "peer addition")
        self.assertEqual(self.remote_text("pages/Dump.wiki"), "dump addition")

    def test_conflicting_canonical_mapping_fails_closed(self):
        self.write(self.worker, "pages/INDEX.tsv", "A\tpages/Old.wiki\n")
        self.peer_push("pages/INDEX.tsv", "A\tpages/New.wiki\n")
        with self.assertRaisesRegex(sync.SyncError, "canonical page path changed"):
            sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/INDEX.tsv"), "A\tpages/New.wiki")

    def test_exhausted_pushes_are_bounded_and_leave_remote_unchanged(self):
        self.write(self.worker, "pages/A.wiki", "dump\n")
        original = sync.git
        pushes = []

        def reject(repo, *args):
            if args[0] == "push":
                pushes.append(args)
                return subprocess.CompletedProcess(args, 1, "", "rejected")
            return original(repo, *args)

        with patch.object(sync, "git", side_effect=reject):
            with self.assertRaisesRegex(sync.SyncError, "after 3 attempts"):
                sync.push_dump(self.worker, attempts=3, retry_seconds=0)
        self.assertEqual(len(pushes), 3)
        self.assertTrue(all("--force" not in args for args in pushes))
        self.assertEqual(self.remote_text("pages/A.wiki"), "original")
        self.assertEqual((self.worker / "pages/A.wiki").read_text(), "dump\n")

    def test_unrelated_staged_change_is_not_committed(self):
        self.write(self.worker, "README.md", "unrelated\n")
        self.run_git(self.worker, "add", "README.md")
        self.write(self.worker, "pages/A.wiki", "dump\n")
        before = self.run_git(self.worker, "rev-parse", "HEAD")
        with self.assertRaisesRegex(sync.SyncError, "Unrelated staged changes"):
            sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(before, self.run_git(self.worker, "rev-parse", "HEAD"))

    def test_conflict_live_reader_preserves_empty_and_original_newlines(self):
        import dump_public_current
        for text in ("", "original\r\nwithout final newline"):
            response = {"query": {"pages": [{"revisions": [{"slots": {"main": {"content": text}}}]}]}}
            with patch.object(dump_public_current, "request_api", return_value=response):
                self.assertEqual(sync.live_page("A"), text)

    def test_full_export_alias_conflict_keeps_upstream_and_cutoff_payload(self):
        self.write(self.worker, "pages/A.wiki", "old compatibility view\n")
        self.write(self.worker, "pages/by-id/1.wiki", "exact cutoff payload\r\n")
        manifest = {"schema_version": 1, "revision_cutoff": "fixed", "namespace_metadata": [{"sha256": "unchanged"}]}
        self.write(self.worker, "pages/public-current/manifest.json", json.dumps(manifest))
        self.peer_push("pages/A.wiki", "newer upstream compatibility view\n")
        with patch.object(sync, "live_page", side_effect=AssertionError("must not refresh snapshot")):
            sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/A.wiki"), "newer upstream compatibility view")
        self.assertEqual(self.remote_text("pages/by-id/1.wiki"), "exact cutoff payload")
        restored = json.loads(self.remote_text("pages/public-current/manifest.json"))
        self.assertEqual(restored["revision_cutoff"], "fixed")
        self.assertEqual(restored["namespace_metadata"], manifest["namespace_metadata"])
        self.assertEqual(restored["compatibility_alias_conflicts_kept_from_upstream"], ["pages/A.wiki"])

    def test_full_export_numeric_payload_conflict_fails_without_refresh(self):
        self.write(self.worker, "pages/by-id/1.wiki", "base\n")
        self.write(self.worker, "pages/public-current/manifest.json", json.dumps({"schema_version": 1}))
        self.commit(self.worker, "full export base")
        self.run_git(self.worker, "push", "origin", "HEAD:main")
        self.run_git(self.peer, "pull", "--ff-only")
        self.write(self.worker, "pages/by-id/1.wiki", "candidate cutoff\n")
        self.peer_push("pages/by-id/1.wiki", "upstream authoritative\n")
        with patch.object(sync, "live_page", side_effect=AssertionError("must not refresh snapshot")):
            with self.assertRaisesRegex(sync.SyncError, "Authoritative public-export"):
                sync.push_dump(self.worker, retry_seconds=0)
        self.assertEqual(self.remote_text("pages/by-id/1.wiki"), "upstream authoritative")

    def test_full_export_index_union_updates_only_compatibility_digest(self):
        self.write(self.worker, "pages/INDEX.tsv", "A\tpages/A.wiki\nDump\tpages/Dump.wiki\n")
        self.write(self.worker, "pages/Dump.wiki", "dump addition\n")
        manifest = {"schema_version": 1, "revision_cutoff": "fixed", "captured_pages": 2,
                    "namespace_metadata": [{"sha256": "immutable"}]}
        self.write(self.worker, "pages/public-current/manifest.json", json.dumps(manifest))
        self.write(self.peer, "pages/Peer.wiki", "peer addition\n")
        self.peer_push("pages/INDEX.tsv", "A\tpages/A.wiki\nPeer\tpages/Peer.wiki\n")
        sync.push_dump(self.worker, retry_seconds=0)
        restored = json.loads(self.remote_text("pages/public-current/manifest.json"))
        index = self.remote_text("pages/INDEX.tsv") + "\n"
        self.assertEqual(restored["index_sha256"], hashlib.sha256(index.encode()).hexdigest())
        self.assertEqual(restored["compatibility_index_entries"], 3)
        self.assertEqual(restored["captured_pages"], 2)
        self.assertEqual(restored["revision_cutoff"], "fixed")
        self.assertEqual(restored["namespace_metadata"], manifest["namespace_metadata"])

    def test_full_export_canonical_repath_preserves_snapshot_and_upstream_mapping(self):
        self.write(self.worker, "pages/INDEX.tsv", "A\tpages/A.wiki\nDump\tpages/Dump.wiki\n")
        self.write(self.worker, "pages/Dump.wiki", "dump\n")
        manifest = {"schema_version": 1, "revision_cutoff": "fixed", "namespace_metadata": [{"sha256": "immutable"}]}
        self.write(self.worker, "pages/public-current/manifest.json", json.dumps(manifest))
        self.write(self.peer, "pages/Repathed.wiki", "upstream\n")
        self.peer_push("pages/INDEX.tsv", "A\tpages/Repathed.wiki\n")
        sync.push_dump(self.worker, retry_seconds=0)
        restored = json.loads(self.remote_text("pages/public-current/manifest.json"))
        self.assertEqual(restored["compatibility_canonical_overrides"]["A"],
                         {"snapshot": "pages/A.wiki", "upstream": "pages/Repathed.wiki"})
        self.assertEqual(restored["namespace_metadata"], manifest["namespace_metadata"])
        self.assertIn("A\tpages/Repathed.wiki", self.remote_text("pages/INDEX.tsv"))

    def test_full_export_automatic_index_merge_rehashes_compatibility_view(self):
        rows = [f"{chr(65+i)}\tpages/{chr(65+i)}.wiki\n" for i in range(26)]
        self.write(self.worker, "pages/INDEX.tsv", "".join(rows))
        self.commit(self.worker, "long index")
        self.run_git(self.worker, "push", "origin", "HEAD:main")
        self.run_git(self.peer, "pull", "--ff-only")
        dumped = "".join(rows[:4] + ["Dump\tpages/Dump.wiki\n"] + rows[4:])
        self.write(self.worker, "pages/INDEX.tsv", dumped)
        manifest = {"schema_version": 1, "revision_cutoff": "fixed", "index_sha256": hashlib.sha256(dumped.encode()).hexdigest(),
                    "namespace_metadata": [{"sha256": "immutable"}]}
        self.write(self.worker, "pages/public-current/manifest.json", json.dumps(manifest))
        peer_index = "".join(rows[:23] + ["Peer\tpages/Peer.wiki\n"] + rows[23:])
        self.peer_push("pages/INDEX.tsv", peer_index)
        sync.push_dump(self.worker, retry_seconds=0)
        restored = json.loads(self.remote_text("pages/public-current/manifest.json"))
        actual = self.remote_text("pages/INDEX.tsv") + "\n"
        self.assertEqual(restored["index_sha256"], hashlib.sha256(actual.encode()).hexdigest())
        self.assertEqual(restored["namespace_metadata"], manifest["namespace_metadata"])


if __name__ == "__main__":
    unittest.main()
