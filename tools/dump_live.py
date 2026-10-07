#!/usr/bin/env python3
"""Dump current wikitext from wiki.swccg.com into pages/.

Live wiki is the source of truth. Run locally or from GitHub Actions:

    python tools/dump_live.py
    python tools/dump_live.py --titles-only
    python tools/dump_live.py --from-tsv path/to/delta.tsv
    python tools/dump_live.py --limit 20
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
PAGES = ROOT / "pages"
INDEX = PAGES / "INDEX.tsv"
API = "https://wiki.swccg.com/api.php"
UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki)"

# Main, Project, MediaWiki, Template, Help, Category, Card.
NAMESPACES = (0, 4, 8, 10, 12, 14, 3000)


def wiki_fname(title: str) -> str:
    name = title.replace(" ", "_").replace(":", "_").replace("/", "_")
    for ch in '?*"<>|':
        name = name.replace(ch, "")
    return name + ".wiki"


def dest_for(title: str, existing: dict[str, Path]) -> Path:
    key = wiki_fname(title)
    if key in existing:
        return existing[key]
    stub = PAGES / "player-stubs" / key
    if stub.exists():
        return stub
    return PAGES / key


def dest_from_tsv(title: str, rel: str, existing: dict[str, Path]) -> Path:
    rel = rel.replace("\\", "/").lstrip("/")
    if rel.startswith("pages/"):
        return ROOT / rel
    return dest_for(title, existing)


def load_tsv(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    seen: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or "\t" not in line:
            continue
        title, rel = line.split("\t", 1)
        title, rel = title.strip(), rel.strip().replace("\\", "/")
        if not title:
            continue
        if title in seen:
            rows[seen[title]] = (title, rel)
        else:
            seen[title] = len(rows)
            rows.append((title, rel))
    return rows


def page_text(page: dict) -> str | None:
    if page.get("missing"):
        return None
    revs = page.get("revisions") or []
    if not revs:
        return None
    slot = revs[0].get("slots", {}).get("main", {})
    text = slot.get("content")
    if text is None:
        text = revs[0].get("content")
    if text is None:
        return None
    if not text.endswith("\n"):
        text += "\n"
    return text.replace("\r\n", "\n").replace("\r", "\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = str(path.resolve())
    if os.name == "nt" and not raw.startswith("\\\\?\\"):
        raw = "\\\\?\\" + raw
    with open(raw, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def write_index(rows: list[tuple[str, str]]) -> None:
    ordered = sorted(rows, key=lambda kv: kv[0].casefold())
    write_text(INDEX, "".join(f"{t}\t{p}\n" for t, p in ordered))


def api(params: dict) -> dict:
    params = dict(params)
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    params.setdefault("maxlag", "5")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) or e.code == 503:
                time.sleep(min(30, 2 ** attempt))
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"API failed after retries: {params.get('action')}")


def index_existing() -> dict[str, Path]:
    found: dict[str, Path] = {}
    if not PAGES.exists():
        return found
    for path in PAGES.rglob("*.wiki"):
        found[path.name] = path
    return found


def dump_titles(ns: int, existing: dict[str, Path], limit: int, written: list[tuple[str, str]]) -> None:
    cont: dict[str, str] = {}
    while True:
        params = {
            "action": "query",
            "list": "allpages",
            "apnamespace": str(ns),
            "aplimit": "500",
        }
        params.update(cont)
        data = api(params)
        for page in data.get("query", {}).get("allpages", []):
            title = page.get("title") or ""
            if not title:
                continue
            dest = dest_for(title, existing)
            rel = dest.relative_to(ROOT).as_posix()
            written.append((title, rel))
            if limit and len(written) >= limit:
                return
        cont_in = data.get("continue")
        if not cont_in:
            return
        cont = {k: str(v) for k, v in cont_in.items()}
        time.sleep(0.1)


def dump_namespace(ns: int, existing: dict[str, Path], limit: int, written: list[tuple[str, str]]) -> None:
    cont: dict[str, str] = {}
    while True:
        params = {
            "action": "query",
            "generator": "allpages",
            "gapnamespace": str(ns),
            "gaplimit": "50",
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
        }
        params.update(cont)
        data = api(params)
        pages = data.get("query", {}).get("pages", [])
        for page in pages:
            title = page.get("title") or ""
            text = page_text(page)
            if not title or text is None:
                continue
            dest = dest_for(title, existing)
            write_text(dest, text)
            existing[dest.name] = dest
            rel = dest.relative_to(ROOT).as_posix()
            written.append((title, rel))
            if len(written) % 200 == 0:
                print(f"ns {ns} {len(written)} pages", flush=True)
            if limit and len(written) >= limit:
                return
        cont_in = data.get("continue")
        if not cont_in:
            return
        cont = {k: str(v) for k, v in cont_in.items()}
        time.sleep(0.15)


def dump_from_tsv(
    tsv: Path, existing: dict[str, Path], written: list[tuple[str, str]]
) -> list[str]:
    rows = load_tsv(tsv)
    if not rows:
        raise RuntimeError(f"empty TSV: {tsv}")
    wanted = {title: rel for title, rel in rows}
    missing: list[str] = []
    titles = list(wanted)
    batch = 50
    for i in range(0, len(titles), batch):
        chunk = titles[i : i + batch]
        data = api(
            {
                "action": "query",
                "titles": "|".join(chunk),
                "prop": "revisions",
                "rvprop": "content",
                "rvslots": "main",
            }
        )
        query = data.get("query", {})
        aliases = {title: title for title in chunk}
        for row in query.get("normalized") or []:
            if row.get("from") and row.get("to"):
                aliases[row["from"]] = row["to"]
        by_returned: dict[str, dict] = {}
        for page in query.get("pages") or []:
            t = page.get("title") or ""
            if t:
                by_returned[t] = page
        for orig in chunk:
            returned_title = aliases.get(orig, orig)
            page = by_returned.get(returned_title)
            text = page_text(page) if page else None
            if text is None:
                missing.append(orig)
                continue
            dest = dest_from_tsv(orig, wanted[orig], existing)
            write_text(dest, text)
            existing[dest.name] = dest
            rel = dest.relative_to(ROOT).as_posix()
            written.append((orig, rel))
        print(f"tsv {min(i + batch, len(titles))}/{len(titles)} pages", flush=True)
        time.sleep(0.1)
    return missing


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="stop after N pages (debug)")
    ap.add_argument(
        "--titles-only",
        action="store_true",
        help="write pages/INDEX.tsv from live titles; do not rewrite wikitext",
    )
    ap.add_argument(
        "--from-tsv",
        type=Path,
        help="dump only titles listed in a leftover/apply TSV (title<TAB>path)",
    )
    args = ap.parse_args()
    PAGES.mkdir(parents=True, exist_ok=True)
    written: list[tuple[str, str]] = []
    if args.from_tsv:
        tsv = args.from_tsv.expanduser().resolve()
        if not tsv.is_file():
            print(f"missing TSV {tsv}", file=sys.stderr)
            return 1
        missing = dump_from_tsv(tsv, {}, written)
        write_index(_merge_index(written, keep_old=True))
        print(f"wrote {len(written)} pages from {tsv.name} index {INDEX}")
        if missing:
            print("MISSING " + "; ".join(missing), file=sys.stderr)
            return 2
        return 0
    existing = index_existing()
    dump = dump_titles if args.titles_only else dump_namespace
    for ns in NAMESPACES:
        dump(ns, existing, args.limit, written)
        write_index(written if not args.limit else _merge_index(written, keep_old=True))
        print(f"ns {ns} running total {len(written)}", flush=True)
        if args.limit and len(written) >= args.limit:
            break
    rows = written if not args.limit else _merge_index(written, keep_old=True)
    write_index(rows)
    kind = "titles" if args.titles_only else "pages"
    print(f"wrote {len(written)} {kind} index {len(rows)} -> {INDEX}")
    return 0


def _merge_index(written: list[tuple[str, str]], keep_old: bool) -> list[tuple[str, str]]:
    prev: dict[str, str] = {}
    if keep_old and INDEX.exists():
        for line in INDEX.read_text(encoding="utf-8").splitlines():
            if "\t" in line:
                t, p = line.split("\t", 1)
                prev[t] = p
    for title, rel in written:
        prev[title] = rel
    return list(prev.items())


if __name__ == "__main__":
    sys.exit(main())
