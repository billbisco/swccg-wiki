#!/usr/bin/env python3
"""Crop 2009 Xerox strips for 2013 Worlds Day 2 p115-p116 (Thomas Whaley)."""
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


def recrop_from_l(tag: str, lines: tuple[int, ...], nvis: int = 29) -> None:
    L = Image.open(OUT / f"{tag}_L.png")
    w, h = L.size
    for n in lines:
        i = n - 1
        y0 = int(h * i / nvis) - 4
        y1 = int(h * (i + 1) / nvis) + 8
        L.crop((0, max(0, y0), w, min(h, y1))).save(OUT / f"{tag}_L{n:02d}b.png")


def recrop_from_r(tag: str, lines: tuple[int, ...]) -> None:
    R = Image.open(OUT / f"{tag}_R.png")
    w, h = R.size
    for n in lines:
        i = n - 41
        y0 = int(h * i / 20) - 6
        y1 = int(h * (i + 1) / 20) + 10
        R.crop((0, max(0, y0), w, min(h, y1))).save(OUT / f"{tag}_R{n:02d}b.png")


def recrop_from_lbot(tag: str, lines: tuple[int, ...]) -> None:
    B = Image.open(OUT / f"{tag}_Lbot.png")
    w, h = B.size
    # Lbot shows ~ lines 30-40 (11 lines) plus footer
    for n in lines:
        i = n - 30
        y0 = int(h * i / 12) - 4
        y1 = int(h * (i + 1) / 12) + 10
        B.crop((0, max(0, y0), w, min(h, y1))).save(OUT / f"{tag}_L{n:02d}b.png")


def main() -> None:
    for page in (115, 116):
        im = Image.open(SRC / f"worlds_d2_p{page}.png")
        tag = f"worlds_d2_p{page}"
        save(im, HEADER, f"{tag}_hdr.png")
        save(im, LEFT, f"{tag}_L.png")
        save(im, RIGHT, f"{tag}_R.png")
        save(im, SHIELDS, f"{tag}_SH.png")
        save(im, ADD, f"{tag}_ADD.png")
        save(im, LEFT_BOT, f"{tag}_Lbot.png")
        print("cropped", tag, im.size)
    recrop_from_l(
        "worlds_d2_p115",
        (9, 15, 16, 17, 18, 19, 24, 26, 27, 29),
    )
    recrop_from_lbot("worlds_d2_p115", (34, 36, 37, 38, 39, 40))
    recrop_from_r("worlds_d2_p115", (43, 44, 45, 50, 53, 60))
    recrop_from_l(
        "worlds_d2_p116",
        (1, 8, 9, 11, 16, 18, 19, 24, 25, 26),
    )
    recrop_from_lbot("worlds_d2_p116", (33, 35, 37, 38, 39, 40))
    recrop_from_r("worlds_d2_p116", (44, 46, 49, 50, 54, 60))


if __name__ == "__main__":
    main()
