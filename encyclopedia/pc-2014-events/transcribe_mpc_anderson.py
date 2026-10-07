#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: John Anderson.

Source: MPC-2014-Day-1-Main-Event.pdf pages 5–6 (2013 form, 15 shields).
Username puck71. Printed GEMP list.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "puck71"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2014 Match Play Championship Day 1 John Anderson LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 John Anderson DS.png"
NOTE = "Printed 2013 Xerox form."
LS_NOTE = (
    "Printed 2013 Xerox. Username puck71. LIGHT checked. MWYHL (V) dested "
    "Mind What You Have Learned (V) / Save You It Can (V). Do Or Do Not & Wise Advice "
    "dested Do, Or Do Not & Wise Advice. SATM/BP dested Sorry About The Mess & Blaster "
    "Proficiency. Shield 15 crossed then Yavin Sentry (V). Jedi Tests 1–6 checked dested "
    "the six Jedi Tests. Unique overcounts sheet-accurate (Rebel Leadership (V) x3, "
    "Luke Skywalker, Jedi Knight x2, Armed And Dangerous & Krayt Dragon Howl x2, "
    "Luke's Bionic Hand x2). (V) from checkbox."
)
DS_NOTE = (
    "Printed 2013 Xerox. Username puck71. LIGHT/DARK boxes empty; Dark 60. HD empty "
    "dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Ni Chuba Na?? (V). P-59 dested P-59. Gift Of The Master dested Gift Of The Master. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. Leave Them To Me (V) marked. "
    "Unique overcounts sheet-accurate (Darth Vader, Dark Lord Of The Sith x4, Visage Of "
    "The Emperor x3, We Must Accelerate Our Plans x3, Force Field (V) x2, I Have You Now "
    "x2, Revenge Of The Sith x2, Darth Maul With Lightsaber x2, Count Dooku x2, Sonic "
    "Bombardment (V) x2, Emperor Palpatine x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("Strong Is Vader"),
    n("It Is The Future You See", True),
    n("Thrown Back", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Daughter Of Skywalker", True),
    n("Elegant Lightsaber", True),
    n("Elegant Lightsaber"),
    n("Rebel Leadership", True, qty=3),
    n("Home One: War Room"),
    n("On The Edge"),
    n("Home One"),
    n("Artoo-Detoo In Red 5"),
    n("Corran Horn"),
    n("Kiffex"),
    n("Projection Of A Skywalker"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Weapon Levitation"),
    n("Escape Pod", True),
    n("The Way Of Things"),
    n("Han, Chewie, And The Falcon", True),
    n("Dagobah: Yoda's Hut"),
    n("Armed And Dangerous & Krayt Dragon Howl", qty=2),
    n("Yoda", True),
    n("Imperial Atrocity", True),
    n("At Peace", True),
    n("Inconsequential Barriers"),
    n("Luke's Bionic Hand", qty=2),
    n("Dagobah: Bog Clearing"),
    n("Houjix"),
    n("Clash Of Sabers"),
    n("Reflection", True),
    n("It's A Trap!"),
    n("Courage Of A Skywalker", True),
    n("Admiral Ackbar", True),
    n("Hear Me Baby, Hold Together", True),
    n("Dagobah: Jungle"),
    n("It Could Be Worse"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Luke's Backpack"),
    n("Alternatives To Fighting"),
    n("Yoda's Hope"),
    n("Obi-Wan Kenobi", True),
    n("Under Attack"),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True),
    n("Quick Draw", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Dodge"),
    n("Collision!"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Bravo Fighter", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Affect Mind", True),
    n("Aim High"),
    n("Your Ship?"),
    n("He Can Go About His Business"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Conduct Your Search"),
    n("Gift Of The Master"),
    n("Emperor Palpatine", qty=2),
    n("Force Field", True, qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Ghhhk"),
    n("Force Lightning"),
    n("Vader's Lightsaber"),
    n("Blaster Rack", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("You Are Beaten"),
    n("I Have You Now", qty=2),
    n("Endor: Back Door"),
    n("No Escape"),
    n("Revenge Of The Sith", qty=2),
    n("Dooku's Lightsaber"),
    n("Cloud City: Security Tower", True),
    n("Lord Sidious"),
    n("Jango Fett, The Assassin"),
    n("Darth Vader, Dark Lord Of The Sith", qty=4),
    n("Visage Of The Emperor", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Darth Maul With Lightsaber", qty=2),
    n("P-59"),
    n("Masterful Move & Endor Occupation"),
    n("Maul's Sith Infiltrator"),
    n("Blast Door Controls"),
    n("Darth Sidious"),
    n("Count Dooku", qty=2),
    n("Masterful Move"),
    n("Sonic Bombardment", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Blockade Flagship: Bridge"),
    n("Force Push", True),
    n("Blizzard 4"),
    n("Sidious' Lightsaber"),
    n("Crush The Rebellion"),
    n("Sith Fury", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Leave Them To Me", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("After Her!", True),
]
DS_ADD = []
