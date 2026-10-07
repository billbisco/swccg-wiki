#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Fernando.

Source: 2012NationalsDay1.pdf pages 21–22 (typed 2010 Xerox, 12 shields).
Name Fernando dested Fernando as written first-name-only. Username blank.
p21 Light Ferndawg / Naboo.
p22 Dark Morgoth / Ralltiir Operations.
Do not dest as Fernando Castañón. Do not dest as Fernando Souza.
"""
from __future__ import annotations

PLAYER = "Fernando"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2012 US Nationals Day 1 Fernando LS.png"
DS_SCAN = "2012 US Nationals Day 1 Fernando DS.png"
LS_DECK_NAME = "Ferndawg"
DS_DECK_NAME = "Morgoth"
NOTE = "Typed 2010 Xerox form. Username blank. Event Date empty Event Name empty."
LS_NOTE = (
    "Typed 2010 Xerox. Name Fernando dested Fernando as written first-name-only. "
    "Username blank. LIGHT checked. Deck Name Ferndawg. "
    "Event Date empty Event Name empty. Do not dest as Fernando Castañón. Do not dest as Fernando Souza. "
    "Naboo dested Naboo analog leftover Devin START. "
    "Wesa Ready To Do Our-sa Part dested Wesa Ready To Do Our-Sa Part True analog leftover Cooleo. "
    "Anger, Fear dested Anger, Fear, Aggression True analog leftover Bali. "
    "Rep Been dested Rep Been leftover_xerox analog leftover Devin. "
    "2-1B crossed dest Admiral Ackbar True. "
    "Senator Jar Jar dested Senator Jar Jar Binks True analog leftover Brodsky. "
    "Famba dested Fambaa analog leftover. "
    "Kaadu crossed dest Scrambled Transmission True. "
    "Kaduu dested Kaadu analog leftover Devin. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements True analog leftover Grant. "
    "We Gotta Grand Army dested Wesa Gotta Grand Army analog leftover Frafjord. "
    "True vs empty kept separate. Unique 60. Shields 6 slots 7–12 blank skip."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Fernando dested Fernando as written first-name-only. "
    "Username blank. DARK checked. Deck Name Morgoth. "
    "Event Date empty Event Name empty. Do not dest as Fernando Castañón. Do not dest as Fernando Souza. "
    "Ralltiir Operations dested Ralltiir Operations empty analog leftover Harpster. "
    "Knowledge and Defence dested Knowledge And Defense analog leftover Cooleo IN THE 60. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi True analog leftover walker. "
    "Ice Heart dested Ysanne Isard True analog leftover Jessica. "
    "Boba Fett In Slave 1 dested Boba Fett In Slave I True analog leftover Frafjord. "
    "Dark jedi lightsaber dested Dark Jedi Lightsaber analog leftover Frafjord. "
    "Alter & Collateral damage dested Alter & Collateral Damage analog leftover. "
    "It's worse dested leftover_xerox analog leftover TYPE_OVERRIDE. "
    "I'd Just As Soon Kiss A Wookie dested I'd Just As Soon Kiss A Wookiee analog leftover Grant. "
    "Sunsdowm dested Sunsdown & Too Cold For Speeders analog leftover. "
    "Victory True dest without extra (V) analog leftover Frafjord. "
    "Oppresive dested Oppressive Enforcement True analog leftover. "
    "True vs empty kept separate. Unique 60. Shields 5 slots 6–12 blank skip."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Naboo"
LS_CARDS = [
    n("Naboo"),
    n("Naboo: Boss Nass' Chambers"),
    n("Careful Planning", True),
    n("Superficial Damage", True),
    n("Wokling", True),
    n("Wesa Ready To Do Our-Sa Part", True),
    n("Anger, Fear, Aggression", True),
    n("Naboo: Swamp"),
    n("Naboo: Battle Plains"),
    n("Naboo: Otoh Gunga Entrance"),
    n("Jar Jar Binks"),
    n("Gungan Guard", qty=3),
    n("Gungan Warrior", qty=4),
    n("Gungan General", qty=3),
    n("Rep Been"),
    n("Chewie With Blaster Rifle"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Admiral Ackbar", True),
    n("Captain Tarpals"),
    n("Senator Jar Jar Binks", True),
    n("Fambaa", qty=3),
    n("Spiral"),
    n("Home One"),
    n("Republic Corvette"),
    n("Electropole", qty=5),
    n("Booma", qty=2),
    n("Scrambled Transmission", True),
    n("Kaadu"),
    n("Slight Weapons Malfunction", qty=3),
    n("Tunnel Vision"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Wesa Gotta Grand Army"),
    n("Houjix"),
    n("The Signal"),
    n("Big Boomers!"),
    n("Rebel Leadership"),
    n("Steady, Steady"),
    n("Gungan Energy Shield", qty=3),
    n("Brisky Morning Munchen"),
    n("Capital Support", qty=3),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Do, Or Do Not", True),
    n("Chasm", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
    n("Battle Plan", True),
]
LS_ADD = []

DS_START = "Ralltiir Operations"
DS_CARDS = [
    n("Ralltiir Operations"),
    n("Prepared Defenses"),
    n("Insignificant Rebellion", True),
    n("Endor Shield", True),
    n("Imperial Arrest Order"),
    n("Knowledge And Defense"),
    n("Ralltiir"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Prefect's Office"),
    n("Ralltiir: Spaceport Financial District", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Janus Greejatus"),
    n("DS-61-2"),
    n("General Veers", True),
    n("The Emperor", True),
    n("Colonel Davod Jon"),
    n("Lt. Shann Childsen"),
    n("Ysanne Isard", True),
    n("Lord Sidious", True),
    n("Darth Vader With Lightsaber", qty=3),
    n("Admiral Ozzel"),
    n("General Nevar", True),
    n("Imperial Stormtrooper", True),
    n("Major Mianda"),
    n("Officer Evax"),
    n("M'iiyoom Onith"),
    n("Commander Praji", True),
    n("Grand Admiral Thrawn"),
    n("DS-181-4"),
    n("Sergeant Barich"),
    n("Captain Jonus"),
    n("Sergeant Irol"),
    n("OS-72-10"),
    n("Dengar In Punishing One"),
    n("Victory", True),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Blizzard 4"),
    n("Blizzard Walker"),
    n("Dark Jedi Lightsaber"),
    n("You Overestimate Their Chances"),
    n("Limited Resources"),
    n("Tauntaun Skull"),
    n("Ghhhk"),
    n("Alter & Collateral Damage"),
    n("Dark Strike"),
    n("It's Worse"),
    n("Outflank", True),
    n("Ng'ok"),
    n("I'd Just As Soon Kiss A Wookiee"),
    n("Shocking Revelation"),
    n("Something Special Planned For Them", True),
    n("Reactor Terminal"),
    n("Overseeing It Personally"),
    n("Sunsdown & Too Cold For Speeders"),
    n("Lateral Damage"),
    n("Black Sun Fleet"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Secret Plans", True),
    n("Resistance", True),
]
DS_ADD = []
