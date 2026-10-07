#!/usr/bin/env python3
"""2013 World Championship Day 2 typed Print Form: Seth Acree Dark."""
from __future__ import annotations

PLAYER = "Seth Acree"
USERNAME = "sjacree"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2013 Worlds Day 2 p02 Seth Acree LS.png"
DS_SCAN = "2013 Worlds Day 2 p01 Seth Acree DS.png"
NOTE = "Typed 2013 Xerox Print Form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World"),
    n("Coruscant: Main Power Plant"),
    n("Coruscant: Lower Levels"),
    n("Planetary Shield"),
    n("Rogue Insertion"),
    n("Heading For The Medical Frigate"),
    n("Declaration Of Rebellion"),
    n("Rogue Squadron Tactics"),
    n("Bacta Infirmary"),
    n("Dressel"),
    n("Coruscant: Jedi Council Chamber"),
    n("Commander Wedge Antilles", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Derek 'Hobbie' Klivian", True),
    n("Zev Senesca"),
    n("Commander Narra"),
    n("Biggs, Rogue Legend"),
    n("Wes Janson, Veteran Rogue"),
    n("Commander Luke Skywalker", True),
    n("Tycho Celchu", True),
    n("Dack Ralter", True),
    n("Ten Numb", True),
    n("Kier Santage"),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Veteran Rogue", qty=2),
    n("Senator Leia Organa"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Alderaan Consular Ship"),
    n("Obi-Wan In Radiant VII"),
    n("Artoo-Detoo In Red 5"),
    n("Red 6"),
    n("Lady Luck"),
    n("Spiral"),
    n("Rogue 1"),
    n("Disruptor Pistol"),
    n("We Wish To Board At Once"),
    n("Strikeforce", True),
    n("Yub Yub, Commander", qty=5),
    n("Nabrun Leids"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Desperate Reach", True),
    n("Speak With The Jedi Council"),
    n("Houjix & Out Of Nowhere"),
    n("Blast The Door, Kid!", qty=2),
    n("Civil Disorder", True),
    n("Field Dressing"),
    n("Menace Fades"),
    n("Echo Base Garrison"),
    n("Imperial Atrocity", True),
    n("Commando Training & K'lor'slug"),
    n("Coruscant Celebration"),
    n("Coruscant", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Ounee Ta", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry"),
    n("The Professor"),
    n("Affect Mind"),
    n("Weapons Display"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("According To My Design"),
    n("The Emperor", True),
    n("Combat Response"),
    n("Jabba's Haven"),
    n("Endor Shield", True),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("Darth Vader", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Maarek Stele, The Emperor's Reach"),
    n("Zuckuss"),
    n("Janus Greejatus"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("U-3PO"),
    n("Arica"),
    n("Dengar With Blaster Carbine", True),
    n("Garindan", True, qty=2),
    n("Slave One, Symbol Of Fear"),
    n("Victory"),
    n("Vader's Personal Shuttle", True),
    n("Maul's Sith Infiltrator"),
    n("Mist Hunter", True),
    n("Blizzard 4", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Sense", qty=3),
    n("Short Range Fighters & Watch Your Back", qty=3),
    n("Look Sir, Droids", True),
    n("Imperial Decree", True),
    n("Special Delivery", True),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Image Of The Dark Lord", True),
    n("Establish Secret Base", True),
    n("Ominous Rumors"),
    n("Black Sun Fleet", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower"),
    n("Imperial Detention"),
    n("Leave Them To Me", True),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Death Star Sentry"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
