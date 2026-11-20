#!/usr/bin/env python3
"""Wayback Machine save queue, run on the VPS by a systemd timer.

Anyone (Claude, Grok, Bill) adds URLs to ops/wayback/queue.txt in billbisco/swccg-wiki and
pushes. Each run this worker submits queued URLs to archive.org's authenticated Save Page Now 2
API (SPN2) ONE AT A TIME, paced at about 6 saves/min, polls each job by job_id, checks the
capture really loads, and records results in ops/wayback/done.json:

    {"<url>": {"capture": "https://web.archive.org/web/<ts>/<url>", "status": "ok",
               "tries": 1, "last": "2026-10-10T16:00:00Z", "job_id": "spn2-..."}}

status: pending (submitted, not yet confirmed) | verified (capture fetched as id_ and matches
the live source: sha256 for files, page text for HTML; this is "opened and checked") |
unverified (capture loads but does not match, or the source could not be fetched; look at it)
| ok (capture loads, not verified yet; the worker verifies these each run, newest first) |
retry (save or check failed; retried later, up to MAX_TRIES) | failed (gave up after MAX_TRIES).

Each run confirms only the newest PENDING_CONFIRM_CAP pending jobs whose last
activity is within PENDING_CONFIRM_MAX_AGE (default 40 jobs / 2 hours). Older
pending rows are not polled; after STALE_PENDING_AGE they are resubmitted (SPN2
answers with the recent capture if the dead job did finish). Entries that failed on a
transient archive.org error are retried after FAILED_RETRY_AGE. Two verify lanes:
the VPS worker tries to open the capture (lane 1); a connection refused / timeout
there is a confirm miss, not a save pause — this PC (manpc) retries (lane 2) via
`ops/wayback_verify_manpc.py` dropping receipts in verify-inbox. HTTP 401/429/5xx
on the Save Page Now API still opens the provider circuit. Stalled jobs are poked
with ?copy=2, not by polling a dead job_id forever.

Verified https://swccg.com/snapshots/… URLs: after verify, delete the staging file under
/opt/swccg-res/snapshots/ only when a main-namespace wiki article already cites a Wayback
URL of that exact snapshot path (Bill 2026-10-22 cite-before-delete; 2026-10-13 prune rule).
The cite index is the wiki DB externallinks table (ns0, Wayback host, snapshot path). Do
not use truncated exturlusage of all web.archive.org/web/ links — that list fills with
DeckTech/YouTube and misses snapshot cites. Wiki File: pages and archive.org items stay.
Uncited verified files stay on disk. KEEP-UNCITED logs only when the staging file still exists.

Bots: push the URL to queue.txt, then read done.json. Cite the capture once status is "verified".
No Wayback access from the bot's own machine is needed.

Auth: archive.org S3-style keys, IA_S3_ACCESS / IA_S3_SECRET, read from the environment or
from KEYS_FILE (root-only, chmod 600, outside any git repo). They are never logged or committed.
Without keys the worker uses anonymous GET /save/<url>. A rejected credential
never falls back to anonymous submissions: it pauses until an authorized key
change, followed by one verified recovery canary. All producers use this owner.

Never queue live forum.starwarsccg.org / www.starwarsccg.org URLs: the worker skips them.

Usage: wayback_worker.py REPO_DIR [--minutes 10]
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import html
import json
import re
import subprocess
import zlib
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
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_owner import OwnerAdapter, load_allowed_objects  # noqa: E402
from preservation_suppression import suppressed_source, suppressed_url  # noqa: E402
from preservation_native import is_native_capture_url, NATIVE_REPRESENTATION, validate_native_mirror
from preservation_registry import iter_records, object_state
from preservation_contracts import registration_object_id  # noqa: E402
from wayback_control import Busy, Control, Paused, atomic_json  # noqa: E402

UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki; wayback queue)"
QUEUE = "ops/wayback/queue.txt"
DONE = "ops/wayback/done.json"
KEYS_FILE = Path(os.environ.get("IA_KEYS_FILE", "/etc/swccg-ops/archive-org-s3.env"))
MAX_TRIES = 6
GAP_S = Control.SUBMISSION_GAP  # minimum gap also survives owner restarts
# 0 = uncapped (tests). Production systemd sets WAYBACK_MAX_SUBMITS=6.
MAX_SUBMITS_PER_RUN = int(os.environ.get("WAYBACK_MAX_SUBMITS") or "0")
RETRY_AFTER = timedelta(minutes=30)
CHECK_AFTER = timedelta(minutes=10)   # anonymous captures only
PENDING_CONFIRM_MAX_AGE = timedelta(hours=2)  # skip stalled pending job_ids
PENDING_CONFIRM_CAP = 40                      # max status polls per run (newest first)
STALE_PENDING_AGE = timedelta(hours=24)       # a pending job this old is dead: resubmit it
FAILED_RETRY_AGE = timedelta(days=7)          # failed on a transient error, retried once a week
TRANSIENT_ERRORS = ("stalled spn2", "connection refused", "errno 111", "timed out", "429", "503", "502")
BANNED_HOSTS = {"forum.starwarsccg.org", "www.starwarsccg.org", "starwarsccg.org"}
SNAPSHOT_HOSTS = {"swccg.com", "www.swccg.com"}
WIKI_API = "https://wiki.swccg.com/api.php"
WIKI_DB_CONTAINER = os.environ.get("SWCCG_WIKI_DB_CONTAINER", "swccg_wiki_db")
WB_SNAPSHOT = re.compile(
    r"^https?://web\.archive\.org/web/\d{14}[a-z_]*/(?:https?://)?(?:www\.)?swccg\.com/snapshots/(.+)$",
    re.I,
)
# MediaWiki 1.43 externallinks.el_to_path for a Wayback snapshot cite:
# /web/20261011191428/https://swccg.com/snapshots/pc/foo.html
WB_SNAPSHOT_IN_PATH = re.compile(
    r"(?:https?://)?(?:www\.)?swccg\.com/snapshots/(.+)$",
    re.I,
)
WIKI_CITE_SQL = """
SELECT DISTINCT el_to_path
FROM externallinks e
JOIN page p ON p.page_id = e.el_from
WHERE p.page_namespace = 0
  AND e.el_to_domain_index LIKE '%archive.web%'
  AND e.el_to_path LIKE '%swccg.com/snapshots/%'
