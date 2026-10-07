#!/usr/bin/env python3
"""Leftover pack: Username on Xerox deck pages + Reid Smith retarget."""
from __future__ import annotations

import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
TSV = ROOT / "y-username-leftover-titles.tsv"
OUT = ROOT / "y-username-leftover.tgz"
SKIP_TITLES = {"List of SWCCG tournaments"}

EXTRA = [
    (
        "2013 Match Play Championship Day 1 Smith LS Communing",
        "pages/2013_Match_Play_Championship_Day_1_Smith_LS_Communing.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Smith DS Kessel",
        "pages/2013_Match_Play_Championship_Day_1_Smith_DS_Kessel.wiki",
    ),
    (
        "Smith (2013 Match Play Championship)",
        "pages/player-stubs/Smith_(2013_Match_Play_Championship).wiki",
    ),
    ("Reid Smith", "pages/player-stubs/Reid_Smith.wiki"),
    ("2013 Match Play Championship", "pages/2013_Match_Play_Championship.wiki"),
]


def wiki_title_from_path(rel: str) -> str | None:
    p = ROOT / rel
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8", errors="replace")
    if text.startswith("#REDIRECT"):
        return None
    m = __import__("re").search(r"^'''(.+?)'''", text)
    if m:
        return m.group(1)
    return Path(rel).stem.replace("_", " ")


def collect() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(title: str, rel: str) -> None:
        if title in SKIP_TITLES or title in seen:
            return
        if not (ROOT / rel).exists():
            print("MISSING", title, rel)
            return
        seen.add(title)
        rows.append((title, rel.replace("\\", "/")))

    for extra_title, rel in EXTRA:
        add(extra_title, rel)

    for p in list(PAGES.glob("2013_*.wiki")) + list(PAGES.glob("2014_*.wiki")):
        if p.name.startswith("File_") or p.name.startswith("Category_"):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if "'''Username:'''" not in text:
            continue
        m = __import__("re").search(r"^'''(.+?)'''", text)
        if not m:
            continue
        add(m.group(1), f"pages/{p.name}")
    return rows


def main() -> None:
    rows = collect()
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in rows), encoding="utf-8", newline="\n"
    )
    with tarfile.open(OUT, "w:gz") as tar:
        for _t, rel in rows:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname=TSV.name)
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        apply = ROOT / "apply-username-leftover.sh"
        if apply.exists():
            tar.add(apply, arcname=apply.name)
    print("packed", OUT, "n", len(rows), "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
