#!/usr/bin/env python3
"""2013 World Championship Day 2: Joe Giannetti Xerox SMO + Local Uprising."""
from __future__ import annotations

PLAYER = "Joe Giannetti"
USERNAME = "Sigga"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 37
DS_PAGE = 36
LS_SCAN = "2013 Worlds Day 2 p37 Joe Giannetti LS.png"
DS_SCAN = "2013 Worlds Day 2 p36 Joe Giannetti DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Joe Giannetti. Username Sigga. "
    "Deck title WTF BBQ. LIGHT. Worlds Day 2. "
    "HFTMF dested Hidden Fortress. "
    "LU / Liberation dested Local Uprising / Liberation. "
    "Lucky Sight dested Lucky Sighting. "
    "Hoth: North Ridge dested Hoth: North Ridge (4th Marker). "
    "Hoth: Main Power Generators dested Hoth: Main Power Generators (1st Marker). "
    "(Non-U) Surprise Assault dested Surprise Assault. "
    "Snowspeeder Garrison dested Snowspeeder Garrison. "
    "Alderaan Consular Ship dested Alderaan Consular Ship. "
    "Hoth: Echo Corridor dested Hoth: Echo Corridor. "
    "Republic Gunship Wing dested Republic Gunship Wing. "
    "Cloud City plaza dested Cloud City: Downtown Plaza. "
    "Han, Chewie & The Falcon dested Han, Chewie, And The Falcon. "
    "Power Harpoon dested Power Harpoon. "
    "All Wings Report In & Darklighter Spin dested "
    "All Wings Report In & Darklighter Spin. "
    "Hoth: Snow Trench dested Hoth: Snow Trench (2nd Marker). "
    "Dash in Rogue 10 dested Dash In Rogue 10. "
    "Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Threepio with his parts showing dested Threepio With His Parts Showing. "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: Echo Docking Bay dested Hoth: Echo Docking Bay. "
    "Hoth: War Room dested Hoth: Echo Command Center (War Room). "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Do or Do Not dested Do, Or Do Not. "
    "Form left column reprints 37–38 on lines 39–40 are Cloud City: Downtown Plaza. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Joe Giannetti. Username Sigga. "
    "Deck title Monkey Pad. DARK. Worlds Day 2. "
    "Spice Mine Operations dested Spice Mine Operations. "
    "Saber Squad TIE dested Saber Squadron TIE. "
    "Saber 4 dested Saber 4. Obsidian 10 dested Obsidian 10. "
    "Saber 2 dested Saber 2. U-3PO dested U-3PO (Yoo-Threepio). "
    "Keder The Black dested Keder The Black. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. "
    "Saber Squad Pilot dested Saber Squadron Pilot. "
    "He Is Not Ready & IP dested He Is Not Ready. "
    "IOTDL dested Image Of The Dark Lord. "
    "MM & EO dested Masterful Move & Endor Occupation. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back!. "
    "APTW dested All Power To Weapons. "
    "Turn it Off dested Turn It Off! Turn It Off!. "
    "Never Yalnal dested Nevar Yalnal. "
    "SFS L-s7.2 laser cannon dested SFS L-s7.2 TIE Cannon. "
    "Kessel Surveillance System dested Kessel Surveillance System. "
    "Tibanna Harvesting Refinery dested Tibanna Floating Refinery. "
    "Kessel: Spice Mines - AO dested Kessel: Spice Mines - Administrator's Office. "
    "We'll Let Fate-a Decide dested We'll Let Fate-A Decide, Huh?. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "Useless Gesture dested A Useless Gesture. "
    "CHYBC dested Come Here You Big Coward. "
    "I Find Your Lack dested I Find Your Lack Of Faith Disturbing. "
    "Form left column reprints 37–38 on lines 39–40 are "
    "Short Range Fighters & Watch Your Back!. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Hidden Fortress"),
    n("Maneuvering Flaps"),
    n("Nick Of Time", True),
    n("Superficial Damage", True),
    n("Wokling", True),
    n("Hoth: North Ridge (4th Marker)"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth"),
    n("Local Uprising / Liberation", True),
    n("Anger, Fear, Aggression", True),
    n("Lucky Sighting", True),
    n("Fixer", True, qty=2),
    n("Rebel Ambush"),
    n("Desperate Reach", qty=2),
    n("Evacuation Control", True),
    n("Surprise Assault", True),
    n("Escape Pod", True, qty=2),
    n("Snowspeeder Garrison"),
    n("Alderaan Consular Ship", True, qty=2),
    n("Were You Looking For Me?", qty=2),
    n("Hoth: Echo Corridor", True),
    n("Let The Wookiee Win", True, qty=4),
    n("Republic Gunship Wing", True, qty=4),
    n("Much To Learn, You Still Have"),
    n("Dual Laser Cannon", True, qty=2),
    n("I Feel The Conflict"),
    n("Cloud City: Downtown Plaza", qty=2),
    n("Lady Luck"),
    n("Han, Chewie, And The Falcon"),
    n("Luke Skywalker", True, qty=2),
    n("Power Harpoon", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Houjix"),
    n("Hoth: Snow Trench (2nd Marker)"),
    n("Dash In Rogue 10"),
    n("Imperial Atrocity", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Senator Leia Organa", True),
    n("Haven"),
    n("Threepio With His Parts Showing"),
    n("A New Secret Base"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Grimtaash"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Battle Plan", True),
    n("Wise Advice", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Traffic Control", True),
    n("Do, Or Do Not", True),
]
LS_ADD = []

DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Spice Mine Operations"),
    n("Saber Squadron TIE", qty=3),
    n("Saber 4"),
    n("Obsidian 10", True),
    n("Saber 2", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Arica"),
    n("Keder The Black", qty=2),
    n("Jango Fett, The Assassin"),
    n("DS-61-2"),
    n("Baron Soontir Fel", qty=2),
    n("Saber Squadron Pilot", qty=3),
    n("He Is Not Ready"),
    n("Imperial Propaganda", True),
    n("Protocol Failure", qty=2),
    n("Image Of The Dark Lord", True),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True),
    n("Abyssin Ornament", qty=2),
    n("Cold Feet", True),
    n("Dark Maneuvers"),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Limited Resources"),
    n("Ghhhk", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("All Power To Weapons", qty=5),
    n("Turn It Off! Turn It Off!"),
    n("Nevar Yalnal"),
    n("Storm Clouds"),
    n("Clouds"),
    n("SFS L-s7.2 TIE Cannon"),
    n("Kessel Surveillance System"),
    n("Tibanna Floating Refinery"),
    n("Combat Readiness", True),
    n("Combat Response", True),
    n("I'll Take Them Myself"),
    n("I'm Sorry", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel"),
    n("Why Didn't You Tell Me?"),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("Imperial Detention"),
]
DS_ADD = [
    n("Reactor Terminal"),
    n("I Find Your Lack Of Faith Disturbing"),
]
