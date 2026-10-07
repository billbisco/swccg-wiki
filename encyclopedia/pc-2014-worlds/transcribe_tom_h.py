#!/usr/bin/env python3
"""Day 2 Xerox transcription: Tom H (no surname on the sheet).

Source scans: extract/day2/d2p2_p09.png (Dark, Same as last year) and
extract/day2/d2p2_p10.png (Light, 2 cards diff from last year). 2010 form.
Light/Dark boxes unchecked; side from the cards. ROPS / Bespin and Watch
Your Step. (V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Tom H"
USERNAME = ""
PDF = "2014 Worlds Day 2 Part 2.pdf"


# --- Dark: d2p2_p09.png, 2010 form. Light/Dark unchecked. ---

DS_DECK_NAME = "Same as last year"
DS_SIDE = "Dark"
DS_FORM = "xerox_2010"
DS_SCAN = "extract/day2/d2p2_p09.png"
DS_PDF_PAGE = 9
DS_STARTING = ("Ralltiir Operations / In The Hands Of The Empire", False)

DS_RESERVE = [
    n("Ralltiir Operations / In The Hands Of The Empire"),  # 1  ROPS
    n("Ralltiir"),  # 2
    n("Prepared Defenses", True),  # 3
    n("Insignificant Rebellion", True),  # 4
    n("First Strike", True),  # 5  First Prize / First Strike
    n("Imperial Justice", True),  # 6
    n("He Hasn't Come Back Yet"),  # 7
    n("Blizzard 4", True),  # 8
    n("Victory"),  # 9
    n("Blizzard 1", True),  # 10
    n("Tyrant"),  # 11
    n("A Dark Time For The Rebellion", True),  # 12
    n("A Dark Time For The Rebellion"),  # 13  ditto; (V) empty
    n("Imbalance & Kintan Strider"),  # 14  6th combo
    n("Ralltiir: Spaceport Financial District"),  # 15  Bespin/Ralltiir Financial District
    n("Jump Down", True),  # 16
    n("Jump Down"),  # 17  ditto
    n("Spaceport Docking Bay"),  # 18  Spaceport DB
    n("Arcona"),  # 19  as written; Premiere Arcona is Light
    n("Trample"),  # 20
    n("Operational As Planned", True),  # 21
    n("Protocol Failure"),  # 22
    n("Outflank", True),  # 23
    n("Kashyyyk"),  # 24
    n("Ghhhk & Those Rebels Won't Escape Us", True),  # 25  Ghhhk combo
    n("Blizzard 2", True),  # 26
    n("Arica"),  # 27
    n("Devastator", True),  # 28
    n("Colonel Davod Jon"),  # 29
    n("Grand Moff Tarkin", True),  # 30
    n("Grand Admiral Thrawn"),  # 31  Thrawn
    n("The Emperor's Reach"),  # 32  Reach
    n("Something Special Planned For Them", True),  # 33  Something Special
    n("Defensive Fire", True),  # 34  Defensive
    n("Commander Igar"),  # 35  Igar
    n("Close Call", True),  # 36
    n("Close Call"),  # 37  ditto; (V) empty
    n("Why Didn't You Tell Me?", True),  # 38
    n("4-LOM"),  # 39
    n("Cold Feet", True),  # 40
    n("Imperial Command"),  # 41
    n("Imperial Command"),  # 42  ditto
    n("Street"),  # 43  Street; see NOTES
    n("General Veers", True),  # 44
    n("Emperor Palpatine"),  # 45
    n("Emperor Palpatine"),  # 46  ditto
    n("Admiral Piett", True),  # 47
    n("Weapon Levitation"),  # 48  Weapon Lev
    n("Victory"),  # 49  Victor Destroyer
    n("Endor"),  # 50
    n("Prefect's Office"),  # 51  Prefect's Office; see NOTES
    n("Sim Aloo", True),  # 52
    n("Imperial Barrier"),  # 53  Barrier
    n("Grand Admiral Thrawn"),  # 54  Thrawn
    n(None),  # 55  Tumbler combo; unread
    n("Control & Set For Stun"),  # 56  Control combo
    n(None),  # 57  short scrawl
    n("Empire's New Order"),  # 58
    n("Knowledge And Defense"),  # 59  KGP
    n("Endor Shield", True),  # 60
]

DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),  # 1  We'll Let Fate Decide
    n("Resistance"),  # 2
    n("Do They Have A Code Clearance?"),  # 3  Code Clearance
    n("Fanfare", True),  # 4
    n("Secret Plans"),  # 5
    n("There Is No Try"),  # 6  TNT
    n("You Cannot Hide Forever", True),  # 7  YCHF
    n("Come Here You Big Coward"),  # 8  Coward
    n("Imperial Detention"),  # 9  Detention
    n("Battle Order"),  # 10
    n("A Useless Gesture"),  # 11  Grabber / Gesture
    n("Firepower", True),  # 12
]

DS_ADD = [
    n("Abyss", True),  # 1
    n("A Useless Gesture", True),  # 2  A Gesture Gesture
    n("Death Star Sentry", True),  # 3  Sentry
]

DS_UNREAD = [55, 57]
DS_NO_DEST: list[str] = []


# --- Light: d2p2_p10.png, 2010 form. Light/Dark unchecked. ---

LS_DECK_NAME = "2 cards diff from last year"
LS_SIDE = "Light"
LS_FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p2_p10.png"
LS_PDF_PAGE = 10
LS_STARTING = ("Watch Your Step / This Place Can Be A Little Rough", True)

LS_RESERVE = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),  # 1  WYS
    n("Heading For The Medical Frigate"),  # 2  HFTMF
    n("Fallen Portal", True),  # 3  Fallen
    n("Captain Han Solo"),  # 4  Captain Han
    n("Rebel Leadership", True),  # 5  Leadership
    n("City In The Clouds"),  # 6  City
    n(None, True),  # 7  Not Pay (V); unread
    n("Cloud City: Casino", True),  # 8  CFC
    n(None),  # 9  IAD & Kim Host; unread
    n("Leia's Blaster Rifle"),  # 10
    n("Leia's Blaster Rifle"),  # 11  Leia BR
    n("Leia's Blaster Rifle"),  # 12  ditto
    n(None),  # 13  Pack GR; unread
    n("Cloud City: Downtown Plaza"),  # 14  Street
    n("Sense"),  # 15
    n("Wedge Antilles, Red Squadron Leader"),  # 16  Wedge RSL
    n("Wedge Antilles, Red Squadron Leader"),  # 17  ditto
    n("Aunt Beru"),  # 18  Aunt ROS
    n("Aunt Beru"),  # 19  ditto
    n("Sergeant Bruckman"),  # 20  Bruckman
    n("Antilles Maneuver", True),  # 21
    n("Antilles Maneuver"),  # 22  ditto; (V) empty
    n("Seeking An Audience", True),  # 23  Seeking
    n("Antilles Maneuver & Rebel Reinforcements"),  # 24  Antilles combo
    n("Red 7"),  # 25  Ube in Red 7
    n("Luke Skywalker, Jedi Knight"),  # 26  LBJK
    n("Luke Skywalker, Jedi Knight"),  # 27  ditto
    n("Rebel Barrier"),  # 28  Barrier
    n("Rebel Barrier"),  # 29  ditto
    n("Torture", True),  # 30  Torture (V); Dark title on LS list
    n("Houjix & Out Of Nowhere"),  # 31  Houjix combo
    n("Melas"),  # 32  Moray
    n("Lady Luck"),  # 33  Ladies UT
    n("Yoda"),  # 34  prior title crossed, Yoda remains
    n("General Crix Madine"),  # 35  General Crix
    n("Spaceport Docking Bay"),  # 36  Spaceport DB
    n("Corellia"),  # 37
    n("Ralltiir", True),  # 38  Ralltiir
    n("You've Got A Lot Of Guts Coming Here"),  # 39  Guts
    n("Evacuation Control", True),  # 40  Evac Control
    n("Imperial Atrocity", True),  # 41
    n("Mace Windu"),  # 42  Mace Windu, MOTS
    n("Jaina Solo"),  # 43
    n("Let The Wookiee Win", True),  # 44  LTWW
    n("Let The Wookiee Win"),  # 45  ditto; (V) empty
    n("Desperate Reach", True),  # 46
    n("Fall Back!", True),  # 47  Retreat
    n("Fall Back!"),  # 48  ditto; (V) empty
    n(None, True),  # 49  WQA (V); unread 3-of
    n(None),  # 50  ditto WQA
    n(None),  # 51  ditto WQA
    n("Power Pivot"),  # 52  Power
    n("Path Of Least Resistance", True),  # 53  Path Radar
    n("Landing Claw", True),  # 54  Landing
    n("Melas"),  # 55  Pales
    n("Lando Calrissian, Scoundrel"),  # 56  Lando's Pride
    n("Lady Luck"),  # 57  Lady Luck (unique listed twice)
    n("Han, Chewie, And The Falcon", True),  # 58  An Chewie
    n("Home One: Docking Bay"),  # 59  H1 DB
    n("Anger, Fear, Aggression", True),  # 60  AFA
]

LS_SHIELDS = [
    n("Jabba's Prize", True),  # 1
    n("Planetary Defenses", True),  # 2
    n("Do, Or Do Not"),  # 3
    n("Don't Do That Again", True),  # 4  DPTA
    n("Let's Keep A Little Optimism Here", True),  # 5
    n("Yavin Sentry", True),  # 6
    n("Ultimatum"),  # 7
    n("Weapons Display", True),  # 8
    n("He Can Go About His Business", True),  # 9
    n("Chasm", True),  # 10
    n("A Tragedy Has Occurred"),  # 11
    n("The Professor", True),  # 12
]

LS_ADD = [
    n("Your Insight Serves You Well", True),  # 1  YISYW
    n("Simple Tricks And Nonsense"),  # 2  Simple Tricks
    n("Aim High", True),  # 3
]

LS_UNREAD = [7, 9, 13, 49, 50, 51]
LS_NO_DEST: list[str] = []


NOTES = """
Tom H (no surname on either sheet), 2014 Worlds Day 2, 2010 form.
Light/Dark unchecked on both pages; side from the cards. Username blank.

