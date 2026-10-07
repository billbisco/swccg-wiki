#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Peter Tenneson Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Peter Tenneson"
USERNAME = "patmagroin"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 93
DS_PAGE = 94
LS_SCAN = "2013 Match Play Championship p93 Peter Tenneson LS.png"
DS_SCAN = "2013 Match Play Championship p94 Peter Tenneson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Peter Tenneson. Light. Deck title TRM. Username patmagroin. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room. "
    "Armed + Dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "Sai'torr dested Sai'torr Kal Fas. Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "Naked 3PO dested Threepio With His Parts Showing. Control Combo dested Control & Tunnel Vision. "
    "SATM Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. R2 in ship dested Artoo-Detoo In Red 5. "
    "LTWW dested Let The Wookiee Win. Found Someone Combo dested Found Someone You Have & Higher Ground. "
    "HTFMF dested Heading For The Medical Frigate. Ant Man Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "AJR dested A Jedi's Resilience. Houjix Combo dested Houjix & Out Of Nowhere. "
    "EPP Qui Gon dested Qui-Gon Jinn With Lightsaber. HCF dested Han, Chewie, And The Falcon. "
    "Leia RP dested Leia, Rebel Princess. Speak With The JCC dested Speak With The Jedi Council. "
    "Form left column reprints 37–38 on lines 39–40 are Leia and Luke's Bionic Hand. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Peter Tenneson. Dark. Deck title ROPS. Username patmagroin. "
    "ROPS / Flip side dested Ralltiir Operations / In The Hands Of The Empire. "
    "Spaceport DB dested Spaceport Docking Bay. Imp Domination dested Imperial Domination. "
    "Justice dested Imperial Justice. KDY dested Kuat Drive Yards. E Shield dested Endor Shield. "
    "Insig Rebellion dested Insignificant Rebellion. Col. Davod Jon dested Colonel Davod Jon. "
    "Janus dested Janus Greejatus. Emperor Palpy dested Emperor Palpatine. "
    "DVDLOTS dested Darth Vader, Dark Lord Of The Sith. Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Dark Time dested A Dark Time For The Rebellion. Control Combo dested Control & Set For Stun. "
    "EPP Kir Kanos dested Kir Kanos With Force Pike. MM Combo dested Masterful Move & Endor Occupation. "
    "Lt. Comm. Ardan dested Lieutenant Commander Ardan. GMT dested Grand Moff Tarkin. "
    "Ice heart dested Ysanne Isard. Barrier dested Imperial Barrier. "
    "Thrawn dested Grand Admiral Thrawn. Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "K&D dested Knowledge And Defense. CHYBC dested Come Here You Big Coward. "
    "YCHFF dested You Cannot Hide Forever. Ralltiir: Financial District dested Ralltiir: Spaceport Financial District. "
    "Form left column reprints 37–38 on lines 39–40 are Trample and Blizzard 4. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Obi-Wan's Journal"),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Jedi Lightsaber", True),
    n("Mace Windu", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Rebel Leadership", True),
    n("Threepio With His Parts Showing"),
    n("Control & Tunnel Vision"),
    n("Either Way, You Win", True),
    n("Blaster Deflection"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Quick Draw", True),
    n("Luke Skywalker, Strong In The Force", True),
    n("Artoo-Detoo In Red 5"),
    n("Wokling", True),
    n("Let The Wookiee Win", True),
    n("Found Someone You Have & Higher Ground", True),
    n("Mace Windu", True),
    n("Luke Skywalker, Strong In The Force", True),
    n("Obi-Wan Kenobi", True),
    n("Rebel Leadership", True),
    n("Blaster Deflection"),
    n("Desperate Reach", True),
    n("Either Way, You Win", True),
    n("Corran Horn"),
    n("Heading For The Medical Frigate"),
    n("Wesa Gotta Grand Army"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Luke's Lightsaber"),
    n("Wesa Gotta Grand Army"),
    n("Obi-Wan Kenobi", True),
    n("Scrambled Transmission", True),
    n("Princess Leia", True),
    n("Luke's Bionic Hand", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Home One"),
    n("Obi-Wan's Lightsaber"),
    n("A Jedi's Resilience"),
    n("Houjix & Out Of Nowhere"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Kessel"),
    n("Admiral Ackbar", True),
    n("Han, Chewie, And The Falcon"),
    n("Let The Wookiee Win", True),
    n("Hear Me Baby, Hold Together", True),
    n("Were You Looking For Me?"),
    n("Leia's Blaster Rifle"),
    n("Leia, Rebel Princess"),
    n("Artoo-Detoo In Red 5"),
    n("Lando Calrissian, Scoundrel"),
    n("A Jedi's Resilience"),
    n("Rebel Leadership", True),
    n("Speak With The Jedi Council"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Spaceport Docking Bay"),
    n("Spaceport Prefect's Office"),
    n("Endor"),
    n("Ralltiir: Spaceport Financial District", True),
    n("Spaceport Street"),
    n("Imperial Domination", True),
    n("Imperial Justice", True),
    n("Imperial Domination", True),
    n("Kuat Drive Yards", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Colonel Davod Jon"),
    n("Ghhhk"),
    n("Janus Greejatus"),
    n("Emperor Palpatine"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Blizzard 2", True),
    n("Arica"),
    n("A Dark Time For The Rebellion", True),
    n("Devastator", True),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Cold Feet", True),
    n("Tempest 1"),
    n("Close Call", True, qty=2),
    n("Outflank", True),
    n("Sneak Attack", True),
    n("Emperor Palpatine"),
    n("Imperial Command"),
    n("Control & Set For Stun"),
    n("Kir Kanos With Force Pike", True),
    n("Why Didn't You Tell Me?", True),
    n("Something Special Planned For Them", True),
    n("Admiral Motti", True),
    n("Masterful Move & Endor Occupation"),
    n("Lieutenant Commander Ardan"),
    n("Trample"),
    n("Blizzard 4"),
    n("Admiral Ozzel"),
    n("Grand Moff Tarkin", True),
    n("Prepared Defenses"),
    n("Where Are You Taking This ... Thing?", True),
    n("Garindan", True),
    n("Ysanne Isard", True),
    n("Imperial Barrier"),
    n("A Dark Time For The Rebellion", True),
    n("Tyrant"),
    n("Why Didn't You Tell Me?", True),
    n("Conquest", True),
    n("Kashyyyk"),
    n("Outflank", True),
    n("Imperial Command"),
    n("Victory", True),
    n("Grand Admiral Thrawn"),
    n("Blizzard 1", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("General Veers", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Leave Them To Me", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
