#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_crops"
OUT.mkdir(exist_ok=True)

# p40-p45 are 1530x1980
jobs = [
    ("worlds_d2_p40.png", "p40_l04.png", (40, 300, 800, 430)),
    ("worlds_d2_p40.png", "p40_l13.png", (40, 520, 800, 720)),
    ("worlds_d2_p40.png", "p40_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p41.png", "p41_l34.png", (40, 1180, 800, 1380)),
    ("worlds_d2_p41.png", "p41_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p42.png", "p42_l02.png", (40, 280, 800, 430)),
    ("worlds_d2_p42.png", "p42_l08.png", (40, 420, 800, 560)),
    ("worlds_d2_p42.png", "p42_l25.png", (40, 900, 800, 1100)),
    ("worlds_d2_p42.png", "p42_l39.png", (40, 1280, 800, 1480)),
    ("worlds_d2_p42.png", "p42_r58.png", (760, 1280, 1530, 1500)),
    ("worlds_d2_p42.png", "p42_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p43.png", "p43_l14.png", (40, 540, 800, 720)),
    ("worlds_d2_p43.png", "p43_l16.png", (40, 620, 800, 780)),
    ("worlds_d2_p43.png", "p43_l52.png", (760, 1050, 1530, 1250)),
    ("worlds_d2_p43.png", "p43_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p44.png", "p44_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p45.png", "p45_hdr.png", (700, 20, 1530, 280)),
    ("worlds_d2_p45.png", "p45_l16.png", (40, 620, 800, 780)),
    ("worlds_d2_p45.png", "p45_r42.png", (760, 320, 1530, 500)),
    ("worlds_d2_p45.png", "p45_r56.png", (760, 1180, 1530, 1400)),
]

for src_name, dest_name, box in jobs:
    im = Image.open(SRC / src_name)
    im.crop(box).save(OUT / dest_name)
    print(dest_name, im.size)
print("DONE")
