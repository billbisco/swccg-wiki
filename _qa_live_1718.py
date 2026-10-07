#!/usr/bin/env python3
"""Fetch live 2017–2018 hubs + team/list pages and report HTML quality issues."""
from __future__ import annotations

import re
import time
import urllib.request
from html.parser import HTMLParser

URLS = [
    "https://wiki.swccg.com/wiki/Team_USA",
    "https://wiki.swccg.com/wiki/Team_Europe",
    "https://wiki.swccg.com/wiki/Team_North_America",
    "https://wiki.swccg.com/wiki/2023_Online_Retro_Event",
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
    "https://wiki.swccg.com/wiki/Timo_Dusel",
    "https://wiki.swccg.com/wiki/Jonny_Chu",
    "https://wiki.swccg.com/wiki/European_Championships",
    "https://wiki.swccg.com/wiki/Category:Teams",
    "https://wiki.swccg.com/wiki/2019_Outrider_Cup",
]


class TableScan(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_td = False
        self.td_text: list[str] = []
        self.empty = 0
        self.cells = 0
        self.dash = 0
        self.sample_empty: list[str] = []
        self.in_content = False
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        if tag == "div" and ad.get("id") == "mw-content-text":
            self.in_content = True
            self.depth = 1
        elif self.in_content and tag == "div":
            self.depth += 1
        if self.in_content and tag in ("td", "th"):
            self.in_td = True
            self.td_text = []

    def handle_endtag(self, tag):
        if self.in_td and tag in ("td", "th"):
            text = re.sub(r"\s+", " ", "".join(self.td_text)).strip()
            self.cells += 1
            if text == "—":
                self.dash += 1
            elif text == "" and tag == "td":
                self.empty += 1
                if len(self.sample_empty) < 6:
                    self.sample_empty.append("(empty td)")
            self.in_td = False
        if self.in_content and tag == "div":
            self.depth -= 1
            if self.depth <= 0:
                self.in_content = False

    def handle_data(self, data):
        if self.in_td:
            self.td_text.append(data)


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "SWCCGWikiQA/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main() -> None:
    for url in URLS:
        title = url.rsplit("/", 1)[-1]
        try:
            status, html = fetch(url)
        except Exception as e:
            print(f"FAIL {title} {e}")
            continue
        flags = []
        if "There is currently no text" in html or "does not exist" in html and 'class="noarticletext"' in html:
            flags.append("MISSING")
        if "Error creating thumbnail" in html:
            flags.append("THUMB")
        if "Decklist pdfs" in html or "Skip to content" in html:
            flags.append("CHROME")
        if "needs_source" in html or "Players Committee / GEMP card database" in html:
            flags.append("DISCLAIMER")
        reds = re.findall(r'href="/wiki/([^"]+)"[^>]*class="new"', html)
        m = re.search(r'id="firstHeading"[^>]*>(.*?)</h1>', html, re.S)
        heading = re.sub("<[^>]+>", "", m.group(1)).strip() if m else "?"
        scan = TableScan()
        scan.feed(html)
        # empty <td></td> or <td>\s+</td> in content
        empty_td = len(re.findall(r"<td[^>]*>\s*</td>", html))
        print(
            f"OK {status} {heading} bytes={len(html)} empty_td={empty_td} "
            f"cells={scan.cells} dash={scan.dash} empty_scan={scan.empty} "
            f"reds={len(reds)} flags={flags}"
        )
        if reds:
            uniq = sorted(set(reds))
            print("  RED", uniq[:20], ("..." if len(uniq) > 20 else ""))
        needles = []
        if "Timo Dusel" in heading or "Retro" in heading:
            for n in ("Timo Dusel", "Joe Horbey", "Imperial Occupation", "Hidden Base"):
                if n in html:
                    needles.append(n)
            print("  needles", needles)
        if heading.startswith("List"):
            for n in ("Team USA", "Team Europe", "Timo Dusel", "2018", "2017", "Kevin Jaap", "Phil Aasen"):
                if n in html:
                    needles.append(n)
            print("  list", needles)
        if "Team" in heading:
            for n in ("Joe Olson", "Bastian Winkelhaus", "Captain's pick", "Murica", "North America"):
                if n in html:
                    needles.append(n)
            print("  team", needles)
        time.sleep(0.25)


if __name__ == "__main__":
    main()
