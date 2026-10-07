#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_2017_2018 import EVENTS  # noqa
from generate_2019_2021 import wiki_fname  # noqa

PAGES = Path(__file__).resolve().parent / "pages"
issues: list[str] = []

for meta in EVENTS:
    p = PAGES / wiki_fname(meta["title"])
    if not p.exists():
        issues.append(f"MISSING {meta['title']}")
        continue
    text = p.read_text(encoding="utf-8")
    if any(s in text.lower() for s in ("skip to content", "decklist pdfs", "volunteer forum")):
        issues.append(f"CHROME {meta['title']}")
    if "]]|" in text:
        issues.append(f"PIPE {meta['title']}")
    if "needs_source" in text or "Players Committee / GEMP card database" in text:
        issues.append(f"DISCLAIMER {meta['title']}")
    for i, ln in enumerate(text.splitlines(), 1):
        if "||" not in ln or not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.split("||")]
        if any(c == "" for c in cells):
            issues.append(f"BLANK {meta['title']} L{i} {ln[:140]}")

lst = (PAGES / "List_of_SWCCG_tournaments.wiki").read_text(encoding="utf-8")
if "== 2018 ==" not in lst or "== 2017 ==" not in lst:
    issues.append("LIST missing year sections")
if "[[Team USA]]" not in lst or "[[Team Europe]]" not in lst:
    issues.append("LIST missing team links")
if "[[Timo Dusel]]" not in lst:
    issues.append("LIST missing Timo")

print("n_issues", len(issues))
for x in issues:
    print(x)
