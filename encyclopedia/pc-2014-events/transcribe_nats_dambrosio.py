#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Mike D'Ambrosio.

Source: Nationals-2014-day-1.pdf pages 9–10 (2010 form).
Name Dambrose dest as written then identified Mike D'Ambrosio.
p09 Dark Clone Wars / AAT. p10 Light Y4 Restore Freedom.
"""
from __future__ import annotations

PLAYER = "Mike D'Ambrosio"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2014 US Nationals Day 1 p10 Mike D'Ambrosio LS.png"
DS_SCAN = "2014 US Nationals Day 1 p09 Mike D'Ambrosio DS.png"
NOTE = "Handwritten 2010 Xerox. Name Dambrose dested Mike D'Ambrosio."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Dambrose dested Mike D'Ambrosio. Username blank. LIGHT Y4. "
    "Restore Freedom dested Restore Freedom To The Galaxy. "
    "Control & Tunnel Vision dested Control & Tunnel Vision. AFA dested Anger, Fear, Aggression. "
    "Run Luke Run dested Run Luke, Run!. "
    "15 Shields doodle, no individual shields. Unique overcounts sheet-accurate "
    "(Projection Of A Skywalker x2, Rogue Squadron X-wing x3, Imperial Atrocity x2, "
    "Let The Wookiee Win x2, Organized Attack x2, Undercover x2, Rebel Barrier x2, "
    "All Wings Report In & Darklighter Spin x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Dambrose dested Mike D'Ambrosio. Username blank. DARK Clone Wars. "
    "Superlaser dested Superlaser Mark II. Geonosis Combat Arena dested Geonosis: Combat Arena. "
    "Observer First dested as written. Cell Pest dested as written. "
    "3B6-RA-7 dested 3B6-RA-7. 3B3-888 dested 3B3-888. "
    "K+D dested Knowledge And Defense. Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "15 Shields doodle, no individual shields. Unique overcounts sheet-accurate "
    "(Observer First x2, Our Blockade Is Perfectly Legal x2, Imperial Barrier x3, "
    "Command Droid x2, AAT Laser Cannon x3, Armored Assault Tank x4, Twin Laser Cannon x3, "
    "Imperial Artillery x2, Maul's Sith Infiltrator x3, Self-Destruct Mechanism x2, "
    "Heavy Fire Zone x2, Darth Maul x2). (V) from checkbox. "
    "NO_DEST (2014 index): Geonosis: Combat Arena; Dual Laser Cannon; Observer First (V); "
    "Droid With Backup; Command Droid; Armored Assault Tank; Twin Laser Cannon; "
    "Muunilinst: Command Center; They're Tracking Us; 3B6-RA-7; Muunilinst: Harnaidan Plains; "
    "Cell Pest (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Yavin 4", True),
    n("Yavin 4: Massassi War Room", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Projection Of A Skywalker", qty=2),
    n("Rogue Squadron X-wing", qty=3),
    n("Kiffex"),
    n("Rebel Fleet"),
    n("Corran Horn"),
    n("Gold Leader In Gold 1", True),
    n("Red 6"),
    n("Imperial Atrocity", True, qty=2),
    n("Lady Luck"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Jaina Solo"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Luke Skywalker, Jedi Knight"),
    n("Artoo-Detoo In Red 5"),
    n("Luke", True),
    n("Massassi Base Sentry"),
    n("S-foils", True),
    n("Haven"),
    n("Tycho Celchu", True),
    n("Red Squadron 1"),
    n("Luke, Trust Me"),
    n("Organized Attack", qty=2),
    n("Captain Han Solo"),
    n("Let The Wookiee Win", True, qty=2),
    n("Alter", True),
    n("Nar Shaddaa"),
    n("X-wing Laser Cannon"),
    n("Bespin"),
    n("Control & Tunnel Vision"),
    n("Millennium Falcon", True),
    n("Undercover", True, qty=2),
    n("Mirax Terrik"),
    n("Rebel Barrier", qty=2),
    n("Escape Pod"),
    n("Run Luke, Run!"),
    n("Careful Planning", True),
    n("It's A Hit!", True),
    n("Ten Numb", True),
    n("Dash Rendar", True),
    n("Lieutenant Blount", True),
    n("Houjix"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Yavin 4: Massassi Headquarters"),
    n("Restore Freedom To The Galaxy"),
    n("Chewbacca", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Superlaser Mark II"
DS_CARDS = [
    n("Superlaser Mark II"),
    n("Geonosis: Combat Arena"),
    n("Dual Laser Cannon"),
    n("Droid Starfighters"),
    n("War Has Begun"),
    n("Ni Chuba Na??"),
    n("Defense Of Muunilinst"),
    n("Observer First", True, qty=2),
    n("Prepared Defenses"),
    n("Droid With Backup"),
    n("Our Blockade Is Perfectly Legal", True),
    n("Our Blockade Is Perfectly Legal"),
    n("Imperial Barrier", qty=3),
    n("Image Of The Dark Lord", True),
    n("Ghhhk"),
    n("Muunilinst: City Of Harnaidan"),
    n("Command Droid", qty=2),
    n("AAT Laser Cannon", qty=3),
    n("Armored Assault Tank", qty=4),
    n("Dengar In Punishing One"),
    n("AAT Assault Leader"),
    n("4-LOM", True),
    n("Twin Laser Cannon", qty=3),
    n("Muunilinst: Command Center"),
    n("Everything Is Going As Planned"),
    n("They're Tracking Us"),
    n("Imperial Artillery", True, qty=2),
    n("Imperial Propaganda", True),
    n("Masterful Move & Endor Occupation"),
    n("Maul's Sith Infiltrator", qty=3),
    n("U-3PO (Yoo-Threepio)"),
    n("Self-Destruct Mechanism", True),
    n("Self-Destruct Mechanism"),
    n("Heavy Fire Zone", qty=2),
    n("Much Anger In Him"),
    n("3B6-RA-7"),
    n("Darth Maul", qty=2),
    n("Open Fire!"),
    n("There They Are!"),
    n("Muunilinst: Harnaidan Plains"),
    n("OOM-9", True),
    n("Cell Pest", True),
    n("3B3-888"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = []
DS_ADD = []
