#!/usr/bin/env python3
"""Wayback Machine save queue, run on the VPS by a systemd timer.

Anyone (Claude, Grok, Bill) adds URLs to ops/wayback/queue.txt in billbisco/swccg-wiki and
pushes. Each run this worker submits queued URLs to archive.org's authenticated Save Page Now 2
API (SPN2) ONE AT A TIME, paced at about 6 saves/min, polls each job by job_id, checks the
capture really loads, and records results in ops/wayback/done.json:

    {"<url>": {"capture": "https://web.archive.org/web/<ts>/<url>", "status": "ok",
               "tries": 1, "last": "2026-10-10T16:00:00Z", "job_id": "spn2-..."}}

status: pending (submitted, not yet confirmed) | ok (capture loads) | retry (save or check
failed; retried later, up to MAX_TRIES) | failed (gave up after MAX_TRIES).

Auth: archive.org S3-style keys, IA_S3_ACCESS / IA_S3_SECRET, read from the environment or
from KEYS_FILE (root-only, chmod 600, outside any git repo). They are never logged or committed.
Without keys the worker falls back to the old anonymous GET /save/<url>.

Never queue live forum.starwarsccg.org / www.starwarsccg.org URLs: the worker skips them.

Usage: wayback_worker.py REPO_DIR [--minutes 10]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gitsync import commit_and_push, reset_to_origin  # noqa: E402

UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki; wayback queue)"
QUEUE = "ops/wayback/queue.txt"
DONE = "ops/wayback/done.json"
KEYS_FILE = Path(os.environ.get("IA_KEYS_FILE", "/etc/swccg-ops/archive-org-s3.env"))
MAX_TRIES = 6
GAP_S = 10            # ~6 saves/min
BACKOFF_START = 30    # seconds; doubles on each 429/5xx, capped
BACKOFF_MAX = 600
RETRY_AFTER = timedelta(minutes=30)
CHECK_AFTER = timedelta(minutes=10)   # anonymous captures only
BANNED_HOSTS = {"forum.starwarsccg.org", "www.starwarsccg.org", "starwarsccg.org"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # keep the 302 so we can read Location
        return None


OPENER = urllib.request.build_opener(NoRedirect)


class Throttled(Exception):
    pass


def now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(t: datetime) -> str:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def load_keys() -> str | None:
    acc, sec = os.environ.get("IA_S3_ACCESS"), os.environ.get("IA_S3_SECRET")
    if not (acc and sec) and KEYS_FILE.exists():
        vals = {}
        for line in KEYS_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                vals[k.strip().removeprefix("export ").strip()] = v.strip().strip("'\"")
        acc, sec = vals.get("IA_S3_ACCESS"), vals.get("IA_S3_SECRET")
    return f"LOW {acc}:{sec}" if acc and sec else None


AUTH = load_keys()


def banned(url: str) -> bool:
    try:
        host = (urllib.parse.urlsplit(url).hostname or "").lower()
    except ValueError:
        return False
    return host in BANNED_HOSTS


def _json(req: urllib.request.Request) -> dict:
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        if e.code == 429 or e.code >= 500:
            raise Throttled(f"HTTP {e.code}") from e
        raise


def spn2_submit(url: str) -> dict:
    data = urllib.parse.urlencode({"url": url, "if_not_archived_within": "30d"}).encode()
    req = urllib.request.Request("https://web.archive.org/save", data=data, method="POST", headers={
        "User-Agent": UA, "Accept": "application/json", "Authorization": AUTH,
        "Content-Type": "application/x-www-form-urlencoded"})
    j = _json(req)
    if not j.get("job_id"):
        msg = str(j.get("message") or j.get("status_ext") or j)[:120]
        if "too many" in msg.lower() or "limit" in msg.lower():
            raise Throttled(msg)
        raise RuntimeError(f"no job_id: {msg}")
    return j


def spn2_status(job_id: str) -> dict:
    req = urllib.request.Request("https://web.archive.org/save/status/" + job_id,
                                 headers={"User-Agent": UA, "Accept": "application/json", "Authorization": AUTH})
    return _json(req)


def save_anon(url: str) -> str:
    req = urllib.request.Request("https://web.archive.org/save/" + url, headers={"User-Agent": UA})
    try:
        resp = OPENER.open(req, timeout=90)
        loc = resp.headers.get("Location") or resp.geturl()
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
            loc = e.headers["Location"]
        elif e.code == 429 or e.code >= 500:
            raise Throttled(f"HTTP {e.code}") from e
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
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
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


def confirm(url: str, e: dict) -> bool:
    """Resolve a pending entry. Returns True if it changed."""
    if e.get("job_id") and AUTH:
        try:
            st = spn2_status(e["job_id"])
        except Exception as ex:  # noqa: BLE001
            print("STATUS-ERR", url, str(ex)[:80], flush=True)
            return False
        s = st.get("status")
        if s == "pending":
            return False
        if s == "success" and st.get("timestamp"):
            e["capture"] = f"https://web.archive.org/web/{st['timestamp']}/{st.get('original_url') or url}"
            e["status"] = "ok" if capture_ok(e["capture"]) else "pending"
            if e["status"] == "pending":
                e.pop("job_id", None)  # fall back to plain capture check next run
        else:
            e["status"] = "retry" if e.get("tries", 1) < MAX_TRIES else "failed"
            e["error"] = str(st.get("status_ext") or st.get("message") or s)[:120]
        e["last"] = iso(now())
        print("CONFIRM", e["status"], url, e.get("capture", ""), flush=True)
        return True
    if now() - parse(e["last"]) < CHECK_AFTER:
        return False
    e["status"] = "ok" if capture_ok(e["capture"]) else ("retry" if e.get("tries", 1) < MAX_TRIES else "failed")
    e["last"] = iso(now())
    return True


def run(repo: Path, minutes: float) -> None:
    reset_to_origin(repo)
    urls, done = load(repo)
    deadline = time.monotonic() + minutes * 60
    changed: dict[str, dict] = {}
    errors_in_row = 0
    backoff = BACKOFF_START
    print("auth:", "SPN2 authenticated" if AUTH else "anonymous", flush=True)

    # 1. confirm earlier captures
    for url, e in list(done.items()):
        if time.monotonic() > deadline - 60:
            break
        if e.get("status") == "pending" and confirm(url, e):
            changed[url] = e
            time.sleep(1)

    # 2. save what is new or due a retry
    submitted: list[str] = []
    for url in urls:
        if time.monotonic() > deadline - 90 or errors_in_row >= 5:
            break
        if banned(url):
            continue
        e = done.get(url)
        if e and (e["status"] in ("ok", "pending", "failed") or now() - parse(e["last"]) < RETRY_AFTER):
            continue
        tries = (e or {}).get("tries", 0) + 1
        try:
            if AUTH:
                j = spn2_submit(url)
                e = {"capture": (e or {}).get("capture", ""), "status": "pending", "tries": tries,
                     "last": iso(now()), "job_id": j["job_id"]}
                submitted.append(url)
                print("SUBMITTED", url, j["job_id"], flush=True)
            else:
                cap = save_anon(url)
                e = {"capture": cap, "status": "pending", "tries": tries, "last": iso(now())}
                print("SAVED", url, cap, flush=True)
            errors_in_row = 0
            backoff = BACKOFF_START
        except Throttled as ex:
            print("THROTTLED", url, str(ex)[:80], f"backing off {backoff}s", flush=True)
            time.sleep(min(backoff, max(0, deadline - time.monotonic() - 90)))
            backoff = min(backoff * 2, BACKOFF_MAX)
            errors_in_row += 1
            continue  # not counted as a try
        except Exception as ex:  # noqa: BLE001
            e = {"capture": (e or {}).get("capture", ""), "status": "retry" if tries < MAX_TRIES else "failed",
                 "tries": tries, "last": iso(now()), "error": str(ex)[:120]}
            errors_in_row += 1
            print("ERROR", url, str(ex)[:120], flush=True)
        done[url] = e
        changed[url] = e
        time.sleep(GAP_S)

    # 3. poll this run's jobs until done or out of time
    while submitted and time.monotonic() < deadline:
        for url in list(submitted):
            if confirm(url, done[url]):
                changed[url] = done[url]
            if done[url]["status"] != "pending" or "job_id" not in done[url]:
                submitted.remove(url)
            time.sleep(1)
        if submitted:
            time.sleep(15)

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
