#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_2015_2016 import EVENTS  # noqa
from generate_2019_2021 import wiki_fname  # noqa

PAGES = Path(__file__).resolve().parent / "pages"
issues: list[str] = []

SLANG_CELL = re.compile(
    r"\|\| (?:TTO|EOps|WHAP|TIGIH|SYCFA|CCT|MKOS|QMC|WYS|TRM|AOBS|BHBM|CRv|CPv|HDADTJ|TDIGWATT)\b",
    re.I,
)

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
    if SLANG_CELL.search(text):
        issues.append(f"SLANG {meta['title']}")
    for i, ln in enumerate(text.splitlines(), 1):
        if "||" not in ln or not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.split("||")]
        if any(c == "" for c in cells):
            issues.append(f"BLANK {meta['title']} L{i} {ln[:140]}")

    if meta["key"] == "15worlds":
        if "[[Joe Olson]]" not in text.split("== Day 2 ==")[0]:
            issues.append("15worlds Day 3 missing Olson")
        d3 = text.split("== Day 2 ==")[0]
        if "| 3 || [[Joe Olson]]" not in d3:
            issues.append("15worlds Olson not 3rd in Day 3")
        if "| 4 || [[Matt Sokol]]" not in d3:
            issues.append("15worlds Sokol not 4th in Day 3")
        if "| 1 || [[Justin Desai]]" not in d3:
            issues.append("15worlds Desai not 1st")
    if meta["key"] == "15sdgp":
        if "| 2 || [[Kevin Shannon]]" not in text:
            issues.append("15sdgp Shannon not 2nd")
        if "| 3 || [[Brian Fred]]" not in text:
            issues.append("15sdgp Fred not 3rd")
        if "| 1 || [[Joe Olson]]" not in text:
            issues.append("15sdgp Olson not 1st")
    if meta["key"] == "16worlds":
        if "| 1 || [[Tom Haid]]" not in text.split("== Day 2 ==")[0]:
            issues.append("16worlds Haid not Day 3 first")
    if meta["key"] == "16euro":
        if "== Day 3 ==" not in text:
            issues.append("16euro missing Day 3")
        if "| 1 || [[Emil Wallin]]" not in text.split("== Day 2 ==")[0]:
            issues.append("16euro Wallin not Day 3 first")

lst = (PAGES / "List_of_SWCCG_tournaments.wiki").read_text(encoding="utf-8")
for year in ("2018", "2017", "2016", "2015"):
    if f"== {year} ==" not in lst:
        issues.append(f"LIST missing {year}")
m2018 = lst.find("== 2018 ==")
m2017 = lst.find("== 2017 ==")
m2016 = lst.find("== 2016 ==")
m2015 = lst.find("== 2015 ==")
mdec = lst.find("== Decipher World Championships ==")
if not (m2018 < m2017 < m2016 < m2015 < mdec):
    issues.append(f"LIST year order {m2018, m2017, m2016, m2015, mdec}")
if "Wiki" in lst[m2016:mdec].split("\n")[4]:
    issues.append("LIST Wiki column in 2015-2016")

ks = PAGES / "Kevin_Shannon.wiki"
if ks.exists():
    kt = ks.read_text(encoding="utf-8")
    if "{|" not in kt or "2015 San Diego Grand Prix" not in kt:
        issues.append("Kevin Shannon missing 2015 SDGP table row")
    if "| 2 ||" not in kt and "|| 2 ||" not in kt:
        # finish cell is 4th column: `| dates || event || format || 2 ||`
        if "|| 2 ||" not in kt.replace("\n", " "):
            if not re.search(r"\|\| 2 \|\|", kt):
                issues.append("Kevin Shannon finish not 2")

print("n_issues", len(issues))
for x in issues:
    print(x)
