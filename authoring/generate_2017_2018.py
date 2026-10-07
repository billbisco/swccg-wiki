#!/usr/bin/env python3
"""2017–2018 tournament hubs from PC wrap lists + dest slang → printed titles."""
from __future__ import annotations

import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_html_missing as hm  # noqa: E402
from generate_2019_2021 import (  # noqa: E402
    TOKEN,
    is_bio,
    is_junk_player,
    refs,
    tidy_player_page,
    wiki_fname,
)
from generate_2026_remaining import upsert_stub  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
WRAP = ROOT / "encyclopedia" / "pc-2017-2018"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC = PAGES / "European_Championships.wiki"
TSV = ROOT / "y2017-2018-titles.tsv"

CANON = dict(TOKEN)
CANON.update(
    {
        "Emil Wallen": "Emil Wallin",
        "Johnny Chu": "Jonny Chu",
        "Casper Jørgenson": "Casper Jørgensen",
        "Casper Jorgenson": "Casper Jørgensen",
        "Casper Jorgensen": "Casper Jørgensen",
        "Quirin Furgut": "Quirin Fürgut",
        "Quirin Fuergut": "Quirin Fürgut",
        "Cedrik Vanderhagen": "Cedrik Vanderhaegen",
        "Jonas Hagen": "Jonas Hagen Nørregaard",
        "Jonas Norregaard": "Jonas Hagen Nørregaard",
        "Jonas Nørregaard": "Jonas Hagen Nørregaard",
        "John Morley": "John Moorley",
        "Jan Bereuda": "Jan Berueda",
        "Jason Reindeau": "Jason Riendeau",
        "Kyle Kreuger": "Kyle Krueger",
        "Steve Cellucci": "Stephen Cellucci",
        "Brian Mischke": "Bryan Mischke",
        "Mike D’amboise": "Mike d'Amboise",
        "Mike D'amboise": "Mike d'Amboise",
        "Trevor Partidge": "Trevor Partridge",
        "Trevor Patridge": "Trevor Partridge",
        "Matthew Carulli": "Matt Carulli",
        "Pat Johnson": "Patrick Johnson",
        "György (Bill)": "György Póra",
        "Gyorgy (Bill)": "György Póra",
        "Pete the Welsh": "Peter Rowlands",
        "Jimmy Falleans": "Jimmy Faelens",
        "Noah Falleans": "Noah Faelens",
        "Julian-Adres Smolarek": "Julian Smolarek",
        "Julian-Andrés Smolarek": "Julian Smolarek",
        "Julien Schmolarik": "Julian Smolarek",
        "Jonas Jukubowski": "Jonas Jakubowski",
        "David Luhaær": "David Luhaær",
        "Zeimowit Skwara": "Ziemowit Skwara",
        "Stephen Skilton": "Steve Skilton",
        "Steve Skilton": "Steve Skilton",
        "Michael Richards": "Mike Richards",
        "Michael Turner": "Mike Turner",
        "Joseph Phillips": "Joe Phillips",
        "Joseph Graham": "Joseph Graham",
        "Sandwhirl": "Sandwhirl",
        "Alex T.": "Alex T.",
        "Kent L.": "Kent Larsen",
        "Piotr Dash_R": "Piotr Dash_R",
        "Clint Menzel": "Clint Menzel",
        "Adam Kwart": "Adam Kwart",
        "Pete Srodoski": "Pete Srodoski",
        "Caleb Foth": "Caleb Foth",
        "Frank Lam": "Frank Lam",
        "Brandon Bunn": "Brandon Bunn",
        "Vince Hutchins": "Vince Hutchins",
        "Joel Pittman": "Joel Pittman",
        "Ross Littauer": "Ross Littauer",
        "Cyrus Morosoff": "Cyrus Morosoff",
        "Travis Egan": "Travis Egan",
        "Mike French": "Mike French",
        "Colin Wellborn": "Colin Wellborn",
        "Greyson Thompson": "Greyson Thompson",
        "Kyle Szklenski": "Kyle Szklenski",
        "Ryan Obman": "Ryan Obman",
        "Vinny Rossi": "Vinny Rossi",
        "Jon McFarland": "Jon McFarland",
        "Michael Tomashewski": "Michael Tomashewski",
        "Nick Amato": "Nick Amato",
        "John Michael Earwood": "John Michael Earwood",
        "Mike Gemme": "Mike Gemme",
        "Matt Schmaltz": "Matt Schmaltz",
        "Mark Sebring": "Mark Sebring",
        "Seth Acree": "Seth Acree",
        "James Barnes": "James Barnes",
        "Jonathan Bauer": "Jonathan Bauer",
        "William Ament": "William Ament",
        "Ethan Phou": "Ethan Phou",
        "Fernando Souza": "Fernando Souza",
        "Stephen Fulner": "Stephen Fulner",
        "Benedict Donnay": "Benedict Donnay",
        "Andrew Sauvageau": "Andrew Sauvageau",
        "Andrew Kline": "Andrew Kline",
        "Charlie Herren": "Charlie Herren",
        "Jeff Visseaux": "Jeff Visseaux",
        "Gerald Sieber": "Gerald Sieber",
        "Jerome Nitschke": "Jerome Nitschke",
        "Tobias Bukkehave": "Tobias Bukkehave",
        "Rasmus Juul": "Rasmus Juul",
        "Darren Malins": "Darren Malins",
        "Jon Holtet": "Jon Benkert Holtet",
        "Jon Benkert Holtet": "Jon Benkert Holtet",
        "Mike Rosenberger": "Mike Rosenberger",
        "Christopher Claßen": "Christopher Claßen",
        "Christopher Claẞen": "Christopher Claßen",
        "Stefan Boersma": "Stefan Boersma",
        "Martin Sommer": "Martin Sommer",
        "Massimiliano Colussi": "Massimiliano Colussi",
        "Pete Rowlins": "Peter Rowlands",
        "Ulli Reuter": "Ulli Reuter",
        "Ralf Wachowiak": "Ralf Wachowiak",
        "Oliver Wielicki": "Oliver Wielicki",
        "Tilmann Petersen": "Tilmann Petersen",
        "Nelson Cazon": "Nelson Cazon",
        "Julian Konrad": "Julian Konrad",
        "Jonas Jacobsen": "Jonas Jacobsen",
        "Jordi Paul": "Jordi Paul",
        "Bertrand Momal": "Bertrand Momal",
        "Amar Banger": "Amar Banger",
        "Alexander Sheynis": "Alexander Sheynis",
        "Gibson Yim": "Gibson Yim",
        "Brandon Baity": "Brandon Baity",
        "Matt Thornton": "Matt Thornton",
        "Matt Wadden": "Matt Wadden",
        "Jeff Scales": "Jeffrey Scales",
        "Jeffrey Scales": "Jeffrey Scales",
        "Pat Johnson": "Patrick Johnson",
        "Joe Giannetti": "Joe Giannetti",
        "Joe Gianetti": "Joe Giannetti",
    }
)

