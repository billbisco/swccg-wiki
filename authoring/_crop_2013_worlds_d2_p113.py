#!/usr/bin/env python3
"""Crop 2010 Xerox strips for 2013 Worlds Day 2 p113-p114 (Chris Westergard)."""
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
    for page in (113, 114):
        im = Image.open(SRC / f"worlds_d2_p{page}.png")
        w, h = im.size
        tag = f"worlds_d2_p{page}"
        save(im, HEADER, f"{tag}_hdr.png")
        save(im, LEFT, f"{tag}_L.png")
        save(im, RIGHT, f"{tag}_R.png")
        save(im, SHIELDS, f"{tag}_SH.png")
        save(im, ADD, f"{tag}_ADD.png")
        save(im, LEFT_BOT, f"{tag}_Lbot.png")
        print("cropped", tag, im.size)
        # Hard rows for ambiguous lines.
        if page == 113:
            # line 58 area in right column ~ lines 41-60 mapped onto RIGHT box
            x0, y0, x1, y1 = RIGHT
            rh = (y1 - y0) / 20
            i = 58 - 41
            im.crop((x0, int(y0 + i * rh) - 6, x1, int(y0 + (i + 1) * rh) + 8)).save(
                OUT / f"{tag}_R58.png"
            )
            x0, y0, x1, y1 = LEFT
            lh = (y1 - y0) / 40
            for n in (6, 14, 19, 31, 37, 38, 39, 40):
                i = n - 1
                im.crop((x0, int(y0 + i * lh) - 4, x1, int(y0 + (i + 1) * lh) + 6)).save(
                    OUT / f"{tag}_L{n:02d}.png"
                )
        else:
            x0, y0, x1, y1 = LEFT
            lh = (y1 - y0) / 40
            for n in (22, 23, 29, 34, 35, 36, 37, 38, 39, 40):
                i = n - 1
                im.crop((x0, int(y0 + i * lh) - 4, x1, int(y0 + (i + 1) * lh) + 6)).save(
                    OUT / f"{tag}_L{n:02d}.png"
                )


if __name__ == "__main__":
    main()
