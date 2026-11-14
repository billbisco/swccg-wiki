#!/usr/bin/env python3
"""Commit a pages/ dump and push without overwriting concurrent Git writers.

The weekly dump can take minutes. Other producers may advance main meanwhile,
so fetch/rebase before each bounded push attempt. Legacy page conflicts can be
read again from the wiki. Full exports keep upstream compatibility views while
their authoritative payload/metadata tree must remain exactly unchanged.
Unknown paths fail closed. Archive.org is never accessed by this helper.
"""
from __future__ import annotations

import argparse
import hashlib
import json
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


def index_rows(text: str, repo: Path | None = None) -> dict[str, str]:
    rows = {}
    root = repo.resolve() if repo is not None else None
    for line in text.splitlines():
        if not line:
            continue
        title, separator, path = line.partition("\t")
        path = path.replace("\\", "/")
        if not separator or not title or not path.startswith("pages/") or ".." in Path(path).parts:
            raise SyncError("Unsafe or malformed page index mapping")
        if path.casefold() == "pages/public-current" or path.casefold().startswith("pages/public-current/"):
            raise SyncError("Canonical INDEX mapping enters reserved public-current storage")
        if root is not None:
            resolved = (root / path).resolve()
            if not resolved.is_relative_to(root):
                raise SyncError("Canonical INDEX mapping leaves repository")
            portable = resolved.relative_to(root).as_posix().casefold()
            if not portable.startswith("pages/") or portable.startswith("pages/public-current/"):
                raise SyncError("Canonical INDEX mapping enters reserved storage or leaves pages")
        if title in rows and rows[title] != path:
            raise SyncError("Ambiguous page index mapping")
        rows[title] = path
    return rows


def live_page(title: str) -> str:
    # This refresh only changes compatibility aliases; authoritative numeric
    # payloads and cutoff metadata belong to the completed public exporter.
    from dump_public_current import request_api

    response = request_api({"action": "query", "titles": title, "prop": "revisions",
                    "rvprop": "content", "rvslots": "main"})
    pages = response.get("query", {}).get("pages", [])
    revisions = pages[0].get("revisions", []) if len(pages) == 1 else []
    if len(revisions) != 1 or "texthidden" in revisions[0]:
        raise SyncError("Conflicting page could not be read from the live wiki")
    slot = revisions[0].get("slots", {}).get("main", {})
    text = slot.get("content") if "content" in slot else revisions[0].get("content")
    if not isinstance(text, str) or "texthidden" in slot:
        raise SyncError("Conflicting page could not be read from the live wiki")
    return text


