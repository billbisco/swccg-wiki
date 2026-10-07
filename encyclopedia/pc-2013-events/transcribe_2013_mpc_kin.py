#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Stephen Kin Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Stephen Kin"
USERNAME = "raith"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 47
DS_PAGE = 48
LS_SCAN = "2013 Match Play Championship p47 Stephen Kin LS.png"
DS_SCAN = "2013 Match Play Championship p48 Stephen Kin DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Stephen Kin. Username raith. Light. "
    "Deck title See you... Space Cowboy. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "LS,JK dested Luke Skywalker, Jedi Knight. Luke's Saber dested Luke's Lightsaber. "
    "Qui-Gon w/ saber dested Qui-Gon Jinn With Lightsaber. Chewie dested Chewie, Enraged. "
    "Antilles Maneuver / Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Sorry about the mess / Blaster Prof. dested Sorry About The Mess & Blaster Proficiency. "
    "Hear Me Baby Hold Together dested Hear Me Baby, Hold Together. "
    "Strike Force dested Strikeforce. Jedi's Prize dested Jabba's Prize. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "More Wisdom as written. "
    "Form left column reprints 37–38 on lines 39–40 are More Wisdom. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Stephen Kin. Username raith. Dark. "
    "Deck title Piano Black. A Stunning Move. "
    "Ni Chuba Ma dested Ni Chuba Na?. CC: Security Tower dested Cloud City: Security Tower. "
    "Reeyesk dested Ree-Yees. The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. Darth Maul, VA dested Darth Maul, Young Apprentice. "
    "BF: Docking Bay / Hallway / Bridge dested Blockade Flagship sites. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Galen's saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg Commander dested General Grievous. Cyborg Commander's saber dested Grievous' Lightsabers. "
    "Short Range Fighters / Watch Your Back dested Short Range Fighters & Watch Your Back. "
    "Sniper / Dark Strike dested Sniper & Dark Strike. "
    "Sith Fury / ETDC dested Sith Fury & End This Destructive Conflict. "
    "Dr E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "He isnt ready / Imperial Propaganda dested He Is Not Ready. "
    "Where are you taking this thing dested Where Are You Taking This ... Thing?. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Garrison as written. Protest as written. "
    "Form left column reprints 37–38 on lines 39–40 are Garrison and Blow Parried. "
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
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Anger, Fear, Aggression", True),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Sai'torr Kal Fas", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Luke's Bionic Hand"),
    n("Luke's Lightsaber"),
    n("Rebel Leadership", True, qty=3),
    n("Punch It!"),
    n("Sense", qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Disarmed"),
    n("Obi-Wan Kenobi", True),
    n("Home One: War Room"),
    n("Chewie, Enraged", True),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Leia, Rebel Princess"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Antilles Maneuver", True),
    n("Hear Me Baby, Hold Together", True),
    n("More Wisdom", True, qty=2),
    n("Lightsaber Proficiency"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan Kenobi", True),
    n("A Jedi's Resilience", qty=2),
    n("Endor: Back Door"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Han's Toolkit", True),
    n("Obi-Wan's Journal"),
    n("A Few Maneuvers"),
    n("Seeking An Audience", True),
    n("Lando Calrissian, Scoundrel"),
    n("Yavin 4: Massassi War Room", True),
    n("That's One", True),
    n("Temporary Foothold"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Lightsaber", True),
    n("Smoke Screen"),
    n("Imperial Atrocity", True),
    n("Strikeforce", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Jabba's Prize"),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("A Stunning Move"),
    n("Insidious Prisoner"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Knowledge And Defense", True),
    n("Cloud City: Security Tower", True),
    n("Ree-Yees", True),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Guri"),
    n("Blaster Rack", True),
    n("Blockade Flagship: Docking Bay"),
    n("Force Push", True),
    n("Short Range Fighters & Watch Your Back", True),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen Marek, Starkiller", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("General Grievous", qty=2),
    n("Nal Hutta"),
    n("Blockade Flagship: Hallway"),
    n("Grievous' Lightsabers"),
    n("Force Field", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Sniper & Dark Strike"),
    n("Garrison", True),
    n("Blow Parried"),
    n("Imperial Barrier", qty=2),
    n("Protest"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Battle Droid Squad"),
    n("Dr. Evazan & Ponda Baba"),
    n("Disarmed", qty=2),
    n("Cold Feet", True),
    n("Blast Door Controls"),
    n("Stunning Leader"),
    n("Imperial Justice", True),
    n("Victory"),
    n("No Escape"),
    n("Blockade Flagship: Bridge"),
    n("Where Are You Taking This ... Thing?"),
    n("The Phantom Menace"),
    n("Something Special Planned For Them", True),
    n("Masterful Move & Endor Occupation"),
    n("He Is Not Ready"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
