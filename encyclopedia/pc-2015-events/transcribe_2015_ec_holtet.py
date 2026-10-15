#!/usr/bin/env python3
"""2015 European Championship Day 2: Jon Benkert Holtet (place 16).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p34 Dark / p35 Light typed slang lists with handwritten edits.
"""
from __future__ import annotations

PLAYER = "Jon Benkert Holtet"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 35
DS_PAGE = 34
LS_SCAN = "2015 European Championship Jon Benkert Holtet LS.png"
DS_SCAN = "2015 European Championship Jon Benkert Holtet DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 16. Not on official form: typed free-text lists with slang headings, blue handwritten edits. "
    "Name handwritten Jon Benkert Holtet \"Holo\". No username box. DS 2:2 / LS 2:2. "
    "Sheet deck names: DS Johnnytanglements, LS Hidden in the \"AErmet\"(sleeve). "
    "Both sides total 59 on the sheet after handwritten edits; kept as written."
)
LS_NOTE = (
    "Posted Hidden base/something something darkside dested Hidden Base / Systems Will Slip Through Your Fingers (no V marked). "
    "Posted Superfaciale damage dested Superficial Damage. Posted 3x blue b-wing squadron dested Blue Squadron B-wing x3. "
    "Posted Obi-wan in Radiant 6 dested Obi-Wan In Radiant VII (VS card, wiki only). Posted Gold leader ind gold 1 v dested Gold Leader In Gold 1 True. "
    "Handwritten HcF dested Han, Chewie, And The Falcon. Handwritten 2x on x-wing laser cannon dested X-wing Laser Cannon x2. "
    "Posted 4 (overwrites typed digit) x protons torpedos dested Proton Torpedoes x4. Handwritten Intruder missile / Concussion Missiles added. "
    "Posted Yoda stew combo dested Yoda Stew & You Do Have Your Moments. Posted Control combo dested Control & Tunnel Vision. "
    "Handwritten Out of Commision combo dested Out Of Commission & Transmission Terminated. Posted 2x all wings report in dested All Wings Report In x2. "
    "Posted Stay sharp dested Stay Sharp!. Posted Alter v dested Alter True. "
    "Posted Boush dested Boushh. Tk-forty-nine crossed out, replaced by handwritten (Han) dested Han. Posted Luke, JK dested Luke Skywalker, Jedi Knight. "
    "Posted lets go left dested Let's Go Left. Combined Attack (Premiere Limited) is on wiki, not in GEMP DB. Main 59 per sheet (not 60). No shields listed."
)
DS_NOTE = (
    "Posted Imperial entanglements/put it where the sun can't shine dested Imperial Entanglements / No One To Stop Us This Time. "
    "Posted Tatooine system dested Tatooine. Handwritten Devastator added. Posted Tatooine: mos eisly / market place / jundland waste / wattos junkyard dested "
    "Tatooine: Mos Eisley / Marketplace / Jundland Wastes / Watto's Junkyard. Posted Spaceport: docking bay dested Spaceport Docking Bay. "
    "Handwritten Tempest scout 1 added; typed 5x Tempest scout corrected to 4x. Posted Baron Sontir Fel dested Baron Soontir Fel; "
    "handwritten +Sergeant Barich, Sergeant Elsek added. Posted Admiral Piet dested Admiral Piett. "
    "Posted Darth Vader, Dark lord of the sith dested Darth Vader, Dark Lord Of The Sith. Typed 3x Sneak attack v corrected to 2x. "
    "Posted dark maneuvers combo dested Dark Maneuvers & Tallon Roll. Posted Masterfull move combo dested Masterful Move & Endor Occupation. "
    "Posted watch your back dested Watch Your Back!. Handwritten Alert my star destroyer added. "
    "Last line '!dos manglende doctor Johnny!' ('manglende' is Danish for 'missing') not transcribed as a card; reviewer may read it as a joke name for "
    "Dr. Evazan & Ponda Baba, which would make 60. Main 59 per sheet. No shields listed."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("A New Secret Base", True),
    n("Superficial Damage"),
    n("Blue Squadron B-wing", qty=3),
    n("Green Leader In Green Squadron 1"),
    n("Red Squadron X-wing", qty=2),
    n("Obi-Wan In Radiant VII"),
    n("Red 8", True),
    n("Gold Leader In Gold 1", True),
    n("Wedge In Red Squadron 1"),
    n("Han, Chewie, And The Falcon"),
    n("X-wing Laser Cannon", qty=2),
    n("Proton Torpedoes", qty=4),
    n("Intruder Missile"),
    n("Concussion Missiles"),
    n("Rebel Barrier", qty=2),
    n("Power Pivot"),
    n("Rebel Artillery"),
    n("All Wings Report In", qty=2),
    n("Steady Aim"),
    n("Stay Sharp!"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Control & Tunnel Vision"),
    n("Slight Weapons Malfunction"),
    n("Rapid Fire", qty=2),
    n("We Wish To Board At Once"),
    n("Combined Attack"),
    n("Alter", True),
    n("Hit And Run"),
    n("Out Of Commission & Transmission Terminated"),
    n("Boushh"),
    n("Han"),
    n("Luke Skywalker, Jedi Knight"),
    n("Concentrate All Fire", qty=2),
    n("Let's Go Left", qty=2),
    n("Roche"),
    n("Tatooine"),
    n("Anoat", True),
    n("Naboo"),
    n("Nar Shaddaa"),
    n("Kiffex"),
    n("Slayn & Korpil Facilities"),
    n("Projection Of A Skywalker", qty=2),
    n("They Win This Round"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Tatooine"),
    n("Devastator"),
    n("Tatooine: Desert Heart"),
    n("Prepared Defenses"),
    n("Aratech Corporation", True),
    n("Endor Shield", True),
    n("Combat Response"),
    n("Tatooine: Mos Eisley"),
    n("Tatooine: Marketplace"),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Mos Espa"),
    n("Spaceport Docking Bay"),
    n("Blizzard Scout 1", True),
    n("Tempest Scout 1"),
    n("Tempest Scout 3", True),
    n("Tempest Scout 4"),
    n("Tempest Scout 5"),
    n("Tempest Scout 6"),
    n("Tempest Scout", qty=4),
    n("Blizzard 4"),
    n("Blizzard 2", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Arica", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Piett"),
    n("DS-61-2"),
    n("DS-61-5"),
    n("Baron Soontir Fel"),
    n("Sergeant Barich"),
    n("Sergeant Elsek"),
    n("Saber 1"),
    n("Black 5"),
    n("Black 2", True),
    n("Sneak Attack", True, qty=2),
    n("All Power To Weapons", qty=3),
    n("Watch Your Back!", qty=2),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Force Push", True),
    n("Trample"),
    n("Control & Set For Stun"),
    n("Tatooine Occupation", qty=2),
    n("Imperial Decree", True),
    n("After Her!"),
    n("Alert My Star Destroyer!"),
    n("Battle Deployment"),
]
DS_SHIELDS = []
DS_ADD = []
