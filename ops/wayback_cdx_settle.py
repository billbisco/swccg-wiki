#!/usr/bin/env python3
"""Settle Wayback ledger rows for our own files in bulk (swccg-guild/work#1340).

One CDX wildcard request lists every capture under a path, with the SHA-1
digest of the captured bytes. We compare that digest with the SHA-1 of our own
file on disk, so hundreds of rows are checked with a handful of requests and no
replay fetches. Results go to the worker's verify-inbox as schema-1 receipts;
the single Wayback owner applies them (this script never writes done.json).

Exact-URL pass (swccg-guild/work#1375): prefix/wildcard CDX queries do not list
recent captures (measured 26 Nov 2026: `url=swccg.com/wiki/images/&matchType=prefix`
returned 0 rows while an exact `url=<file>&output=json` returned the capture).
So every row the prefix pass leaves unsettled (not indexed, digest differs,
other capture, prefix unavailable; not "no_local_file") is then looked up by
its exact URL, newest ledger activity first, with the same acceptance rules.
Bounded by --exact-max (default 500 lookups per run, 0 turns it off) and
paced by --exact-gap (default 4.0 s between requests). A 429 or a refused /
reset connection stops all CDX requests at once (no retry around a refusal);
a 429's Retry-After, or a refusal (at least REFUSED_HOLD_S, 15 min, the same as the worker's own network_refused cooldown), is kept in
<state>/cdx-settle-hold.json and later runs make no CDX request until it has
passed. A refusal hold is marked "refused": the Wayback worker reads it too
and carries it into its shared cooldown (wayback_worker.cdx_hold_cooldown).

Shared cooldown (#1375 review): before any live CDX request, and again before
each one, the worker's control state (<state>/control.json, written by
wayback_control.Control) is read. A provider circuit that is not healthy
(open / half_open / auth_blocked / probe_blocked), or a next_attempt still in
the future (provider cooldown, capacity wait, refusal), means no CDX request
from here either. --cdx-dir mode makes no network request and ignores this.

--cdx-dir DIR (answers fetched elsewhere, e.g. on Bill's PC, and copied here):
  prefix answers:  DIR/<prefix with "/" and ":" replaced by "_">.json
                   e.g. https___swccg.com_snapshots_forum_.json
  exact answers:   DIR/exact-<sha1>.json, where <sha1> is the lowercase hex
                   SHA-1 of the UTF-8 bytes of the URL exactly as it is keyed
                   in ops/wayback/done.json (no normalising, no %-encoding), e.g.
                   https://swccg.com/snapshots/forum/p1259062.html ->
                   exact-4f200595accd7f6858e738bf0863c4017d8c8be1.json
                   The file holds the raw JSON CDX answer of
                   https://web.archive.org/cdx/search/cdx?url=<URL>&output=json
                   (optionally &filter=statuscode:200 and/or
                   &fl=timestamp,original,statuscode,digest): a list whose first
                   row names the columns. "[]" or an empty file means no capture.
                   Columns are read by name; rows that are not statuscode 200 or
                   whose "original" is another URL are ignored. A missing file
                   only skips that URL.
  `--exact-list FILE` writes the URLs the exact pass would look up (one per
  line, UTF-8), so the fetching side knows what to ask for.

Usage (on gemp):
  python3 ops/wayback_cdx_settle.py [--repo /opt/swccg-ops/repos/swccg-wiki] [--dry-run]
      [--exact-max 500] [--exact-gap 4.0] [--cdx-dir DIR] [--exact-list FILE]
"""
import argparse
import base64
import errno
import hashlib
import http.client
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "swccg-wayback-cdx-settle/1.0 (+https://swccg.com; Refs swccg-guild/work#1340)"
CDX = "https://web.archive.org/cdx/search/cdx"
STATE = Path(os.environ.get("WAYBACK_STATE_DIR", "/root/.local/state/swccg-wayback"))
INBOX = STATE / "verify-inbox"
HOLD = STATE / "cdx-settle-hold.json"
CONTROL = STATE / "control.json"   # wayback_control.Control state file
# URL prefix -> directory on disk holding the same files
ROOTS = {
    "https://swccg.com/snapshots/": Path("/opt/swccg-res/snapshots"),
    "https://swccg.com/wiki/images/": Path("/mnt/HC_Volume_107153504/wiki_images"),
}


def batch_checked(url: str) -> bool:
    """Our own files: checked in bulk from CDX digests, not one replay fetch each."""
    return any(url.startswith(p) for p in ROOTS)
