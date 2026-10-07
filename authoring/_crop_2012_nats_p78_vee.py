#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"
for n in (78, 79):
    im = Image.open(EXTRACT / f"nats_d1_p{n:02d}.png")
    w, h = im.size
    out = EXTRACT / f"_p{n:02d}"
    im.crop((int(w * 0.72), int(h * 0.62), w, int(h * 0.88))).save(out / "VEE.png")
    print("vee", n)
