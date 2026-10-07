#!/usr/bin/env python3
"""Live HTML QA for Cite-beside-scan decks + Virtual Legacy hub."""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
UA = {"User-Agent": "SWCCGWikiQA/1.0", "Cache-Control": "no-cache"}

DECKS = [
    (
        "2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation",
        "2014 Worlds Day 3 p06 Matthew Harrison-Trainor DS.png",
        "Page 6 of",
        "2014 Worlds Day 3.pdf",
    ),
    (
        "2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned",
        "2014 Worlds Day 3 p07 Emil Wallin LS.png",
        "Page 7 of",
        "2014 Worlds Day 3.pdf",
    ),
    (
        "2014 Worlds Day 3 Emil Wallin DS Wookiee Slaving Operation",
        "2014 Worlds Day 3 p08 Emil Wallin DS.png",
        "Page 8 of",
        "2014 Worlds Day 3.pdf",
    ),
    (
        "2014 Worlds Day 3 Chris Terwilliger DS Hoth (V)",
        "2014 Worlds Day 3 p02 Chris Terwilliger DS.png",
        "Page 2 of",
        "2014 Worlds Day 3.pdf",
    ),
]


def get(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def api(**kw):
    kw.setdefault("format", "json")
    return json.loads(get(API + "?" + urllib.parse.urlencode(kw)))


def parse(title: str) -> tuple[int, str]:
    parsed = api(action="parse", page=title, prop="text|revid", disablelimitreport="1")
    return parsed["parse"]["revid"], parsed["parse"]["text"]["*"]


def flagged(title: str) -> tuple[int | None, int | None]:
    info = api(action="query", titles=title, prop="info|flagged")
    page = next(iter(info["query"]["pages"].values()))
    st = page.get("flagged", {}).get("stable_revid")
    return page.get("lastrevid"), st


fails: list[str] = []


def check(ok: bool, label: str) -> None:
    print(("OK  " if ok else "FAIL"), label)
    if not ok:
        fails.append(label)


for title, png, page_lab, pdf in DECKS:
    last, stable = flagged(title)
    revid, html = parse(title)
    print(f"\n== {title} last={last} stable={stable} parse={revid} ==")
    check(stable is not None and last == stable, f"{title} stable==latest")
    scan = html[html.find('id="Scan"') : html.find('id="See_also"')] if 'id="Scan"' in html else ""
    refs = html[html.find('id="References"') :] if 'id="References"' in html else ""
    check("<table" in scan, f"{title} scan table")
    check(png.replace(" ", "_") in scan or png in scan, f"{title} png in scan")
    check("cite_ref" in scan or "cite&#95;ref" in scan, f"{title} cite beside scan")
    check(not re.search(r"</figure>\s*<p>\s*<sup", scan), f"{title} no cite under image")
    check(page_lab not in scan, f"{title} no body caption")
    check(page_lab in refs, f"{title} caption in References")
    check(pdf.replace(" ", "_") in refs or pdf in refs, f"{title} pdf in References")

print("\n== Virtual Legacy ==")
last, stable = flagged("Virtual Legacy")
revid, html = parse("Virtual Legacy")
print(f"last={last} stable={stable} parse={revid}")
check(stable is not None and last == stable, "Virtual Legacy stable==latest")
check("#REDIRECT" not in html, "Virtual Legacy not a redirect")
for needle in [
    "Virtual Block 1",
    "Virtual Block 9",
    "Virtual Shields",
    "2014 Virtual Card Pool Reset",
    "Virtual Legacy Final Master DS",
    "Virtual Legacy Final Master LS",
    "2009",
    "Darkness Rising",
    "Republic At War",
]:
    check(needle in html, f"VL has {needle}")

print("\n== Files ==")
for fn in [
    "File:Virtual Legacy Final Master DS.pdf",
    "File:Virtual Legacy Final Master LS.pdf",
]:
    info = api(action="query", titles=fn, prop="imageinfo", iiprop="size|mime|url")
    page = next(iter(info["query"]["pages"].values()))
    ii = (page.get("imageinfo") or [{}])[0]
    print(fn, "size", ii.get("size"), "mime", ii.get("mime"))
    check(ii.get("mime") == "application/pdf", f"{fn} mime pdf")
    check(int(ii.get("size") or 0) > 10_000_000, f"{fn} large")

print("\n== Main Page overview ==")
_, html = parse("Main Page")
check("Overview: <a" in html and "Virtual_Legacy" in html, "Main Page Overview Virtual Legacy")

if fails:
    print("\nFAILS", len(fails))
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("\nQA_OK")
