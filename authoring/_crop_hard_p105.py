#!/usr/bin/env python3
"""Recrop specific hard lines on Stu Wall p105/p106."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"

# L.png is y=350..1470 showing lines 1-31 => ~36.13 px/line
Y0 = 350
LH = 36.13
X0, X1 = 40, 800


def line_box(n: int):
    top = int(Y0 + (n - 1) * LH) - 2
    bot = int(Y0 + n * LH) + 6
    return (X0, top, X1, bot)


def main() -> None:
    im = Image.open(SRC / "worlds_d2_p105.png")
    for n in (1, 4, 6, 11, 12, 13, 16, 17, 20, 27, 32, 33, 35, 36, 37, 38, 39, 40):
        im.crop(line_box(n)).save(OUT / f"p105_hard_L{n:02d}.png")
        print("L", n, line_box(n))
    # right 41-60 at y=350..1105, 20 lines => 37.75
    ry0, rh = 350, 37.75
    for n in range(41, 61):
        i = n - 41
        top = int(ry0 + i * rh) - 2
        bot = int(ry0 + (i + 1) * rh) + 6
        im.crop((760, top, 1510, bot)).save(OUT / f"p105_hard_R{n:02d}.png")
    # shields y=1100..1685, 12 lines
    sy0, sh = 1128, 42.0
    for n in range(1, 13):
        top = int(sy0 + (n - 1) * sh) - 2
        bot = int(sy0 + n * sh) + 6
        im.crop((760, top, 1510, bot)).save(OUT / f"p105_hard_S{n:02d}.png")
    # additional in SH image: after shields heading. From SH crop, add starts ~ y=1540
    ay0, ah = 1548, 38.0
    for n in range(1, 7):
        top = int(ay0 + (n - 1) * ah) - 2
        bot = int(ay0 + n * ah) + 6
        im.crop((760, top, 1510, bot)).save(OUT / f"p105_hard_A{n:02d}.png")
    print("p105 hard done")


if __name__ == "__main__":
    main()
