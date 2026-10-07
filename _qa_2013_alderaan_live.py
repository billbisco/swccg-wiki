#!/usr/bin/env python3
"""Live QA for 2013 Alderaan Regionals hub + leftover typed dest."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Alderaan Regionals",
    "2013 Alderaan Regionals Ryan Jellison DS Imperial Entanglements",
    "2013 Alderaan Regionals Ryan Jellison LS Hidden Base (V)",
    "2013 Alderaan Regionals Chris Menzel DS Hunt Down And Destroy The Jedi",
    "2013 Alderaan Regionals Chris Menzel LS Plead My Case To The Senate",
    "2013 Alderaan Regionals Ganden Yanaga DS Invasion",
    "2013 Alderaan Regionals Ganden Yanaga LS Quiet Mining Colony",
    "2013 Alderaan Regionals Bren Derlin DS Invasion",
    "2013 Alderaan Regionals Bren Derlin LS Communing",
    "2013 Alderaan Regionals Anthony Massung LS The Hyperdrive Generator's Gone",
    "2013 Alderaan Regionals Roy McCarthy DS Kessel",
    "2013 Alderaan Regionals Roy McCarthy LS Sullust",
    "Ryan Jellison",
    "Clayton Atkin",
    "Bren Derlin",
    "Anthony Massung",
    "Roy McCarthy",
    "Chris Menzel",
    "Matthew Harrison-Trainor",
    "Ganden Yanaga",
    "List of SWCCG tournaments",
]
SHORT = 2000
STUBS = {
    "Clayton Atkin",
    "Bren Derlin",
    "Chris Menzel",
    "Ryan Jellison",
    "Anthony Massung",
    "Roy McCarthy",
    "Ganden Yanaga",
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
        if t == "2013 Alderaan Regionals":
            if "Ryan Jellison" not in text:
                issues.append("HUB_MISSING_JELLISON")
            if "Chris Menzel" not in text:
                issues.append("HUB_MISSING_MENZEL")
            if "Ganden Yanaga" not in text:
                issues.append("HUB_MISSING_YANAGA")
            if "Bren Derlin" not in text:
                issues.append("HUB_MISSING_DERLIN")
            if "Roy McCarthy" not in text:
                issues.append("HUB_MISSING_MCCARTHY")
            if "Hidden Base" not in text:
                issues.append("HUB_MISSING_JELLISON_LS")
            if "Wiki column" in text or "!! Wiki" in text:
                issues.append("HAS_WIKI_COLUMN")
        if t == "List of SWCCG tournaments" and "2013 Alderaan Regionals" not in text:
            issues.append("LIST_MISSING_ALDERAAN")
        status = "OK" if not issues else "FAIL " + "; ".join(issues)
        print(f"{status}\t{t}\tid={pid} stable={stable} size={length}")
        if issues:
            issues_all.append(t)
    print("issues", len(issues_all))
    if issues_all:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
