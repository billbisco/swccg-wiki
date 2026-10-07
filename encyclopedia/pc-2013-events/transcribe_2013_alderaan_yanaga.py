#!/usr/bin/env python3
"""2013 Alderaan Regionals: Ganden Yanaga typed 2010 Print Form LS+DS.

Sheet name Camden Yanaga / Cam Solusar.
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2013 Alderaan Regionals p16 Ganden Yanaga LS.png"
DS_SCAN = "2013 Alderaan Regionals p15 Ganden Yanaga DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Cloud Age Symphony. "
    "Sheet name Camden Yanaga (username Cam Solusar). "
    "Uutik → Uutkik. Trooper Utris M'tec → Trooper Utris M'toc. "
    "Ellors Madak → Ellorrs Madak. Tanus Spijik → Tanus Spijek. "
    "Lesolomy Tacema → Leslomy Tacema. "
    "(V) from the print-form checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Binary Solo. "
    "Sheet name Camden Yanaga (username Cam Solusar). "
    "LIGHT/DARK boxes both unchecked; cards are Dark (Invasion). "
    "Slots 19–27 are joke spellings of Destroyer Droid. "
    "He Is Not Ready (Formerly Propaganda Combo) → He Is Not Ready & Imperial Propaganda. "
    "Short Ranger Fighters → Short Range Fighters. "
    "(V) from the print-form checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("All My Urchins & Cloud City Celebration"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("Cloud City: West Gallery"),
    n("Aayla Secura", qty=2),
    n("Harc Seff", True),
    n("Uutkik", True),
    n("Kal'Falnl C'ndros"),
    n("Sergeant Edian", True),
    n("Trooper Utris M'toc"),
    n("Dash Rendar", True),
    n("Mirax Terrik"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Leia, Rebel Princess"),
    n("Luke With Lightsaber"),
    n("Kebyc", True),
    n("Yoxgit"),
    n("Caldera Righim"),
    n("Tanus Spijek", True),
    n("Lobot", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Chewbacca, Walking Carpet"),
    n("Leslomy Tacema", True),
    n("Leesub Sirln", True),
    n("Melas", True),
    n("Errant Venture"),
    n("Lady Luck"),
    n("Booster In Pulsar Skate"),
    n("Overseer"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Landing Claw"),
    n("Rebel Barrier", qty=2),
    n("Desperate Reach", True),
    n("Choke"),
    n("Let The Wookiee Win", True, qty=2),
    n("Path Of Least Resistance"),
    n("Path Of Least Resistance & Revealed"),
    n("Dark Approach", True),
    n("Dark Approach"),
    n("Alter", True),
    n("Alternatives To Fighting"),
    n("It's A Trap!"),
    n("Imperial Atrocity", True),
    n("Ellorrs Madak", True),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("No Questions Asked"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
]
LS_ADD = [
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Do, Or Do Not"),
]


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Droid Racks", True),
    n("Naboo"),
    n("Blockade Flagship"),
    n("Naboo: Swamp"),
    n("Prepared Defenses"),
    n("3,720 To 1", True),
    n("Where Are Those Droidekas?!", True),
    n("At Last We Are Getting Results", True),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Throne Room"),
    n("Blockade Flagship: Bridge"),
    n("P-59", qty=2),
    n("P-60", qty=2),
    n("P-13 & P-14"),
    n("Destroyer Droid", qty=9),
    n("Daultay Dofine", True),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Guri", qty=2),
    n("Darth Maul", qty=2),
    n("Stinger", True),
    n("Maul's Sith Infiltrator"),
    n("Blockade Support Ship"),
    n("Crossfire"),
    n("Tarkin's Bounty", True),
    n("Forced Servitude"),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Master, Destroyers!", qty=2),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Wounded Warrior", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Oh, Switch Off!"),
    n("Outflank", True),
    n("Elis Helrot"),
    n("Sniper & Dark Strike"),
    n("We Must Accelerate Our Plans", qty=3),
    n("You Cannot Hide Forever"),
    n("Self-Destruct Mechanism"),
    n("Something Special Planned For Them", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Abyss", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("You Cannot Hide Forever", True),
    n("Fanfare"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = [
    n("Do They Have A Code Clearance?", True),
    n("Leave Them To Me", True),
    n("Imperial Detention", True),
]