SLANG = {
    "tto": "Endor Operations",
    "eops": "Endor Operations",
    "eop": "Endor Operations",
    "endor ops": "Endor Operations",
    "endor operations": "Endor Operations",
    "that thing's operational": "Endor Operations",
    "ie": "Imperial Entanglements",
    "ie mains": "Imperial Entanglements",
    "imperial entanglements": "Imperial Entanglements",
    "map": "I Want That Map",
    "aobs": "Agents Of Black Sun",
    "black sun": "Agents Of Black Sun",
    "court": "Court Of The Vile Gangster",
    "court mains": "Court Of The Vile Gangster",
    "court scum": "Court Of The Vile Gangster",
    "cotvg": "Court Of The Vile Gangster",
    "cotvg mains": "Court Of The Vile Gangster",
    "first order court": "Court Of The Vile Gangster",
    "hd": "Hunt Down And Destroy The Jedi",
    "hdadtj": "Hunt Down And Destroy The Jedi",
    "hunt down": "Hunt Down And Destroy The Jedi",
    "fo hd": "Hunt Down And Destroy The Jedi",
    "hd tanks": "Hunt Down And Destroy The Jedi",
    "isb": "ISB Operations",
    "bhbm": "Bring Him Before Me",
    "cct": "Carbon Chamber Testing",
    "cct scum": "Carbon Chamber Testing",
    "cct ig": "Carbon Chamber Testing",
    "cct ig-88": "Carbon Chamber Testing",
    "invasion": "Invasion",
    "mkos": "My Kind Of Scum",
    "tdigwatt": "This Deal Is Getting Worse All The Time",
    "fo deal": "This Deal Is Getting Worse All The Time",
    "sycfa": "Set Your Course For Alderaan",
    "senate": "Plead My Case To The Senate",
    "fo senate": "Senate Occupied",
    "ds senate": "Senate Occupied",
    "ls senate": "Plead My Case To The Senate",
    "watto": "No Money, No Parts, No Deal!",
    "combat": "Combat Readiness",
    "ds combat": "Combat Readiness",
    "ls combat": "Combat Preparedness",
    "dark combat": "Combat Readiness",
    "coruscant crv": "Combat Readiness (V)",
    "corsucant crv": "Combat Readiness (V)",
    "hoth crv": "Combat Readiness (V)",
    "tatooine crv": "Combat Readiness (V)",
    "bespin crv": "Combat Readiness (V)",
    "jakku cpv": "Combat Preparedness (V)",
    "tatooine cpv": "Combat Preparedness (V)",
    "hoth cpv": "Combat Preparedness (V)",
    "hoth cpv mains": "Combat Preparedness (V)",
    "yavin 4 cpv": "Combat Preparedness (V)",
    "wys": "Watch Your Step",
    "oa": "Old Allies",
    "old allies": "Old Allies",
    "diplo": "Diplomatic Mission To Alderaan",
    "dmta": "Diplomatic Mission To Alderaan",
    "trm": "Yavin 4: Massassi Throne Room",
    "qmc": "Quiet Mining Colony",
    "hb": "Hidden Base",
    "hidden base": "Hidden Base",
    "hb sandwhirl": "Hidden Base",
    "hb quads": "Hidden Base",
    "hb mains": "Hidden Base",
    "hb b-wings": "Hidden Base",
    "hb b-wings": "Hidden Base",
    "hb acclamators": "Hidden Base",
    "profit": "You Can Either Profit By This",
    "hitco": "He Is The Chosen One",
    "tigih": "This Is Getting Out Of Hand",
    "whap": "We Have A Plan",
    "rst": "Rebel Strike Team",
    "ebo": "Echo Base Operations",
    "y4ops": "Yavin 4 Operations",
    "mwyhl": "Mind What You Have Learned",
    "no idea": "They Have No Idea We're Coming",
    "rtp": "Rescue The Princess",
    "thgg": "The Hyperdrive Generator's Gone (V)",
    "hyperdrive": "The Hyperdrive Generator's Gone (V)",
    "mbo": "Massassi Base Operations",
    "gungans": "Watch Your Step",
    "twin suns": "Twin Suns Of Tatooine",
    "tsot": "Twin Suns Of Tatooine",
    "jcc mains": "Coruscant: Jedi Council Chamber",
    "naboo gungans": "Watch Your Step",
    "rops": "Ralltiir Operations",
    "ropsv": "Ralltiir Operations (V)",
    "rops(v)": "Ralltiir Operations (V)",
    "diplomatic mission": "Diplomatic Mission To Alderaan",
    "there is good in him": "There Is Good In Him",
    "combat readiness v": "Combat Readiness (V)",
    "combat preparedness v": "Combat Preparedness (V)",
    "hb corvette quads": "Hidden Base",
    "hb corvette": "Hidden Base",
    "crv endor first order": "Combat Readiness (V)",
    "endor first order": "Combat Readiness (V)",
    "cpv jakku mains": "Combat Preparedness (V)",
    "hidden base mains": "Hidden Base",
    "naboo mains": "Watch Your Step",
    "hdadtj": "Hunt Down And Destroy The Jedi",
}