"""


def snapshot_root() -> Path:
    return Path(os.environ.get("SWCCG_SNAPSHOT_ROOT", "/opt/swccg-res/snapshots"))


def snapshot_log() -> Path:
    return Path(os.environ.get("SWCCG_SNAPSHOT_LOG", str(snapshot_root() / "DELETED-after-wayback.log")))


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # keep the 302 so we can read Location
        return None


OPENER = urllib.request.build_opener(NoRedirect)


class Throttled(Exception):
    def __init__(self, message, status=None, retry_after=None):
        super().__init__(message)
        self.status, self.retry_after = status, retry_after


ACTIVE_CONTROL = None


def control_directory(repo: Path) -> Path:
    """Shared by every checkout run as the same server account, outside Git resets."""
    return Path(os.environ.get("WAYBACK_CONTROL_DIR", str(Path.home() / ".local/state/swccg-wayback")))


def save_api_url(url: str) -> bool:
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    host = (parts.hostname or "").lower()
    path = parts.path or ""
    return host in {"web.archive.org", "archive.org"} and (path == "/save" or path.startswith("/save/"))


def availability_api_url(url: str) -> bool:
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    host = (parts.hostname or "").lower()
    path = parts.path or ""
    return host == "archive.org" and path.startswith("/wayback/available")


def archive_response(url: str, status: int, headers=None):
    """Pause new saves on Save Page Now / availability HTTP throttle or auth failure.

    Opening a replay page (web.archive.org/web/...) is lane-1 confirm. HTTP there
    does not pause submissions; manpc is lane 2.
    """
    if not ACTIVE_CONTROL:
        return
    if status == 401 and save_api_url(url):
        ACTIVE_CONTROL.authentication_failed()
        return
    if status in {403, 429} or status >= 500:
        if save_api_url(url) or availability_api_url(url):
            ACTIVE_CONTROL.provider_failed(status, (headers or {}).get("Retry-After"))


def archive_transport_failed(url: str):
    """TCP/DNS miss reaching Wayback. Lane 1 skips confirm/verify; lane 2 retries.

    Does not pause new Save Page Now submits.
    """
    return


def now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(t: datetime) -> str:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s: str) -> datetime:
    """Read aware persisted ISO 8601 timestamps without losing their precision."""
    value = datetime.fromisoformat(s)
    if value.tzinfo is None:
        raise ValueError("ledger timestamp requires an explicit UTC offset")
    return value.astimezone(timezone.utc)


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
            archive_response(req.full_url, resp.status, resp.headers)
            return json.loads(resp.read().decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        archive_response(req.full_url, e.code, e.headers)
        if e.code == 429 or e.code >= 500:
            raise Throttled(f"HTTP {e.code}", e.code, (e.headers or {}).get("Retry-After")) from e
        raise
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        archive_transport_failed(req.full_url)
        raise


def spn2_submit(url: str, force: bool = False) -> dict:
    data = urllib.parse.urlencode({"url": url, "if_not_archived_within": "1m" if force else "30d"}).encode()
    req = urllib.request.Request("https://web.archive.org/save", data=data, method="POST", headers={
        "User-Agent": UA, "Accept": "application/json", "Authorization": AUTH,
        "Content-Type": "application/x-www-form-urlencoded"})
    j = _json(req)
    if not j.get("job_id") and "same snapshot had been made" in str(j.get("message", "")):
        j["recent"] = latest_capture(url)
        if j["recent"]:
            return j
    if not j.get("job_id"):
        msg = str(j.get("message") or j.get("status_ext") or j)[:120]
        if "too many" in msg.lower() or "limit" in msg.lower():
            raise Throttled(msg)
        raise RuntimeError(f"no job_id: {msg}")
    return j


def latest_capture(url: str) -> str:
    """Newest existing capture of url (used when SPN2 skips a URL archived within 30d)."""
    q = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    try:
        with urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": UA}), timeout=60) as r:
            archive_response(q, r.status, r.headers)
            snap = json.loads(r.read().decode()).get("archived_snapshots", {}).get("closest") or {}
    except Paused:
        raise
    except urllib.error.HTTPError as error:
        archive_response(q, error.code, error.headers)
        return ""
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        archive_transport_failed(q)
        return ""
    except Exception:  # noqa: BLE001
        return ""
    cap = snap.get("url", "")
    return cap.replace("http://web.archive.org", "https://web.archive.org") if snap.get("available") else ""


def spn2_status(job_id: str) -> dict:
    req = urllib.request.Request("https://web.archive.org/save/status/" + job_id,
                                 headers={"User-Agent": UA, "Accept": "application/json", "Authorization": AUTH})
    return _json(req)


def save_anon(url: str) -> str:
    req = urllib.request.Request("https://web.archive.org/save/" + url, headers={"User-Agent": UA})
    try:
        resp = OPENER.open(req, timeout=90)
        archive_response(req.full_url, resp.status, resp.headers)
        loc = resp.headers.get("Location") or resp.geturl()
    except urllib.error.HTTPError as e:
        archive_response(req.full_url, e.code, e.headers)
        if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
            loc = e.headers["Location"]
        elif e.code == 429 or e.code >= 500:
            raise Throttled(f"HTTP {e.code}", e.code, (e.headers or {}).get("Retry-After")) from e
        else:
            raise
    if "/web/" not in loc:
        raise RuntimeError(f"no capture in redirect: {loc[:120]}")
    if loc.startswith("/"):
        loc = "https://web.archive.org" + loc
    return loc


def submit_capture(url: str, entry: dict | None, session: dict) -> dict:
    """Rejected authentication requires repair, never a new anonymous retry lane."""
    if ACTIVE_CONTROL and suppressed_url(ACTIVE_CONTROL.directory / "registry", url):
        raise PermissionError("exact withdrawn source cannot be submitted")
    if session["authenticated"]:
        try:
            return spn2_submit(url, force=True) if (entry or {}).get("recapture") else spn2_submit(url)
        except urllib.error.HTTPError as ex:
            if ex.code != 401:
                raise
            if ACTIVE_CONTROL:
                ACTIVE_CONTROL.authentication_failed()
            raise
    return {"anonymous_capture": save_anon(url)}


def capture_ok(capture: str) -> bool:
    req = urllib.request.Request(capture, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            archive_response(capture, resp.status, resp.headers)
            return resp.status == 200
    except urllib.error.HTTPError as error:
        archive_response(capture, error.code, error.headers)
        return False
    except (urllib.error.URLError, TimeoutError):
        archive_transport_failed(capture)
        return False


# ---------------------------------------------------------------------------------------------
# Verification (Bill, 2026-10-20): after a capture loads, fetch the capture's id_ URL (the bytes
# Wayback stored, without its toolbar) and compare it with the live source: sha256 for files
# (PDF, images, ...), visible page text for HTML. A match sets status "verified", which counts as
# "opened and checked" for citations, so bots only push queue.txt and read done.json.
#
#   verified    capture matches the source (verify: {"method": "sha256"|"text", ...})
#   unverified  capture loads but does not match (Cloudflare page, different file, text differs),
#               or the source could not be fetched VERIFY_TRIES times; a human or bot must look
#   ok          capture loads, verification not done yet (older entries; the worker works through
#               them each run, newest first)
# ---------------------------------------------------------------------------------------------
VERIFY_TRIES = 3
TEXT_MATCH = 0.85            # share of words the capture and the live page have in common
MAX_BODY = 20 * 1024 * 1024  # bytes kept in memory for HTML comparison (files are hashed streaming)
MAX_FETCH = 300 * 1024 * 1024
BACKLOG_SECONDS = 150        # time per run spent verifying older "ok" entries
VERIFY_GAP_S = 4             # pause between backlog verifications (archive.org refuses bursts)
# Strict capture check (2026-10-26 false-verify fix). A capture counts only when (a) its id_ URL
# answers a real HTTP 200 at the SAME 14-digit timestamp (redirects followed only inside
# web.archive.org for the same original URL), (b) the body is not a Wayback error page, and
# (c) the CDX index lists that exact timestamp with statuscode 2xx (or a warc/revisit).
# Right after Save Page Now, replay can serve a capture from a temporary cache that never reaches
# the index; it 404s days later (seen on captures from 2026-10-20..22). Exact-URL CDX queries
# list new captures within minutes (prefix/matchType queries can miss recent rows). So:
#   ("ok")           replay 200 at the exact timestamp AND CDX lists it 2xx: durable
#   ("replay-only")  replay 200 at the exact timestamp, CDX has no row yet: may be cited
#                    (verify.index = "pending"), re-checked by the worker, never deleted on
#   False            anything else (404, error page, other capture, CDX 4xx/5xx)
# A snapshot file is deleted only on "ok", re-checked at delete time, capture >= DELETE_MIN_AGE.
CDX_API = "https://web.archive.org/cdx/search/cdx"
RECHECK_AFTER = timedelta(hours=24)    # re-check verified "replay-only" captures this often
RECHECKS_PER_RUN = 10
DELETE_MIN_AGE = timedelta(days=7)     # capture age before its staging file may be deleted
DELETE_CHECKS_PER_RUN = 25             # strict re-checks before deletes, per run
WAYBACK_ERROR_RX = re.compile(
    rb"Hrm\.|Wayback Machine doesn(?:'|&#39;|&#x27;|\xe2\x80\x99)t have that page|"
    rb"has not archived that URL|This URL has been excluded from the Wayback Machine|"
    rb"Got an HTTP \d{3} response at crawl time|<title>\s*Wayback Machine\s*</title>", re.I)


def capture_parts(capture: str) -> tuple[str, str]:
    m = re.match(r"https?://web\.archive\.org/web/(\d{14})(?:[a-z]{2}_)?/(.+)$", (capture or "").split("#")[0])
    if not m:
        raise ValueError(f"not a Wayback capture URL: {capture[:100]}")
    return m.group(1), m.group(2)


def _norm_original(u: str) -> str:
    u = urllib.parse.unquote(u.strip())
    u = re.sub(r"^(?:https?:)?//", "", u if re.match(r"^(?:https?:)?//", u) else "//" + u, flags=re.I)
    host, _, rest = u.partition("/")
    host = host.lower().removeprefix("www.").split(":")[0]
    return host + "/" + rest.rstrip("/")


def same_original(a: str, b: str) -> bool:
    return _norm_original(a) == _norm_original(b)


def capture_age(capture: str, now_t: datetime | None = None) -> timedelta | None:
    try:
        ts, _ = capture_parts(capture)
        t = datetime.strptime(ts, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return (now_t or now()) - t


def _raw_get(url: str, limit: int = 1 << 16) -> tuple[int, dict, bytes]:
    """One GET without following redirects; returns (status, headers, first `limit` bytes)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "identity"})
    try:
        resp = OPENER.open(req, timeout=120)
    except urllib.error.HTTPError as e:
        archive_response(url, e.code, e.headers)
        body = b""
        try:
            body = e.read(limit) or b""
        except Exception:  # noqa: BLE001
            pass
        return e.code, dict(e.headers or {}), body
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        archive_transport_failed(url)
        raise VerifyRetry(f"{type(e).__name__}: {str(e)[:80]}", side="capture") from e
    with resp:
        archive_response(url, resp.status, resp.headers)
        return resp.status, dict(resp.headers), resp.read(limit)


