"""Git helpers for the unattended VPS jobs (wayback worker, nightly backup).

The VPS clones are job-only working copies: they never hold work of their own, so each run
starts from origin/main and a rejected push is retried by re-applying the job's change on top
of the new origin/main. Auth is a per-repo GitHub deploy key (GIT_SSH_COMMAND), set by the
systemd unit — never a personal token.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Callable


def git(repo: Path, *args: str, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=str(repo), check=check, text=True,
        stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )


def reset_to_origin(repo: Path) -> None:
    git(repo, "fetch", "-q", "origin", "main")
    git(repo, "reset", "-q", "--hard", "origin/main")


def commit_and_push(repo: Path, paths: list[str], message: str, redo: Callable[[], list[str]], tries: int = 4) -> bool:
    """Stage paths, commit, push. On a rejected push: reset to the new origin/main, call redo()
    (which re-writes the job's files and returns the paths to stage) and try again."""
    for attempt in range(tries):
        if attempt:
            reset_to_origin(repo)
            paths = redo()
        if not paths:
            return False
        git(repo, "add", "--sparse", "--", *paths)
        if git(repo, "diff", "--cached", "--quiet", check=False).returncode == 0:
            return False
        git(repo, "-c", "user.name=swccg-ops (VPS)", "-c", "user.email=swccg-ops@wiki.swccg.com",
            "commit", "-q", "-m", message)
        if git(repo, "push", "-q", "origin", "HEAD:main", check=False).returncode == 0:
            return True
    raise RuntimeError(f"push to {repo} rejected {tries} times")
