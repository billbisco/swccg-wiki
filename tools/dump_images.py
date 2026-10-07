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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", type=Path, default=FILES)
    args = ap.parse_args()
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str, str]] = []
    cont: dict[str, str] = {}
    n = 0
    skipped = 0
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
        for im in data.get("query", {}).get("allimages", []):
            mime = im.get("mime") or ""
            if not any(mime.startswith(k) or mime == k.rstrip("/") for k in KEEP_MIME):
                skipped += 1
                continue
            title = im.get("name") or ""
            url = im.get("url") or ""
            if not title or not url:
                continue
            dest = out / safe_name(title)
            if not dest.exists() or dest.stat().st_size != int(im.get("size") or 0):
                try:
                    write_bytes(dest, download(url))
                except urllib.error.HTTPError as e:
                    print(f"FAIL {title} {e.code}", file=sys.stderr)
                    continue
            if out.resolve() == FILES.resolve():
                rel_s = "files/" + dest.name
            else:
                rel_s = dest.name
            rows.append((title, rel_s, mime, str(im.get("size") or 0)))
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
        time.sleep(0.1)
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
