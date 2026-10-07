#!/usr/bin/env python3
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2014 Texas Mini Worlds",
    "2014 Texas Mini Worlds Day 2 Nick Reisch LS You Can Either Profit By This...",
    "2014 Texas Mini Worlds Day 2 Nick Reisch DS Ralltiir Operations",
    "Nick Reisch",
    "List of SWCCG tournaments",
    "2014 US Nationals",
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
        if t == "List of SWCCG tournaments":
            if "2014 Texas Mini Worlds" not in text:
                issues.append("LIST_MISSING_TMW")
            if "2014 US Nationals" not in text:
                issues.append("LIST_MISSING_NATS")
        if "Nick Reisch LS" in t:
            if "'''Unknown'''" in text:
                issues.append("UNKNOWN_TYPE")
            if "Sai'torr Kal Fas" not in text.split("'''Interrupt'''")[0]:
                issues.append("SAITORR_NOT_CHARACTER")
        if "Nick Reisch DS" in t:
            if "'''Unknown'''" in text:
                issues.append("UNKNOWN_TYPE")
        status = "OK" if not issues else "FAIL " + ",".join(issues)
        print(status, t, "id", page.get("pageid"), "stable", stable, "len", len(text))
    print("DONE")


if __name__ == "__main__":
    main()
