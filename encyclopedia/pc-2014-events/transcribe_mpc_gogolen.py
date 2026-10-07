#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Chris Gogolen.

Source: MPC-2014-Day-1-Main-Event.pdf pages 45–46 (2013 form, 15 shields).
"""
from __future__ import annotations

PLAYER = "Chris Gogolen"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 46
DS_PAGE = 45
LS_SCAN = "2014 Match Play Championship Day 1 Chris Gogolen LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Chris Gogolen DS.png"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. MWYHL dested Mind What You Have Learned / Save You It Can "
    "(V). Strong is Vader + 6 Tests dested Strong Is Vader. Jedi Tests 2–6 checked, "
    "LS_ADD Jedi Test #2 through #6. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Lando's Yacht dested Lady Luck. Daughter dested Daughter Of Skywalker. NOOOO dested "
    "NOOOOOOOOOOOO!. ATR dested AT-RT. Qui-gon's Saber (Ref 3) dested Qui-Gon's Lightsaber. "
    "Shield 15 Jabba's Prize crossed, Do, Or Do Not dested Do, Or Do Not (V). (V) from "
    "checkbox. Unique overcounts sheet-accurate (Let The Wookiee Win (V) x3, Luke "
    "Skywalker, Jedi Knight x2, Escape Pod (V) x2, Houjix x2, Mace Windu (V) x2, Master "
    "Qui-Gon (V) x2, Wesa Gotta Grand Army x2, Artoo-Detoo In Red 5 x2, Luke Skywalker, "
    "Strong In The Force x2, Mechanical Failure x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Kessel starting location. Gift of Master dested Gift Of The "
    "Master. Ni Chu' dested Ni Chuba Na?? (V). I'll take them myself dested I'll Take The "
    "Leader. Galen dested Galen Marek, Starkiller. Galen's saber VG dested Galen's "
    "Lightsaber, Vader's Gift. Slave I SOF dested Slave I, Symbol Of Fear. Jango Fett "
    "Assassin dested Jango Fett, The Assassin. Dooku dested Count Dooku. Special Delivery "
    "(V) dested Special Delivery (V). Short Range / WYB dested Short Range Fighters & "
    "Watch Your Back!. (V) from checkbox. Unique overcounts sheet-accurate (Galen Marek, "
    "Starkiller x3, Count Dooku x2, Lord Sidious x2, Maul With Lightsaber x2, Emperor "
    "Palpatine x2, Protocol Failure x2, Force Lightning x2, Sonic Bombardment (V) x2, "
    "Force Field (V) x2, Lightsaber Deficiency (V) x2, A Dark Time For The Rebellion (V) "
    "x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("Strong Is Vader"),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("It Is The Future You See", True),
    n("Jedi Lightsaber", True),
    n("Wesa Gotta Grand Army"),
    n("Escape Pod", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Hear Me Baby, Hold Together", True),
    n("Let The Wookiee Win", True),
    n("A Jedi's Resilience"),
    n("Weapon Levitation"),
    n("It Could Be Worse"),
    n("Imperial Atrocity", True),
    n("Dagobah: Jungle"),
    n("Qui-Gon's Lightsaber"),
    n("Master Qui-Gon", True),
    n("Corran Horn"),
    n("Let The Wookiee Win", True),
    n("Mace Windu", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Luke Skywalker, Strong In The Force"),
    n("Mace Windu, Master Of The Order"),
    n("Mechanical Failure"),
    n("Out Of Commission & Transmission Terminated"),
    n("Strikeforce", True),
    n("Luke's Lightsaber"),
    n("Artoo-Detoo In Red 5"),
    n("Escape Pod", True),
    n("Sai'torr Kal Fas", True),
    n("Dagobah: Yoda's Hut"),
    n("Republic Gunship Wing"),
    n("Daughter Of Skywalker", True),
    n("NOOOOOOOOOOOO!", True),
    n("Houjix"),
    n("Luke Skywalker, Jedi Knight"),
    n("Let The Wookiee Win", True),
    n("Artoo-Detoo In Red 5"),
    n("Lady Luck"),
    n("Houjix"),
    n("Mace Windu", True),
    n("Reflection", True),
    n("Clash Of Sabers"),
    n("Yoda", True),
    n("Dagobah: Swamp"),
    n("The Way Of Things"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Han, Chewie, And The Falcon", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Luke's Backpack"),
    n("Master Qui-Gon", True),
    n("Projection Of A Skywalker"),
    n("Wesa Gotta Grand Army"),
    n("Naboo: Battle Plains"),
    n("AT-RT"),
    n("Mechanical Failure"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Chasm", True),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("He Can Go About His Business"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("The Professor"),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not", True),
]
LS_ADD = [
    n("Jedi Test #2"),
    n("Jedi Test #3"),
    n("Jedi Test #4"),
    n("Jedi Test #5"),
    n("Jedi Test #6"),
]


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines, Administration Offices"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("I'll Take The Leader"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mine Operations"),
    n("Protocol Failure"),
    n("Emperor Palpatine"),
    n("The Phantom Menace"),
    n("P-59"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Lightning"),
    n("Something Special Planned For Them", True),
    n("You Are Beaten"),
    n("Darth Maul With Lightsaber"),
    n("Lord Sidious"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Count Dooku"),
    n("Blaster Rack", True),
    n("Galen Marek, Starkiller"),
    n("Darth Vader", True),
    n("Dooku's Lightsaber"),
    n("Lightsaber Deficiency", True),
    n("Kessel Surveillance System"),
    n("Garindan", True),
    n("Victory"),
    n("Cold Feet", True),
    n("Force Field", True),
    n("A Dark Time For The Rebellion", True),
    n("Darth Maul With Lightsaber"),
    n("Boba Fett, Prepared Hunter"),
    n("Count Dooku"),
    n("Imperial Barrier"),
    n("Kessel: Mining Colony"),
    n("Kessel: Spice Mines, Administration Offices"),
    n("Kessel: Extraction Facility"),
    n("Emperor Palpatine"),
    n("Protocol Failure"),
    n("Force Push", True),
    n("Lord Sidious"),
    n("Slave I, Symbol Of Fear"),
    n("Sonic Bombardment", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Special Delivery", True),
    n("Force Lightning"),
    n("Maul's Sith Infiltrator"),
    n("Galen Marek, Starkiller"),
    n("Imperial Propaganda", True),
    n("Sith Fury", True),
    n("Limited Resources"),
    n("A Dark Time For The Rebellion", True),
    n("Sidious' Lightsaber"),
    n("Sonic Bombardment", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Force Field", True),
    n("Lightsaber Deficiency", True),
    n("Jango Fett, The Assassin"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Imperial Detention", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Firepower", True),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
