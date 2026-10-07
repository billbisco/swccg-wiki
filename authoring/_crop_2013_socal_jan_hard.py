#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal" / "socal_d1_p43"
im = Image.open(EXTRACT / "socal_d1_p43.png")
print("size", im.size)
for name, box in {
    "ln05": (40, 500, 780, 580),
    "ln13": (40, 780, 780, 860),
    "ln18": (40, 960, 780, 1040),
    "ln21_23": (40, 1080, 780, 1220),
    "ln48_50": (760, 560, 1490, 720),
    "ln55_58": (760, 760, 1490, 920),
    "sh12_15": (760, 1480, 1490, 1720),
    "jt": (760, 1780, 1490, 1920),
}.items():
    im.crop(box).save(OUT / f"{name}.png")
    print("wrote", name)
