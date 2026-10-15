#!/usr/bin/env python3
"""2015 European Championship Day 2: John Moorley (place 15).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p32 Dark / p33 Light handwritten sheets.
"""
from __future__ import annotations

PLAYER = "John Moorley"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 33
DS_PAGE = 32
LS_SCAN = "2015 European Championship John Moorley LS.png"
DS_SCAN = "2015 European Championship John Moorley DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 15. Handwritten. Name John Moorley (LS sheet looks like 'John Morley'). Username blank. "
    "DS 2:2 / LS 2:2 written in Event Name box."
)
LS_NOTE = (
    "Starts Yavin 4: Massassi Throne Room (line 1), matches wiki. "
    "Posted Naboo Battle Plans dested Naboo: Battle Plains. Posted Wohling dested Wokling. Posted Sai'torr hal fas dested Sai'torr Kal Fas. "
    "Posted Threepio with parts showing dested Threepio With His Parts Showing. Posted Qui-Gon Jinn's lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Posted Sorry about the mess / Blaster prof dested Sorry About The Mess & Blaster Proficiency. "
    "Posted The Bith Shuffle / Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Posted All wings report in / Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Posted Free Ride / Endor Celebration dested Free Ride & Endor Celebration (V box scribbled, read as checked). "
    "Posted Heading for the Medical Frigate and Anger, Fear, Aggression as plain cards (V boxes blank). "
    "Posted Professor (V checked) dested The Professor (not a shield; listed in shield section, kept as shield). "
    "Posted Do or Do not dested Do, Or Do Not. Obi-Wan In Radiant VII is a VS14 virtual card (on wiki, not in GEMP DB). Main 60, shields 15."
)
DS_NOTE = (
    "Starts Hunt Down And Destroy The Jedi (line 1), matches wiki. "
    "Posted Executor: Holo theatre dested Executor: Holotheatre. Posted Blockade flagship: Hallway/Bridge dested Blockade Flagship: Hallway/Bridge. "
    "Posted Ender: Back door dested Endor: Back Door. Posted Darth vader, Dark lord of the sith dested Darth Vader, Dark Lord Of The Sith. "
    "Posted Dr Evazan and Ponda Baba dested Dr. Evazan & Ponda Baba (V box scribbled out, no V card; not V). "
    "Posted Vader's lightsaber dested Vader's Lightsaber as written. Posted Repared Defenses dested Prepared Defenses. "
    "Posted Masterful Move / Endor occupation dested Masterful Move & Endor Occupation. "
    "Posted Ommni Box / It's Worse dested Ommni Box & It's Worse. Posted Ghhhk dested Ghhhk. "
    "Posted We'll let fate-a decide, Huh dested We'll Let Fate-a Decide, Huh?. Posted Do they have a code clearance dested Do They Have A Code Clearance?. "
    "Posted I find your lack of faith disturbing (shield list) kept as shield. Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Nar Shaddaa"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber"),
    n("Cloud City: Lower Corridor"),
    n("Naboo: Battle Plains"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Like My Father Before Me"),
    n("Civil Disorder", True),
    n("Draw Their Fire"),
    n("Honor Of The Jedi"),
    n("Corran Horn In Rogue 9"),
    n("Wedge In Red Squadron 1"),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII"),
    n("Azure Angel"),
    n("Han, Chewie, And The Falcon"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Threepio With His Parts Showing"),
    n("Rep Been"),
    n("Boss Nass"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Yoda, Keeper Of The Peace"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Master Qui-Gon", True, qty=3),
    n("Leia, Rebel Princess"),
    n("Jar Jar Binks"),
    n("R2-D2", True),
    n("Mace Windu", True, qty=2),
    n("Wesa Gotta Grand Army", qty=5),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Antilles Maneuver", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Escape Pod", True, qty=2),
    n("We Wish To Board At Once", True),
    n("Hear Me Baby, Hold Together", True),
    n("Were You Looking For Me?"),
    n("Houjix"),
    n("Speak With The Jedi Council"),
    n("Free Ride & Endor Celebration", True),
    n("A Jedi's Concentration"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Affect Mind", True),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Endor: Back Door"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Lord Vader", qty=2),
    n("Grand Moff Tarkin", True),
    n("Boba Fett, Bounty Hunter"),
    n("Janus Greejatus"),
    n("Count Dooku", qty=3),
    n("Jango Fett"),
    n("4-LOM With Concussion Rifle", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=3),
    n("Blizzard 4", qty=2),
    n("Dooku's Lightsaber"),
    n("Vader's Lightsaber"),
    n("Visage Of The Emperor", qty=3),
    n("The Phantom Menace", qty=3),
    n("First Strike"),
    n("Expand The Empire"),
    n("Search And Destroy"),
    n("Conduct Your Search"),
    n("Blaster Rack", True),
    n("Ability, Ability, Ability", True),
    n("Blast Door Controls"),
    n("No Escape"),
    n("Presence Of The Force"),
    n("Prepared Defenses"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ommni Box & It's Worse"),
    n("Ghhhk"),
    n("Maul Strikes"),
    n("Sonic Bombardment"),
    n("Force Lightning", qty=2),
    n("Force Field", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Vote Of No Confidence"),
    n("Do They Have A Code Clearance?"),
    n("Resistance"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
