#!/usr/bin/env python3
"""Crop 2010 Xerox form strips for 2013 Worlds Day 2 p31 (Desai Light)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)

# Page is 1488x2105 (analog 1530x1980). Scale form boxes to this raster.
SX, SY = 1488 / 1530, 2105 / 1980


def box(x0, y0, x1, y1):
    return (int(x0 * SX), int(y0 * SY), int(x1 * SX), int(y1 * SY))


HEADER = box(0, 0, 1530, 360)
LEFT = box(0, 350, 800, 1470)
RIGHT = box(730, 350, 1530, 1105)
SHIELDS = box(730, 1100, 1530, 1685)
ADD = box(730, 1675, 1530, 1900)
LEFT_BOT = box(0, 1460, 800, 1980)


def save(im: Image.Image, box, name: str) -> None:
    im.crop(box).save(OUT / name)


def split_col(im: Image.Image, box, n: int, prefix: str, start: int) -> None:
    x0, y0, x1, y1 = box
    h = (y1 - y0) / n
    pad = 4
    for i in range(n):
        top = int(y0 + i * h) - pad
        bot = int(y0 + (i + 1) * h) + pad
        top = max(y0, top)
        bot = min(y1, bot)
        im.crop((x0, top, x1, bot)).save(OUT / f"{prefix}{start + i:02d}.png")


def main() -> None:
    im = Image.open(SRC / "worlds_d2_p31.png")
    tag = "worlds_d2_p31"
    save(im, HEADER, f"{tag}_hdr.png")
    save(im, LEFT, f"{tag}_L.png")
    save(im, RIGHT, f"{tag}_R.png")
    save(im, SHIELDS, f"{tag}_SH.png")
    save(im, ADD, f"{tag}_ADD.png")
    save(im, LEFT_BOT, f"{tag}_Lbot.png")
    split_col(im, LEFT, 40, f"{tag}_L", 1)
    split_col(im, RIGHT, 20, f"{tag}_R", 41)
    split_col(im, SHIELDS, 12, f"{tag}_S", 1)
    split_col(im, ADD, 6, f"{tag}_A", 1)
    print("cropped", tag, im.size)


if __name__ == "__main__":
    main()
