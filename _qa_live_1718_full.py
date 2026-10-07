#!/usr/bin/env python3
"""Live HTML quality check for 2017–2018 hubs, team pages, 2023 retro."""
import re
import urllib.request

URLS = [
    "https://wiki.swccg.com/wiki/Team_USA",
    "https://wiki.swccg.com/wiki/Team_Europe",
    "https://wiki.swccg.com/wiki/Outrider_Cup",
    "https://wiki.swccg.com/wiki/Category:Teams",
    "https://wiki.swccg.com/wiki/2023_Online_Retro_Event",
    "https://wiki.swccg.com/wiki/Timo_Dusel",
    "https://wiki.swccg.com/wiki/List_of_SWCCG_tournaments",
    "https://wiki.swccg.com/wiki/2018_World_Championship",
    "https://wiki.swccg.com/wiki/2018_European_Championship",
    "https://wiki.swccg.com/wiki/2018_U.S._National_Championship",
    "https://wiki.swccg.com/wiki/2018_Endor_Grand_Prix",
    "https://wiki.swccg.com/wiki/2018_European_Match_Play_Championship",
    "https://wiki.swccg.com/wiki/2018_Match_Play_Championship",
    "https://wiki.swccg.com/wiki/2018_Online_Championship_Series",
    "https://wiki.swccg.com/wiki/2017_Texas_Mini_Worlds",
    "https://wiki.swccg.com/wiki/2017_European_Championship",
    "https://wiki.swccg.com/wiki/2017_World_Championship",
    "https://wiki.swccg.com/wiki/2017_U.S._National_Championship",
    "https://wiki.swccg.com/wiki/2017_Endor_Grand_Prix",
    "https://wiki.swccg.com/wiki/2017_Match_Play_Championship",
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "SWCCGWikiQA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


bad = 0
for url in URLS:
    key = url.rsplit("/", 1)[-1]
    try:
        html = fetch(url)
    except Exception as e:
        print(f"FETCHFAIL {key} {e}")
        bad += 1
        continue
    if "There is currently no text in this page" in html or "does not exist" in html.lower() and "redlink" in html.lower() and "firstHeading" in html:
        if 'class="noarticletext"' in html or "no text in this page" in html:
            print(f"MISSING {key}")
            bad += 1
            continue
    reds = set(re.findall(r'class="new"[^>]*title="([^"]+)"', html))
    reds |= set(re.findall(r'title="([^"]+) \(page does not exist\)"', html))
    empty = len(re.findall(r"<td[^>]*>\s*</td>", html))
    disclaimer = bool(re.search(r"needs_source|GEMP card database|not Decipher printed", html, re.I))
    print(f"{key} bytes={len(html)} empty_td={empty} reds={len(reds)} disclaimer={disclaimer}")
    if empty or reds or disclaimer:
        bad += 1
        if reds:
            print("  RED", sorted(reds)[:20])
print("DONE bad=", bad)
