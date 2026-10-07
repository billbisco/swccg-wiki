#!/usr/bin/env python3
"""Live QA for 2012 US Nationals leftover Xerox dests.

python _qa_2012_nats_xerox.py --delta   # last pair + hub
python _qa_2012_nats_xerox.py --full    # every CHECK (default)
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 US Nationals Day 1 John Anderson DS A Stunning Move",
        ["A Stunning Move", "Grievous, Hunter Of Jedi", "Probot", "John Anderson"],
    ),
    (
        "2012 US Nationals Day 1 John Anderson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "I'll Take The Odds", "Ultimatum", "John Anderson"],
    ),
    (
        "2012 US Nationals Day 1 Devin Aue LS Naboo",
        ["Naboo", "We're Doomed", "Kaadu", "Devin Aue"],
    ),
    (
        "2012 US Nationals Day 1 Devin Aue DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Kitik Keed'kak", "Rystall", "Devin Aue"],
    ),
    (
        "2012 US Nationals Day 1 Grant B LS Restore Freedom To The Galaxy",
        ["Restore Freedom To The Galaxy", "Stay Sharp!", "Luke's Back", "Grant B"],
    ),
    (
        "2012 US Nationals Day 1 Grant B DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Start Your Engines!", "I'd Just As Soon Kiss A Wookiee", "Grant B"],
    ),
    (
        "2012 US Nationals Day 1 Jan B LS Restore Freedom To The Galaxy",
        ["Restore Freedom To The Galaxy", "Yavin 4", "Star Destroyer!", "Jan B"],
    ),
    (
        "2012 US Nationals Day 1 Jan B DS Contract Killers",
        ["Contract Killers", "Gift Of The Mentor", "This Is Just Wrong", "Jan B"],
    ),
    (
        "2012 US Nationals Day 1 Brandon Burgt LS We Have A Plan",
        ["We Have A Plan", "Sai'torr Kal Fas", "Thrown Back", "Brandon Burgt"],
    ),
    (
        "2012 US Nationals Day 1 Brandon Burgt DS Fondor",
        ["Fondor", "Flagship Executor", "I'll Take Them Myself", "Brandon Burgt"],
    ),
    (
        "2012 US Nationals Day 1 Angelo Consoli LS We'll Handle This (V)",
        ["We'll Handle This", "Sai'torr Kal Fas", "Anger, Fear, Aggression", "Angelo Consoli"],
    ),
    (
        "2012 US Nationals Day 1 Angelo Consoli DS A Stunning Move",
        ["A Stunning Move", "Grievous, Hunter Of Jedi", "Oh, Switch Off", "Angelo Consoli"],
    ),
    (
        "2012 US Nationals Day 1 Cooleo LS Rebel Strike Team (V)",
        ["Rebel Strike Team", "Throw Me Another Charge", "The Shield Is Down!", "Cooleo"],
    ),
    (
        "2012 US Nationals Day 1 Cooleo DS Contract Killers",
        ["Contract Killers", "Jabba's Haven", "Boba Fett, Bounty Hunter", "Cooleo"],
    ),
    (
        "2012 US Nationals Day 1 Jessica Echeverria LS Communing",
        ["Communing", "Booster In Pulsar Skate", "Restore Freedom To The Galaxy", "Jessica Echeverria"],
    ),
    (
        "2012 US Nationals Day 1 Jessica Echeverria DS Bring Him Before Me",
        ["Bring Him Before Me", "Grievous, Hunter Of Jedi", "Boba Fett, Bounty Hunter", "Jessica Echeverria"],
    ),
    (
        "2012 US Nationals Day 1 Peter Grouty LS Watch Your Step (V)",
        ["Watch Your Step", "Millennium Falcon", "It's Not My Fault!", "Peter Grouty"],
    ),
    (
        "2012 US Nationals Day 1 Peter Grouty DS Tatooine (Coruscant)",
        ["Tatooine (Coruscant)", "Boba Fett, Bounty Hunter", "Knowledge And Defense", "Peter Grouty"],
    ),
    (
        "2012 US Nationals Day 1 Tom Frafjord LS We'll Handle This (V)",
        ["We'll Handle This", "Yoda, Senior Council Member", "Anger, Fear, Aggression", "Tom Frafjord"],
    ),
    (
        "2012 US Nationals Day 1 Tom Frafjord DS A Stunning Move",
        ["A Stunning Move", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "Tom Frafjord"],
    ),
    (
        "2012 US Nationals Day 1 Fernando LS Naboo",
        ["Naboo", "Admiral Ackbar", "Anger, Fear, Aggression", "Fernando"],
    ),
    (
        "2012 US Nationals Day 1 Fernando DS Ralltiir Operations",
        ["Ralltiir Operations", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "Fernando"],
    ),
    (
        "2012 US Nationals Day 1 George (2012 US Nationals) LS Restore Freedom To The Galaxy",
        ["Restore Freedom To The Galaxy", "Luke Skywalker", "Anger, Fear, Aggression", "George (2012 US Nationals)"],
    ),
    (
        "2012 US Nationals Day 1 George (2012 US Nationals) DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "George (2012 US Nationals)"],
    ),
    (
        "2012 US Nationals Day 1 Chris Haglund LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Luke Skywalker", "Hoth: North Ridge", "Chris Haglund"],
    ),
    (
        "2012 US Nationals Day 1 Chris Haglund DS Knowledge And Defense (V)",
        ["Knowledge And Defense", "Imperial-Class Star Destroyer", "TIE Scout", "Chris Haglund"],
    ),
    (
        "2012 US Nationals Day 1 Matt Hanson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Luke Skywalker, Jedi Knight", "Anger, Fear, Aggression", "Matt Hanson"],
    ),
    (
        "2012 US Nationals Day 1 Matt Hanson DS Endor Operations",
        ["Endor Operations", "Darth Vader", "Knowledge And Defense", "Matt Hanson"],
    ),
    (
        "2012 US Nationals Day 1 Marc Hanson LS Rescue The Princess",
        ["Rescue The Princess", "It Could Be Worse", "Yavin 4", "Marc Hanson"],
    ),
    (
        "2012 US Nationals Day 1 Marc Hanson DS Vader's Lightsaber",
        ["Vader's Lightsaber", "Grand Moff Tarkin", "Death Star Trooper", "Marc Hanson"],
    ),
    (
        "2012 US Nationals Day 1 Brian Herold LS Hidden Base (V)",
        ["Hidden Base", "Blue Squadron B-wing", "Anger, Fear, Aggression", "Brian Herold"],
    ),
    (
        "2012 US Nationals Day 1 Brian Herold DS Combat Readiness (V)",
        ["Combat Readiness", "Jango Fett, The Assassin", "Knowledge And Defense", "Brian Herold"],
    ),
    (
        "2012 US Nationals Day 1 Jeeps LS Hidden Base (V)",
        ["Hidden Base", "All Wings Report In", "Anger, Fear, Aggression", "Jeeps"],
    ),
    (
        "2012 US Nationals Day 1 Jeeps DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Knowledge And Defense", "Jeeps"],
    ),
    (
        "2012 US Nationals Day 1 Calvin Kurten LS There Is Good In Him",
        ["There Is Good In Him", "Ewok Sentry", "Anger, Fear, Aggression", "Calvin Kurten"],
    ),
    (
        "2012 US Nationals Day 1 Calvin Kurten DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Lott Dod", "Knowledge And Defense", "Calvin Kurten"],
    ),
    (
        "2012 US Nationals Day 1 Bryan McCune LS Center Of Tyranny",
        ["Center Of Tyranny", "Luke Skywalker, Rebel Hero", "Anger, Fear, Aggression", "Bryan McCune"],
    ),
    (
        "2012 US Nationals Day 1 Bryan McCune DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Victory", "Knowledge And Defense", "Bryan McCune"],
    ),
    (
        "2012 US Nationals Day 1 Orlie Martin LS Infiltration",
        ["Infiltration", "Anger, Fear, Aggression", "Uh-Oh", "Orlie Martin"],
    ),
    (
        "2012 US Nationals Day 1 Orlie Martin DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Lott Dod", "Knowledge And Defense", "Orlie Martin"],
    ),
    (
        "2012 US Nationals Day 1 Leo Molitor LS Watch Your Step",
        ["Watch Your Step", "Anger, Fear, Aggression", "Luke Skywalker, Rebel Hero", "Leo Molitor"],
    ),
    (
        "2012 US Nationals Day 1 Leo Molitor DS Let Them Make The First Move",
        ["Let Them Make The First Move", "Darth Vader", "Knowledge And Defense", "Leo Molitor"],
    ),
    (
        "2012 US Nationals Day 1 Brady LS You Can Either Profit By This...",
        ["You Can Either Profit By This...", "Anger, Fear, Aggression", "Luke Skywalker, Jedi Knight", "Brady"],
    ),
    (
        "2012 US Nationals Day 1 Brady DS Kessel",
        ["Kessel", "Darth Vader With Lightsaber", "Knowledge And Defense", "Brady"],
    ),
    (
        "2012 US Nationals Day 1 Scott Morgan LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression", "Luke Skywalker, Jedi Knight", "Scott Morgan"],
    ),
    (
        "2012 US Nationals Day 1 Scott Morgan DS A Stunning Move",
        ["A Stunning Move", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "Scott Morgan"],
    ),
    (
        "2012 US Nationals Day 1 Aaron Nelson LS Infiltration",
        ["Infiltration", "Anger, Fear, Aggression", "Han Solo, Innocent Scoundrel", "Aaron Nelson"],
    ),
    (
        "2012 US Nationals Day 1 Jake Nelson LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Luke Skywalker, Jedi Knight", "Queen Amidala, Ruler Of Naboo", "Jake Nelson"],
    ),
    (
        "2012 US Nationals Day 1 Jake Nelson DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Death Star", "Knowledge And Defense", "Jake Nelson"],
    ),
    (
        "2012 US Nationals Day 1 Mitch Nieland LS Quiet Mining Colony",
        ["Quiet Mining Colony", "Anger, Fear, Aggression", "Qui-Gon Jinn With Lightsaber", "Mitch Nieland"],
    ),
    (
        "2012 US Nationals Day 1 Mitch Nieland DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Death Star", "Knowledge And Defense", "Mitch Nieland"],
    ),
    (
        "2012 US Nationals Day 1 Jess Ojala LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression", "Luke Skywalker, Strong In The Force", "Jess Ojala"],
    ),
    (
        "2012 US Nationals Day 1 Jess Ojala DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Darth Vader, Betrayer Of The Jedi", "Jess Ojala"],
    ),
    (
        "2012 US Nationals Day 1 Nick Olson LS You Can Either Profit By This...",
        ["You Can Either Profit By This...", "Anger, Fear, Aggression", "Luke Skywalker, Strong In The Force", "Nick Olson"],
    ),
    (
        "2012 US Nationals Day 1 Nick Olson DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Darth Vader, Betrayer Of The Jedi", "Nick Olson"],
    ),
    (
        "2012 US Nationals Day 1 Alden Peterson LS Hidden Base (V)",
        ["Hidden Base", "Heading For The Medical Frigate", "Anger, Fear, Aggression", "Alden Peterson"],
    ),
    (
        "2012 US Nationals Day 1 Alden Peterson DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Knowledge And Defense", "Mara Jade, The Emperor's Hand", "Alden Peterson"],
    ),
    (
        "2012 US Nationals Day 1 Mark Peterson LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Anger, Fear, Aggression", "Luke Skywalker, Jedi Knight", "Mark Peterson"],
    ),
    (
        "2012 US Nationals Day 1 Mark Peterson DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Darth Vader", "Mark Peterson"],
    ),
    (
        "2012 US Nationals Day 1 Jake Pietruszewski LS You Can Either Profit By This...",
        ["You Can Either Profit By This...", "Anger, Fear, Aggression", "Luke Skywalker, Rebel Hero", "Jake Pietruszewski"],
    ),
    (
        "2012 US Nationals Day 1 Jake Pietruszewski DS Court Of The Vile Gangster",
        ["Court Of The Vile Gangster", "Knowledge And Defense", "Jabba The Hutt", "Jake Pietruszewski"],
    ),
    (
        "2012 US Nationals Day 1 Nick Rambo LS You Can Either Profit By This...",
        ["You Can Either Profit By This...", "Anger, Fear, Aggression", "Luke Skywalker, Strong In The Force", "Nick Rambo"],
    ),
    (
        "2012 US Nationals Day 1 Nick Rambo DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Darth Vader", "Nick Rambo"],
    ),
    (
        "2012 US Nationals Day 1 Chris Schoenthal LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression", "Luke Skywalker, Strong In The Force", "Chris Schoenthal"],
    ),
    (
        "2012 US Nationals Day 1 Chris Schoenthal DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Knowledge And Defense", "Darth Sidious", "Chris Schoenthal"],
    ),
    (
        "2012 US Nationals Day 1 Matt Scott LS Endor",
        ["Endor", "Anger, Fear, Aggression", "Luke Skywalker", "Matt Scott"],
    ),
    (
        "2012 US Nationals Day 1 Matt Scott DS Hoth",
        ["Hoth", "Knowledge And Defense", "Bantha", "Matt Scott"],
    ),
    (
        "2012 US Nationals Day 1 Kevin Shannon LS Infiltration",
        ["Infiltration", "Anger, Fear, Aggression", "Chewbacca, Walking Carpet", "Kevin Shannon"],
    ),
    (
        "2012 US Nationals Day 1 Kevin Shannon DS Ralltiir Operations",
        ["Ralltiir Operations", "Knowledge And Defense", "Darth Vader", "Kevin Shannon"],
    ),
    (
        "2012 US Nationals Day 1 Conrad Simmering LS Quiet Mining Colony",
        ["Quiet Mining Colony", "Anger, Fear, Aggression", "Luke With Lightsaber", "Conrad Simmering"],
    ),
    (
        "2012 US Nationals Day 1 Conrad Simmering DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Darth Vader", "Conrad Simmering"],
    ),
    (
        "2012 US Nationals Day 1 Zach Stenerson LS Communing",
        ["Communing", "Anger, Fear, Aggression", "Chewbacca, Enraged", "Zach Stenerson"],
    ),
    (
        "2012 US Nationals Day 1 Zach Stenerson DS Kessel",
        ["Kessel / Spice Mines Of Kessel", "Knowledge And Defense", "Darth Maul", "Zach Stenerson"],
    ),
    (
        "2012 US Nationals Day 1 Nick Swedal LS Local Uprising (V)",
        ["Local Uprising (V) / Liberation (V)", "Don't Get Cocky", "Commander Luke Skywalker", "Nick Swedal"],
    ),
    (
        "2012 US Nationals Day 1 Nick Swedal DS Endor Operations",
        ["Endor Operations / Imperial Outpost", "Imperial-Class Star Destroyer", "Darth Vader", "Nick Swedal"],
    ),
    (
        "2012 US Nationals Day 1 Matthew Ulstad LS Ewok Log Jam",
        ["Ewok Log Jam", "Anger, Fear, Aggression", "Ewok Sentry", "Matthew Ulstad"],
    ),
    (
        "2012 US Nationals Day 1 John Veasey LS Center Of Tyranny",
        ["Center Of Tyranny / A Liberated World", "Anger, Fear, Aggression", "Luke Skywalker, Rebel Hero", "John Veasey"],
    ),
    (
        "2012 US Nationals Day 1 John Veasey DS Ralltiir Operations",
        ["Ralltiir Operations / In The Hands Of The Empire", "Jango Fett, The Assassin", "Grand Admiral Thrawn", "John Veasey"],
    ),
    (
        "2012 US Nationals Day 1 Mark Walseth LS Careful Planning (V)",
        ["Careful Planning", "Restore Freedom To The Galaxy", "Artoo-Detoo In Red 5", "Mark Walseth"],
    ),
    (
        "2012 US Nationals Day 1 Mark Walseth DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan / The Ultimate Power In The Universe", "Knowledge And Defense", "Death Star", "Mark Walseth"],
    ),
    (
        "2012 US Nationals Day 1 Hayes Hunter LS Fear, Piety, And Passion",
        ["Fear, Piety, And Passion", "Anger, Fear, Aggression", "Luke Skywalker, Rebel Hero", "Hayes Hunter"],
    ),
    (
        "2012 US Nationals Day 1 Hayes Hunter DS Kessel",
        ["Kessel / Spice Mines Of Kessel", "Knowledge And Defense", "Jango Fett, The Assassin", "Hayes Hunter"],
    ),
    (
        "2012 US Nationals Day 1 Unknown Player LS You Can Either Profit By This...",
        ["You Can Either Profit By This... / Or Be Destroyed", "Anger, Fear, Aggression", "Heading For The Medical Frigate", "Unknown Player"],
    ),
    (
        "2012 US Nationals Day 1 Unknown Player DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)", "Grievous, Hunter Of Jedi", "Emperor Palpatine", "Unknown Player"],
    ),
    (
        "2012 US Nationals Day 2 Angelo Consoli LS Mind What You Have Learned (V)",
        ["Mind What You Have Learned (V) / Save You It Can (V)", "Anger, Fear, Aggression", "Luke Skywalker, Jedi Knight", "Angelo Consoli"],
    ),
    (
        "2012 US Nationals Day 2 Angelo Consoli DS A Stunning Move",
        ["A Stunning Move / A Valuable Hostage", "Grievous, Hunter Of Jedi", "Search And Destroy", "Angelo Consoli"],
    ),
    (
        "2012 US Nationals Day 2 Tom Frafjord LS Mind What You Have Learned",
        ["Mind What You Have Learned / Save You It Can", "Anger, Fear, Aggression", "Luke Skywalker, Jedi Knight", "Tom Frafjord"],
    ),
    (
        "2012 US Nationals Day 2 Tom Frafjord DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal? / I Will Make It", "Boba Fett, Renowned Bounty Hunter", "Jango Fett, The Assassin", "Tom Frafjord"],
    ),
    (
        "2012 US Nationals Day 2 Brian Herold LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Communing", "Maneuvering Flaps", "Brian Herold"],
    ),
    (
        "2012 US Nationals Day 2 Brian Herold DS Kessel",
        ["Kessel / Spice Mines Of Kessel", "Combat Readiness / Full Scale Alert (V)", "Knowledge And Defense (V)", "Brian Herold"],
    ),
    (
        "2012 US Nationals Day 2 Aaron Nelson LS There Is Good In Him",
        ["There Is Good In Him / I Can Save Him", "Maris Brood, Fallen Jedi", "Wookiee Roar (V)", "Aaron Nelson"],
    ),
    (
        "2012 US Nationals Day 2 Aaron Nelson DS Imperial Occupation (V)",
        ["Imperial Occupation (V) / Imperial Control (V)", "Endor Shield (V)", "Knowledge And Defense (V)", "Aaron Nelson"],
    ),
    (
        "2012 US Nationals Day 2 Jake Nelson LS Carbon Chamber Testing",
        ["Carbon Chamber Testing / My Favorite Decoration", "Keeping The Empire Out Forever", "Anger, Fear, Aggression (V)", "Jake Nelson"],
    ),
    (
        "2012 US Nationals Day 2 Jake Nelson DS Combat Readiness (V)",
        ["Combat Readiness / Full Scale Alert (V)", "Imperial Propaganda (V)", "Knowledge And Defense", "Jake Nelson"],
    ),
    (
        "2012 US Nationals Day 2 Kevin Shannon LS Watch Your Step (V)",
        ["Watch Your Step (V) / This Place Can Be A Little Rough (V)", "Let The Wookiee Win (V)", "Anger, Fear, Aggression", "Kevin Shannon"],
    ),
    (
        "2012 US Nationals Day 2 Kevin Shannon DS Ralltiir Operations",
        ["Ralltiir Operations / In The Hands Of The Empire", "Tarkin's Bounty", "Darth Sidious", "Kevin Shannon"],
    ),
    (
        "2012 US Nationals",
        ["John Anderson", "Devin Aue", "Grant B", "Jan B", "Brandon Burgt", "Angelo Consoli", "Cooleo", "Jessica Echeverria", "Peter Grouty", "Tom Frafjord", "Fernando", "George (2012 US Nationals)", "Chris Haglund", "Matt Hanson", "Marc Hanson", "Brian Herold", "Jeeps", "Calvin Kurten", "Bryan McCune", "Orlie Martin", "Leo Molitor", "Brady", "Scott Morgan", "Aaron Nelson", "Jake Nelson", "Mitch Nieland", "Jess Ojala", "Nick Olson", "Alden Peterson", "Mark Peterson", "Jake Pietruszewski", "Nick Rambo", "Chris Schoenthal", "Matt Scott", "Kevin Shannon", "Conrad Simmering", "Zach Stenerson", "Nick Swedal", "Matthew Ulstad", "John Veasey", "Mark Walseth", "Hayes Hunter", "Unknown Player", "Emil Wallin", "8–10 June 2012"],
    ),
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "text|revid|displaytitle",
            "format": "json",
            "disablelimitreport": 1,
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def flagged(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    return next(iter(pages.values()))


def select_checks(delta: bool) -> list:
    if not delta:
        return CHECKS
    hub = [c for c in CHECKS if c[0] == "2012 US Nationals"]
    decks = [c for c in CHECKS if c[0] != "2012 US Nationals"]
    return decks[-2:] + hub


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--delta", action="store_true", help="last pair + hub")
    ap.add_argument("--full", action="store_true", help="every CHECK (default)")
    args = ap.parse_args()
    checks = select_checks(args.delta and not args.full)
    fail = 0
    for title, needles in checks:
        data = parse(title)
        if "error" in data:
            print("FAIL", title, data["error"])
            fail += 1
            continue
        html = data["parse"]["text"]["*"]
        missing = [n for n in needles if n not in html]
        fl = flagged(title)
        latest = fl.get("lastrevid")
        stable = (fl.get("flagged") or {}).get("stable_revid")
        fr = "OK" if latest and stable and int(latest) == int(stable) else f"latest={latest} stable={stable}"
        if missing or fr != "OK":
            print("FAIL", title, "missing", missing, "fr", fr)
            fail += 1
        else:
            print("OK", title, "fr", fr)
    mode = "delta" if args.delta and not args.full else "full"
    print("TOTAL", fail, "n", len(checks), mode)


if __name__ == "__main__":
    main()