OPEN = {"pending", "ok", "unverified", "retry", "failed"}
GAP_S = 5.0          # between CDX requests
TRIES = 4            # per CDX request, with growing waits
EXACT_MAX = 500      # exact-URL lookups per run
EXACT_GAP_S = 4.0    # between exact-URL lookups
REFUSED_HOLD_S = 15 * 60  # a refusal holds later CDX requests (and, via the shared cooldown, saves) this long; same as the worker
EXACT_ERRORS_STOP = 5  # consecutive failed exact lookups that end the pass
TS_RX = re.compile(r"/web/(\d{14})[a-z_]*/")
PRUNE_LOG = Path("/opt/swccg-res/snapshots/DELETED-after-wayback.log")


class CdxStop(Exception):
    """archive.org said stop (429) or refused the connection: no more CDX requests this run."""

    def __init__(self, reason: str, retry_after=None, refused=False):
        super().__init__(reason)
        self.retry_after = retry_after
        self.refused = refused


def control_blocked(path: Path | None = None, now=None):
    """Why the Wayback worker's shared state forbids archive.org requests, or None.

    Reads the state file wayback_control.Control keeps: mode (healthy / open /
    half_open / auth_blocked / probe_blocked) and next_attempt (epoch of the
    end of the provider cooldown, capacity wait or refusal backoff). A missing
    file means no worker state yet; an unreadable one blocks (fail closed)."""
    path = CONTROL if path is None else path
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        return "worker control state unreadable"
    if not isinstance(state, dict):
        return "worker control state unreadable"
    mode = state.get("mode")
    if mode != "healthy":
        return f"worker circuit is {mode}" + (f" ({state.get('reason')})" if state.get("reason") else "")
    try:
        until = float(state.get("next_attempt") or 0)
    except (TypeError, ValueError):
        return "worker control state unreadable"
    if until > (now or time.time()):
        try:
            when = datetime.fromtimestamp(until, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except (OverflowError, OSError, ValueError):
            when = str(until)
        return ("worker cooldown until " + when +
                (f" ({state.get('provider_event')})" if state.get("provider_event") else ""))
    return None


def prune_proofs(path: Path = PRUNE_LOG) -> dict:
    """URL -> capture timestamp, for files the pruner deleted after a SHA check of that capture."""
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        f = line.split("\t")
        if len(f) >= 5 and f[1] == "delete" and re.fullmatch(r"\d{14}", f[3]) and re.match(r"verified \([^)]*sha", f[4]):
            out["https://swccg.com/snapshots/" + f[2]] = f[3]
    return out


def norm(url: str) -> str:
    s = urllib.parse.urlsplit(url)
    host = (s.hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host
    path = urllib.parse.unquote(s.path)
    return host + path + ("?" + s.query if s.query else "")


def sha1_b32(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return base64.b32encode(h.digest()).decode("ascii")


def local_file(url: str):
    for prefix, root in ROOTS.items():
        if url.startswith(prefix):
            rel = urllib.parse.unquote(url[len(prefix):].split("?", 1)[0])
            p = (root / rel).resolve()
            if root.resolve() in p.parents and p.is_file():
                return p
    return None


def exact_name(url: str) -> str:
    """--cdx-dir file name of the exact answer for url (see the module docstring)."""
    return "exact-" + hashlib.sha1(url.encode("utf-8")).hexdigest() + ".json"


def cdx_rows(prefix: str, get=None):
    """All 200 captures under prefix: {norm(url): [(timestamp, digest), ...]}"""
    get = get or _get
    q = {"url": prefix + "*", "fl": "timestamp,original,statuscode,digest",
         "filter": "statuscode:200", "output": "json"}
    raw = get(CDX + "?" + urllib.parse.urlencode(q))
    rows = json.loads(raw or b"[]")
    out = {}
    for ts, orig, _code, digest in rows[1:]:
        out.setdefault(norm(orig), []).append((ts, digest))
    return out


def exact_query(url: str) -> str:
    return CDX + "?" + urllib.parse.urlencode({"url": url, "output": "json", "filter": "statuscode:200",
                                               "fl": "timestamp,original,statuscode,digest"})


def parse_exact(url: str, raw: bytes):
    """[(timestamp, digest)] of statuscode-200 rows for exactly url, from a JSON CDX answer."""
    text = (raw or b"").decode("utf-8", "replace").strip()
    rows = json.loads(text) if text else []
    if not isinstance(rows, list) or not rows:
        return []
    head = rows[0] if isinstance(rows[0], list) and "timestamp" in rows[0] else None
    if head is None:
        raise ValueError("CDX answer has no header row")
    col = {name: i for i, name in enumerate(head)}
    if "digest" not in col:
        raise ValueError("CDX answer has no digest column")
    want, out = norm(url), []
    for r in rows[1:]:
        if not isinstance(r, list) or len(r) < len(head):
            continue
        if "statuscode" in col and r[col["statuscode"]] != "200":
            continue
        if "original" in col and norm(r[col["original"]]) != want:
            continue
        out.append((r[col["timestamp"]], r[col["digest"]]))
    return out


def _refused(ex) -> bool:
    for _ in range(6):
        if ex is None:
            return False
        r = getattr(ex, "reason", ex)
        if isinstance(r, (ConnectionRefusedError, ConnectionResetError)) or \
                getattr(r, "errno", None) in (errno.ECONNREFUSED, errno.ECONNRESET):
            return True
        ex = ex.__cause__ or ex.__context__
    return False


def _open(url: str) -> bytes:
    """One request. 429 / refused connection -> CdxStop; other trouble -> RuntimeError."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            ra = e.headers.get("Retry-After") if e.headers else None
            raise CdxStop(f"HTTP 429 (Retry-After {ra})", ra) from e
        raise RuntimeError(f"HTTP {e.code}") from e
    except (OSError, http.client.HTTPException) as e:
        if _refused(e):
            raise CdxStop(f"connection refused: {str(e)[:60]}", refused=True) from e
        raise RuntimeError(str(e)[:80]) from e


def _get(url: str) -> bytes:
    """Prefix query: retried with growing waits, except 429 / refusal, which stop the run."""
    wait = 30
    for i in range(TRIES):
        try:
            return _open(url)
        except RuntimeError as e:
            err = str(e)
        print("CDX-RETRY", i + 1, err, flush=True)
        if i + 1 < TRIES:
            time.sleep(wait)
            wait *= 2
    raise RuntimeError("CDX unavailable: " + err)


def _judge(url, e, caps, digest, pruned):
    """Prefix and exact share these acceptance rules. Returns (timestamp, method) or (None, stat)."""
    method = "cdx-sha1"
    if digest:
        match = [ts for ts, d in caps if d == digest]
    elif url in pruned:
        # File was deleted after the pruner SHA-checked this capture;
        # CDX confirms the capture is a 200 in the index.
        match = [ts for ts, _ in caps if ts == pruned[url]]
        method = "cdx-200+prune-log-sha"
    elif TS_RX.search(e.get("capture") or ""):
        # Source file is gone and nothing recorded a hash: the archive
        # copy is the only copy. Accept the ledger's own capture when
        # CDX lists it as a 200; there is nothing left to compare with.
        match = [ts for ts, _ in caps if ts == TS_RX.search(e["capture"]).group(1)]
        method = "cdx-200 (source deleted, no local copy)"
    else:
        return None, "no_local_file"
    if not match:
        return None, ("not_indexed" if not caps else ("digest_differs" if digest else "deleted_capture_not_indexed"))
    m = TS_RX.search(e.get("capture") or "")
    if m:
        if m.group(1) not in match:
            return None, "other_capture_matches"
        return m.group(1), method
    return max(match), method


def _receipt(url, e, ts, method, digest, now):
    cap = e.get("capture") or f"https://web.archive.org/web/{ts}/{url}"
    return {"capture": cap, "status": "verified", "job_id": e.get("job_id") or "",
            "verify": {"at": now, "method": method, "sha1_b32": digest or "",
                       "capture_id": f"https://web.archive.org/web/{ts}id_/{url}",
                       "index": "cdx"}}


def _verified_stat(digest, url, pruned):
    return "verified" if digest else ("verified_pruned" if url in pruned else "verified_source_gone")


def settle(done: dict, prefixes, get=None, sha=None, now=None, pruned=None,
           exact_get=None, exact_max=0, exact_gap=EXACT_GAP_S, sleep=time.sleep, exact_list=None,
           blocked=None):
    """Return (receipts, stats). Pure apart from get/exact_get/sha.

    get(query_url) -> bytes answers prefix queries; exact_get(url) -> bytes
    answers the exact lookup of a ledger URL (default: live CDX, paced by
    exact_gap). exact_max=0 turns the exact pass off. When exact_list is a
    list, the URLs the exact pass would look up are appended to it instead.
    blocked() -> reason | None is asked before every CDX request (main passes
    the worker's shared cooldown for live runs, nothing for --cdx-dir); a
    reason stops all CDX requests."""
    blocked = blocked or (lambda: None)
    sha = sha or (lambda url: (lambda p: sha1_b32(p) if p else None)(local_file(url)))
    now = now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pruned = {} if pruned is None else pruned
    receipts, outcome, extra, digests = {}, {}, {}, {}
    todo = {}
    for url, e in done.items():
        if e.get("status") not in OPEN:
            continue
        for p in prefixes:
            if url.startswith(p):
                todo.setdefault(p, []).append(url)
    stopped = None
    held = None
    for p, urls in todo.items():
        if not stopped:
            held = blocked()
            if held:
                stopped = CdxStop("shared cooldown: " + held)
                print("CDX-SETTLE stop", str(stopped)[:120], flush=True)
        if stopped:
            outcome.update({u: "prefix_unavailable" for u in urls})
            continue
        try:
            index = cdx_rows(p, get)
        except CdxStop as ex:
            stopped = ex
            print("CDX-SETTLE stop", p, str(ex)[:80], flush=True)
            outcome.update({u: "prefix_unavailable" for u in urls})
            continue
        except (RuntimeError, ValueError) as ex:
            print("CDX-SETTLE skip", p, str(ex)[:80], flush=True)
            outcome.update({u: "prefix_unavailable" for u in urls})
            continue
        if get is None: sleep(GAP_S)
        for url in urls:
            e = done[url]
            digest = digests[url] = sha(url)
            ts, how = _judge(url, e, index.get(norm(url), []), digest, pruned)
            if ts is None:
                outcome[url] = how
                continue
            receipts[url] = _receipt(url, e, ts, how, digest, now)
            outcome[url] = _verified_stat(digest, url, pruned)

    # Exact-URL pass for what the prefix answers could not settle (#1375).
    unsettled = [u for u, k in outcome.items() if u not in receipts and k != "no_local_file"]
    unsettled.sort(key=lambda u: (done[u].get("last") or "", u), reverse=True)
    if exact_list is not None:
        exact_list.extend(unsettled[:exact_max] if exact_max else unsettled)
    elif exact_max and unsettled and not stopped:
        live = exact_get is None
        fetch = exact_get or (lambda u: _open(exact_query(u)))
        lookups = settled = errors = 0
        for url in unsettled:
            if lookups >= exact_max:
                extra["exact_over_budget"] = len(unsettled) - lookups
                break
            if live and lookups:
                sleep(exact_gap)
            held = blocked()
            if held:
                stopped = CdxStop("shared cooldown: " + held)
                print("CDX-SETTLE exact stop", str(stopped)[:120], flush=True)
                break
            lookups += 1
            try:
                caps = parse_exact(url, fetch(url))
            except CdxStop as ex:
                stopped = ex
                print("CDX-SETTLE exact stop", str(ex)[:80], flush=True)
                break
            except FileNotFoundError:
                extra["exact_no_answer"] = extra.get("exact_no_answer", 0) + 1
                continue
            except (RuntimeError, ValueError) as ex:
                errors += 1
                extra["exact_unavailable"] = extra.get("exact_unavailable", 0) + 1
                print("CDX-SETTLE exact skip", url, str(ex)[:80], flush=True)
                if errors >= EXACT_ERRORS_STOP:
                    print("CDX-SETTLE exact pass stops after", errors, "errors in a row", flush=True)
                    break
                continue
            errors = 0
            e = done[url]
            digest = digests[url] if url in digests else sha(url)
            ts, how = _judge(url, e, caps, digest, pruned)
            if ts is None:
                outcome[url] = how
                continue
            receipts[url] = _receipt(url, e, ts, how, digest, now)
            outcome[url] = _verified_stat(digest, url, pruned)
            settled += 1
        extra["exact_lookups"] = lookups
        extra["exact_verified"] = settled
    stats = {}
    for k in outcome.values():
        stats[k] = stats.get(k, 0) + 1
    stats.update(extra)
    if stopped:
        stats["stopped"] = str(stopped)[:80]
        if stopped.retry_after is not None:
            stats["retry_after"] = stopped.retry_after
        if stopped.refused:
            stats["refused"] = True
    return receipts, stats


def save_hold(stats: dict, path: Path | None = None, now=None) -> float:
    """Persist a stop: 429 Retry-After, or a refusal for at least REFUSED_HOLD_S.
    Returns the hold length in seconds (0: nothing saved)."""
    path = HOLD if path is None else path
    now = now or time.time()
    wait = retry_after_seconds(stats.get("retry_after"), now) if "retry_after" in stats else 0.0
    if stats.get("refused"):
        wait = max(wait, REFUSED_HOLD_S)
    if wait <= 0:
        return 0.0
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(path.name + ".part")
        tmp.write_text(json.dumps({"until": now + wait, "reason": stats.get("stopped", ""),
                                   "refused": bool(stats.get("refused"))}), encoding="utf-8")
        os.replace(tmp, path)
    except OSError as ex:
        print("CDX-SETTLE hold not saved", ex, flush=True)
        return 0.0
    return wait


def retry_after_seconds(value, now=None) -> float:
    if value is None:
        return 0.0
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        pass
    try:
        from email.utils import parsedate_to_datetime
        return max(0.0, parsedate_to_datetime(value).timestamp() - (now or time.time()))
    except (TypeError, ValueError, IndexError):
        return 0.0


def hold_active(path: Path | None = None, now=None):
    """Epoch until which a saved 429 Retry-After or refusal forbids CDX requests, or None."""
    path = HOLD if path is None else path
    try:
        until = float(json.loads(path.read_text(encoding="utf-8")).get("until", 0))
    except (OSError, ValueError, TypeError, AttributeError):
        return None
    return until if until > (now or time.time()) else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/opt/swccg-ops/repos/swccg-wiki")
    ap.add_argument("--prefix", action="append", help="URL prefix to settle (default: all known roots' subdirs)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cdx-dir", help="read CDX answers saved as files (fetched from another host) instead of "
                    "asking web.archive.org from here; naming in the module docstring")
    ap.add_argument("--exact-max", type=int, default=EXACT_MAX,
                    help="exact-URL lookups per run for rows the prefix pass left unsettled (0: off)")
    ap.add_argument("--exact-gap", type=float, default=EXACT_GAP_S, help="seconds between exact lookups")
    ap.add_argument("--exact-list", type=Path,
                    help="write the URLs the exact pass would look up to this file; no exact lookups")
    a = ap.parse_args()
    done = json.loads((Path(a.repo) / "ops/wayback/done.json").read_text(encoding="utf-8"))
    prefixes = a.prefix
    if not prefixes:  # one request per first-level folder keeps each CDX answer small
        prefixes = sorted({m.group(0) for u, e in done.items() if e.get("status") in OPEN
                           for m in [re.match(r"https://swccg\.com/(?:snapshots|wiki/images)/[^/]+/", u)] if m})
    get = exact_get = None
    if a.cdx_dir:
        def get(url):
            prefix = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["url"][0][:-1]
            f = Path(a.cdx_dir) / (re.sub(r"[/:]", "_", prefix) + ".json")
            if not f.exists():
                raise RuntimeError("no saved CDX answer " + f.name)
            return f.read_bytes()

        def exact_get(url):
            return (Path(a.cdx_dir) / exact_name(url)).read_bytes()  # FileNotFoundError: skipped
    else:
        held = hold_active()
        if held:
            print("CDX-SETTLE", json.dumps({"held_until": datetime.fromtimestamp(held, timezone.utc)
                                            .strftime("%Y-%m-%dT%H:%M:%SZ")}), "no CDX request made", flush=True)
            return 0
        why = control_blocked()
        if why:
            print("CDX-SETTLE", json.dumps({"shared_cooldown": why}), "no CDX request made", flush=True)
            return 0
    listing = [] if a.exact_list else None
    receipts, stats = settle(done, prefixes, get=get, pruned=prune_proofs(), exact_get=exact_get,
                             exact_max=max(0, a.exact_max), exact_gap=max(0.0, a.exact_gap),
                             exact_list=listing, blocked=None if a.cdx_dir else control_blocked)
    print("CDX-SETTLE", json.dumps(stats, sort_keys=True), flush=True)
    if listing is not None:
        a.exact_list.write_text("".join(u + "\n" for u in listing), encoding="utf-8")
        print("exact-list", a.exact_list, len(listing), flush=True)
    if not a.cdx_dir and ("retry_after" in stats or stats.get("refused")):
        wait = save_hold(stats)
        if wait:
            print("CDX-SETTLE hold saved", int(wait), "s", "(refused; the worker honours it)"
                  if stats.get("refused") else "", flush=True)
    if receipts and not a.dry_run:
        INBOX.mkdir(parents=True, exist_ok=True)
        name = datetime.now(timezone.utc).strftime("cdx-settle-%Y%m%dT%H%M%SZ.json")
        tmp = INBOX / (name + ".part")
        tmp.write_text(json.dumps({"schema": 1, "lane": "cdx-sha1", "updates": receipts}), encoding="utf-8")
        tmp.rename(INBOX / name)
        print("inbox", name, len(receipts), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
