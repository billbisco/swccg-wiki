#!/usr/bin/env python3
"""Handwritten corners + right-edge notes on p78-p81."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"

for n in (78, 79, 80, 81):
    src = EXTRACT / f"nats_d1_p{n:02d}.png"
    out = EXTRACT / f"_p{n:02d}"
    im = Image.open(src)
    w, h = im.size
    # right-bottom corner handwriting
    im.crop((int(w * 0.70), int(h * 0.82), w, h)).save(out / "RBC.png")
    # right-edge mid (annotations next to list)
    im.crop((int(w * 0.70), int(h * 0.08), w, int(h * 0.40))).save(out / "RE1.png")
    im.crop((int(w * 0.70), int(h * 0.38), w, int(h * 0.70))).save(out / "RE2.png")
    print("notes", src.name)
