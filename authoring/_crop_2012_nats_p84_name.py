#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"

# p84 right black bar, p85 left black square
im84 = Image.open(EXTRACT / "nats_d1_p84.png")
w, h = im84.size
im84.crop((int(w * 0.55), 0, w, int(h * 0.28))).save(EXTRACT / "_p84" / "NAME.png")
ImageOps.invert(ImageEnhance.Contrast(im84.crop((int(w * 0.55), 0, w, int(h * 0.28))).convert("L")).enhance(2.5)).save(EXTRACT / "_p84" / "NAME_INV.png")

im85 = Image.open(EXTRACT / "nats_d1_p85.png")
w, h = im85.size
im85.crop((0, 0, int(w * 0.28), int(h * 0.28))).save(EXTRACT / "_p85" / "NAME.png")
ImageOps.invert(ImageEnhance.Contrast(im85.crop((0, 0, int(w * 0.28), int(h * 0.28))).convert("L")).enhance(2.5)).save(EXTRACT / "_p85" / "NAME_INV.png")

im86 = Image.open(EXTRACT / "nats_d1_p86.png")
w, h = im86.size
im86.crop((int(w * 0.65), 0, w, int(h * 0.25))).save(EXTRACT / "_p86" / "NAME.png")
im86.crop((0, 0, int(w * 0.30), int(h * 0.20))).save(EXTRACT / "_p86" / "TL.png")

im87 = Image.open(EXTRACT / "nats_d1_p87.png")
w, h = im87.size
im87.crop((int(w * 0.65), 0, w, int(h * 0.25))).save(EXTRACT / "_p87" / "NAME.png")
print("name crops")
