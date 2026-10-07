#!/usr/bin/env python3
"""Live QA: Unknown Player dest + Unknown players index."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "Unknown players",
    "Unknown Player",
    "Blank Player",
    "unnamed",
    "2014 Worlds Day 2 unnamed LS It Is The Future You See",
    "2014 Worlds Day 2 unnamed DS Separatist Uprising",
    "2014 Worlds Day 2 unnamed LS Hoth",
    "2014 Worlds Day 2 unnamed LS Yavin 4",
    "2014 World Championship",
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "info|flagged|revisions",
            "rvprop": "ids",
            "rvlimit": 1,
            "inprop": "url",
        }
    )
    with urllib.request.urlopen(API + "?" + q, timeout=60) as r:
        data = json.load(r)
    page = next(iter(data["query"]["pages"].values()))
    html_q = urllib.parse.urlencode(
        {"action": "parse", "format": "json", "page": title, "prop": "text|revid"}
    )
    with urllib.request.urlopen(API + "?" + html_q, timeout=60) as r:
        parsed = json.load(r)["parse"]
    html = parsed["text"]["*"]
    flagged = page.get("flagged") or {}
    latest = page.get("lastrevid")
    stable = flagged.get("stable_revid")
    return {
        "title": title,
        "pageid": page.get("pageid"),
        "latest": latest,
        "stable": stable,
        "ok": latest == stable and latest is not None,
        "html": html,
        "revid": parsed.get("revid"),
    }


def main() -> None:
    fail = 0
    for title in TITLES:
        row = parse(title)
        mark = "OK" if row["ok"] else "FAIL"
        if not row["ok"]:
            fail += 1
        print(
            f"{mark} {title} id={row['pageid']} latest={row['latest']} stable={row['stable']}"
        )
        html = row["html"]
        if title == "Unknown players":
            for needle in (
                "Unknown Player",
                "Separatist Uprising",
                "Aaron Kia",
                "Same as Yesterday",
            ):
                if needle not in html:
                    print("  MISS", needle)
                    fail += 1
        if title == "Unknown Player":
            if "Separatist Uprising" not in html:
                print("  MISS stub pair")
                fail += 1
        if title == "Blank Player":
            if "redirectText" not in html and "Unknown Player" not in html:
                print("  MISS redirect")
                fail += 1
        if title.startswith("2014 Worlds Day 2 unnamed"):
            if "Unknown Player" not in html:
                print("  MISS Unknown Player in lead")
                fail += 1
            if " dested " in html or "Handwritten 2010 Xerox" in html:
                print("  DEST DUMP")
                fail += 1
        if title == "2014 World Championship":
            if "Unknown Player" not in html:
                print("  MISS hub Unknown Player")
                fail += 1
    print("QA TOTAL", fail)


if __name__ == "__main__":
    main()
