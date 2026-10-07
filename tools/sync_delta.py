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
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dump_live import dump_from_tsv, write_index, _merge_index  # noqa: E402


def git(args: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(ROOT),
        check=kw.pop("check", True),
        **kw,
    )


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
    subprocess.check_call(cmd, cwd=str(ROOT), env=env)


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
    missing = dump_from_tsv(tsv, {}, written)
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
        push()
        print("pushed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
