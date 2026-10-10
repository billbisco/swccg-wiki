#!/usr/bin/env python3
"""Dest remaining Decipher Deck Designs 60s (tournament hubs + general pages + GEMP)."""
from __future__ import annotations

import html as htmlmod
import json
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

from decipher_notes import inject_strategy, parse_article_notes
from generate_decipher_worlds import CATS, PAGES, TITLES, slug_file, write_page
from gemp_importable import (
    ARCHETYPE_ABBR,
    FORMAT_ABBR,
    TITLE_ALIAS,
    deck_name,
    last_name,
    lookup,
    safe_deck_filename,
    wiki_download_line,
    xml_for,
)

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "decipher-decks"
INDEX_HTML = Path(r"C:\Users\gythe\AppData\Local\Temp\decipher-index-20010608.html")
if not INDEX_HTML.exists():
    INDEX_HTML = ROOT / "decipher-decks" / "index-20010608.html"
CDX_PATH = ROOT / "decipher-decks" / "cdx.txt"
GEMP_OUT = ROOT / "gemp-import-designs"
IDX = "https://web.archive.org/web/20010608205634/http://www.decipher.com/starwars/deckdesigns/index.html"
WB = "https://web.archive.org/web/{ts}id_/http://www.decipher.com/starwars/deckdesigns/{slug}"
_CDX: dict[str, str] | None = None

SKIP_DEST = {
    "102000lightsokol.html",
    "102000darksokol.html",
    "102300lightlapointe.html",
    "102300darklapointe.html",
    "110600lightasselin.html",
    "110700darkasselin.html",
    "111500lightfeldman.html",
    "111500darkfeldman.html",
    "121099laffertylight.html",
    "121399laffertydark.html",
    "111699worldchamplight.html",
    "111699worldchampdark.html",
    "111899worldrunneruplight.html",
    "111899worldrunnerupdark.html",
    "jacobslightdeck.html",
    "jacobsdarkdeck.html",
    "ribouletlightdeck.html",
    "ribouletdarkdeck.html",
    "worldchamplight.html",
    "worldchampdark.html",
}

# Already dested Worlds pages (do not overwrite card lists).
EXISTING_DEST = {
    "102000lightsokol.html": "2000 Decipher World Championship Matt Sokol LS",
    "102000darksokol.html": "2000 Decipher World Championship Matt Sokol DS",
    "102300lightlapointe.html": "2000 Decipher World Championship Yannick Lapointe LS",
    "102300darklapointe.html": "2000 Decipher World Championship Yannick Lapointe DS",
    "110600lightasselin.html": "2000 Decipher World Championship Raphael Asselin LS",
    "110700darkasselin.html": "2000 Decipher World Championship Raphael Asselin DS",
    "111500lightfeldman.html": "2000 Decipher World Championship Paul Todd Feldman LS",
    "111500darkfeldman.html": "2000 Decipher World Championship Paul Todd Feldman DS",
    "121099laffertylight.html": "1999 Decipher World Championship James Lafferty LS",
    "121399laffertydark.html": "1999 Decipher World Championship James Lafferty DS",
    "111699worldchamplight.html": "1999 Decipher World Championship Gary Carman LS",
    "111699worldchampdark.html": "1999 Decipher World Championship Gary Carman DS",
    "111899worldrunneruplight.html": "1999 Decipher World Championship Steven Lewis LS",
    "111899worldrunnerupdark.html": "1999 Decipher World Championship Steven Lewis DS",
    "jacobslightdeck.html": "1997 Decipher World Championship Philipp Jacobs LS",
    "jacobsdarkdeck.html": "1997 Decipher World Championship Philipp Jacobs DS",
    "ribouletlightdeck.html": "1997 Decipher World Championship Michael Riboulet LS",
    "ribouletdarkdeck.html": "1997 Decipher World Championship Michael Riboulet DS",
    "worldchamplight.html": "1996 Decipher World Championship Raphael Asselin LS",
    "worldchampdark.html": "1996 Decipher World Championship Raphael Asselin DS",
}

PLAYER_CANON = {
    "M. Rossou": "Maarten Rossou",
    "Maarten Rossou": "Maarten Rossou",
    "G. Ferrara": "Gaetano Ferrara",
    "Gaetano Ferrara": "Gaetano Ferrara",
    "D. Bojanowski": "Dan Bojanowski",
    "Dan Bojanowski": "Dan Bojanowski",
    "N. Reisch": "Nathan Reisch",
    "Nathan Reisch": "Nathan Reisch",
    "C. Hays": "Clint Hays",
    "Clint Hays": "Clint Hays",
    "K. Reitzel": "Kevin Reitzel",
    "P. Feldman": "Paul Todd Feldman",
    "Paul Feldman": "Paul Todd Feldman",
    "Paul Feldman Squadron": "Paul Todd Feldman",
    "J. Alread": "Joe Alread",
    "B. Winkelhaus": "Bastian Winkelhaus",
    "Bastian Winkelhaus": "Bastian Winkelhaus",
    "Charles Hickey": "Charles Hickey",
    "M. Logghe": "Maarten Logghe",
    "S. Lewis": "Steven Lewis",
    "J. Lafferty": "James Lafferty",
    "G. Carman": "Gary Carman",
    "P. Jacobs": "Philipp Jacobs",
    "Phillip Jacob": "Philipp Jacobs",
    "M. Riboulet": "Michael Riboulet",
    "R. Asselin": "Raphael Asselin",
    "J. VanderMeer": "Jon VanDerMeer",
    "Jon VanderMeer": "Jon VanDerMeer",
    "A. Divers": "Allen Divers",
    "T. Lischke": "Tom Lischke",
    "J. Winter": "Jason Winter",
    "S. Wible": "Sandy Wible",
    "Sandy Wible": "Sandy Wible",
    "R. Harmon": "Richard Harmon",
    "J. Woodland": "Jon Woodland",
    "S. McFadden": "Steve McFadden II",
    "Steve McFadden": "Steve McFadden II",
    "N. Olson": "Nels Olson",
    "Nels Olson": "Nels Olson",
    "J. Kilby": "Jason Kilby",
    "Jason Kilby": "Jason Kilby",
    "Donald Snider": "Donald Snider",
    "M. Salven": "Max Salven",
    "Max Salven": "Max Salven",
    "A. Long": "Aldrin Long",
    "Aldrin Long": "Aldrin Long",
    "D. Harvilla": "Douglas Harvilla",
    "Douglas Harvilla": "Douglas Harvilla",
    "R. Bordier": "Ray Bordier",
    "Ray Bordier": "Ray Bordier",
    "T. Sokol": "Tom Sokol",
    "Tom Sokol": "Tom Sokol",
    "M. Dalton": "Mike Dalton",
    "Mike Dalton": "Mike Dalton",
    "N. Lhai": "Nhat Lai",
    "Nhat Lai": "Nhat Lai",
    "J. Markley": "Jason Markley",
    "Jason Markley": "Jason Markley",
    "J. Mornout": "Joe Mornout",
    "Joe Mornout": "Joe Mornout",
    "Joseph Mornout": "Joe Mornout",
    "T.J. Holman": "T.J. Holman",
    "T. J. Holman": "T.J. Holman",
    "C. Bozman": "Cole Bozman",
    "C. Boleman": "Cole Bozman",
    "Cole Bozman": "Cole Bozman",
    "B. Kallenbach": "Brian Kallenbach",
    "Brian Kallenbach": "Brian Kallenbach",
    "A. Liu": "Andrew Liu",
    "Andrew Liu": "Andrew Liu",
    "A. Lam": "Alex Lam",
    "J. Branson": "Josh Branson",
    "D. Deveau": "David Deveau",
    "M. Moghadam": "Matthew Moghadam",
    "I. Abyzov": "Ilya Abyzov",
    "M. Kalinovich": "Mike Kalinovich",
    "R. Terrio": "Rob Terrio",
    "T. Dewey": "Trevor Dewey",
    "J. Roberson": "John Roberson",
    "G. Christensen": "G. Christensen",
    "A. Giuliano": "Andrew Giuliano",
    "K. Kessenich": "Kyle Kessenich",
    "B. Helgeson": "Brett Helgeson",
    "J. Bader": "Josh Bader",
    "M. Emery": "Mike Emery",
    "M. Ehrhart": "Matt Ehrhart",
    "Matt Ehrhart": "Matt Ehrhart",
    "Matt Ehrhart Though": "Matt Ehrhart",
    "M. Falke": "Martin Falke",
    "T. Anfossi": "Tiuli Anfossi",
    "T. Dowlings": "Thomas Dowlings",
    "E. Taylor": "Eric Taylor",
    "L. Zisla": "Lloyd Zisla",
    "E. Witkowski": "Eric Witkowski",
    "G. Bole": "Greg Bole",
    "H. Kim": "Hak Soo Kim",
    "J. Kernodle": "J. Holt Kernodle",
    "J. Holt Kernodle": "J. Holt Kernodle",
    "J. Griswold": "Justin Griswold",
    "G. Marshall": "Greg Marshall",
    "S. Sutton": "Stephen Sutton",
    "M. Crosby": "Michael Crosby",
    "M. Smith": "Miles Smith",
    "B. Roth": "Blake Roth",
    "A. Wechsler": "Adam Wechsler",
    "Adam": "Adam Wechsler",
    "J. Trent": "John Trent",
    "John Trent": "John Trent",
    "C. Mortonson": "Chris Mortonson",
    "Chris Mortonson": "Chris Mortonson",
    "K. Schlichting": "Kurt Schlichting",
    "Kurt Schlichting": "Kurt Schlichting",
    "Donald Snider Intro": "Donald Snider",
    "R. Harter": "R. Harter",
    "Juliën Rivière": "Juliën Riviëre",
    "Juliën Riviëre": "Juliën Riviëre",
    "Julien Riviere": "Juliën Riviëre",
    "Joeri Hoste": "Joeri Hoste",
}

