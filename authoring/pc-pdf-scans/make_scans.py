#!/usr/bin/env python3
"""make_scans.py <scans.tsv> <pdf_dir> <media_out> : render each deck's sheet page(s) at 130 dpi, stack, save PNG (grayscale)."""
import subprocess, sys, tempfile, os
from pathlib import Path
from PIL import Image, ImageStat


def upright(im, path):
    """Form sheets: the STAR WARS logo block is top-left; if the dark block is bottom-right the scan is upside down.
    Typed lists (no logo): tesseract orientation detection."""
    w, h = im.size
    tl = 255 - ImageStat.Stat(im.crop((int(.04*w), int(.03*h), int(.27*w), int(.17*h)))).mean[0]
    br = 255 - ImageStat.Stat(im.crop((int(.73*w), int(.83*h), int(.96*w), int(.97*h)))).mean[0]
    if br > 50 and br > 2 * tl:
        return im.rotate(180)
    if tl > 50 and tl > 2 * br:
        return im
    try:
        o = subprocess.run(["tesseract", str(path), "-", "--psm", "0"], capture_output=True, text=True, timeout=60).stdout
        if "Rotate: 180" in o and float((__import__("re").search(r"Orientation confidence: ([\d.]+)", o) or [0, "0"])[1]) > 3:
            return im.rotate(180)
    except Exception:
        pass
    return im
tsv, pdfdir, outd = sys.argv[1:4]
Path(outd).mkdir(parents=True, exist_ok=True)
for line in open(tsv, encoding="utf-8").read().splitlines():
    if not line.strip(): continue
    name, pdf, pages = line.split("\t")
    dst = Path(outd) / name
    if dst.exists(): continue
    ims = []
    with tempfile.TemporaryDirectory() as td:
        for p in pages.split(","):
            subprocess.run(["pdftoppm", "-r", "130", "-gray", "-f", p, "-l", p, "-png", os.path.join(pdfdir, pdf), f"{td}/x{p}"], check=True,
                           stderr=subprocess.DEVNULL)
            f = sorted(Path(td).glob(f"x{p}*.png"))[0]
            ims.append(upright(Image.open(f).convert("L"), f))
        w = max(i.width for i in ims); h = sum(i.height for i in ims)
        canvas = Image.new("L", (w, h), 255); y = 0
        for i in ims:
            canvas.paste(i, (0, y)); y += i.height
        canvas.save(dst, optimize=True)
print("ok")
