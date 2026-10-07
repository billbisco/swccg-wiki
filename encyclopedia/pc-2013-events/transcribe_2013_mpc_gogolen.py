#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Gogolen typed slang LS+DS."""
from __future__ import annotations

PLAYER = "Gogolen"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 35
DS_PAGE = 36
LS_SCAN = "2013 Match Play Championship p35 Gogolen LS.png"
DS_SCAN = "2013 Match Play Championship p36 Gogolen DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Typed slang list (not a Xerox Print Form). Gogolen LS MPC. "
    "Title Help Me Obi-wan Baroni. Communing from Tatooine: Slave Quarters. "
    "Tick marks and (xN) as qty. (V) written next to the name. "
    "Threepio With His Parts Showing (AI) kept with (AI) as printed. "
    "Indented Sorry / Blaster Prof under Let The Wookiee Win dested "
    "Sorry About The Mess & Blaster Proficiency. "
    "The Bith Shuffle & Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Out Of Commission & Transmission Terminated one copy (one tick). "
    "Prize (V) dested Jabba's Prize. Sentry dested Yavin Sentry. "
    "Insight dested Your Insight Serves You Well. Optimism dested Let's Keep A Little Optimism Here. "
    "DDTA dested Don't Do That Again. Tragedy dested A Tragedy Has Occurred. "
    "Professor dested The Professor. Simple Tricks dested Simple Tricks And Nonsense."
)
DS_NOTE = (
    "Typed slang list (not a Xerox Print Form). Gogolen DS MPC. "
    "Title That's a spicy meatball. Starting Kessel. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin. "
    "U-3PO (Yoo-Threepio) dested U-3PO (Yoo-Threepio). "
    "Short Range Fighters & Watch Your Back! dested Short Range Fighters & Watch Your Back. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Storm Clouds two copies. "
    "Faith (V) dested I Find Your Lack Of Faith Disturbing. "
    "Cannot Hide dested You Cannot Hide Forever. Coward dested Come Here You Big Coward. "
    "Gesture dested A Useless Gesture. Allegations dested Allegations Of Corruption."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing (AI)"),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian, Scoundrel", True),
    n("Wedge Antilles", True),
    n("Corran Horn"),
    n("Han With Heavy Blaster Pistol"),
    n("Luke With Lightsaber", qty=3),
    n("Chewie, Enraged", True, qty=4),
    n("Master Kenobi"),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Leia With Blaster Rifle"),
    n("Wokling", True),
    n("Rebel Gunrunner"),
    n("Draw Their Fire"),
    n("Launching The Assault"),
    n("K'lor'slug", True),
    n("Scrambled Transmission", True),
    n("Redeemed Apprentice"),
    n("Imperial Atrocity", True, qty=2),
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Houjix", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Escape Pod", True, qty=2),
    n("Use The Force", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("Jedi Levitation", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Let The Wookiee Win", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Tatooine: Slave Quarters"),
    n("Home One: War Room"),
    n("Tatooine"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Chewbacca's Bowcaster"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("The Professor"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Jabba's Prize", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Spice Mine Administrator"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("U-3PO (Yoo-Threepio)"),
    n("DS-61-3"),
    n("Grand Admiral Thrawn"),
    n("Admiral Pellaeon"),
    n("DS-61-2"),
    n("OS-72-10"),
    n("General Veers", True, qty=2),
    n("Kir Kanos With Force Pike"),
    n("Kessel Surveillance System"),
    n("Floating Refinery", True),
    n("I'm Sorry", True),
    n("Image Of The Dark Lord", True),
    n("I'll Take Them Myself"),
    n("Something Special Planned For Them", True),
    n("Combat Response"),
    n("Protocol Failure"),
    n("Imperial Propaganda", True, qty=2),
    n("Knowledge And Defense", True),
    n("Limited Resources"),
    n("Force Push", True),
    n("Combat Readiness", True),
    n("Sonic Bombardment", True, qty=2),
    n("Imperial Barrier", qty=2),
    n("Trample"),
    n("A Dark Time For The Rebellion", True),
    n("Dark Maneuvers & Tallon Roll", qty=3),
    n("Atmospheric Assault", True),
    n("Imperial Command", qty=3),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("All Power To Weapons", qty=2),
    n("Storm Clouds", qty=2),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Cloud City: Security Tower", True),
    n("Kessel"),
    n("Spice Mine Operations"),
    n("Justifier"),
    n("Slave I, Symbol Of Fear"),
    n("Black 3", True),
    n("Obsidian 10"),
    n("OS-72-2 In Obsidian 2"),
    n("Black 2", True),
    n("OS-72-1 In Obsidian 1"),
    n("Blizzard 2", True),
    n("Blizzard 4", True, qty=2),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Battle Order"),
    n("Resistance"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
