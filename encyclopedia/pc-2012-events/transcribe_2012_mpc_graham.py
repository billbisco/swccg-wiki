#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Thomas Graham.

Source: 2012mpcday1.pdf pages 79–80 (2010 form, 12 shields).
Name Thomas Graham dested Thomas Graham (analog encyclopedia / player-stubs / generate empty;
Joseph Graham is a different person).
p79 Light Yavin 4: Massassi Throne Room. p80 Dark My Lord, Is That Legal?
Username Swccgtm. Pack player-stubs/Thomas_Graham.wiki.
"""
from __future__ import annotations

PLAYER = "Thomas Graham"
USERNAME = "Swccgtm"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 79
DS_PAGE = 80
LS_SCAN = "2012 Match Play Championship Day 1 Thomas Graham LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Thomas Graham DS.png"
LS_DECK_NAME = "TRM"
DS_DECK_NAME = "Senate"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Thomas Graham dested Thomas Graham. "
    "Username Swccgtm. LIGHT checked. Deck Name TRM. Event MPC 2012. "
    "Analog encyclopedia / player-stubs / generate empty except Joseph Graham (different person). "
    "Line 1 cropped remnant TRM dested Yavin 4: Massassi Throne Room from analog "
    "(Deck Name TRM + line 59 Y4 Throne). "
    "Wedge in ship True dested Wedge Antilles In Red Squadron 1 (True NO_DEST no (V) reprint). "
    "Tantive True dested Tantive IV True. "
    "naked 3PO dested Threepio With His Parts Showing. "
    "IL 10 True dested I'll Take The Odds (True NO_DEST no (V) reprint). "
    "Mace True then ditto empty kept separate. "
    "Obi w/ dested Obi-Wan With Lightsaber x2. "
    "Qui w/ dested Qui-Gon Jinn With Lightsaber x2. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Luke SITF dested Luke Skywalker, Strong In The Force True x2. "
    "Sense combo dested Sense. Control combo dested Control & Tunnel Vision. "
    "Don't Tread dested Don't Tread On Me True. "
    "LTWW dested Let The Wookiee Win True x3. "
    "Rebel Leadership True then ditto empty kept separate. "
    "Speak Council dested Speak With The Jedi Council. "
    "We Grand Army dested Wesa Gotta Grand Army x2. "
    "AJR dested A Jedi's Resilience x2. "
    "Luke's Stick dested Luke's Lightsaber. "
    "Scramble Transmission dested Scrambled Transmission True. "
    "Hanjix combo dested Odin Nesloor & First Aid. "
    "Desperate Reach dested The Bith Shuffle & Desperate Reach True. "
    "Jedi Saber dested Jedi Lightsaber True. "
    "Imp Atrocity dested Imperial Atrocity. "
    "Sorry mess combo dested Sorry About The Mess & Blaster Proficiency. "
    "Hoth War Room dested Hoth: Echo Command Center. "
    "JCC dested Coruscant: Jedi Council Chamber True. "
    "AFA dested Anger, Fear, Aggression True. "
    "Line 1 analog dested. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Thomas Graham dested Thomas Graham. "
    "Username Swccgtm. DARK checked. Deck Name Senate. Event MPC 2012. "
    "Line 1 cropped remnant Plead-my-case dested My Lord, Is That Legal? / I Will Make It Legal "
    "from analog (DARK checked + Deck Name Senate + Dark senator 60). "
    "K&D dested Knowledge And Defense True. "
    "Hover car dested STAP x2. "
    "WMATOP dested We Must Accelerate Our Plans x2. "
    "Point Conceded dested Point Conceded. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Outrageous dested This Is Outrageous!. "
    "Motion Supported dested Mobility Support. "
    "Blockade dested Our Blockade Is Perfectly Legal. "
    "Accepting dested Accepting Trade Federation Control. "
    "Short range combo dested Short Range Fighters & Watch Your Back (line 46 and line 54). "
    "I have u now dested I Have You Now. "
    "Laser cannons dested SFS L-s9.3 Laser Cannons. "
    "Lateral D dested Lateral Damage. "
    "Combat R dested Combat Response True x2. "
    "Surface D dested Surface Defense True. "
    "The Emperor dested The Emperor True. "
    "Bridge dested Blockade Flagship: Bridge. "
    "Senate dested Coruscant: Galactic Senate. "
    "Landing Site dested Naboo: Theed Palace Courtyard. "
    "Hounds Tooth dested Hound's Tooth True. "
    "Vader's Ship dested Vader's Personal Shuttle True. "
    "Maul w/ dested Darth Maul With Lightsaber x3. "
    "DSS shield dested I Find Your Lack Of Faith Disturbing True. "
    "Grabber dested Resistance. "
    "Coward dested Come Here You Big Coward. "
    "Line 1 analog dested. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Wedge Antilles In Red Squadron 1"),
    n("Tantive IV", True),
    n("Home One"),
    n("Artoo-Detoo In Red 5"),
    n("Threepio With His Parts Showing"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("I'll Take The Odds"),
    n("Mace Windu", True),
    n("Mace Windu"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Sense"),
    n("Alter"),
    n("Control & Tunnel Vision"),
    n("Hindsight", True),
    n("Don't Tread On Me", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Speak With The Jedi Council"),
    n("Wesa Gotta Grand Army", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Draw Their Fire"),
    n("Luke's Lightsaber"),
    n("Smoke Screen"),
    n("Scrambled Transmission", True),
    n("Mechanical Failure"),
    n("Blaster Deflection", qty=2),
    n("Odin Nesloor & First Aid"),
    n("The Bith Shuffle & Desperate Reach", True),
    n("Jedi Lightsaber", True),
    n("Imperial Atrocity"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sense"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Hoth: Echo Command Center"),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Kiffex"),
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Traffic Control", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Only Jedi Carry That Weapon", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Knowledge And Defense", True),
    n("Orn Free Taa", qty=3),
    n("Lott Dod", qty=3),
    n("Toonbuck Toora", qty=2),
    n("Edcel Bar Gane"),
    n("Tikkes"),
    n("Yeb Yeb Adem'thorn"),
    n("Baskol Yeesrim"),
    n("Aks Moe"),
    n("Bossk", True),
    n("Zuckuss", True),
    n("DS-61-2"),
    n("Darth Vader", True),
    n("Dengar", True),
    n("Baron Soontir Fel"),
    n("Saber 1"),
    n("Punishing One", True),
    n("Black 2", True),
    n("Hound's Tooth", True),
    n("Mist Hunter", True),
    n("Vader's Personal Shuttle", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("STAP", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Point Conceded"),
    n("Squabbling Delegates", qty=3),
    n("Ability, Ability, Ability"),
    n("Limited Resources"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("This Is Outrageous!"),
    n("Mobility Support"),
    n("Our Blockade Is Perfectly Legal"),
    n("Accepting Trade Federation Control"),
    n("Short Range Fighters & Watch Your Back"),
    n("I Have You Now"),
    n("Maul Strikes"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Lateral Damage"),
    n("Combat Response", True, qty=2),
    n("Surface Defense", True),
    n("Short Range Fighters & Watch Your Back"),
    n("The Emperor", True),
    n("First Strike"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Galactic Senate"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Abyss", True),
]
DS_ADD = []
