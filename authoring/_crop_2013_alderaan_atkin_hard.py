#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "alderaan"
im = Image.open(EXTRACT / "alderaan_p10.png")
dest = OUT / "alderaan_p10"
dest.mkdir(parents=True, exist_ok=True)
im.crop((40, 400, 780, 620)).save(dest / "p10_L01_08.png")
im.crop((40, 1180, 780, 1400)).save(dest / "p10_L24_28.png")
print("ok", im.size)
