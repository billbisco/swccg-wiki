#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Patrick Ziagos.

Source: 2012mpcday1.pdf pages 149–150 typed GEMP dumps.
Name PATRICK ZIAGOS / ZIAGOS dested Patrick Ziagos as written.
Username blank. Analog generate empty.
p149 Light Profit. p150 Dark Bring Him Before Me.
Pack player-stubs/Patrick_Ziagos.wiki (is_bio False).
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Patrick Ziagos"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 149
DS_PAGE = 150
LS_SCAN = "2012 Match Play Championship Day 1 Patrick Ziagos LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Patrick Ziagos DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "p149 typed GEMP dump Light Profit. p150 typed GEMP dump Dark Bring Him Before Me. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Name PATRICK ZIAGOS dested Patrick Ziagos as written. "
    "Username blank. Analog generate empty. LIGHT dested from the dump. "
    "Do not dest as a new person. "
    "You Can Either Profit By This.../Or Be Destroyed dested "
    "You Can Either Profit By This... / Or Be Destroyed analog leftover. "
    "AFA True dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "Gift Of The Mentor dested as written analog leftover. "
    "Padme Naberrie True dested Padmé Naberrie True analog leftover. "
    "R2-D2 (Artoo-Detoo) dested R2-D2 analog leftover. "
    "Sense & Recoil In Fear dested analog leftover. "
    "Goo Nee Tay dested analog leftover. "
    "I Must Be Allowed To Speak True dested IN THE 60 analog leftover. "
    "Seeking An Audience True dested IN THE 60 analog leftover. "
    "Quick Draw True dested IN THE 60 analog leftover. "
    "Heading For The Medical Frigate dested IN THE 60 analog leftover. "
    "Luke Skywalker, Strong In The Force x3 sheet-accurate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump. Name ZIAGOS dested Patrick Ziagos as written. "
    "Username blank. DARK dested from the dump. "
    "Do not dest as a new person. "
    "Bring Him Before Me/Take Your Father's Place dested "
    "Bring Him Before Me / Take Your Father's Place analog leftover. "
    "K&D True dested Knowledge And Defense True analog leftover IN THE 60. "
    "I Find Your Lack Of Faith Disturbing True dested IN THE 60 analog leftover. "
    "Weapon Of A Sith dested IN THE 60 analog leftover. "
    "Gift Of The Master dested IN THE 60 analog leftover. "
    "I've Lost Artoo True dested I've Lost Artoo! True analog leftover. "
    "Drop True dested Drop! True analog leftover. "
    "Prepared Defenses dested IN THE 60 analog leftover. "
    "Look Sir, Droids True dested analog leftover. "
    "Galen, Secret Apprentice dested as written analog leftover. "
    "Darth Maul (AI) dested Darth Maul analog leftover. "
    "Darth Sidious (AI) dested Darth Sidious analog leftover. "
    "The Phantom Menace (AI) dested The Phantom Menace analog leftover. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover. "
    "Imperial Propaganda empty x2 and True x4 kept separate analog leftover. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Let The Wookiee Win", True),
    n("Narrow Escape"),
    n("Out Of Commission", qty=4),
    n("Under Attack"),
    n("Rebel Barrier", qty=2),
    n("How Did We Get Into This Mess?", qty=5),
    n("Too Close For Comfort"),
    n("Clash Of Sabers"),
    n("Gift Of The Mentor"),
    n("Blaster Deflection"),
    n("Weapon Levitation"),
    n("Nabrun Leids", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Sense & Recoil In Fear", qty=4),
    n("Sai'torr Kal Fas", True),
    n("Goo Nee Tay"),
    n("Tatooine: Mos Eisley"),
    n("Tatooine: Cantina"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Dagobah: Yoda's Hut"),
    n("Obi-Wan's Journal"),
    n("Leia's Blaster Rifle"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Padmé Naberrie", True),
    n("Lando With Vibro-Ax"),
    n("Chewbacca, Protector"),
    n("Ben Kenobi", qty=3),
    n("Leia, Rebel Princess", qty=2),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Threepio With His Parts Showing"),
    n("R2-D2"),
    n("I Must Be Allowed To Speak", True),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate"),
    n("Han With Heavy Blaster Pistol"),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Aim High"),
    n("The Professor", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Restraining Bolt"),
    n("Trophy Of A Kill"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
    n("Knowledge And Defense", True),
    n("Breached Defenses & Molator"),
    n("Gift Of The Master"),
    n("I've Lost Artoo!", True),
    n("Drop!", True),
    n("Prepared Defenses"),
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Death Star II: Throne Room"),
    n("Force Field", True),
    n("Sense"),
    n("Outflank", True, qty=2),
    n("Force Lightning"),
    n("You Overestimate Their Chances"),
    n("Operational As Planned", True),
    n("Look Sir, Droids", True),
    n("Imperial Barrier"),
    n("None Shall Pass", True, qty=2),
    n("Maul's Sith Infiltrator", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Bane Malar", True),
    n("Darth Maul With Lightsaber"),
    n("Darth Maul"),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader, Betrayer Of The Jedi", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Darth Sidious"),
    n("IT-O (Eytee-Oh)", True),
    n("Sith Probe Droid", True, qty=2),
    n("A Sith's Plans"),
    n("Emperor's Power"),
    n("Protocol Failure"),
    n("Imperial Propaganda", qty=2),
    n("The Phantom Menace"),
    n("Security Precautions"),
    n("After Her!"),
    n("Imperial Propaganda", True, qty=4),
    n("Blaster Rack", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Jabba's Palace: Lower Passages"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Insignificant Rebellion"),
    n("Your Destiny"),
]
DS_ADD = []