def cdx_rows(original: str, ts: str) -> list[list[str]]:
    q = CDX_API + "?" + urllib.parse.urlencode({"url": original, "from": ts, "to": ts, "output": "json",
                                                "fl": "timestamp,statuscode,mimetype", "limit": "20"})
    status, _, body = _raw_get(q, limit=1 << 20)
    if status == 429 or status >= 500:
        raise VerifyRetry(f"CDX HTTP {status}", side="capture")
    if status != 200:
        raise VerifyRetry(f"CDX HTTP {status}", side="capture")
    try:
        rows = json.loads(body.decode("utf-8", "replace") or "[]")
    except ValueError as ex:
        raise VerifyRetry("CDX answer is not JSON", side="capture") from ex
    return rows[1:] if rows and rows[0] and rows[0][0] == "timestamp" else rows


def strict_check(capture: str, get=None, cdx=None) -> tuple[bool, str]:
    """(True, "ok") only for a capture that really exists; else (False, reason).
    Raises VerifyRetry(side="capture") when archive.org throttles or is down (try later)."""
    get, cdx = get or _raw_get, cdx or cdx_rows
    ts, original = capture_parts(capture)
    url = f"https://web.archive.org/web/{ts}id_/{original}"
    for _hop in range(6):
        status, headers, body = get(url)
        if status == 429 or status >= 500:
            raise VerifyRetry(f"capture HTTP {status}", side="capture")
        if status in (301, 302, 303, 307, 308):
            loc = urllib.parse.urljoin(url, headers.get("Location") or headers.get("location") or "")
            m = re.match(r"https://web\.archive\.org/web/(\d{14})(?:[a-z]{2}_)?/(.+)$", loc)
            if not m or not same_original(m.group(2), original):
                return False, f"redirects off the capture: {loc[:100]}"
            if m.group(1) != ts:
                return False, f"redirects to another capture {m.group(1)} (no capture at {ts})"
            url = loc
            continue
        if status != 200:
            return False, f"capture HTTP {status}"
        if WAYBACK_ERROR_RX.search(body[:1 << 16]):
            return False, "capture is a Wayback error page"
        break
    else:
        return False, "too many redirects"
    rows = [r for r in cdx(original, ts) if r and r[0] == ts]
    if not rows:
        return True, f"replay-only: timestamp {ts} not in the CDX index yet"
    for r in rows:
        code = r[1] if len(r) > 1 else ""
        if code.startswith("2") or (code == "-" and len(r) > 2 and "revisit" in r[2]):
            return True, "ok"
    return False, f"CDX statuscode {rows[0][1] if len(rows[0]) > 1 else '?'} at {ts}"
CLOUDFLARE_RX = re.compile(r"<title>\s*(?:Just a moment\.\.\.|Attention Required! \| Cloudflare)|cf-chl-|challenge-platform", re.I)


class VerifyRetry(Exception):
    """Transient: try verifying again on a later run. side="capture" means archive.org itself failed
    (connection refused, 429, 5xx); that does not count against the entry's VERIFY_TRIES and stops
    the backlog pass for the run. Anything else (source unreachable, capture 403/404) counts."""

    def __init__(self, msg: str, side: str = "source"):
        super().__init__(msg)
        self.side = side


class StatusRetry(Exception):
    """Transient: web.archive.org refused or timed out during pending confirm. Stop polling
    pending jobs for this run so new submits still get a turn."""


def archive_unreachable(ex: BaseException) -> bool:
    """True when archive.org itself is down, refusing, or throttling this client."""
    if isinstance(ex, (Throttled, StatusRetry)):
        return True
    if isinstance(ex, urllib.error.HTTPError):
        return ex.code == 429 or ex.code >= 500
    if isinstance(ex, urllib.error.URLError):
        return True
    if isinstance(ex, (TimeoutError, ConnectionError)):
        return True
    msg = str(ex).lower()
    return any(
        n in msg
        for n in (
            "111",
            "connection refused",
            "timed out",
            "timeout",
            "temporarily unavailable",
            "network is unreachable",
            "name or service not known",
            "failed to resolve",
        )
    )


def pending_age(e: dict, now_t: datetime | None = None) -> timedelta | None:
    last = e.get("last")
    if not last:
        return None
    try:
        return (now_t or now()) - parse(last)
    except (TypeError, ValueError):
        return None


def stale(e: dict, now_t: datetime | None = None) -> bool:
    """A pending job older than STALE_PENDING_AGE is never polled again (see
    pending_confirm_urls), so resubmit it; a failed entry whose error was transient
    (archive.org stalled or refused) gets a fresh round of tries after FAILED_RETRY_AGE."""
    age = pending_age(e, now_t)
    if age is None:
        return False
    if e.get("status") == "pending":
        return age > STALE_PENDING_AGE
    if e.get("status") == "failed":
        err = str(e.get("error") or "").lower()
        return age > FAILED_RETRY_AGE and any(s in err for s in TRANSIENT_ERRORS)
    return False


def pending_confirm_urls(
    done: dict,
    *,
    now_t: datetime | None = None,
    max_age: timedelta | None = None,
    cap: int | None = None,
) -> list[str]:
    """Newest pending jobs still young enough to be live SPN2 work."""
    max_age = PENDING_CONFIRM_MAX_AGE if max_age is None else max_age
    cap = PENDING_CONFIRM_CAP if cap is None else cap
    now_t = now_t or now()
    rows: list[tuple[datetime, str]] = []
    for url, e in done.items():
        if not isinstance(e, dict) or e.get("status") != "pending":
            continue
        age = pending_age(e, now_t)
        if age is None or age > max_age:
            continue
        rows.append((now_t - age, url))
    rows.sort(reverse=True)
    return [u for _, u in rows[:cap]]


def id_url(capture: str) -> str:
    """https://web.archive.org/web/<ts>/<url> -> https://web.archive.org/web/<ts>id_/<url>"""
    return re.sub(r"(/web/\d{14})(?:[a-z]{2}_)?/", r"\1id_/", capture, count=1)


def _decoder(encoding: str):
    """Wayback replays id_ captures with the Content-Encoding the site sent (usually gzip)."""
    enc = (encoding or "identity").strip().lower()
    if enc in ("", "identity"):
        return None
    if enc in ("gzip", "x-gzip"):
        return zlib.decompressobj(16 + zlib.MAX_WBITS)
    if enc == "deflate":
        return zlib.decompressobj()
    if enc == "br":
        try:
            import brotli  # type: ignore
        except ImportError as ex:
            raise VerifyRetry("brotli-encoded body and no brotli module") from ex
        return brotli.Decompressor()
    raise VerifyRetry(f"unsupported Content-Encoding {enc}")


