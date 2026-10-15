#!/usr/bin/env python3
"""2015 European Championship: Jerome Nitschke Day 2 (place 11).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p24 Dark / p25 Light (handwritten).
"""
from __future__ import annotations

PLAYER = "Jerome Nitschke"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 25
DS_PAGE = 24
LS_SCAN = "2015 European Championship Jerome Nitschke LS.png"
DS_SCAN = "2015 European Championship Jerome Nitschke DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 11 circled. p24 Dark / p25 Light handwritten. Name box 'Jerome', Username box 'Nitschke' (surname written in the "
    "username box, so USERNAME left blank). Event Name EURO 2015. DS 2:2 / LS 2:1. "
    "Sheet deck names: DS 'Cookie Creme Toast', LS 'Watch your Wife' (not used as DECK_NAME). "
    "Ditto lines take the V of the line they copy unless their own box differs."
)
LS_NOTE = (
    "Posted Watch your step dested Watch Your Step / This Place Can Be A Little Rough. Posted tatooine dested Tatooine. "
    "Posted tatooine: DB 94 dested Tatooine: Docking Bay 94. Posted Squadron assignements dested Squadron Assignments. "
    "Posted Patrol craft (+3 ditto) dested Patrol Craft x4. Palace Raider lines 17 (V) / 18 / 19 ditto: 1 V + 2 non-V. "
    "Posted Mearx Terrik dested Mirax Terrik. Posted tatooine: Lars moisture farm dested Tatooine: Lars' Moisture Farm. "
    "Posted Projection of skywalker dested Projection Of A Skywalker. Posted Inconsequential barriers dested Inconsequential Barriers. "
    "Posted Free ride & endor celebration dested Free Ride & Endor Celebration. Posted Nar shaddaa WC & OOS dested Nar Shaddaa Wind Chimes & Out Of Somewhere. "
    "Posted All wings Report In & DS dested All Wings Report In & Darklighter Spin (x3). Posted Stay sharp dested Stay Sharp!. "
    "Posted X-wing Laser Canon dested X-wing Laser Cannon (lines 37 and 58, x2). "
    "Shields: Jabba's prize kept (wiki shield title); goldenrod kept as written; Another pathetic lifeform dested Another Pathetic Lifeform; "
    "affect mind dested Affect Mind. Main 60, shields 15."
)
DS_NOTE = (
    "START Carbon Chamber Testing / My Favorite Decoration (sheet 'Carbon Chamber testing'). "
    "Posted Cloud city: security tower dested Cloud City: Security Tower. Posted Jabba's palace: audience ch dested Jabba's Palace: Audience Chamber. "
    "Posted Blockade flagship bridge dested Blockade Flagship: Bridge. Posted ability, ability, ability dested Ability, Ability, Ability. "
    "Posted We must accelerate our plans (+3 ditto) dested x4. Posted Cease fire dested Cease Fire!. Sith Fury 23 V / 24 ditto unchecked: 1 V + 1 non-V. "
    "Force Field 27/28 both V. Posted Elis helrot dested Elis Helrot. Posted Ghkk dested Ghhhk. "
    "Posted Masterful Move & EO (+ditto) dested Masterful Move & Endor Occupation x2. "
    "Posted Arica (sheet 'Anca') dested Arica V. Count Dooku 41 V + 2 ditto unchecked: 1 V + 2 non-V. "
    "Posted Darth Vader, DLOTS (+ditto) dested Darth Vader, Dark Lord Of The Sith x2. "
    "Posted Danoe dested Daroe (52 V, 53 ditto unchecked). Posted 4 Lom with Concussion rifle dested 4-LOM With Concussion Rifle. "
    "Posted Knowledge and defense dested Knowledge And Defense V. "
    "Shields: Sesret plans dested Secret Plans; I find your lack of Faith disturb dested I Find Your Lack Of Faith Disturbing; "
    "Imperial detention kept (wiki title); Do they have a code clearence dested Do They Have A Code Clearance?. Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Squadron Assignments"),
    n("I Must Be Allowed To Speak", True),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("Patrol Craft", qty=4),
    n("Red Squadron 1"),
    n("Outrider"),
    n("Millennium Falcon"),
    n("Artoo-Detoo In Red 5"),
    n("Palace Raider", True),
    n("Palace Raider", qty=2),
    n("Melas", True, qty=2),
    n("Lando Calrissian", True),
    n("Dash Rendar"),
    n("Wedge Antilles"),
    n("Owen Lars & Beru Lars"),
    n("Talon Karrde"),
    n("Mirax Terrik"),
    n("Captain Han Solo"),
    n("Luke Skywalker", True),
    n("Chewbacca"),
    n("Obi-Wan Kenobi", True),
    n("Tatooine: Lars' Moisture Farm"),
    n("Kessel"),
    n("Projection Of A Skywalker"),
    n("Tatooine Celebration", qty=2),
    n("X-wing Laser Cannon", qty=2),
    n("Combined Fleet Action"),
    n("Jedi Levitation", True, qty=2),
    n("Inconsequential Barriers"),
    n("Moving To Attack Position"),
    n("A Few Maneuvers"),
    n("Harvest"),
    n("It's A Hit!"),
    n("Free Ride & Endor Celebration"),
    n("Choke"),
    n("Fallen Portal"),
    n("Rebel Barrier"),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Control & Tunnel Vision", qty=2),
    n("Stay Sharp!"),
    n("Old Ben"),
    n("No Questions Asked"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize"),
    n("Another Pathetic Lifeform"),
    n("Your Ship?"),
    n("Your Insight Serves You Well"),
    n("Weapons Display"),
    n("Ultimatum"),
    n("The Republic No Longer Functions"),
    n("Simple Tricks And Nonsense"),
    n("Goldenrod"),
    n("Ounee Ta"),
    n("He Can Go About His Business"),
    n("Affect Mind"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Prize"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console"),
    n("Surface Defense", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Blockade Flagship: Bridge"),
    n("Blast Door Controls"),
    n("Security Precautions"),
    n("The Phantom Menace"),
    n("Search And Destroy"),
    n("Ability, Ability, Ability", True),
    n("Zuckuss In Mist Hunter"),
    n("Emperor's Personal Shuttle"),
    n("Maul's Sith Infiltrator"),
    n("Dooku's Lightsaber", True),
    n("We Must Accelerate Our Plans", qty=4),
    n("Cease Fire!"),
    n("Sith Fury", True),
    n("Sith Fury"),
    n("A Dark Time For The Rebellion", True),
    n("Stunning Leader"),
    n("Force Field", True, qty=2),
    n("Elis Helrot"),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Sense"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Imperial Barrier"),
    n("You Are Beaten"),
    n("Hidden Weapons"),
    n("IG-88"),
    n("Arica", True),
    n("Count Dooku", True),
    n("Count Dooku", qty=2),
    n("Darth Vader With Lightsaber"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("P-59"),
    n("Sith Probe Droid", True),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Daroe", True),
    n("Daroe"),
    n("Emperor Palpatine", qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("Jango Fett"),
    n("Grand Moff Tarkin", True),
    n("4-LOM With Concussion Rifle"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("A Useless Gesture"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("You Cannot Hide Forever"),
    n("Vote Of No Confidence"),
    n("Firepower"),
    n("Imperial Detention"),
    n("Leave Them To Me"),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = []
