#!/usr/bin/env python3
"""2013 World Championship Day 2: Stephen Kin Xerox A Stunning Move + WYS."""
from __future__ import annotations

PLAYER = "Stephen Kin"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 51
DS_PAGE = 50
LS_SCAN = "2013 Worlds Day 2 p51 Stephen Kin LS.png"
DS_SCAN = "2013 Worlds Day 2 p50 Stephen Kin DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Stephen Kin. Username blank "
    "(MPC Day 1 Username raith; Worlds box empty, omit). "
    "Event Worlds Day 2. LIGHT. Watch Your Step. "
    "Do not rewrite the 2013 MPC Stephen Kin leftover. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Mace Windu dested Mace Windu. "
    "Chewie dested Chewie. "
    "Leia dested Leia. "
    "Ant Man combo dested Antilles Maneuver & Rebel Reinforcements. "
    "AFA dested Anger, Fear, Aggression. "
    "Endor's Back Door dested Endor: Back Door. "
    "Sorry About The Mess dested Sorry About The Mess. "
    "Additional Weapons Display / A Tragedy moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Seeking An Audience / Endor: Back Door. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Stephen Kin. Username blank. "
    "Event Worlds 2013. DARK. A Stunning Move. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage. "
    "Palpatine's Quarters dested Coruscant: Palpatine's Quarters. "
    "Private Platform dested Coruscant: Private Platform (Docking Bay). "
    "Ni Chuba dested Ni Chuba Na??. "
    "Slave I, SoF dested Slave I, Symbol Of Fear. "
    "Darth Maul, VA dested Darth Maul, Young Apprentice. "
    "Galen dested Galen, Secret Apprentice. "
    "Grievous, Hoj dested Grievous, Hunter Of Jedi. "
    "Jango, The Assassin dested Jango Fett, The Assassin. "
    "Fett, Prep H dested Boba Fett, Prepared Hunter. "
    "Dr E combo dested Dr. Evazan & Ponda Baba. "
    "Reeyesk dested Ree-Yees. "
    "Galen, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Grievous saber dested Grievous' Lightsabers. "
    "Maul's Saber (Double) dested Maul's Double-Bladed Lightsaber. "
    "Luke Lunike dested Luke Skywalker. "
    "A Sith Weapon dested A Sith's Weapon. "
    "Where Are You Taking dested Where Are You Taking This ... Thing?. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Sniper combo dested Sniper & Dark Strike. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "BF Bridge / Hallway / Docking Bay dested Blockade Flagship sites. "
    "Short Range Fighters + WYB dested Short Range Fighters & Watch Your Back!. "
    "We'll Fate-a dested We'll Let Fate-a Decide, Huh?. "
    "Coward dested Come Here You Big Coward. "
    "Oppressive dested Oppressive Enforcement. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "YCHF dested You Cannot Hide Forever. "
    "Additional Abyss / Allegations / Battle Order moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Look Sir, Droids / Those Rebels Won't Escape Us. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("General Solo", True),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Mace Windu", True, qty=2),
    n("Jedi Lightsaber", True),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Lando Calrissian, Scoundrel"),
    n("Rebel Leadership", True),
    n("Home One"),
    n("Yavin 4: Massassi War Room", True),
    n("Sense"),
    n("Hear Me Baby, Hold Together", True),
    n("Obi-Wan's Lightsaber"),
    n("Corran Horn"),
    n("Obi-Wan Kenobi", True),
    n("A Few Maneuvers"),
    n("That's One", True),
    n("Chewie", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Leia", True),
    n("A Jedi's Resilience"),
    n("Blaster Deflection"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Padme Naberrie", True),
    n("Wesa Gotta Grand Army"),
    n("A Jedi's Resilience"),
    n("Leia, Rebel Princess"),
    n("Punch It!"),
    n("Control & Tunnel Vision"),
    n("Admiral Ackbar", True),
    n("Seeking An Audience", True),
    n("Endor: Back Door"),
    n("Obi-Wan Kenobi", True),
    n("Sorry About The Mess"),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Rebel Leadership", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Bionic Hand"),
    n("Han's Toolkit", True),
    n("Disarmed"),
    n("Naboo: Boss Nass' Chambers"),
    n("Antilles Maneuver", True),
    n("Home One: War Room"),
    n("Temporary Foothold"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Rebel Leadership", True),
    n("Blaster Deflection"),
    n("Sense"),
    n("Luke Skywalker, Jedi Knight"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Planetary Defenses", True),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master", True),
    n("Jabba's Haven"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("Ree-Yees", True),
    n("Probot"),
    n("Guri"),
    n("Battle Droid Squad"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Blaster Rack", True),
    n("Luke Skywalker", True),
    n("A Sith's Weapon"),
    n("No Escape"),
    n("Protocol Failure"),
    n("Where Are You Taking This ... Thing?"),
    n("The Phantom Menace"),
    n("Blast Door Controls"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sniper & Dark Strike"),
    n("Look Sir, Droids"),
    n("Those Rebels Won't Escape Us", True),
    n("Force Field", True, qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Imperial Barrier", qty=2),
    n("Operational As Planned", True),
    n("Sonic Bombardment", True, qty=3),
    n("Short Range Fighters & Watch Your Back!"),
    n("Force Push", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("Maul Strikes"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Nal Hutta"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Firepower"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
]
DS_ADD = []
