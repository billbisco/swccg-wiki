#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matt Carulli.

Source: MPC-2014-Day-1-Main-Event.pdf pages 29–30 (2013 form, 15 shields).
Username QuickDraw3457. Sheet Matthew Carulli.
"""
from __future__ import annotations

PLAYER = "Matt Carulli"
USERNAME = "QuickDraw3457"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 30
DS_PAGE = 29
LS_SCAN = "2014 Match Play Championship Day 1 Matt Carulli LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matt Carulli DS.png"
LS_DECK_NAME = "Communing Blasters"
DS_DECK_NAME = "BHBM Blasters"
NOTE = "Handwritten 2013 Xerox form. Sheet Matthew Carulli dested Matt Carulli."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Matthew Carulli dested Matt Carulli. Username "
    "QuickDraw3457. LIGHT checked. Deck Communing Blasters. Communing dested Communing. "
    "SATM & Blast Prof dested Sorry About The Mess & Blaster Proficiency. Unique "
    "overcounts sheet-accurate (Run Luke, Run! (V) x2, Sorry About The Mess & Blaster "
    "Proficiency x4, Luke Skywalker, Strong In The Force x2, All Wings Report In & "
    "Darklighter Spin x2, Anakin Skywalker, Padawan Learner x2, Leia, Rebel Princess x2, "
    "Padme Naberrie (V) x2, Rebel Barrier x2, Han Solo, Courageous Smuggler x2, "
    "Artoo-Detoo In Red 5 x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username QuickDraw3457. Deck BHBM Blasters. Bring Him Before "
    "Me dested Bring Him Before Me / Take Your Father's Place. Ice-Heart dested Ysanne "
    "Isard. The Mandalorian, Father of Fett dested Jango Fett, The Assassin. Where Are "
    "You Taking This Thing? dested Where Are You Taking This ... Thing?. Unique "
    "overcounts sheet-accurate (Aurra Sing's Blaster Rifle x12, Emperor Palpatine x2, "
    "Sonic Bombardment x3, We Must Accelerate Our Plans x3, Sith Probe Droid (V) x2, "
    "Weapon Levitation & The Empire's Back (V) x2, Darth Vader With Lightsaber x2, Darth "
    "Maul With Lightsaber x3, Maul's Sith Infiltrator x2, Mara Jade With Lightsaber x2, "
    "Jango Fett, The Assassin x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("A Good Blaster At Your Side"),
    n("Quick Draw", True),
    n("Run Luke, Run!", True, qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Leia's Blaster Rifle"),
    n("Nabrun Leids"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=4),
    n("It's A Trap!"),
    n("Dark Approach", True),
    n("Tatooine: Cantina", True),
    n("Flash Of Insight", True),
    n("Luke's Bionic Hand"),
    n("Seeking An Audience", True),
    n("Rebel Barrier", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Shmi Skywalker"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Disarmed"),
    n("Tatooine: Mos Eisley"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Desperate Reach", True),
    n("I'm With You Too", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Corran Horn"),
    n("Lady Luck"),
    n("Impressive, Most Impressive", True),
    n("Yoda, Great Warrior"),
    n("Tatooine: City Outskirts"),
    n("Padme Naberrie", True, qty=2),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Anakin's Lightsaber"),
    n("Threepio With His Parts Showing"),
    n("Luke's Lightsaber"),
    n("Sai'torr Kal Fas", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Amidala's Blaster"),
    n("Draw Their Fire"),
    n("Chewie, Enraged", True),
    n("Imperial Atrocity", True),
    n("Han's Heavy Blaster Pistol", True),
    n("Houjix & Out Of Nowhere"),
    n("Obi-Wan's Apparition", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
]
LS_ADD = []


DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Death Star II: Throne Room"),
    n("Insignificant Rebellion"),
    n("Your Destiny"),
    n("Visage Of The Emperor"),
    n("Prepared Defenses", True),
    n("An Entire Legion Of My Best Troops"),
    n("Ni Chuba Na??", True),
    n("Cloud City: Security Tower", True),
    n("Emperor Palpatine", qty=2),
    n("Aurra Sing's Blaster Rifle", qty=12),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Blockade Flagship: Bridge"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sith Probe Droid", True, qty=2),
    n("Weapon Levitation & The Empire's Back", True, qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Force Push", True),
    n("Emperor's Power"),
    n("Ysanne Isard"),
    n("Blockade Flagship: Hallway"),
    n("Blast Door Controls"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Mara Jade With Lightsaber", qty=2),
    n("Jango Fett, The Assassin", qty=2),
    n("Force Lightning"),
    n("Sith Fury", True),
    n("First Strike"),
    n("Where Are You Taking This ... Thing?"),
    n("Maul Strikes"),
    n("Aurra Sing, Deadly Assassin"),
    n("Why Didn't You Tell Me?", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("After Her!", True),
    n("Fanfare", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("A Useless Gesture", True),
]
DS_ADD = []
