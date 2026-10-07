#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Justin Carulli Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Justin Carulli"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 24
DS_PAGE = 23
LS_SCAN = "2013 Match Play Championship p24 Justin Carulli LS.png"
DS_SCAN = "2013 Match Play Championship p23 Justin Carulli DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title That. Light. "
    "Watch Your Step (7-side This Place Can Be A Little Rough). "
    "AFA → Anger, Fear, Aggression. Tatooine (EP1) dested Tatooine. "
    "Rycar Rygaard dested Rycar Ryjerd. "
    "Boshhk, Brash Smuggler dested BoShek, Brash Smuggler. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Booster In Pulsar Skate as written. "
    "Rebel Agent dested Leia, Rebel Princess. "
    "Luke Skywalker, Son Of The Force dested Son Of Skywalker. "
    "Either Win You Win dested Either Way, You Win. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title This. Dark. "
    "You Cannot Hide Forever / Mobilization Points. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Kessel: Spice Mines - Admin Office dested Kessel: Spice Mines - Administrator's Office. "
    "Operational As Planned dested Operational As Planned. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Landed Resources dested Limited Resources. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "OS-72-1 in Obsidian 1 / OS-72-2 in Obsidian 2 as written. "
    "Spice Mine Occupants dested Spice Mine Operations. "
    "DS-61-4 in Black 4 dested DS-61-4. "
    "Prisma of the Force dested Presence Of The Force. "
    "Shield We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Cantina", True),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("A Few Maneuvers"),
    n("Let The Wookiee Win", True),
    n("Run Luke, Run!"),
    n("BoShek, Brash Smuggler"),
    n("Out Of Commission & Transmission Terminated"),
    n("Lady Luck"),
    n("Scrambled Transmission", True),
    n("Let The Wookiee Win", True),
    n("Imperial Atrocity", True),
    n("Luke's Lightsaber"),
    n("Clash Of Sabers"),
    n("Seeking An Audience", True),
    n("Houjix & Out Of Nowhere"),
    n("Mirax Terrik"),
    n("Booster In Pulsar Skate"),
    n("Rebel Barrier"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Obi-Wan's Journal"),
    n("Luke Skywalker, Jedi Knight"),
    n("Redeemed Apprentice"),
    n("Tatooine: Mos Eisley"),
    n("Leia, Rebel Princess"),
    n("Desperate Reach", True),
    n("Corellia", True),
    n("Melas", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Life Debt"),
    n("Sai'torr Kal Fas", True),
    n("Draw Their Fire"),
    n("Imperial Atrocity", True),
    n("Temporary Foothold"),
    n("I'm With You Too", True),
    n("Son Of Skywalker", qty=3),
    n("Wedge Antilles", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Dodge"),
    n("Run Luke, Run!"),
    n("Either Way, You Win", True),
    n("Luke's Bionic Hand", True),
    n("Sergeant Doallyn", True),
    n("Control & Tunnel Vision"),
    n("Moving To Attack Position"),
    n("Uncontrollable Fury"),
    n("Talon Karrde"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Dash Rendar", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("There Is Another"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "You Cannot Hide Forever / Mobilization Points"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("You Cannot Hide Forever / Mobilization Points"),
    n("I'm Sorry", True),
    n("Floating Refinery"),
    n("Presence Of The Force"),
    n("Sienar Fleet Systems"),
    n("U-3PO"),
    n("A Dark Time For The Rebellion", True),
    n("Ghhhk"),
    n("Dark Maneuvers & Tallon Roll", qty=4),
    n("Storm Clouds"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Black 5"),
    n("Operational As Planned", True),
    n("Juno Eclipse, Black Leader"),
    n("Lateral Damage"),
    n("Black 2", True),
    n("Limited Resources"),
    n("Control & Set For Stun"),
    n("Saber 1"),
    n("Baron Soontir Fel"),
    n("Control & Set For Stun"),
    n("Kessel Surveillance System"),
    n("Arica"),
    n("A Dark Time For The Rebellion", True),
    n("Short Range Fighters & Watch Your Back"),
    n("Operational As Planned", True),
    n("DS-61-2"),
    n("Black 1"),
    n("Short Range Fighters & Watch Your Back"),
    n("He Is Not Ready"),
    n("Short Range Fighters & Watch Your Back"),
    n("Protocol Failure"),
    n("Darth Maul With Lightsaber"),
    n("OS-72-1 In Obsidian 1"),
    n("Lightsaber Deficiency", True),
    n("Walker Garrison"),
    n("All Power To Weapons"),
    n("Monnok"),
    n("DS-61-3"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Spice Mine Operations"),
    n("DS-61-4"),
    n("Storm Clouds"),
    n("All Power To Weapons"),
    n("Masterful Move & Endor Occupation"),
    n("All Power To Weapons"),
    n("Combat Response"),
    n("OS-72-2 In Obsidian 2"),
    n("Black 3", True),
    n("We Must Accelerate Our Plans"),
    n("DS-61-5"),
    n("Presence Of The Force"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
