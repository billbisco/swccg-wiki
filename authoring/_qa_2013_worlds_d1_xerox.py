#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 1 Xerox Cellucci DS + Gardner + Littauer + Way."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Stephen Cellucci]]",
            "[[Jeremy Gardner]]",
            "[[Ross Littauer]]",
            "[[Nathan Way]]",
            "Endor Operations",
            "Hidden Base (V)",
            "Imperial Entanglements",
            "Infiltration",
            "Hunt Down And Destroy The Jedi (V)",
            "Mind What You Have Learned (V)",
            "Contract Killers",
        ),
        (),
    ),
    (
        "2013 Worlds Day 1 Stephen Cellucci DS Endor Operations",
        ("[[Stephen Cellucci]]", "'''Username:''' NoLimit", "[[File:"),
        (),
    ),
    (
        "2013 Worlds Day 1 Jeremy Gardner LS Hidden Base (V)",
        ("[[Jeremy Gardner]]", "[[File:"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 1 Jeremy Gardner DS Imperial Entanglements",
        ("[[Jeremy Gardner]]", "Imperial Entanglements"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 1 Ross Littauer LS Infiltration",
        ("[[Ross Littauer]]", "Infiltration / Unlikely Allies"),
        ("'''Username:'''", "Diplomatic Mission"),
    ),
    (
        "2013 Worlds Day 1 Ross Littauer DS Hunt Down And Destroy The Jedi (V)",
        ("[[Ross Littauer]]", "Hunt Down And Destroy The Jedi"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 1 Nathan Way LS Mind What You Have Learned (V)",
        ("[[Nathan Way]]", "Mind What You Have Learned"),
        ("[[Nathan Wall]]", "'''Username:'''"),
    ),
    (
        "2013 Worlds Day 1 Nathan Way DS Contract Killers",
        ("[[Nathan Way]]", "Contract Killers"),
        ("[[Nathan Wall]]", "'''Username:'''"),
    ),
    ("Jeremy Gardner", ("2013 World Championship",), ()),
    ("Ross Littauer", ("2013 World Championship",), ()),
    ("Nathan Way", ("2013 World Championship",), ()),
    ("Stephen Cellucci", ("2013 World Championship",), ()),
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(title: str) -> tuple[dict, str]:
    params = {
        "action": "query",
        "format": "json",
        "prop": "info|flagged|revisions",
        "rvprop": "ids|content",
        "rvslots": "main",
        "titles": title,
        "redirects": "1",
    }
    data = api(params)
    page = next(iter(data["query"]["pages"].values()))
    text = ""
    revs = page.get("revisions") or []
    if revs:
        text = revs[0].get("slots", {}).get("main", {}).get("*", "")
    return page, text


def main() -> int:
    n = 0
    for title, want, ban in CHECKS:
        page, text = fetch(title)
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        missing = [w for w in want if w not in text]
        dumped = [b for b in ban if b in text]
        dest = [d for d in DUMP if d in text]
        ok = (not missing) and (not dumped) and (not dest) and stable == latest
        if not ok:
            n += 1
            print("FAIL", title)
            if missing:
                print("  missing", missing)
            if dumped:
                print("  banned", dumped)
            if dest:
                print("  dest-dump", dest)
            if stable != latest:
                print("  flagged", stable, "latest", latest)
        else:
            print("OK", title, "oldid", latest)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
