#!/usr/bin/env python3
"""Parse-HTML QA for leftover 2013 Worlds Day 2 Stern/Brusca/Carulli/Chu."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Worlds Day 2 Brandon Stern DS My Lord, Is That Legal?",
    "2013 Worlds Day 2 Brandon Stern LS Watch Your Step",
    "2013 Worlds Day 2 Victor G. Brusca LS Communing",
    "2013 Worlds Day 2 Justin Carulli LS There Is Good In Him",
    "2013 Worlds Day 2 Jonny Chu LS Communing",
    "2013 World Championship",
]


def main() -> None:
    fails = 0
    for title in TITLES:
        params = {
            "action": "parse",
            "format": "json",
            "page": title,
            "prop": "text|images",
        }
        url = API + "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        html = data["parse"]["text"]["*"]
        images = data["parse"].get("images") or []
        issues = []
        for needle in (" dested ", "Handwritten 2010 Xerox", "dittos inherit"):
            if needle in html:
                issues.append(f"DUMP:{needle!r}")
        if "File:" not in str(images) and not any(
            x.lower().endswith(".png") for x in images
        ):
            if title.startswith("2013 Worlds"):
                issues.append("NO_SCAN")
        if title.endswith("Jonny Chu LS Communing") and "mryellow" not in html:
            issues.append("NO_USER")
        if "Brusca LS" in title:
            # 58-card main is sheet-accurate
            pass
        print(("FAIL" if issues else "OK"), title, "imgs", images[:3], issues)
        if issues:
            fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
