#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal"

# Tight row crops for ambiguous lines on 1530x2103 Print Form.
# Left numbered rows ~34px; right similar. Calibrated from PRINT L/R.
P23 = EXTRACT / "socal_d1_p23.png"
P24 = EXTRACT / "socal_d1_p24.png"
d23 = OUT / "socal_d1_p23"
d24 = OUT / "socal_d1_p24"

# L01_04 is (40,330,780,520) covering lines 1-4. ~47.5 px/line.
# Use original page crops around known ambiguous rows.
jobs = [
    (P23, d23, "ls01", (40, 330, 780, 430)),
    (P23, d23, "ls06_13", (40, 480, 780, 780)),
    (P23, d23, "ls12_16", (40, 720, 780, 920)),
    (P23, d23, "ls32_40", (40, 1480, 780, 1900)),
    (P23, d23, "ls41_44", (760, 330, 1490, 520)),
    (P23, d23, "ls50_53", (760, 620, 1490, 800)),
    (P23, d23, "lssh", (760, 1000, 1490, 1600)),
    (P24, d24, "ds01_08", (40, 330, 780, 720)),
    (P24, d24, "ds13_15", (40, 760, 780, 920)),
    (P24, d24, "ds32_40", (40, 1480, 780, 1900)),
    (P24, d24, "ds41_46", (760, 330, 1490, 620)),
    (P24, d24, "ds52_60", (760, 720, 1490, 1100)),
    (P24, d24, "dssh", (760, 1000, 1490, 1750)),
]
for src, dest, key, box in jobs:
    dest.mkdir(parents=True, exist_ok=True)
    Image.open(src).crop(box).save(dest / f"{key}.png")
    print("wrote", dest / f"{key}.png")
