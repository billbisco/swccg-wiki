#!/usr/bin/env python3
"""Back up our own files as archive.org items (swccg-guild/work#1340, plan item 4).

Save Page Now handles one URL at a time and shares web.archive.org's per-IP
limits. Our own files (wiki images, swccg.com snapshots) are already on disk, so
they go to archive.org directly through its S3 upload API instead: one PUT per
file into a few large items, checked afterwards with one metadata request per
item (archive.org lists the SHA-1 of every file it stored).

Uses the same archive.org keys as the Wayback worker (IA_S3_ACCESS /
IA_S3_SECRET from /etc/swccg-ops/archive-org-s3.env); never prints them.
Honours SlowDown / 503 / 429 and the account's task-queue limit; stops rather
than pushing harder.

  python3 ops/ia_item_backup.py --group snapshots --minutes 50 [--limit N] [--dry-run]
  python3 ops/ia_item_backup.py --group images --minutes 50
  python3 ops/ia_item_backup.py --verify-only
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "swccg-ia-item-backup/1.0 (+https://swccg.com; Refs swccg-guild/work#1340)"
S3 = "https://s3.us.archive.org"
META = "https://archive.org/metadata"
STATE = Path(os.environ.get("IA_BACKUP_STATE", "/root/.local/state/swccg-ia-items"))
KEYS_FILE = Path(os.environ.get("IA_KEYS_FILE", "/etc/swccg-ops/archive-org-s3.env"))
GAP_S = float(os.environ.get("IA_BACKUP_GAP_S", "1.0"))
IMAGES = Path("/mnt/HC_Volume_107153504/wiki_images")
SNAPSHOTS = Path("/opt/swccg-res/snapshots")
SKIP_DIRS = {"thumb", "temp", "lockdir", "deleted", "transcoded"}
SKIP_FILES = {"DELETED-after-wayback.log", ".htaccess", "README"}


def items_for(group: str) -> dict[str, tuple[Path, str, str]]:
    """item id -> (root folder, title, description)"""
    if group == "snapshots":
        return {"swccg-com-snapshots": (SNAPSHOTS, "swccg.com source snapshots",
                "Copies of web pages and documents cited on wiki.swccg.com (Star Wars CCG), as served at "
                "https://swccg.com/snapshots/. Paths in this item match the URL paths after /snapshots/.")}
    if group == "images":
        out = {}
        for d in "0123456789abcdef":
            out[f"swccg-wiki-images-{d}"] = (IMAGES / d, f"SWCCG Wiki files, folder {d}",
                "Original files uploaded to the SWCCG Wiki (https://wiki.swccg.com), hash folder " + d +
                ". Paths match https://swccg.com/wiki/images/" + d + "/…")
        out["swccg-wiki-images-archive"] = (IMAGES / "archive", "SWCCG Wiki files, earlier versions",
            "Earlier versions of files on the SWCCG Wiki (https://wiki.swccg.com/images/archive/…).")
        return out
    raise SystemExit("unknown group " + group)


def keys() -> str:
    acc, sec = os.environ.get("IA_S3_ACCESS"), os.environ.get("IA_S3_SECRET")
    if not (acc and sec) and KEYS_FILE.exists():
        vals = {}
        for line in KEYS_FILE.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                vals[k.strip()] = v.strip().strip('"').strip("'")
        acc, sec = vals.get("IA_S3_ACCESS"), vals.get("IA_S3_SECRET")
    if not (acc and sec):
        raise SystemExit("archive.org keys not found")
    return f"LOW {acc}:{sec}"


def files_under(root: Path):
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name not in SKIP_FILES and not (set(p.relative_to(root).parts[:-1]) & SKIP_DIRS):
            yield p


def hashes(p: Path) -> tuple[str, str]:
    md5, sha1 = hashlib.md5(), hashlib.sha1()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            md5.update(chunk); sha1.update(chunk)
    return md5.hexdigest(), sha1.hexdigest()


def load_ledger() -> dict:
    f = STATE / "ledger.json"
    return json.loads(f.read_text()) if f.exists() else {}


def save_ledger(led: dict) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    tmp = STATE / "ledger.json.part"
    tmp.write_text(json.dumps(led, indent=0, sort_keys=True))
    tmp.replace(STATE / "ledger.json")


class Stop(Exception):
    pass


def request(method, url, auth=None, data=None, headers=None, timeout=600):
    h = {"User-Agent": UA, **(headers or {})}
    if auth:
        h["Authorization"] = auth
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    return urllib.request.urlopen(req, timeout=timeout)


def over_limit(auth: str, item: str) -> bool:
    acc = auth.split()[1].split(":")[0]
    q = urllib.parse.urlencode({"check_limit": 1, "accesskey": acc, "bucket": item})
    with request("GET", f"{S3}/?{q}", timeout=60) as r:
        j = json.loads(r.read())
    return bool(j.get("over_limit"))


def item_owner_ok(item: str, auth: str) -> bool:
    """A new item id only: an id that already exists (anyone's) is never reused
    unless our own ledger already holds files in it."""
    with request("GET", f"{META}/{item}", timeout=60) as r:
        j = json.loads(r.read() or b"{}")
    return not j


def put(auth: str, item: str, name: str, path: Path, md5hex: str, meta: dict, first: bool) -> None:
    url = f"{S3}/{item}/{urllib.parse.quote(name)}"
    h = {"Content-MD5": base64.b64encode(bytes.fromhex(md5hex)).decode(),
         "Content-Length": str(path.stat().st_size),
         "x-archive-queue-derive": "0", "x-archive-keep-old-version": "0"}
    if first:
        h["x-amz-auto-make-bucket"] = "1"
        h["x-archive-size-hint"] = str(10 * 1024 ** 3)
        for k, v in meta.items():
            h[f"x-archive-meta01-{k}" if k == "subject" else f"x-archive-meta-{k}"] = \
                urllib.parse.quote(v) if any(ord(c) > 127 for c in v) else v
    wait = 60
    for attempt in range(4):
        try:
            with path.open("rb") as f, request("PUT", url, auth, f, h) as r:
                r.read()
            return
        except urllib.error.HTTPError as e:
            body = e.read()[:300].decode("utf-8", "replace")
            if e.code == 429:
                raise Stop(f"429 from archive.org S3: {body[:120]}")
            if e.code in (503, 500) or "SlowDown" in body:
                ra = e.headers.get("Retry-After")
                time.sleep(max(wait, int(ra) if ra and ra.isdigit() else 0)); wait *= 2
                continue
            raise RuntimeError(f"HTTP {e.code}: {body[:160]}")
        except OSError as e:
            time.sleep(wait); wait *= 2
            last = str(e)[:120]
            continue
    raise Stop("archive.org S3 kept refusing; stopping this run")


def verify(led: dict, items: list[str]) -> dict:
    """One metadata request per item: mark files whose stored SHA-1 matches."""
    stats = {}
    for item in items:
        try:
            with request("GET", f"{META}/{item}/files", timeout=120) as r:
                files = json.loads(r.read() or b"{}").get("result") or []
        except (urllib.error.URLError, OSError, ValueError) as e:
            print("IA-VERIFY skip", item, str(e)[:80], flush=True); continue
        stored = {f.get("name"): f.get("sha1") for f in files}
        for key, row in led.items():
            if row.get("item") != item or row.get("verified"):
                continue
            if stored.get(row["name"]) == row["sha1"]:
                row["verified"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                stats["verified"] = stats.get("verified", 0) + 1
            elif row["name"] in stored:
                stats["sha1_differs"] = stats.get("sha1_differs", 0) + 1
            else:
                stats["not_listed_yet"] = stats.get("not_listed_yet", 0) + 1
        time.sleep(2)
    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", choices=["snapshots", "images"])
    ap.add_argument("--minutes", type=float, default=50)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify-only", action="store_true")
    a = ap.parse_args()
    led = load_ledger()
    if a.verify_only or not a.group:
        items = sorted({r["item"] for r in led.values() if not r.get("verified")})
        st = verify(led, items); save_ledger(led)
        print("IA-VERIFY", json.dumps(st, sort_keys=True), flush=True)
        return 0
    auth = keys()
    deadline = time.monotonic() + a.minutes * 60
    sent = 0
    stats = {}
    for item, (root, title, desc) in items_for(a.group).items():
        if not root.is_dir():
            continue
        meta = {"mediatype": "data", "collection": "opensource_media",  # Community Data
                "title": title, "description": desc, "creator": "swccg.com", "subject": "Star Wars CCG",
                "source": "https://swccg.com/"}
        first = not any(r.get("item") == item for r in led.values())
        if first and not a.dry_run and not item_owner_ok(item, auth):
            print("IA-ITEM taken", item, flush=True); continue
        for p in files_under(root):
            if time.monotonic() > deadline or (a.limit and sent >= a.limit):
                break
            name = str(p.relative_to(root))
            key = f"{item}/{name}"
            st = p.stat()
            row = led.get(key)
            if row and row.get("size") == st.st_size and row.get("mtime") == int(st.st_mtime):
                continue
            md5hex, sha1hex = hashes(p)
            if row and row.get("sha1") == sha1hex:
                row.update(size=st.st_size, mtime=int(st.st_mtime)); continue
            if a.dry_run:
                stats["would_upload"] = stats.get("would_upload", 0) + 1
                stats["bytes"] = stats.get("bytes", 0) + st.st_size
                sent += 1; continue
            if sent % 50 == 0 and over_limit(auth, item):
                print("IA-PAUSE task queue over limit; stopping this run", flush=True)
                deadline = 0; break
            try:
                put(auth, item, name, p, md5hex, meta, first)
            except Stop as e:
                print("IA-STOP", str(e), flush=True); deadline = 0; break
            except RuntimeError as e:
                print("IA-ERR", key, str(e)[:120], flush=True)
                stats["errors"] = stats.get("errors", 0) + 1
                continue
            first = False
            led[key] = {"item": item, "name": name, "size": st.st_size, "mtime": int(st.st_mtime),
                        "sha1": sha1hex, "put": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            sent += 1; stats["uploaded"] = stats.get("uploaded", 0) + 1
            stats["bytes"] = stats.get("bytes", 0) + st.st_size
            if sent % 25 == 0:
                save_ledger(led)
            time.sleep(GAP_S)
        if deadline == 0:
            break
    save_ledger(led)
    total = {}
    for r in led.values():
        total[r["item"]] = total.get(r["item"], 0) + 1
    print("IA-BACKUP", json.dumps(stats, sort_keys=True), "items", json.dumps(total, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
