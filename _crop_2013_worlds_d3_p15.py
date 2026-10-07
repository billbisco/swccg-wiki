#!/usr/bin/env python3
"""Crop 2010 Xerox strips for 2013 Worlds Day 3 Emil Wallin p15-p16."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)

HEADER = (0, 0, 1530, 360)
LEFT = (0, 350, 800, 1470)
RIGHT = (730, 350, 1530, 1105)
SHIELDS = (730, 1100, 1530, 1685)
ADD = (730, 1675, 1530, 1900)
LEFT_BOT = (0, 1460, 800, 1900)


def save(im: Image.Image, box, name: str) -> None:
    im.crop(box).save(OUT / name)


def main() -> None:
    for page in (15, 16):
        im = Image.open(SRC / f"worlds_d3_p{page:02d}.png")
        tag = f"worlds_d3_p{page:02d}"
        save(im, HEADER, f"{tag}_hdr.png")
        save(im, LEFT, f"{tag}_L.png")
        save(im, RIGHT, f"{tag}_R.png")
        save(im, SHIELDS, f"{tag}_SH.png")
        save(im, ADD, f"{tag}_ADD.png")
        save(im, LEFT_BOT, f"{tag}_Lbot.png")
        print("cropped", tag, im.size)


if __name__ == "__main__":
    main()
