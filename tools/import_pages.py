#!/usr/bin/env python3
"""Print how to import pages/INDEX.tsv into a MediaWiki.

Does not talk to the live VPS. For wiki.swccg.com, use authoring/apply-tsv.sh
on the box that already has docker swccg_wiki.

    python tools/import_pages.py
    python tools/import_pages.py --format edit-commands
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pages" / "INDEX.tsv"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", type=Path, default=INDEX)
    ap.add_argument("--pages", type=Path, default=ROOT / "pages", help="unused; INDEX paths are repo-relative")
    ap.add_argument(
        "--format",
        choices=("summary", "edit-commands"),
        default="summary",
    )
    args = ap.parse_args()
    if not args.index.exists():
        print(f"missing {args.index} — run python tools/dump_live.py first")
        return 1
    rows = []
    missing = 0
    for line in args.index.read_text(encoding="utf-8").splitlines():
        if "\t" not in line:
            continue
        title, rel = line.split("\t", 1)
        rows.append((title, rel))
        if not (ROOT / rel).is_file():
            missing += 1
    if args.format == "summary":
        print(f"{len(rows)} titles in {args.index}")
        if missing:
            print(f"{missing} INDEX paths have no file yet — run python tools/dump_live.py")
        print("On a MediaWiki box with maintenance scripts:")
        print("  while IFS=$'\\t' read -r title rel; do")
        print("    php maintenance/run.php edit --user=Admin --summary='import from git' \"$title\" < \"$rel\"")
        print("  done < pages/INDEX.tsv")
        print("Same TSV: authoring/apply-tsv.sh pages/INDEX.tsv 'import from git'")
        return 0 if missing == 0 else 2
    for title, rel in rows:
        print(f"php maintenance/run.php edit --user=Admin --summary='import from git' {title!s} < {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
