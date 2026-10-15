#!/usr/bin/env python3
"""2015 European Championship: Marvin Tegeler Day 2 (place 8).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p18 Dark (typed) / p19 Light (handwritten).
"""
from __future__ import annotations

PLAYER = "Marvin Tegeler"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 19
DS_PAGE = 18
LS_SCAN = "2015 European Championship Marvin Tegeler LS.png"
DS_SCAN = "2015 European Championship Marvin Tegeler DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 8 circled. p18 Dark typed list / p19 Light handwritten. Name 'Marvin Tegeler' both sheets, Username blank. "
    "DS 3:1 / LS 2:2 (LS score overwritten)."
)
LS_NOTE = (
    "Posted WHAP dested We Have A Plan / They Will Be Lost And Confused. Posted Evac Control dested Evacuation Control. "
    "Posted Free Ride Combo dested Free Ride & Endor Celebration. Posted Theed Palace Courtyard/Hallway/Throne Room dested Naboo: Theed Palace ... "
    "Posted Sai'tor dested Sai'torr Kal Fas. Posted Sorry About The Mess Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Posted OOC Combo dested Out Of Commission & Transmission Terminated. Posted Hear Me Baby dested Hear Me Baby, Hold Together. "
    "Posted Boss Nass Chambers dested Naboo: Boss Nass' Chambers. Posted Qui-Gon Jinn's/Obi-Wan's/Anakin's/Mace Windu's LS dested ...'s Lightsaber. "
    "Posted Obi-Wan Kenobi, JK dested Obi-Wan Kenobi, Jedi Knight. Posted Anakin Skywalker, PL dested Anakin Skywalker, Padawan Learner. "
    "Posted Captain Rex dested Captain Rex, 501st Legion. Posted Threepio with Parts Showing dested Threepio With His Parts Showing. "
    "Line 59 U-3PO crossed out, R-3PO V written: dested R-3PO (Ar-Threepio) V. "
    "Mace Windu V and Master Qui-Gon V each have a ditto line below; V applied to both copies. "
    "REVIEWED: CONFIRM line 57 \"Yoxgit\" (scrawl) dested Yoxgit. "
    "Shields: Posted Insight V dested Your Insight Serves You Well; Posted Republic No Longer Fn dested The Republic No Longer Functions; "
    "Posted Go About His Business dested He Can Go About His Business; line 8 'Don't Fo..' crossed, Planetary Defenses written. "
    "Shields 12 + 3 in Additional Cards (Weapons Display V, Tragedy dested A Tragedy Has Occurred, Jedi Carry That Weapons dested Only Jedi Carry That Weapon) = 15. "
    "Goldenrod: kept as written (GEMP only has the later combo). Main 60."
)
DS_NOTE = (
    "START Carbon Chamber Testing / My Favorite Decoration (sheet 'Carbon Chamber Testing/My Favourite Decoratio'). "
    "Posted Carbonite Chamber Consonle dested Carbonite Chamber Console. Posted Jabba's Price dested Jabba's Prize. "
    "Posted U-3PO dested U-3PO (Yoo-Threepio). Posted Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Posted Ghhhk & Those Rebels Won't Escape Us kept. Any Methods Necessary (Starting: Prison+BH), IG-88 (Starting), Jabba's Palace: Dungeon (Starting). "
    "Line 60 Anger, Fear, Aggression crossed out, 'K+D' written with (V) box checked: dested Knowledge And Defense V. "
    "Shields handwritten: Allegations dested Allegations Of Corruption; Useless Gesture dested A Useless Gesture; Secret Plan dested Secret Plans; "
    "Fate Decide, HUH? dested We'll Let Fate-a Decide, Huh? (wiki title); Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "Handwritten ticks next to Fanfare, Firepower, You Cannot Hide Forever, Faith Disturbing, Coward read as V. "
    "Shields 12 + 3 in Additional Cards (Coward dested Come Here You Big Coward; Code Clearance dested Do They Have A Code Clearance?; Imperial Detention) = 15. Main 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Evacuation Control", True),
    n("Jedi Levitation", True, qty=2),
    n("Free Ride & Endor Celebration"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway", True),
    n("Naboo: Theed Palace Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("We'll Take The Long Way"),
    n("Grimtaash"),
    n("It's A Trap!"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Nabrun Leids"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Sense"),
    n("Control & Tunnel Vision"),
    n("Were You Looking For Me?"),
    n("Out Of Commission & Transmission Terminated"),
    n("Ascension Guns", True),
    n("Hear Me Baby, Hold Together", True),
    n("Blaster Deflection"),
    n("It Could Be Worse"),
    n("Houjix"),
    n("We're Doomed"),
    n("Clash Of Sabers"),
    n("Escape Pod", True),
    n("A Jedi's Resilience"),
    n("Under Attack"),
    n("Impressive, Most Impressive", True),
    n("Disarmed"),
    n("Ounee Ta"),
    n("Naboo: Boss Nass' Chambers"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight", qty=2),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Queen Amidala", qty=2),
    n("Panaka, Protector Of The Queen", qty=2),
    n("Yoda, Master Of The Force"),
    n("Captain Rex, 501st Legion"),
    n("Jerus Jannick"),
    n("Yoxgit"),
    n("Threepio With His Parts Showing"),
    n("R-3PO (Ar-Threepio)", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind", True),
    n("He Can Go About His Business"),
    n("Planetary Defenses"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Goldenrod"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console"),
    n("Cloud City: Security Tower"),
    n("Jabba's Prize"),
    n("Any Methods Necessary"),
    n("IG-88", True),
    n("Jabba's Palace: Dungeon"),
    n("Despair", True),
    n("Force Lightning"),
    n("Count Dooku", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Stunning Leader", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Search And Destroy"),
    n("Disarmed", qty=2),
    n("Ysanne Isard"),
    n("Sense"),
    n("Jabba's Haven"),
    n("Darth Vader With Lightsaber", qty=2),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Force Field", True),
    n("Emperor Palpatine", qty=2),
    n("Dooku's Lightsaber"),
    n("Hoth: Ice Plains (5th Marker)"),
    n("You Are Beaten"),
    n("Nal Hutta"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imperial Barrier", qty=2),
    n("Jabba's Palace: Audience Chamber"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("First Strike"),
    n("Sniper & Dark Strike"),
    n("Arica"),
    n("Cold Feet", True),
    n("Much Anger In Him"),
    n("Stormtrooper Garrison"),
    n("Grand Moff Tarkin", True),
    n("Close Call", True),
    n("Blockade Flagship: Bridge"),
    n("No Escape"),
    n("Emperor's Personal Shuttle"),
    n("Boba Fett, Bounty Hunter"),
    n("I Have You Now"),
    n("Dr. Evazan", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Vote Of No Confidence"),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?"),
    n("Imperial Detention"),
]
DS_ADD = []