# Live dest titles that differ from the generator naming convention.
LIVE_TITLE = {
    "030801darkbrugge.html": "2001 Brugge Belgian Open Juliën Riviëre DS",
}

# Last-name collisions: dest as written (do not merge).
# R. Bordier vs Roy Bordier / Ray Bordier
# M. Dalton vs Dalton (2012)
# T. Sokol vs Matt Sokol

TOURNEY = {
    "ithorchampdeck.html": {
        "event": "1997 Kiffex Regionals",
        "dates": "August 1997",
        "fmt": "Premiere - Dagobah",
        "finish": "1st",
        "year": 1997,
        "token": "Kiffex",
        "tag": "1997-08",
    },
    "sullustlightdeck.html": {
        "event": "1997 Sullust Regionals",
        "dates": "October 1997",
        "fmt": "Premiere - Dagobah",
        "finish": "1st",
        "year": 1997,
        "token": "Sullust",
        "tag": "1997-10",
    },
    "sullustdarkdeck.html": {
        "event": "1997 Sullust Regionals",
        "dates": "October 1997",
        "fmt": "Premiere - Dagobah",
        "finish": "1st",
        "year": 1997,
        "token": "Sullust",
        "tag": "1997-10",
    },
    "0799haysoriginslight.html": {
        "event": "1999 Origins Open",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "Origins",
        "tag": "1999-07",
    },
    "0799haysoriginsdark.html": {
        "event": "1999 Origins Open",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "Origins",
        "tag": "1999-07",
    },
    "0799holmanoriginslight.html": {
        "event": "1999 Origins Open",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "Origins",
        "tag": "1999-07",
    },
    "0799holmanoriginsdark.html": {
        "event": "1999 Origins Open",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "Origins",
        "tag": "1999-07",
    },
    "072399markleylight.html": {
        "event": "1999 Wizards tournament",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "Wizards",
        "tag": "1999-07",
    },
    "072299markleydark.html": {
        "event": "1999 Wizards tournament",
        "dates": "July 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "Wizards",
        "tag": "1999-07",
    },
    "081999reischlight.html": {
        "event": "1999 GenCon Open",
        "dates": "August 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "GenCon",
        "tag": "1999-08",
    },
    "081999reischdark.html": {
        "event": "1999 GenCon Open",
        "dates": "August 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "GenCon",
        "tag": "1999-08",
    },
    "082099mornoutlight.html": {
        "event": "1999 GenCon Open",
        "dates": "August 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "GenCon",
        "tag": "1999-08",
    },
    "082099mornoutdark.html": {
        "event": "1999 GenCon Open",
        "dates": "August 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "GenCon",
        "tag": "1999-08",
    },
    "091099kilbylight.html": {
        "event": "1999 Endor Regionals",
        "dates": "September 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "EndorReg",
        "tag": "1999-09",
    },
    "091099kilbydark.html": {
        "event": "1999 Endor Regionals",
        "dates": "September 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "EndorReg",
        "tag": "1999-09",
    },
    "090999harvillalight.html": {
        "event": "1999 Endor Regionals",
        "dates": "September 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "EndorReg",
        "tag": "1999-09",
    },
    "090999harvilladark.html": {
        "event": "1999 Endor Regionals",
        "dates": "September 1999",
        "fmt": "Premiere - Endor",
        "finish": "2nd",
        "year": 1999,
        "token": "EndorReg",
        "tag": "1999-09",
    },
    "101999longlight.html": {
        "event": "1999 Outer Rim Regionals",
        "dates": "October 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "OuterRim",
        "tag": "1999-10",
    },
    "101899longdark.html": {
        "event": "1999 Outer Rim Regionals",
        "dates": "October 1999",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 1999,
        "token": "OuterRim",
        "tag": "1999-10",
    },
    "021000seattlegslight.html": {
        "event": "2000 Seattle Grand Slam",
        "dates": "February 2000",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 2000,
        "token": "Seattle",
        "tag": "2000-02",
    },
    "020900seattlegsdark.html": {
        "event": "2000 Seattle Grand Slam",
        "dates": "February 2000",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 2000,
        "token": "Seattle",
        "tag": "2000-02",
    },
    "042700lightbojanowski.html": {
        "event": "2000 Virginia State Championship",
        "dates": "April 2000",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 2000,
        "token": "VAState",
        "tag": "2000-04",
    },
    "042800darkbojanowski.html": {
        "event": "2000 Virginia State Championship",
        "dates": "April 2000",
        "fmt": "Premiere - Endor",
        "finish": "1st",
        "year": 2000,
        "token": "VAState",
        "tag": "2000-04",
    },
    "082300lightrossou.html": {
        "event": "2000 European Championship",
        "dates": "August 2000",
        "fmt": "Premiere - Death Star II",
        "finish": "2nd",
        "year": 2000,
        "token": "Euro",
        "tag": "2000-08",
    },
    "082800darkrossou.html": {
        "event": "2000 European Championship",
        "dates": "August 2000",
        "fmt": "Premiere - Death Star II",
        "finish": "2nd",
        "year": 2000,
        "token": "Euro",
        "tag": "2000-08",
    },
    "030801lightbrugge.html": {
        "event": "2001 Brugge Belgian Open",
        "dates": "March 2001",
        "fmt": "Premiere - Tatooine",
        "finish": "1st",
        "year": 2001,
        "token": "Brugge",
        "tag": "2001-03",
    },
    "030801darkbrugge.html": {
        "event": "2001 Brugge Belgian Open",
        "dates": "March 2001",
        "fmt": "Premiere - Tatooine",
        "finish": "—",
        "year": 2001,
        "token": "Brugge",
        "tag": "2001-03",
    },
}

# Index slug later overwritten on Decipher.com; every Wayback capture is Ferrara Sullust Light.
CONTENT_DUP = {
    "targetdark.html": "sullustlightdeck.html",
}

FMT_CODE = {
    "Premiere": "premiere",
    "Premiere - A New Hope": "premiere_anh",
    "Premiere - Hoth": "premiere_hoth",
    "Premiere - Dagobah": "premiere_dagobah",
    "Premiere - Cloud City": "premiere_cc",
    "Premiere - Jabba's Palace": "premiere_jp",
    "Premiere - Special Edition": "premiere_se",
    "Premiere - Endor": "premiere_endor",
    "Premiere - Death Star II": "premiere_ds2",
    "Premiere - Tatooine": "premiere_tatooine",
}

TYPE_ORDER = [
    "Objective",
    "Character",
    "Creature",
    "Device",
    "Weapon",
    "Starship",
    "Vehicle",
    "Location",
    "Effect",
    "Interrupt",
    "Jedi Test",
    "Admiral's Order",
    "Epic Event",
]

TYPE_WORD = (
    r"objectives?|characters?|locations?|sites?|effects?|interrupts?|"
    r"starships?|vehicles?|weapons?|creatures?|devices?|jedi tests?|"
    r"admiral'?s orders?|epic events?|start|starting|ships?|fleet"
)
HEADER_RE = re.compile(
    rf"^((?:{TYPE_WORD})(?:\s*/\s*(?:{TYPE_WORD}))*)\s*"
    r"[:.]?\s*[\[\(]?\s*(\d+)?\s*[\]\)]?\s*$",
    re.I,
)
CARD_X = re.compile(r"^(.*?)[\s]*[xX][\s]*(\d+)\s*$")
CARD_NX = re.compile(r"^(\d+)\s*[xX]\s+(.*)$")
SKIP_LINE = re.compile(
    r"^(thanks to|send us|beginner|intermediate|expert|light side|dark side|"
    r"star wars ccg|here are? |here's |this deck|i used|i played|content by|"
    r"some are serious|decipher\.com|top$|map$|tm\b|terms and usage|"
    r"all rights reserved|decipher inc|~+|world finals|other finalists|"
    r"enjoy!|notes?:|strategy:|how to |deck designs$)",
    re.I,
)
JUNK_NAMES = {
    "start",
    "starting",
    "objectives",
    "objective",
    "locations",
    "characters",
    "effects",
    "interrupts",
    "starships",
    "vehicles",
    "weapons",
    "fleet",
    "this",
    "here's",
    "here",
    "side",
    "light",
    "dark",
    "squadron",
    "thanks",
    "search",
    "map",
    "top",
}
NAME_TOKEN = r"[A-ZÀ-ÿ][A-Za-zÀ-ÿ.\-']+(?:\s+[A-ZÀ-ÿ][A-Za-zÀ-ÿ.\-']+){0,3}"
TRAIL_JUNK = re.compile(
    r"\s+(Objectives?|Locations?|Characters?|Start|Starting|Light|Dark|Side|"
    r"Effects?|Interrupts?|Starships?|In Game|Intro|First|And|Though|Well|"
    r"Squadron|Everyone|Here's|This|Hi|Ok)\b.*$",
    re.I,
)