DS_FORCE = {
    "Senate Occupied",
    "No Money, No Parts, No Deal!",
    "Combat Readiness",
    "Combat Readiness (V)",
    "Endor Operations",
    "Imperial Entanglements",
    "I Want That Map",
    "Agents Of Black Sun",
    "Court Of The Vile Gangster",
    "Hunt Down And Destroy The Jedi",
    "ISB Operations",
    "Bring Him Before Me",
    "Carbon Chamber Testing",
    "Invasion",
    "My Kind Of Scum",
    "This Deal Is Getting Worse All The Time",
    "Set Your Course For Alderaan",
    "Ralltiir Operations",
    "Ralltiir Operations (V)",
}
LS_FORCE = {
    "Plead My Case To The Senate",
    "Watch Your Step",
    "Old Allies",
    "Diplomatic Mission To Alderaan",
    "Yavin 4: Massassi Throne Room",
    "Quiet Mining Colony",
    "Hidden Base",
    "You Can Either Profit By This",
    "He Is The Chosen One",
    "This Is Getting Out Of Hand",
    "We Have A Plan",
    "Rebel Strike Team",
    "Echo Base Operations",
    "Yavin 4 Operations",
    "Mind What You Have Learned",
    "They Have No Idea We're Coming",
    "Rescue The Princess",
    "The Hyperdrive Generator's Gone (V)",
    "Massassi Base Operations",
    "Combat Preparedness",
    "Combat Preparedness (V)",
    "There Is Good In Him",
}

