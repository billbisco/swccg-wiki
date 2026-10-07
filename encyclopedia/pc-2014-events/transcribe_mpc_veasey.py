#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: John Veasey Light.

Source: MPC-2014-Day-1-Main-Event.pdf page 115 (2013 form, 15 shields).
Name John Veasey. Username VeeZ. Event MPC 2014 01/25/14. Light only.
"""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = "VeeZ"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 115
DS_PAGE = 0
LS_SCAN = "2014 Match Play Championship Day 1 John Veasey LS.png"
DS_SCAN = ""
LS_DECK_NAME = "Hijinks and Scratchcats"
DS_DECK_NAME = ""
NOTE = "Typed 2013 Xerox form plus handwritten replacements. Light only."
LS_NOTE = (
    "Typed 2013 Xerox plus handwritten replacements. Name John Veasey. Username VeeZ. "
    "Event MPC 2014 01/25/14. LIGHT checked. Deck name Hijinks and Scratchcats. "
    "Yavin 4: Massassi Throne Room start. Line 9 Goo Nee Tay crossed, handwritten "
    "Much To Learn You Still Have dested Much To Learn You Still Have. "
    "Padme Naberrie dested Padme Naberrie. Leia dested Leia, Rebel Princess. "
    "Han, Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Line 29 crossed then Revolution dested Revolution. Line 54 Let The Wookiee Win "
    "crossed, Were You Looking For Me dested Were You Looking For Me?. "
    "Line 55 Let The Wookiee Win crossed, Either Way You Win dested Either Way, You Win. "
    "Shield 4 crossed, Affect Mind dested Affect Mind. Shield 15 Affect Mind crossed, "
    "Yavin Sentry dested Yavin Sentry. Unique overcounts sheet-accurate "
    "(Qui-Gon Jinn With Lightsaber x2, Luke With Lightsaber x2, Obi-Wan With Lightsaber x2, "
    "Lando Calrissian, Scoundrel x2, Han, Chewie, And The Falcon x2, Revolution x6, "
    "A Jedi's Resilience x3, Rebel Leadership (V) x2, Wesa Gotta Grand Army x2, "
    "Yavin Sentry (V) x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Civil Disorder", True),
    n("Goo Nee Tay"),
    n("Much To Learn You Still Have"),
    n("I Did It!"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess", True),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Han, Chewie, And The Falcon", True),
    n("Tantive IV", True),
    n("Revolution"),
    n("Wedge In Red Squadron 1"),
    n("Gold Leader In Gold 1", True),
    n("Draw Their Fire"),
    n("Down With The Emperor", True),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Revolution", qty=5),
    n("Mantellian Savrip"),
    n("Escape Pod", True),
    n("Hear Me Baby, Hold Together", True),
    n("Clash Of Sabers"),
    n("Houjix"),
    n("A Jedi's Resilience", True),
    n("A Jedi's Resilience", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True),
    n("Were You Looking For Me?", True),
    n("Either Way, You Win", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Malastare"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Affect Mind"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("The Professor"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("He Can Go About His Business", True),
    n("Battle Plan"),
    n("Do, Or Do Not", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