OBJ_FACE = {
    "Hidden Base": "Hidden Base / Systems Will Slip Through Your Fingers",
    "Local Uprising": "Local Uprising / Liberation",
    "Hunt Down And Destroy The Jedi": (
        "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
    ),
    "ISB Operations": "ISB Operations / Empire's Sinister Agents",
    "Imperial Occupation": "Imperial Occupation / Imperial Control",
    "Mind What You Have Learned": "Mind What You Have Learned / Save You It Can",
    "Bring Him Before Me": "Bring Him Before Me / Take Your Father's Place",
    "Set Your Course For Alderaan": (
        "Set Your Course For Alderaan / The Ultimate Power In The Universe"
    ),
    "There Is Good In Him": "There Is Good In Him / I Can Save Him",
    "Ralltiir Operations": "Ralltiir Operations / In The Hands Of The Empire",
    "Endor Operations": "Endor Operations / Imperial Outpost",
    "Echo Base Operations": "Echo Base Operations / Massassi Base Operations",
    "Massassi Base Operations": "Massassi Base Operations / Echo Base Operations",
    "Watch Your Step": "Watch Your Step / This Place Can Be A Little Rough",
    "Court Of The Vile Gangster": "Court Of The Vile Gangster / Vile Gangsters",
    "Carbon Chamber Testing": "Carbon Chamber Testing / Cloud City Occupation",
    "My Kind Of Scum": "My Kind Of Scum / Fearless And Inventive",
    "You Cannot Hide Forever": "You Cannot Hide Forever / Mobilization Points",
    "That Thing's Operational": "That Thing's Operational / Death Star Operations",
    "Agents In The Court": "Agents In The Court / No Love For The Empire",
    "Agents Of Black Sun": "Agents Of Black Sun / Lucia's List",
    "Dantooine Base Operations": "Dantooine Base Operations / More Dangerous Than You Realize",
    "The Empire's Back": "The Empire's Back / Imperial Control",
}

DARK_SHARED = {"Alter", "Sense", "Control", "Undercover"}


def format_for_date(month: int, year: int) -> str:
    if year == 1996 and month <= 6:
        return "Premiere"
    if year == 1996:
        return "Premiere - A New Hope"
    if year == 1997 and month <= 4:
        return "Premiere - Hoth"
    if year == 1997 and month <= 11:
        return "Premiere - Dagobah"
    if year == 1997:
        return "Premiere - Cloud City"
    if year == 1998 and month <= 3:
        return "Premiere - Cloud City"
    if year == 1998 and month <= 10:
        return "Premiere - Jabba's Palace"
    if year == 1998 or (year == 1999 and month <= 5):
        return "Premiere - Special Edition"
    if year == 1999 or (year == 2000 and month <= 5):
        return "Premiere - Endor"
    return "Premiere - Death Star II"


def _slugs_from_index_html(html: str) -> set[str]:
    slugs = {s.lower() for s in re.findall(r'<OPTION VALUE="([^"]+)"', html, re.I)}
    slugs |= {
        s.lower()
        for s in re.findall(
            r'href="[^"]*/deckdesigns/([A-Za-z0-9._-]+\.html)"', html, re.I
        )
    }
    slugs.discard("")
    return slugs


def index_snapshot_slugs() -> set[str]:
    """Slugs the 8 June 2001 Deck Designs index linked (includes Brugge)."""
    return _slugs_from_index_html(INDEX_HTML.read_text(encoding="latin-1"))


def load_options() -> list[tuple[str, str, str, int, int]]:
    """(slug, label, side, month, year)"""
    html = INDEX_HTML.read_text(encoding="latin-1")
    opts = re.findall(r'<OPTION VALUE="([^"]+)">([^<]*)</OPTION>', html, re.I)
    out = []
    seen = set()
    light = True
    for val, label in opts:
        slug = val.strip()
        lab = htmlmod.unescape(re.sub(r"\s+", " ", label)).strip()
        if slug.lower() == "dotwswd.html" and slug.lower() in seen:
            # index copy-paste: same slug on LS and DS Wible rows
            pass
        m = re.match(r"(\d{2})/(\d{2})", lab)
        if m:
            month, yy = int(m.group(1)), int(m.group(2))
            year = 1900 + yy if yy >= 90 else 2000 + yy
            if month == 12 and yy == 7:
                year = 1997  # 12/07 Welcome to Mos Eisley is 12/97
                month = 12
        else:
            month, year = 0, 0
        side = "LIGHT" if light else "DARK"
        # heuristic: first 082800darkrossou starts dark block
        if slug.lower() == "082800darkrossou.html":
            light = False
            side = "DARK"
        elif light and "dark" in slug.lower() and slug.lower() not in {
            "ddeveaudark.html",
        }:
            pass
        key = slug.lower()
        if key in seen:
            # index copy-paste (dotwswd.html on both Wible rows); dest once
            continue
        out.append((slug, lab, side, month, year))
        seen.add(key)
        if slug.lower() == "yodaechobase.html":
            light = False
    return out


def ensure_cached_html(slug: str) -> str | None:
    """Read cache, or fetch the CDX Wayback snapshot once."""
    raw = read_cached_html(slug)
    if raw is not None:
        return raw
    url = wayback_url(slug)
    print("FETCH", slug, url)
    data = None
    last_err = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "swccg-wiki-notes/1.0"}
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            break
        except Exception as e:
            last_err = e
            print("FETCH_TRY", slug, attempt + 1, e)
            time.sleep(4 * (attempt + 1))
    if data is None:
        print("FETCH_FAIL", slug, last_err)
        return None
    if len(data) < 400:
        print("FETCH_SHORT", slug, len(data))
        return None
    (CACHE / slug.lower()).write_bytes(data)
    return read_cached_html(slug)


def read_cached_html(slug: str) -> str | None:
    path = CACHE / slug
    if not path.exists():
        path = CACHE / slug.lower()
    if not path.exists():
        return None
    data = path.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            raw = data.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raw = data.decode("latin-1", errors="replace")
    return (
        raw.replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u0092", "'")
        .replace("\u0091", "'")
        .replace("\u00d5", "'")
    )


def extract_content(raw: str) -> str:
    m = re.search(
        r"SWCCGmaincontent.*?-->(.*)(?:<!--\s*#EndEditable|</BODY>)",
        raw,
        re.I | re.S,
    )
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk, flags=re.I)
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</(p|div|tr|h[1-6]|li|blockquote)>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = htmlmod.unescape(chunk)
    lines = []
    for ln in chunk.split("\n"):
        s = re.sub(r"[ \t]+", " ", ln).strip()
        if s:
            lines.append(s)
    return "\n".join(lines)


def join_wraps(lines: list[str]) -> list[str]:
    """Rejoin Decipher HTML hard-wraps (qty on next line, split dual-titles)."""
    out: list[str] = []
    for ln in lines:
        if not out:
            out.append(ln)
            continue
        prev = out[-1]
        if HEADER_RE.match(prev) or HEADER_RE.match(ln):
            out.append(ln)
            continue
        if re.match(r"^[xX]\s*\d+$", ln) or re.match(r"^\[\d+\]$", ln):
            out[-1] = prev + " " + ln
            continue
        if prev.endswith("/") or (
            "/" in prev
            and " / " not in prev
            and len(prev.split("/")[-1].split()) < 2
        ):
            out[-1] = prev + " " + ln
            continue
        if re.search(r"(?i)\b(with|the|of|and|&|in|for|to|a|from)\s*$", prev):
            out[-1] = prev + " " + ln
            continue
        if ln[:1].islower() and ln[:1].isalpha():
            out[-1] = prev + " " + ln
            continue
        out.append(ln)
    return out


