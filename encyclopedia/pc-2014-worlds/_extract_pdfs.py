#!/usr/bin/env python3
"""Extract text + first-page renders from 2014 Worlds PDFs."""
from __future__ import annotations

from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parent
PDFS = ROOT / "pdfs"
OUT = ROOT / "extract"
OUT.mkdir(exist_ok=True)


def main() -> None:
    for pdf in sorted(PDFS.glob("*.pdf")):
        print("===", pdf.name, pdf.stat().st_size, flush=True)
        with pdfplumber.open(pdf) as doc:
            print(" pages", len(doc.pages), "meta", doc.metadata, flush=True)
            chunks = []
            for i, pg in enumerate(doc.pages, 1):
                t = pg.extract_text() or ""
                words = len(t.split())
                print(f"  p{i} words={words} w={pg.width:.0f} h={pg.height:.0f}", flush=True)
                chunks.append(f"\n\n===== PAGE {i} =====\n{t}")
                if i <= 2:
                    # save a low-res preview via pdfplumber
                    try:
                        im = pg.to_image(resolution=120)
                        dest = OUT / f"{pdf.stem}_p{i}.png"
                        im.save(dest)
                        print("   img", dest.name, dest.stat().st_size, flush=True)
                    except Exception as e:
                        print("   img-fail", e, flush=True)
            (OUT / (pdf.stem + ".txt")).write_text("".join(chunks), encoding="utf-8")
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
