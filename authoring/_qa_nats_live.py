#!/usr/bin/env python3
"""Live QA for 2014 US Nationals typed apply."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2014 US Nationals",
    "2014 US Nationals Day 1 Mike Tomashewski LS There Is Good In Him",
    "2014 US Nationals Day 1 Mike Tomashewski DS Separatist Uprising",
    "2014 US Nationals Day 1 Brad Eier LS You Can Either Profit By This...",
    "2014 US Nationals Day 1 Brad Eier DS A Stunning Move",
    "2014 US Nationals Day 2 Matthew Harrison-Trainor LS Republic At War",
    "2014 US Nationals Day 2 Matthew Harrison-Trainor DS Hunt Down And Destroy The Jedi (V)",
    "Mike Tomashewski",
    "List of SWCCG tournaments",
]


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
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        issues = []
        if missing:
            issues.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            issues.append(f"UNSTABLE stable={stable} latest={latest}")
        if t.endswith("There Is Good In Him"):
            if "Anakin Skywalker, Padawan Learner" not in text:
                issues.append("NO_PADAWAN")
            if "'''Interrupt'''" in text:
                block = text.split("'''Interrupt'''", 1)[1].split("'''", 1)[0]
                if "Anakin" in block:
                    issues.append("ANAKIN_UNDER_INTERRUPT")
            if "cite&#95;ref" in text or "|center|800px" in text:
                issues.append("BAD_CITE")
        if t == "2014 US Nationals":
            for name in ("Mike Tomashewski", "Brad Eier", "Matthew Harrison-Trainor"):
                if name not in text:
                    issues.append(f"HUB_MISSING_{name}")
        if t == "List of SWCCG tournaments":
            if "2014 US Nationals" not in text:
                issues.append("LIST_MISSING_NATS")
        status = "OK" if not issues else "FAIL " + ",".join(issues)
        print(status, t, "id", pid, "stable", stable, "len", len(text))
    print("DONE")


if __name__ == "__main__":
    main()
