#!/usr/bin/env python3
"""Report, safety-push, or issue-alert unpushed work in known wiki backup clones.

No AI. Safe by default:
  - never force-push, never push to main
  - skip mutation when the checkout is on a safety/* branch, a git lock exists,
    or this repo looks mid-push (in-flight safety branches are left alone)
  - dirty tracked files are reported only (Windows case-fold collisions must
    not be auto-committed)
  - untracked files under files/ are committed on a new dated safety branch
    and that branch is pushed; the original branch is restored
  - commits already ahead of origin/main are pushed to a dated safety branch

Known clones can be overridden with UNPUSHED_GUARD_CLONES (os.pathsep-separated).
A GitHub issue is opened or commented on when unpushed work older than 24 hours
remains after the attempt (needs GH_TOKEN / GIT_ASKPASS_TOKEN / leftover.token()).
Tokens are never printed. Refs swccg-guild/work#1323.
"""
from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _cand in (_HERE / "tools", _HERE.parent / "tools"):
    if (_cand / "backup_git.py").exists():
        sys.path.insert(0, str(_cand))
        break
from backup_git import GitError, git, push_head, redact  # noqa: E402

DEFAULT_CLONES = [
    Path(r"C:\Users\gythe\.grok\swccg-wiki"),
    Path(r"C:\Users\gythe\.grok\swccg-wiki-files"),
    Path("/opt/swccg-ops/repos/swccg-wiki"),
]
ISSUE_REPO = "billbisco/swccg-wiki"
ISSUE_TITLE = "Unpushed local wiki backup work (auto)"
HOUR = 24 * 3600
LOCK_NAMES = ("index.lock", "HEAD.lock", "shallow.lock", "config.lock", "packed-refs.lock")


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def token() -> str | None:
    env = os.environ.get("GH_TOKEN") or os.environ.get("GIT_ASKPASS_TOKEN")
    if env:
        return env
    try:
        import leftover  # type: ignore
        value = leftover.token()
        if value:
            os.environ.setdefault("GH_TOKEN", value)
            return value
    except Exception:
        return None
    return None


def git_ok(repo: Path, args: list[str]) -> subprocess.CompletedProcess:
    return git(repo, args, check=False)


def locks(repo: Path) -> list[str]:
    git_dir = repo / ".git"
    found = []
    if git_dir.is_file():
        # worktree: .git is a pointer file
        return found
    if not git_dir.is_dir():
        return ["no .git"]
    for name in LOCK_NAMES:
        if (git_dir / name).exists():
            found.append(name)
    refs = git_dir / "refs"
    if refs.is_dir():
        for path in refs.rglob("*.lock"):
            found.append(str(path.relative_to(git_dir)))
    return found


def branch_name(repo: Path) -> str:
    proc = git_ok(repo, ["rev-parse", "--abbrev-ref", "HEAD"])
    return (proc.stdout or "").strip() or "HEAD"


def ahead_behind(repo: Path) -> tuple[int, int]:
    git_ok(repo, ["fetch", "-q", "origin", "main"])
    proc = git_ok(repo, ["rev-list", "--left-right", "--count", "origin/main...HEAD"])
    if proc.returncode != 0 or not proc.stdout.strip():
        return 0, 0
    left, right = proc.stdout.strip().split()
    return int(left), int(right)


def ahead_commit_times(repo: Path) -> list[int]:
    proc = git_ok(repo, ["log", "origin/main..HEAD", "--format=%ct"])
    if proc.returncode != 0 or not proc.stdout.strip():
        return []
    return [int(x) for x in proc.stdout.split() if x.strip().isdigit()]


def porcelain(repo: Path) -> list[str]:
    proc = git_ok(repo, ["status", "--porcelain=v1", "--untracked-files=all"])
    return [line for line in (proc.stdout or "").splitlines() if line]


def classify(lines: list[str]) -> tuple[list[str], list[str]]:
    """Return (untracked rels, dirty-tracked rels)."""
    untracked, dirty = [], []
    for line in lines:
        if line.startswith("?? "):
            untracked.append(line[3:])
        else:
            dirty.append(line[3:].strip() if len(line) > 3 else line)
    return untracked, dirty


def safe_untracked(paths: list[str]) -> list[str]:
    """Only auto-commit wiki file binaries / indexes, never hooks or secrets."""
    keep = []
    for rel in paths:
        norm = rel.replace("\\", "/")
        if norm.startswith(".git/") or "/.git/" in norm:
            continue
        lower = norm.lower()
        if lower.endswith((".env", ".pem", ".key", ".tok", ".token", ".credentials")):
            continue
        name = Path(norm).name
        if name in {"INDEX.tsv", "USAGE.tsv", "DUPLICATES.tsv"} or norm.startswith("files/"):
            keep.append(rel)
            continue
        # dump_images --out .../files writes names in files/
        if "/files/" in f"/{norm}":
            keep.append(rel)
    return keep


