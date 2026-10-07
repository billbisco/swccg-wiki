#!/usr/bin/env python3
"""Live QA for 2013 MPC Joe Pinto Xerox + AFA (V) under Effect."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 Joe Pinto LS Plead My Case To The Senate",
    "2013 Match Play Championship Day 1 Joe Pinto DS Carbon Chamber Testing",
    "2013 Match Play Championship",
    "Joe Pinto",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def section(text: str, heading: str) -> str:
    m = re.search(
        r"'''" + re.escape(heading) + r"'''(.*?)(?:'''|\|})",
        text,
        re.S,
    )
    return m.group(1) if m else ""


def main() -> int:
    n = 0
    for t in TITLES:
        data = api(
            {
                "action": "query",
                "format": "json",
                "prop": "info|flagged|revisions",
                "rvprop": "ids|content",
                "rvslots": "main",
                "titles": t,
            }
        )
        page = next(iter(data["query"]["pages"].values()))
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        if t.endswith("Plead My Case To The Senate"):
            effect = section(text, "Effect")
            interrupt = section(text, "Interrupt")
            if "Anger, Fear, Aggression (V)" not in effect:
                got.append("AFA_V_NOT_EFFECT")
            if "Anger, Fear, Aggression (V)" in interrupt:
                got.append("AFA_V_IN_INTERRUPT")
            if "[[File:2013 Match Play Championship p71 Joe Pinto LS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t.endswith("Carbon Chamber Testing"):
            if "Carbon Chamber Testing / My Favorite Decoration" not in text:
                got.append("MISSING_CCT_DUAL")
            if "[[File:2013 Match Play Championship p72 Joe Pinto DS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t == "2013 Match Play Championship":
            if "Joe Pinto DS Carbon Chamber Testing" not in text:
                got.append("HUB_MISSING_PINTO_DS")
            if "Joe Pinto LS Plead My Case To The Senate" not in text:
                got.append("HUB_MISSING_PINTO_LS")
        parsed = api(
            {
                "action": "parse",
                "format": "json",
                "page": t,
                "prop": "text",
            }
        )
        html = (parsed.get("parse") or {}).get("text", {}).get("*", "")
        if t.endswith("Plead My Case To The Senate"):
            m_eff = re.search(r"<b>Effect</b>(.*?)<b>", html, re.S | re.I)
            m_int = re.search(r"<b>Interrupt</b>(.*?)<b>", html, re.S | re.I)
            if "Anger, Fear, Aggression (V)" not in (m_eff.group(1) if m_eff else ""):
                got.append("PARSE_AFA_V_NOT_EFFECT")
            if "Anger, Fear, Aggression (V)" in (m_int.group(1) if m_int else ""):
                got.append("PARSE_AFA_V_IN_INTERRUPT")
        print(t)
        print("  stable", stable, "latest", latest, "len", len(text), "html", len(html))
        print("  issues", got or ["OK"])
        n += len(got)
    print("TOTAL", n, "issues")
    return 1 if n else 0


if __name__ == "__main__":
    raise SystemExit(main())
