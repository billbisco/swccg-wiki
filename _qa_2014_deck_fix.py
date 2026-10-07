#!/usr/bin/env python3
"""Live QA: PDF scans, Virtual Block dests, Coruscant Jawa counterparts."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext|text", "format": "json"}
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "SWCCGWikiQA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))["parse"]


issues: list[str] = []

mht = parse("2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing")
wt, html = mht["wikitext"]["*"], mht["text"]["*"]
if "Sai'torr Kal Fas (V) (Virtual Block 1)" not in wt:
    issues.append("MHT LS missing Sai'torr VB1 dest")
if "Sai'tor Kal Fas" in wt:
    issues.append("MHT LS still has Sai'tor typo dest")
if "2014 Worlds Day 3 p05 Matthew Harrison-Trainor LS.png" not in wt:
    issues.append("MHT LS missing page-scan File")
if "2014_Worlds_Day_3_p05" not in html and "p05_Matthew" not in html:
    issues.append("MHT LS HTML missing scan img")
if 'class="mw-file-element"' not in html and "<img" not in html.lower():
    issues.append("MHT LS HTML has no img")

ds = parse("2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation")
if "Imperial Occupation (V) / Imperial Control (V)" not in ds["wikitext"]["*"]:
    issues.append("MHT DS missing dual (V) dest")
if "2014 Worlds Day 3 p06" not in ds["wikitext"]["*"]:
    issues.append("MHT DS missing page-scan File")

emil = parse("2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned")
if "Mind What You Have Learned (V) / Save You It Can (V)" not in emil["wikitext"]["*"]:
    issues.append("Emil LS missing dual (V) dest")
if "p07 Emil Wallin LS.png" not in emil["wikitext"]["*"]:
    issues.append("Emil LS missing page-scan File")

lsj = parse("Jawa (Coruscant)")
if "Jawa (Dark) (Coruscant)" not in lsj["wikitext"]["*"]:
    issues.append("LS Coruscant Jawa counterpart not DS Coruscant")
if 'href="/wiki/Jawa_(Dark)_(Coruscant)"' not in lsj["text"]["*"]:
    issues.append("LS Coruscant Jawa HTML counterpart not DS Coruscant dest")

dsj = parse("Jawa (Dark) (Coruscant)")
dwt, dhtml = dsj["wikitext"]["*"], dsj["text"]["*"]
if "Jawa (Coruscant)" not in dwt:
    issues.append("DS Coruscant Jawa counterpart not LS Coruscant")
# Counterpart section must not point at Premiere Jawa as the dest.
cp = dwt.split("|counterpart=", 1)[-1].split("|", 1)[0]
if cp.strip() in ("* [[Jawa]] (EP1)", "* [[Jawa]]"):
    issues.append(f"DS counterpart still Premiere: {cp!r}")
if 'href="/wiki/Jawa_(Coruscant)"' not in dhtml:
    issues.append("DS Coruscant Jawa HTML counterpart not LS Coruscant dest")

print("MHT LS scan snip:")
i = html.find("Scan")
print(html[i : i + 700] if i >= 0 else "NO SCAN HEADING")
print("---")
print("LS Jawa counterpart wikitext:", [ln for ln in lsj["wikitext"]["*"].splitlines() if "counterpart" in ln])
print("DS Jawa counterpart wikitext:", [ln for ln in dwt.splitlines() if "counterpart" in ln])
if issues:
    print("ISSUES", len(issues))
    for x in issues:
        print(" -", x)
    raise SystemExit(1)
print("QA OK")
