#!/usr/bin/env python3
from __future__ import annotations
import json, urllib.parse, urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    ("2014 Alderaan Regionals Nathan DS Hunt Down And Destroy The Jedi", "Hunt Down"),
    ("2014 Alderaan Regionals Nathan LS Communing", "Communing"),
    ("2014 Alderaan Regionals", "Nathan"),
    ("Nathan", "2014 Alderaan Regionals Nathan DS Hunt Down And Destroy The Jedi"),
    ("2014 Alderaan Regionals", "Steve"),
    ("2014 Alderaan Regionals", "Gabe"),
]
DUMPS = (" dested ", "dittos inherit", "Handwritten 2010 Xerox", "Handwritten 2013 Xerox")

def parse(title):
    q = urllib.parse.urlencode({"action": "parse", "page": title, "prop": "wikitext", "format": "json"})
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))["parse"]["wikitext"]["*"]

def flagged(title):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "info|flagged", "format": "json"})
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        page = next(iter(json.loads(r.read().decode("utf-8"))["query"]["pages"].values()))
    latest = int(page.get("lastrevid") or 0)
    stable = int((page.get("flagged") or {}).get("stable_revid") or 0)
    return latest, stable

def main():
    fails = 0
    for title, needle in CHECKS:
        text = parse(title)
        latest, stable = flagged(title)
        ok_n = needle in text
        ok_f = latest == stable and latest > 0
        dump = [d for d in DUMPS if d.lower() in text.lower()]
        print(f"{title!r} needle={ok_n} latest={latest} stable={stable} equal={ok_f} dumps={dump}")
        if not ok_n or not ok_f or dump:
            fails += 1
            if not ok_n:
                print("  missing", needle)
    print("TOTAL", fails)

if __name__ == "__main__":
    main()
