#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Matt Carulli.

Source: Nationals-2014-day-1.pdf pages 17–18 (2010 form).
Name Matt Carulli / Matthew Carulli. Username quickdraw345. Dest Matt Carulli.
"""
from __future__ import annotations

PLAYER = "Matt Carulli"
USERNAME = "quickdraw345"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 17
DS_PAGE = 18
LS_SCAN = "2014 US Nationals Day 1 p17 Matt Carulli LS.png"
DS_SCAN = "2014 US Nationals Day 1 p18 Matt Carulli DS.png"
NOTE = "Handwritten 2010 Xerox. Name Matt / Matthew Carulli dested Matt Carulli."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Carulli. Username quickdraw345. Deck name Communing Players. "
    "Communing dested Communing. Master Kenobi dested Master Kenobi. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Luke Skywalker, SITF dested Luke Skywalker, Strong In The Force. "
    "Control Combo dested Control & Tunnel Vision. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Lando's Luxury Yacht dested Lady Luck. Chewie Enraged dested Chewie, Enraged. "
    "I'm With You Too dested I'm With You Too. Unique overcounts sheet-accurate "
    "(Run Luke, Run! x2, Artoo-Detoo In Red 5 x2, Leia, Rebel Princess x2, "
    "All Wings Report In & Darklighter Spin x2, Sorry About The Mess & Blaster Proficiency x4, "
    "Rebel Barrier x2, Han Solo, Courageous Smuggler x2, Luke Skywalker, Strong In The Force x2, "
    "Anakin Skywalker, Padawan Learner x2, Padme Naberrie x2, Anakin's Lightsaber x2). "
    "(V) from checkbox. "
    "NO_DEST (2014 index): A Good Friend At Your Side."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matthew Carulli. Username quickdraw345. "
    "Deck name Aurra Sing's Blaster Rifle / Battle Droid. "
    "Bring Him Before Me dested Bring Him Before Me / Take Your Father's Place. "
    "Death Star II: Throne Room dested Death Star II: Throne Room. "
    "Flagship Bridge dested Blockade Flagship: Bridge. "
    "Mandalorian Father dested Jango Fett, The Assassin. "
    "Aurra Sing's Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Sith Probe Droid dested Sith Probe Droid. K+D dested Knowledge And Defense. "
    "Unique overcounts sheet-accurate (Aurra Sing's Blaster Rifle x11, "
    "We Must Accelerate Our Plans x3, Sonic Bombardment x3, Count Dooku x2, "
    "Darth Maul With Lightsaber x2, Sith Probe Droid x2, "
    "Ghhhk & Those Rebels Won't Escape Us x2). (V) from checkbox. "
    "Where Are You Taking This Thing dested Where Are You Taking This... Thing?. "
    "NO_DEST (2014 index): The Force Is Strong In My Family; Young Jedi & They Have Chosen A New Path."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Quick Draw", True),
    n("A Good Friend At Your Side"),
    n("Shmi Skywalker"),
    n("Tatooine: Mos Espa"),
    n("Maneuvering Flaps", True),
    n("Tatooine: Cantina", True),
    n("Run Luke, Run!", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=4),
    n("Anakin's Lightsaber"),
    n("Yoda, Great Warrior"),
    n("Rebel Barrier", qty=2),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Threepio With His Parts Showing"),
    n("Flash Of Insight", True),
    n("Anakin's Lightsaber"),
    n("Luke Skywalker, Jedi Knight"),
    n("Jedi Levitation", True),
    n("Houjix"),
    n("Draw Their Fire"),
    n("Control & Tunnel Vision"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Seeking An Audience", True),
    n("Dark Approach", True),
    n("Corran Horn"),
    n("Disarmed"),
    n("Chewie, Enraged", True),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Nabrun Leids"),
    n("Escape Pod", True),
    n("Padme Naberrie", True, qty=2),
    n("Han's Heavy Blaster Pistol", True),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Luke's Bionic Hand"),
    n("I'm With You Too", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Aim High"),
    n("Jabba's Prize", True),
    n("Do, Or Do Not"),
]


DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Knowledge And Defense", True),
    n("Death Star II: Throne Room"),
    n("I Have You Now"),
    n("Your Destiny"),
    n("Prepared Defenses"),
    n("Drop", True),
    n("Ni Chuba Na??", True),
    n("The Force Is Strong In My Family"),
    n("Counter Assault"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Blast Door Controls"),
    n("Where Are You Taking This... Thing?"),
    n("Emperor's Power"),
    n("Darth Sidious"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Aurra Sing's Blaster Rifle", qty=11),
    n("We Must Accelerate Our Plans", qty=3),
    n("Jango Fett, The Assassin"),
    n("Force Lightning", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Young Jedi & They Have Chosen A New Path"),
    n("Sith Probe Droid", True, qty=2),
    n("Blockade Flagship: Hallway"),
    n("Sonic Bombardment", True, qty=3),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Count Dooku", qty=2),
    n("Abyssin Ornament", True),
    n("Dengar With Blaster Carbine", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Mara Jade, The Emperor's Hand"),
    n("Force Pike"),
    n("Aurra Sing, Deadly Assassin"),
    n("Emperor Palpatine"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Force Push", True),
    n("Darth Vader With Lightsaber", qty=2),
    n("Mara Jade With Lightsaber"),
]
DS_SHIELDS = [
    n("Imperial Detention"),
    n("Firepower", True),
    n("Abyss", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
]
