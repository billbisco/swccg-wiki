#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 Nick Reisch p78-p79."""
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
            "[[Nick Reisch]]",
            "Hunt Down And Destroy The Jedi (V)",
            "Quiet Mining Colony",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Nick Reisch LS Quiet Mining Colony",
        (
            "[[Nick Reisch]]",
            "[[Quiet Mining Colony / Independent Operation]]",
            "[[Punch It!]]",
            "[[Lady Luck]]",
            "[[Wise Advice]]",
            "[[There is Another|There Is Another]]",
            "[[Chasm (V)]]",
            "[[File:2013 Worlds Day 2 p78 Nick Reisch LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Nick Reisch DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Nick Reisch]]",
            "[[Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)]]",
            "[[I Have You Now]]",
            "[[Jango Fett, The Assassin]]",
            "[[Rogue Shadow]]",
            "[[Weapon Levitation]]",
            "[[Surprise Strike]]",
            "[[Death Star Sentry (V)]]",
            "[[File:2013 Worlds Day 2 p79 Nick Reisch DS.png|800px]]",
        ),
        ("'''Username:'''", "Galen's Fighter", "Blow Parried", "Ice-Heart"),
    ),
    (
        "Nick Reisch",
        (
            "2013 World Championship",
            "Hunt Down And Destroy The Jedi (V)",
            "Quiet Mining Colony",
            "2013 Texas Mini Worlds",
            "2013 Match Play Championship",
        ),
        (),
    ),
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
