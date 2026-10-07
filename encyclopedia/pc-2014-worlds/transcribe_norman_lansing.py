#!/usr/bin/env python3
"""Day 2 Xerox transcription: Norman Lansing (Anastar Reaver).

Source scans: extract/day2/d2p2_p05.png (Dark, Here comes the Scum) and
extract/day2/d2p2_p06.png (Light, There Is Good In Him). 2010 form,
Worlds Day 2 08/23/14. Typed/printed onto the Xerox. Court of the Vile
Gangster is the Dark start but is not among the 60 numbered lines.
(V) follows the sheet checkbox.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Norman Lansing"
USERNAME = "Anastar Reaver"
PDF = "2014 Worlds Day 2 Part 2.pdf"


# --- Dark: d2p2_p05.png, 2010 form. DARK checked. ---

DS_DECK_NAME = "Here comes the Scum"
DS_SIDE = "Dark"
DS_FORM = "xerox_2010"
DS_SCAN = "extract/day2/d2p2_p05.png"
DS_PDF_PAGE = 5
DS_STARTING = ("Court Of The Vile Gangster / I Shall Enjoy Watching You Die", False)

DS_RESERVE = [
    n("Tatooine"),  # 1
    n("Combat Readiness", True),  # 2
    n("Power Of The Hutt"),  # 3
    n("Desilijic Tattoo", True),  # 4
    n("No Bargain"),  # 5
    n("Tatooine: Jabba's Palace"),  # 6
    n("4-LOM With Concussion Rifle"),  # 7
    n("Bane Malar", True),  # 8
    n("Bib Fortuna", True),  # 9
    n("Boba Fett", True),  # 10
    n("Boba Fett With Blaster Rifle"),  # 11
    n("Boba Fett's Blaster Rifle", True),  # 12
    n("Bossk With Mortar Gun"),  # 13
    n("Darth Maul With Lightsaber"),  # 14
    n("Dengar With Blaster Carbine"),  # 15
    n("Dr. Evazan & Ponda Baba"),  # 16
    n("EV-9D9"),  # 17
    n("Emperor Palpatine"),  # 18
    n("Gallid"),  # 19
    n("Guri"),  # 20
    n("IG-88 With Riot Gun"),  # 21
    n("Jabba The Hutt", True),  # 22
    n("Jabba The Hutt", True),  # 23
    n("Jodo Kast"),  # 24
    n("Mara Jade, The Emperor's Hand"),  # 25
    n("Niado Duegad"),  # 26
    n("Prince Xizor"),  # 27
    n("Snoova"),  # 28
    n("U-3PO (Yoo-Threepio)"),  # 29  U-3PO
    n("Bad Feeling Have I"),  # 30
    n("Bounty"),  # 31
    n("Bounty"),  # 32
    n("Expand The Empire"),  # 33
    n("Hutt Bounty", True),  # 34
    n("Hutt Influence"),  # 35
    n("Jabba's Influence", True),  # 36
    n("Knowledge And Defense", True),  # 37
    n("Scum And Villainy"),  # 38
    n("Tatooine Occupation"),  # 39
    n("Wrong Turn"),  # 40
    n("Force Lightning"),  # 41
    n("Force Lightning"),  # 42
    n("Hidden Weapons"),  # 43
    n("Imperial Barrier"),  # 44
    n("Imperial Barrier"),  # 45
    n("Twi'lek Advisor"),  # 46
    n("Twi'lek Advisor"),  # 47
    n("Jabba's Palace: Audience Chamber"),  # 48
    n("Jabba's Palace: Droid Workshop"),  # 49
    n("Jabba's Palace: Dungeon"),  # 50
    n("Jabba's Palace: Entrance Cavern"),  # 51
    n("Jabba's Palace: Lower Passages"),  # 52
    n("Dengar In Punishing One"),  # 53
    n("Jabba's Space Cruiser", True),  # 54
    n("Maul's Sith Infiltrator"),  # 55
    n("Zuckuss In Mist Hunter"),  # 56
    n("All Wrapped Up", True),  # 57
    n("Vibro-Ax"),  # 58
    n("Feltipern Trevagg's Stun Rifle", True),  # 59
    n("Mara Jade's Lightsaber", True),  # 60
]

DS_SHIELDS = [
    n("Abyss", True),  # 1
    n("Battle Order", True),  # 2
    n("Come Here You Big Coward", True),  # 3  Come Here You Big Coward!
    n("Firepower", True),  # 4
    n("Imperial Detention", True),  # 5
    n("Leave Them To Me", True),  # 6
    n("Resistance", True),  # 7
    n("Secret Plans", True),  # 8
    n("There Is No Try", True),  # 9
    n("You Cannot Hide Forever", True),  # 10
]

DS_ADD = []

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []


# --- Light: d2p2_p06.png, 2010 form. LIGHT checked. ---

LS_DECK_NAME = "There Is Good In Him"
LS_SIDE = "Light"
LS_FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p2_p06.png"
LS_PDF_PAGE = 6
LS_STARTING = ("There Is Good In Him / I Can Save Him", False)

LS_RESERVE = [
    n("There Is Good In Him / I Can Save Him"),  # 1
    n("Endor: Chief Chirpa's Hut"),  # 2
    n("Luke Skywalker, Jedi Knight"),  # 3
    n("Luke's Lightsaber"),  # 4
    n("Endor: Landing Platform (Docking Bay)"),  # 5
    n("I Feel The Conflict"),  # 6
    n("Heading For The Medical Frigate"),  # 7
    n("Squadron Assignments"),  # 8
    n("Strike Planning"),  # 9
    n("Wokling", True),  # 10
    n("Admiral Ackbar"),  # 11
    n("ASP-707"),  # 12
    n("Chewbacca, Protector"),  # 13
    n("Firin Morett"),  # 14
    n("First Officer Thaneespi"),  # 15
    n("General Calrissian"),  # 16
    n("Green Leader"),  # 17
    n("Han With Heavy Blaster Pistol"),  # 18
    n("Han With Heavy Blaster Pistol"),  # 19
    n("Leia With Blaster Rifle"),  # 20
    n("Nien Nunb"),  # 21
    n("Obi-Wan With Lightsaber"),  # 22
    n("Senator Mon Mothma", True),  # 23
    n("Ten Numb"),  # 24
    n("Tycho Celchu"),  # 25
    n("Wedge Antilles, Red Squadron Leader"),  # 26
    n("Wicket"),  # 27
    n("Haven"),  # 28
    n("Legendary Starfighter"),  # 29
    n("Legendary Starfighter"),  # 30
    n("Legendary Starfighter"),  # 31
    n("Menace Fades"),  # 32
    n("Order To Engage"),  # 33
    n("S-foils"),  # 34
    n("Special Modifications"),  # 35
    n("Anger, Fear, Aggression"),  # 36
    n("I Know"),  # 37
    n("Protector"),  # 38
    n("Out Of Nowhere"),  # 39
    n("Out Of Nowhere"),  # 40
    n("Out Of Nowhere"),  # 41
    n("Home One: Docking Bay"),  # 42
    n("Home One: War Room"),  # 43
    n("Kessel"),  # 44
    n("Spaceport Docking Bay"),  # 45
    n("Sullust"),  # 46  printed Suliust
    n("Blue Squadron 5"),  # 47
    n("Home One"),  # 48
    n("Gold Squadron 1"),  # 49
    n("Green Squadron 1"),  # 50
    n("Green Squadron 3"),  # 51
    n("Liberty"),  # 52
    n("Red Squadron 1"),  # 53
    n("I'll Take The Leader"),  # 54
    n("Ewok Catapult"),  # 55
    n("Ewok Catapult"),  # 56
    n("X-wing Laser Cannon"),  # 57
    n("Y-wing Laser Cannon"),  # 58
    n("Red Squadron 4"),  # 59
    n("Derek 'Hobbie' Klivian"),  # 60
]

LS_SHIELDS = [
    n("Battle Plan"),  # 1
    n("Yavin Sentry"),  # 2
    n("Affect Mind"),  # 3
    n("Chasm"),  # 4
    n("Let's Keep A Little Optimism Here"),  # 5
    n("Ounee Ta"),  # 6
    n("Your Insight Serves You Well"),  # 7
    n("Simple Tricks And Nonsense"),  # 8
    n("Traffic Control"),  # 9
    n("Do, Or Do Not"),  # 10
    n("Weapons Display"),  # 11
    n("Aim High"),  # 12
]

LS_ADD = []

LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []


NOTES = """
Norman Lansing / Anastar Reaver, 2014 Worlds Day 2 08/23/14, 2010 form.
Email [redacted] on the sheet. Typed/printed list.
Dark d2p2_p05.png Here comes the Scum (DARK checked). Court / Jabba.
Light d2p2_p06.png There Is Good In Him (LIGHT checked). Username AnastarReaver
(no space) on the Light sheet.

DS notes:
- Objective Court Of The Vile Gangster / I Shall Enjoy Watching You Die is
  not among the 60 numbered lines (line 1 is Tatooine). STARTING holds it.
- 19 Gallid as printed.
- 22-23 two Jabba The Hutt (V); unique listed twice as written.
- 29 U-3PO -> U-3PO (Yoo-Threepio).
- 58 Vibro-Ax on Dark as printed (Premiere/JP weapon).
- All 10 filled shield (V) boxes are checked; followed.

LS notes:
- 46 printed Suliust -> Sullust.
- 10 Wokling (V), 23 Senator Mon Mothma (V) are the only reserve (V) checks.
- Shield 3 Affect Mind and shield 10 Do, Or Do Not sit in the shields block
  as printed (Do, Or Do Not is often Additional).
""".strip()


if __name__ == "__main__":
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
    print("file", __file__)
    print("player", PLAYER, "username", USERNAME)
    print("DS", DS_DECK_NAME, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
    print("LS", LS_DECK_NAME, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
