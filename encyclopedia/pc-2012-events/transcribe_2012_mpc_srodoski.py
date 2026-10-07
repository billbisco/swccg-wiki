#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Pete Srodoski.

Source: 2012mpcday1.pdf pages 129–130 (2010 form, 12 shields).
Name Peter Srodoski dested Pete Srodoski (CANON analog generate_2015_2016 / generate_2017_2018).
Username Kavanix.
p129 Light Yavin 4 (V). p130 Dark Invasion.
Pack player-stubs/Pete_Srodoski.wiki.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Pete Srodoski"
USERNAME = "Kavanix"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 129
DS_PAGE = 130
LS_SCAN = "2012 Match Play Championship Day 1 Pete Srodoski LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Pete Srodoski DS.png"
LS_DECK_NAME = "Liberate Art!"
DS_DECK_NAME = "Destroyers!!"
NOTE = "Handwritten 2010 Xerox form. Username Kavanix."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Peter Srodoski dested Pete Srodoski. Username Kavanix. "
    "LIGHT checked. Deck Name Liberate Art!. Event Date 2/11/12 Event Name 2012 MPC. "
    "Y4 True dested Yavin 4 (V). Yoking dested Wokling True analog Erwin. "
    "Caperwl Plan dested Careful Planning True analog Erwin. Poushy dested Boushh. "
    "Wedge RS1 dested Wedge In Red Squadron 1 analog Pinto. "
    "Houjix combo dested Houjix & Out Of Nowhere. JPP dested Jek Porkins True analog Erwin. "
    "Gold dested Gold Leader In Gold 1 analog Erwin. Biggs R L dested Biggs Darklighter True analog Erwin. "
    "Hiding In dested Hindsight True analog Pinto. 5 Folls dested A Few Maneuvers True analog Erwin. "
    "Projection dested Projection Of A Skywalker analog Erwin. "
    "Hobbie True dested as written. Protection dested as written. "
    "AFA True dested in the 60 analog Casey. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Peter Srodoski dested Pete Srodoski. Username Kavanix. "
    "DARK checked. Deck Name Destroyers!!. Event Date 2/11/12 Event Name 2012 MPC. "
    "Invasion empty dested Invasion / In Complete Control. "
    "Master Destroyers dested Master, Destroyers! analog Tony Garcia. "
    "P13 > P14 dested P-13 & P-14 analog Tony. Ten Num dested Tey How analog Tony. "
    "Droid Rack dested Droid Racks True analog Buck. At Last dested At Last We Are Getting Results True analog Tony. "
    "Maul (Tat) dested Darth Maul analog Tony. Nute Gunray N.V. dested Nute Gunray, Neimoidian Viceroy analog Tony. "
    "Trade Fed Battle dested Naboo: Battle Plains analog Tony. "
    "Propaganda True dested Imperial Propaganda True. Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Jabbahaven dested Jabba's Haven True analog Millet. "
    "Blockade Support Ship True AND empty kept separate analog Foth. "
    "Prepared Defenses empty dested in the 60 analog Pistone. "
    "K&D True dested in the 60 analog Murray. On Air dested as written. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Squadron Assignments"),
    n("Luke, Trust Me", True),
    n("Wokling", True),
    n("Careful Planning", True),
    n("Boushh"),
    n("Rebel Artillery", qty=2),
    n("Wedge In Red Squadron 1"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Tatooine"),
    n("X-wing Laser Cannon", qty=2),
    n("Yavin 4: Massassi War Room"),
    n("Restore Freedom To The Galaxy"),
    n("Return Of The Jedi", True),
    n("Massassi Base Sentry", True),
    n("Legendary Starfighter"),
    n("Red Squadron 7"),
    n("I'll Take The Leader", qty=2),
    n("Projection Of A Skywalker"),
    n("Houjix & Out Of Nowhere"),
    n("Mace Windu", True),
    n("Red 3", True),
    n("Corran Horn"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Jek Porkins", True),
    n("Organized Attack", qty=2),
    n("Let The Wookiee Win", True),
    n("Gold Leader In Gold 1"),
    n("Artoo-Detoo In Red 5"),
    n("Hobbie", True),
    n("Coruscant"),
    n("Biggs Darklighter", True),
    n("Hindsight", True),
    n("Haven"),
    n("Protection"),
    n("Red 1", True),
    n("Obi-Wan With Lightsaber"),
    n("Red Squadron 4"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Desperate Reach", True),
    n("Imperial Atrocity", True, qty=2),
    n("Red Squadron 1"),
    n("Red 6"),
    n("Flash Of Insight", True, qty=2),
    n("Rebel Barrier"),
    n("Chewie", True),
    n("Captain Han Solo"),
    n("Lando Calrissian, Scoundrel"),
    n("A Few Maneuvers", True),
    n("Millennium Falcon", True),
    n("Red Leader"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Aim High", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo"),
    n("Nute Gunray", qty=2),
    n("Elis Helrot"),
    n("P-60", qty=2),
    n("P-59", qty=2),
    n("IG-88 With Riot Gun", True),
    n("Oh, Switch Off", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Blockade Support Ship", True),
    n("Darth Maul", qty=2),
    n("Search And Destroy"),
    n("First Strike"),
    n("Naboo: Theed Palace Generator"),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Destroyer Droid", qty=8),
    n("Maul's Sith Infiltrator"),
    n("Imperial Propaganda", True, qty=2),
    n("Self-Destruct Mechanism", True),
    n("Imperial Barrier"),
    n("Master, Destroyers!", qty=2),
    n("Wounded Warrior", qty=2),
    n("Lightsaber Deficiency", True),
    n("P-13 & P-14", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Blockade Flagship", True),
    n("Daultay Dofine", True),
    n("Tey How"),
    n("Scum And Villainy"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Nothing Can Get Through Our Shield"),
    n("Cold Feet", True),
    n("Prepared Defenses"),
    n("Blockade Support Ship"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Swamp"),
    n("At Last We Are Getting Results", True),
    n("Droid Racks", True),
    n("Where Are Those Droidekas?", True),
    n("Jabba's Haven", True),
    n("Naboo: Battle Plains"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("On Air"),
    n("Secret Plans"),
    n("Firepower"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Abyss", True),
]
DS_ADD = []