def untracked_mtimes(repo: Path, rels: list[str]) -> list[float]:
    times = []
    for rel in rels:
        path = repo / rel
        try:
            times.append(path.stat().st_mtime)
        except OSError:
            continue
    return times


def push_ahead_to_safety(repo: Path) -> str | None:
    name = f"safety/unpushed-{now_stamp()}"
    push_head(repo, f"HEAD:refs/heads/{name}")
    return name


def commit_untracked_on_safety(repo: Path, rels: list[str]) -> str | None:
    if not rels:
        return None
    original = branch_name(repo)
    name = f"safety/unpushed-{now_stamp()}"
    git(repo, ["checkout", "-q", "-b", name])
    try:
        for rel in rels:
            git(repo, ["add", "--", rel])
        diff = git_ok(repo, ["diff", "--cached", "--quiet"])
        if diff.returncode == 0:
            git(repo, ["checkout", "-q", original])
            return None
        git(repo, ["commit", "-m", f"Safety commit of untracked wiki backup files ({name})"])
        push_head(repo, f"HEAD:refs/heads/{name}")
    except Exception:
        git_ok(repo, ["checkout", "-q", original])
        raise
    git(repo, ["checkout", "-q", original])
    return name


def open_or_comment_issue(body: str) -> str | None:
    tok = token()
    if not tok:
        print("no GitHub token; cannot open an unpushed-work issue", file=sys.stderr)
        return None
    # Prefer gh when it is logged in; fall back to the API.
    env = os.environ.copy()
    env["GH_TOKEN"] = tok
    env["GIT_TERMINAL_PROMPT"] = "0"
    list_proc = subprocess.run(
        ["gh", "issue", "list", "-R", ISSUE_REPO, "--state", "open",
         "--search", f'in:title "{ISSUE_TITLE}"', "--json", "number",
         "--jq", ".[0].number // empty"],
        capture_output=True, text=True, env=env,
    )
    num = (list_proc.stdout or "").strip() if list_proc.returncode == 0 else ""
    if num:
        proc = subprocess.run(
            ["gh", "issue", "comment", num, "-R", ISSUE_REPO, "--body", body],
            capture_output=True, text=True, env=env,
        )
        return f"commented #{num}" if proc.returncode == 0 else None
    proc = subprocess.run(
        ["gh", "issue", "create", "-R", ISSUE_REPO, "--title", ISSUE_TITLE, "--body", body],
        capture_output=True, text=True, env=env,
    )
    if proc.returncode == 0:
        return (proc.stdout or "").strip() or "opened"
    # REST fallback
    payload = json.dumps({"title": ISSUE_TITLE, "body": body}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{ISSUE_REPO}/issues",
        data=payload,
        headers={
            "Authorization": "token " + tok,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "swccg-unpushed-work-guard",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        return data.get("html_url") or "opened"
    except Exception as exc:
        print("issue create failed:", redact(str(exc)), file=sys.stderr)
        return None


def inspect(repo: Path) -> dict:
    report = {
        "repo": str(repo),
        "exists": repo.is_dir() and (repo / ".git").exists(),
        "branch": None,
        "behind": 0,
        "ahead": 0,
        "untracked": 0,
        "dirty": 0,
        "locks": [],
        "skipped": None,
        "safety_branch": None,
        "oldest_unpushed": None,
        "stale": False,
        "actions": [],
        "error": None,
    }
    if not report["exists"]:
        report["skipped"] = "missing"
        return report
    report["branch"] = branch_name(repo)
    report["locks"] = locks(repo)
    lines = porcelain(repo)
    untracked, dirty = classify(lines)
    report["untracked"] = len(untracked)
    report["dirty"] = len(dirty)
    report["_untracked_paths"] = untracked
    report["_dirty_paths"] = dirty
    return report


def process(repo: Path, *, apply: bool, stale_after: int) -> dict:
    report = inspect(repo)
    if report.get("skipped") == "missing":
        return report
    try:
        # Do not fetch or push while a safety branch or git lock is in play.
        mutate = apply
        if report["locks"]:
            report["skipped"] = "lock:" + ",".join(report["locks"])
            mutate = False
        elif report["branch"] and report["branch"].startswith("safety/"):
            report["skipped"] = "in-flight safety branch " + report["branch"]
            mutate = False

        if mutate or not report["skipped"]:
            behind, ahead = ahead_behind(repo)
        else:
            # Local-only counts: do not fetch/push during an in-flight safety push.
            proc = git_ok(repo, ["rev-list", "--left-right", "--count", "origin/main...HEAD"])
            if proc.returncode == 0 and proc.stdout.strip():
                behind, ahead = [int(x) for x in proc.stdout.split()]
            else:
                behind, ahead = 0, 0
        report["behind"] = behind
        report["ahead"] = ahead
        times = ahead_commit_times(repo) if not report["skipped"] else []
        # ahead_commit_times is local (no fetch) once origin/main is known
        if report["skipped"]:
            proc = git_ok(repo, ["log", "origin/main..HEAD", "--format=%ct"])
            times = [int(x) for x in proc.stdout.split() if x.strip().isdigit()] if proc.returncode == 0 else []
        utimes = untracked_mtimes(repo, report.get("_untracked_paths") or [])
        oldest = None
        if times:
            oldest = min(times)
        if utimes:
            oldest = min(filter(None, [oldest, min(utimes)]))
        report["oldest_unpushed"] = oldest
        if oldest is not None:
            report["stale"] = (time.time() - oldest) >= stale_after

        if mutate and ahead:
            try:
                name = push_ahead_to_safety(repo)
                report["safety_branch"] = name
                report["actions"].append(f"pushed {ahead} ahead commit(s) to {name}")
            except GitError as exc:
                report["error"] = redact(str(exc))
                report["actions"].append("ahead push failed")

        safe = safe_untracked(report.get("_untracked_paths") or [])
        unsafe = [p for p in (report.get("_untracked_paths") or []) if p not in safe]
        if unsafe:
            report["actions"].append(f"left {len(unsafe)} untracked path(s) alone (not files/ backup data)")
        if mutate and safe and not report.get("error"):
            try:
                name = commit_untracked_on_safety(repo, safe)
                if name:
                    report["safety_branch"] = name
                    report["actions"].append(f"committed {len(safe)} untracked file(s) to {name}")
                    # Re-count after the commit/checkout.
                    lines = porcelain(repo)
                    untracked, dirty = classify(lines)
                    report["untracked"] = len(untracked)
                    report["dirty"] = len(dirty)
            except (GitError, OSError) as exc:
                report["error"] = redact(str(exc))
                report["actions"].append("untracked safety commit failed")

        if report["dirty"]:
            report["actions"].append(
                f"reported {report['dirty']} dirty tracked file(s); not auto-committed"
            )

        # Recompute staleness after actions
        behind, ahead = ahead_behind(repo) if apply else (behind, ahead)
        report["behind"], report["ahead"] = behind, ahead
        times = ahead_commit_times(repo)
        utimes = untracked_mtimes(repo, classify(porcelain(repo))[0])
        oldest = None
        if times:
            oldest = min(times)
        if utimes:
            oldest = min(filter(None, [oldest, min(utimes)]))
        report["oldest_unpushed"] = oldest
        report["stale"] = bool(oldest is not None and (time.time() - oldest) >= stale_after)
    except GitError as exc:
        report["error"] = redact(str(exc))
    report.pop("_untracked_paths", None)
    report.pop("_dirty_paths", None)
    return report


def issue_body(reports: list[dict], host: str) -> str:
    lines = [
        "Automatic unpushed-work guard (no AI). Refs swccg-guild/work#1323.",
        "",
        f"Host: `{host}`",
        "",
    ]
    for r in reports:
        lines.append(f"- `{r['repo']}` branch `{r.get('branch') or '?'}`: "
                     f"ahead={r.get('ahead')} untracked={r.get('untracked')} "
                     f"dirty={r.get('dirty')} skipped={r.get('skipped') or 'no'} "
                     f"stale={r.get('stale')}")
        for action in r.get("actions") or []:
            lines.append(f"  - {action}")
        if r.get("error"):
            lines.append(f"  - error: {r['error']}")
        if r.get("safety_branch"):
            lines.append(f"  - safety branch: `{r['safety_branch']}`")
    lines.append("")
    lines.append("This issue is opened when unpushed work older than 24 hours remains.")
    return "\n".join(lines) + "\n"


def default_clones() -> list[Path]:
    raw = os.environ.get("UNPUSHED_GUARD_CLONES")
    if raw:
        return [Path(p) for p in raw.split(os.pathsep) if p.strip()]
    return [p for p in DEFAULT_CLONES if p.exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", action="append", type=Path, default=[])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stale-after", type=int, default=HOUR)
    ap.add_argument("--log-dir", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    token()  # load leftover into env if present, never print
    clones = args.repo or default_clones()
    if not clones:
        print("no wiki backup clones found", file=sys.stderr)
        return 0
    reports = [process(repo, apply=not args.dry_run, stale_after=args.stale_after) for repo in clones]
    host = socket.gethostname()
    if args.log_dir:
        args.log_dir.mkdir(parents=True, exist_ok=True)
        path = args.log_dir / f"unpushed-guard-{now_stamp()}.json"
        path.write_text(json.dumps(reports, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {path}")
    if args.json:
        print(json.dumps(reports, indent=2, sort_keys=True))
    else:
        for r in reports:
            print(
                f"{r['repo']}: branch={r.get('branch')} ahead={r.get('ahead')} "
                f"untracked={r.get('untracked')} dirty={r.get('dirty')} "
                f"skipped={r.get('skipped')} stale={r.get('stale')} "
                f"actions={r.get('actions')} error={r.get('error')}"
            )
    stale = [r for r in reports if r.get("stale") and (r.get("ahead") or r.get("untracked") or r.get("error"))]
    if stale:
        result = open_or_comment_issue(issue_body(reports, host))
        print("issue:", result or "not opened")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
