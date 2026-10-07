#!/usr/bin/env python3
"""Live QA for 2013 World Championship first-slice apply."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 World Championship",
    "2013 Worlds Day 1 Stephen Cellucci LS Plead My Case To The Senate",
    "2013 Worlds Day 1 Drew Powers LS Rescue The Princess",
    "2013 Worlds Day 1 Drew Powers DS Agents Of Black Sun",
    "2013 Worlds Day 2 Seth Acree DS Endor Operations",
    "2013 Worlds Day 2 Seth Acree LS Center Of Tyranny",
    "2013 Worlds Day 2 John Anderson DS Contract Killers",
    "2013 Worlds Day 2 John Anderson LS Infiltration",
    "2013 Worlds Day 2 Casey Anis DS Wookiee Slaving Operation",
    "2013 Worlds Day 2 Casey Anis LS Anger, Fear, Aggression (V)",
    "2013 Worlds Day 3 Vikram Bali LS Anger, Fear, Aggression (V)",
    "Stephen Cellucci",
    "Drew Powers",
    "Seth Acree",
    "John Anderson",
    "Casey Anis",
    "Vikram Bali",
    "List of SWCCG tournaments",
]
SHORT = 2000
STUBS = {
    "Stephen Cellucci",
    "Drew Powers",
    "Seth Acree",
    "John Anderson",
    "Casey Anis",
    "Vikram Bali",
}


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
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
        if t == "2013 World Championship":
            for name in (
                "Stephen Cellucci",
                "Jeremy Gardner",
                "Ross Littauer",
                "Drew Powers",
                "Nathan Way",
                "Steve Baroni",
                "Vikram Bali",
                "Jonny Chu",
                "Kevin Shannon",
                "Reid Smith",
                "Emil Wallin",
                "John Anderson",
                "Casey Anis",
                "Seth Acree",
                "Legacy Open",
            ):
                if name not in text:
                    issues.append(f"HUB_MISSING_{name}")
            if "[[Open]]" in text and "[[Legacy Open]]" not in text:
                issues.append("WRONG_FORMAT_OPEN")
        if t.startswith("2013 Worlds Day 1 Stephen Cellucci"):
            if "Plead My Case To The Senate" not in text:
                issues.append("NO_OBJECTIVE")
            if "|center|800px" in text:
                issues.append("BAD_CITE")
            if "[[Category:2013]]" not in text:
                issues.append("NO_CAT_2013")
            if "[[Category:2014]]" in text:
                issues.append("WRONG_CAT_2014")
        if t == "List of SWCCG tournaments":
            if "== 2013 ==" not in text:
                issues.append("LIST_MISSING_2013_HEADING")
            if "2013 World Championship" not in text:
                issues.append("LIST_MISSING_WORLDS")
        status = "OK" if not issues else "FAIL " + ",".join(issues)
        print(status, t, "id", pid, "stable", stable, "len", len(text), "size", length)
    print("DONE")


if __name__ == "__main__":
    main()
