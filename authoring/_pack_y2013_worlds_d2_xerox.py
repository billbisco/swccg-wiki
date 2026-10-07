#!/usr/bin/env python3
"""Leftover pack: 2013 Worlds Day 2 Justin Desai Light p31."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-worlds-d2-xerox-titles.tsv"
OUT = ROOT / "y2013-worlds-d2-xerox.tgz"
ROWS = [
    (
        "2013 Worlds Day 2 Justin Desai LS Mind What You Have Learned (V)",
        "pages/2013_Worlds_Day_2_Justin_Desai_LS_Mind_What_You_Have_Learned_(V).wiki",
    ),
    ("2013 World Championship", "pages/2013_World_Championship.wiki"),
    ("Justin Desai", "pages/player-stubs/Justin_Desai.wiki"),
]
MEDIA = [
    "y2013-worlds-media/2013 Worlds Day 2 p31 Justin Desai LS.png",
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
        tar.add(TSV, arcname="y2013-worlds-d2-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-worlds-d2-xerox.sh",
            arcname="apply-2013-worlds-d2-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
