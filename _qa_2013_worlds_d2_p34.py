#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Jeremy G / Giannetti / Gogolen."""
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
            "[[Jeremy G]]",
            "[[Joe Giannetti]]",
            "[[Chris Gogolen]]",
            "There Is Good In Him",
            "Spice Mine Operations",
            "Local Uprising (V)",
            "Wookiee Slaving Operation",
            "Communing",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Jeremy G LS There Is Good In Him",
        (
            "[[Jeremy G]]",
            "'''Username:''' Jedi Jer",
            "There Is Good In Him",
            "Swing-And-A-Miss",
            "Odin Nesloor",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Joe Giannetti DS Spice Mine Operations",
        (
            "[[Joe Giannetti]]",
            "'''Username:''' Sigga",
            "Spice Mine Operations",
            "Saber Squadron TIE",
            "[[File:",
        ),
        ("'''Creature'''",),
    ),
    (
        "2013 Worlds Day 2 Joe Giannetti LS Local Uprising (V)",
        (
            "[[Joe Giannetti]]",
            "'''Username:''' Sigga",
            "Local Uprising (V)",
            "Liberation (V)",
            "Hidden Fortress",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Chris Gogolen DS Wookiee Slaving Operation",
        (
            "[[Chris Gogolen]]",
            "Wookiee Slaving Operation",
            "Jango Fett, The Assassin",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Chris Gogolen LS Communing",
        (
            "[[Chris Gogolen]]",
            "Communing",
            "Master Kenobi",
            "Tatooine (Coruscant)",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    ("Jeremy G", ("2013 World Championship", "There Is Good In Him"), ()),
    ("Joe Giannetti", ("2013 World Championship", "Local Uprising"), ()),
    ("Chris Gogolen", ("2013 World Championship", "Communing"), ()),
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
