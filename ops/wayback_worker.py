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
    if src["status"] != 200:
        raise VerifyRetry(f"source HTTP {src['status']}")
    info = {"at": iso(now()), "capture_id": id_url(capture)}
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


def delete_verified_snapshot(url: str, e: dict, root: Path | None = None,
                             log_path: Path | None = None,
                             cited_paths: set[str] | None = None) -> bool:
    """Delete the staging file when verified AND a wiki article cites a Wayback URL of that path."""
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
        if e and (e["status"] in ("ok", "verified", "unverified", "pending", "failed")
                  or now() - parse(e["last"]) < RETRY_AFTER):
            continue
        tries = (e or {}).get("tries", 0) + 1
        try:
            if AUTH:
                j = spn2_submit(url)
                if j.get("recent"):
                    e = {"capture": j["recent"], "status": "ok", "tries": tries, "last": iso(now()),
                         "note": "already archived within 30d"}
                    print("RECENT", url, j["recent"], flush=True)
                    try_verify(url, e)
                    done[url] = e
                    changed[url] = e
                    errors_in_row = 0
                    time.sleep(GAP_S)
                    continue
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

    # 4. verify older loaded captures ("ok"), newest first, in the time left
    stop = min(deadline - 60, time.monotonic() + BACKLOG_SECONDS)
    def due(e: dict) -> bool:  # transient verify errors wait RETRY_AFTER before the next try
        v = e.get("verify") or {}
        return not (v.get("error") and v.get("at") and now() - parse(v["at"]) < RETRY_AFTER)
    backlog = sorted((u for u, e in done.items() if e.get("status") == "ok" and e.get("capture") and due(e)),
                     key=lambda u: done[u].get("last", ""), reverse=True)
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

    # 5. drop staging files whose Wayback capture already matched (Bill 2026-10-14)
    prune_verified_snapshots(done)

    if not changed:
        print("nothing to do")
        return

    def redo() -> list[str]:
        _, fresh = load(repo)
        fresh.update(changed)
        write_done(repo, fresh)
        prune_verified_snapshots(fresh)
        return [DONE]

    write_done(repo, done)
    ver = sum(1 for e in changed.values() if e["status"] == "verified")
    ok = sum(1 for e in changed.values() if e["status"] in ("ok", "pending"))
    bad = len(changed) - ver - ok
    commit_and_push(repo, [DONE], f"wayback: {ver} verified, {ok} saved/confirmed, {bad} unverified or to retry", redo)
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
