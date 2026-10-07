#!/usr/bin/env python3
"""Hard crops for 2013 Worlds Day 2 p62-p67 slang lines."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = [
    ("worlds_d2_p62.png", "p62_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p62.png", "p62_r51.png", (760, 760, 1530, 980)),
    ("worlds_d2_p62.png", "p62_sh8.png", (760, 1480, 1530, 1780)),
    ("worlds_d2_p63.png", "p63_l04.png", (20, 300, 800, 520)),
    ("worlds_d2_p63.png", "p63_l21.png", (20, 880, 800, 1080)),
    ("worlds_d2_p63.png", "p63_r49.png", (760, 700, 1530, 980)),
    ("worlds_d2_p64.png", "p64_hdr.png", (0, 0, 1530, 280)),
    ("worlds_d2_p64.png", "p64_chars.png", (0, 280, 900, 720)),
    ("worlds_d2_p64.png", "p64_bot.png", (0, 1680, 1530, 1980)),
    ("worlds_d2_p64.png", "p64_sh.png", (800, 80, 1530, 720)),
    ("worlds_d2_p65.png", "p65_hdr.png", (0, 0, 1530, 280)),
    ("worlds_d2_p65.png", "p65_sen.png", (0, 240, 900, 720)),
    ("worlds_d2_p65.png", "p65_strike.png", (0, 700, 900, 1100)),
    ("worlds_d2_p65.png", "p65_bot.png", (0, 1680, 1530, 1980)),
    ("worlds_d2_p65.png", "p65_sh.png", (800, 80, 1530, 900)),
    ("worlds_d2_p66.png", "p66_l05.png", (20, 300, 800, 520)),
    ("worlds_d2_p66.png", "p66_l27.png", (20, 1000, 800, 1220)),
    ("worlds_d2_p66.png", "p66_l30.png", (20, 1120, 800, 1320)),
    ("worlds_d2_p66.png", "p66_r42.png", (760, 380, 1530, 620)),
    ("worlds_d2_p66.png", "p66_bot.png", (0, 1700, 1530, 1980)),
    ("worlds_d2_p67.png", "p67_l18.png", (20, 720, 800, 920)),
    ("worlds_d2_p67.png", "p67_l30.png", (20, 1120, 800, 1320)),
    ("worlds_d2_p67.png", "p67_l36.png", (20, 1280, 800, 1500)),
    ("worlds_d2_p67.png", "p67_r43.png", (760, 300, 1530, 520)),
]


def main() -> None:
    for src_name, dest_name, box in JOBS:
        im = Image.open(SRC / src_name)
        im.crop(box).save(OUT / dest_name)
        print("crop", dest_name, im.size, box)
    print("DONE", OUT)


if __name__ == "__main__":
    main()