EVENTS = [
    {
        "key": "18worlds",
        "wrap": "18worlds.html",
        "title": "2018 World Championship",
        "year": "2018",
        "tag": "2018-10",
        "dates": "4–7 October 2018",
        "site": "Morristown, New Jersey",
        "format": "[[Open]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2018 World Championship''' was the Players Committee World Championship in Morristown, New Jersey, 4–7 October 2018. [[Bastian Winkelhaus]] finished 1st in Day 3. Sixty-nine constructed pairs were published for Day 2.",
        "pc": "https://www.starwarsccg.org/2018-world-championships/",
        "deck_prefix": "2018 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
    },
    {
        "key": "18euro",
        "wrap": "18euro.html",
        "title": "2018 European Championship",
        "year": "2018",
        "tag": "2018-09",
        "dates": "21–23 September 2018",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Emil Wallin",
        "lead": "'''2018 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 21–23 September 2018. [[Emil Wallin]] finished 1st in Day 3.",
        "pc": "https://www.starwarsccg.org/2018-european-championships/",
        "deck_prefix": "2018 European Championship",
        "list_label": "European Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
    },
    {
        "key": "18nats",
        "wrap": "18nats.html",
        "title": "2018 U.S. National Championship",
        "year": "2018",
        "tag": "2018-07",
        "dates": "27–29 July 2018",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Tom Haid",
        "lead": "'''2018 U.S. National Championship''' was the Players Committee U.S. National Championship, 27–29 July 2018. [[Tom Haid]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2018-us-nationals/",
        "deck_prefix": "2018 US Nationals",
        "list_label": "U.S. National Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "18egp",
        "wrap": "18egp.html",
        "title": "2018 Endor Grand Prix",
        "year": "2018",
        "tag": "2018-05",
        "dates": "4–6 May 2018",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Lenny Rubin",
        "lead": "'''2018 Endor Grand Prix''' was a Players Committee major event, 4–6 May 2018. [[Lenny Rubin]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2018-endor-grand-prix/",
        "deck_prefix": "2018 EGP",
        "list_label": "Endor Grand Prix",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "18eumpc",
        "wrap": "18eumpc.html",
        "title": "2018 European Match Play Championship",
        "year": "2018",
        "tag": "2018-02",
        "dates": "17 February 2018",
        "site": "Europe",
        "format": "[[Open]]",
        "winner": "Kevin Jaap",
        "lead": "'''2018 European Match Play Championship''' was the Players Committee European match-play championship, 17 February 2018. [[Kevin Jaap]] is published first on the results list.",
        "pc": "https://www.starwarsccg.org/2018-european-match-play-championships/",
        "deck_prefix": "2018 European MPC",
        "list_label": "European Match Play Championship",
        "stages": [("list", "Results")],
    },
    {
        "key": "18mpc",
        "wrap": "18mpc.html",
        "title": "2018 Match Play Championship",
        "year": "2018",
        "tag": "2018-01",
        "dates": "5–7 January 2018",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Reid Smith",
        "lead": "'''2018 Match Play Championship''' was the Players Committee match-play championship, 5–7 January 2018. [[Reid Smith]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2018-match-play-championships/",
        "deck_prefix": "2018 MPC",
        "list_label": "Match Play Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "18ocs",
        "wrap": "",
        "title": "2018 Online Championship Series",
        "year": "2018",
        "tag": "2018-12",
        "dates": "2018",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2018 Online Championship Series''' was the Players Committee online championship series on GEMP. [[Justin Desai]] is the published winner. Constructed pair lists for the playoffs were not posted on the later wrap pages.",
        "pc": "https://www.starwarsccg.org/major-event-winners/",
        "deck_prefix": "2018 OCS",
        "list_label": "Online Championship Series",
        "stages": [],
        "stub_only": True,
    },
    {
        "key": "17tmw",
        "wrap": "17tmw.html",
        "title": "2017 Texas Mini Worlds",
        "year": "2017",
        "tag": "2017-10",
        "dates": "20–22 October 2017",
        "site": "Texas",
        "format": "[[Open]]",
        "winner": "Steve Baroni",
        "lead": "'''2017 Texas Mini Worlds''' was a Players Committee match-play major, 20–22 October 2017. [[Steve Baroni]] is published first on the Day 2 list.",
        "pc": "https://www.starwarsccg.org/2017-texas-mini-worlds/",
        "deck_prefix": "2017 Texas Mini Worlds",
        "list_label": "Texas Mini Worlds",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "17euro",
        "wrap": "17euro.html",
        "title": "2017 European Championship",
        "year": "2017",
        "tag": "2017-09",
        "dates": "8–10 September 2017",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2017 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 8–10 September 2017. [[Bastian Winkelhaus]] finished 1st in Day 3.",
        "pc": "https://www.starwarsccg.org/2017-european-championships/",
        "deck_prefix": "2017 European Championship",
        "list_label": "European Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
    },
    {
        "key": "17worlds",
        "wrap": "17worlds.html",
        "title": "2017 World Championship",
        "year": "2017",
        "tag": "2017-08",
        "dates": "10–13 August 2017",
        "site": "Bloomington, Minnesota",
        "format": "[[Open]]",
        "winner": "Phil Aasen",
        "lead": "'''2017 World Championship''' was the Players Committee World Championship in Bloomington, Minnesota, 10–13 August 2017. [[Phil Aasen]] finished 1st in Day 3. Day 2 published fifty-five constructed pairs plus four drops.",
        "pc": "https://www.starwarsccg.org/2017-world-championships/",
        "deck_prefix": "2017 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
    },
    {
        "key": "17nats",
        "wrap": "",
        "title": "2017 U.S. National Championship",
        "year": "2017",
        "tag": "2017-06",
        "dates": "23–25 June 2017",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Chris Kelly",
        "lead": "'''2017 U.S. National Championship''' was the Players Committee U.S. National Championship, 23–25 June 2017. [[Chris Kelly]] is published first on the Day 2 list.",
        "pc": "https://www.starwarsccg.org/resources/tournament-decklists/",
        "deck_prefix": "2017 US Nationals",
        "list_label": "U.S. National Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
        "inline": True,
    },
    {
        "key": "17egp",
        "wrap": "",
        "title": "2017 Endor Grand Prix",
        "year": "2017",
        "tag": "2017-05",
        "dates": "5–7 May 2017",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Tom Kelly",
        "lead": "'''2017 Endor Grand Prix''' was a Players Committee major event, 5–7 May 2017. [[Tom Kelly]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/resources/tournament-decklists/",
        "deck_prefix": "2017 EGP",
        "list_label": "Endor Grand Prix",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
        "inline": True,
    },
    {
        "key": "17mpc",
        "wrap": "17mpc.html",
        "title": "2017 Match Play Championship",
        "year": "2017",
        "tag": "2017-01",
        "dates": "6–8 January 2017",
        "site": "Princeton, New Jersey",
        "format": "[[Open]]",
        "winner": "Jonny Chu",
        "lead": "'''2017 Match Play Championship''' was the Players Committee match-play championship in Princeton, New Jersey, 6–8 January 2017. [[Jonny Chu]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/match-play-championship/",
        "deck_prefix": "2017 MPC",
        "list_label": "Match Play Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
]


def canon(name: str) -> str:
    name = re.sub(r"\s+", " ", name or "").strip().strip(",")
    name = name.replace("’", "'").replace("\u2019", "'").replace("\u2018", "'")
    if name in CANON:
        return CANON[name]
    if name in TOKEN:
        return TOKEN[name]
    return name


def map_slang(raw: str, side: str | None = None) -> str | None:
    if not raw:
        return None
    s = htmlmod.unescape(raw)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    s = s.replace("’", "'").replace("\u2019", "'")
    k0 = s.lower().strip()
    if k0 in ("day 1", "day 2", "day 3", "drops", "results"):
        return None
    k1 = re.sub(r"\s+", " ", k0.replace("(", "").replace(")", "")).strip()
    k2 = re.sub(
        r"\s+(mains|quads|sandwhirl|b-wings|bwings|tanks|racing|ig-88|ig 88|ansb|lsjk|corvette)$",
        "",
        k1,
    ).strip()
    dest = None
    for key in (k0, k1, k2):
        if key in SLANG:
            dest = SLANG[key]
            break
        if key in hm.SLANG_HUB:
            dest = hm.SLANG_HUB[key]
            if dest == "There Is No Try":
                dest = "Endor Operations"
            if dest == "Watto's Box":
                dest = "No Money, No Parts, No Deal!"
            break
    if not dest:
        return None
    if side == "DS" and dest == "Plead My Case To The Senate":
        dest = "Senate Occupied"
    if side == "LS" and dest == "Senate Occupied":
        dest = "Plead My Case To The Senate"
    if side == "DS" and dest == "Combat Preparedness":
        dest = "Combat Readiness"
    if side == "LS" and dest == "Combat Readiness":
        dest = "Combat Preparedness"
    return dest


def wrap_visible(raw: str) -> str:
    m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]+?)Posted in", raw, re.I)
    if not m:
        m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]{0,40000})", raw, re.I)
    s = m.group(1) if m else raw
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n", s, flags=re.I)
    s = re.sub(r"</h[1-6]>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = re.sub(r"[ \t]+", " ", s)
    return "\n".join(ln.strip() for ln in s.splitlines() if ln.strip())


def heading_stage(line: str) -> str | None:
    tl = line.strip().lower()
    tl = re.sub(r"^results\s+", "", tl).strip(" :-")
    if re.match(r"^day\s*3$", tl):
        return "d3"
    if re.match(r"^day\s*2$", tl):
        return "d2"
    if re.match(r"^day\s*1$", tl):
        return "d1"
    if re.match(r"^drops?$", tl):
        return "drop"
    if re.match(r"^results$", tl):
        return None
    return None


CHROME = {
    "skip to content",
    "volunteer",
    "forum",
    "card search",
    "play",
    "print cards",
    "menu",
    "home",
    "about us",
    "news",
    "store",
    "media",
    "podcasts",
    "videos",
    "tournaments",
    "cube",
    "rules",
    "collecting",
    "donations",
    "posts navigation",
    "scroll to top",
    "the games",
    "the players committee",
    "org chart",
    "player locator",
    "new & returning players",
    "awards and hall of fame",
    "star wars ccg",
    "swccg formats",
    "swccg rules",
    "swccg faq",
}

ROW = re.compile(
    r"^(?:\(?(\d{1,2})\)?[.\)\]]?\s*)?([A-Za-z][A-Za-z .'\-éøæåüßẞÖöÄäÜÉØÆÅ/_().]+?)\s+[–—]\s+(.+)$"
)
NAME_ONLY_NUM = re.compile(
    r"^\(?(\d{1,2})\)?[.\)\]]\s*([A-Za-z][A-Za-z .'\-éøæåüßẞÖöÄäÜÉØÆÅ/_().]+?)\s*$"
)
SKIP_NAMES = {
    "sandwhirl",
    "results",
    "decklist pdfs",
    "day 1",
    "day 2",
    "day 3",
}


def explode_rows(text: str) -> str:
    text = re.sub(r"\s+((?:Day|DAY)\s*[123])\b", r"\n\1", text)
    text = re.sub(r"\s+(Drops?)\b", r"\n\1", text)
    text = re.sub(r"\s+(\(?\d{1,2}\)[.\)]\s*)", r"\n\1", text)
    return text


def parse_text(text: str, default_stage: str = "list"):
    text = explode_rows(text)
    stage = None
    out = defaultdict(list)
    dest = defaultdict(dict)
    place_n = defaultdict(int)

    def keep(p: str) -> bool:
        if not p or " " not in p:
            return False
        if is_junk_player(p) or p.lower() in CHROME or p.lower() in SKIP_NAMES:
            return False
        return True

    def assign(stage_k, p, ds, ls, fin):
        if p not in out[stage_k]:
            out[stage_k].append(p)
        dest[stage_k][p] = (ds, ls, fin)

    for ln in text.splitlines():
        hs = heading_stage(ln)
        if hs:
            stage = hs
            continue
        if not stage:
            if " – " in ln or " — " in ln:
                stage = default_stage
            else:
                continue
        m = ROW.match(ln)
        if not m:
            m3 = NAME_ONLY_NUM.match(ln)
            if m3:
                p = canon(m3.group(2))
                if keep(p):
                    place_n[stage] += 1
                    assign(stage, p, None, None, int(m3.group(1)))
                continue
            m2 = re.match(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z'.\-]+)+)$", ln)
            if m2 and default_stage == "list":
                p = canon(m2.group(1))
                if keep(p):
                    place_n[stage] += 1
                    assign(stage, p, None, None, place_n[stage])
            continue
        place, name, rest = m.groups()
        p = canon(name)
        if not keep(p):
            continue
        parts = re.split(r"\s+[–—-]\s+", rest)
        ds_raw = parts[0].strip() if parts else ""
        ls_raw = parts[1].strip() if len(parts) > 1 else ""
        if len(parts) >= 3:
            ls_raw = parts[-1].strip()
        ds = map_slang(ds_raw, "DS")
        ls = map_slang(ls_raw, "LS")
        if ds in LS_FORCE and ds not in DS_FORCE:
            if ls in DS_FORCE and ls not in LS_FORCE:
                ds, ls = ls, ds
            elif not ls:
                ls, ds = ds, None
        if ls in DS_FORCE and ls not in LS_FORCE and not ds:
            ds, ls = ls, None
        if ds and ds in LS_FORCE and ds not in DS_FORCE and ls == ds:
            ds = None
        if ls and ls in DS_FORCE and ls not in LS_FORCE and ds == ls:
            ls = None
        place_n[stage] += 1
        fin = int(place) if place else place_n[stage]
        assign(stage, p, ds, ls, fin)
    return out, dest


NATS_2017 = """
Day 1
(1) Reid Smith – Coruscant CRv – TRM
(2) Matthew Carulli – Coruscant CRv – Diplo
(3) Chris Kelly – Court – TRM
(4) Matt Scott – TTO – Hidden Base
(5) Justin Carulli – Invasion – TRM
(6) Lenny Rubin – Court – Jakku CPv
(7) Greg Shaw – Imperial Entanglements – Jakku CPv
(8) Tom Haid – Court – EBO
Andy Wexstten – Endor Ops – Old Allies
Bill Kafer – ISB – Jakku CPv
Brian Fred – TTO – Hidden Base
Brian Speight – AOBS – WYS
Cal Aldred – Imperial Entanglements – QMC
Casey Anis – Invasion – TRM
Chris Gogolen – Court – Diplo
Colin Wellborn – ISB – MBO
Greyson Thompson – Imperial Entanglements – EBO
Jeremy DiPaolo – Imperial Entanglements – Old Allies
John Veasey – Watto – WYS
Jon McFarland – CCT Scum – WYS
Josh Mack – Coruscant CRv – Jakku CPv
Kyle Szklenski – Imperial Entanglements – Old Allies
Michael Tomashewski – BHBM – Jakku CPv
Mike Kessling – Court – WYS
Ming Huo – ISB – TRM
Pat Johnson – BHBM – WHAP
Ryan Obman – TDIGWATT – QMC
Shawn Dickson – Imperial Entanglements – Old Allies
Tim Culver – Invasion – WYS
Trevor Partridge – CCT – Diplo
Vikram Bali – Endor Ops – TRM
Vinny Rossi – Endor Ops – WYS
Day 2
Chris Kelly – Court – TRM
Reid Smith – Hunt Down – TRM
Matt Scott – Coruscant CRv – Hidden Base
Greg Shaw – Imperial Entanglements – Jakku CPv
Matthew Carulli – Coruscant CRv – TRM
Justin Carulli – Court – Diplo
Lenny Rubin – ISB – Jakku CPv
Tom Haid – Imperial Entanglements – Diplo
"""

EGP_2017 = """
Day 1
(1) Tom Kelly – Imperial Entanglements – Watch Your Step
(2) Kyle Krueger – CCT – IG-88 – Watch Your Step
(3) Michael Erisman – HB Corvette Quads – CRv Endor First Order
(4) Greg Shaw – TTO – Profit
(5) Mike French – TTO – QMC
(6) Matt Thornton – Court Scum – HB Mains
(7) Matt Sokol – Black Sun – TRM
(8) Joe Phillips – Hoth Tractor Beams – Hidden Base
Chris Wirfs – Endor Operations – Diplomatic Mission
Ryan Jellison – ISB – Hidden Base
Steve Harpster – Endor Operations – Diplomatic Mission
Amar Banger – Invasion – TRM
Jan Westergard – Black Sun – Watch Your Step
Cyrus Morosoff – Court – Old Allies
Mike Turner – CCT – EBO
Brandon Romano – Black Sun – QMC
Lenny Rubin – ISB – Old Allies
Alexander Sheynis – BHBM – EBO
Gibson Yim – Hunt Down – Watch Your Step
Jacy Smith – Hunt Down – Diplomatic Mission
Brandon Baity – Maul Mains – There Is Good In Him
Jeremy Gardner – Black Sun – Profit
Jerry Heine – Imperial Entanglements – TRM
Phil Aasen – Imperial Entanglements – TRM
Matt Wadden – EOps – Jakku CPv
Mark Sebring – Court – Diplomatic Mission
David Beaubier – SYCFA – Profit
Travis Egan – BHBM – TRM
Day 2
1. Tom Kelly – Imperial Entanglements – Old Allies
2. Matt Sokol – Black Sun – WHAP
3. Michael Erisman – Lightsaber Combat Podracing – Diplomatic Mission
4. Mike French – TTO – QMC
5. Kyle Krueger – TTO – Old Allies
6. Greg Shaw – TTO – CPv Jakku mains
7. Matt Thornton – Court – Hidden Base Mains
8. Joe Phillips – Tatooine Tractor Beams – QMC
"""


def accordion_nats_egp():
    return {"17nats": NATS_2017, "17egp": EGP_2017}


def emit_deck_page(title: str, player: str, side: str, obj: str, stage_lab: str, meta: dict):
    env = meta["format"]
    src = meta["pc"]
    side_word = "Dark" if side == "DS" else "Light"
    obj_link = f"[[{obj}]]" if obj else "—"
    body = f"""'''{title}''' was the {side_word} Side constructed list played by [[{player}]] at [[{meta['title']}]] ({stage_lab}).

== Deck info ==

* '''Starting Card:''' {obj_link}
* '''Format:''' {env}
* '''Stage:''' {stage_lab}
* '''Source:''' [{src} PC list]

== See also ==

* [[{meta['title']}]]
* [[{player}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{src} {meta['title']}], starwarsccg.org

{refs()}

[[Category:Decklists]]
[[Category:{meta['year']}]]
"""
    (PAGES / wiki_fname(title)).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def people_table(heading, players, dt, hl, stage, dest_fin):
    bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
    for p in players:
        rec = dest_fin.get(p) or (None, None, None)
        if len(rec) < 3:
            rec = (
                rec[0] if rec else None,
                rec[1] if rec and len(rec) > 1 else None,
                None,
            )
        fin = rec[2]
        fin_s = str(fin) if fin else "—"
        ds_page = dt.get((p, stage, "DS"))
        ls_page = dt.get((p, stage, "LS"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        bits += ["|-", f"| {fin_s} || [[{p}]] || {ds} || {ls}"]
    bits.append("|}")
    return "\n".join(bits)


def write_hub(meta, by_stage, dest, dt, hl):
    secs = []
    for stage, heading in meta.get("stages") or []:
        players = by_stage.get(stage) or []
        if not players:
            continue
        note = ""
        if heading == "Day 1":
            note = "Published constructed lists (every published pair, not Top 8 only).\n\n"
        elif heading == "Results":
            note = "Published constructed list in wrap order.\n\n"
        tbl = people_table(heading, players, dt, hl, stage, dest.get(stage) or {})
        secs.append(f"== {heading} ==\n\n{note}{tbl}\n")
    if meta.get("key") == "17worlds" and by_stage.get("drop"):
        tbl = people_table("Drops", by_stage["drop"], dt, hl, "drop", dest.get("drop") or {})
        secs.append(f"== Drops ==\n\nPublished constructed pairs listed as drops on the wrap.\n\n{tbl}\n")
    body_sec = "\n".join(secs)
    if not body_sec:
        body_sec = ""
    body = f"""{meta["lead"]}<ref name="pc">{meta["pc"]}</ref>

== Format ==

* '''Environment:''' {meta["format"]}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}
* '''Winner:''' [[{meta["winner"]}]]

{body_sec}
== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [{meta["pc"]} PC results]

== Sources ==

* [{meta["pc"]} {meta["title"]}], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{meta["year"]}]]
"""
    (PAGES / wiki_fname(meta["title"])).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def patch_list(year_rows):
    text = LIST.read_text(encoding="utf-8")
    for year in ("2018", "2017"):
        rows = year_rows.get(year) or []
        if not rows:
            continue
        section = f"""== {year} ==

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{chr(10).join(rows)}
|}}

"""
        if f"== {year} ==" in text:
            text = re.sub(
                rf"== {year} ==.*?(?=\n== )",
                section,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.replace(
                "== Decipher World Championships ==",
                section + "== Decipher World Championships ==",
                1,
            )
        if f"[[Category:{year}]]" not in text:
            text = text.replace("[[Category:2019]]", f"[[Category:2019]]\n[[Category:{year}]]")
    LIST.write_text(text, encoding="utf-8", newline="\n")
    if EC.exists():
        et = EC.read_text(encoding="utf-8")
        et = et.replace(
            "| 2018 || 2018 European Championship || — || — || —",
            "| 2018 || [[2018 European Championship]] || Bochum, Germany || [[Open]] || [[Emil Wallin]]",
        )
        et = et.replace(
            "| 2017 || 2017 European Championship || — || — || [[Bastian Winkelhaus]]",
            "| 2017 || [[2017 European Championship]] || Bochum, Germany || [[Open]] || [[Bastian Winkelhaus]]",
        )
        EC.write_text(et, encoding="utf-8", newline="\n")


def upsert_player(player, rows, meta):
    if is_junk_player(player):
        return None
    dest_stub = STUBS / (player.replace(" ", "_") + ".wiki")
    bio = PAGES / (player.replace(" ", "_") + ".wiki")
    cat = f"[[Category:{meta['year']}]]"
    if bio.exists() and is_bio(bio.read_text(encoding="utf-8", errors="replace")):
        text = bio.read_text(encoding="utf-8")
        text = re.sub(rf"\|-\s*\n\| [^\n]*\[\[{re.escape(meta['title'])}\]\][^\n]*\n", "", text)
        if "|}" in text and "Tournament Results" in text:
            text = text.replace("|}\n", "\n".join(rows) + "\n|}\n", 1)
        if cat not in text:
            text = text.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
        bio.write_text(text, encoding="utf-8", newline="\n")
        tidy_player_page(bio)
        return (player, f"pages/{bio.name}")
    upsert_stub(player, rows, meta["title"], meta["pc"])
    if dest_stub.exists():
        st = dest_stub.read_text(encoding="utf-8")
        if cat not in st:
            st = st.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
            dest_stub.write_text(st, encoding="utf-8", newline="\n")
        tidy_player_page(dest_stub)
        return (player, f"pages/player-stubs/{dest_stub.name}")
    return None


def main():
    STUBS.mkdir(parents=True, exist_ok=True)
    acc = accordion_nats_egp()
    titles = []
    list_rows = defaultdict(list)
    STAGE_LAB = {"d3": "Day 3", "d2": "Day 2", "d1": "Day 1", "list": "Results", "drop": "Drops"}

    for meta in EVENTS:
        by_stage = defaultdict(list)
        dest = defaultdict(dict)
        if meta.get("stub_only"):
            write_hub(meta, {}, {}, {}, {})
            titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))
            list_rows[meta["year"]].append(
                f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || [[{meta['winner']}]]"
            )
            print("stub", meta["title"])
            continue
        text = ""
        if meta.get("wrap"):
            path = WRAP / meta["wrap"]
            if path.exists():
                text = wrap_visible(path.read_text(encoding="utf-8", errors="replace"))
        if meta["key"] in acc:
            text = acc[meta["key"]]
        default = "list" if meta["key"] in ("18eumpc",) else "d2"
        parsed_stage, parsed_dest = parse_text(text, default)
        for st, names in parsed_stage.items():
            by_stage[st] = names
            dest[st] = parsed_dest[st]
        # remap list → first stage if needed
        if "list" in by_stage and meta["key"] == "18eumpc":
            pass
        dt, hl = {}, {}
        for stage, heading in meta.get("stages") or []:
            for i, p in enumerate(by_stage.get(stage) or [], 1):
                rec = dest.get(stage, {}).get(p)
                if rec and len(rec) == 3:
                    ds, ls, fin = rec
                elif rec and len(rec) == 2:
                    ds, ls = rec
                    fin = i
                    dest[stage][p] = (ds, ls, fin)
                else:
                    ds = ls = None
                    fin = i
                    dest[stage][p] = (None, None, fin)
                lab = STAGE_LAB.get(stage, heading)
                if ds:
                    title = f"{meta['deck_prefix']} {'' if lab == 'Day 1' else lab + ' '}{p} DS {ds}".replace("  ", " ").strip()
                    title = re.sub(r"[#<>\[\]\|\{\}?*\"]", "", title)
                    emit_deck_page(title, p, "DS", ds, lab, meta)
                    dt[(p, stage, "DS")] = title
                    hl[title] = ds
                    titles.append((title, f"pages/{wiki_fname(title)}"))
                if ls:
                    title = f"{meta['deck_prefix']} {'' if lab == 'Day 1' else lab + ' '}{p} LS {ls}".replace("  ", " ").strip()
                    title = re.sub(r"[#<>\[\]\|\{\}?*\"]", "", title)
                    emit_deck_page(title, p, "LS", ls, lab, meta)
                    dt[(p, stage, "LS")] = title
                    hl[title] = ls
                    titles.append((title, f"pages/{wiki_fname(title)}"))
        if meta["key"] == "17worlds":
            for p in by_stage.get("drop") or []:
                rec = dest.get("drop", {}).get(p)
                ds = rec[0] if rec else None
                ls = rec[1] if rec else None
                for side, obj in (("DS", ds), ("LS", ls)):
                    if not obj:
                        continue
                    title = f"{meta['deck_prefix']} Drops {p} {side} {obj}"
                    title = re.sub(r"[#<>\[\]\|\{\}?*\"]", "", title)
                    emit_deck_page(title, p, side, obj, "Drops", meta)
                    dt[(p, "drop", side)] = title
                    hl[title] = obj
                    titles.append((title, f"pages/{wiki_fname(title)}"))

        write_hub(meta, by_stage, dest, dt, hl)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))

        by_p = defaultdict(list)
        for stage, heading in (meta.get("stages") or []) + ([("drop", "Drops")] if meta["key"] == "17worlds" else []):
            for p in by_stage.get(stage) or []:
                by_p[p].append(stage)
        rank = {"d3": 0, "d2": 1, "list": 1, "d1": 2, "drop": 3}
        for p, stages in by_p.items():
            rows = []
            for stage in sorted(set(stages), key=lambda s: rank.get(s, 9)):
                lab = STAGE_LAB.get(stage, stage)
                ev = f"[[{meta['title']}]] ({lab})" if lab not in ("Day 1", "Results") else f"[[{meta['title']}]]"
                rec = dest.get(stage, {}).get(p)
                fin = rec[2] if rec and len(rec) == 3 else "—"
                ds_page = dt.get((p, stage, "DS"))
                ls_page = dt.get((p, stage, "LS"))
                ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
                ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
                rows.append(
                    f"|- \n| {meta['dates']} || {ev} || {meta['format']} || {fin} || {ds} || {ls}"
                )
            got = upsert_player(p, rows, meta)
            if got:
                titles.append(got)
        list_rows[meta["year"]].append(
            f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || [[{meta['winner']}]]"
        )
        print(
            "event",
            meta["title"],
            {k: len(v) for k, v in by_stage.items()},
        )

    def tag_key(row: str) -> str:
        m = re.search(r"\| (\d{4}-\d{2})", row)
        return m.group(1) if m else ""

    for year in list_rows:
        list_rows[year] = sorted(list_rows[year], key=tag_key, reverse=True)
    patch_list(list_rows)
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("European Championships", "pages/European_Championships.wiki"))

    seen = set()
    lines = []
    for title, rel in titles:
        if title in seen:
            continue
        seen.add(title)
        lines.append(f"{title}\t{rel}")
    TSV.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("TSV", TSV, "n", len(lines))


if __name__ == "__main__":
    main()
