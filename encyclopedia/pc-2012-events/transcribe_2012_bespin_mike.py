#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Mike Dark only.

Source: 2012BespinRegionals.pdf page 35.
p35 Dark handwritten 2010 Xerox. Name Mike dested Mike (2012 Bespin Regionals)
analog leftover generate_2012_nats.py George last-name/first-name collision
([[Mike]] is #REDIRECT [[Mike Thomas]]; Username blank). Username blank.
p36 Light MIKE Event Date 21/4/12 other-event skip analog leftover p12 Nats bound-in.
No facing Bespin Light. LS_CARDS empty skip Light analog leftover Brist.
Do not dest as Mike Thomas. Do not overwrite the existing [[Mike]] redirect.
Do not dest as Mike Richards / Mike Pistone / Mike Gemme / Mike Kessling.
Pack player-stubs/Mike_(2012_Bespin_Regionals).wiki.
"""
from __future__ import annotations

PLAYER = "Mike"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 35
DS_PAGE = 35
LS_SCAN = ""
DS_SCAN = "2012 Bespin Regionals Mike DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p35 Dark. Name Mike dested Mike (2012 Bespin Regionals) "
    "analog leftover generate_2012_nats.py George collision ([[Mike]] is #REDIRECT "
    "[[Mike Thomas]]; Username blank). Username blank. Event Date 7/14/12 dest Bespin. "
    "p36 Light MIKE Event Date 21/4/12 other-event skip analog leftover p12 Nats bound-in. "
    "No facing Bespin Light. Hub Light stays —. "
    "Do not dest as Mike Thomas. Do not overwrite the existing [[Mike]] redirect. "
    "Do not dest as Mike Richards / Mike Pistone / Mike Gemme / Mike Kessling."
)
LS_NOTE = (
    "No facing Bespin Light. p36 Light MIKE Event Date 21/4/12 other-event skip analog leftover "
    "p12 Nats bound-in. LS_CARDS empty skip Light analog leftover Brist."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p35 Dark. Name Mike dested Mike (2012 Bespin Regionals). Username blank. "
    "DARK checked. Event Date 7/14/12. Event Name blank. Deck Name blank. "
    "EOPS dested Endor Operations / Imperial Outpost analog leftover nats Hanson. "
    "End: bunker dested Endor: Bunker analog leftover nats Hanson. "
    "End: platform dested Endor: Landing Platform (Docking Bay) analog leftover nats Hanson. "
    "Prep Def dested Prepared Defenses analog leftover. "
    "Est. Control dested Establish Control analog leftover Hanson. "
    "I-40 dested I've Lost Artoo analog leftover Brist. "
    "incensed losses dested Intensify The Forward Batteries analog leftover nats Hanson. "
    "Temp Sc. 1 dested Tempest Scout 1 analog leftover nats Hanson. "
    "End: back door dested Endor: Back Door analog leftover typical. "
    "Green Fighter dested TIE Fighter analog leftover typical. "
    "Imp. Decree dested Imperial Decree analog leftover nats Hanson. "
    "SFS Cannon dested SFS L-s9.3 Laser Cannon analog leftover Nelson. "
    "Imp artillery dested Imperial Artillery analog leftover jake nelson d2. "
    "Endor Shield dested analog leftover nats Hanson. "
    "Corp. Jacosyn dest as written analog leftover empty. "
    "Naraddo dested Nar Shaddaa analog leftover Kafer. "
    "Sneak Attack True lines 23 and 38 dest qty=2 at first; empty line 33 kept separate analog leftover differing checkbox. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Anderson. "
    "Flap! eep dested Maneuvering Flaps analog leftover Anderson. "
    "Est. Sec Base dested Establish Secret Base analog leftover nats Hanson. "
    "Combat Response dested analog leftover Nelson. "
    "Vader Shuttle dested Vader's Personal Shuttle analog leftover Li. "
    "Conduct Your Search dested analog leftover Lush. "
    "Black 2 dested analog leftover Nelson. "
    "Wounded Warrior dested analog leftover TYPE_OVERRIDE. "
    "Baron Fel dested Baron Soontir Fel analog leftover Nelson. "
    "imp cuff dested Imperial Arrest Order analog leftover Fernando. "
    "Sens. Barrier dested Sense analog leftover typical. "
    "Def. Fire dested Defensive Fire analog leftover Kurten. "
    "If armor dested If The Armor's Fully Operational analog leftover typical. "
    "U3PO dested U-3PO analog leftover Howland. "
    "ATST Cannon dested AT-ST Dual Cannon analog leftover Gogolen qty=2. "
    "4 Loms concussion dested 4-LOM With Concussion Rifle analog leftover Howland. "
    "SRF / watch back dested Short Range Fighters & Watch Your Back! analog leftover Nelson qty=2. "
    "Pendor dested Fondor analog leftover nats Hanson. "
    "Zuckuss in Hunter dested Zuckuss In Mist Hunter analog leftover Hanson. "
    "Mst magician dested Masterful Move & Endor Occupation analog leftover Baroni. "
    "Lt. Watts dested Lieutenant Watts analog leftover Gogolen. "
    "Bliz Sct 1 dested Blizzard Scout 1 analog leftover Gogolen. "
    "Lt. Grond dested Lieutenant Grond analog leftover Gardner. "
    "Knowl + def dested Knowledge And Defense analog leftover nats Hanson IN THE 60. "
    "Shield 1 Cannot hide forever dested You Cannot Hide Forever analog leftover extra S clip. "
    "OPP Enforc dested Oppressive Enforcement analog leftover Hanson. "
    "Useless gestr dested A Useless Gesture analog leftover Hanson. "
    "Come here coward dested Come Here You Big Coward analog leftover Hanson. "
    "Flag area dest as written analog leftover empty. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor"),
    n("Prepared Defenses"),
    n("Establish Control", True),
    n("I've Lost Artoo"),
    n("Intensify The Forward Batteries", True),
    n("Tempest Scout 1"),
    n("Endor: Back Door"),
    n("TIE Fighter"),
    n("Imperial Decree", True),
    n("SFS L-s9.3 Laser Cannon"),
    n("Arica"),
    n("Imperial Artillery"),
    n("DS-61-2"),
    n("Perimeter Patrol"),
    n("Endor Shield", True),
    n("Corporal Jacosyn"),
    n("Kashyyyk"),
    n("Nar Shaddaa"),
    n("Limited Resources"),
    n("Sneak Attack", True, qty=2),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader"),
    n("Maneuvering Flaps", True),
    n("Darth Maul"),
    n("Establish Secret Base", True),
    n("Combat Response", True),
    n("Tempest Scout 5"),
    n("Vader's Personal Shuttle", True),
    n("Conduct Your Search"),
    n("Sneak Attack"),
    n("Black 2", True),
    n("Wounded Warrior"),
    n("Baron Soontir Fel"),
    n("Imperial Arrest Order"),
    n("Sense"),
    n("Defensive Fire", True),
    n("Saber 1"),
    n("If The Armor's Fully Operational"),
    n("U-3PO"),
    n("AT-ST Dual Cannon", True, qty=2),
    n("4-LOM With Concussion Rifle"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Fondor"),
    n("Zuckuss In Mist Hunter"),
    n("Tempest Scout 3"),
    n("Masterful Move & Endor Occupation"),
    n("Tempest Scout 2"),
    n("Lieutenant Watts"),
    n("Blizzard Scout 1", True),
    n("Trample"),
    n("Lieutenant Grond", True),
    n("Avenger"),
    n("Tempest Scout 6"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever"),
    n("Oppressive Enforcement", True),
    n("Fanfare"),
    n("A Useless Gesture"),
    n("Crossfire"),
    n("Resistance", True),
    n("Battle Order", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Flag Area"),
    n("Secret Plans", True),
]
DS_ADD = []
