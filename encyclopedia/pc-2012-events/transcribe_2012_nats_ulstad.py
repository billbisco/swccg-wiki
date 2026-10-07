#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Matthew Ulstad.

Source: 2012NationalsDay1.pdf pages 76–77 (handwritten notebook dump).
p76 Light / p77 Dark Name Matthew Ulstad Username blank dested Matthew Ulstad
analog leftover empty dest as written. Pack player-stubs/Matthew_Ulstad.wiki.
p77 Dark Starter Dark Side Deck joke empty 60 skip card text.
"""
from __future__ import annotations

PLAYER = "Matthew Ulstad"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 76
DS_PAGE = 77
LS_SCAN = "2012 US Nationals Day 1 Matthew Ulstad LS.png"
DS_SCAN = "2012 US Nationals Day 1 Matthew Ulstad DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten notebook dump. Name Matthew Ulstad dested Matthew Ulstad analog leftover empty. "
    "Username blank. p77 Dark empty 60 skip card text. Do not dest as a new identified person until analog identifies."
)
LS_NOTE = (
    "Handwritten notebook. Name Matthew Ulstad dested Matthew Ulstad analog leftover empty. "
    "Username blank. Light Side. Circled 1 Ewok Log Jam dested dest-as-written slang LS_START. "
    "Wukon Serper dested Wyron Serper analog leftover SAN. "
    "Yub Yub! dested analog leftover Scott. "
    "Endor Back Door dested Endor: Back Door analog leftover Scott. "
    "Endor: Dense Forest dested analog leftover dest-as-written x3. "
    "Endor: Great Forest dested analog leftover dest-as-written x3. "
    "The Time For Our Attack dested analog leftover dest-as-written x2. "
    "Swamp dested Swamp analog leftover Martin. "
    "Endor: Landing Platform dested analog leftover Gogolen. "
    "Sound The Attack dested analog leftover Scott. "
    "We're Doomed dested analog leftover Amato. "
    "Endor: Hidden Forest Trail dested analog leftover Scott. "
    "AFA dested Anger, Fear, Aggression analog leftover Scott IN THE 60. "
    "Firefight dested analog leftover Peterson. "
    "Ewok Rescue dested analog leftover Murray. "
    "Ewok Sentry dested analog leftover Scott. "
    "Ord Mantell dested analog leftover dest-as-written. "
    "Rebel Trooper x5 unique overcount. Endor Scout Trooper x3. "
    "No (V) boxes. Shields none. Unique 60."
)
DS_NOTE = (
    "Handwritten notebook. Name Matthew Ulstad dested Matthew Ulstad analog leftover empty. "
    "Username blank. Dark Side. Starter Dark Side Deck (But Seriously) It was. "
    "Empty 60 skip card text analog leftover Aaron Nelson Light-only emit. Unique 0. Shields 0."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Ewok Log Jam"
LS_CARDS = [
    n("Ewok Log Jam", qty=2),
    n("Endor Scout Trooper", qty=3),
    n("Wyron Serper"),
    n("Blaster Rifle", qty=2),
    n("A-wing", qty=2),
    n("Ewok Spear", qty=2),
    n("Critical Error Revealed"),
    n("Corporal Midge", qty=2),
    n("Ewok Spearman", qty=2),
    n("Yub Yub!"),
    n("Wioslea"),
    n("Rebel Trooper", qty=5),
    n("Grappling Hook"),
    n("Battle Plan"),
    n("Panic"),
    n("Dressellian Commando"),
    n("Endor: Back Door"),
    n("Endor: Dense Forest", qty=3),
    n("X-wing"),
    n("Endor: Great Forest", qty=3),
    n("General Dodonna"),
    n("The Time For Our Attack", qty=2),
    n("Swamp"),
    n("Blaster", qty=2),
    n("B-wing Bomber", qty=2),
    n("Rebel Guard"),
    n("Ewok Bow", qty=2),
    n("Ewok Tribesman", qty=2),
    n("Endor"),
    n("Endor: Landing Platform"),
    n("Sound The Attack"),
    n("We're Doomed"),
    n("Endor: Hidden Forest Trail"),
    n("Anger, Fear, Aggression"),
    n("Firefight"),
    n("Ewok Rescue"),
    n("Y-wing"),
    n("Ewok Sentry"),
    n("Ord Mantell"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
