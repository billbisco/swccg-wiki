#!/usr/bin/env python3
"""Settle Wayback ledger rows for our own files in bulk (swccg-guild/work#1340).

One CDX wildcard request lists every capture under a path, with the SHA-1
digest of the captured bytes. We compare that digest with the SHA-1 of our own
file on disk, so hundreds of rows are checked with a handful of requests and no
replay fetches. Results go to the worker's verify-inbox as schema-1 receipts;
the single Wayback owner applies them (this script never writes done.json).

Usage (on gemp):
  python3 ops/wayback_cdx_settle.py [--repo /opt/swccg-ops/repos/swccg-wiki] [--dry-run]
"""
import argparse
import base64
import hashlib
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
INBOX = Path(os.environ.get("WAYBACK_STATE_DIR", "/root/.local/state/swccg-wayback")) / "verify-inbox"
# URL prefix -> directory on disk holding the same files
ROOTS = {
    "https://swccg.com/snapshots/": Path("/opt/swccg-res/snapshots"),
}
OPEN = {"pending", "ok", "unverified", "retry", "failed"}
GAP_S = 5.0          # between CDX requests
TRIES = 4            # per CDX request, with growing waits
TS_RX = re.compile(r"/web/(\d{14})[a-z_]*/")
PRUNE_LOG = Path("/opt/swccg-res/snapshots/DELETED-after-wayback.log")


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


def _get(url: str) -> bytes:
    wait = 30
    for i in range(TRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                ra = e.headers.get("Retry-After")
                raise SystemExit(f"CDX-SETTLE 429 (Retry-After {ra}); stopping") from e
            err = f"HTTP {e.code}"
        except OSError as e:
            err = str(e)[:80]
        print("CDX-RETRY", i + 1, err, flush=True)
        if i + 1 < TRIES:
            time.sleep(wait)
            wait *= 2
    raise RuntimeError("CDX unavailable: " + err)


def settle(done: dict, prefixes, get=None, sha=None, now=None, pruned=None):
    """Return (receipts, stats). Pure apart from get/sha."""
    sha = sha or (lambda url: (lambda p: sha1_b32(p) if p else None)(local_file(url)))
    now = now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pruned = {} if pruned is None else pruned
    receipts, stats = {}, {}
    def bump(k): stats[k] = stats.get(k, 0) + 1
    todo = {}
    for url, e in done.items():
        if e.get("status") not in OPEN:
            continue
        for p in prefixes:
            if url.startswith(p):
                todo.setdefault(p, []).append(url)
    for p, urls in todo.items():
        try:
            index = cdx_rows(p, get)
        except (RuntimeError, ValueError) as ex:
            print("CDX-SETTLE skip", p, str(ex)[:80], flush=True)
            stats["prefix_unavailable"] = stats.get("prefix_unavailable", 0) + len(urls)
            continue
        if get is None: time.sleep(GAP_S)
        for url in urls:
            e = done[url]
            digest = sha(url)
            caps = index.get(norm(url), [])
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
                bump("no_local_file"); continue
            if not match:
                bump("not_indexed" if not caps else ("digest_differs" if digest else "deleted_capture_not_indexed")); continue
            m = TS_RX.search(e.get("capture") or "")
            if m:
                if m.group(1) not in match:
                    bump("other_capture_matches"); continue
                ts = m.group(1)
            else:
                ts = max(match)
            cap = e.get("capture") or f"https://web.archive.org/web/{ts}/{url}"
            receipts[url] = {"capture": cap, "status": "verified", "job_id": e.get("job_id") or "",
                             "verify": {"at": now, "method": method, "sha1_b32": digest or "",
                                        "capture_id": f"https://web.archive.org/web/{ts}id_/{url}",
                                        "index": "cdx"}}
            bump("verified" if digest else ("verified_pruned" if url in pruned else "verified_source_gone"))
    return receipts, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/opt/swccg-ops/repos/swccg-wiki")
    ap.add_argument("--prefix", action="append", help="URL prefix to settle (default: all known roots' subdirs)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cdx-dir", help="read CDX answers saved as <dir>/<prefix with / and : as _>.json "
                    "(fetched from another host) instead of asking web.archive.org from here")
    a = ap.parse_args()
    done = json.loads((Path(a.repo) / "ops/wayback/done.json").read_text(encoding="utf-8"))
    prefixes = a.prefix
    if not prefixes:  # one request per first-level folder keeps each CDX answer small
        prefixes = sorted({m.group(0) for u in done
                           for m in [re.match(r"https://swccg\.com/snapshots/[^/]+/", u)] if m})
    get = None
    if a.cdx_dir:
        def get(url):
            prefix = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["url"][0][:-1]
            f = Path(a.cdx_dir) / (re.sub(r"[/:]", "_", prefix) + ".json")
            if not f.exists():
                raise RuntimeError("no saved CDX answer " + f.name)
            return f.read_bytes()
    receipts, stats = settle(done, prefixes, get=get, pruned=prune_proofs())
    print("CDX-SETTLE", json.dumps(stats, sort_keys=True), flush=True)
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
