#!/usr/bin/env python3
"""Live QA for 2013 Texas Mini Worlds typed Reisch apply."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Texas Mini Worlds",
    "2013 Texas Mini Worlds Day 1 Nick Reisch DS Hunt Down And Destroy The Jedi (V)",
    "2013 Texas Mini Worlds Day 1 Nick Reisch LS The Hyperdrive Generator's Gone",
    "2013 Texas Mini Worlds Day 1 Mike Richards DS Kessel: Spice Mines Administration Office",
    "2013 Texas Mini Worlds Day 1 Mike Richards LS Quiet Mining Colony",
    "2013 Texas Mini Worlds Day 1 Evan Kirkpatrick DS Set Your Course For Alderaan",
    "2013 Texas Mini Worlds Day 1 Evan Kirkpatrick LS Anger, Fear, Aggression (V)",
    "2013 Texas Mini Worlds Day 1 James Barnes DS Hunt Down And Destroy The Jedi (V)",
    "2013 Texas Mini Worlds Day 1 James Barnes LS The Hyperdrive Generator's Gone",
    "Nick Reisch",
    "Aaron Nelson",
    "Robbie Hendon",
    "Greg Shaw",
    "Mike Richards",
    "Evan Kirkpatrick",
    "James Barnes",
    "List of SWCCG tournaments",
]
SHORT = 2000
STUBS = {
    "Nick Reisch",
    "Aaron Nelson",
    "Robbie Hendon",
    "Greg Shaw",
    "Mike Richards",
    "Evan Kirkpatrick",
    "James Barnes",
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
        if t == "2013 Texas Mini Worlds":
            for name in (
                "Nick Reisch",
                "Aaron Nelson",
                "Robbie Hendon",
                "Greg Shaw",
                "Mike Richards",
                "Evan Kirkpatrick",
                "James Barnes",
                "Legacy Open",
            ):
                if name not in text:
                    issues.append(f"HUB_MISSING_{name}")
            if "[[Open]]" in text and "[[Legacy Open]]" not in text:
                issues.append("WRONG_FORMAT_OPEN")
        if t.startswith("2013 Texas Mini Worlds Day 1") and t != "2013 Texas Mini Worlds":
            if "|center|800px" in text:
                issues.append("BAD_CITE")
            if "[[Category:2013]]" not in text:
                issues.append("NO_CAT_2013")
        if t.endswith("Mike Richards LS Quiet Mining Colony"):
            if "p13 Mike Richards LS.png" not in text:
                issues.append("MISSING_EXTRA_SCAN")
        if t == "List of SWCCG tournaments":
            if "2013 Texas Mini Worlds" not in text:
                issues.append("LIST_MISSING_TMW")
        status = "OK" if not issues else "FAIL " + ",".join(issues)
        print(status, t, "id", pid, "stable", stable, "len", len(text), "size", length)
    print("DONE")


if __name__ == "__main__":
    main()
