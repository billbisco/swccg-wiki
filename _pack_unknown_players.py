#!/usr/bin/env python3
"""Leftover pack: Unknown Player dest + Unknown players index."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "unknown-players-titles.tsv"
OUT = ROOT / "unknown-players.tgz"
ROWS = [
    ("Unknown players", "pages/Unknown_players.wiki"),
    ("Unknown Player", "pages/player-stubs/Unknown_Player.wiki"),
    ("Blank Player", "pages/Blank_Player.wiki"),
    ("unnamed", "pages/unnamed.wiki"),
    (
        "2014 Worlds Day 2 unnamed LS It Is The Future You See",
        "pages/2014_Worlds_Day_2_unnamed_LS_It_Is_The_Future_You_See.wiki",
    ),
    (
        "2014 Worlds Day 2 unnamed DS Separatist Uprising",
        "pages/2014_Worlds_Day_2_unnamed_DS_Separatist_Uprising.wiki",
    ),
    (
        "2014 Worlds Day 2 unnamed LS Hoth",
        "pages/2014_Worlds_Day_2_unnamed_LS_Hoth.wiki",
    ),
    (
        "2014 Worlds Day 2 unnamed LS Yavin 4",
        "pages/2014_Worlds_Day_2_unnamed_LS_Yavin_4.wiki",
    ),
    ("2014 World Championship", "pages/2014_World_Championship.wiki"),
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("Tournaments", "pages/Tournaments.wiki"),
    ("Championships", "pages/Championships.wiki"),
]


def main() -> None:
    missing = [p for _t, p in ROWS if not (ROOT / p).exists()]
    if missing:
        raise SystemExit("missing " + "; ".join(missing))
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ROWS), encoding="utf-8", newline="\n"
    )
    with tarfile.open(OUT, "w:gz") as tar:
        for _t, rel in ROWS:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname="unknown-players-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-unknown-players.sh",
            arcname="apply-unknown-players.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS))


if __name__ == "__main__":
    main()
