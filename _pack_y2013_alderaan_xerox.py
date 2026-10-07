#!/usr/bin/env python3
"""Leftover pack: 2013 Alderaan Xerox Tom / Shannon / Schoenthal / Nathan."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-alderaan-xerox-titles.tsv"
OUT = ROOT / "y2013-alderaan-xerox.tgz"
ROWS = [
    (
        "2013 Alderaan Regionals Tom LS Watch Your Step (V)",
        "pages/2013_Alderaan_Regionals_Tom_LS_Watch_Your_Step_(V).wiki",
    ),
    (
        "2013 Alderaan Regionals Tom DS Agents Of Black Sun",
        "pages/2013_Alderaan_Regionals_Tom_DS_Agents_Of_Black_Sun.wiki",
    ),
    (
        "2013 Alderaan Regionals Kevin Shannon LS Quiet Mining Colony",
        "pages/2013_Alderaan_Regionals_Kevin_Shannon_LS_Quiet_Mining_Colony.wiki",
    ),
    (
        "2013 Alderaan Regionals Kevin Shannon DS Carbon Chamber Testing",
        "pages/2013_Alderaan_Regionals_Kevin_Shannon_DS_Carbon_Chamber_Testing.wiki",
    ),
    (
        "2013 Alderaan Regionals Chris Schoenthal LS Watch Your Step",
        "pages/2013_Alderaan_Regionals_Chris_Schoenthal_LS_Watch_Your_Step.wiki",
    ),
    (
        "2013 Alderaan Regionals Chris Schoenthal DS Ralltiir Operations",
        "pages/2013_Alderaan_Regionals_Chris_Schoenthal_DS_Ralltiir_Operations.wiki",
    ),
    (
        "2013 Alderaan Regionals Nathan LS Yavin 4: Throne Room",
        "pages/2013_Alderaan_Regionals_Nathan_LS_Yavin_4__Throne_Room.wiki",
    ),
    (
        "2013 Alderaan Regionals Nathan DS Ralltiir Operations",
        "pages/2013_Alderaan_Regionals_Nathan_DS_Ralltiir_Operations.wiki",
    ),
    ("2013 Alderaan Regionals", "pages/2013_Alderaan_Regionals.wiki"),
    ("Tom", "pages/player-stubs/Tom.wiki"),
    ("Kevin Shannon", "pages/Kevin_Shannon.wiki"),
    ("Chris Schoenthal", "pages/Chris_Schoenthal.wiki"),
    ("Nathan", "pages/player-stubs/Nathan.wiki"),
]
MEDIA = [
    "y2013-alderaan-media/2013 Alderaan Regionals p03 Tom LS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p04 Tom DS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p07 Kevin Shannon DS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p08 Kevin Shannon LS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p21 Chris Schoenthal LS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p22 Chris Schoenthal DS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p25 Nathan DS.png",
    "y2013-alderaan-media/2013 Alderaan Regionals p26 Nathan LS.png",
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
        tar.add(TSV, arcname="y2013-alderaan-xerox-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-alderaan-xerox.sh",
            arcname="apply-2013-alderaan-xerox.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS), "media", len(MEDIA))


if __name__ == "__main__":
    main()
