#!/usr/bin/env python3
"""Low-res header crops of 2014 Xerox PDFs so we can index player names."""
from __future__ import annotations

from pathlib import Path

import pdfplumber
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2014-events"
OUT = SRC / "extract" / "headers"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = [
    ("MPC-2014-Day-1-Main-Event.pdf", "mpc_d1"),
    ("Nationals-2014-day-2.pdf", "nats_d2"),
    ("2014-TMW-Day-1.pdf", "tmw_d1"),
    ("2014-TMW-Day-2.pdf", "tmw_d2"),
    ("2014-Alderaan-Regionals.pdf", "alderaan"),
    ("MPC-2014-Day-2-Consolation-Event.pdf", "mpc_cons"),
]


def main() -> None:
    for fname, prefix in JOBS:
        pdf = SRC / fname
        print("===", fname, flush=True)
        if not pdf.exists():
            print(" MISSING", flush=True)
            continue
        with pdfplumber.open(pdf) as doc:
            print(" pages", len(doc.pages), flush=True)
            for i, pg in enumerate(doc.pages, start=1):
                dest = OUT / f"{prefix}_h{i:03d}.png"
                if dest.exists() and dest.stat().st_size > 2_000:
                    continue
                im = pg.to_image(resolution=72)
                pil = im.original
                w, h = pil.size
                # name box is top-right of 2010/2013 form
                crop = pil.crop((int(w * 0.55), 0, w, int(h * 0.22)))
                crop.save(dest)
                if i <= 3 or i % 10 == 0:
                    print(" ", dest.name, crop.size, dest.stat().st_size, flush=True)
        print(" done", prefix, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
