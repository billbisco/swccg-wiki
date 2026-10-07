#!/usr/bin/env python3
"""Leftover pack: 2013 SoCal Day 1 Jan Westergard p43 Light / p44 Dark."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-socal-xerox-titles.tsv"
OUT = ROOT / "y2013-socal-xerox.tgz"
ROWS = [
    (
        "2013 SoCal Grand Prix Day 1 Jan Westergard LS Watch Your Step",
        "pages/2013_SoCal_Grand_Prix_Day_1_Jan_Westergard_LS_Watch_Your_Step.wiki",
    ),
    (
        "2013 SoCal Grand Prix Day 1 Jan Westergard DS Invasion",
        "pages/2013_SoCal_Grand_Prix_Day_1_Jan_Westergard_DS_Invasion.wiki",
    ),
    ("2013 SoCal Grand Prix", "pages/2013_SoCal_Grand_Prix.wiki"),
    ("Jan Westergard", "pages/player-stubs/Jan_Westergard.wiki"),
]
MEDIA = [
    "y2013-socal-media/2013 SoCal Grand Prix Day 1 p43 Jan Westergard LS.png",
    "y2013-socal-media/2013 SoCal Grand Prix Day 1 p44 Jan Westergard DS.png",
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
        tar.add(TSV, arcname="y2013-socal-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-socal-xerox.sh",
            arcname="apply-2013-socal-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
