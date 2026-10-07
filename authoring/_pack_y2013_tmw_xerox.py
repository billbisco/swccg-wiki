#!/usr/bin/env python3
"""Leftover pack: 2013 TMW Day 1 Matt Wehner p40 Light / p41 Dark."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-tmw-xerox-titles.tsv"
OUT = ROOT / "y2013-tmw-xerox.tgz"
ROWS = [
    (
        "2013 Texas Mini Worlds Day 1 Matt Wehner LS Mind What You Have Learned",
        "pages/2013_Texas_Mini_Worlds_Day_1_Matt_Wehner_LS_Mind_What_You_Have_Learned.wiki",
    ),
    (
        "2013 Texas Mini Worlds Day 1 Matt Wehner DS Set Your Course For Alderaan",
        "pages/2013_Texas_Mini_Worlds_Day_1_Matt_Wehner_DS_Set_Your_Course_For_Alderaan.wiki",
    ),
    ("2013 Texas Mini Worlds", "pages/2013_Texas_Mini_Worlds.wiki"),
    ("Matt Wehner", "pages/player-stubs/Matt_Wehner.wiki"),
]
MEDIA = [
    "y2013-tmw-media/2013 Texas Mini Worlds Day 1 p40 Matt Wehner LS.png",
    "y2013-tmw-media/2013 Texas Mini Worlds Day 1 p41 Matt Wehner DS.png",
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
        tar.add(TSV, arcname="y2013-tmw-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-tmw-xerox.sh",
            arcname="apply-2013-tmw-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
