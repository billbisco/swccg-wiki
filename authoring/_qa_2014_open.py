#!/usr/bin/env python3
"""QA 2014 Open generated pages before apply."""
from __future__ import annotations
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2014-open-titles.tsv"
PAGES = ROOT / "pages"

n_deck = n_hub = 0
constructed = []
low_v = Counter()
start_dash = []
dmm = []
qty_issues = []
format_wrong = []
no_list = []

for line in TSV.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    p = ROOT / rel.strip()
    if not p.exists():
        print("MISSING", title)
        continue
    text = p.read_text(encoding="utf-8")
    is_hub = title in {
        "2014 Philadelphia Premiere Event",
        "2014 European Championship Reset Beta",
        "2014 World Championship Reset Beta",
        "List of SWCCG tournaments",
        "European Championships",
        "2014 World Championship",
    } or title.startswith("Category:")
    if "[[Category:Decklists]]" in text or "== Decklist ==" in text:
        n_deck += 1
        if " constructed'''" in text.split("\n", 1)[0] or title.endswith("constructed"):
            constructed.append(title)
        if "* '''Starting Card:''' —" in text or "* '''Starting Card:''' -" in text:
            start_dash.append(title)
        if "[[Legacy Open]]" in text:
            format_wrong.append(title)
        for m in re.finditer(r"\[\[([^\]]+\(v\))(?:\|[^\]]+)?\]\]", text):
            low_v[m.group(1)] += 1
        # count card lines
        cards = re.findall(r"^\* (\d+)x ", text, re.M)
        ones = re.findall(r"^\* \[\[", text, re.M)
        n = sum(int(x) for x in cards) + len(ones)
        if n < 50:
            qty_issues.append((title, n))
        if "DDM" in title or " DDM" in text[:200]:
            dmm.append(title)
    elif is_hub or "== Results ==" in text:
        n_hub += 1

print("decks", n_deck, "hubs", n_hub)
print("constructed titles", len(constructed))
for t in constructed:
    print("  ", t)
print("start —", len(start_dash))
for t in start_dash:
    print("  ", t)
print("format Legacy", format_wrong)
print("qty<50", qty_issues[:20], "n", len(qty_issues))
print("DDM", dmm)
print("lowercase (v) unique", len(low_v), "total", sum(low_v.values()))
print("top (v):")
for k, v in low_v.most_common(15):
    print(f"  {v:3d} {k}")
