#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Orlie Martin.

Source: 2012NationalsDay1.pdf pages 38–39 (handwritten 2010 Xerox, 12 shields).
p38 Light / p39 Dark Name Orlie Martin dested Orlie Martin as written.
Username blank. Analog leftover generate empty dest as written.
Do not dest as James Martin / Martin den Boef / Bill Martinson.
Pack player-stubs/Orlie_Martin.wiki.
"""
from __future__ import annotations

PLAYER = "Orlie Martin"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 38
DS_PAGE = 39
LS_SCAN = "2012 US Nationals Day 1 Orlie Martin LS.png"
DS_SCAN = "2012 US Nationals Day 1 Orlie Martin DS.png"
LS_DECK_NAME = "This is my Light Deck"
DS_DECK_NAME = "Senate"
NOTE = "Handwritten 2010 Xerox. Name Orlie Martin dested Orlie Martin as written. Username blank."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Orlie Martin dested Orlie Martin as written. "
    "Username blank. LIGHT checked. Deck Name This is my Light Deck. Event Date 6/9/12 Event Name Nats. "
    "Analog leftover generate empty dest as written. Do not dest as James Martin / Martin den Boef / Bill Martinson. "
    "Infiltration/Unlikely Allies empty dested Infiltration / Unlikely Allies analog leftover Anderson. "
    "Uh-oh. dested Uh-Oh True analog leftover. "
    "Scoundrel's Engenvity dested Scoundrel's Ingenuity analog leftover. "
    "Scoundrel's Branado dested Scoundrel's Bravado analog leftover. "
    "AFA dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Booster's Star Destroyer dested analog leftover Consoli leftover_xerox. "
    "Stay Sharp dested Stay Sharp! analog leftover Grant. "
    "Plastrod Armor dested Blastrod Armor True analog leftover. "
    "All Wings combo dested All Wings Report In & Darklighter Spin analog leftover Veasey x3 unique overcount. "
    "Clakidor dested Clak'dor VII analog leftover. "
    "Han's Back dested as written leftover_xerox True. "
    "Lando Calrissian, Scoundrel dested analog leftover TMW Skilton x2. "
    "Projection of a Skywalker dested Projection Of A Skywalker analog leftover 2013 MPC Herold x2. "
    "Imperial Atrocity dested analog leftover TMW Herold True x2. "
    "Simple Tricks dested Simple Tricks And Nonsense True analog leftover Herold. "
    "Your Insight dested Your Insight Serves You Well True analog leftover TMW Skilton. "
    "Affect Mind dested analog leftover True. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Orlie Martin dested Orlie Martin as written. "
    "Username blank. DARK checked. Deck Name Senate. Event Date 6/9/12 Event Name Nats. "
    "Analog leftover generate empty dest as written. Do not dest as James Martin / Martin den Boef / Bill Martinson. "
    "My Lord, Is That Legal? empty dested analog leftover Smith. "
    "Prepared Defenses dested analog leftover IN THE 60. "
    "Naboo dested analog leftover Devin. "
    "Ni Chuba Na?? dested analog leftover Anderson True. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Lott Dod dested analog leftover Smith x4 unique overcount. "
    "Toonbuck Toora dested analog leftover Kurten x2. "
    "Orn Free Taa dested analog leftover SAN x2. "
    "Squabbling Delegates dested analog leftover Dalton x3 unique overcount. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back! analog leftover Anderson x2. "
    "Yeb Yeb Adem'thorn dested as written leftover_xerox analog leftover Kurten. "
    "Baskol Yeersim dested Baskol Yeesrim analog leftover Smith. "
    "Edrel Bar Gane dested Edcel Bar Gane analog leftover Kurten. "
    "This Is Outrageous! dested This Is Outrageous analog leftover Kurten. "
    "Our Blockade dested Our Blockade Is Perfectly Legal analog leftover SAN. "
    "Bossk In Hound's Tooth dested analog leftover Kurten True. "
    "Saber 1 dested analog leftover Graham. "
    "Vote Now! dested Vote Now analog leftover Kurten. "
    "Maul Strikes dested analog leftover Carulli. "
    "Senate Hovercam dested analog leftover Smith. "
    "Ability, Ability, Ability dested analog leftover TMW Baroni. "
    "The Phantom Menace dested analog leftover Kelly. "
    "I Find Your Lack dested I Find Your Lack Of Faith Disturbing True analog leftover Ziagos. "
    "Death Star Sentry dested analog leftover Lepine True. "
    "Code Clearance dested Do They Have A Code Clearance? True analog leftover Anderson. "
    "Come Here You Big Coward dested analog leftover Anderson True. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Heading For The Medical Frigate"),
    n("Squadron Assignments"),
    n("Uh-Oh", True),
    n("Rycar Ryjerd", True),
    n("Scoundrel's Luck"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Ingenuity"),
    n("Scoundrel's Bravado"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Anger, Fear, Aggression", True),
    n("Booster's Star Destroyer"),
    n("Mirax Terrik"),
    n("Tala 1"),
    n("Colonel Cracken"),
    n("Han Solo, Innocent Scoundrel"),
    n("Han's Heavy Blaster Pistol", True),
    n("Nudj", qty=3),
    n("Corran Horn"),
    n("Scrambled Transmission", True),
    n("Stay Sharp!"),
    n("Rebel Agent's Blaster Rifle"),
    n("Blastrod Armor", True),
    n("Dash Rendar"),
    n("Figrin D'an"),
    n("Power Pivot", qty=2),
    n("Redeemed Apprentice"),
    n("Double Agent"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Intruder Missile"),
    n("A Vergence In The Force"),
    n("Mercenary Armor", True),
    n("Rebel Agent"),
    n("Clak'dor VII"),
    n("Portable Scanner"),
    n("Han's Back", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Booster In Pulsar Skate"),
    n("Projection Of A Skywalker", qty=2),
    n("Swamp"),
    n("Max Rebo"),
    n("Rebel Barrier", qty=2),
    n("Outrider"),
    n("Lieutenant Blount", True),
    n("Tala 2"),
    n("Han's Toolkit"),
    n("Outpost"),
    n("Imperial Atrocity", True, qty=2),
    n("A Good Blaster At Your Side"),
    n("Imperial Navigation Charts"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not", True),
    n("Don't Do That Again"),
    n("Affect Mind", True),
    n("Chasm", True),
    n("Aim High", True),
    n("Wise Advice", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal?"
DS_CARDS = [
    n("My Lord, Is That Legal?"),
    n("Prepared Defenses"),
    n("Naboo"),
    n("Naboo: Theed Palace Generator Core"),
    n("Tatooine: Desert Landing Site"),
    n("Coruscant: Galactic Senate"),
    n("Ni Chuba Na??", True),
    n("Combat Response", True),
    n("Crush The Rebellion"),
    n("Knowledge And Defense", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Lott Dod", qty=4),
    n("Toonbuck Toora", qty=2),
    n("Orn Free Taa", qty=2),
    n("Squabbling Delegates", qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sense", qty=2),
    n("Coruscant Guard"),
    n("Yeb Yeb Adem'thorn"),
    n("Tikkes"),
    n("Baskol Yeesrim"),
    n("Edcel Bar Gane"),
    n("Passel Argente"),
    n("Aks Moe"),
    n("Motion Supported"),
    n("Accepting Trade Federation Control"),
    n("This Is Outrageous"),
    n("Our Blockade Is Perfectly Legal"),
    n("Mist Hunter", True),
    n("Zuckuss", True),
    n("Punishing One", True),
    n("Dengar", True),
    n("Bossk In Hound's Tooth", True),
    n("Baron Soontir Fel"),
    n("Saber 1"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Limited Resources"),
    n("Evader & Monnok"),
    n("You Are Beaten"),
    n("I Have You Now"),
    n("Masterful Move"),
    n("Vote Now"),
    n("Maul Strikes"),
    n("First Strike"),
    n("Senate Hovercam"),
    n("Blast Door Controls"),
    n("Ability, Ability, Ability"),
    n("The Phantom Menace"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward", True),
    n("Secret Plans", True),
    n("There Is No Try", True),
    n("Battle Order", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
