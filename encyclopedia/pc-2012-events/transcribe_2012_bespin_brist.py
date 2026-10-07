#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Brandon Brist Dark only.

Source: 2012BespinRegionals.pdf page 11 (typed 2010 Xerox).
p11 Dark Name Brandon Brist Username bristicles dested Brandon Brist analog leftover
2008 Worlds generate. Encyclopedia / player-stubs empty dest Name box as written.
p12 Nats bound-in skip. p13–p14 MN States other-event skip. No facing Bespin Light.
LS_CARDS empty skip Light analog leftover Baroni Day 2 / Nelson missing side.
Do not dest as a new person. Pack player-stubs/Brandon_Brist.wiki.
"""
from __future__ import annotations

PLAYER = "Brandon Brist"
USERNAME = "bristicles"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 11
DS_PAGE = 11
LS_SCAN = ""
DS_SCAN = "2012 Bespin Regionals Brandon Brist DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox p11 Dark. Name Brandon Brist dested Brandon Brist analog leftover "
    "2008 Worlds generate. Username bristicles. Event Date blank. "
    "p12 Nats bound-in skip (6/9/12 Brian Herold AirDog 2003). "
    "p13–p14 MN States other-event skip. No facing Bespin Light. Hub Light stays —. "
    "Do not dest as a new person."
)
LS_NOTE = (
    "No facing Bespin Light. p12 Nats bound-in skip. p13–p14 MN States other-event skip. "
    "LS_CARDS empty skip Light analog leftover Baroni Day 2 empty Same as."
)
DS_NOTE = (
    "Typed 2010 Xerox p11 Dark. Name Brandon Brist dested Brandon Brist. Username bristicles. "
    "DARK checked. Deck Name v[ery original deck title] dested off article. "
    "Tatooine (Starting) dested Tatooine analog leftover. "
    "Combat Readiness (Starting) dested Combat Readiness / Full Scale Alert True analog leftover Herold. "
    "I've Lost Artoo dested I've Lost Artoo True analog leftover Atkin. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Zuckuss in Mist Hunter crossed dest Mara Jade analog leftover Gardner crossed-with-replacement. "
    "Boba Fett, Prepared Hunter dested analog leftover Atkin. "
    "Elis in Hinthra dested Elis In Hinthra True analog leftover. "
    "Maul's Double Bladed Lighsaber dested Maul's Double-Bladed Lightsaber analog leftover Morgan. "
    "Sniper / Dark Strike dested Sniper & Dark Strike analog leftover Morgan qty=2. "
    "Phantom Menace dested The Phantom Menace analog leftover Morgan. "
    "lave them to me dested Leave Them To Me analog leftover Chris. "
    "Knowledge And Defense True IN THE 60. None Shall Pass True qty=4. Sense qty=4. "
    "Shields 11–12 empty skip unique 10 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []

DS_START = "Combat Readiness / Full Scale Alert"
DS_CARDS = [
    n("Tatooine"),
    n("Combat Readiness / Full Scale Alert", True),
    n("Tatooine: Jabba's Palace"),
    n("I've Lost Artoo", True),
    n("Sundown", True),
    n("Gift Of The Master", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Tatooine: Desert Landing Site"),
    n("Darth Maul", qty=3),
    n("Arica", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Mara Jade"),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear", True),
    n("Dengar In Punishing One"),
    n("Bossk In Hound's Tooth", True),
    n("Elis In Hinthra", True),
    n("Victory", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Mara Jade's Lightsaber", True),
    n("Trophy Of A Kill", True),
    n("None Shall Pass", True, qty=4),
    n("Imperial Barrier", qty=3),
    n("Force Field", True, qty=3),
    n("You Are Beaten", qty=3),
    n("Sniper & Dark Strike", qty=2),
    n("Sense", qty=4),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Alter", True),
    n("Elis Helrot"),
    n("Vader's Obsession"),
    n("The Circle Is Now Complete"),
    n("Force Push", True),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("The Phantom Menace"),
    n("Tatooine Occupation"),
    n("Trained In The Jedi Arts", True),
    n("Special Delivery", True),
    n("Disarmed"),
    n("Blaster Rack", True),
    n("Deep Hatred", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Leave Them To Me"),
    n("There Is No Try"),
    n("A Useless Gesture"),
    n("Abyss", True),
]
DS_ADD = []
