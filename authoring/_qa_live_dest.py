#!/usr/bin/env python3
import re
import urllib.request

URLS = [
    "https://wiki.swccg.com/wiki/Outrider_Cup",
    "https://wiki.swccg.com/wiki/Team_USA",
    "https://wiki.swccg.com/wiki/2018_European_Championship",
    "https://wiki.swccg.com/wiki/2018_European_Match_Play_Championship",
    "https://wiki.swccg.com/wiki/2017_European_Championship",
    "https://wiki.swccg.com/wiki/Timo_Dusel",
    "https://wiki.swccg.com/wiki/2023_Online_Retro_Event",
    "https://wiki.swccg.com/wiki/Category:Teams",
]
NEED = {
    "Outrider_Cup": ["Team USA", "Team Europe", "2019 Outrider Cup", "2021 Outrider Cup"],
    "Team_USA": ["Outrider Cup"],
    "2018_European_Championship": ["Twin Suns Of Tatooine", "Jedi Council Chamber", "Emil Wallin"],
    "2018_European_Match_Play_Championship": ["Twin Suns Of Tatooine", "Kevin Jaap"],
    "2017_European_Championship": ["Twin Suns Of Tatooine", "Jedi Council Chamber", "Bastian Winkelhaus"],
    "Timo_Dusel": ["2023 Online Retro Event", "Imperial Occupation"],
    "2023_Online_Retro_Event": ["Timo Dusel", "Imperial Occupation", "Joe Horbey"],
    "Category:Teams": ["Team USA", "Team Europe", "Outrider Cup"],
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "SWCCGWikiQA/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


for url in URLS:
    key = url.rsplit("/", 1)[-1]
    html = fetch(url)
    reds = re.findall(r'href="/wiki/([^"]+)" class="new"', html)
    reds2 = re.findall(r'class="new"[^>]*href="/wiki/([^"]+)"', html)
    empty = len(re.findall(r"<td[^>]*>\s*</td>", html))
    hits = [n for n in NEED.get(key, []) if n in html]
    miss = [n for n in NEED.get(key, []) if n not in html]
    print(key, "bytes", len(html), "empty_td", empty, "reds", len(set(reds + reds2)), "hits", hits, "MISS", miss)
    if reds or reds2:
        print("  RED", sorted(set(reds + reds2))[:12])
    if key == "Timo_Dusel":
        m = re.search(r"2023 Online Retro Event.{0,400}", html)
        if m:
            snippet = re.sub("<[^>]+>", " ", m.group(0))
            snippet = re.sub(r"\s+", " ", snippet)[:240]
            print("  retro", snippet)
