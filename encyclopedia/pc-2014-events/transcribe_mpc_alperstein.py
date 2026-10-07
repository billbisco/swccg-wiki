#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Barry Alperstein.

Source: MPC-2014-Day-1-Main-Event.pdf pages 1–2 (2013 form, 15 shields).
Username blank. Light deck name: I clearly have no clue what I am doing.
"""
from __future__ import annotations

PLAYER = "Barry Alperstein"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2014 Match Play Championship Day 1 Barry Alperstein LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Barry Alperstein DS.png"
LS_DECK_NAME = "I clearly have no clue what I am doing"
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. Deck name I clearly have no clue "
    "what I am doing. LIGHT checked. Yavin 4 (V) is the starting location "
    "(no Objective). Harc Seff dested Harc Seff. Lando, UH dested Lando "
    "Calrissian, Unlikely Hero. Yoda, CW dested Yoda, Great Warrior. "
    "Don't Get dested Don't Get Cocky. H,C + F dested Han, Chewie, And The Falcon. "
    "Mace MOTO dested Mace Windu, Master Of The Order. Control + TV dested "
    "Control & Tunnel Vision. Houjix + Out of Nowhere dested Houjix & Out Of Nowhere. "
    "AFA dested Anger, Fear, Aggression. Nar Shadda Wind Chimes dested "
    "Nar Shaddaa Wind Chimes. OICTA dested OICTW. YTSYG dested Your Insight "
    "Serves You Well. Shield 1 Yavin Sentry (V). Waggady dested as written. "
    "Unique overcounts sheet-accurate (Fire Extinguisher x5, Nar Shaddaa Wind "
    "Chimes x3, Rebel Leadership x3, It's Not My Fault (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. DARK checked. ASM dested "
    "A Stunning Move / A Valuable Hostage (starting Objective). K+D (V) dested "
    "Knowledge And Defense (V). Cor: Palo's Quarters dested Coruscant: Palpatine's "
    "Quarters. Flagship: DB dested Blockade Flagship: Docking Bay. Sniper + DS "
    "dested Sniper & Dark Strike. YAR dested You Are Beaten. MM + EO dested "
    "Masterful Move & Endor Occupation. Short Range Fighters + WYB dested "
    "Short Range Fighters & Watch Your Back!. Ni Chuba Na dested Ni Chuba Na??. "
    "Gift of The Mentor dested Gift Of The Master. Cyborg Commander dested "
    "Grievous, Hunter Of Jedi. Galen dested Galen Marek, Starkiller. Jango, "
    "Father of Fett dested Jango Fett, The Assassin. Dr. E + Ponda dested "
    "Dr. Evazan & Ponda Baba. Bodyguard Droid dested IG-100 MagnaGuard. "
    "P-59 dested P-59. Reegesh dested Reegesh. Galen's Saber, Vader's Grip dested "
    "Galen's Lightsaber, Vader's Gift. Maul's Double Bladed dested Maul's "
    "Double-Bladed Lightsaber. Slave I, SOF dested Slave I, Symbol Of Fear. "
    "AUG dested A Useless Gesture. Let Fate Decide dested We'll Let Fate-a "
    "Decide, Huh?. YCHF dested You Cannot Hide Forever. Allegiance dested "
    "Allegiance. Unique overcounts sheet-accurate (Sith Fury (V) x3, Force Field "
    "(V) x2, Galen x2, Darth Maul, Young Apprentice x3). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Yavin 4: Massassi Headquarters"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
    n("Restore Freedom To The Galaxy"),
    n("Haven"),
    n("Massassi Base Sentry"),
    n("Return Of The Jedi"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Wokling", True),
    n("Luke, Trust Me"),
    n("Cell 2187", True),
    n("Harc Seff"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Luke Skywalker", True),
    n("Baragwin", qty=2),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Artoo-Detoo In Red 5", True),
    n("Threepio With His Parts Showing", True),
    n("Yoda, Great Warrior"),
    n("Mace Windu, Master Of The Order"),
    n("Han, Chewie, And The Falcon", True),
    n("Han, Chewie, And The Falcon"),
    n("Wedge In Red Squadron 1", qty=2),
    n("Lady Luck"),
    n("Don't Get Cocky"),
    n("X-wing Laser Cannon"),
    n("Fire Extinguisher", qty=5),
    n("Nar Shaddaa Wind Chimes", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("It's Not My Fault", True, qty=2),
    n("Punch It", qty=2),
    n("Droid Shutdown", qty=2),
    n("It's A Trap", qty=2),
    n("Either Way, You Win", True, qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Desperate Reach", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Careful Planning", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Wise Advice", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Waggady"),
    n("Jabba's Prize", True),
    n("OICTW", True),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Nal Hutta"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Prepared Defenses", True),
    n("Sniper & Dark Strike"),
    n("You Are Beaten"),
    n("Ghhhk"),
    n("Force Push", True),
    n("Masterful Move & Endor Occupation"),
    n("Imperial Barrier", qty=2),
    n("Oh, Switch Off"),
    n("Cold Feet", True),
    n("Force Field", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sith Fury", True, qty=3),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("A Sith's Weapon"),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("Disarmed", qty=2),
    n("The Phantom Menace", qty=2),
    n("No Escape"),
    n("Imperial Justice", True),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan & Ponda Baba", qty=2),
    n("IG-100 MagnaGuard", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Battle Droid Squad", qty=2),
    n("P-59"),
    n("Reegesh", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Dark Jedi Lightsaber", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance"),
    n("Death Star Sentry"),
    n("Firepower", True),
    n("Weapon Of A Sith"),
    n("Resistance"),
    n("Abyss", True),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
