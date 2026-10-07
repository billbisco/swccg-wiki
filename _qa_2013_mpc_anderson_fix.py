#!/usr/bin/env python3
"""Live QA for Anderson/Herold LS MWYHL 7-side and Jedi Test grouping."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 John Anderson LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Brian Herold LS Mind What You Have Learned (V)",
]
JEDI = [
    "Great Warrior",
    "A Jedi's Strength",
    "Domain Of Evil",
    "Size Matters Not",
    "It Is The Future You See",
    "You Must Confront Vader",
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
        if "I'm On The Leader" in text:
            got.append("SLANG_7SIDE")
        if "[[Mind What You Have Learned (V) / Save You It Can (V)]]" not in text:
            got.append("MISSING_DUAL_DEST")
        epic = section(text, "Epic Event")
        jedi = section(text, "Jedi Test")
        sh = section(text, "Defensive Shield")
        if "It Is The Future You See (V)" not in epic:
            got.append("IITFYS_V_NOT_EPIC")
        if "It Is The Future You See (V)" in jedi:
            got.append("IITFYS_V_IN_JEDI_TEST")
        for name in JEDI:
            if f"[[{name}]]" not in jedi:
                got.append(f"JEDI_MISSING_{name}")
            if f"[[{name}]]" in sh:
                got.append(f"JEDI_IN_SHIELD_{name}")
        parsed = api(
            {
                "action": "parse",
                "format": "json",
                "page": t,
                "prop": "text",
            }
        )
        html = (parsed.get("parse") or {}).get("text", {}).get("*", "")
        if "I'm On The Leader" in html:
            got.append("PARSE_SLANG_7SIDE")
        if "Save You It Can (V)" not in html:
            got.append("PARSE_MISSING_7SIDE")
        if "Jedi Test" not in html:
            got.append("PARSE_MISSING_JEDI_HEADING")
        if "Great Warrior" not in html:
            got.append("PARSE_MISSING_GREAT_WARRIOR")
        print(t)
        print("  stable", stable, "latest", latest, "len", len(text), "html", len(html))
        print("  issues", got or ["OK"])
        n += len(got)
    print("TOTAL", n, "issues")
    return 1 if n else 0


if __name__ == "__main__":
    raise SystemExit(main())
