#!/usr/bin/env python3
"""Live QA for 2014 Alderaan Regionals dest."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2014 Alderaan Regionals",
    "2014 Alderaan Regionals Ganden Yanaga LS We Have A Plan",
    "2014 Alderaan Regionals Ganden Yanaga DS Imperial Entanglements",
    "2014 Alderaan Regionals Anthony Massung LS Republic At War",
    "2014 Alderaan Regionals Anthony Massung DS Separatist Uprising",
    "2014 Alderaan Regionals Peter Huderich LS Quiet Mining Colony",
    "2014 Alderaan Regionals Peter Huderich DS Court Of The Vile Gangster",
    "2014 Alderaan Regionals Roy McCarthy LS Quiet Mining Colony",
    "2014 Alderaan Regionals Roy McCarthy DS A Stunning Move",
    "Ganden Yanaga",
    "Anthony Massung",
    "Peter Huderich",
    "Roy McCarthy",
    "List of SWCCG tournaments",
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
        p = next(iter(data["query"]["pages"].values()))
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
        if t == "2014 Alderaan Regionals":
            for needle in (
                "Ganden Yanaga",
                "Anthony Massung",
                "Peter Huderich",
                "Roy McCarthy",
                "We Have A Plan",
                "Imperial Entanglements",
                "Republic At War",
                "Separatist Uprising",
                "Quiet Mining Colony",
                "Court Of The Vile Gangster",
                "A Stunning Move",
                "Legacy Open",
            ):
                if needle not in wt:
                    issues.append(f"missing {needle!r}")
        if t.startswith("2014 Alderaan Regionals ") and "File:" not in wt:
            issues.append("no scan File")
        if "cite" not in html and t.startswith("2014 Alderaan Regionals "):
            issues.append("no cite in html")
        print(
            ("OK" if not issues else "ISSUE"),
            t,
            "id",
            pid,
            "stable",
            stable,
            "size",
            size,
            *issues,
        )
    print("DONE")


if __name__ == "__main__":
    main()
