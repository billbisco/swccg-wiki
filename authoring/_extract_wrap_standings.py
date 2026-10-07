#!/usr/bin/env python3
"""Dump wrap headings + Name – Dark – Light lines for 2019–2021 hubs."""
from __future__ import annotations

import html
import re
from pathlib import Path

BASE = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2019-2021")
OUT = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2019-2021-standings.txt")

FILES = [
    "19egp.html",
    "19mpc.html",
    "19euro.html",
    "19nac.html",
    "19worlds.html",
    "19outrider.html",
    "20egp.html",
    "20mpc.html",
    "20texas.html",
    "20worlds.html",
    "21mpc.html",
    "21nats.html",
    "21retro-b.html",
    "21regionals.html",
    "21throwback.html",
    "21worlds.html",
    "21ocs.html",
    "21outrider.html",
]


def visible(raw: str) -> str:
    m = re.search(
        r'fl-module-fl-post-content[\s\S]*?fl-module-content fl-node-content">([\s\S]*?)<div class="fl-col fl-node-5d13d237ac255"',
        raw,
    )
    if not m:
        m = re.search(
            r'fl-module-fl-post-content[\s\S]*?fl-module-content fl-node-content">([\s\S]*?)</div>\s*</div>\s*</div>\s*</div>',
            raw,
        )
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</h[1-6]>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<h([1-6])[^>]*>", r"\n###H\1 ", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", "\n", chunk)
    chunk = html.unescape(chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    lines = [ln.strip() for ln in chunk.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def main() -> None:
    bits = []
    for name in FILES:
        p = BASE / name
        if not p.exists():
            bits.append(f"MISSING {name}\n")
            continue
        raw = p.read_text(encoding="utf-8", errors="replace")
        text = visible(raw)
        bits.append("=" * 80)
        bits.append(name)
        bits.append("-" * 40)
        # keep headings and dash-name lines
        keep = []
        for ln in text.splitlines():
            if ln.startswith("###H") or re.match(
                r"^(Day\s*[123]|FINAL|Final|Top\s*\d|Round|Bespin|Endor|Yavin|Tatooine|Coruscant|Dagobah|Corellia|Alderaan|Nal Hutta|Team |USA|Europe|Congrats|Winner)",
                ln,
                re.I,
            ):
                keep.append(ln)
            elif re.match(r"^\d{1,2}[\.\)]\s+\S", ln):
                keep.append(ln)
            elif re.search(r"[–—-].+[–—-]", ln) and re.match(r"^[A-Z]", ln):
                keep.append(ln)
            elif re.search(r"def\.|defeated", ln, re.I):
                keep.append(ln)
        bits.extend(keep[:220])
        bits.append("")
    OUT.write_text("\n".join(bits) + "\n", encoding="utf-8")
    print("wrote", OUT, "lines", len(bits))


if __name__ == "__main__":
    main()
