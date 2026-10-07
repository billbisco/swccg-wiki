#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Josh Mack Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Josh Mack"
USERNAME = "Remaker"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 60
DS_PAGE = 59
LS_SCAN = "2013 Match Play Championship p60 Josh Mack LS.png"
DS_SCAN = "2013 Match Play Championship p59 Josh Mack DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Josh Mack. Username Remaker. Light. Deck title Dem Step. "
    "Watch Your Step / This Place Can Be A Little Rough (Decipher; (V) unchecked). "
    "Tatooine (episode I) dested Tatooine. Tatooine: Docking Bay 94 as written. "
    "Rycar Ryjerd as written. Boshhk, Brash Smuggler dested BoShek, Brash Smuggler. "
    "Rebel Agent dested Leia, Rebel Princess. Luke Skywalker, STTF dested Son Of Skywalker. "
    "LSJK dested Luke Skywalker, Jedi Knight. Han Solo, Courageous Smuggler as written. "
    "Lando's Luxury Yacht dested Lady Luck. Boshek's Modified Light Freighter as written. "
    "SATM & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "OOC & Trans Terminated dested Out Of Commission & Transmission Terminated. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "AFA dested Anger, Fear, Aggression. Charm dested Chasm. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Form left column reprints 37–38 on lines 39–40 are I'm With You Too and Uncontrollable Fury. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Josh Mack. Username Remaker. Dark. Deck title Pitties. "
    "Starting Kessel + Combat Readiness. "
    "Kessel: Spice Mines - Administrator's Ofc dested Kessel: Spice Mines - Administrator's Office. "
    "You Cannot Hide Forever & Mobilization Points dested You Cannot Hide Forever & Mobilization Points. "
    "Black Leader dested Juno Eclipse, Black Leader. Darth Maul w/ Lightsaber dested Darth Maul With Lightsaber. "
    "U-3PO dested U-3PO (Yoo-Threepio). DS-61-4 in Black 4 dested DS-61-4. "
    "OS-72-1 in Obsidian 1 / OS-72-2 in Obsidian 2 as written. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "Control & Set For Stun dested Control & Set For Stun. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Come here You Big Coward! dested Come Here You Big Coward. "
    "Do they have a code clearance dested Do They Have A Code Clearance?. "
    "Form left column reprints 37–38 on lines 39–40 are All Power To Weapons dittos. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Squadron Assignments"),
    n("Talon Karrde"),
    n("Dash Rendar", True),
    n("Chewbacca, Walking Carpet"),
    n("Melas", True),
    n("Mirax Terrik"),
    n("BoShek, Brash Smuggler"),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles", True),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Son Of Skywalker", qty=3),
    n("Luke Skywalker, Jedi Knight"),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Lady Luck"),
    n("Millennium Falcon"),
    n("Pulsar Skate"),
    n("BoShek's Modified Light Freighter"),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Luke's Bionic Hand"),
    n("Tatooine: Mos Eisley"),
    n("Corellia", True),
    n("Naboo: Boss Nass' Chambers"),
    n("I'll Take The Leader"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("I'm With You Too", True),
    n("Uncontrollable Fury"),
    n("Houjix & Out Of Nowhere"),
    n("A Few Maneuvers"),
    n("Control & Tunnel Vision"),
    n("Old Ben"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("Dodge"),
    n("Out Of Commission & Transmission Terminated"),
    n("Desperate Reach", True),
    n("Moving To Attack Position"),
    n("Rebel Barrier"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Run Luke, Run!", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("There Is Another"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan", True),
    n("Let's Keep A Little Optimism Here", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Aim High", True),
    n("Ultimatum", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("I'm Sorry", True),
    n("I'll Take Them Myself"),
    n("Juno Eclipse, Black Leader"),
    n("DS-61-2"),
    n("DS-61-3"),
    n("DS-61-5"),
    n("Baron Soontir Fel"),
    n("Darth Maul With Lightsaber"),
    n("Arica"),
    n("U-3PO (Yoo-Threepio)"),
    n("Black 1"),
    n("Black 2", True),
    n("Black 3", True),
    n("Black 5"),
    n("DS-61-4"),
    n("Saber 1"),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Kessel Surveillance System"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Spice Mine Operations"),
    n("Storm Clouds", qty=2),
    n("Wakeelmui"),
    n("Floating Refinery"),
    n("Lateral Damage"),
    n("Protocol Failure"),
    n("Presence Of The Force", qty=2),
    n("He Is Not Ready"),
    n("Combat Response"),
    n("Sienar Fleet Systems"),
    n("All Power To Weapons", qty=3),
    n("Control & Set For Stun", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Short Range Fighters & Watch Your Back", qty=3),
    n("Dark Maneuvers & Tallon Roll", qty=4),
    n("Limited Resources"),
    n("Ghhhk"),
    n("Monnok"),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Operational As Planned", True, qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans", True),
    n("Come Here You Big Coward", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Battle Order", True),
    n("Resistance", True),
    n("There Is No Try", True),
]
DS_ADD = []
