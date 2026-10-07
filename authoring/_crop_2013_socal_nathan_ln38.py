#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal" / "socal_d1_p42"
im = Image.open(EXTRACT / "socal_d1_p42.png")
print("size", im.size)
# Lbot was (40, 1600, 780, 1900) covering 35-40
# tighter slices
for name, box in {
    "ln37": (40, 1680, 780, 1750),
    "ln38": (40, 1735, 780, 1810),
    "ln38w": (40, 1720, 900, 1830),
    "ln39": (40, 1790, 780, 1860),
    "ln40": (40, 1840, 780, 1910),
}.items():
    im.crop(box).save(OUT / f"{name}.png")
    print("wrote", name, box)
