#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: Robbie Hendon.

Source: 2012TMWDay2.pdf pages 11–12 (typed slang printout, not a handwritten
Xerox form). Name Robbie Hendon dested Robbie Hendon analog leftover Day 1
CANON / player-stubs/Robbie_Hendon.wiki. Username blank.
p11 Light Watch Your Step. p12 Dark My Lord, Is That Legal?.
Do not dest as a new person.
Do not dest Day 1 TMW / 2013 TMW Hendon 60s again.
"""
from __future__ import annotations

PLAYER = "Robbie Hendon"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2012 Texas Mini Worlds Day 2 Robbie Hendon LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 Robbie Hendon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout p11 Light / p12 Dark (not a handwritten Xerox form). "
    "Name Robbie Hendon dested Robbie Hendon analog leftover Day 1 CANON. "
    "Username blank. Event TMW Day 2. "
    "Do not dest as a new person. Do not dest Day 1 TMW / 2013 TMW Hendon 60s again."
)
LS_NOTE = (
    "Typed slang printout p11 Light. Name Robbie Hendon dested Robbie Hendon. Username blank. "
    "Watch Your Step empty dested analog leftover Gardner. "
    "BoShek's Modified Light Freighter dested BoShek's Modified Freighter analog leftover Shaw. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Hendon. "
    "Rayc Ryjerd dested analog leftover. "
    "Fallen Portal dested Falling Portal analog leftover Dalton qty=2. "
    "Control/Tunnel Vision dested Control & Tunnel Vision analog leftover qty=2. "
    "It's a Hit dested It's A Hit! analog leftover Nelson. "
    "Antilles Maneuver/Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements analog leftover. "
    "Strikeforce dested Strike Force analog leftover Hendon True. "
    "Legendary Starfighter crossed dest Tatooine: Mos Espa Docking Bay analog leftover Atkin. "
    "Corellian Retort V crossed dest Houjix & Out Of Nowhere analog leftover Lingrell. "
    "Hear Me Baby, Hold Together V crossed without replacement dest skip. "
    "All Wings Report In/Darklighter Spin dested All Wings Report In & Darklighter Spin analog leftover qty=2. "
    "Palace Raider dested Palace Raider analog leftover Molitor qty=6. "
    "Honor of the Jedi dested Honor Of The Jedi analog leftover Hendon. "
    "Tat: Docking Bay 94 dested Tatooine: Docking Bay 94 analog leftover. "
    "Tat: Cantina dested Tatooine: Cantina analog leftover Hendon. "
    "Insurrection/Aim High dested Insurrection & Aim High analog leftover Shaw. "
    "Anger Fear Aggression dested Anger, Fear, Aggression analog leftover Barnes IN THE 60. "
    "Shield Weapon's Display dested Weapons Display analog leftover Hendon True. "
    "Shield Yavin Sentry dested Massassi Base Sentry analog leftover Shaw True. "
    "Unique 59 sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Typed slang printout p12 Dark. Name Robbie Hendon dested Robbie Hendon. Username blank. "
    "My Lord is That Legal/I Will Make It Legal dested My Lord, Is That Legal? / I Will Make It Legal analog leftover 2013 TMW Hendon. "
    "Cor: Galactic Senate dested Coruscant: Galactic Senate analog leftover 2013 TMW Hendon. "
    "Darth Maul w/Saber dested Darth Maul With Lightsaber analog leftover 2013 TMW Hendon qty=3. "
    "Short Range Fighters/Watch Your Back dested Short Range Fighters & Watch Your Back analog leftover Bali qty=2. "
    "SFS Ls93 Laser Cannons dested SFS L-s9.3 Laser Cannons analog leftover 2013 TMW Hendon. "
    "Lott Dodd dested Lott Dod analog leftover Dalton qty=3. "
    "Yeb Yeb dested Yeb Yeb Adem'thorn analog leftover 2013 TMW Hendon. "
    "DS 61-2 dested DS-61-2 analog leftover 2013 TMW Hendon. "
    "This is Outrageous dested This Is Outrageous! analog leftover 2013 TMW Hendon. "
    "Our Blockade is Perfectly Legal dested Our Blockade Is Perfectly Legal analog leftover 2013 TMW Hendon. "
    "Knowledge and Defense dested Knowledge And Defense analog leftover Hendon True IN THE 60. "
    "Shield We'll Let Fate a Decide, Huh dested We'll Let Fate-a Decide, Huh? analog leftover 2013 TMW Hendon True. "
    "Shield Do They Have a Code Clearance dested Do They Have A Code Clearance? analog leftover Hendon True. "
    "Shield After Her dested After Her! analog leftover Chu True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step"),
    n("Pulsar Skate"),
    n("BoShek, Brash Smuggler"),
    n("BoShek's Modified Freighter"),
    n("X-Wing Laser Cannon"),
    n("Han Solo, Courageous Smuggler"),
    n("Millennium Falcon"),
    n("Luke Skywalker", True),
    n("Artoo-Detoo In Red 5"),
    n("Tatooine Celebration", qty=2),
    n("Dash Rendar"),
    n("Rayc Ryjerd", True),
    n("I'll Take The Leader", qty=2),
    n("Patrol Craft", qty=5),
    n("Outrider"),
    n("Falling Portal", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Rebel Barrier"),
    n("It's A Hit!"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("On The Edge"),
    n("It Could Be Worse"),
    n("Kessel"),
    n("Bacta Tank"),
    n("Menace Fades"),
    n("Hindsight", True),
    n("Strike Force", True),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Houjix & Out Of Nowhere"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Palace Raider", qty=6),
    n("Melas", True),
    n("Imperial Atrocity", True),
    n("Flash Of Insight", True),
    n("Honor Of The Jedi"),
    n("Mirax Terrik"),
    n("Tatooine: Docking Bay 94"),
    n("Spaceport Docking Bay"),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Squadron Assignments"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Ounee Ta", True),
    n("Another Pathetic Lifeform", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Massassi Base Sentry", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Naboo: Theed Palace Generator Core"),
    n("Punishing One", True),
    n("Vader's Personal Shuttle", True),
    n("Hound's Tooth", True),
    n("Combat Response", True, qty=2),
    n("Surface Defense", True),
    n("Zuckuss", True),
    n("Dengar", True),
    n("Darth Vader", True),
    n("Bossk", True),
    n("Black 2", True),
    n("Mist Hunter", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("We Must Accelerate Our Plans", qty=2),
    n("I Have You Now"),
    n("Limited Resources"),
    n("Saber 1"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("SFS L-s9.3 Laser Cannons"),
    n("Lott Dod", qty=3),
    n("Orn Free Taa", qty=3),
    n("Toonbuck Toora", qty=2),
    n("Baskol Yeesrim", qty=1),
    n("Edcel Bar Gane"),
    n("Passel Argente"),
    n("Tikkes"),
    n("Yeb Yeb Adem'thorn"),
    n("Aks Moe"),
    n("Senate Hovercam", qty=2),
    n("DS-61-2"),
    n("Baron Soontir Fel"),
    n("Squabbling Delegates", qty=3),
    n("Naboo"),
    n("Blockade Flagship: Bridge"),
    n("Maul Strikes"),
    n("The Phantom Menace"),
    n("First Strike"),
    n("Blast Door Controls"),
    n("This Is Outrageous!"),
    n("Accepting Trade Federation Control"),
    n("Our Blockade Is Perfectly Legal"),
    n("Motion Supported"),
    n("Cold Feet", True),
    n("Something Special Planned For Them", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("After Her!", True),
]
DS_ADD = []
