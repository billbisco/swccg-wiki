#!/usr/bin/env python3
"""Commit a pages/ dump and push without overwriting concurrent Git writers.

The weekly dump can take minutes. Other producers may advance main meanwhile,
so fetch/rebase before each bounded push attempt. A content conflict is a hard
stop: leave the local snapshot commit intact for inspection instead of choosing
either writer's page text automatically. This helper never accesses the wiki or
Archive.org, and does not change the dump's namespace/content coverage.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import time


class SyncError(RuntimeError):
    pass


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["GIT_EDITOR"] = "true"
    return subprocess.run(
        ["git", *args], cwd=repo, env=env, capture_output=True,
        text=True, encoding="utf-8", errors="replace",
    )


def checked(repo: Path, *args: str) -> subprocess.CompletedProcess:
    result = git(repo, *args)
    if result.returncode:
        # Do not echo Git output: remote URLs or auth configuration may contain
        # credentials. The operation name and exit status are enough to diagnose
        # this workflow; the retained local commit identifies the snapshot.
        raise SyncError(f"git {args[0]} failed (exit {result.returncode})")
    return result


def push_dump(repo: Path, attempts: int = 5, retry_seconds: float = 3) -> dict:
    if not 1 <= attempts <= 10:
        raise ValueError("attempts must be between 1 and 10")
    if retry_seconds < 0:
        raise ValueError("retry_seconds cannot be negative")
    # Only this ephemeral workflow clone is supported. Refuse to sweep an
    # unrelated staged change into the generated backup commit.
    staged = checked(repo, "diff", "--cached", "--name-only", "-z").stdout
    if any(not path.startswith("pages/") for path in staged.split("\0") if path):
        raise SyncError("Unrelated staged changes; refusing to commit them")
    checked(repo, "add", "--", "pages")
    changed = git(repo, "diff", "--cached", "--quiet")
    if changed.returncode == 0:
        print("No wikitext changes", flush=True)
        return {"changed": False, "push_attempts": 0}
    if changed.returncode != 1:
        raise SyncError("Could not inspect staged dump changes")
    checked(repo, "commit", "-m", "Sync encyclopedia wikitext from wiki.swccg.com")
    snapshot = checked(repo, "rev-parse", "HEAD").stdout.strip()
    print(f"Dump snapshot commit: {snapshot}", flush=True)
    for attempt in range(1, attempts + 1):
        checked(repo, "fetch", "--no-tags", "origin", "+refs/heads/main:refs/remotes/origin/main")
        rebased = git(repo, "rebase", "refs/remotes/origin/main")
        if rebased.returncode:
            checked(repo, "rebase", "--abort")
            raise SyncError(
                "Concurrent content conflict; no push performed. "
                f"Local dump snapshot retained at {snapshot}. Rerun from a fresh live dump."
            )
        pushed = git(repo, "push", "origin", "HEAD:refs/heads/main")
        if pushed.returncode == 0:
            print(f"Pushed dump after {attempt} attempt(s)", flush=True)
            return {"changed": True, "push_attempts": attempt, "snapshot_commit": snapshot}
        print(f"Push attempt {attempt}/{attempts} rejected or failed; refreshing main", flush=True)
        if attempt < attempts:
            time.sleep(retry_seconds)
    raise SyncError(
        f"Push failed after {attempts} attempts; no force push used. "
        f"Local dump snapshot retained at {snapshot}."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--attempts", type=int, default=5)
    parser.add_argument("--retry-seconds", type=float, default=3)
    args = parser.parse_args()
    try:
        push_dump(args.repo, args.attempts, args.retry_seconds)
    except (SyncError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
