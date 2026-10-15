#!/usr/bin/env python3
"""2015 European Championship Day 2: Nico Oster (place 18).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p1-2 Light (p2 top), p2 bottom-p4 Dark, typed category lists.
"""
from __future__ import annotations

PLAYER = "Nico Oster"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 1
DS_PAGE = 3
LS_SCAN = "2015 European Championship Nico Oster LS.png"
DS_SCAN = "2015 European Championship Nico Oster DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18. Typed category lists headed 2015 EM / Nico Oster LS|DS, no form, no username. "
    "LS runs p1 to top of p2; DS starts bottom of p2 (Starting/Locations/first 3 characters) and continues p3-p4. "
    "DS_PAGE=3 per page map. LS 1:3 / DS 3:1 handwritten."
)
LS_NOTE = (
    "Starting: Anger, Fear, Aggression (v) (+Defensive Shields), Yavin 4: Massassi Throne Room, Heading For The Medical Frigate (+3 effects). "
    "START = Yavin 4: Massassi Throne Room (matches wiki). Posted Master Qui-gon dested Master Qui-Gon. "
    "Posted Qui-gon's Lightsaber dested Qui-Gon's Lightsaber. Posted Wise Advise dested Wise Advice. "
    "Sorry About The Mess and Sorry About The Mess & Blaster Proficiency both listed, kept separate. Main 60, shields 15."
)
DS_NOTE = (
    "Starting: Knowledge And Defense (V) (+Defensive Shields), Imperial Entanglements/No One To Stop Us This Time, Tatooine (Premiere), "
    "Tatooine: Desert Heart, Devastator, Prepared Defenses (+3 effects). START = Imperial Entanglements (matches wiki). "
    "Posted Tatooine (Premiere) dested Tatooine. Posted Corporal Dresolyn dested Corporal Drelosyn. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Nar Shaddaa"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Corran Horn", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker", True),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Keeper Of The Peace"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Azure Angel"),
    n("Han, Chewie, And The Falcon"),
    n("Obi-Wan In Radiant VII"),
    n("Red Squadron 1"),
    n("Tantive IV", True),
    n("Anakin's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Civil Disorder", True),
    n("Draw Their Fire"),
    n("Honor Of The Jedi"),
    n("Like My Father Before Me"),
    n("Sai'torr Kal Fas", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Escape Pod", True),
    n("Free Ride & Endor Celebration"),
    n("Houjix"),
    n("Sorry About The Mess"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("Were You Looking For Me?", qty=2),
    n("Wesa Gotta Grand Army", qty=4),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Ship?"),
]
LS_ADD = []

DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Tatooine"),
    n("Tatooine: Desert Heart"),
    n("Devastator"),
    n("Prepared Defenses"),
    n("Executor: Docking Bay"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Admiral Motti", True),
    n("Admiral Ozzel"),
    n("Admiral Piett"),
    n("Commander Desanne"),
    n("Corporal Drelosyn"),
    n("Darth Vader", True),
    n("DS-61-5"),
    n("Emperor Palpatine"),
    n("General Veers", True),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Mara Jade With Lightsaber"),
    n("Sergeant Barich"),
    n("Sergeant Elsek"),
    n("Sergeant Irol"),
    n("Conquest", True),
    n("Flagship Executor"),
    n("Blizzard 1"),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Tempest Scout 1"),
    n("Tempest Scout 3", True),
    n("Battle Deployment"),
    n("We're In Attack Position Now", qty=2),
    n("Endor Shield", True),
    n("Imperial Arrest Order"),
    n("Imperial Decree", True),
    n("Imperial Justice", True),
    n("Mobilization Points"),
    n("Something Special Planned For Them", True),
    n("Tatooine Occupation", qty=3),
    n("Cease Fire!", qty=2),
    n("Close Call", True),
    n("Force Push", True),
    n("I Can't Shake Him!", True, qty=3),
    n("Imperial Barrier"),
    n("Imperial Command", qty=3),
    n("Ommni Box & It's Worse"),
    n("Trample"),
    n("Turn It Off! Turn It Off!", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Wipe Them Out, All Of Them"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