def fetch(url: str) -> dict:
    """GET url; return status, content type, sha256 and size of the whole (decoded) body, and its
    first MAX_BODY bytes."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "identity"})
    h, size, head = hashlib.sha256(), 0, bytearray()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            archive_response(url, resp.status, resp.headers)
            status, ctype = resp.status, resp.headers.get("Content-Type", "")
            dec = _decoder(resp.headers.get("Content-Encoding", ""))
            while True:
                raw = resp.read(1 << 16)
                if not raw:
                    chunk = dec.flush() if dec is not None and hasattr(dec, "flush") else b""
                    if not chunk:
                        break
                else:
                    chunk = (dec.decompress(raw) if hasattr(dec, "decompress") else dec.process(raw)) if dec is not None else raw
                h.update(chunk)
                size += len(chunk)
                if len(head) < MAX_BODY:
                    head += chunk[:MAX_BODY - len(head)]
                if size > MAX_FETCH:
                    raise VerifyRetry(f"larger than {MAX_FETCH} bytes: {url[:80]}")
    except urllib.error.HTTPError as e:
        archive_response(url, e.code, e.headers)
        return {"status": e.code, "ctype": e.headers.get("Content-Type", "") if e.headers else "", "sha256": "",
                "size": 0, "body": b""}
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError, zlib.error) as e:
        archive_transport_failed(url)
        raise VerifyRetry(f"{type(e).__name__}: {str(e)[:80]}") from e
    return {"status": status, "ctype": ctype, "sha256": h.hexdigest(), "size": size, "body": bytes(head)}


def is_html(r: dict) -> bool:
    if "html" in r["ctype"].lower() or "xml" in r["ctype"].lower():
        return True
    start = r["body"][:512].lstrip().lower()
    return start.startswith((b"<!doctype html", b"<html", b"<?xml")) or b"<html" in start


def page_words(body: bytes, ctype: str = "") -> collections.Counter:
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I) or re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", body[:4096], re.I)
    enc = (m.group(1).decode() if isinstance(m.group(1), bytes) else m.group(1)) if m else "utf-8"
    try:
        t = body.decode(enc, "replace")
    except LookupError:
        t = body.decode("utf-8", "replace")
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<(script|style|noscript|template)\b.*?</\1\s*>", " ", t, flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return collections.Counter(w.lower() for w in re.findall(r"\w+", t))


def text_match(a: collections.Counter, b: collections.Counter) -> float:
    total = max(sum(a.values()), sum(b.values()))
    return sum((a & b).values()) / total if total else 1.0


def verify(url: str, capture: str, get=None) -> tuple[str, dict]:
    """Compare a capture with its live source. Returns ("verified" | "unverified", details).
    Raises VerifyRetry when either side could not be fetched (try again later)."""
    get = get or fetch
    good, why = strict_check(capture)
    if not good:
        return "unverified", {"at": iso(now()), "capture_id": id_url(capture), "method": "strict",
                              "reason": why}
    try:
        cap = get(id_url(capture))
    except VerifyRetry as ex:
        raise VerifyRetry(f"capture: {ex}", side="capture") from ex
    if cap["status"] != 200:  # 429/5xx = archive.org throttling or outage; 403/404 = this capture's problem
        side = "capture" if cap["status"] == 429 or cap["status"] >= 500 else "source"
        raise VerifyRetry(f"capture HTTP {cap['status']}", side=side)
    src = get(url)
    if src["status"] != 200:
        raise VerifyRetry(f"source HTTP {src['status']}")
    info = {"at": iso(now()), "capture_id": id_url(capture), "index": "cdx" if why == "ok" else "pending"}
    native = is_native_capture_url(url)
    if cap["sha256"] == src["sha256"] and (not native or cap["size"] == src["size"]):
        return "verified", {**info, "method": "sha256", "sha256": src["sha256"], "bytes": src["size"]}
    if native or not (is_html(src) and is_html(cap)):
        return "unverified", {**info, "method": "sha256", "reason": "file differs from the source",
                              "sha256": src["sha256"], "capture_sha256": cap["sha256"]}
    cap_text = cap["body"].decode("utf-8", "replace")
    if CLOUDFLARE_RX.search(cap_text) and not CLOUDFLARE_RX.search(src["body"].decode("utf-8", "replace")):
        return "unverified", {**info, "method": "text", "reason": "capture is a Cloudflare challenge page"}
    ratio = text_match(page_words(src["body"], src["ctype"]), page_words(cap["body"], cap["ctype"]))
    status = "verified" if ratio >= TEXT_MATCH else "unverified"
    out = {**info, "method": "text", "text_match": round(ratio, 3)}
    if status == "unverified":
        out["reason"] = f"page text matches {ratio:.0%} (< {TEXT_MATCH:.0%})"
    return status, out


def verify_entry(url: str, e: dict, get=None) -> bool:
    """Verify a loaded capture in place (status ok -> verified/unverified). Returns True if e changed."""
    if not e.get("capture"):
        return False
    try:
        status, info = verify(url, e["capture"], get)
    except VerifyRetry as ex:
        print("VERIFY-ERR", url, str(ex)[:80], flush=True)
        if ex.side == "capture":  # archive.org trouble: leave the entry alone, try next run
            raise
        n = e.get("verify_tries", 0) + 1
        e["verify_tries"] = n
        e["verify"] = {"at": iso(now()), "error": str(ex)[:120]}
        if n >= VERIFY_TRIES:
            e["status"] = "unverified"
            e["verify"]["reason"] = f"could not fetch after {n} tries"
        return True
    e["status"], e["verify"] = status, info
    e.pop("verify_tries", None)
    print("VERIFY", status, url, info.get("text_match", info.get("method")), flush=True)
    return True


def mark_verify_deferred(e: dict, reason: str) -> None:
    """Lane 1 could not open Wayback; leave the capture for manpc (lane 2)."""
    info = dict(e.get("verify") or {})
    info.update(at=iso(now()), defer="manpc", error=reason[:120])
    e["verify"] = info


def try_verify(url: str, e: dict) -> None:
    """Verify right after a capture loads; replay misses leave it ok for lane 2."""
    try:
        verify_entry(url, e)
    except VerifyRetry as error:
        if error.side == "capture":
            mark_verify_deferred(e, str(error))
            print("VERIFY-DEFER", url, str(error)[:80], flush=True)


def verify_inbox_dir(control: Control) -> Path:
    path = control.directory / "verify-inbox"
    path.mkdir(parents=True, exist_ok=True)
    return path


def verify_candidates(done: dict, *, limit: int = 40) -> list[dict]:
    """URLs lane 2 should try: pending/ok/unverified with a capture or job_id.

    Prefer manpc-deferred rows, then live swccg.com / res.starwarsccg.org saves,
    then other https captures. Dead http://decipher.com sources go last.
    """
    ours = ("swccg.com", "res.starwarsccg.org", "wiki.swccg.com")
    rows = []
    for url, entry in done.items():
        if entry.get("status") not in {"ok", "pending", "unverified"}:
            continue
        if not (entry.get("capture") or entry.get("job_id")):
            continue
        rows.append({
            "url": url,
            "status": entry.get("status"),
            "capture": entry.get("capture") or "",
            "job_id": entry.get("job_id") or "",
            "defer": (entry.get("verify") or {}).get("defer") or "",
        })

    def rank(row: dict) -> tuple:
        url = row["url"]
        defer = 0 if row["defer"] == "manpc" else 1
        our = 0 if any(host in url for host in ours) else 1
        has_capture = 0 if row["capture"] else 1
        dead = 1 if url.startswith("http://decipher.com") else 0
        return (defer, dead, our, has_capture, url)

    rows.sort(key=rank)
    return rows[:limit]


def apply_verify_inbox(control: Control, done: dict, changed: dict, *, allowed_urls=None) -> int:
    """Consume schema-1 receipts without losing unresolved or malformed evidence."""
    import base64
    applied = 0
    for path in sorted(verify_inbox_dir(control).glob("*.json")):
        if allowed_urls is not None and path.stat().st_size > 8 * 1024 * 1024:
            continue  # A scoped run does not consume unrelated/oversize evidence.
        if path.stat().st_size > 8 * 1024 * 1024:
            report_dir = control.directory / "verify-receipts" / ("oversize-" + hashlib.sha256(path.name.encode("utf-8")).hexdigest())
            report_dir.mkdir(parents=True, exist_ok=True)
            atomic_json(report_dir / "disposition.json", {"inbox_name":path.name,
                        "bytes":path.stat().st_size, "reason":"over metadata budget; original retained in inbox"})
            print("VERIFY-INBOX-ERR", path.name, "over metadata budget; retained", flush=True)
            continue
        with path.open("rb") as stream:
            raw = stream.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            print("VERIFY-INBOX-ERR", path.name, "grew over metadata budget; retained", flush=True)
            continue
        if allowed_urls is not None:
            try:
                peek = json.loads(raw)
                if not isinstance(peek, dict) or not isinstance(peek.get("updates"), dict) or not (set(peek["updates"]) & allowed_urls):
                    continue
            except (ValueError, TypeError):
                continue
        original_done = json.loads(json.dumps(done))
        digest = hashlib.sha256(raw).hexdigest()
        retained = control.directory / "verify-receipts" / digest
        retained.mkdir(parents=True, exist_ok=True)
        # Exact original bytes remain retrievable even after a fully consumed
        # inbox file is removed. Unresolved inputs also stay in the inbox.
        atomic_json(retained / "original.json", {
            "sha256":digest, "bytes":len(raw),
            "original_base64":base64.b64encode(raw).decode("ascii"),
        })
        dispositions, pending, updates = {}, {}, {}
        try:
            data = json.loads(raw)
            if data.get("schema") != 1 or not isinstance(data.get("updates"), dict):
                raise ValueError("unsupported receipt schema")
            updates = data["updates"]
            lane = data.get("lane") or "manpc"
            for url, receipt in updates.items():
                if allowed_urls is not None and url not in allowed_urls:
                    dispositions[url] = "outside_native_cohort"
                    continue
                if not isinstance(receipt, dict) or receipt.get("status") != "verified":
                    dispositions[url] = "unsupported_receipt"
                    continue
                cap, cur = receipt.get("capture"), done.get(url)
                if not cur or not cap:
                    dispositions[url] = "missing_prior_done_or_capture"
                    continue
                if cur.get("capture") and cur["capture"] != cap:
                    dispositions[url] = "capture_conflict"
                    continue
                if cur.get("status") == "verified":
                    dispositions[url] = "already_verified"
                    continue
                entry = dict(cur)
                info = dict(receipt.get("verify") or {})
                info["lane"] = lane
                entry.update(capture=cap, status="verified", verify=info, last=iso(now()))
                pending[url] = entry
                dispositions[url] = "applied"
        except (ValueError, TypeError, AttributeError):
            dispositions = {"$receipt":"malformed_or_unsupported"}
            pending = {}
        report = {"original_sha256":digest, "dispositions":dispositions}
        report_hash = hashlib.sha256(json.dumps(report, sort_keys=True).encode("utf-8")).hexdigest()
        atomic_json(retained / (report_hash + ".json"), report)
        done.update(pending)
        changed.update(pending)
        complete = bool(dispositions) and all(v in {"applied", "already_verified"}
                                             for v in dispositions.values())
        if complete:
            control.checkpoint(done, getattr(control, "initial_done", original_done))
            path.unlink()
        applied += len(pending)
        print("VERIFY-INBOX", path.name, len(pending), "applied", "complete" if complete else "retained", flush=True)
    return applied


def load(repo: Path) -> tuple[list[str], dict]:
    q = repo / QUEUE
    urls = []
    seen = set()
    if q.exists():
        for line in q.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and line not in seen:
                urls.append(line)
                seen.add(line)
    d = repo / DONE
    done = json.loads(d.read_text(encoding="utf-8")) if d.exists() else {}
    return urls, done


def write_done(repo: Path, done: dict) -> None:
    p = repo / DONE
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(done, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def snapshot_relpath(url: str) -> str | None:
    """Relative path under /opt/swccg-res/snapshots for a swccg.com snapshot URL, or None."""
    try:
        p = urllib.parse.urlsplit(url.strip())
    except ValueError:
        return None
    if (p.hostname or "").lower() not in SNAPSHOT_HOSTS:
        return None
    parts = [x for x in p.path.split("/") if x]
    if len(parts) < 2 or parts[0] != "snapshots" or ".." in parts:
        return None
    rel = "/".join(parts[1:])
    return rel or None


def snapshot_file(url: str, root: Path | None = None) -> Path | None:
    rel = snapshot_relpath(url)
    if not rel:
        return None
    base = (root or snapshot_root()).resolve()
    dest = (base / rel).resolve()
    try:
        dest.relative_to(base)
    except ValueError:
        return None
    if dest == base:
        return None
    return dest


def capture_timestamp(capture: str) -> str:
    m = re.search(r"/web/(\d{14})", capture or "")
    return m.group(1) if m else ""


def wiki_api(params: dict) -> dict:
    req = urllib.request.Request(
        WIKI_API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def snapshot_rel_from_el_to_path(path: str) -> str | None:
    """Parse snapshot rel from externallinks.el_to_path or a full Wayback URL."""
    m = WB_SNAPSHOT.match(path or "")
    if m:
        rel = urllib.parse.unquote(m.group(1).split("#")[0].split("?")[0])
        return rel or None
    m = WB_SNAPSHOT_IN_PATH.search(path or "")
    if not m:
        return None
    rel = urllib.parse.unquote(m.group(1).split("#")[0].split("?")[0])
    if not rel or ".." in rel.split("/"):
        return None
    return rel


def wiki_snapshot_wayback_paths_from_db() -> set[str] | None:
    """All ns0 Wayback snapshot paths from MediaWiki externallinks (no 20k API cap)."""
    try:
        proc = subprocess.run(
            [
                "docker", "exec", "-i", WIKI_DB_CONTAINER,
                "sh", "-c",
                'export MYSQL_PWD="$MYSQL_PASSWORD"; mysql -N -u"$MYSQL_USER" "$MYSQL_DATABASE"',
            ],
            input=WIKI_CITE_SQL.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as ex:
        print("WIKI-CITE-DB-ERR", type(ex).__name__, str(ex)[:80], flush=True)
        return None
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", "replace").strip().splitlines()
        tail = err[-1][:120] if err else f"rc={proc.returncode}"
        print("WIKI-CITE-DB-ERR", tail, flush=True)
        return None
    out: set[str] = set()
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        rel = snapshot_rel_from_el_to_path(line.strip())
        if rel:
            out.add(rel)
    return out


def wiki_snapshot_wayback_paths_from_api(get_json) -> set[str]:
    """exturlusage of web.archive.org/web/ — truncated (~20k rows). Fallback only."""
    out: set[str] = set()
    cont: dict = {}
    pages = 0
    while True:
        q = {
            "action": "query", "list": "exturlusage",
            "euquery": "web.archive.org/web/",
            "euprotocol": "https",
            "eulimit": "500",
            "euprop": "title|url",
            "eunamespace": "0",
            "format": "json", "formatversion": "2",
        }
        q.update(cont)
        d = get_json(q)
        for e in d.get("query", {}).get("exturlusage", []):
            rel = snapshot_rel_from_el_to_path(e.get("url") or "")
            if rel:
                out.add(rel)
        pages += 1
        if "continue" not in d or pages >= 40:
            break
        cont = d["continue"]
    return out


def wiki_snapshot_wayback_paths(get_json=None) -> set[str]:
    """Relative snapshot paths that a main-namespace article cites via a Wayback URL."""
    if get_json is None:
        db = wiki_snapshot_wayback_paths_from_db()
        if db is not None:
            print("wiki wayback snapshot cites", len(db), "via db", flush=True)
            return db
        print("wiki wayback snapshot cites db-miss, falling back to exturlusage", flush=True)
        get_json = wiki_api
    out = wiki_snapshot_wayback_paths_from_api(get_json)
    print("wiki wayback snapshot cites", len(out), "via api", flush=True)
    return out


class DeleteBudget:
    """Strict re-checks allowed before deletes in one run (archive.org refuses bursts)."""
    left = DELETE_CHECKS_PER_RUN


def delete_check(url: str, e: dict) -> tuple[bool, str]:
    """Re-check a verified capture right before its staging file is deleted (2026-10-26)."""
    cap = e.get("capture") or ""
    age = capture_age(cap)
    if age is None or age < DELETE_MIN_AGE:
        return False, "capture younger than DELETE_MIN_AGE"
    if DeleteBudget.left <= 0:
        return False, "delete re-check budget used up this run"
    DeleteBudget.left -= 1
    try:
        ok, why = strict_check(cap)
    except VerifyRetry as ex:
        return False, f"retry: {ex}"
    finally:
        time.sleep(VERIFY_GAP_S)
    if ok and why != "ok":
        return False, "retry: " + why  # replay works but not indexed yet: keep the file
    return ok, why


def delete_verified_snapshot(url: str, e: dict, root: Path | None = None,
                             log_path: Path | None = None,
                             cited_paths: set[str] | None = None) -> bool:
    """Delete the staging file when verified AND a wiki article cites a Wayback URL of that path
    AND the capture passes strict_check again now (never on the stored 'verified' alone)."""
    if e.get("status") != "verified":
        return False
    rel = snapshot_relpath(url)
    if not rel:
        return False
    fp = snapshot_file(url, root)
    if fp is None or not fp.is_file() or fp.name == "DELETED-after-wayback.log":
        return False
    if not cited_paths or rel not in cited_paths:
        print("KEEP-UNCITED", rel, flush=True)
        return False
    good, why = delete_check(url, e)
    if not good:
        print("KEEP-UNCHECKED", rel, why, flush=True)
        if not why.startswith(("retry:", "capture younger", "delete re-check budget")):
            # the stored "verified" was wrong: demote so the URL is looked at / recaptured
            demote(url, e, why, root)
            DEMOTED[url] = e
        return False
    method = (e.get("verify") or {}).get("method") or "checked"
    ts = capture_timestamp(e.get("capture") or "")
    size = fp.stat().st_size
    fp.unlink()
    line = f"{iso(now())}\tdelete\t{rel}\t{ts}\tverified ({method}) cited-on-wiki by wayback_worker\n"
    log = log_path or snapshot_log()
    try:
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError as ex:
        print("DELETE-LOG-ERR", rel, ex, flush=True)
    print("DELETED", rel, size, ts, flush=True)
    return True


DEMOTED: dict[str, dict] = {}


def demote(url: str, e: dict, why: str, root: Path | None = None) -> None:
    """A stored 'verified' capture failed strict_check. swccg.com snapshots whose staging file still
    exists, and ordinary live URLs (not PC/forum hosts), are re-saved (status retry, fresh tries);
    a snapshot whose file is gone, or a banned host, becomes unverified."""
    e["dead_capture"] = e.get("capture", "")
    e["verify"] = {"at": iso(now()), "method": "strict", "reason": why[:120]}
    e["last"] = iso(now())
    fp = snapshot_file(url, root)
    live_ok = fp is None and not banned(url)  # an ordinary live URL (never PC/forum): re-save it
    if (fp is not None and fp.is_file()) or live_ok:
        e.update(status="retry", tries=0, recapture=True)
        e["last"] = iso(now() - RETRY_AFTER)
    else:
        e["status"] = "unverified"  # staging file gone or banned host: needs a person/bot
    print("DEMOTED", e["status"], url, why[:80], flush=True)


def recheck_replay_only(done: dict, changed: dict, deadline: float) -> None:
    """Re-check verified captures that were not in CDX yet (index pending) once a day."""
    rows = []
    for url, e in done.items():
        if not isinstance(e, dict):
            continue
        v = e.get("verify") or {}
        if e.get("status") == "verified" and v.get("index") == "pending":
            last = v.get("rechecked") or v.get("at")
            try:
                if last and now() - parse(last) < RECHECK_AFTER:
                    continue
            except ValueError:
                pass
            rows.append(url)
    for url in rows[:RECHECKS_PER_RUN]:
        if time.monotonic() > deadline:
            break
        e = done[url]
        try:
            ok, why = strict_check(e["capture"])
        except VerifyRetry:
            print("archive.org not answering; replay-only recheck stops", flush=True)
            break
        if ok:
            e["verify"]["rechecked"] = iso(now())
            if why == "ok":
                e["verify"]["index"] = "cdx"
        else:
            demote(url, e, why)
        changed[url] = e
        time.sleep(VERIFY_GAP_S)


def prune_verified_snapshots(done: dict, root: Path | None = None,
                             log_path: Path | None = None,
                             cited_paths: set[str] | None = None) -> int:
    if cited_paths is None:
        try:
            cited_paths = wiki_snapshot_wayback_paths()
        except Exception as ex:  # noqa: BLE001
            print("WIKI-CITE-ERR skip deletes", ex, flush=True)
            return 0
    n = 0
    for url, e in done.items():
        if isinstance(e, dict) and delete_verified_snapshot(
            url, e, root, log_path, cited_paths=cited_paths
        ):
            n += 1
    if n:
        print("pruned", n, "verified snapshots", flush=True)
    return n


def confirm(url: str, e: dict) -> bool:
    """Resolve a pending entry. Returns True if it changed.

    Raises StatusRetry when web.archive.org is unreachable so the caller can
    stop the pending walk for this run.
    """
    if e.get("job_id") and AUTH:
        try:
            st = spn2_status(e["job_id"])
        except (StatusRetry, Paused):
            raise
        except Exception as ex:  # noqa: BLE001
            print("STATUS-ERR", url, str(ex)[:80], flush=True)
            if archive_unreachable(ex):
                raise StatusRetry(str(ex)[:80]) from ex
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
                try_verify(url, e)
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
    if e["status"] == "ok":
        try_verify(url, e)
    return True


def reconcile_recovery_probe(control: Control, done: dict, changed: dict, deadline: float) -> None:
    """One accepted canary bypasses the ordinary pending-job age window.

    Never resubmit an acknowledged probe merely because it was offline. Poll or
    verify it once per run; an unresolved24h outcome becomes an explicit repair.
    """
    probe = control.state.get("probe_url")
    if control.state["mode"] != "half_open" or not probe:
        return
    entry = done.get(probe)
    if not entry or not (entry.get("job_id") or entry.get("capture")):
        control.probe_needs_repair("accepted canary receipt is missing")
    if time.monotonic() > deadline - 60:
        return
    if control.state.get("probe_started_at") is None:
        try:
            value = control.state.get("last_submission_attempt_at") or entry["last"]
            date = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if date.tzinfo is None:
                raise ValueError("canary time has no timezone")
            started = date.timestamp()
        except (KeyError, ValueError):
            control.probe_needs_repair("accepted canary age cannot be established")
        control.state["probe_started_at"] = started
        control.save()
    try:
        if entry.get("status") == "pending":
            if confirm(probe, entry):
                changed[probe] = entry
        elif entry.get("status") == "ok":
            try_verify(probe, entry)
            changed[probe] = entry
    except StatusRetry as ex:
        print("CONFIRM-DEFER", probe, str(ex)[:80], flush=True)
    control.checkpoint(done, control.initial_done)
    if (entry.get("status") != "verified" and
            control.clock() - control.state["probe_started_at"] >= Control.PROBE_DEADLINE):
        control.probe_needs_repair("accepted canary unresolved after24hours")


def registry_repair(control: Control, phase: str, error: Exception) -> None:
    """Persist only metadata; exception messages can contain private URLs/keys."""
    repair = {"schema": 1, "status": "open", "repair_issue": 410,
              "owner": "server-wayback-owner", "updated_at": iso(now()),
              "continuation": "existing owner retries this phase on its next eligible run",
              "phase": phase, "error_type": type(error).__name__}
    atomic_json(control.directory / "registry-repair.json", repair)


def registry_recovered(control: Control, phase: str) -> None:
    path = control.directory / "registry-repair.json"
    if path.exists():
        repair = json.loads(path.read_text(encoding="utf-8"))
        if repair.get("phase") == phase and repair.get("status") == "open":
            repair.update(status="resolved", updated_at=iso(now()))
            atomic_json(path, repair)


def prune_legacy_snapshots(control: Control, done: dict) -> None:
    if getattr(control, "registry_prepare_failed", False):
        return
    try:
        protected = {snapshot_file(url) for url in control.registry_adapter.protected_snapshot_urls()}
        protected.discard(None)
        candidates = {url: entry for url, entry in done.items()
                      if snapshot_file(url) not in protected}
    except Exception as error:
        # An incomplete inventory must never authorize even legacy deletions.
        registry_repair(control, "prune-inventory", error)
        return
    registry_recovered(control, "prune-inventory")
    prune_verified_snapshots(candidates)


def native_capture_scope(control: Control, object_ids) -> set[str] | None:
    """Resolve a bounded installed approval without changing the owner or provider."""
    if object_ids is None:
        return None
    if isinstance(object_ids, (str, bytes)):
        raise ValueError("native cohort must list exact object identities")
    keys = set(object_ids)
    if not 1 <= len(keys) <= 6 or any(not isinstance(k, str) or not re.fullmatch(r"[0-9a-f]{64}", k) for k in keys):
        raise ValueError("native capture requires one to six exact object identities")
    registry = control.directory / "registry"
    if not keys <= load_allowed_objects(registry):
        raise PermissionError("native cohort lacks installed owner approval")
    found, urls = set(), set()
    for entry in iter_records(registry, object_ids=keys):
        request = entry["request"]
        source = request["source"]
        key = registration_object_id(request["subject"], source)
        if (source.get("representation") != NATIVE_REPRESENTATION or
                validate_native_mirror(source) or object_state(request) != "ready" or
                suppressed_source(registry, source) or suppressed_url(registry, source["url"])):
            raise PermissionError("native cohort requires checked, ready, non-withdrawn originals")
        found.add(key)
        urls.add(source["url"])
    if found != keys or len(urls) != len(keys):
        raise ValueError("native cohort has missing or duplicate capture identities")
    if control.state.get("probe_url") and control.state["probe_url"] not in urls:
        raise Paused("existing recovery probe is outside the bounded native cohort")
    return urls


def _run(repo: Path, minutes: float, control: Control, *, native_object_ids=None) -> None:
    scope = native_capture_scope(control, native_object_ids)
    gap = max(GAP_S, 60) if scope is not None else GAP_S
    submit_limit = min(MAX_SUBMITS_PER_RUN or 6, 6) if scope is not None else MAX_SUBMITS_PER_RUN
    reset_to_origin(repo)
    urls, done = load(repo)
    control.done = done
    control.initial_done = json.loads(json.dumps(done))
    restored = control.restore_updates(done)
    deadline = time.monotonic() + minutes * 60
    changed: dict[str, dict] = dict(restored)
    apply_verify_inbox(control, done, changed, allowed_urls=scope)
    errors_in_row = 0
    print("auth:", "SPN2 authenticated" if AUTH else "anonymous", flush=True)
    print(
        f"pace: gap={gap}s max_submits={submit_limit or 'uncapped'}",
        flush=True,
    )
    submission_session = {"authenticated": bool(AUTH)}

    # Recovery is not stranded behind the ordinary2h pending-confirm cutoff.
    reconcile_recovery_probe(control, done, changed, deadline)
    control.registry_deadline = deadline
    control.registry_prepare_failed = False
    try:
        allowed = load_allowed_objects(control.directory / "registry") if scope is None else set(native_object_ids)
        adapter = OwnerAdapter(sys.modules[__name__], repo, control, allowed,
                               limit=2 if scope is None else len(allowed))
        control.registry_adapter = adapter
        prepared = adapter.prepare(deadline)
        done.update(prepared["ledger_updates"])
        changed.update(prepared["ledger_updates"])
        registry_recovered(control, "prepare")
    except Paused:
        raise
    except Exception as error:
        control.registry_prepare_failed = True
        registry_repair(control, "prepare", error)
    control.checkpoint(done, control.initial_done)
    # Queue appends may reset the shared checkout; keep our journal-backed ledger.
    urls = load(repo)[0]
    if scope is not None:
        urls = [url for url in urls if url in scope]

    # 1. confirm earlier captures (recent pending only; stop if Wayback is down)
    confirm_done = done if scope is None else {u: e for u, e in done.items() if u in scope}
    confirm_urls = [url for url in pending_confirm_urls(confirm_done) if url != control.state.get("probe_url")]
    print(
        f"pending-confirm {len(confirm_urls)} cap={PENDING_CONFIRM_CAP} "
        f"max_age_s={int(PENDING_CONFIRM_MAX_AGE.total_seconds())}",
        flush=True,
    )
    for url in confirm_urls:
        if time.monotonic() > deadline - 60:
            break
        try:
            if confirm(url, done[url]):
                changed[url] = done[url]
                control.checkpoint(done, control.initial_done)
                time.sleep(1)
        except StatusRetry as ex:
            print("CONFIRM-DEFER pending walk", str(ex)[:80], flush=True)
            break

    # 2. save what is new or due a retry
    submitted: list[str] = []
    save_attempts = 0
    for url in urls:
        if time.monotonic() > deadline - 90 or errors_in_row >= 5:
            break
        if suppressed_url(control.directory / "registry", url):
            continue
        if banned(url):
            continue
        if submit_limit and save_attempts >= submit_limit:
            print("PACE-CAP", submit_limit, "Save Page Now attempts this run", flush=True)
            break
        if not control.may_submit(url):
            break
        e = done.get(url)
        is_stale = bool(e) and stale(e)
        if e and not is_stale and (e["status"] in ("ok", "verified", "unverified", "pending", "failed")
                                   or now() - parse(e["last"]) < RETRY_AFTER):
            continue
        if is_stale:
            print("STALE", e["status"], url, flush=True)
            if e["status"] == "failed":
                e = dict(e, tries=0)
        registry_epoch = {field: e[field] for field in
                          ("registered_payload_sha256", "registry_job_id", "previous_capture", "recapture")
                          if e and field in e}
        tries = (e or {}).get("tries", 0) + 1
        try:
            control.submitting(url)
            save_attempts += 1
            j = submit_capture(url, e, submission_session)
            if "anonymous_capture" not in j:
                if j.get("recent"):
                    e = {"capture": j["recent"], "status": "ok", "tries": tries, "last": iso(now()),
                         "note": "already archived within 30d"}
                    e.update(registry_epoch)
                    print("RECENT", url, j["recent"], flush=True)
                    try_verify(url, e)
                    done[url] = e
                    changed[url] = e
                    control.checkpoint(done, control.initial_done)
                    errors_in_row = 0
                    time.sleep(gap)
                    continue
                e = {"capture": (e or {}).get("capture", ""), "status": "pending", "tries": tries,
                     "last": iso(now()), "job_id": j["job_id"]}
                submitted.append(url)
                print("SUBMITTED", url, j["job_id"], flush=True)
            else:
                cap = j["anonymous_capture"]
                e = {"capture": cap, "status": "pending", "tries": tries, "last": iso(now())}
                print("SAVED", url, cap, flush=True)
            errors_in_row = 0
        except Paused:
            raise
        except Throttled as ex:
            control.provider_failed(ex.status, ex.retry_after)
        except Exception as ex:  # noqa: BLE001
            e = {"capture": (e or {}).get("capture", ""), "status": "retry" if tries < MAX_TRIES else "failed",
                 "tries": tries, "last": iso(now()), "error": str(ex)[:120]}
            errors_in_row += 1
            print("ERROR", url, str(ex)[:120], flush=True)
        e.update(registry_epoch)
        done[url] = e
        changed[url] = e
        control.checkpoint(done, control.initial_done)
        time.sleep(gap)

    # 3. poll this run's jobs until done or out of time
    while submitted and time.monotonic() < deadline:
        for url in list(submitted):
            try:
                if confirm(url, done[url]):
                    changed[url] = done[url]
            except StatusRetry as ex:
                print("CONFIRM-DEFER", url, str(ex)[:80], flush=True)
                submitted.clear()
                break
            if done[url]["status"] != "pending" or "job_id" not in done[url]:
                submitted.remove(url)
            time.sleep(1)
        if submitted:
            time.sleep(15)

    # 4. verify older loaded captures ("ok"), newest first, in the time left
    stop = min(deadline - 60, time.monotonic() + BACKLOG_SECONDS)
    def due(e: dict) -> bool:  # transient verify errors wait RETRY_AFTER before the next try
        v = e.get("verify") or {}
        return not (v.get("error") and v.get("at") and now() - parse(v["at"]) < RETRY_AFTER)
    backlog = sorted((u for u, e in done.items() if (scope is None or u in scope) and e.get("status") == "ok" and e.get("capture") and due(e)),
                     key=lambda u: done[u].get("last", ""), reverse=True)
    for url in backlog:
        if time.monotonic() > stop:
            break
        try:
            if verify_entry(url, done[url]):
                changed[url] = done[url]
        except VerifyRetry as ex:
            if ex.side == "capture":
                mark_verify_deferred(done[url], str(ex))
                changed[url] = done[url]
            print("VERIFY-DEFER backlog", url, str(ex)[:80], flush=True)
            break
        time.sleep(VERIFY_GAP_S)

    # 4b. re-check verified captures that CDX did not list yet
    selected_done = done if scope is None else {u: e for u, e in done.items() if u in scope}
    recheck_replay_only(selected_done, changed, min(deadline - 45, time.monotonic() + 60))

    # 5. drop staging files whose Wayback capture already matched (Bill 2026-10-14), after a
    #    fresh strict check; entries that fail it are demoted to unverified and pushed
    DEMOTED.clear()
    DeleteBudget.left = DELETE_CHECKS_PER_RUN
    if scope is None:
        prune_legacy_snapshots(control, done)
        changed.update(DEMOTED)

    control.checkpoint(done, control.initial_done)
    persist_changes(repo, done, changed, control.initial_done)
    control.ledger_saved()


def persist_changes(repo: Path, done: dict, changed: dict, baseline: dict) -> None:
    if not changed:
        print("nothing to do")
        return

    callback_ran = False

    def redo() -> list[str]:
        nonlocal callback_ran
        _, fresh = load(repo)
        for url, entry in changed.items():
            if fresh.get(url) != baseline.get(url) and fresh.get(url) != entry:
                raise RuntimeError("Ledger receipt advanced; preserve journal and reconcile before overwrite")
        fresh.update(changed)
        write_done(repo, fresh)
        done.clear()
        done.update(fresh)
        callback_ran = True
        return [DONE]

    # gitsync invokes redo under its short repository lock, including attempt1.
    # Do not write tracked files before that lock or hold it during capture waits.
    ver = sum(1 for e in changed.values() if e["status"] == "verified")
    ok = sum(1 for e in changed.values() if e["status"] in ("ok", "pending"))
    bad = len(changed) - ver - ok
    commit_and_push(repo, [DONE], f"wayback: {ver} verified, {ok} saved/confirmed, {bad} unverified or to retry", redo)
    if not callback_ran:
        raise RuntimeError("Compatible locked-redo Git helper required; pending-job journal retained")
    print("pushed", len(changed), "updates")



def run(repo: Path, minutes: float, *, native_object_ids=None) -> None:
    """One exclusive owner; provider/auth pauses survive Git resets and restarts."""
    global ACTIVE_CONTROL
    try:
        with Control(control_directory(repo), AUTH) as control:
            if native_object_ids is not None:
                if not AUTH:
                    raise PermissionError("bounded native capture requires existing authenticated owner credentials")
                native_object_ids = frozenset(native_object_ids)
                try:
                    native_capture_scope(control, native_object_ids)
                except Paused as error:
                    # An unrelated recovery probe remains exclusively owned by
                    # its existing workflow. Do not begin, reconcile or clear it.
                    print("WAYBACK-PAUSED", str(error), flush=True)
                    return
                control.SUBMISSION_GAP = max(control.SUBMISSION_GAP, 60)
            outcome = "completed"
            control.done = load(repo)[1]
            control.initial_done = json.loads(json.dumps(control.done))
            control.restore_updates(control.done)
            try:
                control.begin()
                ACTIVE_CONTROL = control
                if native_object_ids is None:
                    _run(repo, minutes, control)
                else:
                    _run(repo, minutes, control, native_object_ids=native_object_ids)
            except Paused as error:
                outcome = "paused"
                changed = {u:e for u,e in control.done.items()
                           if e != control.initial_done.get(u)}
                control.checkpoint(control.done, control.initial_done)
                persist_changes(repo, control.done, changed, control.initial_done)
                control.ledger_saved()
                print("WAYBACK-PAUSED", str(error), flush=True)
            except BaseException:
                outcome = "failed"
                control.checkpoint(control.done, control.initial_done)
                # Keep the journal even if Git or this process is unavailable.
                raise
            finally:
                finish_error = None
                adapter = getattr(control, "registry_adapter", None)
                if adapter is not None:
                    try:
                        adapter.finish(control.registry_deadline)
                        registry_recovered(control, "finish")
                    except Exception as error:
                        finish_error = error
                        # Recreate/preserve acknowledged-job recovery even if Git saved.
                        try:
                            control.checkpoint(control.done, control.initial_done)
                        except Exception as journal_error:
                            print("REGISTRY-JOURNAL-ERR", type(journal_error).__name__, flush=True)
                        try:
                            registry_repair(control, "finish", error)
                        except Exception as repair_error:
                            # Keep the primary pause/failure even if storage is broken.
                            print("REGISTRY-REPAIR-ERR", type(repair_error).__name__, flush=True)
                ACTIVE_CONTROL = None
                previously_verified = {u for u,e in control.initial_done.items()
                                       if e.get("status") == "verified"}
                control.reconcile(control.done, previously_verified)
                primary_completed = outcome == "completed"
                if finish_error is not None and primary_completed:
                    outcome = "paused" if isinstance(finish_error, Paused) else "failed"
                health = control.health(control.done, outcome)
                print("WAYBACK-HEALTH", json.dumps(health, sort_keys=True), flush=True)
                if finish_error is not None and primary_completed and not isinstance(finish_error, Paused):
                    raise finish_error
    except Busy:
        print("WAYBACK-BUSY existing owner active; no network request made", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--minutes", type=float, default=10)
    ap.add_argument("--adopt-native-receipt", type=Path,
                    help="Offline owner-locked adoption of a checked native capture bundle")
    ap.add_argument("--approved-receipt-sha256", help="Explicit approval hash of the adoption manifest")
    ap.add_argument("--health", action="store_true", help="Read saved health; no Git or Archive.org request")
    ap.add_argument("--native-cohort-file", type=Path,
                    help="Only installed-approved ready native objects; preserves unrelated jobs and skips pruning")
    a = ap.parse_args()
    native_ids = None
    if a.native_cohort_file:
        if a.health or a.adopt_native_receipt:
            ap.error("native capture cannot be combined with health or adoption")
        with a.native_cohort_file.open("rb") as stream:
            raw = stream.read(65537)
        if len(raw) > 65536:
            ap.error("native cohort metadata exceeds its budget")
        document = json.loads(raw)
        if not isinstance(document, dict) or not isinstance(document.get("object_ids"), list):
            ap.error("native cohort must contain object_ids")
        native_ids = document["object_ids"]
    if a.adopt_native_receipt:
        if a.health or not a.approved_receipt_sha256:
            ap.error("adoption requires its approval hash and cannot be combined with health")
        from preservation_capture_adoption import adopt
        with Control(control_directory(a.repo.resolve()), AUTH) as control:
            print(json.dumps(adopt(sys.modules[__name__], a.repo.resolve(), control,
                                   a.adopt_native_receipt.absolute(), a.approved_receipt_sha256),
                             sort_keys=True))
        return 0
    if a.approved_receipt_sha256:
        ap.error("approval hash requires --adopt-native-receipt")
    if a.health:
        path = control_directory(a.repo) / "health.json"
        print(path.read_text(encoding="utf-8") if path.exists() else '{"outcome":"not_recorded"}')
        return 0
    run(a.repo.resolve(), a.minutes, native_object_ids=native_ids)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
