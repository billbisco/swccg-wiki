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
retry (save or check failed; retried later, up to MAX_TRIES) | failed (gave up after MAX_TRIES,
or after PENDING_MAX_CYCLES pending timeouts).

Stuck pending (Chief, 2026-10-20): an entry still "pending" PENDING_TIMEOUT after its "last" stamp
gets an exact-URL CDX lookup; each capture found (newest first) is checked like any other capture.
Verified -> status "verified" with that capture. Otherwise the entry goes back to "retry" for a fresh
save, and after PENDING_MAX_CYCLES timeouts it is "failed". Additive fields: "pending_timeouts" (int),
"pending_timeout" ({"at", "cycle", "result", "cdx_captures", "cdx_timestamp" | "reason"}) and
"stale_job_id". Scomp re-saves (scomp.starwarsccg.org, or its swccg.com/snapshots/scomp/ copies) go last.

Bots: push the URL to queue.txt, then read done.json. Cite the capture once status is "verified".
No Wayback access from the bot's own machine is needed.

Auth: archive.org S3-style keys, IA_S3_ACCESS / IA_S3_SECRET, read from the environment or
from KEYS_FILE (root-only, chmod 600, outside any git repo). They are never logged or committed.
Without keys the worker falls back to the old anonymous GET /save/<url>.

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


def _env_num(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, "") or default)
    except ValueError:
        return default


# Pending timeout (Chief, 2026-10-20). Env vars, or --pending-timeout-hours / --pending-max-cycles.
PENDING_TIMEOUT = timedelta(hours=_env_num("WAYBACK_PENDING_TIMEOUT_HOURS", 6))
PENDING_MAX_CYCLES = int(_env_num("WAYBACK_PENDING_MAX_CYCLES", 3))
PENDING_SECONDS = 120   # time per run spent on timed-out pending entries
CDX_CANDIDATES = 3      # newest exact-URL captures checked per timed-out entry
SCOMP_SNAPSHOT_RX = re.compile(r"^https?://(?:www\.)?swccg\.com/snapshots/scomp/", re.I)


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


EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def parse(s) -> datetime:
    """Timestamps in done.json: "2026-10-20T22:02:22Z" (the worker's own), plus anything a bot or a
    reconciliation may write: +00:00 / -04:00 offsets, fractional seconds, a space instead of "T",
    no zone (taken as UTC), a 14-digit Wayback timestamp, or epoch seconds. Missing or unreadable ->
    EPOCH (very old)."""
    if isinstance(s, (int, float)) and not isinstance(s, bool):
        return datetime.fromtimestamp(s, timezone.utc)
    s = str(s or "").strip()
    if re.fullmatch(r"\d{14}", s):
        return datetime.strptime(s, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    try:
        t = datetime.fromisoformat(re.sub(r"(?i)z$", "+00:00", s))
    except ValueError:
        return EPOCH
    return (t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc)).replace(microsecond=0)


def is_scomp(url: str) -> bool:
    """Scomp card pages and their swccg.com snapshots: always last in the save order (Bill, 2026-10-20)."""
    try:
        host = (urllib.parse.urlsplit(url).hostname or "").lower()
    except ValueError:
        return False
    return host == "scomp.starwarsccg.org" or bool(SCOMP_SNAPSHOT_RX.match(url))


def scomp_last(urls) -> list[str]:
    return sorted(urls, key=is_scomp)  # stable: everything else keeps its order


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
            snap = json.loads(r.read().decode()).get("archived_snapshots", {}).get("closest") or {}
    except Exception:  # noqa: BLE001
        return ""
    cap = snap.get("url", "")
    return cap.replace("http://web.archive.org", "https://web.archive.org") if snap.get("available") else ""


def cdx_captures(url: str, limit: int = CDX_CANDIDATES) -> list[str]:
    """Exact-URL CDX lookup: newest-first capture URLs of url with HTTP 200. Archive.org trouble
    (429, 5xx, connection refused) raises VerifyRetry(side="capture")."""
    q = ("https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(
        {"url": url, "matchType": "exact", "output": "json", "fl": "timestamp,original,statuscode",
         "filter": "statuscode:200", "limit": f"-{limit}"}))
    try:
        with urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": UA}), timeout=90) as r:
            body = r.read().decode("utf-8", "replace").strip()
    except urllib.error.HTTPError as e:
        raise VerifyRetry(f"CDX HTTP {e.code}", side="capture" if e.code == 429 or e.code >= 500 else "source") from e
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        raise VerifyRetry(f"CDX {type(e).__name__}: {str(e)[:80]}", side="capture") from e
    return parse_cdx(body)


