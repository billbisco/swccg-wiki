#!/usr/bin/env python3
"""Live API QA for 2014 leftover Xerox batches applied this turn."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    ("2014 Alderaan Regionals Brandon DS Wookiee Slaving Operation", "Wookiee Slaving Operation"),
    ("2014 Alderaan Regionals Brandon LS Watch Your Step (V)", "Watch Your Step"),
    ("2014 Alderaan Regionals", "Brandon"),
    ("Brandon", "2014 Alderaan Regionals Brandon DS Wookiee Slaving Operation"),
    ("2014 US Nationals Day 1 Jon Boy DS Wookiee Slaving Operation", "Wookiee Slaving Operation"),
    ("2014 US Nationals Day 1 Mike D'Ambrosio DS Superlaser Mark II", "Superlaser Mark II"),
    ("2014 US Nationals Day 1 Vince Hutchins DS Darth Vader, Dark Lord Of The Sith", "Darth Vader"),
    ("2014 US Nationals", "Jon Boy"),
    ("2014 Match Play Championship Day 1 Joe G DS Knowledge And Defense (V)", "Knowledge And Defense"),
    ("2014 Match Play Championship Day 1 Jared DS Separatist Uprising", "Separatist Uprising"),
    ("2014 Match Play Championship Day 1 Nate Louderback DS Hunt Down And Destroy The Jedi (V)", "Hunt Down"),
    ("2014 Match Play Championship Day 1 Unknown Player DS Imperial Occupation (V)", "Imperial Occupation"),
    ("2014 Match Play Championship Day 1 Casey Anis DS Hunt Down And Destroy The Jedi (V)", "Hunt Down"),
    ("2014 Match Play Championship", "Joe G"),
    ("Joe G", "2014 Match Play Championship Day 1 Joe G DS Knowledge And Defense (V)"),
    ("Unknown players", "2014 Match Play Championship"),
]
DUMPS = (" dested ", "dittos inherit", "Handwritten 2010 Xerox", "Handwritten 2013 Xerox")


def parse(title: str) -> str:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    )
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["parse"]["wikitext"]["*"]


def flagged(title: str) -> tuple[int, int]:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    page = next(iter(data["query"]["pages"].values()))
    latest = int(page.get("lastrevid") or 0)
    stable = int((page.get("flagged") or {}).get("stable_revid") or 0)
    return latest, stable


def main() -> None:
    fails = 0
    for title, needle in CHECKS:
        try:
            text = parse(title)
            latest, stable = flagged(title)
        except Exception as e:
            print(f"{title!r} ERROR {e}")
            fails += 1
            continue
        ok_n = needle in text
        ok_f = latest == stable and latest > 0
        dump = [d for d in DUMPS if d.lower() in text.lower()]
        print(
            f"{title!r} needle={ok_n} latest={latest} stable={stable} "
            f"equal={ok_f} dumps={dump}"
        )
        if not ok_n or not ok_f or dump:
            fails += 1
            if not ok_n:
                print("  missing", needle)
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
