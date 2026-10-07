#!/usr/bin/env python3
"""Live QA for 2013 SoCal Grand Prix hub + typed dest."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 SoCal Grand Prix",
    "2013 SoCal Grand Prix Day 1 Phil Aasen LS It Is The Future You See (V)",
    "2013 SoCal Grand Prix Day 1 Phil Aasen DS Wookiee Slaving Operation",
    "2013 SoCal Grand Prix Day 1 John Anderson LS Infiltration",
    "2013 SoCal Grand Prix Day 1 John Anderson DS Hunt Down And Destroy The Jedi",
    "2013 SoCal Grand Prix Day 1 Clayton Atkin LS Communing",
    "2013 SoCal Grand Prix Day 1 Clayton Atkin DS Hunt Down And Destroy The Jedi (V)",
    "2013 SoCal Grand Prix Day 1 Ganden Yanaga LS Quiet Mining Colony",
    "2013 SoCal Grand Prix Day 1 Ganden Yanaga DS Endor Operations",
    "2013 SoCal Grand Prix Day 1 Brian Herold LS There Is Good In Him",
    "2013 SoCal Grand Prix Day 1 Brian Herold DS Wookiee Slaving Operation",
    "2013 SoCal Grand Prix Day 1 Anthony Massung LS There Is Good In Him",
    "2013 SoCal Grand Prix Day 1 Anthony Massung DS Set Your Course For Alderaan",
    "2013 SoCal Grand Prix Day 1 Kevin Shannon LS Plead My Case To The Senate",
    "2013 SoCal Grand Prix Day 1 Kevin Shannon DS Imperial Entanglements",
    "2013 SoCal Grand Prix Day 1 Greg Shaw LS Watch Your Step (V)",
    "2013 SoCal Grand Prix Day 1 Greg Shaw DS Carbon Chamber Testing",
    "2013 SoCal Grand Prix Day 1 Matthew Harrison-Trainor LS Watch Your Step (V)",
    "2013 SoCal Grand Prix Day 1 Matthew Harrison-Trainor DS Imperial Occupation (V)",
    "2013 SoCal Grand Prix Day 1 Joe Olson LS We'll Handle This",
    "2013 SoCal Grand Prix Day 1 Joe Olson DS My Lord, Is That Legal",
    "2013 SoCal Grand Prix Day 2 Matthew Harrison-Trainor LS Watch Your Step (V)",
    "2013 SoCal Grand Prix Day 2 Matthew Harrison-Trainor DS Hunt Down And Destroy The Jedi (V)",
    "2013 SoCal Grand Prix Day 2 Clayton Atkin LS Communing",
    "2013 SoCal Grand Prix Day 2 Clayton Atkin DS Hunt Down And Destroy The Jedi (V)",
    "2013 SoCal Grand Prix Day 2 Kevin Shannon LS We'll Handle This",
    "2013 SoCal Grand Prix Day 2 Kevin Shannon DS Carbon Chamber Testing",
    "2013 SoCal Grand Prix Day 1 Steve Skilton LS It Is The Future You See (V)",
    "2013 SoCal Grand Prix Day 1 Steve Skilton DS Hunt Down And Destroy The Jedi",
    "2013 SoCal Grand Prix Day 1 Reid Smith LS There Is Good In Him",
    "2013 SoCal Grand Prix Day 1 Reid Smith DS Kessel",
    "2013 SoCal Grand Prix Day 2 Reid Smith LS It Is The Future You See (V)",
    "2013 SoCal Grand Prix Day 2 Reid Smith DS A Stunning Move",
    "2013 SoCal Grand Prix Day 1 Matt Thornton LS Watch Your Step (V)",
    "2013 SoCal Grand Prix Day 1 Matt Thornton DS My Lord, Is That Legal",
    "Steve Skilton",
    "Reid Smith",
    "John Anderson",
    "Matthew Harrison-Trainor",
    "Joe Olson",
    "Phil Aasen",
    "Clayton Atkin",
    "Ganden Yanaga",
    "Brian Herold",
    "Anthony Massung",
    "Kevin Shannon",
    "Greg Shaw",
    "Matt Thornton",
    "List of SWCCG tournaments",
]
SHORT = 2000
STUBS = {
    "Phil Aasen",
    "Clayton Atkin",
    "Ganden Yanaga",
    "Brian Herold",
    "Anthony Massung",
    "Matt Thornton",
    "Steve Skilton",
}


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
    issues_all = []
    for t in TITLES:
        data = api(
            {
                "action": "query",
                "format": "json",
                "prop": "info|flagged|revisions",
                "rvprop": "ids|content",
                "rvslots": "main",
                "titles": t,
            }
        )
        page = next(iter(data["query"]["pages"].values()))
        pid = page.get("pageid")
        missing = "missing" in page
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        length = page.get("length") or 0
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        issues = []
        if missing:
            issues.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            issues.append(f"UNSTABLE stable={stable} latest={latest}")
        if (
            length
            and int(length) < SHORT
            and t != "List of SWCCG tournaments"
            and t not in STUBS
        ):
            issues.append(f"SHORT_PAGE size={length}")
        if t == "2013 SoCal Grand Prix":
            if "John Anderson" not in text:
                issues.append("HUB_MISSING_ANDERSON")
            if "Matthew Harrison-Trainor" not in text:
                issues.append("HUB_MISSING_MHT")
            if "Joe Olson" not in text:
                issues.append("HUB_MISSING_OLSON")
            if "Ganden Yanaga" not in text:
                issues.append("HUB_MISSING_YANAGA")
            if "Wiki column" in text or "!! Wiki" in text:
                issues.append("HAS_WIKI_COLUMN")
            if "[[Open]]" in text and "[[Legacy Open]]" not in text:
                issues.append("WRONG_FORMAT")
        if t == "List of SWCCG tournaments" and "2013 SoCal Grand Prix" not in text:
            issues.append("LIST_MISSING_SOCAL")
        if t.startswith("2013 SoCal Grand Prix Day") and "File:" not in text:
            issues.append("NO_SCAN")
        status = "OK" if not issues else "FAIL " + "; ".join(issues)
        print(f"{status}\t{t}\tid={pid} stable={stable} size={length}")
        if issues:
            issues_all.append(t)
    print("issues", len(issues_all))
    if issues_all:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