def parse_cards(text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    in_list = False
    lines = join_wraps([ln.strip() for ln in text.split("\n") if ln.strip()])
    for ln in lines:
        if HEADER_RE.match(ln):
            in_list = True
            continue
        if re.match(r"^strategy\s*:", ln, re.I):
            if in_list:
                break
            continue
        if SKIP_LINE.search(ln):
            if in_list and re.match(
                r"^(thanks to|content by|send us|tm\b|terms and usage|all rights reserved)",
                ln,
                re.I,
            ):
                break
            continue
        if not in_list:
            continue
        if re.match(
            r"^(see also|sources|references|send us|content by|how it works|"
            r"introduction:|conclusion:|strategies:|weaknesses:|about the author)\b",
            ln,
            re.I,
        ):
            break
        if re.search(r"how it works", ln, re.I) and len(ln.split()) > 4:
            break
        words = ln.split()
        if len(words) > 16 and "/" not in ln and ":" not in ln:
            break
        name = ln
        name = re.sub(r"\s*\((?:start|starts?|starting location)\)\s*$", "", name, flags=re.I)
        name = re.sub(r"([A-Za-z])\?{1,2}([A-Za-z])", r"\1'\2", name)
        name = re.sub(r"\s+[xX](\d+)v$", r" x\1", name)
        qty = 1
        m = CARD_NX.match(name)
        if m:
            qty = int(m.group(1))
            name = m.group(2).strip()
        else:
            m = CARD_X.match(name)
            if m and m.group(1).strip():
                name = m.group(1).strip()
                qty = int(m.group(2))
        name = re.sub(r"\s+", " ", name).strip(" .,;")
        name = re.sub(r"\s*:\s*", ": ", name)
        if not name or len(name) < 2:
            continue
        if name.lower() in JUNK_NAMES:
            continue
        if re.fullmatch(r"\d+", name) or re.fullmatch(r"[\(\[]?\d+[\)\]]?", name):
            continue
        if re.match(
            r"^(ships?|vehicles?|characters?|effects?|interrupts?)(\s*&\s*(ships?|vehicles?))?:?\s*\d*$",
            name,
            re.I,
        ):
            continue
        name = re.sub(r"([A-Za-z])\?{1,2}([A-Za-z])", r"\1'\2", name)
        name = re.sub(r"\s+x(\d+)v$", r" x\1", name, flags=re.I)
        if "/" in name and " / " not in name and not re.search(r"d['’]al", name, re.I):
            left, right = name.split("/", 1)
            if len(left.split()) >= 2 and len(right.split()) >= 2:
                name = left.strip()
        mplus = re.fullmatch(r"(.+?)\s+(\d+)\s+\+\s+(\d+)$", name)
        if mplus:
            pref = mplus.group(1).strip()
            rows.append((qty, f"{pref} {mplus.group(2)}"))
            rows.append((qty, f"{pref} {mplus.group(3)}"))
            continue
        split_m = None
        if re.search(r"\s+and\s+", name, re.I) and " / " not in name:
            split_m = re.split(r"\s+and\s+", name, maxsplit=1, flags=re.I)
        elif re.search(r"\s+or\s+", name, re.I) and " / " not in name:
            split_m = re.split(r"\s+or\s+", name, maxsplit=1, flags=re.I)
        if split_m and len(split_m) == 2:
            left, right = split_m[0].strip(), split_m[1].strip()
            if 2 <= len(left.split()) <= 4 and 2 <= len(right.split()) <= 4:
                rows.append((qty, left))
                rows.append((qty, right))
                continue
        rows.append((qty, name))
    merged: list[tuple[int, str]] = []
    for q, n in rows:
        if merged and merged[-1][1].casefold() == n.casefold():
            merged[-1] = (merged[-1][0] + q, merged[-1][1])
        else:
            merged.append((q, n))
    return merged


def byline_player(text: str, fallback: str) -> str:
    head = "\n".join(text.split("\n")[:45])
    m = re.search(rf"\d{{2}}/\d{{2}}\s*[-–—]\s*({NAME_TOKEN})", head)
    if m:
        return TRAIL_JUNK.sub("", m.group(1)).strip(" ,")
    m = re.search(rf"({NAME_TOKEN})\s*[-–—]\s*(?:19|20)\d{{2}}", head)
    if m:
        return TRAIL_JUNK.sub("", m.group(1)).strip(" ,")
    m = re.search(rf"({NAME_TOKEN})\s+played this", head, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(rf"({NAME_TOKEN})\s+from France", head)
    if m:
        return m.group(1).strip()
    return TRAIL_JUNK.sub("", fallback).strip(" ,")


def author_from_label(label: str) -> str:
    if " - " in label:
        return label.rsplit(" - ", 1)[-1].strip(" -")
    m = re.search(r"[-–]\s*([A-Z][A-Za-z.]+(?:\s+[A-Z][A-Za-z.]+)*)\s*$", label)
    if m:
        return m.group(1).strip()
    return label


def canon_player(name: str) -> str:
    name = re.sub(r"\s+", " ", name).strip(" -")
    name = re.sub(r"^(Light|Dark)\s+Side\s+", "", name, flags=re.I)
    name = re.sub(r"\s+(This|Here's|Hi|Ok|Everyone|Starting|Rule With|Aldrin|Nathan|Joe Mornout)$", "", name, flags=re.I)
    name = TRAIL_JUNK.sub("", name).strip(" -")
    parts = name.split()
    if len(parts) >= 4 and [p.casefold() for p in parts[:2]] == [p.casefold() for p in parts[2:4]]:
        name = " ".join(parts[:2])
    if len(parts) >= 3 and parts[0].casefold() == parts[-1].casefold():
        name = " ".join(parts[:-1])
    name = re.sub(r"\s+Well$", "", name)
    if name in PLAYER_CANON:
        return PLAYER_CANON[name]
    # initial + last
    m = re.match(r"^([A-Z])\.\s+(.+)$", name)
    if m:
        key = f"{m.group(1)}. {m.group(2)}"
        if key in PLAYER_CANON:
            return PLAYER_CANON[key]
    return name


def wiki_card(gemp_title: str, side: str, category: str) -> str:
    import wiki_cardlink as cl

    if category == "OBJECTIVE" or gemp_title in OBJ_FACE:
        dest = OBJ_FACE.get(gemp_title, gemp_title)
        vis = dest.split(" / ", 1)[0]
        return cl.wrap(gemp_title, side, dest=dest, label=vis if dest != vis else None)
    if side == "DARK" and gemp_title in DARK_SHARED:
        return cl.wrap(gemp_title, side, dest=f"{gemp_title} (Dark)", label=gemp_title)
    return cl.wrap(gemp_title, side)


def table_from_cards(cards: list[tuple[int, dict]], side: str) -> str:
    groups: dict[str, list[tuple[int, str]]] = defaultdict(list)
    cat_map = {
        "OBJECTIVE": "Objective",
        "CHARACTER": "Character",
        "CREATURE": "Creature",
        "DEVICE": "Device",
        "WEAPON": "Weapon",
        "STARSHIP": "Starship",
        "VEHICLE": "Vehicle",
        "LOCATION": "Location",
        "EFFECT": "Effect",
        "INTERRUPT": "Interrupt",
        "JEDI_TEST": "Jedi Test",
        "ADMIRALS_ORDER": "Admiral's Order",
        "EPIC_EVENT": "Epic Event",
    }
    qty_acc: dict[tuple[str, str], int] = {}
    order_keys: list[tuple[str, str]] = []
    for q, card in cards:
        cat = cat_map.get((card.get("cardCategory") or "").upper(), "Character")
        title = card["title"]
        key = (cat, title)
        if key not in qty_acc:
            order_keys.append(key)
            qty_acc[key] = 0
        qty_acc[key] += q
    grouped: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for cat, title in order_keys:
        grouped[cat].append((qty_acc[(cat, title)], title))
    ordered = [(t, grouped[t]) for t in TYPE_ORDER if t in grouped]
    for t, rows in grouped.items():
        if t not in TYPE_ORDER:
            ordered.append((t, rows))
    weights = [1 + len(rows) for _, rows in ordered]
    total = sum(weights) or 1
    best_i = max(1, (len(ordered) + 1) // 2)
    best = None
    acc = 0
    for i in range(1, len(ordered)):
        acc += weights[i - 1]
        score = abs(acc - (total - acc))
        if best is None or score < best:
            best = score
            best_i = i

    def col(parts):
        chunks = []
        for t, rows in parts:
            chunks.append(f"'''{t}'''")
            for qty, name in rows:
                chunks.append(f"* {qty}x {wiki_card(name, side, t.upper().replace(' ', '_'))}")
            chunks.append("")
        return "\n".join(chunks).rstrip()

    return (
        '{| class="wikitable" style="width:100%;"\n|-\n'
        f'| style="width:50%; vertical-align:top;" |\n{col(ordered[:best_i])}\n'
        f'| style="width:50%; vertical-align:top;" |\n{col(ordered[best_i:])}\n|}}'
    )


def infer_start(cards: list[tuple[int, dict]], side: str, text: str = "") -> tuple[str, str]:
    objs = [c for _, c in cards if (c.get("cardCategory") or "").upper() == "OBJECTIVE"]
    if objs:
        t = objs[0]["title"]
        return t, t
    titles = [c["title"] for _, c in cards]
    blob = text or ""
    if re.search(r"Y4MWR|use Y4MWR as starting", blob, re.I) and any(
        "Massassi War Room" in t for t in titles
    ):
        return "Yavin 4: Massassi War Room", "Yavin 4: Massassi War Room"
    if side == "LIGHT" and any("Massassi Throne Room" in t for t in titles):
        return "Yavin 4: Massassi Throne Room", "Throne Room Mains"
    locs = [c["title"] for _, c in cards if (c.get("cardSubtype") or "").upper() == "SITE"]
    if locs:
        return locs[0], locs[0]
    return "—", "—"


def gemp_fn(fmt: str, start: str, strategy: str, player: str, side: str, year: int, event: str) -> str:
    arch = strategy if strategy and strategy != "—" else start
    if "Massassi Throne Room" in arch:
        arch = "Throne Room Mains"
    name = safe_deck_filename(deck_name(fmt, arch, player, side, year, event))
    return name + ".txt"


def load_cdx() -> dict[str, str]:
    global _CDX
    if _CDX is not None:
        return _CDX
    out: dict[str, str] = {}
    path = CDX_PATH
    if not path.exists():
        path = Path(r"C:\Users\gythe\AppData\Local\Temp\decipher-cdx.txt")
    if path.exists():
        for ln in path.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = ln.split()
            if len(parts) < 3 or parts[2] != "200":
                continue
            slug = parts[0].rstrip("/").rsplit("/", 1)[-1].lower()
            if slug.endswith(".html") and slug not in out:
                out[slug] = parts[1]
    _CDX = out
    return out


def clean_label(label: str) -> str:
    lab = re.sub(r"\brigins\b", "Origins", label, flags=re.I)
    lab = re.sub(r"\bSullest\b", "Sullust", lab)
    return lab


def wayback_url(slug: str) -> str:
    ts = load_cdx().get(slug.lower())
    if ts:
        return WB.format(ts=ts, slug=slug)
    return "https://web.archive.org/web/2000/http://www.decipher.com/starwars/deckdesigns/" + slug


def src_lines(slug: str, label: str) -> str:
    url = wayback_url(slug)
    return f"* [{url} {clean_label(label)}] (Wayback)\n* [{IDX} Decipher Deck Designs index] (Wayback 8 June 2001)"


def write_deck_page(
    title: str,
    player: str,
    event: str | None,
    stage: str,
    finish: str,
    fmt: str,
    side: str,
    start: str,
    strategy: str,
    filename: str,
    cards: list[tuple[int, dict]],
    sources: str,
    year: int,
    published: str,
    extra: str = "",
    before_notes: str = "",
    after_notes: str = "",
) -> None:
    n = sum(q for q, _ in cards)
    side_title = "Light" if side == "LIGHT" else "Dark"
    if start == "—":
        start_field = "—"
    elif start in OBJ_FACE:
        start_field = wiki_card(start, side, "OBJECTIVE")
    else:
        start_field = wiki_card(start, side, "LOCATION")
    ev_line = f"* '''Event:''' [[{event}]]\n" if event else "* '''Published:''' " + published + " (Decipher Deck Designs)\n"
    stage_line = f"* '''Stage:''' {stage}\n" if event else ""
    finish_line = f"* '''Finish:''' {finish}\n" if event and finish and finish != "—" else ""
    see = []
    if event:
        see.append(f"* [[{event}]]")
    see.append("* [[Decipher deck designs]]")
    see.append(f"* [[{player}]]")
    see.append("* [[GEMP importable decklist]]")
    see_block = "\n".join(see)
    cats = CATS + "[[Category:Decklists]]\n"
    if event:
        cats += "[[Category:Championships]]\n" if "Championship" in event or "World" in event else ""
    cats += f"[[Category:{year}]]\n"
    extra_block = (extra.rstrip() + "\n\n") if extra.strip() else ""
    before_sec = f"== Introduction ==\n\n{before_notes}\n\n" if before_notes else ""
    after_sec = f"\n== Strategy ==\n\n{after_notes}\n" if after_notes else ""
    body = f"""'''{title}''' is a [[{side_title}]] constructed list published on Decipher Deck Designs.

== Deck info ==
* '''Player:''' [[{player}]]
{ev_line}{stage_line}{finish_line}* '''Format:''' [[{fmt}]]
* '''Side:''' [[{side_title}]]
* '''Starting Card:''' {start_field}
* '''Strategy:''' {strategy}
{wiki_download_line(filename)}

{extra_block}{before_sec}== Decklist ==

{table_from_cards(cards, side)}
{after_sec}
== See also ==

{see_block}

== Sources ==

{sources}

{cats}"""
    write_page(title, body)


TIMO_HEADER = "! Date !! Event !! Format !! Finish !! Dark !! Light"


def _result_table_from_rows(rows: list[tuple[str, str, str, str, str, str]]) -> str:
    lines = ["{| class=\"wikitable\"", "|-", TIMO_HEADER]
    for date, event, fmt, finish, dark, light in rows:
        lines.append("|-")
        lines.append(f"| {date} || {event} || {fmt} || {finish} || {dark} || {light}")
    lines.append("|}")
    return "\n".join(lines) + "\n"


def _merge_result_row(
    text: str,
    date: str,
    event: str,
    fmt: str,
    finish: str,
    dark: str,
    light: str,
) -> str:
    """Insert or merge one Timo row. Tournament dests, not Decipher.com designs."""
    text = re.sub(r"== Tournament results ==", "== Tournament Results ==", text, count=1)
    event_title = re.search(r"\[\[([^\]|]+)", event)
    needle = event_title.group(1) if event_title else event
    m = re.search(
        rf"(\|- *\n\| [^\n]*\[\[{re.escape(needle)}\]\][^\n]*\n)",
        text,
    )
    if m:
        line = m.group(1)
        # keep existing dests; fill — on the side we now have
        if dark != "—" and re.search(r"\|\| — \|\|", line):
            # Dark cell is the 5th || value; only replace a Dark — when this call has Dark
            parts = line.rstrip("\n").split(" || ")
            if len(parts) >= 6 and parts[4].strip() == "—" and dark != "—":
                parts[4] = dark
            if len(parts) >= 6 and parts[5].strip() == "—" and light != "—":
                parts[5] = light
            new = " || ".join(parts) + "\n"
            return text[: m.start()] + new + text[m.end() :]
        if needle in line:
            return text
    row = f"|-\n| {date} || {event} || {fmt} || {finish} || {dark} || {light}"
    m = re.search(
        r"(== Tournament Results ==\s*\{\| class=\"wikitable\"[\s\S]*?)(\n\|\}\s*)",
        text,
    )
    if m:
        return text[: m.start(2)] + "\n" + row + text[m.start(2) :]
    table = _result_table_from_rows([(date, event, fmt, finish, dark, light)])
    block = "== Tournament Results ==\n\n" + table
    if "== Tournament Results ==" in text:
        return text.replace("== Tournament Results ==", block, 1)
    if "== See also ==" in text:
        return text.replace("== See also ==", block + "\n== See also ==", 1)
    return text.rstrip() + "\n\n" + block


def _inject_design_bullet(text: str, bullet: str) -> str:
    title_bit = bullet.split("[[", 1)[-1].split("]]", 1)[0] if "[[" in bullet else bullet
    if title_bit and title_bit in text:
        return text
    if "== Deck designs ==" in text:
        m = re.search(r"(== Deck designs ==\n(?:\n)?)", text)
        if m:
            return text[: m.end()] + f"{bullet}\n" + text[m.end() :]
        return text.replace("== Deck designs ==", f"== Deck designs ==\n{bullet}\n", 1)
    block = f"== Deck designs ==\n\n{bullet}\n"
    if "== See also ==" in text:
        return text.replace("== See also ==", block + "\n== See also ==", 1)
    return text.rstrip() + "\n\n" + block


def touch_player(
    player: str,
    *,
    design_bullet: str | None = None,
    row: tuple[str, str, str, str, str, str] | None = None,
) -> None:
    """Add a Timo tournament row or a Deck designs bullet. Never dump dests as results bullets."""
    candidates = [
        (PAGES / slug_file(player), f"pages/{slug_file(player)}"),
        (PAGES / "player-stubs" / slug_file(player), f"pages/player-stubs/{slug_file(player)}"),
        (PAGES / "people" / slug_file(player), f"pages/people/{slug_file(player)}"),
    ]
    for fp, rel in candidates:
        if not fp.exists():
            continue
        text = fp.read_text(encoding="utf-8")
        if row:
            date, event, fmt, finish, dark, light = row
            event_title = re.search(r"\[\[([^\]|]+)", event)
            needle = event_title.group(1) if event_title else event
            dest_bits = [c for c in (dark, light) if c != "—"]
            if needle in text and all(b.split("|")[0].strip("[]") in text for b in dest_bits):
                TITLES.append((player, rel))
                return
            text = _merge_result_row(text, date, event, fmt, finish, dark, light)
        elif design_bullet:
            text = _inject_design_bullet(text, design_bullet)
        fp.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
        TITLES.append((player, rel))
        return
    if row:
        player_stub(player, row=row)
    else:
        player_stub(player, design_bullet=design_bullet)


def player_stub(
    player: str,
    bits: list[str] | None = None,
    *,
    row: tuple[str, str, str, str, str, str] | None = None,
    design_bullet: str | None = None,
) -> None:
    """Write a new stub only. Never overwrite an existing bio."""
    path = PAGES / slug_file(player)
    stubs = PAGES / "player-stubs" / slug_file(player)
    people = PAGES / "people" / slug_file(player)
    for p, rel in (
        (path, f"pages/{path.name}"),
        (stubs, f"pages/player-stubs/{stubs.name}"),
        (people, f"pages/people/{people.name}"),
    ):
        if p.exists():
            TITLES.append((player, rel))
            return
    if row:
        mid = "== Tournament Results ==\n\n" + _result_table_from_rows([row])
    elif design_bullet:
        mid = f"== Deck designs ==\n\n{design_bullet}\n"
    else:
        mid = "\n".join(bits or []) + "\n"
    body = (
        f"'''{player}''' published constructed lists on Decipher Deck Designs.\n\n"
        + mid
        + "\n== See also ==\n\n* [[Decipher deck designs]]\n* [[Decklists]]\n\n"
        + CATS
        + "[[Category:Players]]\n"
    )
    dest = PAGES / "player-stubs"
    dest.mkdir(exist_ok=True)
    fp = dest / slug_file(player)
    fp.write_text(body.strip() + "\n", encoding="utf-8", newline="\n")
    TITLES.append((player, f"pages/player-stubs/{fp.name}"))


def infer_side(slug: str, label: str, text: str, hint: str) -> str:
    sl = slug.lower()
    if sl == "sullustdarkdeck.html":
        return "DARK"
    if "light" in sl:
        return "LIGHT"
    if "dark" in sl:
        return "DARK"
    headings = "\n".join(
        ln for ln in text.split("\n")[:12] if len(ln.split()) <= 12
    )
    blob = f"{label}\n{headings}"
    if re.search(r"\blight side (deck|version)\b", blob, re.I):
        return "LIGHT"
    if re.search(r"\bdark side (deck|version)\b", blob, re.I):
        return "DARK"
    if re.search(r"\bthis is the light side\b", blob, re.I):
        return "LIGHT"
    if re.search(r"\bthis is the dark side\b", blob, re.I):
        return "DARK"
    return hint or "LIGHT"


def try_lookup(name: str, side: str, allowed) -> dict | None:
    try:
        return lookup(name, side, allowed)
    except KeyError:
        return None


def lookup_rows(
    raw_rows: list[tuple[int, str]], side: str, fmt: str
) -> tuple[list[tuple[int, dict]], list[tuple[int, str]]]:
    code = FMT_CODE.get(fmt, fmt)
    from gemp_importable import load_format_sets

    allowed = load_format_sets().get(code)
    out: list[tuple[int, dict]] = []
    misses: list[tuple[int, str]] = []
    rows = list(raw_rows)
    i = 0
    while i < len(rows):
        q, n = rows[i]
        card = try_lookup(n, side, allowed)
        consumed = 1
        qty = q
        if card is None and i + 1 < len(rows):
            q2, n2 = rows[i + 1]
            combos = [n + " " + n2, n + n2, n + "/" + n2]
            for comb in combos:
                card = try_lookup(comb, side, allowed)
                if card:
                    consumed = 2
                    qty = q2 if q == 1 and q2 != 1 else q
                    break
            if card is None and i + 2 < len(rows):
                q3, n3 = rows[i + 2]
                comb = n + " " + n2 + " " + n3
                card = try_lookup(comb, side, allowed)
                if card:
                    consumed = 3
                    qty = next((x for x in (q, q2, q3) if x != 1), q)
        if card:
            out.append((qty, card))
        else:
            misses.append((q, n))
        i += consumed
    return out, misses


def process_one(slug: str, label: str, side_hint: str, month: int, year: int, parse_only: bool) -> dict | None:
    raw = read_cached_html(slug)
    if raw is None:
        print("NOFILE", slug)
        return None
    text = extract_content(raw)
    rows = parse_cards(text)
    qty = sum(q for q, _ in rows)
    author = canon_player(byline_player(text, author_from_label(label)))
    tourney = TOURNEY.get(slug.lower())
    fmt = tourney["fmt"] if tourney else format_for_date(month, year)
    side = infer_side(slug, label, text, side_hint)
    title_from_label = re.sub(r"^\d{2}/\d{2}\s*", "", label)
    title_from_label = re.sub(r"\s*[-–]\s*[^-]+$", "", title_from_label).strip(" ,")
    rec = {
        "slug": slug,
        "label": label,
        "player": author,
        "side": side,
        "qty": qty,
        "rows": rows,
        "fmt": fmt,
        "month": month,
        "year": year or (tourney["year"] if tourney else 0),
        "tourney": tourney,
        "pub_title": title_from_label,
        "text": text[:400],
    }
    print(f"PARSE {slug} qty={qty} {side} {author!r} {fmt}")
    if parse_only:
        cards, misses = lookup_rows(rows, side, fmt)
        n = sum(q for q, _ in cards)
        rec["qty_lookup"] = n
        rec["misses"] = misses
        if misses:
            print("LOOKUP_MISS", slug, misses[:10])
        print(f"LOOKUP {slug} n={n} want={40 if 'jr' in slug.lower() else 60} misses={len(misses)}")
        return rec
    if slug.lower() in SKIP_DEST:
        rec["wiki_title"] = EXISTING_DEST.get(slug.lower(), "")
        return rec
    if slug.lower() in CONTENT_DUP:
        rec["skip_dest"] = True
        rec["dup_of"] = CONTENT_DUP[slug.lower()]
        print("SKIP_DUP", slug, "->", rec["dup_of"])
        return rec
    cards, misses = lookup_rows(rows, side, fmt)
    rec["misses"] = misses
    if misses:
        print("LOOKUP_MISS", slug, misses[:12], ("..." if len(misses) > 12 else ""))
        rec["fail"] = "; ".join(n for _, n in misses[:8])
    wiki_cards = list(cards)
    for q, n in misses:
        if re.fullmatch(r"[\(\[]?\d+[\)\]]?", n) or len(n) < 3:
            continue
        if re.match(r"^(starting cards|ships?\s*&|how |introduction|conclusion)", n, re.I):
            continue
        if n in OBJ_FACE or " / " in n:
            cat = "OBJECTIVE"
        elif ":" in n:
            cat = "LOCATION"
        else:
            cat = "CHARACTER"
        wiki_cards.append((q, {"title": n, "cardCategory": cat}))
    n = sum(q for q, _ in wiki_cards)
    rec["qty"] = n
    rec["rows"] = [(q, c["title"]) for q, c in wiki_cards]
    want = 40 if "jr" in slug.lower() or "40 Card" in label else 60
    if n != want:
        print(f"QTY_WARN {slug} got={n} want={want} parsed={qty} misses={len(misses)}")
    if not wiki_cards:
        rec["fail"] = rec.get("fail") or "no cards"
        return rec
    start, strategy = infer_start(wiki_cards, side, text)
    if tourney:
        strategy = start if start != "—" else title_from_label
    else:
        strategy = title_from_label or start
    year_i = rec["year"] or 1999
    event_token = tourney["token"] if tourney else "Designs"
    fn = gemp_fn(fmt, start, strategy, author, side, year_i, event_token)
    GEMP_OUT.mkdir(exist_ok=True)
    if cards:
        xml, notes = xml_for([(q, c["title"], None) for q, c in cards], side, FMT_CODE.get(fmt, fmt))
        (GEMP_OUT / fn).write_text(xml, encoding="utf-8", newline="\n")
        if notes:
            print("NOTES", slug, notes)
    else:
        fn = ""
    side_tok = "LS" if side == "LIGHT" else "DS"
    if tourney:
        wiki_title = f"{tourney['event']} {author} {side_tok}"
        event = tourney["event"]
        published = tourney["dates"]
        stage = "Published lists"
        finish = tourney["finish"]
    else:
        wiki_title = f"{author} {title_from_label}"
        if not title_from_label:
            wiki_title = f"{author} Decipher deck design {side_tok}"
        event = None
        published = f"{['','January','February','March','April','May','June','July','August','September','October','November','December'][month]} {year_i}".strip()
        stage = ""
        finish = ""
    wiki_title = re.sub(r'["*?<>|]', "", wiki_title)
    wiki_title = re.sub(r"\s+", " ", wiki_title).strip()
    sources = src_lines(slug, label)
    extra = ""
    if slug.lower() == "sullustdarkdeck.html":
        extra = (
            "Decipher published this file as the Sullust Regional Dark list; "
            "the printed character and starship lines match the Light file.\n"
        )
    before_notes, after_notes = parse_article_notes(raw, pub_title=title_from_label)
    rec["before_notes"] = before_notes
    rec["after_notes"] = after_notes
    write_deck_page(
        wiki_title,
        author,
        event,
        stage,
        finish,
        fmt,
        side,
        start,
        strategy,
        fn,
        wiki_cards,
        sources,
        year_i,
        published,
        extra,
        before_notes,
        after_notes,
    )
    rec["wiki_title"] = wiki_title
    rec["gemp"] = fn
    rec["start"] = start
    rec["cards"] = wiki_cards
    dest_cell = f"[[{wiki_title}|{start}]]" if start and start != "—" else f"[[{wiki_title}]]"
    if tourney:
        dark = dest_cell if side == "DARK" else "—"
        light = dest_cell if side == "LIGHT" else "—"
        touch_player(
            author,
            row=(
                published,
                f"[[{event}]]",
                f"[[{fmt}]]",
                finish or "—",
                dark,
                light,
            ),
        )
    else:
        touch_player(author, design_bullet=f"* [[{wiki_title}]] ({side_tok}, {published})")
    return rec


def start_from_page(wiki_title: str) -> str:
    if not wiki_title:
        return "—"
    path = PAGES / slug_file(wiki_title)
    if not path.exists():
        return "—"
    text = path.read_text(encoding="utf-8")
    m = re.search(r"\* '''Starting Card:'''\s*(.+)", text)
    if not m:
        return "—"
    raw = m.group(1).strip()
    if raw == "—":
        return "—"
    m2 = re.search(r"\[\[(?:[^|\]]+\|)?([^\]]+)\]\]", raw)
    return m2.group(1).strip() if m2 else raw


def deck_cell(rec: dict | None) -> str:
    """GEMPC-style Dark/Light cell: dest article, pipe text is start/objective."""
    if not rec or not rec.get("wiki_title"):
        return "—"
    start = rec.get("start") or "—"
    vis = OBJ_FACE.get(start, start).split(" / ", 1)[0]
    if vis in {"", "—"}:
        vis = rec.get("vis") or ("Light" if rec.get("side") == "LIGHT" else "Dark")
    return f"[[{rec['wiki_title']}|{vis}]]"


def finish_sort_key(finish: str) -> int:
    f = (finish or "—").strip()
    aliases = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4}
    if f in aliases:
        return aliases[f]
    try:
        return int(f)
    except ValueError:
        return 99


def mm_yy_key(date: str) -> tuple[int, int]:
    """Oldest-first sort for MM/YY cells. Unknown dates last."""
    m = re.match(r"(\d{1,2})/(\d{2})$", (date or "").strip())
    if not m:
        return (9999, 99)
    month, yy = int(m.group(1)), int(m.group(2))
    year = 1900 + yy if yy >= 90 else 2000 + yy
    return (year, month)


def attach_index_fields(rec: dict) -> dict:
    """Fill wiki_title / start from live dest pages without rewriting them."""
    slug = rec["slug"].lower()
    if rec.get("skip_dest"):
        return rec
    if rec.get("player") in {"Juliën Rivière", "Julien Riviere"}:
        rec["player"] = "Juliën Riviëre"
    side_tok = "LS" if rec["side"] == "LIGHT" else "DS"
    if slug in EXISTING_DEST:
        rec["wiki_title"] = EXISTING_DEST[slug]
    elif slug in LIVE_TITLE:
        rec["wiki_title"] = LIVE_TITLE[slug]
    elif rec.get("tourney"):
        rec["wiki_title"] = f"{rec['tourney']['event']} {rec['player']} {side_tok}"
    else:
        title = rec.get("pub_title") or ""
        rec["wiki_title"] = f"{rec['player']} {title}".strip()
        if not title:
            rec["wiki_title"] = f"{rec['player']} Decipher deck design {side_tok}"
    rec["wiki_title"] = re.sub(r'["*?<>|]', "", rec["wiki_title"])
    rec["wiki_title"] = re.sub(r"\s+", " ", rec["wiki_title"]).strip()
    if not rec.get("start"):
        rec["start"] = start_from_page(rec["wiki_title"])
    return rec


def write_event_hub(event: str, recs: list[dict], meta: dict) -> None:
    fmt = meta["fmt"]
    dates = meta["dates"]
    year = meta["year"]
    by_player: dict[str, dict] = {}
    for r in recs:
        by_player.setdefault(r["player"], {})[r["side"]] = r
    rows = []
    for player, sides in by_player.items():
        ls = sides.get("LIGHT")
        ds = sides.get("DARK")
        finish = (ls or ds)["tourney"]["finish"] if (ls or ds) and (ls or ds).get("tourney") else "—"
        rows.append((finish, player, deck_cell(ds), deck_cell(ls)))
    # sort 1st then 2nd then rest
    order = {"1st": 0, "2nd": 1}
    rows.sort(key=lambda x: (order.get(x[0], 9), x[1]))
    table = [
        '{| class="wikitable"',
        "! Finish !! Player !! Dark !! Light",
    ]
    for finish, player, ds, ls in rows:
        table.append("|-")
        table.append(f"| {finish} || [[{player}]] || {ds} || {ls}")
    table.append("|}")
    src = f"* [{IDX} Decipher Deck Designs index] (Wayback 8 June 2001)\n"
    for r in recs:
        src += f"* [{wayback_url(r['slug'])} {clean_label(r['label'])}] (Wayback)\n"
    body = f"""'''{event}''' was a Decipher-era constructed event. Published lists from this event are the 60s Decipher posted on Deck Designs.

== Format ==

* '''Environment:''' [[{fmt}]]
* '''Dates:''' {dates}

== Published lists ==

{chr(10).join(table)}

== See also ==

* [[Decipher deck designs]]
* [[List of SWCCG tournaments]]
* [[GEMP importable decklist]]
* [[Formats]]

== Sources ==

{src}
{CATS}
[[Category:Tournaments]]
[[Category:{year}]]
[[Category:Decklists]]
"""
    write_page(event, body)


def rewrite_index(recs: list[dict], options: list) -> None:
    # Worlds rows the Deck Designs index linked. Do not add Scrye /
    # championship-hub extras (1996 2nd–4th, 1998 Potter). Source is the
    # 8 June 2001 capture (includes Brugge).
    worlds = [
        ("12/96", "Premiere - A New Hope", "1996 Decipher World Championship", "1", "Raphael Asselin",
         "[[1996 Decipher World Championship Raphael Asselin DS|Death Star]]",
         "[[1996 Decipher World Championship Raphael Asselin LS|Yavin 4: Massassi War Room]]"),
        ("12/97", "Premiere - Cloud City", "1997 Decipher World Championship", "1", "Philipp Jacobs",
         "[[1997 Decipher World Championship Philipp Jacobs DS|Mains & Toys]]",
         "[[1997 Decipher World Championship Philipp Jacobs LS|Dagobah turtle]]"),
        ("12/97", "Premiere - Cloud City", "1997 Decipher World Championship", "2", "Michael Riboulet",
         "[[1997 Decipher World Championship Michael Riboulet DS|Dagobah manipulator]]",
         "[[1997 Decipher World Championship Michael Riboulet LS|Dagobah Miner's Guild]]"),
        ("11/99", "Premiere - Endor", "1999 Decipher World Championship", "1", "Gary Carman",
         "[[1999 Decipher World Championship Gary Carman DS|ISB Operations]]",
         "[[1999 Decipher World Championship Gary Carman LS|Hidden Base]]"),
        ("11/99", "Premiere - Endor", "1999 Decipher World Championship", "2", "Steven Lewis",
         "[[1999 Decipher World Championship Steven Lewis DS|Hunt Down And Destroy The Jedi]]",
         "[[1999 Decipher World Championship Steven Lewis LS|Local Uprising]]"),
        ("12/99", "Premiere - Endor", "1999 Decipher World Championship", "4", "James Lafferty",
         "[[1999 Decipher World Championship James Lafferty DS|ISB Operations]]",
         "[[1999 Decipher World Championship James Lafferty LS|Yavin 4: Massassi Throne Room]]"),
        ("10/00", "Premiere - Death Star II", "2000 Decipher World Championship", "1", "Matt Sokol",
         "[[2000 Decipher World Championship Matt Sokol DS|ISB Operations]]",
         "[[2000 Decipher World Championship Matt Sokol LS|Hidden Base]]"),
        ("10/00", "Premiere - Death Star II", "2000 Decipher World Championship", "2", "Yannick Lapointe",
         "[[2000 Decipher World Championship Yannick Lapointe DS|Bring Him Before Me]]",
         "[[2000 Decipher World Championship Yannick Lapointe LS|Mind What You Have Learned]]"),
        ("11/00", "Premiere - Death Star II", "2000 Decipher World Championship", "7", "Raphael Asselin",
         "[[2000 Decipher World Championship Raphael Asselin DS|Bring Him Before Me]]",
         "[[2000 Decipher World Championship Raphael Asselin LS|Mind What You Have Learned]]"),
        ("11/00", "Premiere - Death Star II", "2000 Decipher World Championship", "11", "Paul Todd Feldman",
         "[[2000 Decipher World Championship Paul Todd Feldman DS|Set Your Course For Alderaan]]",
         "[[2000 Decipher World Championship Paul Todd Feldman LS|Hidden Base]]"),
    ]
    on_index = index_snapshot_slugs()
    t_html = [
        '{| class="wikitable sortable"',
        "! Date !! Format !! Event !! Finish !! Player !! Dark !! Light",
    ]

    def add_t(date, fmt, event, finish, player, dark, light):
        t_html.append("|-")
        t_html.append(
            f"| {date} || [[{fmt}]] || [[{event}]] || {finish} || [[{player}]] || {dark} || {light}"
        )

    tourney_recs = [
        r
        for r in recs
        if r and r.get("tourney") and r["slug"].lower() in on_index
    ]
    grouped = defaultdict(list)
    for r in tourney_recs:
        grouped[(r["tourney"]["event"], r["player"])].append(r)
    t_rows = [tuple(row) for row in worlds]
    seen_wp = {(w[2], w[4]) for w in worlds}
    for (event, player), rs in grouped.items():
        if (event, player) in seen_wp:
            continue
        meta = rs[0]["tourney"]
        tag = meta["tag"]
        date = f"{tag[5:]}/{tag[2:4]}"
        by_side = {r["side"]: r for r in rs}
        t_rows.append(
            (
                date,
                meta["fmt"],
                event,
                meta["finish"],
                player,
                deck_cell(by_side.get("DARK")),
                deck_cell(by_side.get("LIGHT")),
            )
        )
    t_rows.sort(key=lambda x: (mm_yy_key(x[0]), x[2], finish_sort_key(x[3]), x[4]))
    for date, fmt, event, finish, player, dark, light in t_rows:
        add_t(date, fmt, event, finish, player, dark, light)
    t_html.append("|}")

    g_html = [
        '{| class="wikitable sortable"',
        "! Date !! Format !! Title !! Side !! Author",
    ]
    g_rows = []
    for r in recs:
        if not r or r.get("tourney") or r["slug"].lower() in SKIP_DEST:
            continue
        if r["slug"].lower() not in on_index:
            continue
        if r.get("skip_dest"):
            continue
        if not r.get("wiki_title"):
            continue
        date = f"{r['month']:02d}/{str(r['year'])[2:]}" if r["month"] else "—"
        side = "Light" if r["side"] == "LIGHT" else "Dark"
        pub = r.get("pub_title") or r["wiki_title"]
        title_cell = f"[[{r['wiki_title']}|{pub}]]"
        g_rows.append((date, r["fmt"], title_cell, side, r["player"], pub))
    g_rows.sort(key=lambda x: (mm_yy_key(x[0]), x[5].lower(), x[4]))
    for date, fmt, title_cell, side, player, _pub in g_rows:
        g_html.append("|-")
        g_html.append(
            f"| {date} || [[{fmt}]] || {title_cell} || {side} || [[{player}]]"
        )
    g_html.append("|}")

    body = f"""'''Decipher deck designs''' were constructed 60s Decipher published on decipher.com under Star Wars CCG Deck Designs. This page inventories that Deck Designs index as captured on 8 June 2001.<ref name="idx">[{IDX} Decipher Deck Designs index] (Wayback 8 June 2001)</ref>

It lists every 60 that page linked. Lists that were never on Deck Designs stay on the event hubs ([[1996 Decipher World Championship]] 2nd–4th from Scrye, [[1998 Decipher World Championship]] Potter).

Lists that name a tournament on that index also belong on the event hub. Lists that do not name a tournament belong here under [[Decklists]].

Format follows the publication month and the newest printed set legal at that date:

* 05/96–06/96 — [[Premiere]]
* 07/96–11/96 — [[Premiere - A New Hope]] (A New Hope, July 1996)
* 12/96 Worlds — [[Premiere - A New Hope]]
* early 1997 — [[Premiere - Hoth]]
* mid 1997 after Dagobah (May 1997) — [[Premiere - Dagobah]]
* 12/97 Worlds — [[Premiere - Cloud City]]
* 1998 Jabba's Palace (April/May) — [[Premiere - Jabba's Palace]]
* 11/98 Special Edition — [[Premiere - Special Edition]]
* 1999 Endor (June/July) — [[Premiere - Endor]]
* 2000 Death Star II / Third Anthology (June) — [[Premiere - Death Star II]]
* 03/01 Brugge — [[Premiere - Tatooine]]

== Tournament lists ==

Rows the Decipher Deck Designs index presented as tournament results. Dark and Light link the dest articles. Extra lists that were never on this index stay on the event hub.

{chr(10).join(t_html)}

== General lists ==

Published as Deck Designs without a named tournament. The Title links the dest article; that article has the list and the [[GEMP importable decklist]] Download.

{chr(10).join(g_html)}

The index still lists 04/97 Target the Main Generators (R. Harter). Every Wayback capture of that slug is [[Gaetano Ferrara]]'s Sullust Light 60, dested on [[1997 Sullust Regionals]].

== See also ==

* [[Decklists]]
* [[GEMP importable decklist]]
* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Formats]]

== Sources ==

* [{IDX} Decipher Deck Designs index] (Wayback 8 June 2001)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Meta]]
"""
    write_page("Decipher deck designs", body)


def patch_list(events: list[tuple[str, dict]]) -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    marker = "== Decipher World Championships =="
    section = [
        "== Decipher-era regionals and opens ==",
        "",
        "Published constructed 60s from Decipher Deck Designs that name a tournament other than Worlds.",
        "",
        '{| class="wikitable sortable"',
        "! Tag !! Event !! Dates !! Site !! Format !! Winner",
    ]
    # newest first
    events = sorted(events, key=lambda x: x[1]["tag"], reverse=True)
    seen = set()
    for event, meta in events:
        if event in seen:
            continue
        seen.add(event)
        winner = "—"
        section.append("|-")
        section.append(
            f"| {meta['tag']} || [[{event}]] || {meta['dates']} || — || [[{meta['fmt']}]] || {winner}"
        )
    section.append("|}")
    section.append("")
    block = "\n".join(section) + "\n"
    if "== Decipher-era regionals and opens ==" in text:
        text = re.sub(
            r"== Decipher-era regionals and opens ==.*?(?=\n== Decipher World Championships ==)",
            block,
            text,
            count=1,
            flags=re.S,
        )
    else:
        text = text.replace(marker, block + marker)
    # fill winners for known 1st-place dests later in caller
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    TITLES.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))


