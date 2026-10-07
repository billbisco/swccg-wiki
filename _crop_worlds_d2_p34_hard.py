#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(exist_ok=True)

jobs = [
    ("worlds_d2_p34.png", "p34_l09_33.png", (0, 280, 780, 1500)),
    ("worlds_d2_p34.png", "p34_l33.png", (0, 1180, 780, 1380)),
    ("worlds_d2_p34.png", "p34_sh10.png", (720, 1550, 1488, 2105)),
    ("worlds_d2_p34.png", "p34_add.png", (720, 1750, 1488, 2105)),
    ("worlds_d2_p34.png", "p34_r46.png", (720, 280, 1488, 900)),
    ("worlds_d2_p36.png", "p36_l01_16.png", (0, 250, 780, 1100)),
    ("worlds_d2_p36.png", "p36_l20.png", (0, 900, 780, 1400)),
    ("worlds_d2_p36.png", "p36_r46_60.png", (720, 250, 1488, 1600)),
    ("worlds_d2_p36.png", "p36_sh.png", (720, 1500, 1488, 2105)),
    ("worlds_d2_p37.png", "p37_l01_16.png", (0, 250, 780, 1100)),
    ("worlds_d2_p37.png", "p37_l09.png", (0, 400, 780, 700)),
    ("worlds_d2_p37.png", "p37_r45_55.png", (720, 250, 1488, 1100)),
    ("worlds_d2_p37.png", "p37_add.png", (720, 1700, 1488, 2105)),
]

for src_name, dest_name, box in jobs:
    im = Image.open(SRC / src_name)
    im.crop(box).save(OUT / dest_name)
    print(dest_name, im.size)
print("DONE")
