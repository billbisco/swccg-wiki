#!/usr/bin/env python3
"""Live QA leftover 2013 Worlds Day 2 Stern/Brusca/Carulli/Chu."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Worlds Day 2 Brandon Stern DS My Lord, Is That Legal?",
    "2013 Worlds Day 2 Brandon Stern LS Watch Your Step",
    "2013 Worlds Day 2 Victor G. Brusca DS Hunt Down And Destroy The Jedi (V)",
    "2013 Worlds Day 2 Victor G. Brusca LS Communing",
    "2013 Worlds Day 2 Justin Carulli DS Spice Mine Operations",
    "2013 Worlds Day 2 Justin Carulli LS There Is Good In Him",
    "2013 Worlds Day 2 Jonny Chu DS Spice Mine Operations",
    "2013 Worlds Day 2 Jonny Chu LS Communing",
    "2013 World Championship",
    "Brandon Stern",
    "Victor G. Brusca",
    "Justin Carulli",
    "Jonny Chu",
]
BAD = (
    " dested ",
    "Handwritten 2010 Xerox",
    "dittos inherit",
    "as written.",
)


def fetch(titles: list[str]) -> dict:
    params = {
        "action": "query",
        "format": "json",
        "prop": "info|flagged|revisions",
        "rvprop": "content|ids",
        "rvslots": "main",
        "inprop": "url",
        "titles": "|".join(titles),
    }
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def main() -> None:
    fails = 0
    data = fetch(TITLES)
    pages = data.get("query", {}).get("pages", {})
    for pid, p in pages.items():
        title = p.get("title", "?")
        flagged = p.get("flagged") or {}
        last = p.get("lastrevid")
        stable = flagged.get("stable_revid")
        revs = p.get("revisions") or []
        text = ""
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        issues = []
        if not text:
            issues.append("EMPTY")
        if last and stable and int(last) != int(stable):
            issues.append(f"UNSTABLE last={last} stable={stable}")
        for needle in BAD:
            if needle in text:
                issues.append(f"DUMP:{needle!r}")
        want_user = "mryellow" if title.endswith("Jonny Chu LS Communing") else None
        if want_user:
            if f"'''Username:''' {want_user}" not in text:
                issues.append("MISSING_USERNAME")
        elif "'''Username:'''" in text and title.startswith("2013 Worlds"):
            issues.append("UNEXPECTED_USERNAME")
        if title == "2013 World Championship":
            for bit in (
                "Brandon Stern",
                "Victor G. Brusca",
                "Justin Carulli",
                "Jonny Chu",
                "My Lord, Is That Legal?",
                "Watch Your Step",
            ):
                if bit not in text:
                    issues.append(f"HUB_MISSING:{bit}")
        if "Starting Card:" in text and "Communing" in title and "Communing" not in text.split("Starting Card:")[1][:200]:
            issues.append("START")
        n_star = text.count("* [[") + text.count("* 2x") + text.count("* 3x") + text.count("* 4x")
        print(
            f"{'FAIL' if issues else 'OK'} {title} last={last} stable={stable} nstar~{n_star} {issues}"
        )
        if issues:
            fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
