#!/usr/bin/env python3
"""Live QA: 2013 Worlds leftover Xerox Aaron + Day 2 Alperstein/Arlandson/Bali/Banger/Baroni/Birgander."""
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
            "[[Aaron Kia]]",
            "[[Charlie Arlandson]]",
            "[[Barry Alperstein]]",
            "[[Amar Banger]]",
            "[[Steve Baroni]]",
            "[[Pär Birgander]]",
            "Walker Garrison",
            "Sai'torr Kal Fas (V)",
            "Wookiee Slaving Operation",
            "Quiet Mining Colony",
            "Infiltration",
            "Communing",
            "Mind What You Have Learned (V)",
        ),
        ("[[Charles Arlandson]]",),
    ),
    (
        "2013 Worlds Day 1 Aaron Kia LS Sai'torr Kal Fas (V)",
        ("[[Aaron Kia]]", "Name as written on the Day 1 sheet.", "[[File:"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 1 Aaron Kia DS Walker Garrison",
        ("[[Aaron Kia]]", "Walker Garrison", "[[File:"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Barry Alperstein LS You Can Either Profit By This...",
        ("[[Barry Alperstein]]", "'''Username:''' MrFromMars", "[[File:"),
        (),
    ),
    (
        "2013 Worlds Day 2 Barry Alperstein DS Wookiee Slaving Operation",
        ("[[Barry Alperstein]]", "'''Username:''' MrFromMars"),
        (),
    ),
    (
        "2013 Worlds Day 2 Charlie Arlandson LS Quiet Mining Colony",
        ("[[Charlie Arlandson]]", "'''Username:''' Brazen", "Quiet Mining Colony"),
        ("[[Charles Arlandson]]",),
    ),
    (
        "2013 Worlds Day 2 Charlie Arlandson DS No Money, No Parts, No Deal!",
        ("[[Charlie Arlandson]]", "'''Username:''' Brazen"),
        ("[[Charles Arlandson]]",),
    ),
    (
        "2013 Worlds Day 2 Vikram Bali LS Anger, Fear, Aggression (V)",
        ("[[Vikram Bali]]", "'''Username:''' DVD ROTS"),
        (),
    ),
    (
        "2013 Worlds Day 2 Vikram Bali DS Set Your Course For Alderaan",
        ("[[Vikram Bali]]", "'''Username:''' DVD ROTS"),
        (),
    ),
    (
        "2013 Worlds Day 2 Amar Banger LS Infiltration",
        ("[[Amar Banger]]", "Infiltration / Unlikely Allies", "[[File:"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Amar Banger DS Hunt Down And Destroy The Jedi",
        ("[[Amar Banger]]", "The Circle Is Now Complete"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Steve Baroni LS Mind What You Have Learned (V)",
        ("[[Steve Baroni]]", "Mind What You Have Learned", "Great Warrior"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Steve Baroni DS Hunt Down And Destroy The Jedi (V)",
        ("[[Steve Baroni]]", "Hunt Down And Destroy The Jedi"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Pär Birgander LS Communing",
        ("[[Pär Birgander]]", "'''Username:''' pbira", "Communing"),
        (),
    ),
    (
        "2013 Worlds Day 2 Pär Birgander DS Imperial Entanglements",
        ("[[Pär Birgander]]", "'''Username:''' pbira", "Imperial Entanglements"),
        (),
    ),
    ("Aaron Kia", ("2013 World Championship",), ()),
    ("Charlie Arlandson", ("2013 World Championship", "Quiet Mining Colony"), ()),
    ("Amar Banger", ("2013 World Championship",), ()),
    ("Steve Baroni", ("2013 World Championship",), ()),
    ("Pär Birgander", ("2013 World Championship",), ()),
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
