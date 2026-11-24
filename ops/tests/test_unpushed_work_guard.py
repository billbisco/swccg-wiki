"""Local Git fixtures for the unpushed-work guard (swccg-guild/work#1323)."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ops"))
sys.path.insert(0, str(ROOT / "tools"))
import unpushed_work_guard as guard  # noqa: E402


def run(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(repo), check=check, capture_output=True, text=True)


def init_pair() -> tuple[Path, Path]:
    tmp = Path(tempfile.mkdtemp(prefix="unpushed-guard-"))
    origin = tmp / "origin.git"
    clone = tmp / "clone"
    run(tmp, "init", "--bare", str(origin))
    run(tmp, "clone", str(origin), str(clone))
    run(clone, "config", "user.email", "guard@example.test")
    run(clone, "config", "user.name", "Guard Test")
    (clone / "README").write_text("main\n", encoding="utf-8")
    run(clone, "add", "README")
    run(clone, "commit", "-m", "initial")
    # Ensure main is the branch name
    run(clone, "branch", "-M", "main")
    run(clone, "push", "-u", "origin", "main")
    return origin, clone


class UnpushedWorkGuardTest(unittest.TestCase):
    def test_ahead_commits_pushed_to_safety_branch_not_main(self):
        origin, clone = init_pair()
        (clone / "extra.txt").write_text("ahead\n", encoding="utf-8")
        run(clone, "add", "extra.txt")
        run(clone, "commit", "-m", "local only")
        report = guard.process(clone, apply=True, stale_after=24 * 3600)
        self.assertTrue(report["safety_branch"].startswith("safety/unpushed-"))
        self.assertTrue(any("ahead commit" in a for a in report["actions"]))
        self.assertEqual(run(clone, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip(), "main")
        # Safety branch exists on origin; main did not move
        remote_main = run(clone, "rev-parse", "origin/main").stdout.strip()
        local_head = run(clone, "rev-parse", "HEAD").stdout.strip()
        self.assertNotEqual(remote_main, local_head)
        run(clone, "ls-remote", "--heads", "origin", report["safety_branch"])
        # confirm the safety ref is on the origin
        refs = run(origin, "show-ref").stdout
        self.assertIn(report["safety_branch"], refs)
        self.assertNotIn("extra.txt", run(clone, "show", "origin/main:README", check=False).stdout)

    def test_untracked_files_committed_on_safety_branch_and_checkout_restored(self):
        origin, clone = init_pair()
        files = clone / "files"
        files.mkdir()
        (files / "photo.jpg").write_bytes(b"fake-jpeg")
        report = guard.process(clone, apply=True, stale_after=24 * 3600)
        self.assertEqual(run(clone, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip(), "main")
        self.assertTrue(report["safety_branch"].startswith("safety/unpushed-"))
        self.assertTrue(any("untracked" in a for a in report["actions"]))
        # File lives on the safety branch, not on main
        run(clone, "fetch", "origin")
        listed = run(clone, "ls-tree", "-r", "--name-only", report["safety_branch"]).stdout
        self.assertIn("files/photo.jpg", listed)
        main_listed = run(clone, "ls-tree", "-r", "--name-only", "origin/main").stdout
        self.assertNotIn("files/photo.jpg", main_listed)

    def test_safety_branch_is_not_mutated(self):
        origin, clone = init_pair()
        run(clone, "checkout", "-b", "safety/manpc-wiki-files-wip-20261124-1321")
        (clone / "files").mkdir()
        (clone / "files" / "new.bin").write_bytes(b"x")
        report = guard.process(clone, apply=True, stale_after=1)
        self.assertIn("in-flight safety branch", report["skipped"] or "")
        self.assertEqual(report["safety_branch"], None)
        self.assertEqual(
            run(clone, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip(),
            "safety/manpc-wiki-files-wip-20261124-1321",
        )
        # Still untracked; nothing committed
        status = run(clone, "status", "--porcelain", "--untracked-files=all").stdout
        self.assertTrue("files/new.bin" in status or "files/" in status, status)
        # Nothing was committed on the in-flight branch
        self.assertEqual(
            run(clone, "rev-parse", "HEAD").stdout.strip(),
            run(clone, "rev-parse", "origin/main").stdout.strip(),
        )

    def test_dirty_tracked_files_are_not_committed(self):
        origin, clone = init_pair()
        (clone / "README").write_text("edited\n", encoding="utf-8")
        report = guard.process(clone, apply=True, stale_after=24 * 3600)
        self.assertTrue(any("dirty tracked" in a for a in report["actions"]))
        self.assertEqual(run(clone, "rev-parse", "HEAD", "origin/main").stdout.split()[0],
                         run(clone, "rev-parse", "origin/main").stdout.strip())
        self.assertIn("README", run(clone, "status", "--porcelain").stdout)

    def test_index_lock_skips_mutation(self):
        origin, clone = init_pair()
        (clone / "files").mkdir()
        (clone / "files" / "a.bin").write_bytes(b"a")
        lock = clone / ".git" / "index.lock"
        lock.write_text("", encoding="utf-8")
        try:
            report = guard.process(clone, apply=True, stale_after=1)
        finally:
            lock.unlink(missing_ok=True)
        self.assertTrue((report["skipped"] or "").startswith("lock:"))
        self.assertEqual(report["safety_branch"], None)

    def test_stale_untracked_sets_stale_flag(self):
        origin, clone = init_pair()
        files = clone / "files"
        files.mkdir()
        photo = files / "old.jpg"
        photo.write_bytes(b"old")
        old = time.time() - 48 * 3600
        os.utime(photo, (old, old))
        report = guard.process(clone, apply=False, stale_after=24 * 3600)
        self.assertTrue(report["stale"])
        self.assertEqual(report["untracked"], 1)
        self.assertIsNone(report["safety_branch"])


if __name__ == "__main__":
    unittest.main()
