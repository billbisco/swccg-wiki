#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Kendall Halman.

Source: Nationals-2014-day-1.pdf pages 19–20 (2010 form).
Name Kendall Hartman. Username Corran. Dest Kendall Halman.
"""
from __future__ import annotations

PLAYER = "Kendall Halman"
USERNAME = "Corran"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2014 US Nationals Day 1 p20 Kendall Halman LS.png"
DS_SCAN = "2014 US Nationals Day 1 p19 Kendall Halman DS.png"
NOTE = "Handwritten 2010 Xerox. Name Kendall Hartman; username Corran dested Kendall Halman."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Kendall Hartman. Username Corran. "
    "Deck name I choose to be destroyed! "
    "You Can Either Profit By This dested You Can Either Profit By This… / Or Be Destroyed. "
    "JP: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Tati: Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Obi-Wan Kenobi dested Obi-Wan Kenobi. Princess Leia dested Princess Leia. "
    "Lars Moisture Farm dested Tatooine: Lars' Moisture Farm. "
    "Tatooine Utility Belt dested Tatooine Utility Belt. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "AFA dested Anger, Fear, Aggression. Unique overcounts sheet-accurate "
    "(Wesa Gotta Grand Army x2, A Jedi's Resilience x2, Owen Lars & Beru Lars x2, "
    "Speak With The Jedi Council x2, Let The Wookiee Win x2, Luke Skywalker, Strong In The Force x2, "
    "Sorry About The Mess & Blaster Proficiency x2). (V) from checkbox. "
    "NO_DEST (2014 index): Sweeip."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Kendall Hartman. Username Corran. "
    "Deck name I play what I want. Desert Landing Site dested Tatooine: Desert Landing Site. "
    "Flagship Bridge dested Blockade Flagship: Bridge. Force Unleashed dested The Force Unleashed. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Slave I, SOF dested Slave I, Symbol Of Fear. Mandalorian Combo dested Mandalorian Mishap & Jedi Mind Trick. "
    "Galen dested Galen Marek, Starkiller. Jango, Assassin dested Jango Fett, The Assassin. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. Gift of the Master dested Gift Of The Master. "
    "K+D dested Knowledge And Defense. Unique overcounts sheet-accurate "
    "(Darth Maul x4, Galen Marek, Starkiller x2, Darth Vader With Lightsaber x2, "
    "Lightsaber Deflection x3, ComScan Detection x2, Phantom Menace x2, Sonic Bombardment x2, "
    "We Must Accelerate Our Plans x2, Sniper & Dark Strike x2). (V) from checkbox. "
    "Sidious's Lightsaber dested Sidious' Lightsaber. "
    "NO_DEST (2014 index): Lightsaber Deflection (V); Mandalorian Mishap & Jedi Mind Trick."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Leia's Blaster Rifle"),
    n("Jaina Solo", True),
    n("Obi-Wan Kenobi", True),
    n("Princess Leia", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Tatooine Utility Belt", True),
    n("Civil Disorder", True),
    n("Lady Luck"),
    n("Desperate Reach", True),
    n("Nabrun Leids"),
    n("Harvest"),
    n("Houjix"),
    n("Heading For The Medical Frigate"),
    n("Grimtaash"),
    n("Chewie, Enraged"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Coruscant: Jedi Council Chamber"),
    n("Artoo"),
    n("A Gift"),
    n("It Could Be Worse"),
    n("Clash Of Sabers"),
    n("Someone Who Loves You"),
    n("Han", True),
    n("Shmi Skywalker"),
    n("Owen Lars & Beru Lars", qty=2),
    n("Corran Horn"),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Disarmed"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Blaster Deflection"),
    n("A Jedi's Resilience", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Padme Naberrie", True),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Escape Pod", True),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Threepio With His Parts Showing"),
    n("Sweeip"),
    n("I Must Be Allowed To Speak", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ounee Ta", True),
    n("Weapons Display"),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Traffic Control", True),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Don't Do That Again", True),
]
LS_ADD = [
    n("Chasm", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred"),
]


DS_START = "The Force Unleashed"
DS_CARDS = [
    n("Tatooine: Desert Landing Site"),
    n("Tatooine"),
    n("Blockade Flagship: Bridge"),
    n("The Force Unleashed"),
    n("Imperial Propaganda", True),
    n("Dengar With Blaster Carbine", True),
    n("Mara Jade With Lightsaber"),
    n("Image Of The Dark Lord", True),
    n("There Is No Conflict"),
    n("Disarmed"),
    n("Sniper & Dark Strike"),
    n("Sidious' Lightsaber"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Death Star: War Room"),
    n("Cloud City: Security Tower", True),
    n("Force Field", True),
    n("Tarkin's Orders"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Masterful Move"),
    n("Lightsaber Deflection", True, qty=3),
    n("ComScan Detection", True, qty=2),
    n("Combat Readiness", True),
    n("Ghhhk"),
    n("Maul Strikes"),
    n("I Will Find Them Quickly, Master"),
    n("If The Trace Was Correct"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("The Phantom Menace", qty=2),
    n("Presence Of The Force"),
    n("Gift Of The Master"),
    n("Mandalorian Mishap & Jedi Mind Trick"),
    n("Darth Maul", qty=4),
    n("Galen Marek, Starkiller", qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Sith Probe Droid", True),
    n("Darth Sidious"),
    n("Lord Sidious"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Sonic Bombardment", True, qty=2),
    n("I Have You Now"),
    n("Garindan", True),
    n("P-59"),
    n("Sniper & Dark Strike"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Resistance", True),
    n("Battle Order", True),
    n("Combat Readiness", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Oppressive Enforcement", True),
    n("Imperial Detention"),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
]
DS_ADD = [
    n("Death Star Sentry", True),
    n("No Escape"),
    n("Secret Plans"),
]
