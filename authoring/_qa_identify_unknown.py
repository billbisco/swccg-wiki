#!/usr/bin/env python3
"""Live QA: facing-page dests + informed-identity merges."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2014 Worlds Day 2 Vinayum Bari LS Yavin 4",
        ["Vinayum Bari", "Yavin 4: Massassi Throne Room", "played by"],
    ),
    (
        "2014 Worlds Day 2 unnamed LS Yavin 4",
        ["Vinayum Bari"],
    ),
    (
        "2014 Worlds Day 2 Mike Stirling LS Hoth",
        ["Mike Stirling", "Hoth: Main Power Generators"],
    ),
    (
        "2014 Worlds Day 2 unnamed LS Hoth",
        ["Mike Stirling"],
    ),
    ("Unknown players", ["Vinayum Bari", "Brian Terwilliger", "Matt Sokol", "Separatist Uprising"]),
    ("Unknown Player", ["Separatist Uprising"]),
    ("2014 World Championship", ["Vinayum Bari LS Yavin 4", "Mike Stirling LS Hoth"]),
    ("BTwigg", ["Brian Terwilliger"]),
    ("Sokol", ["Matt Sokol"]),
    ("2013 Match Play Championship", ["Brian Terwilliger", "Matt Sokol", "Steve Harpster"]),
    ("Brian Terwilliger", ["2013 Match Play Championship"]),
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
        "missing": page.get("missing") is not None,
    }


def main() -> None:
    fail = 0
    for title, needles in CHECKS:
        row = parse(title)
        mark = "OK" if row["ok"] and not row["missing"] else "FAIL"
        if mark == "FAIL":
            fail += 1
        print(
            f"{mark} {title} id={row['pageid']} latest={row['latest']} stable={row['stable']}"
        )
        html = row["html"]
        for needle in needles:
            if needle not in html:
                print("  MISS", needle)
                fail += 1
        if title == "Unknown Player" and "Yavin 4" in html and "Vinayum" not in html:
            # unnamed Yavin 4 should have left this stub
            if "unnamed LS Yavin 4" in html:
                print("  STALE unnamed Yavin 4 still on Unknown Player")
                fail += 1
        if title == "Unknown players" and "Possible pair with" in html:
            print("  STALE possible-pair wording")
            fail += 1
    print("TOTAL", fail)


if __name__ == "__main__":
    main()
