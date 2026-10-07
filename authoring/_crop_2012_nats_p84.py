#!/usr/bin/env python3
"""Notebook-dump bands for 2012 Nats Day 1 p84–p87 (not 2010 Xerox forms)."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"

for n in (84, 85, 86, 87):
    src = EXTRACT / f"nats_d1_p{n:02d}.png"
    out = EXTRACT / f"_p{n:02d}"
    out.mkdir(parents=True, exist_ok=True)
    im = Image.open(src)
    w, h = im.size
    im.crop((0, 0, w, int(h * 0.14))).save(out / "TOP.png")
    im.crop((0, int(h * 0.86), w, h)).save(out / "BOT.png")
    im.crop((int(w * 0.70), 0, w, int(h * 0.22))).save(out / "TR.png")
    im.crop((0, 0, int(w * 0.35), int(h * 0.18))).save(out / "TL.png")
    lx0, lx1 = int(w * 0.02), int(w * 0.52)
    rx0, rx1 = int(w * 0.48), int(w * 0.99)
    for name, y0f, y1f in (("C1", 0.08, 0.40), ("C2", 0.38, 0.70), ("C3", 0.68, 0.95)):
        im.crop((lx0, int(h * y0f), lx1, int(h * y1f))).save(out / f"{name}.png")
        im.crop((rx0, int(h * y0f), rx1, int(h * y1f))).save(out / f"R{name[1]}.png")
    print("cropped", src.name, w, h)
