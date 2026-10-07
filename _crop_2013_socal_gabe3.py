#!/usr/bin/env python3
"""Deeper left-bottom recrop for Gabe extra 37-40 both sides."""
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
        im.crop((40, 1600, 780, 1900)).save(dest / "Lbot.png")
        im.crop((760, 300, 1490, 480)).save(dest / "R37_40.png")
        print("recrop3", page)


if __name__ == "__main__":
    main()