Dark d2p2_p09.png Same as last year. ROPS = Ralltiir Operations / In The
Hands Of The Empire, with Bespin/Ralltiir sites and walkers.
Light d2p2_p10.png 2 cards diff from last year. WYS.

DS uncertain:
- 5 First Prize (V) -> First Strike (set 7 Dark); Prize/Strike scramble.
- 14 6th combo -> Imbalance & Kintan Strider.
- 16-17 Jump Down as written (no GEMP title hit in pre-check).
- 19 Arcona as written (Premiere Arcona is Light).
- 32 Reach -> The Emperor's Reach.
- 43 Street as written (likely a Cloud City / Ralltiir site).
- 49 Victor Destroyer -> second Victory.
- 51 Prefect's Office as written.
- 55 Tumbler combo unread (not Imbalance / Ghhhk / Control, already listed).
- 57 short scrawl unread.
- 59 KGP -> Knowledge And Defense (KAD).
- Shield 11 Gesture/Grabber -> A Useless Gesture.

LS uncertain:
- 3 Fallen (V) -> Fallen Portal (DSII site).
- 6 City -> City In The Clouds (CC Effect, not the later objective).
- 7 Not Pay (V) unread (not I Know / Guts; Guts is 39).
- 8 CFC (V) -> Cloud City: Casino.
- 9 IAD & Kim Host unread.
- 13 Pack GR unread.
- 14 Street -> Cloud City: Downtown Plaza.
- 18-19 Aunt ROS -> Aunt Beru.
- 25 Ube in Red 7 -> Red 7.
- 26 LBJK -> Luke Skywalker, Jedi Knight.
- 30 Torture (V): Dark interrupt title on a Light list; kept as written.
- 32 Moray -> Melas. 55 Pales -> Melas.
- 34 crossed title then Yoda.
- 47 Retreat (V) -> Fall Back!.
- 49-51 WQA 3-of unread (not AFM / ICBW / Sense).
- 56 Lando's Pride -> Lando Calrissian, Scoundrel.
- 58 An Chewie (V) -> Han, Chewie, And The Falcon.
""".strip()


if __name__ == "__main__":
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
    print("file", __file__)
    print("player", PLAYER, "username", USERNAME or "-")
    print("DS", DS_DECK_NAME, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
    print("LS", LS_DECK_NAME, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
