#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Aaron Kinser Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Aaron Kinser"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 49
DS_PAGE = 50
LS_SCAN = "2013 Match Play Championship p49 Aaron Kinser LS.png"
DS_SCAN = "2013 Match Play Championship p50 Aaron Kinser DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Aaron Kinser. Light. Deck title Icy Stars. "
    "Local Uprising dested Local Uprising / Liberation. "
    "Maneuvering Flaps + Nick Of Time dested Maneuvering Flaps & Nick Of Time. "
    "Wedge Antilles RS dested Wedge Antilles, Red Squadron Leader. "
    "Hoth MPG dested Hoth: Main Power Generators. "
    "Hoth Echo Base Garrison dested Echo Base Garrison. "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter. "
    "Hoth Snow Trench dested Hoth: Snow Trench. "
    "Hoth North Ridge dested Hoth: North Ridge. "
    "I'll take the Leader dested I'll Take The Leader. "
    "Line 25 started Commander Luke, struck, ditto of Escape Pod. "
    "Wrist Comlink as written. Jek Porkins dested Jek Porkins. "
    "Rycar Ryjerd dested Rycar Ryjerd. "
    "Get To Your Ships dested Get To Your Ships!. "
    "All Wings Report In + Darklighter dested All Wings Report In & Darklighter Spin. "
    "Snow Speeder Garrison dested Snowspeeder Garrison. "
    "Derek \"Hobbie\" Klivian dested Derek 'Hobbie' Klivian. "
    "Red 6 dested Red 6. Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. "
    "Han Chewie + Falcon dested Han, Chewie, And The Falcon. "
    "X-wing Laser Cannon as written. That's One dested That's One. "
    "Rebel Laser Cannon dested Dual Laser Cannon. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Simple Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "Do or do not dested Do, Or Do Not. "
    "Don't do that again dested Don't Do That Again. "
    "Form left column reprints 37–38 on lines 39–40 are I'll Take The Leader and Ice Storm. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Aaron Kinser. Dark. Deck title Chris Twigg Style. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control. "
    "Veers dested Veers. Cyclone Walker dested Cyclone Walker. "
    "We're in Attack Position dested We're In Attack Position Now. "
    "Image of a dark lord dested Image Of The Dark Lord. "
    "U3PO dested U-3PO (Yoo-Threepio). "
    "The Mandalorian, Father Fett dested Jango Fett, The Assassin. "
    "AT-AT Deployment Platform dested AT-AT Deployment Platform. "
    "Imbalance + Kintan Strider dested Imbalance & Kintan Strider. "
    "Imperial Arrest dested Imperial Arrest Order. "
    "The Emperor's Power dested Emperor's Power. "
    "General Nevar dested General Nevar. "
    "Sith Fury + End This Destructive Conflict dested Sith Fury & End This Destructive Conflict. "
    "Masterful Move + Endor Occup dested Masterful Move & Endor Occupation. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Hoth Blockade dested Hoth Blockade. "
    "Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter. "
    "Black 2 dested Black 2. "
    "Hoth Ice Plains dested Hoth: Ice Plains. "
    "Hoth Mountains dested Hoth: Mountains. "
    "Hoth Main Power Generator dested Hoth: Main Power Generators. "
    "Fleet Security Protocols dested Fleet Security Protocols. "
    "Imperial Decree dested Imperial Decree. "
    "You May Start Your Landing dested You May Start Your Landing. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Reactor Terminal dested Reactor Terminal. "
    "A useless gesture dested A Useless Gesture. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "There is no try dested There Is No Try. "
    "Firepower (V) written in the name; checkbox empty. "
    "Oppressive Enforcement dested Oppressive Enforcement. "
    "Form left column reprints 37–38 on lines 39–40 are Commander Igar and Target The Main Generator. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Echo Base Garrison"),
    n("Maneuvering Flaps & Nick Of Time", True),
    n("Veteran Rogue", True),
    n("Organized Attack", qty=3),
    n("T-47 Battle Formation"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Rogue 1"),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Projection Of A Skywalker", qty=2),
    n("Hoth: Main Power Generators", True),
    n("Echo Base Garrison"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth"),
    n("Hoth: Snow Trench"),
    n("Hoth: North Ridge"),
    n("Haven"),
    n("I'll Take The Leader"),
    n("Escape Pod", True, qty=2),
    n("Commander Luke Skywalker", True, qty=2),
    n("I'm With You Too", True),
    n("Wrist Comlink"),
    n("Jek Porkins", True),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Get To Your Ships!"),
    n("Menace Fades", True),
    n("Heading For The Medical Frigate"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Snowspeeder Garrison"),
    n("I'll Take The Leader"),
    n("Ice Storm"),
    n("Imperial Atrocity", True),
    n("Dash Rendar", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Commander Wedge Antilles", True),
    n("Frostbite", True, qty=2),
    n("Zev Senesca"),
    n("Red 6", True),
    n("Rebel Leadership", True),
    n("We're Doomed"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Gold Leader In Gold 1", True),
    n("Han, Chewie, And The Falcon"),
    n("X-wing Laser Cannon"),
    n("We Wish To Board At Once"),
    n("That's One"),
    n("Dual Laser Cannon", True),
    n("Lando Calrissian, Scoundrel"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("Chasm", True),
    n("Battle Plan", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Veers", True),
    n("Cyclone Walker", True, qty=3),
    n("We're In Attack Position Now"),
    n("Image Of The Dark Lord"),
    n("U-3PO (Yoo-Threepio)"),
    n("Admiral Motti", True),
    n("Control"),
    n("Jango Fett, The Assassin"),
    n("A Dark Time For The Rebellion"),
    n("AT-AT Cannon", True),
    n("AT-AT Deployment Platform", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("Blizzard Scout 1", True),
    n("Grand Admiral Thrawn"),
    n("Imbalance & Kintan Strider", True),
    n("Trample"),
    n("Sonic Bombardment", True),
    n("Garindan", True),
    n("Imperial Arrest Order"),
    n("Conquest", True),
    n("Emperor's Power", True),
    n("General Nevar", True),
    n("Sith Fury & End This Destructive Conflict"),
    n("Do They Have A Code Clearance?"),
    n("Masterful Move & Endor Occupation"),
    n("Blizzard 4"),
    n("Walker Garrison"),
    n("Admiral Piett"),
    n("Slave I, Symbol Of Fear", True),
    n("Close Call", True),
    n("Imperial Command"),
    n("Grand Moff Tarkin", True),
    n("Tempest 1"),
    n("Commander Igar"),
    n("Target The Main Generator"),
    n("Hoth Blockade", True),
    n("Boba Fett, Prepared Hunter", True),
    n("No Escape"),
    n("Imperial Command"),
    n("Hoth: Defensive Perimeter"),
    n("Victory", True),
    n("Prepared Defenses", True),
    n("Blizzard 2", True),
    n("Black 2", True),
    n("Darth Vader", True),
    n("Flagship Executor"),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Mountains"),
    n("Hoth: Main Power Generators", True),
    n("Fleet Security Protocols", True),
    n("Imperial Decree", True),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Resistance", True),
    n("Reactor Terminal", True),
    n("A Useless Gesture"),
    n("Fanfare"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
