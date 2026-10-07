#!/usr/bin/env python3
"""Crop 2010 Xerox strips for 2013 Worlds Day 3 leftover sheets."""
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

# 2010 Xerox leftover pages (skip p03 empty Bali DS, p04 Bali LS live,
# p09-p10 HT Day 2 leftover, p13-p14 typed Print Form, p15-p16 Same as Yesterday).
PAGES = (1, 2, 5, 6, 7, 8, 11, 12)


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
    for n in lines:
        i = n - 30
        y0 = int(h * i / 12) - 4
        y1 = int(h * (i + 1) / 12) + 10
        B.crop((0, max(0, y0), w, min(h, y1))).save(OUT / f"{tag}_L{n:02d}b.png")


def recrop_from_sh(tag: str, lines: tuple[int, ...]) -> None:
    S = Image.open(OUT / f"{tag}_SH.png")
    w, h = S.size
    for n in lines:
        i = n - 1
        y0 = int(h * i / 12) - 4
        y1 = int(h * (i + 1) / 12) + 10
        S.crop((0, max(0, y0), w, min(h, y1))).save(OUT / f"{tag}_SH{n:02d}b.png")


def main() -> None:
    for page in PAGES:
        im = Image.open(SRC / f"worlds_d3_p{page:02d}.png")
        tag = f"worlds_d3_p{page:02d}"
        save(im, HEADER, f"{tag}_hdr.png")
        save(im, LEFT, f"{tag}_L.png")
        save(im, RIGHT, f"{tag}_R.png")
        save(im, SHIELDS, f"{tag}_SH.png")
        save(im, ADD, f"{tag}_ADD.png")
        save(im, LEFT_BOT, f"{tag}_Lbot.png")
        print("cropped", tag, im.size)
        recrop_from_l(tag, tuple(range(1, 30)))
        recrop_from_lbot(tag, tuple(range(30, 41)))
        recrop_from_r(tag, tuple(range(41, 61)))
        recrop_from_sh(tag, tuple(range(1, 13)))


if __name__ == "__main__":
    main()
