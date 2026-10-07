#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(exist_ok=True)
jobs = [
    ("worlds_d2_p52.png", "p52_l17.png", (20, 790, 800, 860)),
    ("worlds_d2_p52.png", "p52_l34.png", (20, 1320, 800, 1580)),
    ("worlds_d2_p52.png", "p52_r60.png", (760, 1450, 1530, 1560)),
    ("worlds_d2_p53.png", "p53_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p53.png", "p53_l08.png", (20, 500, 800, 680)),
    ("worlds_d2_p53.png", "p53_r55.png", (760, 1400, 1530, 1560)),
    ("worlds_d2_p54.png", "p54_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p54.png", "p54_l15.png", (20, 720, 800, 840)),
    ("worlds_d2_p54.png", "p54_sh1112.png", (760, 1760, 1530, 1920)),
    ("worlds_d2_p55.png", "p55_hdr.png", (0, 0, 1530, 320)),
    ("worlds_d2_p55.png", "p55_l16.png", (20, 760, 800, 860)),
]
for src_name, dest_name, box in jobs:
    Image.open(SRC / src_name).crop(box).save(OUT / dest_name)
    print(dest_name)
print("DONE")
