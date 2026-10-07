#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Chris Terwilliger.

Source: Nationals-2014-day-1.pdf pages 13–14 (2010 form).
Name Chris Twigg. Username Vader322. Dest Chris Terwilliger.
p13 Dark Hunt Down Walkers. p14 Light IITFYS / Y4.
"""
from __future__ import annotations

PLAYER = "Chris Terwilliger"
USERNAME = "Vader322"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2014 US Nationals Day 1 p14 Chris Terwilliger LS.png"
DS_SCAN = "2014 US Nationals Day 1 p13 Chris Terwilliger DS.png"
NOTE = "Handwritten 2010 Xerox. Name Chris Twigg; username Vader322 dested Chris Terwilliger."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Twigg. Username Vader322. Deck name Y4. "
    "IITFYS dested It Is The Future You See / A Tremor In The Force. "
    "Do or do not & Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Battle Plan & Draw Their Fire dested Battle Plan & Draw Their Fire. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Mace Windu, Master of the Order dested Mace Windu, Master Of The Order. "
    "Luke Skywalker, Strong in the Force dested Luke Skywalker, Strong In The Force. "
    "Obi-Wan Kenobi, Jedi Knight dested Obi-Wan Kenobi, Jedi Knight. "
    "Master Qui-Gon dested Master Qui-Gon. SATM dested Sorry About The Mess. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Control Combo dested Control & Tunnel Vision. AFA dested Anger, Fear, Aggression. "
    "Unique overcounts sheet-accurate (Escape Pod x2, Wesa Gotta Grand Army x3, "
    "Rebel Leadership x3, Let The Wookiee Win x3, Luke Skywalker, Jedi Knight x2, "
    "Master Qui-Gon x2, Clash Of Sabers x2, Sense x2). (V) from checkbox. "
    "Hoth: War Room dested Hoth: Echo Command Center (War Room). "
    "NO_DEST (2014 index): What Are You Tryin' To Push On Us?."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Twigg. Username Vader322. Deck name HDv. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Hoth Marker 1 dested Hoth: Main Power Generators. Marker 6 dested Hoth: Wampa Cave. "
    "Marker 5 dested Hoth: North Ridge. Marker 3 dested Hoth: Defensive Perimeter. "
    "Control & Set For Stun dested Control & Set For Stun. Ni Chuba Na dested Ni Chuba Na??. "
    "Jango Fett, the Assassin dested Jango Fett, The Assassin. "
    "Juno Eclipse, Black Leader dested Juno Eclipse. "
    "Maarek Stele, The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "K+D dested Knowledge And Defense. Unique overcounts sheet-accurate "
    "(We're In Attack Position Now x2, Imperial Command x3, Force Push x2, "
    "A Dark Time For The Rebellion x2, Imperial Decree x2, Blizzard 4 x2, Victory x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Escape Pod", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Speak With The Jedi Council"),
    n("Mechanical Failure"),
    n("Seeking An Audience", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Mace Windu, Master Of The Order", True),
    n("Mace Windu", True),
    n("Jedi Lightsaber", True),
    n("Home One", True),
    n("Lady Luck", True),
    n("Imperial Atrocity"),
    n("Sense", qty=2),
    n("Houjix", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Master Qui-Gon", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Jedi Levitation"),
    n("A Jedi's Resilience"),
    n("Flash Of Insight", True),
    n("Projection Of A Skywalker"),
    n("Blaster Deflection", True),
    n("Sai'torr Kal Fas", True),
    n("Threepio With His Parts Showing"),
    n("What Are You Tryin' To Push On Us?"),
    n("Sorry About The Mess"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers", qty=2),
    n("Control & Tunnel Vision"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here"),
    n("Don't Do That Again", True),
    n("Affect Mind", True),
]
LS_ADD = [
    n("Only Jedi Carry That Weapon"),
    n("There Is Another"),
    n("He Can Go About His Business"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Wampa Cave"),
    n("Hoth: North Ridge"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("We're In Attack Position Now", qty=2),
    n("Cease Fire!"),
    n("Alert My Star Destroyer!"),
    n("Hoth Blockade", True),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Control & Set For Stun"),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing", True),
    n("Do They Have A Code Clearance?"),
    n("Endor Shield", True),
    n("Imperial Command", qty=3),
    n("Trample"),
    n("Force Push", True, qty=2),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Stop Motion", True),
    n("Sniper & Dark Strike"),
    n("Walker Garrison"),
    n("Prepared Defenses", True),
    n("Crash Landing"),
    n("U-3PO (Yoo-Threepio)"),
    n("Admiral Ozzel"),
    n("Commander Igar", True),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader", True),
    n("Grand Moff Tarkin", True),
    n("Admiral Piett"),
    n("AT-AT Commander", True),
    n("Veers", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Grand Admiral Thrawn"),
    n("Garindan", True),
    n("Jango Fett, The Assassin", True),
    n("Cold Feet", True),
    n("Blizzard 4", qty=2),
    n("Blizzard 1", True),
    n("Tempest 1"),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6"),
    n("Victory", True, qty=2),
    n("Conquest", True),
    n("Flagship Executor"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Leave Them To Me"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever"),
    n("Wipe Them Out, All Of Them"),
    n("Death Star Sentry", True),
    n("Fanfare"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Abyss", True),
    n("Firepower", True),
    n("Allegations Of Corruption"),
]
