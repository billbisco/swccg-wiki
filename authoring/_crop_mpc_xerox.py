#!/usr/bin/env python3
"""Column crops for 2013 MPC Xerox Print Form pages (1530x1980)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "mpc"

# Scaled from SoCal PRINT boxes (1530x2103) onto 1530x1980.
PRINT = {
    "hdr": (0, 0, 1530, 405),
    "L": (40, 377, 780, 1582),
    "La": (40, 377, 780, 781),
    "Lb": (40, 763, 780, 1167),
    "Lc": (40, 1148, 780, 1582),
    "Lf": (40, 1540, 780, 1960),
    "Rtop": (760, 377, 1490, 960),
    "Rmid": (760, 941, 1490, 1412),
    "Rbot": (760, 1393, 1490, 1960),
}

JOBS = [
    "mpc_p31.png",
    "mpc_p32.png",
    "mpc_p33.png",
    "mpc_p34.png",
    "mpc_p37.png",
    "mpc_p38.png",
    "mpc_p47.png",
    "mpc_p48.png",
    "mpc_p73.png",
    "mpc_p74.png",
    "mpc_p79.png",
    "mpc_p80.png",
    "mpc_p81.png",
    "mpc_p82.png",
    "mpc_p87.png",
    "mpc_p88.png",
    "mpc_p89.png",
    "mpc_p90.png",
    "mpc_p91.png",
    "mpc_p92.png",
    "mpc_p95.png",
    "mpc_p96.png",
    "mpc_p101.png",
    "mpc_p102.png",
    "mpc_p107.png",
    "mpc_p108.png",
    "mpc_p109.png",
    "mpc_p110.png",
    "mpc_p111.png",
    "mpc_p112.png",
    "mpc_p113.png",
    "mpc_p114.png",
    "mpc_p115.png",
    "mpc_p116.png",
]

INFORMAL = {
    "hdr": (0, 0, 1530, 180),
    "TL": (0, 0, 765, 990),
    "TR": (765, 0, 1530, 990),
    "BL": (0, 990, 765, 1980),
    "BR": (765, 990, 1530, 1980),
}
INFORMAL_JOBS = []


def main() -> None:
    for name in JOBS:
        src = EXTRACT / name
        dest = OUT / name.replace(".png", "")
        dest.mkdir(parents=True, exist_ok=True)
        im = Image.open(src)
        for key, box in PRINT.items():
            im.crop(box).save(dest / f"{key}.png")
        print("cropped", name, im.size, "->", dest)
    for name in INFORMAL_JOBS:
        src = EXTRACT / name
        dest = OUT / name.replace(".png", "")
        dest.mkdir(parents=True, exist_ok=True)
        im = Image.open(src)
        for key, box in INFORMAL.items():
            im.crop(box).save(dest / f"{key}.png")
        print("cropped informal", name, im.size, "->", dest)


if __name__ == "__main__":
    main()
