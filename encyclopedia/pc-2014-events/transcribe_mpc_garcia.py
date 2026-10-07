#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Joe G.

Source: MPC-2014-Day-1-Main-Event.pdf pages 43–44 (2013 form, 15 shields).
Name Joe G. dested Joe G as written. Username jigga. Adjacent Joseph
Gagliardi is a different username (DVMABA22).
"""
from __future__ import annotations

PLAYER = "Joe G"
USERNAME = "jigga"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 43
DS_PAGE = 44
LS_SCAN = "2014 Match Play Championship Day 1 Joe G LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Joe G DS.png"
LS_DECK_NAME = "god DAMPIT WHY?!"
DS_DECK_NAME = "It's viable... really"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Tony G dested Tony Garcia. Username jigga. Deck name "
    "god DAMPIT WHY?!. Home One: War Room starting location. A, F, A dested Anger, Fear, "
    "Aggression (V). BO & DTF dested Battle Plan & Draw Their Fire. Do or Do Not / WA "
    "dested Do, Or Do Not & Wise Advice. It is the future you see dested It Is The Future "
    "You See (V). Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero (V). SATM & "
    "BP dested Sorry About The Mess & Blaster Proficiency. LTWW dested Let The Wookiee Win "
    "(V). (V) from checkbox. Unique overcounts sheet-accurate (Luke, Jedi Knight x2, Luke "
    "Skywalker, Strong In The Force (V) x2, Master Qui-Gon (V) x2, Mace Windu (V) x2, "
    "Imperial Atrocity x2, Let The Wookiee Win (V) x3, Rebel Leadership (V) x3, Speak With "
    "The Jedi Council x2, Clash Of Sabers x2, A Jedi's Resilience x2, Wesa Gotta Grand Army "
    "x3, Escape Pod (V) x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Tony G dested Tony Garcia. Username jigga. Deck name "
    "It's viable... really. Knowledge And Defense (V) starting. Kessel. I'll take them "
    "myself dested I'll Take The Leader (V). Jango Fett, The Assassin dested Jango Fett, "
    "The Assassin (V). SRF & WYB dested Short Range Fighters & Watch Your Back!. MM & "
    "Endor Occupation dested Masterful Move & Endor Occupation. Vanguard (V) x4 unique "
    "overcount. All Power To Weapons x4 unique overcount. Battle Order (Non-V) dested "
    "Battle Order. (V) from checkbox. Unique overcounts sheet-accurate (Vanguard (V) x4, "
    "Saber Squadron Pilot (V) x3, Saber Squadron TIE (V) x3, Outer Rim Scout x2, Hoth: Ice "
    "Plains x2, Imperial Propaganda (V) x2, Protocol Failure (V) x2, SRF & WYB x3, All "
    "Power To Weapons x4, Nevar Yalnal x2, Ghhhk x2, Sonic Bombardment (V) x3, Imperial "
    "Barrier (V) x3)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Home One: War Room"),
    n("Anger, Fear, Aggression", True),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("It Is The Future You See", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Admiral Ackbar", True),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Home One"),
    n("Artoo-Detoo In Red 5"),
    n("Nabrun Leids"),
    n("Lady Luck", True),
    n("Han, Chewie, And The Falcon", True),
    n("Luke's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Naboo: Battle Plains"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Imperial Atrocity", True),
    n("Imperial Atrocity"),
    n("What Are You Trying To Push On Us?"),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Sense"),
    n("Jedi Levitation", True),
    n("Blaster Deflection"),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Houjix"),
    n("Weapon Levitation"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council", qty=2),
    n("Clash Of Sabers", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Escape Pod", True, qty=2),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Battle Plan", True),
    n("Simple Tricks And Nonsense", True),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Affect Mind", True),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Kessel: Spice Mines, Administration Offices", True),
    n("Kessel"),
    n("Combat Response", True),
    n("Combat Readiness", True),
    n("I'll Take The Leader", True),
    n("I'm Sorry", True),
    n("Kessel Surveillance System", True),
    n("Kessel: Spice Mine Operations", True),
    n("Vanguard", True, qty=4),
    n("Outer Rim Scout", qty=2),
    n("Jango Fett, The Assassin", True),
    n("Saber Squadron Pilot", True, qty=3),
    n("Arica"),
    n("Hoth: Ice Plains", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("OS-72-10"),
    n("Slave I"),
    n("Saber 4"),
    n("Saber Squadron TIE", True, qty=3),
    n("Obsidian 10"),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True, qty=2),
    n("Protocol Failure", True, qty=2),
    n("Slow Landing", True),
    n("Evader"),
    n("Surface Patrol Crawler", True),
    n("SFS L-s9.3 Laser Cannons"),
    n("Force Push", True),
    n("Abyssin Ornament", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("All Power To Weapons", qty=4),
    n("Lateral Damage"),
    n("Nevar Yalnal", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Imperial Barrier", True, qty=3),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Abyss", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Reactor Terminal", True),
    n("Imperial Detention", True),
    n("Battle Order"),
]
DS_ADD = []
