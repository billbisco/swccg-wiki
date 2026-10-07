#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 typed slang printout: James Barnes.

Source: 2014-TMW-Day-1.pdf pages 27–28 (typed, not Xerox forms).
"""
from __future__ import annotations

PLAYER = "James Barnes"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 27
DS_PAGE = 28
LS_SCAN = "2014 Texas Mini Worlds Day 1 p27 James Barnes LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p28 James Barnes DS.png"
NOTE = "Typed slang printout (not a handwritten Xerox form)."
LS_NOTE = (
    "Typed slang printout. Name James Barnes. Username blank. Light Side. "
    "Deck title Michael Richards is the Greatest. "
    "AFA dested Anger, Fear, Aggression. WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Spaceport: City dested Corellia: Spaceport City. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Mace Windu, MOTO dested Mace Windu, Master Of The Order. "
    "EPP Qui-gon dested Master Qui-Gon. "
    "Chewie dested Chewie, Enraged. "
    "That's One dested That's One. "
    "LTWW dested Let The Wookiee Win. "
    "Wesa dested Wesa Gotta Grand Army. "
    "Houjix combo dested Houjix & Out Of Nowhere. "
    "SATM combo dested Sorry About The Mess & Blaster Proficiency. "
    "AJR dested A Jedi's Resilience. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Unique overcounts sheet-accurate (Luke Skywalker, Jedi Knight x3, Rebel Leadership x3, "
    "Wesa Gotta Grand Army x3). "
    "(V) from a trailing v on the printout."
)
DS_NOTE = (
    "Typed slang printout. Name James Barnes. Username blank. Dark Side. "
    "Deck title I learned everything from Michael Richards. "
    "K&D dested Knowledge And Defense. "
    "Gift of the Master dested Gift Of The Master. "
    "Ni Chu dested Ni Chuba Na?. "
    "Imperial Arrest Order combo dested Imperial Arrest Order & Secret Shipyard. "
    "Grievous dested Grievous, Hunter Of Jedi. "
    "EPP Maul dested Darth Maul With Lightsaber. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "Boba PH dested Boba Fett, Prepared Hunter. "
    "Nute Gunray dested Nute Gunray. "
    "Aurra DA dested Aurra Sing, Deadly Assassin. "
    "Slave 1 Sof dested Slave I, Symbol Of Fear. "
    "ZiMH dested Zuckuss In Mist Hunter. "
    "Bossk in HT dested Bossk In Hound's Tooth. "
    "SSPFT dested Something Special Planned For Them. "
    "SRF&WYB dested Short Range Fighters & Watch Your Back!. "
    "Imbalance Combo dested Imbalance & Kintan Strider. "
    "Sniper combo dested Sniper & Dark Strike. "
    "Sith Fury combo dested Sith Fury & End This Destructive Conflict. "
    "Coward dested Come Here You Big Coward. "
    "A Sith's Weapon dested Weapon Of A Sith. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "YCHF dested You Cannot Hide Forever. "
    "Naboo 3/2 dested Naboo: Theed Palace Generator Core. "
    "Unique overcounts sheet-accurate (Grievous, Hunter Of Jedi x3, Sonic Bombardment x3). "
    "(V) from a trailing v on the printout."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("General Solo", True),
    n("Corellia: Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Endor: Back Door"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Master Qui-Gon", qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Chewie, Enraged", True),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Guardian's Lightsaber"),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Han's Toolkit", True),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Lightsaber Proficiency"),
    n("That's One", True),
    n("Strikeforce", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("Hear Me Baby, Hold Together", True),
    n("Clash Of Sabers"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection"),
    n("A Jedi's Resilience"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Antilles Maneuver", True, qty=2),
    n("Punch It!", qty=2),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Jabba's Prize", True),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Separatist Uprising / At War With Itself"),
    n("War Has Begun"),
    n("Geonosis: Separatist Council Room"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na?", True),
    n("Imperial Arrest Order & Secret Shipyard"),
    n("Rally The Cause"),
    n("Geonosis"),
    n("Naboo: Theed Palace Generator Core"),
    n("Cloud City: Security Tower", True),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Count Dooku", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Jango Fett, The Assassin", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Nute Gunray", True),
    n("Aurra Sing, Deadly Assassin"),
    n("Durge"),
    n("Keder The Black"),
    n("Darth Sidious"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Bossk In Hound's Tooth", True),
    n("Dark Jedi Lightsaber", qty=2),
    n("Dooku's Lightsaber"),
    n("Trophy Of A Kill"),
    n("Imperial Propaganda", True),
    n("First Strike"),
    n("No Escape"),
    n("Jabba's Haven"),
    n("Empire's New Order"),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("Sonic Bombardment", True, qty=3),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Abyssin Ornament", True, qty=2),
    n("Force Field", qty=2),
    n("Force Lightning"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Imbalance & Kintan Strider"),
    n("You Are Beaten"),
    n("Sniper & Dark Strike"),
    n("Operational As Planned", True),
    n("Sith Fury & End This Destructive Conflict"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Death Star Sentry", True),
    n("Resistance"),
]
DS_ADD = []
