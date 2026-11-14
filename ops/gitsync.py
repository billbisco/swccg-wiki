"""Git helpers for the unattended VPS jobs (wayback worker, nightly backup).

The VPS clones are job-only working copies: they never hold work of their own, so each run
starts from origin/main and a rejected push is retried by re-applying the job's change on top
of the new origin/main. Auth is a per-repo GitHub deploy key (GIT_SSH_COMMAND), set by the
systemd unit — never a personal token.
"""
from __future__ import annotations

import os
import contextlib
import errno
import subprocess
import time
from pathlib import Path
from typing import Callable


def git(repo: Path, *args: str, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=str(repo), check=check, text=True,
        stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )


class RepositoryBusy(RuntimeError):
    """Another existing job owns the shared checkout; no checkpoint may advance."""


@contextlib.contextmanager
def repository_write_lock(repo: Path, timeout: float = 120):
    """Coordinate all tracked writes in the shared job checkout, across processes.

    This short lock is independent of the archive submission owner. Never hold
    it during archive-service waits. It also covers worktrees sharing Git data.
    """
    common = git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir", capture=True).stdout.strip()
    path = Path(common) / "swccg-repository-write.lock"
    with path.open("a+b") as stream:
        if stream.tell() == 0:
            stream.write(b"0")
            stream.flush()
        deadline = time.monotonic() + timeout
        while True:
            stream.seek(0)
            try:
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError as error:
                if error.errno not in (errno.EACCES, errno.EAGAIN, errno.EDEADLK):
                    raise
                if time.monotonic() >= deadline:
                    raise RepositoryBusy("shared repository writer is busy; retry without advancing state") from None
                time.sleep(min(0.1, max(0, deadline - time.monotonic())))
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


def _reset_to_origin_locked(repo: Path) -> None:
    git(repo, "fetch", "-q", "origin", "main")
    git(repo, "reset", "-q", "--hard", "origin/main")


def reset_to_origin(repo: Path) -> None:
    with repository_write_lock(repo):
        _reset_to_origin_locked(repo)


def commit_and_push(repo: Path, paths: list[str], message: str, redo: Callable[[], list[str]], tries: int = 4) -> bool:
    """Reset, write, commit and push within one shared-checkout transaction.

    ``paths`` remains for caller compatibility, but ``redo`` supplies the actual
    write set on EVERY attempt. Callers must not write tracked files beforehand.
    Accepted archive-job journals and registration inboxes stay outside Git.
    """
    with repository_write_lock(repo):
        for attempt in range(tries):
            _reset_to_origin_locked(repo)
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