def refresh_conflicts(repo: Path, paths: list[str], snapshot: str, read_live=None) -> None:
    """Resolve known compatibility views, preserving the authoritative snapshot.

    The upstream commits remain parents of the rebased backup. For INDEX.tsv,
    retain concurrent additions instead of replacing it with the older full dump.
    A title changing its canonical path needs manual reconciliation, not a guess.
    """
    read_live = read_live or live_page
    manifest_path = repo / "pages/public-current/manifest.json"
    full_manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
    if full_manifest is not None and full_manifest.get("schema_version") != 1:
        raise SyncError("Unknown full export manifest; refusing automatic resolution")
    if any(path.startswith("pages/public-current/") for path in paths):
        raise SyncError("Authoritative public-export payload/metadata conflict; rerun the full exporter")
    remote = index_rows(checked(repo, "show", "refs/remotes/origin/main:pages/INDEX.tsv").stdout, repo)
    dumped = index_rows(checked(repo, "show", f"{snapshot}:pages/INDEX.tsv").stdout, repo)
    canonical_overrides = {}
    for title in remote.keys() & dumped.keys():
        if remote[title] != dumped[title]:
            if full_manifest is None:
                raise SyncError("Concurrent canonical page path changed; refusing automatic resolution")
            canonical_overrides[title] = {"snapshot": dumped[title], "upstream": remote[title]}
    merged = {**dumped, **remote}
    by_path: dict[str, list[str]] = {}
    for title, path in merged.items():
        by_path.setdefault(path, []).append(title)
    canonical_paths = set(remote.values()) | set(dumped.values())
    updates = {}
    retained_aliases = []
    for path in paths:
        if path == "pages/INDEX.tsv":
            updates[path] = "".join(f"{title}\t{merged[title]}\n" for title in sorted(merged, key=str.casefold))
        elif full_manifest is not None and path in canonical_paths and path.endswith(".wiki"):
            # Compatibility aliases may be repathed or ambiguous. Keeping the
            # upstream alias/deletion cannot alter the numeric cutoff payloads.
            if git(repo, "cat-file", "-e", f"refs/remotes/origin/main:{path}").returncode == 0:
                checked(repo, "checkout", "--ours", "--", path)
                checked(repo, "add", "--", path)
            else:
                checked(repo, "rm", "--", path)
            retained_aliases.append(path)
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
    if full_manifest is not None:
        if "pages/INDEX.tsv" in updates:
            full_manifest["index_sha256"] = hashlib.sha256(updates["pages/INDEX.tsv"].encode("utf-8")).hexdigest()
            full_manifest["compatibility_index_entries"] = len(merged)
        if retained_aliases:
            full_manifest["compatibility_alias_conflicts_kept_from_upstream"] = sorted(set(
                full_manifest.get("compatibility_alias_conflicts_kept_from_upstream", []) + retained_aliases))
        if canonical_overrides:
            full_manifest["compatibility_canonical_overrides"] = {
                **full_manifest.get("compatibility_canonical_overrides", {}), **canonical_overrides}
        manifest_path.write_text(json.dumps(full_manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n")
        checked(repo, "add", "--", "pages/public-current/manifest.json")
    mode = "upstream compatibility views; authoritative snapshot unchanged" if full_manifest is not None else "live wiki/index mappings"
    print(f"Reconciled {len(paths)} conflicting generated file(s) using {mode}", flush=True)


def reconcile_compatibility_index(repo: Path) -> None:
    """An automatic Git merge can also change INDEX without a conflict."""
    index = (repo / "pages/INDEX.tsv").read_bytes()
    parsed_index = index_rows(index.decode("utf-8"), repo)
    manifest_path = repo / "pages/public-current/manifest.json"
    if not manifest_path.exists():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise SyncError("Unknown public export manifest")
    digest = hashlib.sha256(index).hexdigest()
    if digest == manifest.get("index_sha256"):
        return
    manifest["index_sha256"] = digest
    manifest["compatibility_index_entries"] = len(parsed_index)
    manifest["compatibility_index_reconciled_after_rebase"] = True
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n")
    checked(repo, "add", "--", "pages/public-current/manifest.json")
    head = checked(repo, "rev-parse", "HEAD").stdout.strip()
    upstream = checked(repo, "rev-parse", "refs/remotes/origin/main").stdout.strip()
    if head != upstream:
        checked(repo, "merge-base", "--is-ancestor", upstream, head)
        checked(repo, "commit", "--amend", "--no-edit")
    else:
        checked(repo, "commit", "-m", "Reconcile wiki backup compatibility index digest")


def verify_authoritative_snapshot(repo: Path, snapshot: str) -> None:
    """Git may merge different payload/JSONL lines without reporting a conflict."""
    manifest_path = repo / "pages/public-current/manifest.json"
    reference = git(repo, "show", f"{snapshot}:pages/public-current/manifest.json")
    if reference.returncode:
        if manifest_path.exists():
            raise SyncError("Legacy dump cannot update a completed public export; rerun full exporter")
        return
    if not manifest_path.exists():
        raise SyncError("Authoritative public export manifest disappeared during reconciliation")
    changes = git(repo, "diff", "--quiet", snapshot, "HEAD", "--", "pages/public-current",
                  ":(exclude)pages/public-current/manifest.json")
    if changes.returncode:
        raise SyncError("Authoritative payload/namespace tree changed during Git reconciliation; no push performed")
    before = json.loads(reference.stdout)
    after = json.loads(manifest_path.read_text(encoding="utf-8"))
    compatibility = {"index_sha256", "compatibility_index_entries",
                     "compatibility_alias_conflicts_kept_from_upstream", "compatibility_canonical_overrides",
                     "compatibility_index_reconciled_after_rebase"}
    if {k: v for k, v in before.items() if k not in compatibility} != {k: v for k, v in after.items() if k not in compatibility}:
        raise SyncError("Authoritative public export manifest changed during Git reconciliation; no push performed")


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
        reconcile_compatibility_index(repo)
        verify_authoritative_snapshot(repo, snapshot)
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
