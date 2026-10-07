#!/usr/bin/env python3
"""Bottom + full-width mid strips for typed dump p78–p81."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"

for n in (78, 79, 80, 81):
    src = EXTRACT / f"nats_d1_p{n:02d}.png"
    out = EXTRACT / f"_p{n:02d}"
    im = Image.open(src)
    w, h = im.size
    im.crop((0, int(h * 0.88), w, h)).save(out / "BOT.png")
    # tiny top strip in case a header sits above the whitespace
    im.crop((0, 0, w, int(h * 0.04))).save(out / "TINYTOP.png")
    print(src.name, w, h)
