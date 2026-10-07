#!/usr/bin/env python3
"""Download live wiki File: binaries (images + PDFs) into files/.

    python tools/dump_images.py
    python tools/dump_images.py --limit 20

Skips GEMP xml/text uploads. Writes files/INDEX.tsv (title<TAB>path<TAB>mime<TAB>size).
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
KEEP_MIME = ("image/", "application/pdf")


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
    title = im.get("name") or ""
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
    lines = "".join(f"{t}\t{p}\t{m}\t{s}\n" for t, p, m, s in rows)
    raw = str(index.resolve())
    if os.name == "nt" and not raw.startswith("\\\\?\\"):
        raw = "\\\\?\\" + raw
    with open(raw, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(lines)
    print(f"wrote {n} files skipped {skipped} index {index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
