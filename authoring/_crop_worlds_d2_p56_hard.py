#!/usr/bin/env python3
"""Hard crops for 2013 Worlds Day 2 p56-p61 slang lines."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(parents=True, exist_ok=True)

# (src, dest, box)
JOBS = [
    ("worlds_d2_p56.png", "p56_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p56.png", "p56_l39.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p56.png", "p56_r50.png", (760, 700, 1530, 920)),
    ("worlds_d2_p56.png", "p56_r51_59.png", (760, 760, 1530, 1400)),
    ("worlds_d2_p56.png", "p56_sh.png", (760, 1480, 1530, 1980)),
    ("worlds_d2_p57.png", "p57_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p57.png", "p57_l06.png", (20, 420, 800, 620)),
    ("worlds_d2_p57.png", "p57_l08_17.png", (20, 500, 800, 920)),
    ("worlds_d2_p57.png", "p57_l25.png", (20, 1000, 800, 1200)),
    ("worlds_d2_p57.png", "p57_r43_51.png", (760, 300, 1530, 900)),
    ("worlds_d2_p57.png", "p57_r57_60.png", (760, 1260, 1530, 1580)),
    ("worlds_d2_p57.png", "p57_sh.png", (760, 1480, 1530, 1980)),
    ("worlds_d2_p58.png", "p58_l15.png", (20, 720, 800, 860)),
    ("worlds_d2_p58.png", "p58_l38.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p58.png", "p58_r54.png", (760, 1260, 1530, 1580)),
    ("worlds_d2_p59.png", "p59_l03.png", (20, 300, 800, 480)),
    ("worlds_d2_p59.png", "p59_l11_16.png", (20, 560, 800, 860)),
    ("worlds_d2_p59.png", "p59_l31.png", (20, 1180, 800, 1400)),
    ("worlds_d2_p59.png", "p59_r42_48.png", (760, 300, 1530, 800)),
    ("worlds_d2_p59.png", "p59_r57.png", (760, 1320, 1530, 1580)),
    ("worlds_d2_p59.png", "p59_sh.png", (760, 1480, 1530, 1980)),
    ("worlds_d2_p60.png", "p60_l.png", (0, 280, 800, 1580)),
    ("worlds_d2_p61.png", "p61_l15.png", (20, 720, 800, 860)),
    ("worlds_d2_p61.png", "p61_r44_47.png", (760, 380, 1530, 720)),
    ("worlds_d2_p61.png", "p61_sh.png", (760, 1480, 1530, 1980)),
]


def main() -> None:
    for src_name, dest_name, box in JOBS:
        im = Image.open(SRC / src_name)
        im.crop(box).save(OUT / dest_name)
        print("crop", dest_name, im.size, box)
    print("DONE", OUT)


if __name__ == "__main__":
    main()
