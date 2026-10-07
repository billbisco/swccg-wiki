#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Calvin Kurten.

Source: 2012BespinRegionals.pdf pages 15–16.
p15 Dark handwritten 2010 Xerox / p16 Light typed 2010 Xerox.
Name Calvin Kurten dested Calvin Kurten analog leftover 2012 Nats /
player-stubs/Calvin_Kurten.wiki. Username blank.
Do not dest as a new person. Do not dest 2012 Nats Kurten 60s again.
"""
from __future__ import annotations

PLAYER = "Calvin Kurten"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2012 Bespin Regionals Calvin Kurten LS.png"
DS_SCAN = "2012 Bespin Regionals Calvin Kurten DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p15 Dark handwritten 2010 Xerox / p16 Light typed 2010 Xerox. "
    "Name Calvin Kurten dested Calvin Kurten analog leftover 2012 Nats / "
    "player-stubs/Calvin_Kurten.wiki. Username blank. Date 7/14/12 Event Bespin Regional. "
    "Do not dest as a new person. Do not dest 2012 Nats Kurten 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox p16 Light. Name Calvin Kurten dested Calvin Kurten. Username blank. "
    "LIGHT checked. Deck Name Wok and Roll dested off article. "
    "There Is Good In Him dested There Is Good In Him / I Can Save Him analog leftover Kurten Nats. "
    "Endor Landing Platform dested Endor: Landing Platform (Docking Bay) analog leftover Kurten Nats. "
    "Threepio With Parts Showing dested Threepio With His Parts Showing analog leftover Kurten Nats. "
    "Noooooooooooo dested Noooooooooooo True analog leftover Arlandson qty=4 at first occurrence. "
    "Rebel Artillery empty qty=8 at first. Ewok Catapult empty qty=8 at first. Ewok Sentry empty qty=8 at first. "
    "Were You Looking For Me? qty=2 at first. Anger, Fear, Aggression True IN THE 60. "
    "Shield A Tragedy Has Occured dested A Tragedy Has Occurred True analog leftover. "
    "Shield 12 A Jedi's Resilience dested analog leftover clip. Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p15 Dark. Name Calvin Kurten dested Calvin Kurten. Username blank. "
    "DARK checked. Deck Name Pretty Pretty Princess dested off article. "
    "Bring Him Before Me dested Bring Him Before Me / Take Your Father's Place analog leftover Bordier. "
    "Imperial Decree True IN THE 60. "
    "Imperial Arrest Order + Secret Plans dested Imperial Arrest Order & Secret Plans analog leftover Cooleo. "
    "Royal Guard dested Emperor's Royal Guard analog leftover qty=7 unique overcount. "
    "Myn Kyneugh empty line 17 and True line 18 kept separate. "
    "Darth Vader, More Machine Than Man True qty=2 and empty line 21 kept separate. "
    "Kecler The Blacke dested Kepler The Black dest as written. "
    "Duty Betrayal + Sacrifice dested Duty, Betrayal And Sacrifice True analog leftover. "
    "Hutt Smooch dest as written. Force Pike qty=6 unique overcount. "
    "We'll Let Fate-a Decide dested We'll Let Fate-a Decide, Huh? True analog leftover Massung. "
    "No Escape empty shield 8 and True shield 10 kept separate. "
    "Knowledge And Defense True IN THE 60. Unique 60 shields 12."
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
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Heading For The Medical Frigate"),
    n("Noooooooooooo", True, qty=4),
    n("Kazak"),
    n("Were You Looking For Me?", qty=2),
    n("Rebel Artillery", qty=8),
    n("Graak"),
    n("Han, Chewie, And The Falcon"),
    n("Ewok Catapult", qty=8),
    n("Don't Underestimate Our Chances"),
    n("Endor: Back Door"),
    n("Ewok Sentry", qty=8),
    n("Surprise Assault"),
    n("Romba"),
    n("Wicket"),
    n("Chief Chirpa", True),
    n("Endor: Hidden Forest Trail"),
    n("Wokling"),
    n("Civil Disorder"),
    n("Nar Shaddaa Wind Chimes"),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Endor: Ewok Village", True),
    n("Logray"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not", True),
    n("Traffic Control", True),
    n("Weapons Display", True),
    n("Wise Advice", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("A Jedi's Resilience"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Imperial Decree", True),
    n("Imperial Arrest Order & Secret Plans"),
    n("The Emperor Is Coming Here?", True),
    n("Insignificant Rebellion"),
    n("Your Destiny"),
    n("Prepared Defenses"),
    n("Death Star II: Throne Room"),
    n("Emperor's Royal Guard", qty=7),
    n("Kir Kanos"),
    n("Myn Kyneugh"),
    n("Myn Kyneugh", True),
    n("Darth Vader, More Machine Than Man", True, qty=2),
    n("Darth Vader, More Machine Than Man"),
    n("Emperor Palpatine", qty=2),
    n("Kepler The Black"),
    n("Arica"),
    n("Spaceport Docking Bay"),
    n("Coruscant: Docking Bay", qty=2),
    n("Death Star II: Docking Bay"),
    n("Coruscant: Night Club", True),
    n("Royal Escort"),
    n("Overseeing It Personally"),
    n("Emperor's Power"),
    n("Presence Of The Force", qty=2),
    n("Hutt Smooch"),
    n("Lone Warrior", qty=3),
    n("Duty, Betrayal And Sacrifice", True),
    n("Brief Loss Of Control"),
    n("Alter"),
    n("Sense", qty=3),
    n("Sneak Attack", qty=3),
    n("Twi'lek Advisor", qty=3),
    n("Force Lightning", qty=2),
    n("Force Pike", qty=6),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans", True),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward", True),
    n("No Escape"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("No Escape", True),
    n("There Is No Try", True),
    n("Battle Order"),
]
DS_ADD = []
