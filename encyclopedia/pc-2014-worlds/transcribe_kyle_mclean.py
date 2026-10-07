#!/usr/bin/env python3
"""Kyle McLean, 2014 Worlds Day 2. Typed Holotable dump plus margin handwriting.

Light worlds light WYS: extract/day2/d2p2_p19.png.
Dark worlds dark Hunt Down: extract/day2/d2p2_p20.png.
Handwritten qty (x2) on three Light cards; three Light names added at the foot;
Dark Stunning Leader → Search And Destroy; Accuser → Bossk In Hound's Tooth;
shield lists in the right margin.
"""
from __future__ import annotations

PLAYER = "Kyle McLean"
USERNAME = ""
KIND = "type_groups"

# --- Light WYS ---
LS_DECK_NAME = "worlds light"
LS_SIDE = "Light"
LS_SCAN = "extract/day2/d2p2_p19.png"
LS_PDF = "2014 Worlds Day 2 Part 2.pdf"
LS_PDF_PAGE = 19
LS_STARTING = ("Watch Your Step / This Place Can Be A Little Rough", False)

LS_GROUPS = [
    ("Objective", [
        (1, "Watch Your Step / This Place Can Be A Little Rough", False),
    ]),
    ("Character", [
        (1, "Wedge Antilles", False),
        (1, "Theron Nett", False),
        (1, "Threepio With His Parts Showing", False),
        (1, "Mirax Terrik", False),
        (1, "Dash Rendar", False),
        (1, "LE-BO2D9 (Leebo)", False),
        (2, "Chewie, Enraged (V)", True),
        (1, "Melas (V)", True),
        (3, "Han Solo (V)", True),
        (1, "Booster In Pulsar Skate", False),
        (2, "Palace Raider (V)", True),
        (2, "Luke With Lightsaber", False),
    ]),
    ("Defensive shield", [
        (1, "Only Jedi Carry That Weapon", False),
        (1, "He Can Go About His Business", False),
        (1, "Battle Plan", False),
        (1, "Aim High", False),
        (1, "Chasm", False),
        (1, "Another Pathetic Lifeform", False),  # margin "APL"
        (1, "Jabba's Prize", False),
        (1, "Affect Mind", False),
        (1, "The Professor", False),
        (1, "Ultimatum", False),
        (1, "Your Insight Serves You Well", False),
        (1, "A Tragedy Has Occurred", False),
        (1, "Don't Do That Again", False),
        (1, "Let's Keep A Little Optimism Here", False),
        (1, "Simple Tricks And Nonsense", False),
    ]),
    ("Effect", [
        (1, "Anger, Fear, Aggression (V)", True),
        (1, "Squadron Assignments", False),
        (1, "Menace Fades", False),
        (2, "Projection Of A Skywalker", False),  # (x2) handwritten
        (1, "Sai'torr Kal Fas (V)", True),
        (1, "Superficial Damage (V)", True),
        (1, "Eject! Eject! (V)", True),
        (1, "Han's Back (V)", True),
    ]),
    ("Interrupt", [
        (1, "Control & Tunnel Vision", False),  # Tunnel Vision handwritten onto Control
        (1, "Heading For The Medical Frigate", False),
        (1, "Life Debt", False),
        (1, "Houjix & Out Of Nowhere", False),
        (1, "The Signal", False),
        (1, "Blast The Door, Kid!", False),
        (1, "Fallen Portal", False),
        (2, "Sorry About The Mess", False),
        (1, "The Bith Shuffle & Desperate Reach", False),
        (1, "Put That Down", False),
        (1, "Hyper Escape", False),
        (2, "Kessel Run", False),
        (2, "I Don't Need Their Scum, Either (V)", True),  # (x2) handwritten
        (2, "Han's Dice (V)", True),
        (1, "Wookiee Strangle", False),  # handwritten
        (1, "Out Of Commission", False),  # handwritten; cramped 'Commission'
        (1, "Rebel Barrier", False),  # handwritten
    ]),
    ("Location", [
        (1, "Kessel", False),
        (1, "Corellia", False),
        (1, "Tatooine: Docking Bay 94", False),
        (1, "Tatooine: Cantina", False),
        (1, "Tatooine", False),
    ]),
    ("Starship", [
        (1, "Red 10", False),
        (1, "Red Squadron 1", False),
        (1, "Outrider", False),
        (1, "Lando In Millennium Falcon", False),
    ]),
    ("Vehicle", [
        (2, "Racing Skiff", False),
    ]),
    ("Weapon", [
        (2, "X-wing Laser Cannon", False),  # (x2) handwritten
        (1, "Chewbacca's Bowcaster", False),
        (1, "Han's Heavy Blaster Pistol (V)", True),
    ]),
]

