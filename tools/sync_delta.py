#!/usr/bin/env python3
"""Dump leftover/apply TSV titles from wiki.swccg.com into this clone and commit.

Run from anywhere; writes into the clone that contains this script
(C:\\Users\\gythe\\.grok\\swccg-wiki). After live QA:

    python tools/sync_delta.py --from-tsv path/to/y2012-yavin-xerox-delta.tsv --push

--push needs GH_TOKEN or GIT_ASKPASS_TOKEN in the environment (leftover.token()).
Do not print those values. Do not git status the whole tree.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dump_live import INDEX, dump_from_tsv, load_tsv, write_index, _merge_index  # noqa: E402

_SECRET_RES = [
    re.compile(r"(?i)(authorization:\s*(?:bearer|basic|token)\s+)\S+"),
    re.compile(r"(?i)(extraheader=)[^'\"\s]+(?:\s+[^'\"\s]+)*"),
    re.compile(r"()\bgh[pousr]_[A-Za-z0-9]{10,}"),
    re.compile(r"()\bgithub_pat_[A-Za-z0-9_]{10,}"),
    re.compile(r"(https?://)[^/@\s]+@"),
]


def redact(text: str) -> str:
    """Strip auth headers and token-looking strings from text."""
    for rx in _SECRET_RES:
        text = rx.sub(lambda m: m.group(1) + "[REDACTED]" + ("@" if m.group(0).endswith("@") else ""), text)
    return text


class GitError(RuntimeError):
    pass


def _run(cmd: list[str], env: dict | None = None, check: bool = True) -> subprocess.CompletedProcess:
    """Run git; on failure raise GitError with redacted command/stderr only."""
    proc = subprocess.run(cmd, cwd=str(ROOT), env=env, capture_output=True, text=True)
    if proc.stdout:
        sys.stdout.write(redact(proc.stdout))
    if check and proc.returncode != 0:
        safe_cmd = redact(" ".join(cmd))
        raise GitError(
            f"git failed (exit {proc.returncode}): {safe_cmd}\n{redact(proc.stderr or '').strip()}"
        )
    return proc


def git(args: list[str], **kw) -> subprocess.CompletedProcess:
    return _run(["git", *args], check=kw.pop("check", True))


def canonical_tsv(tsv: Path) -> Path:
    """Prefer the path INDEX.tsv already records for a title over the TSV's path,
    so hand-written apply TSVs can't create duplicate copies of a page."""
    known: dict[str, str] = {}
    if INDEX.exists():
        for line in INDEX.read_text(encoding="utf-8").splitlines():
            if "\t" in line:
                t, rel = line.split("\t", 1)
                known[t] = rel
    rows = []
    for title, rel in load_tsv(tsv):
        if title in known and known[title] != rel:
            print(f"path for {title!r}: using INDEX {known[title]} (TSV said {rel})")
            rel = known[title]
        rows.append(f"{title}\t{rel}\n")
    fd, out = tempfile.mkstemp(suffix=".tsv")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.writelines(rows)
    return Path(out)


def push() -> None:
    env = os.environ.copy()
    token = env.get("GH_TOKEN") or env.get("GIT_ASKPASS_TOKEN")
    env["GIT_TERMINAL_PROMPT"] = "0"
    cmd = ["git", "push", "origin", "HEAD"]
    if token:
        cmd = [
            "git",
            "-c",
            f"http.extraheader=AUTHORIZATION: bearer {token}",
            "push",
            "origin",
            "HEAD",
        ]
    _run(cmd, env=env)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-tsv", type=Path, required=True)
    ap.add_argument("--push", action="store_true")
    ap.add_argument(
        "--message",
        default="Sync leftover dest titles from wiki.swccg.com",
    )
    args = ap.parse_args()
    tsv = args.from_tsv.expanduser().resolve()
    if not tsv.is_file():
        print(f"missing TSV {tsv}", file=sys.stderr)
        return 1
    written: list[tuple[str, str]] = []
    missing = dump_from_tsv(canonical_tsv(tsv), {}, written)
    write_index(_merge_index(written, keep_old=True))
    if missing:
        print("MISSING " + "; ".join(missing), file=sys.stderr)
        return 2
    rels = sorted({rel for _, rel in written} | {"pages/INDEX.tsv"})
    for rel in rels:
        git(["add", "--", rel])
    diff = git(["diff", "--cached", "--quiet"], check=False)
    if diff.returncode == 0:
        print(f"no GitHub changes for {len(written)} titles")
        return 0
    git(["commit", "-m", args.message])
    print(f"committed {len(written)} titles")
    if args.push:
        try:
            push()
        except GitError as exc:
            print(redact(str(exc)), file=sys.stderr)
            return 3
        print("pushed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
