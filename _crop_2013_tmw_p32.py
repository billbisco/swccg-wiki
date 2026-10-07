#!/usr/bin/env python3
"""Crop 2010 Xerox strips for 2013 TMW Day 1 p32 Barry Alperstein Dark / p33 Light."""
from __future__ import annotations
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "tmw"
OUT.mkdir(parents=True, exist_ok=True)

HEADER = (0, 0, 1530, 360)
LEFT = (0, 350, 800, 1470)
RIGHT = (730, 350, 1530, 1105)
SHIELDS = (730, 1100, 1530, 1685)
ADD = (730, 1675, 1530, 1900)
LEFT_BOT = (0, 1460, 800, 1980)


def save(im: Image.Image, box, name: str) -> None:
    im.crop(box).save(OUT / name)


def crop_page(page: int) -> None:
    im = Image.open(SRC / f"tmw_d1_p{page:02d}.png")
    tag = f"tmw_d1_p{page:02d}"
    save(im, HEADER, f"{tag}_hdr.png")
    save(im, LEFT, f"{tag}_L.png")
    save(im, RIGHT, f"{tag}_R.png")
    save(im, SHIELDS, f"{tag}_SH.png")
    save(im, ADD, f"{tag}_ADD.png")
    save(im, LEFT_BOT, f"{tag}_Lbot.png")
    print("cropped", tag, im.size)


def main() -> None:
    crop_page(32)
    crop_page(33)


if __name__ == "__main__":
    main()
