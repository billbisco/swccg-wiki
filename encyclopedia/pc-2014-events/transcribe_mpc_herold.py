#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Brian Herold.

Source: MPC-2014-Day-1-Main-Event.pdf pages 57–58 (2013 form, 15 shields).
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 57
DS_PAGE = 58
LS_SCAN = "2014 Match Play Championship Day 1 Brian Herold LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Brian Herold DS.png"
LS_DECK_NAME = "MWYHL"
DS_DECK_NAME = "HD"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. MWYHL dested Mind What You Have Learned / Save You It Can "
    "(V). Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. Lando's "
    "Luxury Yacht dested Lady Luck. SATM & BP dested Sorry About The Mess & Blaster "
    "Proficiency. Ant Man & Rebel Reinforcements dested Antilles Maneuver & Rebel "
    "Reinforcements. Thrown Back dested Thrown Back (V). Jedi Tests 1–6 all checked, "
    "LS_ADD Jedi Test #1 through #6. (V) from checkbox. Unique overcounts sheet-accurate "
    "(Luke Skywalker, Jedi Knight x2, Luke's Bionic Hand x2, Elegant Lightsaber x2, "
    "Armed & Dangerous & Krayt Dragon Howl x2, Rebel Leadership (V) x3)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Hunt Down And Destroy The Jedi. The Mandalorian Father of "
    "Fett dested Jango Fett, The Assassin. P-59 dested P-59. Slave I, Symbol Of Fear "
    "dested Slave I, Symbol Of Fear. MM & EO dested Masterful Move & Endor Occupation. "
    "You ARE Beaten dested You Are Beaten. (V) from checkbox. Unique overcounts "
    "sheet-accurate (Visage Of The Emperor x3, Darth Sidious x2, Count Dooku x2, Emperor "
    "Palpatine x2, Darth Maul With Lightsaber x2, Darth Vader, Dark Lord Of The Sith x2, "
    "Blizzard 4 x2, Revenge Of The Sith x2, I Have You Now x2, We Must Accelerate Our "
    "Plans x3, Sonic Bombardment (V) x3, Force Lightning x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("Strong Is Vader"),
    n("It Is The Future You See"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Thrown Back", True),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Major Haash'n"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Daughter Of Skywalker", True),
    n("Yoda", True),
    n("Fallen Jedi"),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke's Backpack"),
    n("Luke's Bionic Hand", qty=2),
    n("Elegant Lightsaber", qty=2),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Bog Clearing"),
    n("Dagobah: Jungle"),
    n("Home One: War Room"),
    n("Coruscant"),
    n("Jedi Levitation"),
    n("Courage Of A Skywalker", True),
    n("Clash Of Sabers"),
    n("Houjix"),
    n("Escape Pod", True),
    n("Armed & Dangerous & Krayt Dragon Howl", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Artoo-Detoo In Red 5"),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Lady Luck"),
    n("The Way Of Things"),
    n("Projection Of A Skywalker"),
    n("Quick Draw", True),
    n("Reflection", True),
    n("Imperial Atrocity", True),
    n("Yoda's Hope"),
    n("Dodge"),
    n("Control & Tunnel Vision"),
    n("Hear Me Baby, Hold Together", True),
    n("Alternatives To Fighting"),
    n("It's A Trap!"),
    n("It Could Be Worse"),
    n("Under Attack"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("On The Edge"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("At Peace", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = [
    n("Jedi Test #1"),
    n("Jedi Test #2"),
    n("Jedi Test #3"),
    n("Jedi Test #4"),
    n("Jedi Test #5"),
    n("Jedi Test #6"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheater"),
    n("Visage Of The Emperor"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Conduct Your Search"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Sidious", qty=2),
    n("Count Dooku", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Blizzard 4", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Vader's Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Revenge Of The Sith", qty=2),
    n("Blast Door Controls"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Emperor's Power", True),
    n("Visage Of The Emperor", qty=2),
    n("Crush The Rebellion"),
    n("Garindan", True),
    n("Force Field"),
    n("I Have You Now", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True),
    n("Force Lightning", qty=2),
    n("You Are Beaten"),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
