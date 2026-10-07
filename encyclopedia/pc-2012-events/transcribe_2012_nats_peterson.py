#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Alden Peterson.

Source: 2012NationalsDay1.pdf pages 56–57 (handwritten 2010 Xerox, 12 shields).
p56 Dark / p57 Light Name Alden Peterson Username -maul dested Alden Peterson analog leftover 2008 Worlds.
Pack player-stubs/Alden_Peterson.wiki.
"""
from __future__ import annotations

PLAYER = "Alden Peterson"
USERNAME = "-maul"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 57
DS_PAGE = 56
LS_SCAN = "2012 US Nationals Day 1 Alden Peterson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Alden Peterson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Alden Peterson dested Alden Peterson analog leftover 2008 Worlds. "
    "Username -maul. Event Date 06/09/12 Event Name Nationals."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Alden Peterson dested Alden Peterson analog leftover 2008 Worlds. "
    "Username -maul. LIGHT checked. Event Date 06/09/12 Event Name Nationals. "
    "HTFME dested Heading For The Medical Frigate analog leftover. "
    "LS_START Hidden Base / Uncharted dested Hidden Base / Systems Will Slip Through Your Fingers True analog leftover Herold. "
    "Uncharted Settlements dested Uncharted Settlements True leftover_xerox. "
    "AFA dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Padme dested Padmé Naberrie analog leftover Brady. "
    "L+WW dested Let The Wookiee Win True analog leftover Brady x2. "
    "All Wings Combo dested All Wings Report In analog leftover Echeverria x4 unique overcount. "
    "Houjix Combo dested Houjix & Out Of Nowhere analog leftover. "
    "Shield Optimism dested Let's Keep A Little Optimism Here True analog leftover. "
    "Shield Insight dested Your Insight Serves You Well True analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Alden Peterson dested Alden Peterson analog leftover 2008 Worlds. "
    "Username -maul. DARK checked. Event Date 06/09/12 Event Name Nationals. "
    "AOBS / V of DP dested Agents Of Black Sun / Vengeance Of The Dark Prince analog leftover Aue. "
    "Mara Jade TEH dested Mara Jade, The Emperor's Hand analog leftover Aue x2. "
    "Dengar IP1 dested Dengar In Punishing One analog leftover Brady. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun analog leftover. "
    "Elis in Hinthra dested Elis In Hinthra True analog leftover Cullen. "
    "Trophy of a Kill dested Trophy Of A Kill True analog leftover Aue x4 unique overcount. "
    "Stunning Leader dested Stunning Leader True analog leftover Aue x3 unique overcount. "
    "Dark Time for Rebellion dested A Dark Time For The Rebellion True analog leftover x4 unique overcount. "
    "K&D dested Knowledge And Defense analog leftover Cooleo IN THE 60 x2. "
    "PotF dested Presence Of The Force analog leftover leftover_xerox x2. "
    "Shield Coward dested Come Here You Big Coward True analog leftover. "
    "Code Clearance dested Do They Have A Code Clearance? True analog leftover. "
    "TINT dested There Is No Try analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Get To Your Ships"),
    n("We Didn't Hit It"),
    n("Hidden Landing Site", True),
    n("Nal Hutta"),
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Uncharted Settlements", True),
    n("Anger, Fear, Aggression", True),
    n("Aquaris"),
    n("Kiffex"),
    n("Rebel Cell: Situation Room", True),
    n("Yoda, Mystic", qty=2),
    n("Senator Leia Organa", True),
    n("Captain Panaka"),
    n("Jens Vanick"),
    n("Padmé Naberrie"),
    n("Jedi Pilot", True, qty=3),
    n("Clone Pilot", True, qty=3),
    n("Officer Dolphe"),
    n("Ric Olie, Bravo Leader"),
    n("Alderaan Consular Ship", True),
    n("Republic Starfighter", True, qty=3),
    n("Bravo Fighter", True),
    n("Bravo 1"),
    n("Bravo 2"),
    n("Bravo 3"),
    n("Bravo 4"),
    n("Bravo 5"),
    n("Fly On Autopilot"),
    n("We'll Take The Long Way", True),
    n("Flash Of Insight", True),
    n("Uncontrollable Fury"),
    n("Bacta Tank"),
    n("Imperial Atrocity", True),
    n("Hiding In The Garbage", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Firefight", True, qty=2),
    n("Are You Brain Dead?!"),
    n("All Wings Report In", qty=4),
    n("Alter", True),
    n("HMB, HT", True),
    n("Control Combo"),
    n("It's Not My Fault", True),
    n("It's A Hit"),
    n("Houjix & Out Of Nowhere"),
    n("Taking Them With Us", True),
    n("Full Throttle Spinning"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("No Bargain", True),
    n("Start Your Engines"),
    n("Sebulba's Pod"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Presence Of The Force", qty=2),
    n("Shada", True),
    n("Coruscant (Special Edition)"),
    n("Imperial City"),
    n("Kad", True),
    n("Prophetess", True),
    n("Gardulla The Hutt"),
    n("Shedda", True),
    n("Kitik Keed'kak", True),
    n("Aurra Sing"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("P-59"),
    n("P-60"),
    n("Probot", True),
    n("IG-88 With Riot Gun"),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra", True),
    n("Trophy Of A Kill", True, qty=4),
    n("Flagship Bridge"),
    n("Hoth: War Room"),
    n("Death Star: War Room", True),
    n("Dark Deal", True),
    n("No Escape"),
    n("Jabba's Haven"),
    n("Surprise"),
    n("Weapon Levitation"),
    n("Wookiee Kiss", qty=3),
    n("Projective Telepathy", qty=2),
    n("Stunning Leader", True, qty=3),
    n("Elis Helrot"),
    n("Comscan Deflection", True),
    n("Vader's Obsession", qty=2),
    n("Control", qty=2),
    n("Imperial Barrier", qty=2),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Knowledge And Defense", qty=2),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Secret Plans"),
    n("Allegations Of Corruption", True),
    n("Fanfare"),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try"),
]
DS_ADD = []
