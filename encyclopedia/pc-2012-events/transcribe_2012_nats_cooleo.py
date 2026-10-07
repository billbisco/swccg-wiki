#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Cooleo.

Source: 2012NationalsDay1.pdf pages 13–14 (handwritten 2010 Xerox, 12 shields).
Name Cooleo dested Cooleo as written. Username Cooleo.
p13 Dark Contracts / Contract Killers.
p14 Light Yub Yub / Rebel Strike Team.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Cooleo"
USERNAME = "Cooleo"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2012 US Nationals Day 1 Cooleo LS.png"
DS_SCAN = "2012 US Nationals Day 1 Cooleo DS.png"
LS_DECK_NAME = "Yub Yub"
DS_DECK_NAME = "Contracts"
NOTE = "Handwritten 2010 Xerox form. Username Cooleo."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Cooleo dested Cooleo as written. Username Cooleo. "
    "LIGHT checked. Deck Name Yub Yub. Event Date blank Event Name blank. "
    "Do not dest as a new person. Analog generate empty dest as written. "
    "Rebel Strike Team dested Rebel Strike Team / Garrison Destroyed True analog leftover Murray. "
    "Throw me a charge dested Throw Me Another Charge analog leftover Murray. "
    "Heading Frigate dested Heading For The Medical Frigate True analog leftover. "
    "Antilles Combo dested Antilles Maneuver & Rebel Reinforcements True analog leftover Grant. "
    "Narshadda Chimes dested Nar Shaddaa Wind Chimes analog leftover. "
    "Ewok Village dested Endor: Ewok Village analog leftover Murray. "
    "Dense Forest dested Endor: Dense Forest analog leftover Murray. "
    "Death Star Generator dested Deactivate The Shield Generator analog leftover Murray. "
    "Bunker dested Endor: Bunker analog leftover. "
    "Back Door dested Endor: Back Door analog leftover Murray. "
    "General Madine dested General Crix Madine analog leftover Murray. "
    "Threepio dested C-3PO analog leftover. "
    "General Solo dested General Solo analog leftover Murray. "
    "EL-14 dested leftover_xerox. "
    "Ackbar dested Admiral Ackbar analog leftover Murray. "
    "Major Haashn dested Major Haash'n analog leftover. "
    "Wedge Red 1 dested Wedge In Red Squadron 1 analog leftover Schroeder. "
    "I hope she's all right dested I Hope She's All Right True analog leftover Murray. "
    "Hunt sight dested Hindsight True analog leftover Anderson. "
    "Combat Mun En dested Combat Readiness True analog leftover Richards. "
    "The Shield is down dested The Shield Is Down! True analog leftover Murray. "
    "We'll do our part dested Wesa Ready To Do Our-Sa Part True analog leftover Murray. "
    "That's One dested leftover_xerox. "
    "Shield Don't Do That dested Don't Do That Again True analog leftover. "
    "Shield Let's Keep Optimism dested Let's Keep A Little Optimism Here analog leftover. "
    "Shield Your Insights dested Your Insight Serves You Well analog leftover. "
    "Lines 32–37 blank skip. Unique 54 sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Cooleo dested Cooleo as written. Username Cooleo. "
    "DARK checked. Deck Name Contracts. Event Date blank Event Name blank. "
    "Do not dest as a new person. Analog generate empty dest as written. "
    "Knowledge dested Knowledge And Defense True analog leftover IN THE 60. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy True analog leftover Jan. "
    "CC Prison dested Cloud City: Prison analog leftover. "
    "Dengar w/ Saber dested Dengar analog leftover. "
    "Combo Combo dested Ghhhk analog leftover Jan. "
    "Death Mark combo dested Death Mark & Hutt Bounty True analog leftover Jan. "
    "Lightsaber Prof dested Lightsaber Deficiency True analog leftover Jan. "
    "Fett Bounty Killer dested Boba Fett, Bounty Hunter analog leftover Booker. "
    "Boba Fett Prepared dested Boba Fett, Bounty Hunter analog leftover Anderson. "
    "Mandalorian Father dested Jango Fett, The Assassin analog leftover. "
    "One Beautiful dested One Beautiful Thing analog leftover. "
    "Aurra Sing Deadly dested Aurra Sing analog leftover Jan. "
    "Mara Saber dested Mara Jade's Lightsaber analog leftover. "
    "Jowille dested leftover_xerox. "
    "Fett, Shadow Killer dested leftover_xerox. "
    "Galen Saber, Gift dested Galen's Lightsaber, Vader's Gift analog leftover Ziagos. "
    "Coruscant Casino dested Coruscant: Casino analog leftover Jan. "
    "Subcity lair dested Coruscant: Sub City Lair analog leftover Jan. "
    "Emperor Palpy dested Emperor Palpatine analog leftover. "
    "Mara Jade Handy dested Mara Jade, The Emperor's Hand analog leftover. "
    "Shield Come to Me dested leftover_xerox. "
    "Shield Code Clearance dested Do They Have A Code Clearance? True analog leftover Anderson. "
    "Shield YCHF dested You Cannot Hide Forever True analog leftover. "
    "Unique 60. Shields 12. True vs empty kept separate. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rebel Strike Team / Garrison Destroyed"
