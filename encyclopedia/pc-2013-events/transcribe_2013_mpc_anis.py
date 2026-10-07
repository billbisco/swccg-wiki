#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Casey Anis informal LS+DS."""
from __future__ import annotations

PLAYER = "Casey Anis"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2013 Match Play Championship p08 Casey Anis LS.png"
DS_SCAN = "2013 Match Play Championship p07 Casey Anis DS.png"
LS_NOTE = (
    "Informal handwritten list (not a 2010 Xerox Print Form). Light. "
    "AFA → Anger, Fear, Aggression. You Can Either Profit By This → You Can Either Profit By This... / Or Be Destroyed. "
    "Han dested Han With Heavy Blaster Pistol. Cell 2187 as written. "
    "LSJT dested Luke Skywalker, Jedi Knight. Hear Me Baby Hold Together as written. "
    "Strike Force dested Strikeforce. Run Luke Run dested Run Luke, Run!. "
    "Obi-Wan's Lightsaber marked Premiere. Artoo dested R2-D2. "
    "Armed + Dangerous and Krayt Dragon Howl as written. SATM combo dested Sorry About The Mess & Blaster Proficiency. "
    "See-Threepio as written. (V) from parenthetical marks; dittos inherit the first named line."
)
DS_NOTE = (
    "Informal handwritten list (not a 2010 Xerox Print Form). Dark. "
    "K+D → Knowledge And Defense. A Stunning Move dested A Stunning Move / A Valuable Hostage. "
    "Prep Defenses → Prepared Defenses. Ni Chuba Ne dested Ni Chuba Na??. "
    "BF Bridge / Docking Bay / Hallway dested Blockade Flagship sites. "
    "Dr. Evazan combo dested Dr. Evazan & Ponda Baba. Probot dested Probe Droid. "
    "Cyborg Commander, Hunter of Jedi dested Darth Vader. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Masterful Move combo dested Masterful Move & Endor Occupation. "
    "Cyborg Commander's Lightsabers dested Darth Vader's Lightsaber. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Short Range combo dested Short Range Fighters & Watch Your Back. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "He is Not Ready and Imp. Propaganda dested He Is Not Ready. "
    "YCHF dested You Cannot Hide Forever. (V) from parenthetical marks; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han With Heavy Blaster Pistol", True),
    n("Tatooine: Jabba's Palace"),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Cell 2187", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Yavin 4: Massassi War Room", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke's Bionic Hand", qty=2),
    n("Imperial Atrocity", True),
    n("Hear Me Baby, Hold Together", True),
    n("Strike Force", True),
    n("Run Luke, Run!"),
    n("Scrambled Transmission", True),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Obi-Wan's Lightsaber"),
    n("A Gift"),
    n("See-Threepio", True),
    n("R2-D2"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Chewie, Enraged", True, qty=3),
    n("Mace Windu", True, qty=2),
    n("Chewbacca's Bowcaster"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tatooine Utility Belt", True),
    n("Blaster Deflection", qty=2),
    n("Nabrun Leids"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel"),
    n("Leia's Blaster Rifle"),
    n("Sense", qty=2),
    n("Alter"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Nal Hutta"),
    n("Dr. Evazan & Ponda Baba"),
    n("Probe Droid"),
    n("P-59"),
    n("Battle Droid Squad", qty=2),
    n("Darth Vader", True, qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("Restraining Bolt"),
    n("Trophy Of A Kill", qty=3),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Blaster Rack", True),
    n("The Phantom Menace", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Force Field", True, qty=2),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Something Special Planned For Them", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("A Sith's Weapon"),
    n("Blockade Flagship: Hallway"),
    n("Sith Fury", True),
    n("Sniper & Dark Strike"),
    n("Darth Vader's Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Short Range Fighters & Watch Your Back"),
    n("Tarkin's Bounty", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Disarmed", qty=2),
    n("He Is Not Ready"),
    n("Astromech Shortage", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
]
DS_ADD = []
