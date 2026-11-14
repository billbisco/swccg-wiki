#!/usr/bin/env python3
"""Commit a pages/ dump and push without overwriting concurrent Git writers.

The weekly dump can take minutes. Other producers may advance main meanwhile,
so fetch/rebase before each bounded push attempt. Conflicting page text is read
again from the live wiki rather than choosing either Git writer's stale text.
Unknown paths and ambiguous mappings fail closed. Archive.org is never accessed;
the dump's existing namespace/content coverage is unchanged.
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


def index_rows(text: str) -> dict[str, str]:
    rows = {}
    for line in text.splitlines():
        if not line:
            continue
        title, separator, path = line.partition("\t")
        if not separator or not title or not path.startswith("pages/") or ".." in Path(path).parts:
            raise SyncError("Unsafe or malformed page index mapping")
        if title in rows and rows[title] != path:
            raise SyncError("Ambiguous page index mapping")
        rows[title] = path
    return rows


def live_page(title: str) -> str:
    # Reuse the legacy export's API and text normalization. It only contacts
    # wiki.swccg.com; no preservation/provider calls are made by this module.
    from dump_live import api, page_text

    response = api({"action": "query", "titles": title, "prop": "revisions",
                    "rvprop": "content", "rvslots": "main"})
    pages = response.get("query", {}).get("pages", [])
    if len(pages) != 1 or (text := page_text(pages[0])) is None:
        raise SyncError("Conflicting page could not be read from the live wiki")
    return text


def refresh_conflicts(repo: Path, paths: list[str], snapshot: str, read_live=None) -> None:
    """Resolve only known generated files, using current live text and a union index.

    The upstream commits remain parents of the rebased backup. For INDEX.tsv,
    retain concurrent additions instead of replacing it with the older full dump.
    A title changing its canonical path needs manual reconciliation, not a guess.
    """
    read_live = read_live or live_page
    remote = index_rows(checked(repo, "show", "refs/remotes/origin/main:pages/INDEX.tsv").stdout)
    dumped = index_rows(checked(repo, "show", f"{snapshot}:pages/INDEX.tsv").stdout)
    for title in remote.keys() & dumped.keys():
        if remote[title] != dumped[title]:
            raise SyncError("Concurrent canonical page path changed; refusing automatic resolution")
    merged = {**dumped, **remote}
    by_path: dict[str, list[str]] = {}
    for title, path in merged.items():
        by_path.setdefault(path, []).append(title)
    updates = {}
    for path in paths:
        if path == "pages/INDEX.tsv":
            updates[path] = "".join(f"{title}\t{merged[title]}\n" for title in sorted(merged, key=str.casefold))
        elif path.startswith("pages/") and path.endswith(".wiki") and len(by_path.get(path, [])) == 1:
            updates[path] = read_live(by_path[path][0])
        else:
            raise SyncError("Unknown or ambiguous conflicting dump path; refusing automatic resolution")
    for path, text in updates.items():
        destination = repo / path
        if destination.is_symlink() or not destination.resolve().is_relative_to(repo.resolve()):
            raise SyncError("Conflicting dump path leaves the repository")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8", newline="\n")
        checked(repo, "add", "--", path)
    print(f"Refreshed {len(paths)} conflicting generated file(s) from live wiki/index mappings", flush=True)


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
            conflicts = checked(repo, "diff", "--name-only", "--diff-filter=U", "-z").stdout
            paths = [path for path in conflicts.split("\0") if path]
            try:
                if not paths:
                    raise SyncError(f"Rebase failed (exit {rebased.returncode}) without unresolved content paths")
                refresh_conflicts(repo, paths, snapshot)
                remaining = git(repo, "diff", "--cached", "--quiet")
                if remaining.returncode not in (0, 1):
                    raise SyncError("Could not inspect refreshed dump changes")
                checked(repo, "rebase", "--skip" if remaining.returncode == 0 else "--continue")
            except Exception as exc:
                aborted = git(repo, "rebase", "--abort")
                if aborted.returncode:
                    raise SyncError("Rebase failed and could not be aborted; no push performed") from exc
                raise SyncError(f"{exc}; no push performed. Local dump snapshot: {snapshot}") from exc
        pushed = git(repo, "push", "origin", "HEAD:refs/heads/main")
        if pushed.returncode == 0:
            current = checked(repo, "rev-parse", "HEAD").stdout.strip()
            print(f"Published dump commit: {current}", flush=True)
            print(f"Pushed dump after {attempt} attempt(s)", flush=True)
            return {"changed": True, "push_attempts": attempt, "snapshot_commit": snapshot, "published_commit": current}
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