LS_CARDS = [
    n("Rebel Strike Team / Garrison Destroyed", True),
    n("Throw Me Another Charge", qty=2),
    n("Nabrun Leids", qty=3),
    n("Heading For The Medical Frigate", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Nar Shaddaa Wind Chimes", qty=2),
    n("Endor: Ewok Village", True),
    n("Endor: Dense Forest"),
    n("Deactivate The Shield Generator"),
    n("Endor: Bunker"),
    n("Endor"),
    n("Endor: Back Door"),
    n("Explosive Charge", qty=2),
    n("Ewok Catapult", qty=2),
    n("Toryn Farr"),
    n("General Crix Madine"),
    n("C-3PO"),
    n("General Solo"),
    n("EL-14", True),
    n("Admiral Ackbar", True),
    n("Major Haash'n"),
    n("Ewok Sentry"),
    n("Strategic Effect", True),
    n("Wicket", True),
    n("Kazak"),
    n("Graak"),
    n("Romba"),
    n("Logray"),
    n("Wedge In Red Squadron 1", True),
    n("Home One"),
    n("I Hope She's All Right", True),
    n("Honor Of The Jedi"),
    n("Hindsight", True),
    n("Ewok Celebration"),
    n("Scrambled Transmission", True),
    n("That's One", True),
    n("Combat Readiness", True),
    n("Menace Fades"),
    n("Imperial Atrocity", True),
    n("Wokling", True),
    n("Strike Planning"),
    n("The Shield Is Down!", True),
    n("Chief Chirpa", True),
    n("No Questions Asked", True),
    n("Wesa Ready To Do Our-Sa Part", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
    n("Battle Plan", True),
    n("Aim High"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well"),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Do, Or Do Not", True),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("Cloud City: Prison", True),
    n("Blaster Rack", True),
    n("Jabba's Haven", True),
    n("On The Hunt", True),
    n("Guild Of Assassins", True),
    n("Prepared Defenses"),
    n("Emperor Palpatine"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Aurra Sing", qty=4),
    n("Force Lightning"),
    n("Dengar"),
    n("Ghhhk"),
    n("Nal Hutta"),
    n("Coruscant"),
    n("Gift Of The Master", True),
    n("Guri", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Death Mark & Hutt Bounty", True),
    n("Galen, Secret Apprentice", True),
    n("Slave I, Symbol Of Fear", True),
    n("Lightsaber Deficiency", True),
    n("Tarkin's Bounty", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Boba Fett, Bounty Hunter"),
    n("Bane Malar", True),
    n("Abyssin Ornament", True, qty=3),
    n("Jango Fett, The Assassin", True, qty=2),
    n("Sith Fury", qty=3),
    n("Velken Tezeri", True),
    n("Molator", True),
    n("One Beautiful Thing", True),
    n("One Beautiful Thing", qty=2),
    n("Mara Jade's Lightsaber", True),
    n("Slave I, Symbol Of Fear"),
    n("Boba Fett, Bounty Hunter", True),
    n("Jowille", True),
    n("According To My Design"),
    n("Protocol Failure"),
    n("Trophy Of A Kill", qty=2),
    n("Fett, Shadow Killer"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Galen, Secret Apprentice"),
    n("Coruscant: Casino"),
    n("Coruscant: Sub City Lair"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Come To Me", True),
    n("Battle Order"),
    n("Secret Plans", True),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
]
DS_ADD = []
