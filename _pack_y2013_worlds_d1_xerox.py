#!/usr/bin/env python3
"""Leftover pack: 2013 Worlds Day 1 Xerox Cellucci DS + Gardner + Littauer + Way."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-worlds-d1-xerox-titles.tsv"
OUT = ROOT / "y2013-worlds-d1-xerox.tgz"
ROWS = [
    (
        "2013 Worlds Day 1 Stephen Cellucci DS Endor Operations",
        "pages/2013_Worlds_Day_1_Stephen_Cellucci_DS_Endor_Operations.wiki",
    ),
    (
        "2013 Worlds Day 1 Jeremy Gardner LS Hidden Base (V)",
        "pages/2013_Worlds_Day_1_Jeremy_Gardner_LS_Hidden_Base_(V).wiki",
    ),
    (
        "2013 Worlds Day 1 Jeremy Gardner DS Imperial Entanglements",
        "pages/2013_Worlds_Day_1_Jeremy_Gardner_DS_Imperial_Entanglements.wiki",
    ),
    (
        "2013 Worlds Day 1 Ross Littauer LS Infiltration",
        "pages/2013_Worlds_Day_1_Ross_Littauer_LS_Infiltration.wiki",
    ),
    (
        "2013 Worlds Day 1 Ross Littauer DS Hunt Down And Destroy The Jedi (V)",
        "pages/2013_Worlds_Day_1_Ross_Littauer_DS_Hunt_Down_And_Destroy_The_Jedi_(V).wiki",
    ),
    (
        "2013 Worlds Day 1 Nathan Way LS Mind What You Have Learned (V)",
        "pages/2013_Worlds_Day_1_Nathan_Way_LS_Mind_What_You_Have_Learned_(V).wiki",
    ),
    (
        "2013 Worlds Day 1 Nathan Way DS Contract Killers",
        "pages/2013_Worlds_Day_1_Nathan_Way_DS_Contract_Killers.wiki",
    ),
    ("2013 World Championship", "pages/2013_World_Championship.wiki"),
    ("Stephen Cellucci", "pages/player-stubs/Stephen_Cellucci.wiki"),
    ("Jeremy Gardner", "pages/player-stubs/Jeremy_Gardner.wiki"),
    ("Ross Littauer", "pages/player-stubs/Ross_Littauer.wiki"),
    ("Nathan Way", "pages/player-stubs/Nathan_Way.wiki"),
]
MEDIA = [
    "y2013-worlds-media/2013 Worlds Day 1 p02 Stephen Cellucci DS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p03 Jeremy Gardner LS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p04 Jeremy Gardner DS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p05 Ross Littauer DS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p06 Ross Littauer LS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p11 Nathan Way LS.png",
    "y2013-worlds-media/2013 Worlds Day 1 p12 Nathan Way DS.png",
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
        tar.add(TSV, arcname="y2013-worlds-d1-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-worlds-d1-xerox.sh",
            arcname="apply-2013-worlds-d1-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
