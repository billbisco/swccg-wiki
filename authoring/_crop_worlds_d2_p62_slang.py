#!/usr/bin/env python3
"""Recrop remaining slang from original strip files (source of truth)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
STRIPS = ROOT / "encyclopedia" / "pc-2013-events" / "extract" / "_strips" / "worlds"
OUT = ROOT / "encyclopedia" / "pc-2013-events" / "extract" / "_crops"
OUT.mkdir(parents=True, exist_ok=True)

# Strip images are left-column / right-column / shields slices of 1530x1980.
# Lbot is lower-left main lines; Rtop is upper-right continuation.
JOBS = [
    # p65 bottom handwritten extra interrupt
    ("worlds_d2_p65_SH.png", "p65_nogoodoo.png", (0, 0, 0, 0)),  # filled below
]


def save(src, dest, box):
    im = Image.open(STRIPS / src)
    im.crop(box).save(OUT / dest)
    print("crop", dest, im.size, box)


def main() -> None:
    # inspect sizes first
    for name in [
        "worlds_d2_p65_SH.png",
        "worlds_d2_p65_Lbot.png",
        "worlds_d2_p66_Rtop.png",
        "worlds_d2_p66_SH.png",
        "worlds_d2_p67_Lbot.png",
        "worlds_d2_p67_SH.png",
        "worlds_d2_p62_Rbot.png",
        "worlds_d2_p63_Lbot.png",
        "worlds_d2_p64_bot.png" if False else "worlds_d2_p64_Lbot.png",
    ]:
        p = STRIPS / name
        if p.exists():
            im = Image.open(p)
            print("size", name, im.size)

    # p65 Lbot: Tyranus Jar Jar is near top of Lbot
    save("worlds_d2_p65_Lbot.png", "p65_tyranus.png", (0, 0, 900, 180))
    # p65 SH bottom: Nogoodoo line
    im = Image.open(STRIPS / "worlds_d2_p65_SH.png")
    w, h = im.size
    save("worlds_d2_p65_SH.png", "p65_nogoodoo.png", (0, h - 220, w, h))
    save("worlds_d2_p65_SH.png", "p65_sh_hand.png", (0, 0, w, h))  # already have

    # p66 Rtop line 42 ~ 6th row of continuation (37-42)
    im = Image.open(STRIPS / "worlds_d2_p66_Rtop.png")
    w, h = im.size
    # 12-ish lines in Rtop; line 42 is 6th of 37-48
    save("worlds_d2_p66_Rtop.png", "p66_l42.png", (0, int(h * 0.38), w, int(h * 0.58)))

    # p66 SH line 30 is left column ~4th visible main line
    im = Image.open(STRIPS / "worlds_d2_p66_SH.png")
    w, h = im.size
    save("worlds_d2_p66_SH.png", "p66_navander.png", (0, int(h * 0.18), int(w * 0.62), int(h * 0.38)))
    save("worlds_d2_p66_SH.png", "p66_sh13.png", (0, h - 160, w, h))

    # p67 Lbot line 18 is 3rd row
    im = Image.open(STRIPS / "worlds_d2_p67_Lbot.png")
    w, h = im.size
    save("worlds_d2_p67_Lbot.png", "p67_l18b.png", (0, int(h * 0.08), w, int(h * 0.28)))
    save("worlds_d2_p67_Lbot.png", "p67_l30b.png", (0, int(h * 0.78), w, h))

    print("DONE", OUT)


if __name__ == "__main__":
    main()
