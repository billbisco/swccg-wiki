#!/usr/bin/env python3
"""Small Git helpers for wiki backup scripts. Never print tokens."""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

_SECRET_RES = [
    re.compile(r"(?i)(authorization:\s*(?:bearer|basic|token)\s+)\S+"),
    re.compile(r"(?i)(extraheader=)[^'\"\s]+(?:\s+[^'\"\s]+)*"),
    re.compile(r"()\bgh[pousr]_[A-Za-z0-9]{10,}"),
    re.compile(r"()\bgithub_pat_[A-Za-z0-9_]{10,}"),
    re.compile(r"(https?://)[^/@\s]+@"),
]


class GitError(RuntimeError):
    pass


def redact(text: str) -> str:
    for rx in _SECRET_RES:
        text = rx.sub(
            lambda m: m.group(1) + "[REDACTED]" + ("@" if m.group(0).endswith("@") else ""),
            text,
        )
    return text


def git(repo: Path, args: list[str], check: bool = True, env: dict | None = None) -> subprocess.CompletedProcess:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(repo),
        env=env,
        capture_output=True,
        text=True,
    )
    if check and proc.returncode != 0:
        raise GitError(
            f"git failed (exit {proc.returncode}): {redact(' '.join(['git', *args]))}\n"
            f"{redact(proc.stderr or '').strip()}"
        )
    return proc


def git_root(path: Path) -> Path:
    path = path.resolve()
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=str(path if path.is_dir() else path.parent),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise GitError(f"not a git checkout: {path}")
    return Path(proc.stdout.strip())


def commit_if_changed(repo: Path, rels: list[str], message: str) -> bool:
    """Stage only rels and commit if the index changed. Returns True if committed."""
    for rel in rels:
        git(repo, ["add", "--", rel])
    diff = git(repo, ["diff", "--cached", "--quiet"], check=False)
    if diff.returncode == 0:
        return False
    git(repo, ["commit", "-m", message])
    return True


def push_head(repo: Path, refspec: str = "HEAD") -> None:
    env = os.environ.copy()
    token = env.get("GH_TOKEN") or env.get("GIT_ASKPASS_TOKEN")
    env["GIT_TERMINAL_PROMPT"] = "0"
    cmd = ["push", "origin", refspec]
    if token:
        cmd = ["-c", f"http.extraheader=AUTHORIZATION: bearer {token}", "push", "origin", refspec]
    git(repo, cmd, env=env)
