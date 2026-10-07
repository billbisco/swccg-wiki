#!/usr/bin/env python3
"""Live QA for 2014 EC hub + winner updates."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2014 European Championship",
    "2014 US Nationals",
    "2014 Match Play Championship",
    "2014 Texas Mini Worlds",
    "List of SWCCG tournaments",
    "European Championships",
    "Casper Jørgensen",
    "Matthew Harrison-Trainor",
    "Kevin Shannon",
    "Greg Shaw",
]


def api(**kw):
    q = urllib.parse.urlencode(kw)
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
    for t in TITLES:
        data = api(
            action="query",
            titles=t,
            prop="info|flagged|revisions",
            rvprop="ids|size",
            rvlimit="1",
            format="json",
        )
        pages = data["query"]["pages"]
        p = next(iter(pages.values()))
        pid = p.get("pageid")
        missing = "missing" in p
        flagged = p.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = p.get("lastrevid")
        size = (p.get("revisions") or [{}])[0].get("size")
        parse = api(action="parse", page=t, prop="wikitext|text", format="json")
        wt = parse["parse"]["wikitext"]["*"]
        html = parse["parse"]["text"]["*"]
        issues = []
        if missing:
            issues.append("MISSING")
        if stable != latest:
            issues.append(f"stable!=latest {stable} {latest}")
        checks = {
            "2014 European Championship": ["Casper Jørgensen", "Legacy Open", "12–14 September"],
            "2014 US Nationals": ["Matthew Harrison-Trainor", "Winner"],
            "2014 Match Play Championship": ["Kevin Shannon", "Winner"],
            "2014 Texas Mini Worlds": ["Greg Shaw", "Winner"],
            "List of SWCCG tournaments": [
                "2014 European Championship",
                "Casper Jørgensen",
                "Matthew Harrison-Trainor",
                "Kevin Shannon",
            ],
            "European Championships": ["[[2014 European Championship]]"],
            "Casper Jørgensen": ["2014 European Championship"],
            "Matthew Harrison-Trainor": ["2014 US Nationals"],
            "Kevin Shannon": ["2014 Match Play Championship"],
            "Greg Shaw": ["2014 Texas Mini Worlds"],
        }
        for needle in checks.get(t, []):
            if needle not in wt:
                issues.append(f"missing {needle!r}")
        if t == "Kevin Shannon" and size and size < 2000:
            issues.append(f"SHORT_PAGE size={size}")
        print(
            "OK" if not issues else "ISSUE",
            t,
            "id",
            pid,
            "stable",
            stable,
            "size",
            size,
            *issues,
        )
        if t == "Kevin Shannon":
            print("  shannon rows", wt.count("|-"))
    print("DONE")


if __name__ == "__main__":
    main()
