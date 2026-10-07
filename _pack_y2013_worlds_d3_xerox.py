#!/usr/bin/env python3
"""Leftover pack: 2013 Worlds Day 3 Emil Wallin Xerox."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-worlds-d3-xerox-titles.tsv"
OUT = ROOT / "y2013-worlds-d3-xerox.tgz"
ROWS = [
    (
        "2013 Worlds Day 3 Emil Wallin LS There Is Good In Him",
        "pages/2013_Worlds_Day_3_Emil_Wallin_LS_There_Is_Good_In_Him.wiki",
    ),
    (
        "2013 Worlds Day 3 Emil Wallin DS Imperial Entanglements",
        "pages/2013_Worlds_Day_3_Emil_Wallin_DS_Imperial_Entanglements.wiki",
    ),
    ("2013 World Championship", "pages/2013_World_Championship.wiki"),
    ("Emil Wallin", "pages/player-stubs/Emil_Wallin.wiki"),
]
MEDIA = [
    "y2013-worlds-media/2013 Worlds Day 3 p15 Emil Wallin LS.png",
    "y2013-worlds-media/2013 Worlds Day 3 p16 Emil Wallin DS.png",
]


def main() -> None:
    missing = [p for p in [r for _t, r in ROWS] + MEDIA if not (ROOT / p).exists()]
    if missing:
        raise SystemExit("missing " + "; ".join(missing))
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ROWS), encoding="utf-8", newline="\n"
    )
    with tarfile.open(OUT, "w:gz") as tar:
        for _t, rel in ROWS:
            tar.add(ROOT / rel, arcname=rel)
        for rel in MEDIA:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname="y2013-worlds-d3-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-worlds-d3-xerox.sh",
            arcname="apply-2013-worlds-d3-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
