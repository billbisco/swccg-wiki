#!/usr/bin/env python3
"""2013 Alderaan Regionals: Roy McCarthy typed 2010 Print Form LS+DS.

No (Vn) tags and no (V) checkboxes — Decipher-card space lists.
"""
from __future__ import annotations

PLAYER = "Roy McCarthy"
USERNAME = "RybackStun"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 27
DS_PAGE = 28
LS_SCAN = "2013 Alderaan Regionals p27 Roy McCarthy LS.png"
DS_SCAN = "2013 Alderaan Regionals p28 Roy McCarthy DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Concentrate All Firepower on that Super "
    "Star Destroyer! No (V) checkboxes and no (Vn) tags. Battle Plan is listed in the "
    "Reserve 60 (slot 3), not on the shield pad. GrimTassh → Grimtaash. "
    "BlasTech E-110 → BlasTech E-11B Blaster Rifle. Karle Neth → Karie Neth. "
    "Shield and additional-card pads are empty."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form. Deck title Intensify Forward Firepower! Dated 14 July 2013. "
    "No (V) checkboxes and no (Vn) tags. Battle Order is listed in the Reserve 60 (slot 5). "
    "TIE Defender Mark 1 → TIE Defender Mark I. Endor: Ancient Forrest → Endor: Ancient Forest. "
    "Shield and additional-card pads are empty."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Sullust"
LS_CARDS = [
    n("Sullust"),
    n("Heading For The Medical Frigate"),
    n("Battle Plan"),
    n("Squadron Assignments"),
    n("Superficial Damage"),
    n("Admiral Ackbar"),
    n("General Solo"),
    n("Chewbacca Of Kashyyyk"),
    n("Gray Squadron Y-wing Pilot", qty=2),
    n("Kin Kian"),
    n("Derek 'Hobbie' Klivian"),
    n("Keir Santage"),
    n("Karie Neth"),
    n("Dresselian Commando", qty=2),
    n("Corporal Beezer"),
    n("Corporal Midge"),
    n("Corporal Janse"),
    n("Corporal Delevar"),
    n("Sergeant Junkin"),
    n("Captain Yutani"),
    n("Gray Squadron 1"),
    n("Gray Squadron 2"),
    n("Red Squadron 4"),
    n("Red Squadron 7"),
    n("Y-wing"),
    n("X-wing", qty=2),
    n("Nebulon-B Frigate", qty=3),
    n("B-wing Bomber", qty=3),
    n("A-wing", qty=3),
    n("Bespin"),
    n("Tatooine"),
    n("Endor"),
    n("Endor: Great Forest"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Hidden Forest Trail"),
    n("Endor: Back Door"),
    n("BlasTech E-11B Blaster Rifle", qty=2),
    n("Intruder Missile", qty=2),
    n("Concussion Missiles", qty=2),
    n("Enhanced Proton Torpedoes"),
    n("Houjix"),
    n("Steady Aim"),
    n("Careful Planning"),
    n("Take The Initiative"),
    n("Grimtaash", qty=2),
    n("A Few Maneuvers", qty=2),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Prepared Defenses"),
    n("Combat Response"),
    n("Inconsequential Losses"),
    n("Battle Order"),
    n("Admiral Piett"),
    n("Captain Jonus"),
    n("Lieutenant Hebsly"),
    n("DS-181-3"),
    n("DS-181-4"),
    n("Reserve Pilot"),
    n("Lieutenant Arnet"),
    n("Lieutenant Grond"),
    n("Sergeant Tarl"),
    n("Corporal Drazin"),
    n("Elite Squadron Stormtrooper", qty=3),
    n("Tempest 1"),
    n("Tempest Scout 3"),
    n("Tempest Scout", qty=2),
    n("Scimitar 2"),
    n("Black 3"),
    n("Scythe 3"),
    n("Saber 3"),
    n("Saber 4"),
    n("Scythe Squadron TIE", qty=2),
    n("TIE Interceptor", qty=3),
    n("TIE Defender Mark I", qty=3),
    n("Victory-Class Star Destroyer", qty=3),
    n("Dark Maneuvers", qty=2),
    n("Monnok", qty=2),
    n("Ghhhk"),
    n("Flawless Marksmanship"),
    n("Imperial Reinforcements"),
    n("Combat Readiness"),
    n("SFS L-s7.2 TIE Cannon", qty=2),
    n("Blaster Rifle", qty=2),
    n("Intruder Missile", qty=2),
    n("Concussion Missiles"),
    n("Mon Calamari"),
    n("Sullust"),
    n("Endor"),
    n("Endor: Ancient Forest"),
    n("Endor: Back Door"),
    n("Endor: Great Forest"),
    n("Endor: Landing Platform (Docking Bay)"),
]
DS_SHIELDS = []
DS_ADD = []
