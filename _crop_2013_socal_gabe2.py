#!/usr/bin/env python3
"""Recrop Gabe p03 37-41 and p04 matching band; also full L/R."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal"


def main() -> None:
    for page in (3, 4):
        im = Image.open(EXTRACT / f"socal_d1_p{page:02d}.png")
        dest = OUT / f"socal_d1_p{page:02d}"
        dest.mkdir(parents=True, exist_ok=True)
        # 37-41 sit under CARD TITLE [continued], clipped by hdr/Rtop.
        im.crop((760, 330, 1490, 520)).save(dest / "R37_41.png")
        im.crop((40, 330, 780, 520)).save(dest / "L01_04.png")
        # extra 37-40 on left reprint band if present
        im.crop((40, 1640, 780, 1780)).save(dest / "L37_40.png")
        print("recrop", page, im.size)


if __name__ == "__main__":
    main()
