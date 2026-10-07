#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Jake Nelson.

Source: 2012BespinRegionals.pdf pages 31–32.
p31 Dark handwritten 2010 Xerox / p32 Light handwritten 2010 Xerox.
Name Jake N dested Jake Nelson analog leftover generate_2012_nats.py CANON /
player-stubs/Jake_Nelson.wiki. Username blank.
Do not dest as Aaron Nelson. Do not dest 2012 Nats Day 1 / Day 2 Jake Nelson 60s again.
Pack player-stubs/Jake_Nelson.wiki.
"""
from __future__ import annotations

PLAYER = "Jake Nelson"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 32
DS_PAGE = 31
LS_SCAN = "2012 Bespin Regionals Jake Nelson LS.png"
DS_SCAN = "2012 Bespin Regionals Jake Nelson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p31 Dark handwritten 2010 Xerox / p32 Light handwritten 2010 Xerox. "
    "Name Jake N dested Jake Nelson analog leftover generate_2012_nats.py CANON / "
    "player-stubs/Jake_Nelson.wiki. Username blank. "
    "Event Date blank both dest both as Bespin facing pair analog leftover Cooleo. "
    "Deck Name Classic / WYS dested off article. "
    "Do not dest as Aaron Nelson. Do not dest 2012 Nats Day 1 / Day 2 Jake Nelson 60s again. "
    "Pack player-stubs/Jake_Nelson.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p32 Light. Name Jake N dested Jake Nelson. Username blank. "
    "LIGHT checked. Event Date blank. Deck Name WYS dested off article. "
    "Line 1 QMC dested Quiet Mining Colony / Independent Operation analog leftover Nieland. "
    "CC Guest Quarters dested Cloud City: Guest Quarters analog leftover Nieland. "
    "Kabe Cindros dested Kal'Falnl C'ndros analog leftover Nieland. "
    "P Thyss dested Pucumir Thryss analog leftover Nieland. "
    "Qui-Gon w/ stick dested Qui-Gon Jinn With Lightsaber analog leftover Nieland qty=2. "
    "Lando Calrissian True lines 11 and 54 dest qty=2 at first analog leftover Nieland. "
    "Alternates To Fighting dested Alternatives To Fighting analog leftover Nieland qty=3. "
    "Obi w/ stick dested Obi-Wan With Lightsaber analog leftover Nieland qty=3 unique overcount. "
    "Override True dested Overseer True analog leftover Nieland. "
    "Luke w/ stick dested Luke With Lightsaber analog leftover Nieland qty=2. "
    "Path Of Least Resistance qty=4 unique overcount analog leftover Nieland qty=3. "
    "Hard to see dested Harc Seff True analog leftover Nieland. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon analog leftover Nieland. "
    "CC West Gallery dested Cloud City: West Gallery analog leftover Anderson. "
    "Imperial Atrocity empty line 37 and True line 42 kept separate. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Nieland. "
    "Anger, Fear, Aggression True IN THE 60. Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p31 Dark. Name Jake N dested Jake Nelson. Username blank. "
    "DARK checked. Event Date blank. Deck Name Classic dested off article. "
    "Line 1 clipped dest Black 2 True analog leftover Li extra L01. "
    "Slave 1 Symbol of Fear dested Slave I, Symbol Of Fear True analog leftover Li. "
    "The Mandalorian father of Fett dested Jango Fett, The Assassin True analog leftover Li. "
    "Senate dested Coruscant: Galactic Senate analog leftover nats Jake empty line 9; "
    "line 35 Coruscant crossed dest Senate True kept separate analog leftover differing checkbox. "
    "Short Range Fighters Combo dested Short Range Fighters & Watch Your Back! analog leftover Massung qty=2. "
    "Vote Now dested Vote Now analog leftover Kurten. "
    "Combat Readiness True dested Combat Readiness / Full Scale Alert True analog leftover Brist. "
    "Military Support dested Motion Supported analog leftover Li. "
    "Our little secret is legal dested Our Blockade Is Perfectly Legal analog leftover Li. "
    "Accepting their control dested Accepting Trade Federation Control analog leftover Li. "
    "Palest door controls dested Blast Door Controls analog leftover Li. "
    "Besieged yavin dested Baskol Yeesim analog leftover Li. "
    "left out dested Lott Dod analog leftover Li/Martin qty=3. "
    "Kessel Anger dested Passel Argente analog leftover Li. "
    "to annihilate them dested Toonbuck Toora analog leftover Li qty=2. "
    "Take your Adventure dested Yeb Yeb Adem'thorn analog leftover Li. "
    "Scrambling device dested Squabbling Delegates analog leftover Li. "
    "Something destroyers dested Edcel Bar Gane analog leftover Li. "
    "Darth Vader w/ stick dested Darth Vader With Lightsaber analog leftover Martin qty=2. "
    "Maul w/ stick dested Darth Maul With Lightsaber analog leftover Li qty=2. "
    "I'm free then dested Orn Free Taa analog leftover Li qty=2. "
    "All's Well dested Aks Moe analog leftover Li. "
    "Killers dested Tikkes analog leftover Li. "
    "Ability x3 dested Ability, Ability, Ability analog leftover Morgan. "
    "IGS LS-3 Combo dested SFS L-s9.3 Laser Cannon analog leftover Li. "
    "Boba Fett something dested Baron Soontir Fel analog leftover Li. "
    "Mighty hunter dested Mist Hunter analog leftover Li. "
    "Sniper dested Saber 1 analog leftover Li. "
    "Predated musical dested Combat Response analog leftover Martin. "
    "something docked dested Death Star: Docking Bay 327 analog leftover nats Jake Docking Bay. "
    "Why you in the war dested What Have You Done? analog leftover typical. "
    "Let them dested Let Them Make The First Move analog leftover nats Jake. "
    "Knowledge And Defense empty IN THE 60 analog leftover Li. "
    "Shield 12 Resistance analog leftover Li extra S1112. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("It Could Be Worse"),
    n("Cloud City Celebration", qty=2),
    n("Kal'Falnl C'ndros"),
    n("Pucumir Thryss"),
    n("Tantive IV", True),
    n("Kebyc", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Lando Calrissian", True, qty=2),
    n("Alternatives To Fighting", qty=3),
    n("Corran Horn", qty=2),
    n("Kessel"),
    n("Lando's Not A System, He's A Man"),
    n("Obi-Wan With Lightsaber", qty=3),
    n("Overseer", True),
    n("Projection Of A Skywalker"),
    n("Narrow Escape", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Path Of Least Resistance", qty=4),
    n("Harc Seff", True),
    n("Off The Edge"),
    n("A Jedi's Resilience", qty=2),
    n("Ghhhk"),
    n("Rebel Barrier", qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Relentless", True),
    n("Dodge", qty=2),
    n("Clash Of Sabers"),
    n("Imperial Atrocity"),
    n("Cloud City: West Gallery"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Alter"),
    n("Gentle Touch", True),
    n("Heading For The Medical Frigate"),
    n("Cloud City: North Corridor"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever", True),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("The Professor"),
    n("Wise Advice"),
    n("Yavin Sentry"),
    n("Do Or Do Not"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("Chasm"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
]
LS_ADD = []

DS_START = "Combat Readiness / Full Scale Alert"
DS_CARDS = [
    n("Black 2", True),
    n("Slave I, Symbol Of Fear", True),
    n("DS-61-2"),
    n("Limited Resources"),
    n("Jango Fett, The Assassin", True),
    n("A Dark Time For The Rebellion", qty=2),
    n("Tatooine: Desert Landing Site"),
    n("Coruscant: Galactic Senate"),
    n("Naboo"),
    n("Death Star: Docking Bay 327"),
    n("I Love You."),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Vote Now"),
    n("Combat Response"),
    n("Sense"),
    n("Control"),
    n("You Are Beaten"),
    n("What Have You Done?"),
    n("Naboo: Theed Palace Courtyard"),
    n("Combat Readiness / Full Scale Alert", True),
    n("Crush The Rebellion"),
    n("First Strike"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("Accepting Trade Federation Control"),
    n("This Is Outrageous!"),
    n("The Phantom Menace"),
    n("Blast Door Controls"),
    n("Baskol Yeesim"),
    n("Force Push"),
    n("Lott Dod", qty=3),
    n("Passel Argente"),
    n("Coruscant: Galactic Senate", True),
    n("Let Them Make The First Move"),
    n("Toonbuck Toora", qty=2),
    n("Yeb Yeb Adem'thorn"),
    n("Squabbling Delegates"),
    n("Edcel Bar Gane"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Orn Free Taa", qty=2),
    n("Aks Moe"),
    n("Tikkes"),
    n("Ability, Ability, Ability"),
    n("Senate Hovercam"),
    n("Punishing One"),
    n("Saber 1"),
    n("Mist Hunter"),
    n("SFS L-s9.3 Laser Cannon"),
    n("Zuckuss"),
    n("Baron Soontir Fel"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Prepared Defenses"),
    n("A Useless Gesture"),
    n("Do They Have A Code Clearance?"),
    n("Abyss"),
    n("Secret Plans"),
    n("Firepower"),
    n("Fanfare"),
    n("Resistance"),
]
DS_ADD = []
