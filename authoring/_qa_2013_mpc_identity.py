#!/usr/bin/env python3
"""Live QA: 2013 MPC Schwartz/Steve S. Username identity dests."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
    "Name as written on the Day 1 sheet",
)
CHECKS = [
    (
        "2013 Match Play Championship",
        (
            "[[Matt Schmaltz]]",
            "[[Steve Skilton]]",
        ),
        ("| [[Schwartz]] ||", "| [[Steve S.]] ||"),
    ),
    (
        "2013 Match Play Championship Day 1 Matt Schmaltz LS Hidden Base",
        ("[[Matt Schmaltz]]", "'''Username:''' dashmudtz", "[[File:"),
        ("[[Schwartz]]",),
    ),
    (
        "2013 Match Play Championship Day 1 Matt Schmaltz DS Imperial Occupation (V)",
        ("[[Matt Schmaltz]]", "'''Username:''' dashmudtz"),
        ("[[Schwartz]]",),
    ),
    (
        "2013 Match Play Championship Day 1 Steve Skilton LS We'll Handle This",
        ("[[Steve Skilton]]", "'''Username:''' stevetotheizzo"),
        ("[[Steve S.]]",),
    ),
    (
        "2013 Match Play Championship Day 1 Steve Skilton DS Contract Killers",
        ("[[Steve Skilton]]", "'''Username:''' stevetotheizzo"),
        ("[[Steve S.]]",),
    ),
    ("Matt Schmaltz", ("2013 Match Play Championship",), ()),
    ("Steve Skilton", ("2013 Match Play Championship",), ()),
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(title: str, follow: bool = True) -> tuple[dict, str]:
    params = {
        "action": "query",
        "format": "json",
        "prop": "info|flagged|revisions",
        "rvprop": "ids|content",
        "rvslots": "main",
        "titles": title,
    }
    if follow:
        params["redirects"] = "1"
    data = api(params)
    page = next(iter(data["query"]["pages"].values()))
    text = ""
    revs = page.get("revisions") or []
    if revs:
        text = revs[0].get("slots", {}).get("main", {}).get("*", "")
    return page, text


def main() -> int:
    n = 0
    extras = [
        ("2013 Match Play Championship Day 1 Schwartz LS Hidden Base", "Matt Schmaltz"),
        ("2013 Match Play Championship Day 1 Schwartz DS Imperial Occupation (V)", "Matt Schmaltz"),
        ("2013 Match Play Championship Day 1 Steve S. LS We'll Handle This", "Steve Skilton"),
        ("2013 Match Play Championship Day 1 Steve S. DS Contract Killers", "Steve Skilton"),
        ("Schwartz", "Matt Schmaltz"),
        ("Steve S.", "Steve Skilton"),
    ]
    for t, want, ban in CHECKS:
        page, text = fetch(t)
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        for marker in DUMP:
            if marker in text:
                got.append(f"DUMP_{marker.strip()[:24]}")
        for needle in want:
            if needle not in text:
                got.append(f"MISSING_{needle[:40]}")
        for needle in ban:
            if needle in text:
                got.append(f"BANNED_{needle[:40]}")
        if got:
            n += 1
            print("FAIL", t, got)
        else:
            print("OK", t)
    for t, dest in extras:
        page, text = fetch(t, follow=False)
        got = []
        if "missing" in page:
            got.append("MISSING")
        if not text.lstrip().startswith("#REDIRECT"):
            got.append("NOT_REDIRECT")
        elif dest not in text:
            got.append(f"REDIR_DEST {text[:80]!r}")
        if got:
            n += 1
            print("FAIL", t, got)
        else:
            print("OK redir", t)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
