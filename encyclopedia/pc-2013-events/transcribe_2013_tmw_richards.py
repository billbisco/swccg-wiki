#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Mike Richards LS typed GEMP printout + DS typed 2010 form."""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 12
DS_PAGE = 11
LS_SCAN = "2013 Texas Mini Worlds Day 1 p12 Mike Richards LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p11 Mike Richards DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 Texas Mini Worlds Day 1 p13 Mike Richards LS.png",
        "Page 13 of [[:File:2013 Texas Mini Worlds Day 1.pdf]].",
    )
]
LS_NOTE = "Typed GEMP printout (not a handwritten Xerox form). Page 13 continues the starting cards. The printout totals 59 cards in the Reserve Deck."
DS_NOTE = "Typed 2010 Xerox Print Form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Cloud City: Guest Quarters"),
    n("Bespin"),
    n("Anger, Fear, Aggression", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Chasm Walkway"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Rebel Barrier"),
    n("Punch It!", qty=2),
    n("Path Of Least Resistance", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Into The Ventilation Shaft, Lefty", qty=3),
    n("Houjix"),
    n("Fall Of The Legend", qty=3),
    n("Escape Pod", True),
    n("Choke", qty=2),
    n("Blast The Door, Kid!"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Weather Vane", True),
    n("Imperial Atrocity", True),
    n("Spiral", qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Lady Luck"),
    n("Overseer"),
    n("Outrider"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Pucumir Thryss", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Cloud City Celebration", qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Kebyc", True),
    n("Harc Seff", True),
    n("Lobot", True),
    n("Dash Rendar", True, qty=2),
    n("Artoo, Brave Little Droid"),
    n("Keeping The Empire Out Forever"),
    n("Wokling", True),
    n("Beldon's Eye", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Heading For The Medical Frigate"),
]
LS_ADD = []


DS_START = "Kessel: Spice Mines Administration Office"
DS_CARDS = [
    n("Kessel: Spice Mines Administration Office"),
    n("Combat Response"),
    n("I'm Sorry", True),
    n("Obsidian 10", True),
    n("OS-72-10"),
    n("I'll Take Them Myself"),
    n("According To My Design"),
    n("Spice Mine Operations"),
    n("DS-61-3"),
    n("Something Special Planned For Them", True),
    n("Black 2", True),
    n("Darth Maul With Lightsaber"),
    n("Force Field", True),
    n("All Power To Weapons", qty=4),
    n("Mara Jade With Lightsaber"),
    n("Atmospheric Assault", True, qty=2),
    n("Tibanna Floating Refinery"),
    n("U-3PO"),
    n("Baron Soontir Fel"),
    n("You Are Beaten"),
    n("Knowledge And Defense", True),
    n("Storm Clouds"),
    n("DS-61-5"),
    n("Imperial Propaganda", True),
    n("Black 5"),
    n("Force Lightning"),
    n("Juno Eclipse, Black Leader"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Black 1"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Where Are You Taking This Thing?"),
    n("Dark Maneuvers & Tallon Roll", qty=3),
    n("Clouds"),
    n("Masterful Move & Endor Celebration"),
    n("Emperor Palpatine"),
    n("Spice Mine Administrator"),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Kessel Surveillance System"),
    n("Darth Maul With Lightsaber"),
    n("Arica"),
    n("Saber 1"),
    n("Ghhhk"),
    n("Black 3", True),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Kessel"),
    n("DS-61-2"),
    n("Kessel: Spice Mines Extraction Facility"),
    n("Darth Vader With Lightsaber"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Resistance"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
]
DS_ADD = [
    n("Imperial Detention"),
    n("Firepower", True),
    n("Leave Them To Me", True),
]