LS_NOTES = (
    "Typed Holotable 'worlds light'; signature Kyle McLean. "
    "Control has handwritten 'Tunnel Vision' → Control & Tunnel Vision. "
    "Handwritten (x2) on X-wing Laser Cannon, Projection Of A Skywalker, "
    "I Don't Need Their Scum, Either (V). Foot adds: Wookiee Strangle, "
    "Out Of Commission (cramped; could be misread), Rebel Barrier. "
    "Typed list is 60 before the three foot adds (63 with them); do not invent outs. "
    "Palace Raider is a character (x2). Margin 'D shields' 15 names; APL read as "
    "Another Pathetic Lifeform. No (V) marks on the handwritten shield list."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

# --- Dark Hunt Down ---
DS_DECK_NAME = "worlds dark"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2/d2p2_p20.png"
DS_PDF = "2014 Worlds Day 2 Part 2.pdf"
DS_PDF_PAGE = 20
DS_STARTING = (
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
    False,
)

DS_GROUPS = [
    ("Objective", [
        (1, "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", False),
    ]),
    ("Character", [
        (1, "Arica (V)", True),
        (2, "Dr. Evazan", False),
        (1, "Darth Vader, Dark Lord Of The Sith", False),
        (1, "Darth Maul, Young Apprentice", False),
        (1, "ISB Sector Commander", False),
        (1, "Galen Marek, Starkiller", False),  # sheet (AI)
        (1, "Count Dooku", False),
        (1, "Grand Moff Tarkin (V)", True),  # (V) handwritten
        (1, "Emperor Palpatine", False),
        (2, "Lord Vader", False),
        (1, "Bane Malar", False),  # handwritten at foot
    ]),
    ("Defensive shield", [
        (1, "We'll Let Fate-a Decide, Huh?", False),
        (1, "Death Star Sentry", False),
        (1, "I Find Your Lack Of Faith Disturbing", False),
        (1, "Weapon Of A Sith", False),
        (1, "Fanfare", False),
        (1, "Leave Them To Me", False),
        (1, "Imperial Detention", False),
        (1, "Firepower", False),
        (1, "Battle Order", False),
        (1, "Do They Have A Code Clearance?", False),
        (1, "A Useless Gesture", False),
        (1, "Secret Plans", False),
        (1, "Allegations Of Corruption", False),
        (1, "Abyss", False),
        (1, "Come Here You Big Coward", False),
    ]),
    ("Effect", [
        (1, "Knowledge And Defense (V)", True),
        (2, "Disarmed", False),
        (1, "Search And Destroy", False),  # Stunning Leader crossed
        (1, "Imperial Decree", False),
        (1, "You Cannot Hide Forever & Mobilization Points", False),
        (1, "Expand The Empire", False),
        (1, "Blaster Rack (V)", True),
        (1, "Wipe Them Out, All Of Them (V)", True),
        (1, "Responsibility Of Command", False),
        (1, "The Phantom Menace", False),
        (1, "Image Of The Dark Lord", False),
        (2, "Visage Of The Emperor", False),
        (1, "Prepared Defenses", False),
    ]),
    ("Interrupt", [
        (2, "Force Lightning", False),
        (2, "Voyeur (V)", True),
        (2, "Control", False),
        (2, "Close Call", False),  # (x2) handwritten
        (2, "Imperial Barrier", False),
        (2, "Twi'lek Advisor", False),
        (3, "Fear (V)", True),
    ]),
    ("Location", [
        (1, "Executor: Meditation Chamber (V)", True),  # (V) handwritten
        (1, "Executor: Holotheatre", False),
        (1, "Hoth: Defensive Perimeter (3rd Marker)", False),
        (1, "Hoth: Echo Command Center (War Room)", False),
        (1, "Rendili", False),
    ]),
    ("Starship", [
        (1, "Dominator", False),
        (1, "Victory", False),
        (1, "Zuckuss In Mist Hunter", False),
        (1, "Boba Fett In Slave I (V)", True),
        (1, "Bossk In Hound's Tooth", False),  # Accuser crossed
    ]),
    ("Vehicle", [
        (1, "Blizzard 4", False),
    ]),
    ("Weapon", [
        (1, "Mara Jade's Lightsaber (V)", True),
        (1, "Galen's Lightsaber, Vader's Gift", False),
        (1, "Maul's Double-Bladed Lightsaber", False),
        (1, "Vader's Lightsaber", False),
        (1, "Dooku's Lightsaber", False),
        (1, "Darth Vader's Lightsaber", False),
    ]),
]

DS_NOTES = (
    "Typed Holotable 'worlds dark'; signature Kyle McLean. "
    "Stunning Leader crossed; handwritten 'Search & Destroy'. "
    "Accuser crossed; handwritten 'Bossk in Hound's Tooth'. "
    "Handwritten (V) on Executor: Meditation Chamber and Grand Moff Tarkin. "
    "Close Call (x2) handwritten 2. Foot add Bane Malar (signature-like; treated as a card). "
    "Typed list with replacements is 60 before Bane Malar (61 with it); do not invent a cut. "
    "Margin 'Defensive Shields' 15 names, no (V) ticks. "
    "Galen Marek marked (AI)."
)
DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []

SIDE = None
GROUPS = None
SCAN = LS_SCAN
PDF = LS_PDF
STARTING = LS_STARTING
NOTES = LS_NOTES
UNREAD = LS_UNREAD
NO_DEST = LS_NO_DEST

_SKIP_HEADINGS = {"Defensive shield", "Hidden Fortress"}


def _qty(groups: list) -> int:
    return sum(
        q
        for heading, cards in groups
        if heading not in _SKIP_HEADINGS
        for q, _n, _v in cards
    )


def _shields(groups: list) -> int:
    return sum(
        q
        for heading, cards in groups
        if heading == "Defensive shield"
        for q, _n, _v in cards
    )


if __name__ == "__main__":
    print(
        f"transcribe_kyle_mclean.py  {PLAYER}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}"
    )
