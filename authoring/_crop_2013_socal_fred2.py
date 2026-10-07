#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parent
ST = ROOT / "encyclopedia" / "pc-2013-events" / "extract" / "_strips" / "socal"
p11 = ST / "socal_d1_p11"
p12 = ST / "socal_d1_p12"
im = Image.open(p11 / "Rmid.png")
w, h = im.size
im.crop((0, int(h * 2 / 16) - 4, w, int(h * 5 / 16) + 8)).save(p11 / "sh01.png")
im = Image.open(p11 / "Rmid.png")
im.crop((0, int(h * 13 / 16) - 8, w, h)).save(p11 / "sh13.png")
im = Image.open(p12 / "La.png")
w, h = im.size
im.crop((0, 0, w, int(h * 3 / 12) + 10)).save(p12 / "s02.png")
im = Image.open(p12 / "Lb.png")
w, h = im.size
im.crop((0, int(h * 3 / 12) - 4, w, int(h * 5 / 12) + 10)).save(p12 / "s16.png")
im = Image.open(p12 / "Lc.png")
w, h = im.size
im.crop((0, int(h * 4 / 13) - 4, w, int(h * 6 / 13) + 10)).save(p12 / "s28.png")
im.crop((0, int(h * 10 / 13) - 4, w, int(h * 12 / 13) + 8)).save(p12 / "s35.png")
im = Image.open(p12 / "Lbot.png")
w, h = im.size
im.crop((0, int(h * 4 / 6) - 4, w, h)).save(p12 / "s40.png")
im = Image.open(p12 / "Rtop.png")
w, h = im.size
im.crop((0, int(h * 7 / 17) - 4, w, int(h * 9 / 17) + 8)).save(p12 / "s49.png")
im.crop((0, int(h * 14 / 17) - 4, w, int(h * 16 / 17) + 8)).save(p12 / "s56.png")
im = Image.open(p12 / "Rmid.png")
w, h = im.size
im.crop((0, 0, w, int(h * 3 / 16) + 10)).save(p12 / "s60.png")
print("ok")
