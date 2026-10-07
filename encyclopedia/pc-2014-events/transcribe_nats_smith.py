#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Reid Smith.

Source: Nationals-2014-day-1.pdf pages 28–29 (2010 form).
Name RSmith. Username 3MW0J8. Dest Reid Smith.
"""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = "3MW0J8"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 29
DS_PAGE = 28
LS_SCAN = "2014 US Nationals Day 1 p29 Reid Smith LS.png"
DS_SCAN = "2014 US Nationals Day 1 p28 Reid Smith DS.png"
NOTE = "Handwritten 2010 Xerox. Name RSmith; username 3MW0J8 dested Reid Smith."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name RSmith. Username 3MW0J8. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "Endor: Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Don't Tread dested Don't Tread On Me. LSJK dested Luke Skywalker, Jedi Knight. "
    "Sense (Pre.) dested Sense. SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "AFA dested Anger, Fear, Aggression. Unique overcounts sheet-accurate "
    "(Let The Wookiee Win x3, Wesa Gotta Grand Army x3, A Jedi's Resilience x2, "
    "Rebel Leadership x2, Speak With The Jedi Council x2, Dark Approach x2, "
    "Obi-Wan With Lightsaber x2, Lando Calrissian, Scoundrel x2, Han With Heavy Blaster Pistol x2, "
    "Qui-Gon Jinn With Lightsaber x2, Chewie, Enraged x2, Rebel Barrier x2, "
    "Blaster Deflection x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name RSmith. Username 3MW0J8. "
    "Deck name Nature teaches beasts to know their friends. "
    "Is That Legal dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Tatooine Desert Landing Site dested Tatooine: Desert Landing Site. "
    "Slave I Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "The Mandalorian Father Of Fett dested Jango Fett, The Assassin. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Line 39 arrowed to additional dested Blast Door Controls. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "K+D dested Knowledge And Defense. Unique overcounts sheet-accurate "
    "(Guri x2, Lott Dod x3, Orn Free Taa x2, Aks Moe x3, Toonbuck Toora x2, "
    "Jango Fett, The Assassin x2, Senate Hovercam x2, Boba Fett, Prepared Hunter x2, "
    "Short Range Fighters & Watch Your Back! x2, Squabbling Delegates x3, "
    "Darth Maul With Lightsaber x3, Sonic Bombardment x3, We Must Accelerate Our Plans x3). "
    "(V) from checkbox. "
    "NO_DEST (2014 index): Yeb Yeb Maash."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Mechanical Failure"),
    n("Imperial Atrocity", True),
    n("Sense", qty=2),
    n("Home One"),
    n("Naboo: Battle Plains"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Rebel Leadership", True, qty=2),
    n("Tarfful, Wookiee Insurgent"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Dark Approach", True, qty=2),
    n("Escape Pod", True),
    n("Speak With The Jedi Council", qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Grimtaash"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Home One: War Room"),
    n("Corran Horn"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Nabrun Leids"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Chewie, Enraged", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Admiral Ackbar", True),
    n("Mace Windu, Master Of The Order"),
    n("Rebel Barrier", qty=2),
    n("Blaster Deflection", qty=2),
    n("Clash Of Sabers"),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Seeking An Audience", True),
    n("Leia, Rebel Princess"),
    n("Houjix"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor"),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
]
LS_ADD = [
    n("Ultimatum"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Tatooine: Desert Landing Site"),
    n("Prepared Defenses", True),
    n("Imperial Decree", True),
    n("Jabba's Haven", True),
    n("Ni Chuba Na??", True),
    n("Guri", qty=2),
    n("Edcel Bar Gane"),
    n("Lott Dod", qty=3),
    n("Orn Free Taa", qty=2),
    n("Aks Moe", qty=3),
    n("Toonbuck Toora", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin", qty=2),
    n("Senate Hovercam", qty=2),
    n("This Is Outrageous!"),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Tikkes"),
    n("Broken Concentration", True),
    n("Yeb Yeb Maash"),
    n("Squabbling Delegates", qty=3),
    n("Zuckuss In Mist Hunter"),
    n("Accepting Trade Federation Control"),
    n("Blast Door Controls"),
    n("Cloud City: Security Tower", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Black Sun Fleet"),
    n("Our Blockade Is Perfectly Legal"),
    n("Victory"),
    n("Nal Hutta"),
    n("Arica"),
    n("Motion Supported"),
    n("OOM-9", True),
    n("Blockade Flagship: Bridge"),
    n("Limited Resources"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Firepower", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try", True),
]
DS_ADD = [
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("Imperial Detention"),
]
