#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Kevin Shannon.

Source: 2012NationalsDay2.pdf pages 11–12 (handwritten 2010 Xerox, 12 shields).
Name Shannon dested Kevin Shannon analog leftover Day 1 / 2013 Alderaan CANON.
Username blank. p11 Light WYS Power Hour's Revenge. p12 Dark Same as Yesterday with In/Out.
Do not dest as a new person. Do not dest Day 1 Shannon 60s again.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2012 US Nationals Day 2 Kevin Shannon LS.png"
DS_SCAN = "2012 US Nationals Day 2 Kevin Shannon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover Day 1. "
    "Username blank. p11 LIGHT checked. p12 DARK checked. "
    "Do not dest as a new person. Do not dest Day 1 Shannon 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover Day 1. "
    "Username blank. LIGHT checked. Deck Name Power Hour's Revenge skip. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough True analog leftover grouty. "
    "Spaceport City dested Corellia: Spaceport City True analog leftover location prefix. "
    "Falcon dested Millennium Falcon analog leftover grouty. "
    "Heading dested Heading For The Medical Frigate True analog leftover grouty. "
    "Wokling dested analog leftover Kelly True. "
    "Back Door dested Endor: Back Door True analog leftover 2014 Worlds. "
    "JCC dested Coruscant: Jedi Council Chamber analog leftover McCune. "
    "Nass Chamber dested Naboo: Boss Nass' Chambers analog leftover Hanson. "
    "H1 War Room dested Home One: War Room analog leftover Nelson. "
    "LSJK dested Luke Skywalker, Jedi Knight analog leftover Kelly empty x2 True x1. "
    "Master Qui-Gon dested analog leftover Herold True x2. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover grouty. "
    "Obi Wans Saber premier dested Obi-Wan's Lightsaber analog leftover. "
    "Jedi Lightsaber dested analog leftover Kelly. "
    "Qui Gon Jins Saber destiny 1 dested Qui-Gon Jinn's Lightsaber analog leftover. "
    "Lukes Saber dested Luke's Lightsaber analog leftover grouty. "
    "Seeking Audience dested Seeking An Audience analog leftover Day 1 Shannon. "
    "Atrocity dested Imperial Atrocity True analog leftover Day 1. "
    "Sai Torr dested Sai'torr Kal Fas analog leftover Day 1 Shannon. "
    "Lightsaber Prof dested Lightsaber Proficiency analog leftover Shaw. "
    "That's One dested analog leftover Cooleo. "
    "Line 40 Blaster Deflection ditto dest qty=2. "
    "LTWW dested Let The Wookiee Win True analog leftover Nelson qty=2. "
    "Impressive Most Impressive dested Impressive, Most Impressive analog leftover Consoli. "
    "Punch It dested Punch It! True analog leftover grouty. "
    "Antilles Maneuver + RR dested Antilles Maneuver & Rebel Reinforcements True analog leftover McCune. "
    "A-JR dested All Wings Report In & Darklighter Spin analog leftover grouty qty=2. "
    "Mess + Blaster Prof dested Sorry About The Mess & Blaster Proficiency analog leftover Nelson qty=2. "
    "Speak w/Jedi Council dested Speak With The Jedi Council analog leftover MPC. "
    "Houjix + OON dested Houjix & Out Of Nowhere True analog leftover MPC. "
    "AFA dested Anger, Fear, Aggression analog leftover grouty IN THE 60. "
    "Shield Lets Keep Optimism dested Let's Keep A Little Optimism Here True analog leftover Herold. "
    "Shield Professor dested The Professor analog leftover Day 1 Shannon. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense True analog leftover Herold. "
    "Shield Tragedy dested A Tragedy Has Occurred True analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover Day 1. "
    "Username blank. DARK checked. Deck Name blank. "
    "Same as Yesterday dested Day 1 Ralltiir Operations / In The Hands Of The Empire analog leftover Consoli In/Out. "
    "OUT Something Special Planned For Them True, Tempest 1, Blizzard 1 True analog leftover Day 1. "
    "IN Tarkin's Bounty dested analog leftover Banger. "
    "IN Darth Sidious dested analog leftover Schoenthal. "
    "IN Blizzard 4 already in Day 1 keep analog leftover Consoli. "
    "Shields Same as Yesterday dest Day 1 shields. Unique 59 sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia"),
    n("Corellia: Spaceport City", True),
    n("General Solo", True),
    n("Millennium Falcon"),
    n("Heading For The Medical Frigate", True),
    n("Wokling", True),
    n("Rycar Ryyder", True),
    n("Quick Draw"),
    n("Endor: Back Door", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Jedi Knight", True),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", qty=2),
    n("Obi-Wan Kenobi", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Chewbacca"),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Seeking An Audience"),
    n("Temporary Foothold"),
    n("Imperial Atrocity", True),
    n("Disarmed", True),
    n("Sai'torr Kal Fas"),
    n("Lightsaber Proficiency"),
    n("That's One"),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Impressive, Most Impressive"),
    n("Punch It!", True),
    n("Rebel Leadership", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Antilles Maneuver"),
    n("Sense"),
    n("Wesa Gotta Grand Army", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Speak With The Jedi Council"),
    n("Houjix & Out Of Nowhere", True),
    n("Desperate Reach", True),
    n("Dark Approach", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor"),
    n("Battle Plan", True),
    n("Weapons Display"),
    n("Aim High", True),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry"),
    n("A Tragedy Has Occurred", True),
    n("Jabba's Prize"),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Arica"),
    n("Masterful Move & Endor Occupation"),
    n("Imperial Justice", True),
    n("Admiral Ozzel"),
    n("Embrace Your Hatred"),
    n("Special Delivery", True),
    n("Outflank", True),
    n("Victory", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jango Fett, The Assassin"),
    n("Sith Bombardment", True),
    n("Sith Bombardment"),
    n("Emperor Palpatine", qty=2),
    n("Lieutenant Commander Arden Lace"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Spaceport Prefect's Office"),
    n("Imperial Barrier"),
    n("Kashyyyk"),
    n("General Nevar"),
    n("Blizzard 4", True),
    n("Imperial Command", qty=2),
    n("Spaceport Street"),
    n("2 FMT"),
    n("Emperor's Shuttle"),
    n("Close Call", True),
    n("A Dark Time For The Rebellion", True),
    n("Young Skywalker"),
    n("Colonel Davod Jon"),
    n("Slave I, Symbol Of Fear"),
    n("Ghhhk"),
    n("Search And Destroy"),
    n("Grand Moff Tarkin", True),
    n("Ralltiir: Spaceport Prefabricated District"),
    n("He Hasn't Come Back Yet"),
    n("General Veers", True),
    n("Gerendel", True, qty=2),
    n("Cloud City: Security Tower", True),
    n("Blizzard 2", True),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Endor"),
    n("Boba Fett, Prepared Hunter"),
    n("Spaceport Docking Bay"),
    n("Ysanne Isard"),
    n("Imperial Propaganda", True),
    n("Grand Admiral Thrawn"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("We'll Call It Even", True),
    n("Why Didn't You Tell Me?"),
    n("Knowledge And Defense", True),
    n("Tarkin's Bounty"),
    n("Darth Sidious"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Abyss"),
    n("Firepower"),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
]
DS_ADD = []
