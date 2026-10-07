#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: John Veasey Xerox LS+DS."""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = "veez"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 103
DS_PAGE = 104
LS_SCAN = "2013 Match Play Championship p103 John Veasey LS.png"
DS_SCAN = "2013 Match Play Championship p104 John Veasey DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. John Veasey. Light. Username veez. Starting Communing. "
    "Tatooine Slave Quarters dested Tatooine: Slave Quarters. "
    "Maneuvering Flaps and Nick of Time dested Maneuvering Flaps & Nick Of Time. "
    "Tatooine Jundland Wastes dested Tatooine: Jundland Wastes. Tatooine (EP1) dested Tatooine. "
    "Tatooine Obi-Wan Hut dested Tatooine: Obi-Wan's Hut. Dual Laser Cannons dested Dual Laser Cannon. "
    "Padme Naberrie dested Padme Naberrie. Threepio With Parts Showing dested Threepio With His Parts Showing. "
    "Let's Go Left dested Let's Go Left. Strike Force dested Strikeforce. "
    "Obi-Wan's Apprentice dested Anakin Skywalker, Padawan Learner. "
    "Yub Yub Commander dested Yub Yub, Commander. Hear Me Baby dested Hear Me Baby, Hold Together. "
    "Antilles Maneuver and Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "It's Not My Fault dested It's Not My Fault!. "
    "Form left column reprints 37–38 on lines 39–40 are Let's Go Left and Seeking An Audience. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. John Veasey. Dark. Username veez. "
    "A Stunning Move / Available Hostages dested A Stunning Move / A Valuable Hostage. "
    "Coruscant Palpatine's Quarters dested Coruscant: Palpatine's Quarters. "
    "Coruscant Private Platform dested Coruscant: Private Platform (Docking Bay). "
    "Ni Chuba Na dested Ni Chuba Na. Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Galen Secret Apprentice dested Galen Marek, Starkiller. TC Bodyguard droid dested TC-14. "
    "Battle Droid Squadron dested Battle Droid Squad. "
    "Dr Evazan and Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "4LOM With Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Galen Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Maul's Double Bladed Lightsaber dested Maul's Double-Bladed Lightsaber. "
    "Image of the Dark Lord dested Image Of The Dark Lord. "
    "Sniper and Dark Strike dested Sniper & Dark Strike. "
    "Imbalance and Kintan Strider dested Imbalance & Kintan Strider. "
    "Short Range Fighters and Watch Your Back dested Short Range Fighters & Watch Your Back. "
    "Masterful Move and Endor Occup dested Masterful Move & Endor Occupation. "
    "He Is Not Ready and Imperial Propaganda dested He Is Not Ready. "
    "A Dark For the Rebellion dested A Dark Time For The Rebellion. "
    "Form left column reprints 37–38 on lines 39–40 are Imperial Justice and No Escape. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Maneuvering Flaps & Nick Of Time"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Rebel Gunrunner"),
    n("Dual Laser Cannon", True),
    n("Padme Naberrie", True),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Commander Wedge Antilles", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Zev Senesca"),
    n("Derek 'Hobbie' Klivian"),
    n("Corporal Beezer", True),
    n("Admiral Ackbar", True),
    n("Captain Verrack", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Rogue 1", qty=2),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Han, Chewie, And The Falcon", True),
    n("Lady Luck"),
    n("Home One"),
    n("Let's Go Left", True, qty=2),
    n("Seeking An Audience", True),
    n("Flash Of Insight", True, qty=3),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Evacuation Control"),
    n("Menace Fades"),
    n("Echo Base Garrison"),
    n("We're Doomed"),
    n("Houjix"),
    n("It's Not My Fault!", True, qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Yub Yub, Commander"),
    n("Hear Me Baby, Hold Together"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Escape Pod", True),
    n("Scrambled Transmission", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na", True),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Knowledge And Defense", True),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower", True),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Battle Droid Squad"),
    n("TC-14"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("P-59"),
    n("Dark Jedi Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Imperial Propaganda", True),
    n("Blaster Rack", True),
    n("Where Are You Taking This ... Thing?"),
    n("Imperial Justice"),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("A Sith's Weapon"),
    n("Image Of The Dark Lord", True),
    n("The Phantom Menace", qty=2),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("Imbalance & Kintan Strider"),
    n("Force Field", True, qty=2),
    n("Sonic Bombardment", True),
    n("Maul Strikes"),
    n("Control"),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion"),
    n("Short Range Fighters & Watch Your Back"),
    n("Masterful Move & Endor Occupation"),
    n("Sonic Bombardment"),
    n("Battle Droid Squad"),
    n("He Is Not Ready"),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Firepower", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("There Is No Try", True),
    n("Abyss", True),
]
DS_ADD = []