def patch_euro() -> None:
    path = PAGES / "European_Championships.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    row = "| 2000 || [[2000 European Championship]] || — || [[Premiere - Death Star II]] || —"
    if "2000 European Championship" not in text:
        text = text.replace(
            "| 2001 || 2001 European Championship",
            row + "\n|-\n| 2001 || 2001 European Championship",
        )
        path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
        TITLES.append(("European Championships", "pages/European_Championships.wiki"))


def write_tsv(path: Path) -> None:
    # unique titles
    seen = set()
    lines = []
    for title, rel in TITLES:
        if title in seen:
            continue
        seen.add(title)
        lines.append(f"{title}\t{rel}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("TSV", path, "n=", len(lines))


def fetch_live_wikitext(titles: list[str]) -> dict[str, str]:
    """Pull current dest wikitext so notes inject keeps the live 60."""
    api = "https://wiki.swccg.com/api.php"
    out: dict[str, str] = {}
    for i in range(0, len(titles), 40):
        batch = titles[i : i + 40]
        params = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
            "titles": "|".join(batch),
            "maxage": "0",
            "smaxage": "0",
        }
        url = api + "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=90) as r:
            data = json.loads(r.read().decode("utf-8"))
        for page in (data.get("query") or {}).get("pages", {}).values():
            title = page.get("title") or ""
            revs = page.get("revisions") or []
            if not title or not revs:
                continue
            slot = (revs[0].get("slots") or {}).get("main") or revs[0]
            text = slot.get("*") or ""
            if text:
                out[title] = text
        print("LIVE", i + len(batch), "/", len(titles), "got", len(out))
    missing = [t for t in titles if t not in out]
    for title in missing:
        raw_url = (
            "https://wiki.swccg.com/index.php?title="
            + urllib.parse.quote(title.replace(" ", "_"))
            + "&action=raw"
        )
        try:
            req = urllib.request.Request(
                raw_url, headers={"User-Agent": "swccg-wiki-notes/1.0"}
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                text = r.read().decode("utf-8", errors="replace")
        except Exception as e:
            print("RAW_FAIL", title, e)
            continue
        if text.strip() and "<html" not in text[:80].lower():
            out[title] = text
            print("RAW", title, len(text))
    return out


def notes_only() -> int:
    """Inject published Decipher prose into live dests. No hubs, bios, or GEMP."""
    TITLES.clear()
    options = load_options()
    recs = []
    for slug, label, side_hint, month, year in options:
        raw = ensure_cached_html(slug)
        if raw is None:
            print("NOFILE", slug)
            continue
        text = extract_content(raw)
        author = canon_player(byline_player(text, author_from_label(label)))
        tourney = TOURNEY.get(slug.lower())
        title_from_label = re.sub(r"^\d{2}/\d{2}\s*", "", label)
        title_from_label = re.sub(r"\s*[-–]\s*[^-]+$", "", title_from_label).strip(" ,")
        rec = {
            "slug": slug,
            "label": label,
            "player": author,
            "side": infer_side(slug, label, text, side_hint),
            "tourney": tourney,
            "pub_title": title_from_label,
        }
        attach_index_fields(rec)
        recs.append(rec)
    have = {r["slug"].lower() for r in recs}
    for slug, wiki_title in EXISTING_DEST.items():
        if slug in have:
            continue
        recs.append(
            {
                "slug": slug,
                "label": wiki_title,
                "player": "",
                "side": "LIGHT" if "light" in slug else "DARK",
                "tourney": TOURNEY.get(slug),
                "pub_title": wiki_title,
                "wiki_title": wiki_title,
            }
        )
        print("EXTRA_DEST", slug, wiki_title)
    jobs = []
    for rec in recs:
        slug = rec["slug"]
        if slug.lower() in CONTENT_DUP:
            print("SKIP_DUP", slug)
            continue
        title = rec.get("wiki_title") or ""
        if not title:
            print("NOTITLE", slug)
            continue
        raw = ensure_cached_html(slug)
        if raw is None:
            print("NOFILE", slug)
            continue
        before, after = parse_article_notes(raw, pub_title=rec.get("pub_title") or "")
        if not before and not after:
            print("NONOTES", slug, title)
            continue
        jobs.append((slug, title, before, after))
    live = fetch_live_wikitext([t for _, t, _, _ in jobs])
    n_ok = 0
    for slug, title, before, after in jobs:
        wiki = live.get(title)
        if not wiki:
            path = PAGES / slug_file(title)
            if path.exists():
                wiki = path.read_text(encoding="utf-8")
                print("LOCAL", title)
            else:
                print("NOPAGE", title)
                continue
        try:
            new = inject_strategy(wiki, before, after)
        except ValueError as e:
            print("INJECT_FAIL", title, e)
            continue
        if new == wiki:
            print("UNCHANGED", title)
            continue
        write_page(title, new)
        n_ok += 1
        print(
            "NOTES",
            slug,
            title,
            "before",
            len(before),
            "after",
            len(after),
        )
    write_tsv(ROOT / "y-decipher-notes-delta.tsv")
    print("NOTES-ONLY wrote", n_ok, "pages tsv", len(TITLES))
    for rec in recs:
        title = rec.get("wiki_title") or ""
        if not title or title in TITLES:
            continue
        path = PAGES / slug_file(title)
        if not path.exists():
            continue
        wiki = path.read_text(encoding="utf-8")
        if "== Strategy ==" not in wiki and "== Introduction ==" not in wiki:
            continue
        raw = read_cached_html(rec["slug"])
        before = after = ""
        if raw:
            before, after = parse_article_notes(
                raw, pub_title=rec.get("pub_title") or ""
            )
        if before or after:
            continue
        new = inject_strategy(wiki, "", "")
        if new != wiki:
            path.write_text(new, encoding="utf-8", newline="\n")
            print("STRIP_LOCAL", title)
    return 0


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--parse-only", action="store_true")
    ap.add_argument(
        "--index-only",
        action="store_true",
        help="Rewrite [[Decipher deck designs]] from dest pages; do not write dests or hubs.",
    )
    ap.add_argument(
        "--notes-only",
        action="store_true",
        help="Inject published before/after list prose; do not rewrite lists, hubs, or GEMP.",
    )
    args = ap.parse_args()
    TITLES.clear()
    if args.notes_only:
        return notes_only()
    if not args.index_only and GEMP_OUT.exists():
        for p in GEMP_OUT.glob("*.txt"):
            p.unlink()
    options = load_options()
    print("options", len(options))
    recs = []
    fails = []
    for slug, label, side, month, year in options:
        rec = process_one(
            slug, label, side, month, year, args.parse_only or args.index_only
        )
        if rec is None:
            fails.append(slug)
            continue
        if rec.get("fail"):
            fails.append(slug)
        if args.index_only:
            attach_index_fields(rec)
        recs.append(rec)
    if args.parse_only:
        print("parse done", len(recs), "fails", len(fails))
        return 0 if not fails else 1
    if args.index_only:
        rewrite_index(recs, options)
        write_tsv(ROOT / "y-decipher-index-delta.tsv")
        print("INDEX-ONLY pages", len(TITLES), "fails", fails)
        return 0
    # hubs
    by_event: dict[str, list[dict]] = defaultdict(list)
    metas = {}
    for r in recs:
        if r.get("tourney") and r.get("wiki_title") and r["slug"].lower() not in SKIP_DEST:
            ev = r["tourney"]["event"]
            by_event[ev].append(r)
            metas[ev] = r["tourney"]
    for ev, rs in by_event.items():
        write_event_hub(ev, rs, metas[ev])
        # winner cell
        winners = [x["player"] for x in rs if x.get("tourney") and x["tourney"]["finish"] == "1st"]
        if winners:
            metas[ev]["winner"] = winners[0]
    patch_list([(ev, metas[ev]) for ev in by_event])
    # fill winners on list
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for ev, meta in metas.items():
            w = meta.get("winner")
            if not w:
                continue
            old = f"| [[{ev}]] || {meta['dates']} || — || [[{meta['fmt']}]] || —"
            new = f"| [[{ev}]] || {meta['dates']} || — || [[{meta['fmt']}]] || [[{w}]]"
            text = text.replace(old, new)
        path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    patch_euro()
    rewrite_index(recs, options)
    write_tsv(ROOT / "y-decipher-designs-delta.tsv")
    print("FAILS", fails)
    print("pages", len(TITLES), "gemp", len(list(GEMP_OUT.glob('*.txt'))) if GEMP_OUT.exists() else 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
