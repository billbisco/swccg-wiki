"""Offline real-Git fixtures for the shared backup/Wayback checkout contract."""
import os
import subprocess
import sys
import tempfile
import time
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gitsync
import nightly_backup


class SharedCheckoutTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.origin = self.root / "origin.git"
        self.repo = self.root / "job"
        self.run_git(self.root, "init", "--bare", "--initial-branch=main", str(self.origin))
        self.run_git(self.root, "init", "--initial-branch=main", str(self.repo))
        self.run_git(self.repo, "config", "user.name", "offline fixture")
        self.run_git(self.repo, "config", "user.email", "fixture@example.invalid")
        self.run_git(self.repo, "config", "core.autocrlf", "false")
        (self.repo / "page.wiki").write_text("before\n", encoding="utf-8")
        self.run_git(self.repo, "add", "page.wiki")
        self.run_git(self.repo, "commit", "-qm", "fixture")
        self.run_git(self.repo, "remote", "add", "origin", str(self.origin))
        self.run_git(self.repo, "push", "-qu", "origin", "main")

    @staticmethod
    def run_git(repo, *args):
        return subprocess.check_output(["git", *args], cwd=repo, stderr=subprocess.STDOUT, text=True)

    def child_lock(self):
        ready, release = self.root / "ready", self.root / "release"
        program = (
            "import sys,time;from pathlib import Path;sys.path.insert(0,sys.argv[1]);"
            "from gitsync import repository_write_lock;"
            "\nwith repository_write_lock(Path(sys.argv[2])):"
            "\n Path(sys.argv[3]).write_text('ready')"
            "\n end=time.monotonic()+15"
            "\n while not Path(sys.argv[4]).exists() and time.monotonic()<end:time.sleep(.02)"
        )
        process = subprocess.Popen([sys.executable, "-c", program,
                                    str(Path(gitsync.__file__).parent), str(self.repo), str(ready), str(release)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        deadline = time.monotonic() + 10
        while not ready.exists() and time.monotonic() < deadline and process.poll() is None:
            time.sleep(.02)
        if not ready.exists():
            process.kill()
            output = process.communicate()
            self.fail("fixture lock holder did not start: " + repr(output))
        return process, release

    def test_cross_process_contention_times_out_without_resetting_partial_state(self):
        journal = self.root / "accepted-job.json"
        journal.write_text('{"job":"accepted"}', encoding="utf-8")
        process, release = self.child_lock()
        try:
            with self.assertRaises(gitsync.RepositoryBusy):
                with gitsync.repository_write_lock(self.repo, timeout=.05):
                    self.fail("concurrent writer acquired the lock")
            self.assertEqual("before\n", (self.repo / "page.wiki").read_text(encoding="utf-8"))
            self.assertEqual('{"job":"accepted"}', journal.read_text(encoding="utf-8"))
        finally:
            release.write_text("release", encoding="utf-8")
            process.communicate(timeout=10)
        self.assertEqual(0, process.returncode)
        with gitsync.repository_write_lock(self.repo, timeout=.1):
            pass

    def test_first_write_is_redo_under_lock_and_remote_contains_exact_payload(self):
        calls = []
        def write():
            calls.append("write")
            # A separate process proves that the callback owns the Git lock.
            program = "from pathlib import Path;from gitsync import repository_write_lock,RepositoryBusy\ntry:\n with repository_write_lock(Path(" + repr(str(self.repo)) + "),timeout=.02):raise SystemExit(9)\nexcept RepositoryBusy:pass"
            env = dict(os.environ, PYTHONPATH=str(Path(gitsync.__file__).parent))
            result = subprocess.run([sys.executable, "-c", program], env=env, capture_output=True)
            self.assertEqual(0, result.returncode, result.stderr)
            (self.repo / "page.wiki").write_text("exact snapshot\n", encoding="utf-8")
            return ["page.wiki"]
        self.assertTrue(gitsync.commit_and_push(self.repo, [], "backup fixture", write))
        self.assertEqual(["write"], calls)
        self.assertEqual("exact snapshot\n", self.run_git(self.origin, "show", "main:page.wiki"))

    def test_rejected_push_replays_fresh_state_and_keeps_other_job_and_journal(self):
        other = self.root / "other"
        self.run_git(self.root, "clone", "-q", str(self.origin), str(other))
        self.run_git(other, "config", "user.name", "offline fixture")
        self.run_git(other, "config", "user.email", "fixture@example.invalid")
        journal = self.root / "accepted-job.json"
        journal.write_text("durable accepted state", encoding="utf-8")
        real_git = gitsync.git
        pushes = []
        writes = []
        def git(repo, *args, **kwargs):
            if args[:2] == ("push", "-q") and not pushes:
                pushes.append(True)
                (other / "done.json").write_text('{"preserved":"other job"}', encoding="utf-8")
                self.run_git(other, "add", "done.json")
                self.run_git(other, "commit", "-qm", "other job")
                self.run_git(other, "push", "-q", "origin", "main")
            return real_git(repo, *args, **kwargs)
        def write():
            writes.append(True)
            (self.repo / "page.wiki").write_text("backup after retry\n", encoding="utf-8")
            return ["page.wiki"]
        with patch.object(gitsync, "git", side_effect=git):
            self.assertTrue(gitsync.commit_and_push(self.repo, [], "retry fixture", write))
        self.assertEqual(2, len(writes))
        self.assertIn("other job", self.run_git(self.origin, "show", "main:done.json"))
        self.assertEqual("backup after retry\n", self.run_git(self.origin, "show", "main:page.wiki"))
        self.assertEqual("durable accepted state", journal.read_text(encoding="utf-8"))


class NightlyTransactionTests(unittest.TestCase):
    def test_page_writer_has_no_prewrite_before_locked_callback(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            written = []
            fake = SimpleNamespace(
                INDEX=repo / "INDEX.tsv", index_existing=lambda: {},
                dump_from_tsv=lambda tsv, existing, rows: rows.append(("Example", "pages/Example.wiki")),
                _merge_index=lambda rows, keep_old: rows,
                write_index=lambda rows: written.append(rows),
            )
            def commit(repo, paths, message, redo):
                self.assertEqual([], paths)
                self.assertEqual([], written, "page text was written before the Git transaction")
                self.assertFalse((repo / ".nightly-titles.tsv").exists())
                self.assertEqual(["pages/Example.wiki", "pages/INDEX.tsv"], redo())
                return True
            with patch.dict(sys.modules, dump_live=fake), patch.object(nightly_backup, "commit_and_push", side_effect=commit):
                self.assertEqual(1, nightly_backup.backup_pages(repo, {"Example"}))
            self.assertEqual(1, len(written))

    def test_git_failure_keeps_nightly_checkpoint_for_same_window_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "state.json"
            previous = '{"last":"2026-11-13T00:00:00Z"}'
            state.write_text(previous, encoding="utf-8")
            argv = ["nightly_backup.py", str(root), str(root), "--state", str(state)]
            with patch.object(sys, "argv", argv), patch.object(nightly_backup, "changed_since", return_value=({"Example"}, set())), patch.object(nightly_backup, "backup_pages", side_effect=gitsync.RepositoryBusy("busy")):
                with self.assertRaises(gitsync.RepositoryBusy):
                    nightly_backup.main()
            self.assertEqual(previous, state.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
