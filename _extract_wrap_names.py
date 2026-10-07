#!/usr/bin/env python3
"""Pull player-ish lines from wrap HTML around last-name tokens."""
from __future__ import annotations

import html
import re
from pathlib import Path

WRAP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024")
NEEDLES = [
    "Birgander",
    "Gabor",
    "George",
    "Petersson",
    "Póra",
    "Pora",
    "Smolarek",
    "Tegeler",
    "Wauters",
    "Bolletino",
    "Bollentino",
    "Sammartano",
    "Butterworth",
    "Partridge",
    "Cooper",
    "LaPorta",
    "Laporta",
    "Lutz",
    "Murray",
    "Pittman",
    "Sesnick",
    "Hayes",
    "Kahler",
    "Usnats",
    "Kafer",
    "Carr",
    "Marlin",
    "Scinocca",
    "Tarbox",
    "Christiana",
    "Gardner",
    "Haid",
    "Kristiansen",
    "Louderback",
    "Bailey",
    "Boyd",
    "Carulli",
    "Dixon",
    "Fuentes",
    "Hedlund",
    "Hull",
    "Wexstten",
    "Luhks",
    "Joe ",
]

FILES = [
    "2024-09-worlds.html",
    "2024-08-nacc.html",
    "2024-04-eclipse.html",
    "2024-01-sss.html",
    "2024-06-euro.html",
    "2023-04-nats.html",
    "2023-09-egp.html",
    "2023-11-outrider.html",
    "2023-06-retro.html",
    "2023-07-worlds.html",
    "2022-04-pc20.html",
    "2022-07-nats.html",
]


def text_of(p: Path) -> str:
    raw = p.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
    raw = re.sub(r"<style[\s\S]*?</style>", " ", raw, flags=re.I)
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"</p>", "\n", raw, flags=re.I)
    raw = re.sub(r"</li>", "\n", raw, flags=re.I)
    raw = re.sub(r"</h[1-6]>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = raw.replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    return raw


for fn in FILES:
    p = WRAP / fn
    if not p.exists():
        print("NOFILE", fn)
        continue
    t = text_of(p)
    print("\n========", fn, "========")
    for needle in NEEDLES:
        for m in re.finditer(re.escape(needle), t, flags=re.I):
            a = max(0, m.start() - 80)
            b = min(len(t), m.end() + 80)
            snippet = t[a:b].replace("\n", " | ")
            print(f"  {needle}: ...{snippet}...")
