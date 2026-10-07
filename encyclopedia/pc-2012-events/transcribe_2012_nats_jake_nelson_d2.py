#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Jake Nelson.

Source: 2012NationalsDay2.pdf pages 9–10 (handwritten 2010 Xerox, 12 shields).
Name Jake N dested Jake Nelson analog leftover Day 1 / 2013 Worlds.
Username blank. p09 Light CCT. p10 Name blank facing dest Jake Nelson.
Do not dest as Aaron Nelson. Do not dest as Mark Walseth.
Do not dest Day 1 Jake Nelson 60s again.
"""
from __future__ import annotations

PLAYER = "Jake Nelson"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2012 US Nationals Day 2 Jake Nelson LS.png"
DS_SCAN = "2012 US Nationals Day 2 Jake Nelson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Jake N dested Jake Nelson analog leftover Day 1. "
    "Username blank. p10 Name blank facing dest Jake Nelson. LIGHT/DARK empty dest from filled 60s. "
    "Do not dest as Aaron Nelson. Do not dest as Mark Walseth. Do not dest Day 1 Jake Nelson 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jake N dested Jake Nelson analog leftover Day 1. "
    "Username blank. LIGHT/DARK empty dest from filled Light 60s. "
    "OML dested Carbon Chamber Testing / My Favorite Decoration analog leftover 2014 MPC. "
    "Luke w/ stick dested Luke With Lightsaber analog leftover Day 1. "
    "Obi w/ stick dested Obi-Wan With Lightsaber analog leftover Day 1. "
    "Qui w/ stick dested Qui-Gon Jinn With Lightsaber analog leftover. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon analog leftover Day 1. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Day 1. "
    "Jedi's Resilience dested A Jedi's Resilience analog leftover Day 1. "
    "Atrocity dested Imperial Atrocity analog leftover Day 1. "
    "Medical Frigate dested Heading For The Medical Frigate analog leftover Day 1. "
    "Bith Shuffle dested The Bith Shuffle analog leftover Day 1. "
    "Keeping Empire Out Forever dested Keeping The Empire Out Forever True analog leftover. "
    "Line 59 Corran Horn + Anger, Fear, Aggression True dest all written lines. "
    "Line 60 Knowledge And Defense crossed skip. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name blank facing p09 Jake N dested Jake Nelson analog leftover Day 1. "
    "Username blank. LIGHT/DARK empty dest from filled Dark 60s. Deck Name Do Nothing joke skip. "
    "Do not dest as Mark Walseth. Combat Readiness True dested Combat Readiness / Full Scale Alert True analog leftover Herold IN THE 60. "
    "SFS Laser Cannons dested SFS L-s9.3 Laser Cannons analog leftover. "
    "Location x3 dested Location, Location, Location analog leftover. "
    "MM & EO dested Masterful Move & Endor Occupation analog leftover Rambo. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Carbon Chamber Testing / My Favorite Decoration"
LS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Guest Quarters"),
    n("Overseer", True),
    n("Luce Soth"),
    n("Luke With Lightsaber", qty=2),
    n("Narrow Escape", qty=2),
    n("Lando's Not A System, He's A Man", True),
    n("You'll Learn If You Survive"),
    n("Rebel Barrier"),
    n("Lesser", True),
    n("Padme Naberrie"),
    n("Dodge", True),
    n("Rebel", True),
    n("Tantive IV"),
    n("Path Of Least Resistance"),
    n("Projection Of A Skywalker"),
    n("Grimtaash"),
    n("Off The Edge", True),
    n("Imperial Atrocity", qty=2),
    n("Travis Brice"),
    n("Palowick Thug"),
    n("Alternating Fighting"),
    n("Cloud City: Downtown"),
    n("Path Of Least Resistance", True),
    n("Strike Force"),
    n("Cloud City: Upper Walkway"),
    n("Leia, Rebel Princess"),
    n("It Could Be Worse", True),
    n("Seeking An Audience"),
    n("Special"),
    n("Alternating To City", qty=2),
    n("LWSMF"),
    n("Path Of Least Resistance", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Dodge"),
    n("Alter"),
    n("Han, Chewie, And The Falcon"),
    n("A Jedi's Resilience", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Heading For The Medical Frigate"),
    n("Lando Calrissian"),
    n("Fall For Credits"),
    n("Clash Of Sabers", True),
    n("The Bith Shuffle"),
    n("Keeping The Empire Out Forever", True),
    n("Wokling"),
    n("Bespin"),
    n("Corran Horn"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Wise Advice", True),
    n("Yavin Sentry", True),
    n("Do, Or Do Not", True),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High", True),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Combat Readiness / Full Scale Alert"
DS_CARDS = [
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Combat Readiness / Full Scale Alert", True),
    n("Inconsequential Losses", True),
    n("I'm Sorry", True),
    n("You May Start Your Landing"),
    n("Imperial Propaganda", True, qty=5),
    n("Imperial Propaganda", qty=2),
    n("Why Didn't You Tell Me", True),
    n("Floating Refuge", True, qty=2),
    n("Clouds", qty=2),
    n("Blizzard 2", True),
    n("A Sith Weapon"),
    n("Location, Location, Location"),
    n("Presence Of The Force", qty=2),
    n("Operational As Planned", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Short Range Fighters", qty=4),
    n("TIE Interceptor", qty=4),
    n("Ghhhk"),
    n("SFS L-s9.3 Laser Cannons", qty=3),
    n("Imperial Artillery", qty=4),
    n("Dark Waters", qty=2),
    n("Trample"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Imperial Decree"),
    n("Death Mark"),
    n("Counter Assault"),
    n("Image Of The Dark Lord"),
    n("No Escape"),
    n("Limited Resources"),
    n("Who Are You Taking This Thing"),
    n("Reactor Terminal"),
    n("Flawless Marksmanship"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("There Is No Try", True),
    n("Come Here You Big Coward", True),
    n("Oppressive Enforcement", True),
    n("Firepower", True),
    n("Fanfare"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Secret Plans", True),
    n("Battle Order", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
