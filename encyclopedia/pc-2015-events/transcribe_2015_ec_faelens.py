#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Jimmy Faelens Day 2 (place 2).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p06 Dark / p07 Light (typed PC forms).
"""
from __future__ import annotations

PLAYER = "Jimmy Faelens"
USERNAME = "JIMMY FRENCH"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 7
DS_PAGE = 6
LS_SCAN = "2015 European Championship Jimmy Faelens LS.png"
DS_SCAN = "2015 European Championship Jimmy Faelens DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 2 circled. p06 Dark / p07 Light typed PC forms. Event Date 10/17/15, Event Name EURO 2015. "
    "Username DS 'JIMMY FRENCH', LS 'JIMMYFRENCH'. DS 3:1 / LS 4:0. "
    "Sheet deck names: DS 'AOBS SCUM 12', LS 'WHAP SPACE' (not used as DECK_NAME)."
)
LS_NOTE = (
    "START We Have A Plan / They Will Be Lost And Confused (sheet 'We Have A Plan/They Will Be Lost And Confu..'). "
    "Line 22 'Were You Looking For Me?' crossed out, handwritten 'All Wings (Combo)' dested All Wings Report In & Darklighter Spin. "
    "Posted Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII (wiki title; not in GEMP file). "
    "Posted Sense (premiere) dested Sense. Posted R-3PO dested R-3PO. "
    "Posted Sorry About The Mess & *Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Posted Free Ride & *Endor Celebration dested Free Ride & Endor Celebration. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "Posted AOBS dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Posted Coruscant (SE) dested Coruscant (Special Edition version). "
    "Posted Imperial City dested Coruscant: Imperial City. "
    "REVIEWED: CONFIRM line 4 \"BRIDGE\" dested Blockade Flagship: Bridge (only DS Bridge site in 2015; Invisible Hand: Bridge is 2019). "
    "Posted Jabba's Palace dested Tatooine: Jabba's Palace. Posted Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Posted Lower Passages dested Jabba's Palace: Lower Passages. Posted Knowledge & Defense dested Knowledge And Defense. "
    "Posted Search & Destroy dested Search And Destroy. Posted U Will Be Dead! dested You'll Be Dead!. "
    "Posted Scum & Villainy dested Scum And Villainy. Posted Cease Fire dested Cease Fire!. "
    "Posted Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "Posted Jabba's Thru With U dested Jabba's Through With You. Posted Oh Switch Off dested Oh, Switch Off. "
    "Posted Zuckuss In Mist Hunter kept. Posted 4-LOM EPP dested 4-LOM With Concussion Rifle. "
    "Posted Dengar EPP dested Dengar With Blaster Carbine. Posted IG-88 EPP dested IG-88 With Riot Gun. "
    "Posted Boba Fett Bounty Hunter dested Boba Fett, Bounty Hunter. Posted Joda Kast dested Jodo Kast. "
    "Posted Xizor dested Prince Xizor. "
    "Shield 'We'll Let Fate A Decide Huh?' dested We'll Let Fate-a Decide, Huh?. "
    "A Useless Gesture listed twice (one (V) checked, one not). Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway", True),
    n("Naboo: Theed Palace Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Anger, Fear, Aggression"),
    n("We'll Take The Long Way", True),
    n("Squadron Assignments"),
    n("Projection Of A Skywalker"),
    n("Naboo"),
    n("Naboo: Boss Nass' Chambers"),
    n("Bravo 1"),
    n("Bravo 2"),
    n("Azure Angel"),
    n("Bravo Fighter", True),
    n("Obi-Wan In Radiant VII"),
    n("Were You Looking For Me?"),
    n("Alternatives To Fighting"),
    n("Wesa Gotta Grand Army", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("We're Doomed"),
    n("Hyper Escape"),
    n("First Aid"),
    n("A Few Maneuvers"),
    n("Ascension Guns", True, qty=2),
    n("Put That Down", True),
    n("Sense", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Jedi Levitation", True, qty=2),
    n("Free Ride & Endor Celebration"),
    n("A Jedi's Resilience"),
    n("Under Attack"),
    n("Impressive, Most Impressive", True),
    n("Mace Windu", True, qty=2),
    n("Anakin Skywalker, Padawan Learner", True),
    n("Captain Rex, 501st Legion", True),
    n("Queen Amidala", qty=2),
    n("Panaka, Protector Of The Queen", qty=2),
    n("Jerus Jannick"),
    n("Ric Olie, Bravo Leader"),
    n("Officer Dolphe"),
    n("Yoda, Master Of The Force"),
    n("Qui-Gon Jinn, Jedi Master", qty=2),
    n("R-3PO", True),
    n("Threepio With His Parts Showing"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Taking Them With Us"),
    n("I'll Try Spinning"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses"),
    n("He Can Go About His Business"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("The Republic No Longer Functions"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Goldenrod"),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City", True),
    n("Blockade Flagship: Bridge"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Lower Passages"),
    n("Knowledge And Defense", True),
    n("Search And Destroy"),
    n("You'll Be Dead!", True),
    n("Presence Of The Force"),
    n("Jabba's Haven", True),
    n("No Escape"),
    n("Scum And Villainy"),
    n("Something Special Planned For Them", True),
    n("Ghhhk"),
    n("Hidden Weapons", qty=2),
    n("Control", qty=2),
    n("Defensive Fire", True),
    n("Cease Fire!", qty=2),
    n("Weapon Levitation"),
    n("They're Still Coming Through!"),
    n("Elis Helrot", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sith Fury", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Jabba's Through With You", qty=2),
    n("Surface Defense", True),
    n("Force Push", True),
    n("Oh, Switch Off", qty=2),
    n("Stun Blaster"),
    n("Vibro-Ax"),
    n("Aurra Sing's Blaster Rifle"),
    n("Zuckuss In Mist Hunter"),
    n("4-LOM With Concussion Rifle"),
    n("Djas Puhr", True),
    n("Dengar With Blaster Carbine", True),
    n("Boba Fett, Bounty Hunter"),
    n("Emperor Palpatine"),
    n("Snoova"),
    n("Jodo Kast"),
    n("IG-88 With Riot Gun"),
    n("Vigo", True),
    n("Jango Fett", True),
    n("Aurra Sing"),
    n("P-59"),
    n("Prince Xizor"),
    n("Guri"),
    n("Bane Malar"),
    n("Bossk", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Vote Of No Confidence"),
    n("Firepower"),
    n("Battle Order"),
    n("There Is No Try"),
]
DS_ADD = []
