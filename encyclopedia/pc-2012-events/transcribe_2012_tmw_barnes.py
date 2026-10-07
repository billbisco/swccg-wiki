#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: James Barnes.

Source: 2012TMWDay1.pdf pages 9–10 (typed slang printout, not a handwritten
Xerox form). Name James Barnes dested James Barnes analog leftover 2013 TMW /
2014 TMW / player-stubs/James_Barnes.wiki. Username blank.
p09 Light. p10 Dark. Do not dest as a new person. Do not dest 2013 TMW
Barnes 60s again.
"""
from __future__ import annotations

PLAYER = "James Barnes"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2012 Texas Mini Worlds Day 1 James Barnes LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 James Barnes DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name James Barnes dested James Barnes analog leftover 2013 TMW. "
    "Username blank. Do not dest as a new person. Do not dest 2013 TMW Barnes 60s again."
)
LS_NOTE = (
    "Typed slang printout. Name James Barnes dested James Barnes. Username blank. "
    "Anger, Fear, Aggression True dested analog leftover IN THE 60. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber analog leftover. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "EPP Qui-gon dested Qui-Gon Jinn With Lightsaber analog leftover qty=2. "
    "EPP Obi dested Obi-Wan Kenobi With Lightsaber analog leftover. "
    "Artoo, Brave Little Droid dested leftover_xerox True. "
    "Threepio with His Parts Showing dested Threepio With His Parts Showing analog leftover. "
    "Han, Chewie, and the Falcon dested Han, Chewie, And The Falcon analog leftover qty=2. "
    "Sai Tor dested Sai'torr Kal Fas analog leftover True. "
    "Strikeforce dested Strike Force analog leftover Richards True. "
    "Don't Forget the Droids dested Don't Forget The Droids analog leftover True qty=2. "
    "Sorry About The Mess combo dested Sorry About The Mess & Blaster Proficiency analog leftover Barnes 2013. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements analog leftover. "
    "Houjix combo dested Houjix & Out Of Nowhere analog leftover Lingrell. "
    "Shield Simple Tricks & Nonsense dested Simple Tricks And Nonsense analog leftover. "
    "Shield Do Or Do Not dested Do, Or Do Not analog leftover Barnes 2013. "
    "Shield Yavin Sentry dested Massassi Base Sentry analog leftover Shaw True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed slang printout. Name James Barnes dested James Barnes. Username blank. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover True IN THE 60. "
    "SYCFA dested Set Your Course For Alderaan analog leftover Walseth. "
    "Prepared Defense dested Prepared Defenses analog leftover True. "
    "A Million Voices dested A Million Voices Crying Out analog leftover Cullen. "
    "EPP Maul dested Darth Maul With Lightsaber analog leftover qty=2. "
    "Vader, Betrayer dested Darth Vader, Betrayer Of Jedi analog leftover. "
    "MM&EO dested Masterful Move & Endor Occupation analog leftover. "
    "He Is Not Ready & Propaganda dested He Is Not Ready & Imperial Propaganda analog leftover Jellison. "
    "Tarkin Doctrine dested Tarkin's Doctrine analog leftover McCune. "
    "Shield Coward dested Come Here You Big Coward analog leftover. "
    "Shield We'll Let-a Fate Decide, HUH? dested We'll Let Fate-a Decide, Huh? analog leftover Richards. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Kiffex"),
    n("Coruscant: Night Club"),
    n("Home One: War Room"),
    n("Hoth: Echo War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Yoda, Master Of The Force"),
    n("Obi-Wan Kenobi With Lightsaber"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Padme Naberrie", True),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Artoo, Brave Little Droid", True),
    n("Threepio With His Parts Showing"),
    n("IL-19"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Tantive IV", True),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True, qty=2),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Strike Force", True),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("A Jedi's Plans"),
    n("Don't Forget The Droids", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Desperate Reach", True),
    n("Hear Me Baby, Hold Together", True),
    n("Blaster Deflection", qty=2),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Houjix & Out Of Nowhere"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Massassi Base Sentry", True),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Weapons Display", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Set Your Course For Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Rendili"),
    n("Nal Hutta"),
    n("Corulag"),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Darth Sidious", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Protocol Failure"),
    n("Overwhelmed", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True),
    n("Force Push", True),
    n("Relentless Pursuit", qty=2),
    n("Stunning Leader", qty=2),
    n("Cease Fire!"),
    n("Force Field", True),
    n("Imperial Command"),
    n("Why Didn't You Tell Me?", True),
    n("Myn Kenaugh", True),
    n("Arica"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Judicator", qty=2),
    n("Tyrant"),
    n("Thunderflare"),
    n("Conquest"),
    n("Devastator", True),
    n("Visage"),
    n("Stalker", True),
    n("Victory"),
    n("Intensify The Forward Batteries", qty=2),
    n("The Phantom Menace"),
    n("Imperial Propaganda", True, qty=2),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Image Of The Dark Lord", True),
    n("Lateral Damage", qty=2),
    n("Tarkin's Doctrine"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Plan"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
