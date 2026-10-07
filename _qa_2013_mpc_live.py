#!/usr/bin/env python3
"""Live QA for 2013 Match Play Championship typed Banger/Brown apply."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship",
    "2013 Match Play Championship Day 1 Amar Banger DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Amar Banger LS Anger, Fear, Aggression (V)",
    "2013 Match Play Championship Day 1 Keith Brown DS Wookiee Slaving Operation",
    "2013 Match Play Championship Day 1 Keith Brown LS There Is Good In Him",
    "2013 Match Play Championship Day 1 Wayne Cullen DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Wayne Cullen LS Communing",
    "2013 Match Play Championship Day 1 Barry Alperstein DS A Stunning Move",
    "2013 Match Play Championship Day 1 Barry Alperstein LS Quiet Mining Colony",
    "2013 Match Play Championship Day 1 Nicholas Amato DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Nicholas Amato LS Communing",
    "2013 Match Play Championship Day 1 John Anderson DS Kessel",
    "2013 Match Play Championship Day 1 John Anderson LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Steve Baroni DS Hunt Down And Destroy The Jedi (V)",
    "2013 Match Play Championship Day 1 Steve Baroni LS There Is Good In Him",
    "2013 Match Play Championship Day 1 Andrew Bollentino DS Contract Killers",
    "2013 Match Play Championship Day 1 Andrew Bollentino LS Plead My Case To The Senate",
    "2013 Match Play Championship Day 1 Brian Brodsky DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Brian Brodsky LS You Can Either Profit By This...",
    "2013 Match Play Championship Day 1 Carl Buck DS Hunt Down And Destroy The Jedi",
    "2013 Match Play Championship Day 1 Carl Buck LS There Is Good In Him",
    "2013 Match Play Championship Day 1 Matt Carulli DS Hunt Down And Destroy The Jedi",
    "2013 Match Play Championship Day 1 Matt Carulli LS Careful Planning (V)",
    "2013 Match Play Championship Day 1 Casey Anis DS A Stunning Move",
    "2013 Match Play Championship Day 1 Casey Anis LS You Can Either Profit By This...",
    "2013 Match Play Championship Day 1 Justin Carulli DS You Cannot Hide Forever",
    "2013 Match Play Championship Day 1 Justin Carulli LS Watch Your Step",
    "2013 Match Play Championship Day 1 Jerry Heine DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Jerry Heine LS We'll Handle This",
    "2013 Match Play Championship Day 1 Matthew Harrison-Trainor DS Ralltiir Operations",
    "2013 Match Play Championship Day 1 Matthew Harrison-Trainor LS Watch Your Step (V)",
    "2013 Match Play Championship Day 1 Brian Hunter DS A Stunning Move",
    "2013 Match Play Championship Day 1 Brian Hunter LS Plead My Case To The Senate",
    "2013 Match Play Championship Day 1 Brian Herold DS Kessel: Spice Mines - Administrator's Office",
    "2013 Match Play Championship Day 1 Brian Herold LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Cole Lepine DS Ralltiir Operations",
    "2013 Match Play Championship Day 1 Cole Lepine LS Watch Your Step (V)",
    "2013 Match Play Championship Day 1 Sam Marlow DS Hunt Down And Destroy The Jedi",
    "2013 Match Play Championship Day 1 Sam Marlow LS Coruscant: Night Club",
    "Amar Banger",
    "Keith Brown",
    "Barry Alperstein",
    "Nicholas Amato",
    "John Anderson",
    "Steve Baroni",
    "Casey Anis",
    "Andrew Bollentino",
    "Brian Brodsky",
    "Carl Buck",
    "Matt Carulli",
    "Justin Carulli",
    "Wayne Cullen",
    "Jerry Heine",
    "Brian Herold",
    "Brian Hunter",
    "Cole Lepine",
    "Sam Marlow",
    "Matthew Harrison-Trainor",
    "Joe Pinto",
    "Mike Tomashewski",
    "Chris Westergard",
    "List of SWCCG tournaments",
]
SHORT = 2000
STUBS = {
    "Barry Alperstein",
    "Nicholas Amato",
    "John Anderson",
    "Steve Baroni",
    "Casey Anis",
    "Andrew Bollentino",
    "Brian Brodsky",
    "Carl Buck",
    "Matt Carulli",
    "Justin Carulli",
    "Wayne Cullen",
    "Jerry Heine",
    "Brian Herold",
    "Brian Hunter",
    "Cole Lepine",
    "Sam Marlow",
    "Matthew Harrison-Trainor",
    "Joe Pinto",
    "Mike Tomashewski",
    "Chris Westergard",
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
        if t == "2013 Match Play Championship":
            if "Amar Banger" not in text:
                issues.append("HUB_MISSING_BANGER")
            if "Keith Brown" not in text:
                issues.append("HUB_MISSING_BROWN")
            if "Wayne Cullen" not in text:
                issues.append("HUB_MISSING_CULLEN")
            if "Communing" not in text:
                issues.append("HUB_MISSING_CULLEN_LS")
            if "Barry Alperstein" not in text:
                issues.append("HUB_MISSING_ALPERSTEIN")
            if "A Stunning Move" not in text:
                issues.append("HUB_MISSING_ALPERSTEIN_DS")
            if "Quiet Mining Colony" not in text:
                issues.append("HUB_MISSING_ALPERSTEIN_LS")
            if "Nicholas Amato" not in text:
                issues.append("HUB_MISSING_AMATO")
            if "John Anderson" not in text:
                issues.append("HUB_MISSING_ANDERSON")
            if "Mind What You Have Learned" not in text:
                issues.append("HUB_MISSING_ANDERSON_LS")
            if "Steve Baroni" not in text:
                issues.append("HUB_MISSING_BARONI")
            if "Hunt Down And Destroy The Jedi" not in text:
                issues.append("HUB_MISSING_BARONI_DS")
            if "'''Winner:''' [[Steve Baroni]]" not in text:
                issues.append("HUB_MISSING_WINNER")
            if "New Brunswick" not in text:
                issues.append("HUB_MISSING_SITE")
            if "Andrew Bollentino" not in text:
                issues.append("HUB_MISSING_BOLLENTINO")
            if "Contract Killers" not in text:
                issues.append("HUB_MISSING_BOLLENTINO_DS")
            if "Brian Brodsky" not in text:
                issues.append("HUB_MISSING_BRODSKY")
            if "You Can Either Profit" not in text:
                issues.append("HUB_MISSING_BRODSKY_LS")
            if "Carl Buck" not in text:
                issues.append("HUB_MISSING_BUCK")
            if "There Is Good In Him" not in text:
                issues.append("HUB_MISSING_BUCK_LS")
            if "Matt Carulli" not in text:
                issues.append("HUB_MISSING_CARULLI")
            if "Careful Planning" not in text:
                issues.append("HUB_MISSING_CARULLI_LS")
            if "Casey Anis" not in text:
                issues.append("HUB_MISSING_ANIS")
            if "A Stunning Move" not in text:
                issues.append("HUB_MISSING_ANIS_DS")
            if "Justin Carulli" not in text:
                issues.append("HUB_MISSING_JUSTIN_CARULLI")
            if "You Cannot Hide Forever" not in text:
                issues.append("HUB_MISSING_JUSTIN_DS")
            if "Jerry Heine" not in text:
                issues.append("HUB_MISSING_HEINE")
            if "We'll Handle This" not in text:
                issues.append("HUB_MISSING_HEINE_LS")
            if "Cole Lepine" not in text:
                issues.append("HUB_MISSING_LEPINE")
            if "Sam Marlow" not in text:
                issues.append("HUB_MISSING_MARLOW")
            if "Wiki column" in text or "!! Wiki" in text:
                issues.append("HAS_WIKI_COLUMN")
        if t == "List of SWCCG tournaments" and "2013 Match Play Championship" not in text:
            issues.append("LIST_MISSING_MPC")
        status = "OK" if not issues else "FAIL " + "; ".join(issues)
        print(f"{status}\t{t}\tid={pid} stable={stable} size={length}")
        if issues:
            issues_all.append(t)
    print("issues", len(issues_all))
    if issues_all:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
