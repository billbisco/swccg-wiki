#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Gabe typed 2013 Print Form LS+DS.

Name field Gabe. Username blank. Dest as written.
"""
from __future__ import annotations

PLAYER = "Gabe"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 SoCal Grand Prix Day 1 p03 Gabe LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p04 Gabe DS.png"
LS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Gabe. Username blank. Deck Name Rebels Senates. Event Name SDGP 2013. LIGHT. "
    "AFA dested Anger, Fear, Aggression. "
    "Plead My Case to the Senate dested Plead My Case To The Senate / Sanity And Compassion. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Gen Crix Madine dested General Crix Madine. "
    "Lt Page dested Lieutenant Page. "
    "Threepio With parts showing dested Threepio With His Parts Showing. "
    "Sen Leia Organa dested Senator Leia Organa. "
    "LS,JK dested Luke Skywalker, Jedi Knight. "
    "CAPT Yutani with blaster cannon dested Captain Yutani With Blaster Cannon. "
    "Sen Padme Amidala dested Senator Padme Amidala. "
    "Bail Organa Father of Rebellion dested Bail Organa, Father Of Rebellion. "
    "Derek Hobbie Klivian dested Derek 'Hobbie' Klivian. "
    "Sen Mon Mothma dested Senator Mon Mothma. "
    "Yoda, MOTF dested Yoda, Master Of The Force. "
    "Gen Calrissian dested General Calrissian. "
    "Sen Hovercam dested Senate Hovercam. "
    "Sai'torr dested Sai'torr Kal Fas. "
    "Lukes Lightsaber dested Luke's Lightsaber. "
    "Line 40 handwritten HCF (Non-V) dested Han, Chewie, And The Falcon. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. "
    "Alderaan Counselor Ship dested Alderaan Consular Ship. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "LTWW dested Let The Wookiee Win. "
    "A Jedis Resilience dested A Jedi's Resilience. "
    "Control/ Tunnel Vision dested Control & Tunnel Vision. "
    "Coruscant: Nightclub dested Coruscant: Night Club. "
    "Coruscant (Cor) dested Coruscant. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Simple Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "lets keep a little optimism dested Let's Keep A Little Optimism Here. "
    "Shields 13-15 empty. (V) from the checkbox."
)
DS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Gabe. Username blank. Deck Name DTRM. Event Name SDGP 2013. DARK. "
    "K&D dested Knowledge And Defense. "
    "SYCFA dested Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Boba Fett, Prep Hunter dested Boba Fett, Prepared Hunter. "
    "Slave 1 SOF dested Slave I, Symbol Of Fear. "
    "Boba Fetts Blaster Rifle dested Boba Fett's Blaster Rifle. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Darth Vader W/ Stick dested Darth Vader With Lightsaber. "
    "Darth Maul W/ Stick dested Darth Maul With Lightsaber. "
    "Mara Jade W/ Stick dested Mara Jade With Lightsaber. "
    "4-Lom W/ Gun dested 4-LOM With Concussion Rifle. "
    "Dengar W/ Gun dested Dengar With Blaster Carbine. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Jabbas Haven dested Jabba's Haven. "
    "A.A.A dested Ability, Ability, Ability. "
    "Imbalance $ Kintan Strider dested Imbalance & Kintan Strider. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Sense & Uncertain is the Furture dested Sense & Uncertain Is The Future. "
    "weapon of an Ungrateful Son dested Weapon Of An Ungrateful Son. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back. "
    "Shields 13-15 empty. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Anger, Fear, Aggression"),
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Strike Planning"),
    n("General Crix Madine"),
    n("Lieutenant Page"),
    n("Mas Amedda"),
    n("Tycho Celchu", True),
    n("Threepio With His Parts Showing"),
    n("Senator Leia Organa", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Captain Yutani With Blaster Cannon", True),
    n("Corran Horn"),
    n("Senator Padme Amidala", True),
    n("Bail Organa", True),
    n("Bail Organa, Father Of Rebellion", True, qty=2),
    n("Derek 'Hobbie' Klivian", True),
    n("Senator Mon Mothma", True),
    n("Yoda, Master Of The Force"),
    n("Mace Windu", True),
    n("Mace Windu"),
    n("General Calrissian"),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("So This Is How Liberty Dies", True),
    n("Senate Hovercam"),
    n("Sai'torr Kal Fas", True),
    n("Disarmed"),
    n("Advantage"),
    n("Lightsaber Proficiency"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Gold Leader In Gold 1", True),
    n("Tantive IV", True),
    n("Alderaan Consular Ship", True),
    n("Wedge In Red Squadron 1", True),
    n("Alter"),
    n("Blaster Deflection", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Chewie, Enraged"),
    n("Let The Wookiee Win", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Control & Tunnel Vision"),
    n("Sense"),
    n("Coruscant: Night Club", True),
    n("Coruscant"),
    n("Houjix & Out Of Nowhere"),
]
LS_SHIELDS = [
    n("The Professor"),
    n("Affect Mind"),
    n("Weapons Display"),
    n("Wise Advice"),
    n("Your Insight Serves You Well"),
    n("Chasm"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here"),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Any Methods Necessary"),
    n("Boba Fett, Prepared Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Boba Fett's Blaster Rifle", True),
    n("Cloud City: Security Tower", True),
    n("Darth Vader With Lightsaber", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Garindan", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Jango Fett, The Assassin", True),
    n("Stormtrooper Garrison"),
    n("ISB Sector Commander", True),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Battle Droid Squad", True),
    n("Myn Kyneugh", True),
    n("Victory", True, qty=2),
    n("Punishing One", True),
    n("Blizzard 4", qty=2),
    n("Blizzard Scout 1", True, qty=2),
    n("First Strike"),
    n("No Escape"),
    n("Jabba's Haven", True),
    n("The Phantom Menace"),
    n("Ability, Ability, Ability", True),
    n("Protocol Failure", True),
    n("Imperial Justice", True),
    n("Broken Concentration", True),
    n("Imbalance & Kintan Strider", True),
    n("Imperial Barrier"),
    n("Force Push", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sense & Uncertain Is The Future"),
    n("You Are Beaten"),
    n("Weapon Of An Ungrateful Son"),
    n("Sneak Attack", True),
    n("Elis Helrot"),
    n("Imperial Command"),
    n("Short Range Fighters & Watch Your Back"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Blockade Flagship: Bridge"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Abyss"),
    n("Battle Order"),
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Leave Them To Me"),
    n("Firepower"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
