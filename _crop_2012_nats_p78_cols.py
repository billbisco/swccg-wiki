#!/usr/bin/env python3
"""Tall left-column bands for typed dump p78-p81 (list is left-aligned)."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"

for n in (78, 79, 80, 81):
    src = EXTRACT / f"nats_d1_p{n:02d}.png"
    out = EXTRACT / f"_p{n:02d}"
    im = Image.open(src)
    w, h = im.size
    x0, x1 = int(w * 0.04), int(w * 0.78)
    bands = (
        ("C1", 0.08, 0.40),
        ("C2", 0.38, 0.70),
        ("C3", 0.68, 0.92),
    )
    for name, y0f, y1f in bands:
        im.crop((x0, int(h * y0f), x1, int(h * y1f))).save(out / f"{name}.png")
    print("cols", src.name)