def parse_cdx(body: str) -> list[str]:
    rows = json.loads(body) if body else []
    if rows and rows[0] and rows[0][0] == "timestamp":
        rows = rows[1:]
    caps = [f"https://web.archive.org/web/{r[0]}/{r[1]}" for r in rows if len(r) >= 2 and re.fullmatch(r"\d{14}", str(r[0]))]
    return sorted(set(caps), key=lambda c: re.search(r"/web/(\d{14})", c).group(1), reverse=True)


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
CLOUDFLARE_RX = re.compile(r"<title>\s*(?:Just a moment\.\.\.|Attention Required! \| Cloudflare)|cf-chl-|challenge-platform", re.I)


class VerifyRetry(Exception):
    """Transient: try verifying again on a later run. side="capture" means archive.org itself failed
    (connection refused, 429, 5xx); that does not count against the entry's VERIFY_TRIES and stops
    the backlog pass for the run. Anything else (source unreachable, capture 403/404) counts."""

    def __init__(self, msg: str, side: str = "source"):
        super().__init__(msg)
        self.side = side


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
        return {"status": e.code, "ctype": e.headers.get("Content-Type", "") if e.headers else "", "sha256": "",
                "size": 0, "body": b""}
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError, zlib.error) as e:
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
    try:
        cap = get(id_url(capture))
    except VerifyRetry as ex:
        raise VerifyRetry(f"capture: {ex}", side="capture") from ex
    if cap["status"] != 200:  # 429/5xx = archive.org throttling or outage; 403/404 = this capture's problem
        side = "capture" if cap["status"] == 429 or cap["status"] >= 500 else "source"
        raise VerifyRetry(f"capture HTTP {cap['status']}", side=side)
    src = get(url)
    info = {"at": iso(now()), "capture_id": id_url(capture)}
    if src["status"] in (404, 410) and SNAPSHOT_URL_RX.match(url):
        return snapshot_header_check(cap, info)
    if src["status"] != 200:
        raise VerifyRetry(f"source HTTP {src['status']}")
    if cap["sha256"] == src["sha256"]:
        return "verified", {**info, "method": "sha256", "sha256": src["sha256"], "bytes": src["size"]}
    if not (is_html(src) and is_html(cap)):
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


# Our own swccg.com/snapshots/ pages are deleted from the VPS once Wayback has them
# (snapshots/DELETED-after-wayback.log), so there is no live source to compare with. The capture is
# then checked for the header make_snapshot.py writes: <!-- snapshot-of: <url> captured: <ts> -->.
SNAPSHOT_URL_RX = re.compile(r"^https?://(?:www\.)?swccg\.com/snapshots/.+\.html?$", re.I)
SNAPSHOT_HEADER_RX = re.compile(r"<!--\s*snapshot-of:\s*(\S+)\s+captured:\s*(\S+)")


def snapshot_header_check(cap: dict, info: dict) -> tuple[str, dict]:
    text = cap["body"].decode("utf-8", "replace")
    m = SNAPSHOT_HEADER_RX.search(text[:65536])
    if m and is_html(cap) and not CLOUDFLARE_RX.search(text):
        return "verified", {**info, "method": "snapshot-header", "snapshot_of": m.group(1), "snapshot_captured": m.group(2),
                            "sha256": cap["sha256"], "bytes": cap["size"], "note": "source snapshot deleted after Wayback"}
    return "unverified", {**info, "method": "snapshot-header", "reason": "source snapshot gone and capture has no snapshot-of header"}


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


def try_verify(url: str, e: dict) -> None:
    """Verify right after a capture loads; archive.org errors leave it "ok" for the backlog pass."""
    try:
        verify_entry(url, e)
    except VerifyRetry:
        pass


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
                try_verify(url, e)
        else:
            e["status"] = "retry" if int(e.get("tries", 1) or 1) < MAX_TRIES else "failed"
            e["error"] = str(st.get("status_ext") or st.get("message") or s)[:120]
        e["last"] = iso(now())
        print("CONFIRM", e["status"], url, e.get("capture", ""), flush=True)
        return True
    if not e.get("capture") or now() - parse(e.get("last")) < CHECK_AFTER:
        return False
    e["status"] = "ok" if capture_ok(e["capture"]) else ("retry" if int(e.get("tries", 1) or 1) < MAX_TRIES else "failed")
    e["last"] = iso(now())
    if e["status"] == "ok":
        try_verify(url, e)
    return True


