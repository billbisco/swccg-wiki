#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Brian Terwilliger.

Source: MPC-2014-Day-1-Main-Event.pdf pages 111–112 (2013 form, 15 shields).
Name Brian Twigg dested Brian Terwilliger. Username blank.
"""
from __future__ import annotations

PLAYER = "Brian Terwilliger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 111
DS_PAGE = 112
LS_SCAN = "2014 Match Play Championship Day 1 Brian Terwilliger LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Brian Terwilliger DS.png"
LS_DECK_NAME = "No Touché"
DS_DECK_NAME = "Your a Slave for me..."
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Brian Twigg dested Brian Terwilliger. Username blank. "
    "LIGHT checked. Deck name No Touché. Yavin 4 (V) system start. "
    "Restore Freedom dested Restore Freedom To The Galaxy. Kipley dested Kiffex. "
    "Y4 Massassi HQ dested Yavin 4: Massassi Headquarters. Y4 War Room dested "
    "Yavin 4: Massassi War Room. Luke Twin Star dested Luke Skywalker. "
    "Nar Shaddaa dested Nar Shaddaa. Jaina Solo dested Jaina Solo. "
    "Lt. Blount dested Lieutenant Blount; (V) scribbled dested without (V). "
    "Chewie dested Chewbacca. Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. Lady Luck dested Lady Luck. "
    "R2 in Red 5 dested Artoo-Detoo In Red 5. Mission Brief Safety dested Massassi Base Sentry. "
    "POAS dested Projection Of A Skywalker; (V) scribbled dested without (V). "
    "Control / TV dested Control & Tunnel Vision. All Wings / DLS dested "
    "All Wings Report In & Darklighter Spin. Organized Attack dested Organized Attack. "
    "Antilles Maneuver / Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Rebel Acc dested Rebel Barrier. Unique overcounts sheet-accurate "
    "(Imperial Atrocity (V) x2, Rebel Barrier x2, Let The Wookiee Win x2, "
    "Undercover (V) x2, Projection Of A Skywalker x2, All Wings Report In & Darklighter Spin x2, "
    "Organized Attack x2, Rogue Squadron X-wing (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Brian Twigg dested Brian Terwilliger. Username blank. "
    "DARK checked. Deck name Your a Slave for me... Wookiee Slaving Operation / "
    "Indentured To The Empire dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Ket Maliss, Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. Jango Fett, The Assassin dested "
    "Jango Fett, The Assassin. P-59 dested P-59. Gela Yeens dested Gela Yeens. "
    "Operatives as Planned dested Something Special Planned For Them. "
    "Ghhhk / Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "Den Of Thieves / Special Delivery dested Den Of Thieves & Special Delivery. "
    "Tampell Banner dested Tarkin's Orders. SRF / Watch Your Back dested "
    "Short Range Fighters & Watch Your Back!. Evader / You Are Beaten dested "
    "Evader / You Are Beaten. Braccles & Defense / Whatever dested "
    "Defensive Fire & Hutt Smooch. Elis in Hunter dested Mist Hunter. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Kashyyyk Forest Maze dested Kashyyyk: Forest Maze. K+D dested Knowledge And Defense. "
    "Scum & Villainy dested Scum And Villainy. Cease Fire dested Cease Fire!. "
    "Lurkers in West Hall dested Jabba's Palace: Audience Chamber. "
    "Unique overcounts sheet-accurate (Outer Rim Scout x3, Ghhhk & Those Rebels Won't Escape Us x2, "
    "Cease Fire! x2, Elis Helrot x2, Sonic Bombardment (V) x3). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Yavin 4", True),
    n("Kiffex"),
    n("Yavin 4: Massassi Headquarters"),
    n("Yavin 4: Massassi War Room"),
    n("Squadron Assignments"),
    n("Luke Skywalker", True),
    n("Wokling", True),
    n("Nar Shaddaa", True),
    n("Ten Numb", True),
    n("Leebo", True),
    n("Dash Rendar", True),
    n("Captain Han Solo"),
    n("Jaina Solo", True),
    n("Luke Skywalker", True),
    n("Lieutenant Blount"),
    n("Chewbacca", True),
    n("Tycho Celchu", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Corran Horn"),
    n("Jek Porkins", True),
    n("Boushh"),
    n("Millennium Falcon", True),
    n("Gold Leader In Gold 1", True),
    n("Outrider"),
    n("Red Squadron 1"),
    n("Rogue Squadron X-wing", True, qty=2),
    n("Lady Luck", True),
    n("Artoo-Detoo In Red 5"),
    n("Red 6"),
    n("X-wing Laser Cannon"),
    n("Imperial Atrocity", True, qty=2),
    n("I've Got A Bad Feeling About This"),
    n("Rebel Barrier", qty=2),
    n("Let The Wookiee Win", qty=2),
    n("Massassi Base Sentry", True),
    n("Legendary Starfighter"),
    n("Undercover", True, qty=2),
    n("Projection Of A Skywalker", qty=2),
    n("Haven"),
    n("S-foils", True),
    n("Houjix"),
    n("Escape Pod", True),
    n("Control & Tunnel Vision"),
    n("Sabotage", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Organized Attack", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Careful Planning", True),
    n("Rebel Barrier", True),
    n("Restore Freedom To The Galaxy", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Jabba's Prize", True),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
    n("Battle Plan"),
    n("There Is Another", True),
    n("Aim High"),
    n("Do, Or Do Not", True),
    n("Ultimatum", True),
    n("A Tragedy Has Occurred", True),
    n("Wise Advice", True),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Ket Maliss, Shadow Killer", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Dengar With Blaster Carbine", True),
    n("Jabba The Hutt", True),
    n("Prince Xizor"),
    n("Mara Jade With Lightsaber", True),
    n("Bossk With Mortar Gun", True),
    n("Ponda Baba", True),
    n("Jango Fett, The Assassin", True),
    n("Velken Tezeri", True),
    n("Lady Valarian", True),
    n("Bib Fortuna", True),
    n("Ephant Mon"),
    n("P-59"),
    n("Probot", True),
    n("Gela Yeens", True),
    n("Outer Rim Scout", qty=3),
    n("Mercenary Slavers", True),
    n("Something Special Planned For Them", True),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Hutt Bounty", True),
    n("Crush The Rebellion"),
    n("Wookiee Subjugation", True),
    n("Look Sir, Droids"),
    n("Power Of The Hutt"),
    n("Den Of Thieves & Special Delivery", True),
    n("Tarkin's Orders"),
    n("First Strike"),
    n("Jabba's Haven", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Scum And Villainy"),
    n("Protocol Failure", True),
    n("Cease Fire!", qty=2),
    n("Evader / You Are Beaten"),
    n("Defensive Fire & Hutt Smooch", True),
    n("Elis Helrot", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency"),
    n("Jabba's Palace: Audience Chamber"),
    n("Slave I, Symbol Of Fear", True),
    n("Jabba's Space Cruiser", True),
    n("Mist Hunter", True),
    n("Jabba's Sail Barge", True),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Kashyyyk: Forest Maze", True),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Kashyyyk: Skyhook Platform", True),
    n("Kashyyyk"),
    n("Nal Hutta"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("Allegations Of Corruption", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward", True),
    n("Resistance", True),
    n("Do They Have A Code Clearance", True),
    n("There Is No Try", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
