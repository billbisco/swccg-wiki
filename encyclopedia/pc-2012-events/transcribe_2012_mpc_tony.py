#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Tony Garcia.

Source: 2012mpcday1.pdf pages 71–72 (2010 form, 12 shields).
Name Tony G dested Tony Garcia (2013 leftover analog PLAYER=\"Tony G\").
Username tazmizzionz. Do not copy 2014 leftover Username jigga.
p71 Light Rescue The Princess. p72 Dark Invasion.
Do not dest as a new person. Do not dest as Tony DaCosta / Tony Petersson.
Do not rewrite 2013 leftovers. Pack player-stubs/Tony_Garcia.wiki.
"""
from __future__ import annotations

PLAYER = "Tony Garcia"
USERNAME = "tazmizzionz"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 71
DS_PAGE = 72
LS_SCAN = "2012 Match Play Championship Day 1 Tony Garcia LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Tony Garcia DS.png"
LS_DECK_NAME = "Thank You Artoo! But Our Princess Is In Another Death Star!"
DS_DECK_NAME = "iDD"
NOTE = "Typed 2010 Xerox form."
LS_NOTE = (
    "Typed 2010 Xerox. Name Tony G dested Tony Garcia. Username tazmizzionz. "
    "LIGHT checked. Deck Name Thank You Artoo! But Our Princess Is In Another Death Star!. "
    "Event MPC Date 02/11/12. Email @gmail.com. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Rescue The Princess dested Rescue The Princess / Sometimes I Amaze Even Myself empty. "
    "Artoo & *Threepio dested Artoo & Threepio True. "
    "Odin Nesloor & *First Aid dested Odin Nesloor & First Aid x3. "
    "Sorry About The Mess & *Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency x2. "
    "Antilles Maneuver & *Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Unique 60. Shields 12. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Tony G dested Tony Garcia. Username tazmizzionz. "
    "DARK checked. Deck Name iDD. Event MPC Date 02/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Invasion dested Invasion / In Complete Control empty. "
    "Naboo dested Naboo. Where Are Those Droidekas?! dested Where Are Those Droidekas?. "
    "3,720 To 1 dested 3,720 To 1 True. "
    "Elis Helrot dested Elis Helrot. "
    "Short Range Fighters & *Watch Your Back! dested Short Range Fighters & Watch Your Back!. "
    "P-13 & *P-14 dested P-13 & P-14. "
    "Destroyer Droid x9 sheet-accurate. Unique 60. Shields 12. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rescue The Princess / Sometimes I Amaze Even Myself"
LS_CARDS = [
    n("Rescue The Princess / Sometimes I Amaze Even Myself"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Docking Bay"),
    n("Death Star: Docking Bay 327"),
    n("Death Star: Detention Block Corridor"),
    n("Senator Leia Organa"),
    n("Prisoner 2187"),
    n("Scomp Link Access", True),
    n("Cell 2187", True),
    n("Rycar Ryjerd", True),
    n("Artoo & Threepio", True),
    n("IL-19"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Captain Verrack", True),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Home One"),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Home One: War Room"),
    n("Kiffex"),
    n("Thank The Maker"),
    n("A Jedi's Resilience", qty=3),
    n("Houjix"),
    n("Sense", qty=2),
    n("Escape Pod", True),
    n("Desperate Reach", True),
    n("Inconsequential Barriers"),
    n("Odin Nesloor & First Aid", qty=3),
    n("We're Doomed"),
    n("How Did We Get Into This Mess?", qty=2),
    n("Rebel Leadership", True),
    n("Houjix & Out Of Nowhere"),
    n("Grimtaash"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Hopping Mad", True),
    n("Our Most Desperate Hour", True),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo"),
    n("Blockade Flagship"),
    n("Naboo: Swamp"),
    n("Droid Racks", True),
    n("Prepared Defenses"),
    n("Where Are Those Droidekas?", True),
    n("At Last We Are Getting Results", True),
    n("3,720 To 1", True),
    n("Combat Response"),
    n("Crossfire"),
    n("First Strike"),
    n("Search And Destroy"),
    n("Forced Servitude"),
    n("Master, Destroyers!", qty=2),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Self-Destruct Mechanism", qty=2),
    n("Oh, Switch Off", qty=2),
    n("Wounded Warrior", qty=2),
    n("Imperial Barrier", qty=2),
    n("Those Rebels Won't Escape Us", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Elis Helrot"),
    n("Take Them Away"),
    n("Sniper & Dark Strike"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Battle Plains"),
    n("Blockade Support Ship", qty=2),
    n("Maul's Sith Infiltrator"),
    n("Stinger", True),
    n("Destroyer Droid", qty=9),
    n("P-13 & P-14"),
    n("P-59"),
    n("P-60"),
    n("Guri", qty=2),
    n("Darth Maul"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Daultay Dofine", True),
    n("Tey How"),
    n("Cold Feet", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
