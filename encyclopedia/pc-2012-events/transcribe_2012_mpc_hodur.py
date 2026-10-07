#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Greg Hodur.

Source: 2012mpcday1.pdf pages 83–84 (2010 form, 12 shields).
Name Greg Hodur dested Greg Hodur (analog generate empty).
p83 Light Center Of Tyranny. p84 Dark My Kind Of Scum.
Username blank. Pack player-stubs/Greg_Hodur.wiki.
"""
from __future__ import annotations

PLAYER = "Greg Hodur"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 83
DS_PAGE = 84
LS_SCAN = "2012 Match Play Championship Day 1 Greg Hodur LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Greg Hodur DS.png"
LS_DECK_NAME = "Loopty Loop"
DS_DECK_NAME = "Ghetto Scum"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Hodur dested Greg Hodur. "
    "Username blank. LIGHT checked. Deck Name Loopty Loop. "
    "Event Date 02/11/12 Event Name 2012 MPC. Analog generate empty. "
    "Center of Tyranny / A Liberated world dested Center Of Tyranny / A Liberated World True. "
    "Wedge Antilles, red squadron leader (BDW) dested Wedge Antilles, Red Squadron Leader. "
    "Commando training & K'lor'slug dested Commando Training & K'lor'slug True. "
    "Strike force dested Strikeforce True. "
    "To close for comfort dested Too Close For Comfort. "
    "Han, Chewie and the falcon dested Han, Chewie, And The Falcon. "
    "Artoo detoo in red 5 dested Artoo-Detoo In Red 5. "
    "Keir santange dested Kier Santage. "
    "Derek \"hobbie\" kilvian dested Derek 'Hobbie' Klivian True. "
    "Yub Yub commander dested Yub Yub, Commander True x4. "
    "Luke Skywalker, rebel hero dested Luke Skywalker, Rebel Hero True x3. "
    "Shield 12 remnant dested Yavin Sentry. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Hodur dested Greg Hodur. "
    "Username blank. DARK checked. Deck Name Ghetto Scum. "
    "Event Date 02/11/12 Event Name 2012 MPC. Analog generate empty. "
    "MY KIND OF SCUM / FEARLESS AND INVENTIVE dested My Kind Of Scum / Fearless And Inventive. "
    "Gailid dested Gailid. T'doshok hunting vow dested T'doshok Hunting Vow True. "
    "Bossk in hounds tooth dested Bossk In Hound's Tooth. "
    "Why didnt you tell me dested Why Didn't You Tell Me? True. "
    "Skrilling dested Skrilling x10 sheet-accurate. "
    "We must accelerate our plans dested We Must Accelerate Our Plans x3. "
    "Fire power dested Firepower True. "
    "Come here you big coward dested Come Here You Big Coward True. "
    "Shield 12 remnant dested Oppressive Enforcement. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World", True),
    n("Heading For The Medical Frigate"),
    n("Coruscant", True),
    n("Coruscant: Lower Levels", True),
    n("Coruscant: Main Power Plant", True),
    n("Planetary Shield", True),
    n("Bacta Infirmary", True),
    n("Rogue Insertion", True),
    n("Rogue Squadron Tactics", True),
    n("Declaration Of Rebellion", True),
    n("Alderaan Consular Ship", True),
    n("Luke's Blaster Pistol", True),
    n("Veteran Rogue", True, qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Inconsequential Barriers", qty=2),
    n("Dash Rendar", True),
    n("Yub Yub, Commander", True, qty=4),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Honor Of The Jedi"),
    n("Commando Training & K'lor'slug", True),
    n("Commander Narra", True),
    n("Hear Me Baby, Hold Together", True),
    n("Dressel", True),
    n("Corellian Retort", True),
    n("Artoo-Detoo In Red 5"),
    n("Ten Numb", True),
    n("Imperial Atrocity", True),
    n("Senator Leia Organa", True),
    n("Strikeforce", True),
    n("Dack Ralter", True),
    n("Corran Horn"),
    n("Kier Santage"),
    n("Wes Janson, Rogue Veteran", True),
    n("Obi-Wan In Radiant VII", True),
    n("Tycho Celchu", True),
    n("Houjix"),
    n("Coruscant: Jedi Council Chamber"),
    n("Too Close For Comfort"),
    n("It Could Be Worse"),
    n("Wedge Antilles, Legendary Rogue", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Biggs, Rogue Legend", True),
    n("Menace Fades"),
    n("Coruscant Celebration"),
    n("Jedi Levitation", True),
    n("Escape Pod", True),
    n("Tantive IV", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not", True),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Another Pathetic Lifeform", True),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Yavin Sentry"),
]
LS_ADD = []

DS_START = "My Kind Of Scum / Fearless And Inventive"
DS_CARDS = [
    n("My Kind Of Scum / Fearless And Inventive"),
    n("Tatooine: Desert Heart"),
    n("Tatooine: Jabba's Palace"),
    n("Prepared Defenses"),
    n("Power Of The Hutt"),
    n("Jabba's Haven", True),
    n("T'doshok Hunting Vow", True),
    n("Blast Door Controls"),
    n("Jabba's Sail Barge", True),
    n("Jabba's Palace: Lower Passages"),
    n("Hutt Bounty", True),
    n("Zuckuss In Mist Hunter"),
    n("Pote Snitkin", qty=2),
    n("Skrilling", qty=10),
    n("None Shall Pass", True, qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("Jabba's Palace: Audience Chamber"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Imperial Barrier"),
    n("Battle Droid Squad", True, qty=2),
    n("Podracer Collision"),
    n("Gailid"),
    n("Jabba The Hutt", True),
    n("Unsalvageable"),
    n("Bossk In Hound's Tooth"),
    n("Den Of Thieves"),
    n("Chall Bekan"),
    n("Why Didn't You Tell Me?", True),
    n("IG-88 In IG-2000"),
    n("Cold Feet", True),
    n("Bib Fortuna"),
    n("Nal Hutta"),
    n("Outflank", True),
    n("First Strike"),
    n("Jabba's Space Cruiser", True),
    n("Abyssin Ornament", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Scum And Villainy"),
    n("4-LOM With Concussion Rifle"),
    n("Ephant Mon"),
    n("Molator", True),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Mara Jade With Lightsaber", True),
    n("Boelo"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate Decide, Huh?"),
    n("There Is No Try", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
