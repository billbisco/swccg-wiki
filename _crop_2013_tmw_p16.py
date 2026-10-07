#!/usr/bin/env python3
"""Zoom hard lines on 2013 TMW Day 1 p16-p17 Hilbun Xerox."""
from __future__ import annotations
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "tmw"
OUT.mkdir(parents=True, exist_ok=True)

# Full-page line boxes (page coords). 2010 form: left 1-40, right 41-60.
# Empirically: header ~360, left lines ~37.3px, right starts ~y=390.
JOBS = [
    ("tmw_d1_p16.png", (40, 360, 800, 430), "p16_l01.png"),
    ("tmw_d1_p16.png", (40, 395, 800, 465), "p16_l02.png"),
    ("tmw_d1_p16.png", (40, 1285, 800, 1355), "p16_l26.png"),
    ("tmw_d1_p16.png", (40, 1545, 800, 1615), "p16_l33.png"),
    ("tmw_d1_p16.png", (40, 1770, 800, 1840), "p16_l39.png"),
    ("tmw_d1_p16.png", (760, 390, 1500, 460), "p16_l41.png"),
    ("tmw_d1_p16.png", (760, 425, 1500, 495), "p16_l42.png"),
    ("tmw_d1_p16.png", (760, 950, 1500, 1020), "p16_l56.png"),
    ("tmw_d1_p16.png", (760, 1025, 1500, 1095), "p16_l58.png"),
    ("tmw_d1_p16.png", (760, 1060, 1500, 1130), "p16_l59.png"),
    ("tmw_d1_p16.png", (760, 1100, 1500, 1165), "p16_sh1.png"),
    ("tmw_d1_p16.png", (760, 1680, 1500, 1750), "p16_add1.png"),
    ("tmw_d1_p16.png", (760, 1715, 1500, 1785), "p16_add2.png"),
    ("tmw_d1_p17.png", (40, 360, 800, 430), "p17_l01.png"),
    ("tmw_d1_p17.png", (40, 470, 800, 580), "p17_l04_06.png"),
    ("tmw_d1_p17.png", (40, 1060, 800, 1170), "p17_l20_22.png"),
    ("tmw_d1_p17.png", (40, 1430, 800, 1500), "p17_l30.png"),
    ("tmw_d1_p17.png", (40, 1545, 800, 1615), "p17_l33.png"),
    ("tmw_d1_p17.png", (40, 1580, 800, 1650), "p17_l34.png"),
    ("tmw_d1_p17.png", (760, 390, 1500, 500), "p17_l41_42.png"),
    ("tmw_d1_p17.png", (760, 650, 1500, 760), "p17_l48_49.png"),
    ("tmw_d1_p17.png", (760, 830, 1500, 970), "p17_l53_56.png"),
    ("tmw_d1_p17.png", (760, 1045, 1500, 1115), "p17_l60.png"),
    ("tmw_d1_p17.png", (760, 1470, 1500, 1540), "p17_sh11.png"),
    ("tmw_d1_p17.png", (760, 1680, 1500, 1785), "p17_add12.png"),
]


def main() -> None:
    for src_name, box, out_name in JOBS:
        im = Image.open(SRC / src_name)
        im.crop(box).save(OUT / out_name)
        print("cropped", out_name, im.size)


if __name__ == "__main__":
    main()
