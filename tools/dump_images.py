#!/usr/bin/env python3
"""Download live wiki File: uploads (images, PDFs, GEMP importable decklists) into files/.

    python tools/dump_images.py                       # everything, rewrite INDEX
    python tools/dump_images.py --limit 20
    python tools/dump_images.py --mime application/xml --mime text/plain --merge --usage

GEMP importable decklists (application/xml, text/plain) are kept: the wiki is a
preservation archive and every File: upload is backed up (Bill, 2026-10-10).

Writes files/INDEX.tsv (title<TAB>path<TAB>mime<TAB>size). --merge keeps rows already
in INDEX.tsv for files not in this run. --usage also writes files/USAGE.tsv
(file title<TAB>article title) so each file stays tied to the article(s) that use it.
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
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ROOT / "files"
INDEX = FILES / "INDEX.tsv"
API = "https://wiki.swccg.com/api.php"
UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki)"
KEEP_MIME = ("image/", "application/pdf", "application/xml", "text/plain")


def api(params: dict) -> dict:
    q = dict(params)
    q.setdefault("format", "json")
    q.setdefault("formatversion", "2")
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(q),
        headers={"User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))


def safe_name(title: str) -> str:
    name = title.replace(" ", "_").replace(":", "_").replace("/", "_")
    for ch in '?*"<>|':
        name = name.replace(ch, "")
    return name


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = str(path.resolve())
    if os.name == "nt" and not raw.startswith("\\\\?\\"):
        raw = "\\\\?\\" + raw
    with open(raw, "wb") as fh:
        fh.write(data)


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def one(im: dict, out: Path, files_root: Path) -> tuple[str, tuple[str, str, str, str] | None]:
    mime = im.get("mime") or ""
    if not any(mime.startswith(k) or mime == k.rstrip("/") for k in KEEP_MIME):
        return "skip", None
    title = (im.get("name") or "").replace("_", " ")  # same title form as USAGE.tsv
    url = im.get("url") or ""
    if not title or not url:
        return "skip", None
    dest = out / safe_name(title)
    size = int(im.get("size") or 0)
    if not dest.exists() or dest.stat().st_size != size:
        try:
            write_bytes(dest, download(url))
        except urllib.error.HTTPError as e:
            print(f"FAIL {title} {e.code}", file=sys.stderr)
            return "fail", None
    if out.resolve() == files_root.resolve():
        rel_s = "files/" + dest.name
    else:
        rel_s = dest.name
    return "ok", (title, rel_s, mime, str(size))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", type=Path, default=FILES)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--mime", action="append", default=[], help="only this MIME (prefix); repeatable")
    ap.add_argument("--merge", action="store_true", help="keep existing INDEX rows not in this run")
    ap.add_argument("--usage", action="store_true", help="write USAGE.tsv for every wiki file")
    args = ap.parse_args()
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str, str]] = []
    cont: dict[str, str] = {}
    n = 0
    skipped = 0
    workers = max(1, args.workers)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        while True:
            params = {
                "action": "query",
                "list": "allimages",
                "aisort": "name",
                "ailimit": "100",
                "aiprop": "url|size|mime",
            }
            params.update(cont)
            data = api(params)
            batch = data.get("query", {}).get("allimages", [])
            if args.mime:
                keep = [im for im in batch if any((im.get("mime") or "").startswith(m) for m in args.mime)]
                skipped += len(batch) - len(keep)
                batch = keep
            futs = [pool.submit(one, im, out, FILES) for im in batch]
            for fut in as_completed(futs):
                kind, row = fut.result()
                if kind == "skip":
                    skipped += 1
                    continue
                if kind != "ok" or row is None:
                    continue
                rows.append(row)
                n += 1
                if n % 100 == 0:
                    print(f"files {n}", flush=True)
                if args.limit and n >= args.limit:
                    break
            if args.limit and n >= args.limit:
                break
            cont_in = data.get("continue")
            if not cont_in:
                break
            cont = {k: str(v) for k, v in cont_in.items()}
            time.sleep(0.05)
    index = out / "INDEX.tsv" if out != FILES else INDEX
    if args.merge and index.exists():
        fresh = {r[0] for r in rows}
        for line in index.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) == 4 and parts[0] not in fresh:
                rows.append(tuple(parts))
    rows.sort(key=lambda r: r[0])
    lines = "".join(f"{t}\t{p}\t{m}\t{s}\n" for t, p, m, s in rows)
    raw = str(index.resolve())
    if os.name == "nt" and not raw.startswith("\\\\?\\"):
        raw = "\\\\?\\" + raw
    with open(raw, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(lines)
    print(f"wrote {n} files skipped {skipped} index {index}")
    if args.usage:
        write_usage(index.parent / "USAGE.tsv")
    return 0


def write_usage(path: Path) -> None:
    """file title<TAB>article title for every wiki file (one row per use; '-' if unused)."""
    out: list[str] = []
    cont: dict[str, str] = {}
    while True:
        params = {
            "action": "query",
            "generator": "allimages",
            "gailimit": "50",
            "prop": "fileusage",
            "fulimit": "max",
        }
        params.update(cont)
        data = api(params)
        for p in data.get("query", {}).get("pages", []):
            name = p["title"].split(":", 1)[1]
            uses = [u["title"] for u in p.get("fileusage", [])]
            for u in uses or ["-"]:
                out.append(f"{name}\t{u}\n")
        cont_in = data.get("continue")
        if not cont_in:
            break
        cont = {k: str(v) for k, v in cont_in.items()}
        time.sleep(0.05)
    out = sorted(set(out))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(out)
    print(f"usage rows {len(out)} -> {path}")


if __name__ == "__main__":
    raise SystemExit(main())