KEEP_FIELDS = ("pending_timeouts", "pending_timeout")


def keep(e: dict | None) -> dict:
    """Fields that survive a re-save (the timeout cycle count must, or the cap never bites)."""
    return {k: e[k] for k in KEEP_FIELDS if e and k in e}


def pending_timed_out(e: dict, at: datetime | None = None) -> bool:
    return e.get("status") == "pending" and (at or now()) - parse(e.get("last")) >= PENDING_TIMEOUT


def resolve_timed_out(url: str, e: dict, cdx=None, get=None) -> str:
    """A pending entry older than PENDING_TIMEOUT: exact-URL CDX, then check each capture (newest first).
    Returns the new status. Raises VerifyRetry(side="capture") if archive.org is not answering; the
    entry is then left as it was."""
    cdx = cdx or cdx_captures
    caps = cdx(url)
    cycle = int(e.get("pending_timeouts", 0) or 0) + 1
    rec = {"at": iso(now()), "cycle": cycle, "cdx_captures": len(caps)}
    last_reason = "no capture in CDX" if not caps else ""
    for i, cap in enumerate(caps):
        if i:
            time.sleep(VERIFY_GAP_S)
        try:
            status, info = verify(url, cap, get)
        except VerifyRetry as ex:
            if ex.side == "capture":
                raise
            last_reason = str(ex)[:120]
            continue
        if status == "verified":
            ts = re.search(r"/web/(\d{14})", cap).group(1)
            e.update(status="verified", capture=cap, verify=info, last=iso(now()), pending_timeouts=cycle,
                     pending_timeout={**rec, "result": "verified", "cdx_timestamp": ts})
            e.pop("job_id", None)
            e.pop("verify_tries", None)
            e.pop("error", None)
            print("PENDING-TIMEOUT verified", url, cap, flush=True)
            return "verified"
        last_reason = info.get("reason", status)
    failed = cycle >= PENDING_MAX_CYCLES
    e.update(status="failed" if failed else "retry", last=iso(now()), pending_timeouts=cycle,
             error=f"pending timeout {cycle}/{PENDING_MAX_CYCLES}: {last_reason}"[:120],
             pending_timeout={**rec, "result": "failed" if failed else "resave", "reason": last_reason})
    if e.get("job_id"):
        e["stale_job_id"] = e.pop("job_id")
    print("PENDING-TIMEOUT", e["status"], url, last_reason[:80], flush=True)
    return e["status"]


