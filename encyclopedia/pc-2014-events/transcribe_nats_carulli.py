#!/usr/bin/env python3
"""2014 US Nationals Day 2 Xerox: Matt Carulli.

Source: Nationals-2014-day-2.pdf pages 5–6 (2010 form).
Name Matthew / Matt Carulli. Dest Matt Carulli.
p05 LS Same as Yesterday with In/Out: dest Day 1 LS minus OUT plus IN.
"""
from __future__ import annotations

PLAYER = "Matt Carulli"
USERNAME = "quickdraw345"
STAGE = "Day 2"
PDF = "2014 US Nationals Day 2.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2014 US Nationals Day 2 p05 Matt Carulli LS.png"
DS_SCAN = "2014 US Nationals Day 2 p06 Matt Carulli DS.png"
NOTE = "Handwritten 2010 Xerox. Name Matthew / Matt Carulli dested Matt Carulli."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Matthew Carulli. Deck name Communing Players. "
    "Same as Yesterday with OUT Disarmed, Flash of Insight (V) and IN Sense, Mandalorian Saber. "
    "Dest Day 1 LS minus those OUT plus Sense and Mandalorian Saber. "
    "Mandalorian Saber dested as written. (V) from Day 1 checkbox. "
    "NO_DEST (2014 index): A Good Friend At Your Side; Mandalorian Saber."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Carulli. Deck name Ready… Invasion? "
    "Invasion dested Invasion / In Complete Control. YCFTF combo dested You Can Follow Them & Those Rebel Pilots. "
    "Where Are You Taking This Thing dested Where Are You Taking This... Thing?. "
    "At Last We Are Getting Results dested At Last We Are Getting Results. "
    "Where Are Those Droidekas dested Where Are Those Droidekas?. "
    "Masterful Move & Endor Occ dested Masterful Move & Endor Occupation. "
    "P-59 dested P-59. Reegesh dested Reegesh. "
    "Nute Gunray, Neimoidian Viceroy dested Nute Gunray, Neimoidian Viceroy. "
    "I Too Can dested I Will Find Them Quickly, Master. "
    "K+D dested Knowledge And Defense. Unique overcounts sheet-accurate "
    "(We Must Accelerate Our Plans x3, Destroyer Droid x8, Guri x2, P-59 x2, P-60 x3, "
    "On The Edge x2, Imperial Barrier x2, Rolling, Rolling, Rolling x2, "
    "Wounded Warrior x2, Self-Destruct Mechanism x2, Blockade Flagship: Hangar x2, "
    "Force Push x2). (V) from checkbox. "
    "NO_DEST (2014 index): Droid Bodies (V); You Can Follow Them & Those Rebel Pilots; "
    "On The Edge; Blockade Flagship: Hangar; Gravik."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Quick Draw", True),
    n("A Good Friend At Your Side"),
    n("Shmi Skywalker"),
    n("Tatooine: Mos Espa"),
    n("Maneuvering Flaps", True),
    n("Tatooine: Cantina", True),
    n("Run Luke, Run!", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=4),
    n("Anakin's Lightsaber"),
    n("Yoda, Great Warrior"),
    n("Rebel Barrier", qty=2),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Threepio With His Parts Showing"),
    n("Anakin's Lightsaber"),
    n("Luke Skywalker, Jedi Knight"),
    n("Jedi Levitation", True),
    n("Houjix"),
    n("Draw Their Fire"),
    n("Control & Tunnel Vision"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Seeking An Audience", True),
    n("Dark Approach", True),
    n("Corran Horn"),
    n("Chewie, Enraged", True),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Nabrun Leids"),
    n("Escape Pod", True),
    n("Padme Naberrie", True, qty=2),
    n("Han's Heavy Blaster Pistol", True),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Luke's Bionic Hand"),
    n("I'm With You Too", True),
    n("Sense"),
    n("Mandalorian Saber"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Aim High"),
    n("Jabba's Prize", True),
    n("Do, Or Do Not"),
]


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo"),
    n("Blockade Flagship"),
    n("Droid Starfighters"),
    n("Droid Bodies", True),
    n("Prepared Defenses"),
    n("You Can Follow Them & Those Rebel Pilots"),
    n("At Last We Are Getting Results", True),
    n("Where Are Those Droidekas?", True),
    n("On The Edge", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Masterful Move", qty=2),
    n("Sniper & Dark Strike"),
    n("Imperial Barrier", qty=2),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Force Push", True),
    n("Masterful Move & Endor Occupation"),
    n("Wounded Warrior", qty=2),
    n("Ghhhk"),
    n("Self-Destruct Mechanism", qty=2),
    n("Blockade Flagship: Hangar", qty=2),
    n("Force Push"),
    n("Destroyer Droid", qty=8),
    n("Count Dooku", True),
    n("Guri", qty=2),
    n("P-59", qty=2),
    n("P-60", qty=3),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Nute Gunray"),
    n("Naboo: Theed Palace Generator"),
    n("Blockade Flagship: Bridge"),
    n("Reegesh"),
    n("Forced Servitude"),
    n("Imperial Justice", True),
    n("First Strike"),
    n("I Will Find Them Quickly, Master", True),
    n("Where Are You Taking This... Thing?"),
    n("Imperial Decree", True),
    n("Gravik"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
]
DS_ADD = [
    n("Secret Plans"),
    n("Abyss"),
    n("Oppressive Enforcement"),
]
