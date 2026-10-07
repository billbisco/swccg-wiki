#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(exist_ok=True)

# Full pages 1530x1980. Line 1 ~y=310, ~31px/line.
jobs = [
    ("worlds_d2_p52.png", "p52_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p52.png", "p52_l16.png", (20, 760, 800, 920)),
    ("worlds_d2_p52.png", "p52_l35.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p52.png", "p52_r43.png", (760, 300, 1530, 520)),
    ("worlds_d2_p52.png", "p52_r59.png", (760, 1320, 1530, 1580)),
    ("worlds_d2_p52.png", "p52_add.png", (760, 1680, 1530, 1900)),
    ("worlds_d2_p53.png", "p53_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p53.png", "p53_l07.png", (20, 480, 800, 680)),
    ("worlds_d2_p53.png", "p53_l26.png", (20, 1040, 800, 1240)),
    ("worlds_d2_p53.png", "p53_l37.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p53.png", "p53_r55.png", (760, 1260, 1530, 1580)),
    ("worlds_d2_p54.png", "p54_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p54.png", "p54_l13.png", (20, 680, 800, 900)),
    ("worlds_d2_p54.png", "p54_l30.png", (20, 1180, 800, 1400)),
    ("worlds_d2_p54.png", "p54_l37.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p54.png", "p54_sh11.png", (760, 1680, 1530, 1900)),
    ("worlds_d2_p55.png", "p55_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p55.png", "p55_l15.png", (20, 720, 800, 920)),
    ("worlds_d2_p55.png", "p55_l38.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p55.png", "p55_r45.png", (760, 380, 1530, 620)),
    ("worlds_d2_p55.png", "p55_r56.png", (760, 1260, 1530, 1580)),
]

for src_name, dest_name, box in jobs:
    im = Image.open(SRC / src_name)
    im.crop(box).save(OUT / dest_name)
    print(dest_name, im.size)
print("DONE")
