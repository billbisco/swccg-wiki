#!/usr/bin/env python3
"""2013 Alderaan Regionals: Bren Derlin typed 2010 Print Form LS+DS.

(Vn)/(VD) tags on the printout are Holotable virtual versions.
"""
from __future__ import annotations

PLAYER = "Bren Derlin"
USERNAME = "Bren Derlin"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 17
DS_PAGE = 18
LS_SCAN = "2013 Alderaan Regionals p17 Bren Derlin LS.png"
DS_SCAN = "2013 Alderaan Regionals p18 Bren Derlin DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Communing Pile. "
    "LIGHT/DARK boxes both unchecked; cards are Light (Communing). "
    "(Vn) and (VD) tags on the printout are Holotable virtual versions. "
    "Tatooine (EP1) is the Coruscant system (Tatooine (location))."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Destroyer Droids. "
    "LIGHT/DARK boxes both unchecked; cards are Dark (Invasion). "
    "(Vn) and (VD) tags on the printout are Holotable virtual versions. "
    "Ni Chuba Na?? → Ni Chuba Na?."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Grimtaash"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix", qty=2),
    n("Jedi Levitation", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Inconsequential Barriers"),
    n("A Jedi's Resilience"),
    n("Use The Force", True, qty=2),
    n("Escape Pod", True, qty=3),
    n("Run Luke, Run!", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=4),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior", True),
    n("Shmi Skywalker"),
    n("Wedge Antilles", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Admiral Ackbar", True),
    n("Chewbacca Of Kashyyyk", True),
    n("Corran Horn"),
    n("Han With Heavy Blaster Pistol"),
    n("Leia, Rebel Princess"),
    n("Luke With Lightsaber", qty=3),
    n("Chewie, Enraged", True, qty=3),
    n("Redeemed Apprentice", True),
    n("K'lor'slug", True),
    n("Strikeforce", True),
    n("Launching The Assault"),
    n("Seeking An Audience", True),
    n("Flash Of Insight", True),
    n("Draw Their Fire"),
    n("Tatooine (location)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner", True),
    n("Wokling", True),
    n("Master Kenobi", True),
    n("Communing", True),
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
]
LS_ADD = [
    n("Aim High"),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred"),
]


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Outflank", True),
    n("Cold Feet", True),
    n("Sniper & Dark Strike"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Rolling, Rolling, Rolling"),
    n("Wounded Warrior"),
    n("Self-Destruct Mechanism", qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Master, Destroyers!", qty=2),
    n("Oh, Switch Off!", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Blockade Support Ship", True, qty=2),
    n("Destroyer Droid", qty=9),
    n("P-60", qty=2),
    n("P-59", qty=2),
    n("P-13 & P-14", True),
    n("OOM-9", True),
    n("Rune Haako"),
    n("Tey How"),
    n("Nute Gunray"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Daultay Dofine", True),
    n("Protocol Failure", True),
    n("Forced Servitude"),
    n("3,720 To 1", True),
    n("Crossfire"),
    n("Blast Door Controls"),
    n("Imperial Justice", True, qty=2),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Battle Plains"),
    n("Blockade Flagship: Bridge"),
    n("Ni Chuba Na?", True),
    n("At Last We Are Getting Results", True),
    n("Where Are Those Droidekas?!", True),
    n("Prepared Defenses"),
    n("Droid Racks", True),
    n("Blockade Flagship"),
    n("Naboo: Swamp"),
    n("Naboo"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
]
