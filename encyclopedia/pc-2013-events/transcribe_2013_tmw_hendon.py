#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Robbie Hendon Xerox Senate."""
from __future__ import annotations

PLAYER = "Robbie Hendon"
USERNAME = "/hendon"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2013 Texas Mini Worlds Day 1 p05 Robbie Hendon LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p06 Robbie Hendon DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Robbie Hendon. Username /hendon. "
    "LIGHT. Event TMW 2013. Deck Name blank. "
    "Please My Case dested Plead My Case To The Senate / Sanity And Compassion. "
    "Cor Senate dested Coruscant: Galactic Senate. "
    "Cor Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Luke w/ Lightsaber dested Luke With Lightsaber. "
    "Qui-Gon w/ Lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Obi w/ Lightsaber dested Obi-Wan With Lightsaber. "
    "Were You Looking For Me dested Were You Looking For Me?. "
    "Threepio w/ Parts Showing dested Threepio With His Parts Showing. "
    "Horox Ryder dested Horox Ryyder. "
    "Lwana Merian dested Liana Merian. "
    "Yarna dested Yarna d'al' Gargan. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Unique overcounts sheet-accurate: Horox Ryyder x3, Senator Palpatine x3, "
    "Might Of The Republic x3, Queen Amidala, Ruler Of Naboo x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Robbie Hendon. Username /hendon "
    "(Dark box reads rhendon). DARK. Event TMW 2013. Deck Name blank. "
    "My Lord, Is That Legal dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Cor Senate dested Coruscant: Galactic Senate. "
    "This Is Outrageous dested This Is Outrageous!. "
    "Yeb Yeb dested Yeb Yeb Adem'thorn. "
    "Baskol dested Baskol Yeesrim. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Tat Desert Landing Site dested Tatooine: Desert Landing Site. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Knowledge & Defence dested Knowledge And Defense. "
    "Unique overcounts sheet-accurate: Darth Maul With Lightsaber x3, "
    "Lott Dod x3, Orn Free Taa x2, Toonbuck Toora x2, Senate Hovercam x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Draw Their Fire"),
    n("Wokling", True),
    n("Corran Horn"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Inconsequential Barriers"),
    n("Clash Of Sabers"),
    n("All Wings Report In & Darklighter Spin"),
    n("Life Debt"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Imperial Atrocity", True),
    n("Leia's Blaster Rifle"),
    n("Bacta Tank"),
    n("Sense", qty=2),
    n("Alter", True),
    n("Luke With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Were You Looking For Me?"),
    n("Threepio With His Parts Showing"),
    n("Horox Ryyder", qty=3),
    n("Queen Amidala, Ruler Of Naboo", qty=2),
    n("Senator Palpatine", qty=3),
    n("Senator Mon Mothma", True),
    n("Liana Merian"),
    n("Yarna d'al' Gargan"),
    n("Ascertaining The Truth"),
    n("Plea To The Court"),
    n("The Gravest Of Circumstances"),
    n("Senate Hovercam"),
    n("Might Of The Republic", qty=3),
    n("I Will Not Defer"),
    n("Senator Jar Jar Binks", True),
    n("Princess Leia", True),
    n("Jedi Levitation", True, qty=2),
    n("Nar Shaddaa", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Lady Luck", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("There Is Another", True),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Aim High"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well"),
]
LS_ADD = [
    n("Let's Keep A Little Optimism Here"),
    n("Battle Plan"),
    n("He Can Go About His Business"),
]


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Surface Defense", True),
    n("Vader's Personal Shuttle", True),
    n("Black 2", True),
    n("Hound's Tooth", True),
    n("Punishing One", True),
    n("Mist Hunter", True),
    n("Combat Response", True, qty=2),
    n("Zuckuss", True),
    n("Bossk", True),
    n("Dengar", True),
    n("Darth Vader", True),
    n("Squabbling Delegates", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Maul Strikes"),
    n("Limited Resources"),
    n("Edcel Bar Gane"),
    n("The Phantom Menace"),
    n("Tikkes"),
    n("I Have You Now"),
    n("Baron Soontir Fel"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Lott Dod", qty=3),
    n("Aks Moe"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Naboo"),
    n("DS-61-2"),
    n("Saber 1"),
    n("Tatooine: Desert Landing Site"),
    n("First Strike"),
    n("Blast Door Controls"),
    n("Senate Hovercam", qty=2),
    n("Passel Argente"),
    n("Yeb Yeb Adem'thorn"),
    n("Orn Free Taa", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Baskol Yeesrim"),
    n("Blockade Flagship: Bridge"),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous!"),
    n("Accepting Trade Federation Control"),
    n("Slave I, Symbol Of Fear", True),
    n("Sonic Bombardment", True, qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Cloud City: Security Tower", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever"),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Abyss", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = [
    n("Imperial Detention", True),
    n("Death Star Sentry", True),
    n("There Is No Try"),
]