def run(repo: Path, minutes: float) -> None:
    reset_to_origin(repo)
    urls, done = load(repo)
    deadline = time.monotonic() + minutes * 60
    changed: dict[str, dict] = {}
    errors_in_row = 0
    backoff = BACKOFF_START
    print("auth:", "SPN2 authenticated" if AUTH else "anonymous", flush=True)

    # 0. pending past PENDING_TIMEOUT: CDX + check, else back to retry (Scomp last), one at a time
    stop0 = min(deadline - 120, time.monotonic() + PENDING_SECONDS)
    for url in scomp_last([u for u, e in done.items() if isinstance(e, dict) and pending_timed_out(e)]):
        if time.monotonic() > stop0:
            break
        try:
            resolve_timed_out(url, done[url])
            changed[url] = done[url]
        except VerifyRetry as ex:
            print("archive.org not answering (", str(ex)[:80], "); pending timeouts stop for this run", flush=True)
            break
        except Exception as ex:  # noqa: BLE001  (bad CDX JSON etc.: leave the entry, go on)
            print("PENDING-TIMEOUT-ERR", url, str(ex)[:80], flush=True)
        time.sleep(VERIFY_GAP_S)

    # 1. confirm earlier captures
    for url, e in list(done.items()):
        if time.monotonic() > deadline - 60:
            break
        if isinstance(e, dict) and e.get("status") == "pending" and confirm(url, e):
            changed[url] = e
            time.sleep(1)

    # 2. save what is new or due a retry
    # Timed-out entries are re-saved even if their URL has left queue.txt; Scomp always goes last.
    resave = [u for u, e in done.items() if isinstance(e, dict) and e.get("status") == "retry" and e.get("pending_timeouts")]
    submitted: list[str] = []
    for url in scomp_last(list(dict.fromkeys(urls + resave))):
        if time.monotonic() > deadline - 90 or errors_in_row >= 5:
            break
        if banned(url):
            continue
        e = done.get(url)
        if e is not None and not isinstance(e, dict):
            continue
        # Only "retry" is due a new save; a status this worker does not know is left alone.
        if e and (e.get("status") != "retry" or now() - parse(e.get("last")) < RETRY_AFTER):
            continue
        try:
            tries = int((e or {}).get("tries", 0) or 0) + 1
        except (TypeError, ValueError):
            tries = 1
        try:
            if AUTH:
                j = spn2_submit(url)
                if j.get("recent"):
                    e = {**keep(e), "capture": j["recent"], "status": "ok", "tries": tries, "last": iso(now()),
                         "note": "already archived within 30d"}
                    print("RECENT", url, j["recent"], flush=True)
                    try_verify(url, e)
                    done[url] = e
                    changed[url] = e
                    errors_in_row = 0
                    time.sleep(GAP_S)
                    continue
                e = {**keep(e), "capture": (e or {}).get("capture", ""), "status": "pending", "tries": tries,
                     "last": iso(now()), "job_id": j["job_id"]}
                submitted.append(url)
                print("SUBMITTED", url, j["job_id"], flush=True)
            else:
                cap = save_anon(url)
                e = {**keep(e), "capture": cap, "status": "pending", "tries": tries, "last": iso(now())}
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
            e = {**keep(e), "capture": (e or {}).get("capture", ""), "status": "retry" if tries < MAX_TRIES else "failed",
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

    # 4. verify older loaded captures ("ok"), newest first, in the time left
    stop = min(deadline - 60, time.monotonic() + BACKLOG_SECONDS)
    def due(e: dict) -> bool:  # transient verify errors wait RETRY_AFTER before the next try
        v = e.get("verify") or {}
        return not (v.get("error") and v.get("at") and now() - parse(v["at"]) < RETRY_AFTER)
    backlog = sorted((u for u, e in done.items() if isinstance(e, dict) and e.get("status") == "ok" and e.get("capture") and due(e)),
                     key=lambda u: parse(done[u].get("last")), reverse=True)
    for url in backlog:
        if time.monotonic() > stop:
            break
        try:
            if verify_entry(url, done[url]):
                changed[url] = done[url]
        except VerifyRetry:
            print("archive.org not answering; backlog stops for this run", flush=True)
            break
        time.sleep(VERIFY_GAP_S)

    if not changed:
        print("nothing to do")
        return

    def redo() -> list[str]:
        _, fresh = load(repo)
        fresh.update(changed)
        write_done(repo, fresh)
        return [DONE]

    write_done(repo, done)
    ver = sum(1 for e in changed.values() if e.get("status") == "verified")
    ok = sum(1 for e in changed.values() if e.get("status") in ("ok", "pending"))
    bad = len(changed) - ver - ok
    commit_and_push(repo, [DONE], f"wayback: {ver} verified, {ok} saved/confirmed, {bad} unverified or to retry", redo)
    print("pushed", len(changed), "updates")


def main() -> int:
    global PENDING_TIMEOUT, PENDING_MAX_CYCLES
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--minutes", type=float, default=10)
    ap.add_argument("--pending-timeout-hours", type=float, default=None,
                    help=f"re-check pending entries older than this (default {PENDING_TIMEOUT.total_seconds() / 3600:g}; env WAYBACK_PENDING_TIMEOUT_HOURS)")
    ap.add_argument("--pending-max-cycles", type=int, default=None,
                    help=f"pending timeouts before status failed (default {PENDING_MAX_CYCLES}; env WAYBACK_PENDING_MAX_CYCLES)")
    a = ap.parse_args()
    if a.pending_timeout_hours is not None:
        PENDING_TIMEOUT = timedelta(hours=a.pending_timeout_hours)
    if a.pending_max_cycles is not None:
        PENDING_MAX_CYCLES = a.pending_max_cycles
    run(a.repo.resolve(), a.minutes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
