#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: light_frank.

Source: 2012mpcday1.pdf pages 151–154 typed GEMP dumps.
Filename light_frank / BHBM.txt dested light_frank as written.
Username light_frank. Analog generate empty.
p151–p152 Light Hidden Base. p153–p154 Dark Bring Him Before Me.
Pack player-stubs/light_frank.wiki (is_bio False).
Do not dest as Frank Lam / Frank Walsh / Frank Amore.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "light_frank"
USERNAME = "light_frank"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 151
DS_PAGE = 153
LS_SCAN = "2012 Match Play Championship Day 1 light_frank LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 light_frank DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "BHBM"
NOTE = (
    "p151–p152 typed GEMP dump Light Hidden Base filename light_frank. "
    "p153–p154 typed GEMP dump Dark Bring Him Before Me filename BHBM.txt. "
    "Username light_frank. Analog generate empty."
)
LS_NOTE = (
    "Typed GEMP dump pages 151–152. Filename light_frank dested light_frank "
    "as written. Username light_frank. Analog generate empty. "
    "Do not dest as Frank Lam / Frank Walsh / Frank Amore. "
    "Do not dest as a new person. "
    "Hidden Base/Systems Will Slip Through Your Fingers (V) (1 starting) dested "
    "Hidden Base / Systems Will Slip Through Your Fingers True analog leftover. "
    "(1 starting) on shields dest LS_SHIELDS. "
    "AFA True (1 starting) dested IN THE 60 analog leftover. "
    "Wokling True (1 starting) dested IN THE 60 analog leftover. "
    "Get To Your Ships! (1 starting) dested IN THE 60 analog leftover. "
    "We Didn't Hit It (1 starting) dested IN THE 60 analog leftover. "
    "Uncharted Settlements (1 starting) dested IN THE 60 analog leftover. "
    "HFTMF (1 starting) dested IN THE 60 analog leftover. "
    "LTWW True x2 dested IN THE 60 analog leftover. "
    "Padme Naberrie True dested analog leftover dump. "
    "Alderaan Consular Ship dested as written analog leftover dump. "
    "Rebel Cell sites dested as written. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump pages 153–154. Filename BHBM.txt facing light_frank dested "
    "light_frank. Username light_frank. DARK dested from the dump. "
    "Do not dest as a new person. "
    "Bring Him Before Me/Take Your Father's Place (1 starting) dested "
    "Bring Him Before Me / Take Your Father's Place analog leftover. "
    "(1 starting) on shields dest DS_SHIELDS including Weapon Of A Sith. "
    "Your Destiny (1 starting) dested IN THE 60 analog leftover dump Effect. "
    "Insignificant Rebellion (1 starting) dested IN THE 60 analog leftover. "
    "Gift Of The Master (1 starting) dested IN THE 60 analog leftover. "
    "Drop! True (1 starting) dested IN THE 60 analog leftover. "
    "K&D True (1 starting) dested IN THE 60 analog leftover Murray. "
    "Prepared Defenses (1 starting) dested IN THE 60 analog leftover. "
    "Darth Sidious (AI) x2 dested Darth Sidious analog leftover unique variant. "
    "Galen, Secret Apprentice dested as written leftover_xerox TYPE_OVERRIDE Character. "
    "Imperial Propaganda empty x2 AND True x4 kept separate analog leftover. "
    "You Overestimate Their Chances dested as written analog leftover. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("I'll Try Spinning"),
    n("Taking Them With Us", True),
    n("Yoda, Master Of The Force", qty=2),
    n("Senator Leia Organa"),
    n("Jedi Pilot", qty=3),
    n("Jerus Jannick"),
    n("Panaka, Protector Of The Queen"),
    n("Clone Pilot", qty=3),
    n("Officer Dolphe"),
    n("Ric Olie, Bravo Leader"),
    n("Padme Naberrie", True),
    n("Wokling", True),
    n("It's On Automatic Pilot!"),
    n("Get To Your Ships!"),
    n("We Didn't Hit It"),
    n("We'll Take The Long Way"),
    n("Uncharted Settlements"),
    n("Flash Of Insight", True),
    n("Hiding In The Garbage", True),
    n("Uncontrollable Fury"),
    n("Civil Disorder"),
    n("Legendary Starfighter"),
    n("Anger, Fear, Aggression", True),
    n("Control & Tunnel Vision"),
    n("Found Someone You Have", True),
    n("It's Not My Fault!", True),
    n("Firefight", True, qty=2),
    n("Are You Brain Dead?!"),
    n("Houjix & Out Of Nowhere"),
    n("All Wings Report In & Darklighter Spin", qty=4),
    n("Alter (Coruscant)", True),
    n("Diversionary Tactics", True),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Cell - Hidden Landing Site"),
    n("Rebel Cell - Situation Room"),
    n("Aquaris"),
    n("Kiffex"),
    n("Naboo"),
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Alderaan Consular Ship"),
    n("Bravo Fighter", True),
    n("Bravo 2"),
    n("Bravo 3"),
    n("Bravo 4"),
    n("Bravo 5"),
    n("Republic Starfighter", qty=3),
    n("Bravo 1"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Affect Mind", True),
]
DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bane Malar", True),
    n("Darth Sidious", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Sith Probe Droid", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("IT-O (Eytee-Oh)", True),
    n("Darth Vader, Betrayer Of The Jedi", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul With Lightsaber"),
    n("Trophy Of A Kill"),
    n("Restraining Bolt"),
    n("Blaster Rack", True),
    n("Your Destiny"),
    n("Insignificant Rebellion"),
    n("Gift Of The Master"),
    n("I've Lost Artoo!", True),
    n("The Phantom Menace"),
    n("Drop!", True),
    n("A Sith's Plans"),
    n("Emperor's Power"),
    n("Breached Defenses & Molator"),
    n("Imperial Propaganda", True, qty=4),
    n("Protocol Failure"),
    n("After Her!"),
    n("Imperial Propaganda", qty=2),
    n("Knowledge And Defense", True),
    n("You Overestimate Their Chances"),
    n("Outflank", True, qty=2),
    n("Imperial Barrier"),
    n("None Shall Pass", True, qty=2),
    n("Operational As Planned", True),
    n("Human Shield"),
    n("Weapon Levitation"),
    n("Sense & Uncertain Is The Future"),
    n("Force Lightning"),
    n("Look Sir, Droids", True),
    n("Prepared Defenses"),
    n("Tatooine: Jabba's Palace"),
    n("Death Star II: Throne Room"),
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Lower Passages"),
    n("Maul's Sith Infiltrator"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Sidious' Lightsaber"),
    n("Vader's Lightsaber"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
]
