#!/usr/bin/env python3
"""Wayback Machine save queue, run on the VPS by a systemd timer.

Anyone (Claude, Grok, Bill) adds URLs to ops/wayback/queue.txt in billbisco/swccg-wiki and
pushes. Each run this worker saves queued URLs to archive.org ONE AT A TIME (archive.org
throttles parallel saves), checks earlier captures really exist, and records results in
ops/wayback/done.json:

    {"<url>": {"capture": "https://web.archive.org/web/<ts>/<url>", "status": "ok",
               "tries": 1, "last": "2026-10-10T16:00:00Z"}}

status: pending (saved, not yet confirmed) | ok (capture loads) | retry (save or check failed;
retried later, up to MAX_TRIES) | failed (gave up after MAX_TRIES).

Usage: wayback_worker.py REPO_DIR [--minutes 10]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gitsync import commit_and_push, reset_to_origin  # noqa: E402

UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki; wayback queue)"
QUEUE = "ops/wayback/queue.txt"
DONE = "ops/wayback/done.json"
MAX_TRIES = 6
GAP_S = 20            # pause between saves
RETRY_AFTER = timedelta(minutes=30)
CHECK_AFTER = timedelta(minutes=10)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # keep the 302 so we can read Location
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(t: datetime) -> str:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def save(url: str) -> str:
    """Ask archive.org to capture url; return the capture URL from the redirect."""
    req = urllib.request.Request("https://web.archive.org/save/" + url, headers={"User-Agent": UA})
    try:
        resp = OPENER.open(req, timeout=90)
        loc = resp.headers.get("Location") or resp.geturl()
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
            loc = e.headers["Location"]
        else:
            raise
    if "/web/" not in loc:
        raise RuntimeError(f"no capture in redirect: {loc[:120]}")
    if loc.startswith("/"):
        loc = "https://web.archive.org" + loc
    return loc


def capture_ok(capture: str) -> bool:
    req = urllib.request.Request(capture, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return resp.status == 200
    except urllib.error.HTTPError:
        return False


def load(repo: Path) -> tuple[list[str], dict]:
    q = repo / QUEUE
    urls = []
    if q.exists():
        for line in q.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and line not in urls:
                urls.append(line)
    d = repo / DONE
    done = json.loads(d.read_text(encoding="utf-8")) if d.exists() else {}
    return urls, done


def write_done(repo: Path, done: dict) -> None:
    p = repo / DONE
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(done, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def run(repo: Path, minutes: float) -> None:
    reset_to_origin(repo)
    urls, done = load(repo)
    deadline = time.monotonic() + minutes * 60
    t = now()
    changed: dict[str, dict] = {}
    errors_in_row = 0

    # 1. confirm earlier captures
    for url, e in list(done.items()):
        if time.monotonic() > deadline:
            break
        if e.get("status") == "pending" and t - parse(e["last"]) >= CHECK_AFTER:
            if capture_ok(e["capture"]):
                e["status"] = "ok"
            else:
                e["status"] = "retry" if e.get("tries", 1) < MAX_TRIES else "failed"
            e["last"] = iso(now())
            changed[url] = e
            time.sleep(2)

    # 2. save what is new or due a retry
    for url in urls:
        if time.monotonic() > deadline or errors_in_row >= 3:
            break
        e = done.get(url)
        if e and (e["status"] in ("ok", "pending", "failed") or now() - parse(e["last"]) < RETRY_AFTER):
            continue
        tries = (e or {}).get("tries", 0) + 1
        try:
            cap = save(url)
            e = {"capture": cap, "status": "pending", "tries": tries, "last": iso(now())}
            errors_in_row = 0
            print("SAVED", url, cap, flush=True)
        except Exception as ex:  # noqa: BLE001
            e = {"capture": (e or {}).get("capture", ""), "status": "retry" if tries < MAX_TRIES else "failed",
                 "tries": tries, "last": iso(now()), "error": str(ex)[:120]}
            errors_in_row += 1
            print("ERROR", url, str(ex)[:120], flush=True)
        done[url] = e
        changed[url] = e
        time.sleep(GAP_S)

    if not changed:
        print("nothing to do")
        return

    def redo() -> list[str]:
        _, fresh = load(repo)
        fresh.update(changed)
        write_done(repo, fresh)
        return [DONE]

    write_done(repo, done)
    ok = sum(1 for e in changed.values() if e["status"] in ("ok", "pending"))
    commit_and_push(repo, [DONE], f"wayback: {ok} saved/confirmed, {len(changed) - ok} to retry", redo)
    print("pushed", len(changed), "updates")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--minutes", type=float, default=10)
    a = ap.parse_args()
    run(a.repo.resolve(), a.minutes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
