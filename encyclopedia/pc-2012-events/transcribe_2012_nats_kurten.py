#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Calvin Kurten.

Source: 2012NationalsDay1.pdf pages 34–35 (handwritten 2010 Xerox, 12 shields).
Name Calvin Kurten dested Calvin Kurten as written. Username blank.
p34 Light There Is Good In Him. p35 Dark My Lord, Is That Legal?.
Analog leftover generate empty dest as written.
Do not dest as a new identified person until analog identifies.
Pack player-stubs/Calvin_Kurten.wiki.
"""
from __future__ import annotations

PLAYER = "Calvin Kurten"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 34
DS_PAGE = 35
LS_SCAN = "2012 US Nationals Day 1 Calvin Kurten LS.png"
DS_SCAN = "2012 US Nationals Day 1 Calvin Kurten DS.png"
LS_DECK_NAME = "Wok + Role"
DS_DECK_NAME = "I guess that's legal?"
NOTE = "Handwritten 2010 Xerox. Name Calvin Kurten dested Calvin Kurten as written. Username blank."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Calvin Kurten dested Calvin Kurten as written. "
    "Username blank. LIGHT checked. Deck Name Wok + Role. Event Date 6/9/12 Event Name Nationals. "
    "Analog leftover generate empty dest as written. "
    "There Is Good In Him empty dested There Is Good In Him / I Can Save Him analog leftover Kelly. "
    "Republic Logistics dested analog leftover Alperstein True. "
    "I Hope She's All Right dested analog leftover Frafjord True. "
    "I Feel The Conflict dested analog leftover Kelly. "
    "Endor Landing Platform dested Endor: Landing Platform (Docking Bay) analog leftover Hanson. "
    "Endor Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut analog leftover Kelly. "
    "Luke Skywalker, Rebel Scout dested analog leftover Dubreuil True. "
    "Qui-Gon Sinn with Lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover Graham. "
    "Obi-Wan Kenobi with Lightsaber dested Obi-Wan With Lightsaber analog leftover Graham. "
    "Threepio With His Parts Showing dested analog leftover Bollentino. "
    "Home One dested analog leftover Hanson. "
    "Han, Chewie, & the Falcon dested Han, Chewie, And The Falcon analog leftover Booker. "
    "Endor Ewok Village dested Endor: Ewok Village True analog leftover Cooleo. "
    "Endor Back Door dested Endor: Back Door analog leftover Gogolen. "
    "Endor Hidden Forest Trail dested Endor: Hidden Forest Trail analog leftover. "
    "Civil Disorder dested analog leftover Haglund. "
    "Don't Underestimate Our Chances dested analog leftover. "
    "Nar Shaddaa Wind Chimes dested analog leftover Haglund. "
    "Were You Looking For Me? dested analog leftover Booker x2. "
    "Ewok Sentry x8 unique overcount. Ewok Catapult x8 unique overcount. Rebel Artillery x8 unique overcount. "
    "Noooooooooooo dested NOOOOOOOOOOOO! True analog leftover Heine x3 unique overcount. "
    "Wooooooooooo dested Wookiee Roar True analog leftover Frafjord. "
    "AFA dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "A Tragedy Was Occured dested A Tragedy Has Occurred True analog leftover. "
    "Only Jedi Carry That Weapon dested analog leftover Bordier. Unique 60. Shields 10 slots 11–12 blank skip."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Calvin Kurten dested Calvin Kurten as written. "
    "Username blank. DARK checked. Deck Name I guess that's legal?. Event Date 6/9/12 Event Name Nationals. "
    "Analog leftover generate empty dest as written. "
    "My Lord Is That Legal? empty dested My Lord, Is That Legal? analog leftover Smith. "
    "Imperial Arrest Order & Secret Plans dested analog leftover Gogolen. "
    "Battle Order & First Strike dested analog leftover Bordier. "
    "Ni Chuba Na?? dested analog leftover Anderson True. "
    "Prepared Defences dested Prepared Defenses analog leftover. "
    "Naboo: Theed Palace Generator Core dested analog leftover Booker. "
    "Accepting Trade Federation Control dested analog leftover Dalton. "
    "Our Blockade Is Perfectly Legal dested analog leftover SAN. "
    "Boba Fett In Slave I dested analog leftover Booker True. "
    "Bossk In Hound's Tooth dested analog leftover. "
    "Dengar In Punishing One dested analog leftover. "
    "IG-88 In IG-2000 dested analog leftover. "
    "Zuckuss In Mist Hunter dested analog leftover Anderson. "
    "The Emperor dested analog leftover Fernando True. "
    "Rure Haako dested Rune Haako analog leftover. "
    "Lott Dodd dested Lott Dod analog leftover Smith x6 unique overcount. "
    "Baskol Yessrim dested Baskol Yeesrim analog leftover Smith. "
    "Edcel Bar Gane dested analog leftover. "
    "Yeb Yeb Adem'thorn dested analog leftover. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Fire Power dested Firepower True analog leftover Bollentino. "
    "We'll Let Fate-a Decide, Huh? dested analog leftover Pistone. Unique 60. Shields 9 slots 10–12 blank skip."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Republic Logistics", True),
    n("Ewok Celebration"),
    n("I Hope She's All Right", True),
    n("I Feel The Conflict"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Heading For The Medical Frigate"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Threepio With His Parts Showing"),
    n("Chief Chirpa", True),
    n("Wicket"),
    n("Kazak"),
    n("Romba"),
    n("Graak"),
    n("Logray"),
    n("Ewok Sentry", qty=8),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Endor: Ewok Village", True),
    n("Endor: Back Door"),
    n("Endor: Hidden Forest Trail"),
    n("Wokling"),
    n("Civil Disorder"),
    n("Ewok Catapult", qty=8),
    n("Surprise Assault"),
    n("Don't Underestimate Our Chances"),
    n("Nar Shaddaa Wind Chimes"),
    n("Were You Looking For Me?", qty=2),
    n("Rebel Artillery", qty=8),
    n("NOOOOOOOOOOOO!", True, qty=3),
    n("Wookiee Roar", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Aim High", True),
    n("Battle Plan"),
    n("Do, Or Do Not", True),
    n("Ultimatum"),
    n("Traffic Control", True),
    n("Wise Advice", True),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal?"
DS_CARDS = [
    n("My Lord, Is That Legal?"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Battle Order & First Strike"),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses"),
    n("Coruscant: Galactic Senate"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo"),
    n("This Is Outrageous"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("Accepting Trade Federation Control"),
    n("Senate Hovercam"),
    n("The Phantom Menace"),
    n("Presence Of The Force"),
    n("Enter The Bureaucrat"),
    n("Defensive Fire"),
    n("Vote Now", qty=2),
    n("Squabbling Delegates", qty=2),
    n("The Point Is Conceded", qty=2),
    n("Limited Resources", qty=2),
    n("Brief Loss Of Control", True),
    n("Control"),
    n("Sense"),
    n("Boba Fett In Slave I", True),
    n("Bossk In Hound's Tooth"),
    n("Dengar In Punishing One"),
    n("IG-88 In IG-2000"),
    n("Zuckuss In Mist Hunter"),
    n("The Emperor", True),
    n("Rune Haako"),
    n("Dr. Evazan"),
    n("Mara Jade With Lightsaber", True),
    n("Darth Vader With Lightsaber"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Lott Dod", qty=6),
    n("Orn Free Taa", qty=2),
    n("Baskol Yeesrim", qty=2),
    n("Edcel Bar Gane", qty=2),
    n("Yeb Yeb Adem'thorn", qty=2),
    n("Passel Argente", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward", True),
    n("No Escape", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
