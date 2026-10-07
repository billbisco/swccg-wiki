#!/usr/bin/env python3
"""2013 World Championship Day 2 typed Print Form: Walseth Endor Ops + Space."""
from __future__ import annotations

PLAYER = "Walseth"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 110
DS_PAGE = 109
LS_SCAN = "2013 Worlds Day 2 p110 Walseth LS.png"
DS_SCAN = "2013 Worlds Day 2 p109 Walseth DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Typed 2012 Print Form. Name Walseth. Username blank. Email blank. LIGHT. "
    "Deck title Space. Event Worlds. Dest as written; do not dest as Mark Walseth. "
    "No Objective; starting location Yavin 4 + Massassi Headquarters. "
    "Careful Planning (Starting) checked (V) is the starting interrupt. "
    "Rycar Ryjerd (Starting) and Luke, Trust Me (Starting) checked (V). "
    "Get to Your Ships (Starting) unchecked. "
    "Yavin 4: War Room dested Yavin 4: Massassi War Room. "
    "Yavin 4:Throne Room dested Yavin 4: Massassi Throne Room. "
    "All Wings Report In & Darklighter Spln dested "
    "All Wings Report In & Darklighter Spin. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred. "
    "Additional cards 1-3 are extra shields. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Typed 2012 Print Form. Name Walseth. Username blank. Email blank. DARK. "
    "Deck title Endor Ops. Event Worlds 2013. Dest as written; do not dest as Mark Walseth. "
    "Endor Operations / Imperial Outpost dested Endor Operations / Imperial Outpost. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Lone Pilot (Starting) checked (V) is the starting interrupt. "
    "You Cannot Hide Forever / Mob Points dested You Cannot Hide Forever & Mobilization Points. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin. "
    "Vader's Shuttle dested Vader's Personal Shuttle. "
    "Galen's Fighter dested Rogue Shadow. "
    "Hounds Tooth dested Hound's Tooth. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Short Range Fighters & Watch Your Back! dested "
    "Short Range Fighters & Watch Your Back. "
    "After Her dested After Her!. "
    "Line 43 Something Special Planned for Them struck; omitted; "
    "handwritten Battle Deployment (V) replacement kept. "
    "Battler Order dested Battle Order. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Additional cards 1-3 are extra shields. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Yavin 4"),
    n("Yavin 4: Massassi Headquarters"),
    n("Careful Planning", True),
    n("Rycar Ryjerd", True),
    n("Luke, Trust Me", True),
    n("Get To Your Ships"),
    n("Yavin 4: Massassi War Room", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Ralltiir"),
    n("Luke Skywalker", True),
    n("Wedge Antilles"),
    n("Elyhek Rue"),
    n("Ric Olie, Bravo Leader"),
    n("Officer Dolphe"),
    n("Lieutenant Rya Kirsch"),
    n("Artoo-Detoo In Red 5", qty=4),
    n("Red Squadron 1"),
    n("Red 7"),
    n("Bravo 1"),
    n("Bravo 2"),
    n("Bravo 4"),
    n("Han, Chewie, And The Falcon"),
    n("X-Wing Laser Cannon", qty=2),
    n("Portable Scanner"),
    n("Power Pivot", qty=2),
    n("Rebel Barrier", qty=3),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Corellian Slip", True, qty=2),
    n("We're Doomed", qty=2),
    n("Sorry About The Mess"),
    n("It Could Be Worse"),
    n("It's Not My Fault", True),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True, qty=3),
    n("Projection Of A Skywalker", qty=2),
    n("A Vergence In The Force"),
    n("Uncontrollable Fury"),
    n("It's On Automatic Pilot"),
    n("Logistical Delay", True),
    n("Wokling", True),
    n("Much To Learn You Still Have", True),
    n("Massassi Base Sentry", True),
    n("I'm With You Too", True),
    n("I'll Take The Leader"),
    n("Restore Freedom To The Galaxy", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not", True),
    n("Another Pathetic Lifeform", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Lone Pilot", True),
    n("Kuat"),
    n("DS-61-2"),
    n("Black 2", True),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("Wakeelmui"),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("Darth Vader", True),
    n("Juno Eclipse, Black Leader", True),
    n("Dengar", True),
    n("Bossk", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Baron Soontir Fel"),
    n("Zuckuss"),
    n("Sergeant Irol", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Vader's Personal Shuttle", True),
    n("Victory", True),
    n("Mist Hunter", True),
    n("Saber 1"),
    n("Rogue Shadow", True),
    n("Punishing One", True),
    n("Hound's Tooth", True),
    n("Slave I, Symbol Of Fear", True),
    n("Short Range Fighters & Watch Your Back", qty=4),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Prepared Defenses"),
    n("Force Push", True),
    n("Limited Resources"),
    n("Trample"),
    n("Battle Deployment", qty=4),
    n("Astromech Shortage", True),
    n("Tarkin's Bounty", True),
    n("Broken Concentration", True),
    n("Lateral Damage", qty=3),
    n("Combat Response", True),
    n("Presence Of The Force"),
    n("Crossfire", True),
    n("Endor Shield", True),
    n("Establish Secret Base", True),
    n("Ominous Rumors"),
    n("Fighters Coming In"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("Leave Them To Me", True),
    n("Resistance"),
    n("After Her!", True),
    n("Fanfare"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
