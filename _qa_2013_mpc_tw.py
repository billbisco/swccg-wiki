#!/usr/bin/env python3
"""Live QA for 2013 MPC Tomashewski + Westergard Xerox leftover."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 Mike Tomashewski LS Yavin 4: Massassi Throne Room",
    "2013 Match Play Championship Day 1 Mike Tomashewski DS Invasion",
    "2013 Match Play Championship Day 1 Chris Westergard LS Watch Your Step",
    "2013 Match Play Championship Day 1 Chris Westergard DS Wookiee Slaving Operation",
    "2013 Match Play Championship",
    "Mike Tomashewski",
    "Chris Westergard",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def section(text: str, heading: str) -> str:
    m = re.search(
        r"'''" + re.escape(heading) + r"'''(.*?)(?:'''|\|})",
        text,
        re.S,
    )
    return m.group(1) if m else ""


def main() -> int:
    n = 0
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
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        if t.endswith("Massassi Throne Room"):
            effect = section(text, "Effect")
            interrupt = section(text, "Interrupt")
            if "Anger, Fear, Aggression (V)" not in effect:
                got.append("AFA_V_NOT_EFFECT")
            if "Anger, Fear, Aggression (V)" in interrupt:
                got.append("AFA_V_IN_INTERRUPT")
            if "[[File:2013 Match Play Championship p99 Mike Tomashewski LS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t.endswith("Tomashewski DS Invasion"):
            if "Invasion / In Complete Control" not in text:
                got.append("MISSING_INVASION_DUAL")
            if "Master, Destroyers!" not in text:
                got.append("MISSING_MASTER_DESTROYERS")
            if "[[File:2013 Match Play Championship p100 Mike Tomashewski DS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t.endswith("Westergard LS Watch Your Step"):
            if "Watch Your Step / This Place Can Be A Little Rough" not in text:
                got.append("MISSING_WYS_DUAL")
            if "(V) / This Place Can Be A Little Rough (V)" in text.split("== Scan ==")[0]:
                got.append("WYS_SHOULD_BE_DECIPHER")
            interrupt = section(text, "Interrupt")
            if "Anger, Fear, Aggression (V)" in interrupt or (
                "Anger, Fear, Aggression (V)" in section(text, "Effect")
            ):
                got.append("AFA_SHOULD_BE_DECIPHER")
            if "[[File:2013 Match Play Championship p105 Chris Westergard LS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t.endswith("Wookiee Slaving Operation") and "Westergard" in t:
            if "Wookiee Slaving Operation / Indentured To The Empire" not in text:
                got.append("MISSING_SLAVING_DUAL")
            if "[[File:2013 Match Play Championship p106 Chris Westergard DS.png|800px]]" not in text:
                got.append("MISSING_SCAN")
        if t == "2013 Match Play Championship":
            if "Mike Tomashewski DS Invasion" not in text:
                got.append("HUB_MISSING_TOMASHEWSKI_DS")
            if "Mike Tomashewski LS Yavin 4: Massassi Throne Room" not in text:
                got.append("HUB_MISSING_TOMASHEWSKI_LS")
            if "Chris Westergard DS Wookiee Slaving Operation" not in text:
                got.append("HUB_MISSING_WESTERGARD_DS")
            if "Chris Westergard LS Watch Your Step" not in text:
                got.append("HUB_MISSING_WESTERGARD_LS")
        print(t, "OK" if not got else "FAIL " + "; ".join(got))
        n += len(got)
    print("TOTAL", n)
    return 0 if n == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
