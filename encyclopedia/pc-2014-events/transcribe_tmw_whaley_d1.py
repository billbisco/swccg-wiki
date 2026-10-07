#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Thomas Whaley.

Source: 2014-TMW-Day-1.pdf pages 31–32 (2010 form).
"""
from __future__ import annotations

PLAYER = "Thomas Whaley"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 31
DS_PAGE = 32
LS_SCAN = "2014 Texas Mini Worlds Day 1 p31 Thomas Whaley LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p32 Thomas Whaley DS.png"
NOTE = "Handwritten 2010 Xerox Print Form (12 shields + Additional)."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). "
    "Name Thomas Whaley. Username blank. LIGHT checked. Deck Name WTF. "
    "Republic At War dested Republic At War / A Precarious Predicament. "
    "Geonosis: Forward Command Center dested Geonosis: Forward Command Center. "
    "A Grand Army Of The Republic dested A Grand Army Of The Republic. "
    "Begun, The Clone War Has dested Begun, The Clone War Has. "
    "Anakin Skywalker, PL dested Anakin Skywalker, Padawan Learner. "
    "Out Of Commission + TT dested Out Of Commission & Transmission Terminated. "
    "AT-TE Walker dested AT-TE. "
    "Republic Gunship Wings dested Republic Attack Gunship. "
    "Low-Altitude Assault Transport dested Low-Altitude Assault Transport. "
    "Hear Me Baby, Hold Together dested Hear Me Baby, Hold Together. "
    "Aa- Something Wind Chimes dested as written. "
    "Path Of Least Resistance + Barrier dested Path Of Least Resistance. "
    "Muunilinst: RLS dested Muunilinst: Republic Landing Site. "
    "Muunilinst: HP dested Muunilinst: Harnaidan Plains. "
    "Muunilinst: COH dested Muunilinst: City Of Harnaidan. "
    "Threepio, WTHPS dested See-Threepio. "
    "Arrow-BLD dested as written. "
    "K'lor Slug dested K'lor'slug. "
    "Shields 11–12 empty skipped. "
    "Unique overcounts sheet-accurate (Anakin Skywalker, Padawan Learner x3, "
    "Out Of Commission & Transmission Terminated x2, Clone Specialist x8, AT-TE x3, "
    "Republic Attack Gunship x2, Low-Altitude Assault Transport x2, Blaster Rifle x2, "
    "Flash Of Insight x2, Out Of Nowhere x2, Escape Pod x2, Rebel Barrier x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). "
    "Name Thomas Whaley. Username blank. DARK checked. "
    "Deck Name some old bull shit. "
    "Knowledge And Defense dested Knowledge And Defense (starting interrupt; no objective). "
    "My Lord, Is That Legal dested My Lord, Is That Legal. "
    "Begin Landing Your Troops dested Begin Landing Your Troops. "
    "Blockade Flagship: Bridge dested Blockade Flagship: Bridge. "
    "Breached Defenses + Malfunction dested as written. "
    "Ni Chuba Na dested Ni Chuba Na?. "
    "NO_DEST remaining: Aa- Something Wind Chimes, Arrow-BLD, My Lord Is That Legal, "
    "Breached Defenses + Malfunction, Iott Droid, Open Fire + TAD, Tikkos, Baskol Yeersin, "
    "Jano Eclipse, Tatooine: DLS, Motion Support, Droid, Accepting Trade Federation, "
    "Republic Attack Gunship, Republic At War / A Precarious Predicament. "
    "Iott Droid dested as written. "
    "Aks Moc dested Aks Moe. "
    "Open Fire + TAD dested as written. "
    "Toobuck Toora dested Toonbuck Toora. "
    "Edcel Bar Gane dested Edcel Bar Gane. "
    "Tikkos dested as written. "
    "Passel Argente dested Passel Argente. "
    "Baskol Yeersin dested Baskol Yeersin. "
    "Darth Vader With Stick dested Darth Vader With Lightsaber. "
    "Galen Marek dested Galen Marek, Starkiller. "
    "Darth Maul With Stick dested Darth Maul With Lightsaber. "
    "Jano Eclipse dested as written. "
    "Aurra Sing, DA dested Aurra Sing, Deadly Assassin. "
    "Jango Fett, TA dested Jango Fett, The Assassin. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. "
    "Tatooine: DLS dested as written. "
    "Coruscant: PQ dested Coruscant: Palpatine's Quarters. "
    "Rogue Shadow dested Rogue Shadow. "
    "Slave I, SOF dested Slave I, Symbol Of Fear. "
    "Ghhhk & TRWEU dested Ghhhk & Those Rebels Won't Escape Us. "
    "Sith Fury & ETDC dested Sith Fury & End This Destructive Conflict. "
    "Omni Box + Its Worse dested Omni Box & It's Worse. "
    "Accepting Trade Federation dested Accepting Trade Federation. "
    "Our Blockade Is Perfectly Legal dested Our Blockade Is Perfectly Legal. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "CHYBC dested Come Here You Big Coward. "
    "TINT dested There Is No Try. "
    "Unique overcounts sheet-accurate (Iott Droid x3, Open Fire + TAD x2, "
    "Toonbuck Toora x2, Edcel Bar Gane x2, Darth Vader With Lightsaber x3, "
    "Galen Marek, Starkiller x2, Darth Maul With Lightsaber x2, "
    "Squabbling Delegates x3, Blizzard 4 x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / A Precarious Predicament"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Geonosis: Forward Command Center"),
    n("A Grand Army Of The Republic", True),
    n("Begun, The Clone War Has", True),
    n("Cloning Cylinders", True),
    n("Wokling", True),
    n("The Dark Side Is Growing", True),
    n("Republic At War / A Precarious Predicament", True),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Anakin Skywalker, Padawan Learner"),
    n("Out Of Commission & Transmission Terminated", True, qty=2),
    n("Clone Specialist", True, qty=8),
    n("AT-TE", True, qty=3),
    n("Republic Attack Gunship", True, qty=2),
    n("Low-Altitude Assault Transport", True),
    n("Low-Altitude Assault Transport"),
    n("Blaster Rifle", True, qty=2),
    n("Quick Draw", True),
    n("Hear Me Baby, Hold Together", True),
    n("Aa- Something Wind Chimes"),
    n("Path Of Least Resistance"),
    n("Rebel Barrier"),
    n("Out Of Nowhere"),
    n("Flash Of Insight", True),
    n("Imperial Atrocity", True),
    n("Muunilinst: Republic Landing Site", True),
    n("Muunilinst: Harnaidan Plains", True),
    n("Muunilinst: City Of Harnaidan", True),
    n("Much To Learn You Still Have", True),
    n("See-Threepio"),
    n("Out Of Nowhere"),
    n("Houjix"),
    n("We Wish To Board At Once"),
    n("Flash Of Insight", True),
    n("Azure Angel", True),
    n("Concussion Missiles"),
    n("Acclamator-Class Assault Ship"),
    n("Arrow-BLD"),
    n("Restraining Bolt"),
    n("Thrown Back"),
    n("Assault On Muunilinst"),
    n("K'lor'slug", True),
    n("Escape Pod", True),
    n("Anakin's Lightsaber"),
    n("Escape Pod", True),
    n("It Could Be Worse"),
    n("Rebel Barrier"),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Wise Advice", True),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
]
LS_ADD = []


DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("My Lord, Is That Legal"),
    n("Begin Landing Your Troops"),
    n("Prepared Defenses"),
    n("Coruscant: Galactic Senate"),
    n("Blockade Flagship: Bridge"),
    n("Breached Defenses + Malfunction", True),
    n("Ni Chuba Na?"),
    n("Iott Droid", qty=3),
    n("Aks Moe"),
    n("Open Fire + TAD", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Edcel Bar Gane", qty=2),
    n("Tikkos"),
    n("Passel Argente"),
    n("Baskol Yeersin"),
    n("Darth Vader With Lightsaber", qty=3),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Count Dooku", True),
    n("P-59"),
    n("Arica", True),
    n("Battle Droid Squad", True),
    n("Jano Eclipse", True),
    n("Aurra Sing, Deadly Assassin", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Death Star: War Room", True),
    n("Tatooine: DLS", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Rogue Shadow", True),
    n("Slave I, Symbol Of Fear", True),
    n("Squabbling Delegates", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sith Fury & End This Destructive Conflict", True),
    n("Unsalvageable"),
    n("Lightsaber Deficiency", True),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Omni Box & It's Worse", True),
    n("Senate Hovercam"),
    n("First Strike"),
    n("Motion Support"),
    n("Blast Door Controls"),
    n("Droid"),
    n("This Is Outrageous"),
    n("Accepting Trade Federation"),
    n("Our Blockade Is Perfectly Legal"),
    n("No Escape"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Battle Order"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Abyss"),
]
DS_ADD = []
