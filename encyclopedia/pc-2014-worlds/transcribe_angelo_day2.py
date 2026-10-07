#!/usr/bin/env python3
"""Day 2 Xerox transcription: Angelo Consoli (DrevithShadow).

Source scans: extract/day2/d2p2_p17.png (Dark, Slavers) and
extract/day2/d2p2_p18.png (Light, QMC). 2013 form, Worlds '14 08/23/14.
(V) follows the sheet checkbox. Dittos expanded.
Day 2 60 is not the Day 3 ASM / WHT(v) list.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Angelo Consoli"
USERNAME = "DrevithShadow"
FORM = "xerox_2013"
PDF = "2014 Worlds Day 2 Part 2.pdf"

ANGELO_D2_PLAYER = PLAYER
ANGELO_D2_USERNAME = USERNAME
ANGELO_D2_DS_DECK_NAME = "Slavers"
ANGELO_D2_LS_DECK_NAME = "QMC"


# --- Dark: d2p2_p17.png. DARK checked. Wookiee Slaving Operations. ---

ANGELO_D2_DS_SCAN = "extract/day2/d2p2_p17.png"
ANGELO_D2_DS_PDF_PAGE = 17
ANGELO_D2_DS_SIDE = "Dark"
ANGELO_D2_DS_STARTING = n("Wookiee Slaving Operation / Indentured To The Empire")

ANGELO_D2_DS_RESERVE = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),  # 1  Slaving Obj.
    n("Take Evasive Action"),  # 2
    n("Sonic Bombardment", True),  # 3
    n("Sonic Bombardment", True),  # 4
    n("Sonic Bombardment", True),  # 5
    n("IG-88 With Riot Gun"),  # 6  IG-88 w/Gun
    n("Kashyyyk"),  # 7
    n("Kashyyyk: Slaving Camp Headquarters"),  # 8
    n("Mercenary Slavers"),  # 9
    n("Power Of The Hutt"),  # 10
    n("Jabba's Haven"),  # 11
    n("Abyssin Ornament"),  # 12
    n("Prince Xizor"),  # 13  Xizor
    n("Jango Fett"),  # 14
    n("Jabba's Sail Barge: Passenger Deck"),  # 15  PD
    n("Outer Rim Scout"),  # 16  ORS
    n("Outer Rim Scout"),  # 17
    n("Outer Rim Scout"),  # 18
    n("Outer Rim Scout"),  # 19
    n("Hutt Bounty", True),  # 20
    n("Ephant Mon"),  # 21
    n("Slave I, Symbol Of Fear"),  # 22  Slave I, SOF
    n("Monnok"),  # 23
    n("Boba Fett, Prepared Hunter"),  # 24  Boba, PH
    n("Dengar With Blaster Carbine", True),  # 25  Dengar w/Gun
    n("Masterful Move"),  # 26
    n("Masterful Move"),  # 27
    n("Scum And Villainy"),  # 28  S+V
    n("Scum And Villainy"),  # 29
    n("Nal Hutta"),  # 30
    n("Jabba's Sail Barge"),  # 31  Jabba's SB
    n("Bossk", True),  # 32
    n("They're Still Coming Through!"),  # 33
    n("Jabba The Hutt", True),  # 34
    n("Elis Helrot"),  # 35
    n("Probot"),  # 36
    n("Zuckuss In Mist Hunter"),  # 37  Zuckuss in MH
    n("P-59"),  # 38
    n("4-LOM With Concussion Rifle"),  # 39  4-LOM w/Gun
    n("Sneak Attack", True),  # 40
    n("Sneak Attack", True),  # 41
    n("Kashyyyk: Skyhook Platform"),  # 42
    n("Imperial Propaganda", True),  # 43
    n("Short Range Fighters & Watch Your Back!"),  # 44  SRF Combo
    n("Imbalance & Kintan Strider"),  # 45  Imbalance Combo
    n("Mara Jade With Lightsaber"),  # 46
    n("OOM-9", True),  # 47
    n("Imperial Barrier"),  # 48
    n("Jabba's Space Cruiser", True),  # 49
    n("Wookiee Subjugation"),  # 50
    n("Guri", True),  # 51  short G-scrawl; (V)
    n("Kashyyyk: Wookiee Slaving Camp"),  # 52
    n("Lady Valarian", True),  # 53
    n("Ponda Baba", True),  # 54
    n("Velken Tezeri", True),  # 55  Velken T.
    n("Mercenary Pilot"),  # 56
    n("Force Push", True),  # 57
    n("Ghhhk"),  # 58
    n("Den Of Thieves & Special Delivery"),  # 59  Den Of Thieves Combo
    n("Knowledge And Defense", True),  # 60  K+D
]

ANGELO_D2_DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),  # 1
    n("We'll Let Fate-a Decide, Huh?", True),  # 2  We'll let...
    n("A Useless Gesture", True),  # 3
    n("Battle Order"),  # 4
    n("You Cannot Hide Forever"),  # 5
    n("Firepower"),  # 6
    n("Resistance"),  # 7
    n("There Is No Try", True),  # 8
    n("Fanfare", True),  # 9
    n("Imperial Detention"),  # 10
    n("Come Here You Big Coward", True),  # 11  CHYBC
    n("Secret Plans"),  # 12
    n("Allegations Of Corruption"),  # 13
    n("Abyss", True),  # 14
    n("Oppressive Enforcement", True),  # 15  OP En
]

ANGELO_D2_DS_ADD: list[tuple[str | None, bool]] = []


# --- Light: d2p2_p18.png. LIGHT checked. QMC. ---

ANGELO_D2_LS_SCAN = "extract/day2/d2p2_p18.png"
ANGELO_D2_LS_PDF_PAGE = 18
ANGELO_D2_LS_SIDE = "Light"
ANGELO_D2_LS_STARTING = n("Quiet Mining Colony / Independent Operation")

ANGELO_D2_LS_RESERVE = [
    n("Quiet Mining Colony / Independent Operation"),  # 1  QMC
    n("Bespin"),  # 2
    n("Cloud City: Guest Quarters"),  # 3  CC: Guest Quarters
    n("Heading For The Medical Frigate", True),  # 4
    n("All My Urchins & Cloud City Celebration"),  # 5  All my Urchins Combo
    n("Keeping The Empire Out Forever"),  # 6  Keeping The Emp.
    n("Beldon's Eye", True),  # 7
    n("Desperate Reach", True),  # 8
    n("Desperate Reach", True),  # 9
    n("Ellorrs Madak", True),  # 10
    n("Imperial Atrocity", True),  # 11
    n("Kal'Falnl C'ndros"),  # 12  C'ndros looks like Combo
    n("Booster In Pulsar Skate"),  # 13  Booster in PS
    n("Senator Jar Jar Binks"),  # 14  Jar Jar Binks
    n("Dexter Jettster"),  # 15  Dexter
    n("It's A Hit!"),  # 16
    n("Luke With Lightsaber"),  # 17
    n("Rebel Barrier"),  # 18
    n("Lady Luck"),  # 19
    n("Cloud City: North Corridor"),  # 20
    n("Choke"),  # 21
    n("Lando Calrissian, Unlikely Hero"),  # 22  Lando C, UH
    n("Path Of Least Resistance"),  # 23  Path
    n("It's A Trap!"),  # 24
    n("Leesub Sirln", True),  # 25  Leesub Sirln
    n("Menace Fades"),  # 26
    n("Foul Moudama"),  # 27
    n("Leia, Rebel Princess"),  # 28  Leia, RP
    n("Sergeant Edian", True),  # 29
    n("Alternatives To Fighting"),  # 30
    n("Landing Claw"),  # 31
    n("Tanus Spijek", True),  # 32
    n("Aayla Secura"),  # 33  Aayla
    n("Let The Wookiee Win", True),  # 34  LTWW
    n("Yoxgit"),  # 35
    n("Cloud City: West Gallery"),  # 36  CC: WG; blob crossed
    n("Overseer"),  # 37
    n("Dash Rendar"),  # 38
    n("Gola"),  # 39  short G-scrawl (Day 3 Sokol also Gola)
    n("Han Solo, Innocent Scoundrel"),  # 40  Han Solo, IS
    n("Mirax Terrik"),  # 41  Mirax
    n(None),  # 42  Gallian/Shocking Info Combo — unread
    n("Leslomy Tacema", True),  # 43
    n("All My Urchins", True),  # 44  Ad My. (V)
    n("Houjix & Out Of Nowhere"),  # 45  Houjix Combo
    n("Luke's Hunting Rifle", True),  # 46  Hunt Gift (V)
    n("All Wings Report In & Darklighter Spin"),  # 47  All Wings Combo
    n("Caldera Righim"),  # 48  Caldera R.
    n("Lobot", True),  # 49
    n("Bothan Spy", True),  # 50  Boushh crossed; Bothan, RLD
    n("Melas", True),  # 51
    n("Cloud City: Upper Plaza Corridor"),  # 52  CC: UPC
    n("Dark Approach", True),  # 53
    n("Trooper Utris M'toc", True),  # 54
    n("Kebyc", True),  # 55
    n("Nien Nunb, Sullustan Smuggler"),  # 56  Nien Nunb, SS
    n("Chewbacca, Walking Carpet"),  # 57  Chewbacca, WC
    n("Path Of Least Resistance"),  # 58  Path
    n("Seeking An Audience", True),  # 59  Seeking
    n("Anger, Fear, Aggression"),  # 60  AFA; (V) empty
]

ANGELO_D2_LS_SHIELDS = [
    n("Yavin Sentry", True),  # 1
    n("Chasm", True),  # 2
    n("Aim High", True),  # 3
    n("Let's Keep A Little Optimism Here", True),  # 4  Optimism
    n("Jabba's Prize", True),  # 5
    n("He Can Go About His Business", True),  # 6  Business
    n("Your Insight Serves You Well", True),  # 7  Insight
    n("Battle Plan"),  # 8
    n("The Professor", True),  # 9  The Prof
    n("Do, Or Do Not"),  # 10
    n("Weapons Display", True),  # 11
    n("Ultimatum"),  # 12
    n("Don't Do That Again", True),  # 13
    n("Simple Tricks And Nonsense"),  # 14
    n("A Tragedy Has Occurred"),  # 15  Tragedy
]

ANGELO_D2_LS_ADD: list[tuple[str | None, bool]] = []


ANGELO_D2_DS_UNREAD: list[int] = []
ANGELO_D2_LS_UNREAD = [42]
ANGELO_D2_DS_NO_DEST: list[str] = []
ANGELO_D2_LS_NO_DEST = ["Gola"]

NOTES = """
Angelo Consoli / DrevithShadow, 2014 Worlds Day 2, 2013 form.
Name Angelo. Worlds '14 08/23/14.
Dark d2p2_p17 Slavers (DARK checked). Light d2p2_p18 QMC (LIGHT checked).

DS: line 1 Slaving Obj. (V) empty. Line 2 Take Evasive Action.
Line 6 IG-88 w/Gun → IG-88 With Riot Gun. Line 32 Bossk (V).
Line 51 short G-scrawl (V) taken as Guri. Line 55 Velken T. → Velken Tezeri (V).
Shield 2 We'll let... → We'll Let Fate-a Decide, Huh? (V).
Shield 15 OP En → Oppressive Enforcement (V).

LS: line 12 Kal'Falnl C'ndros (C'ndros looks like Combo).
Line 25 Leesub Sirln (V). Line 39 Gola (same unread title as Sokol Day 3).
Line 42 Gallian/Shocking Info Combo unread.
Line 44 Ad My. (V) → All My Urchins (V).
Line 46 Hunt Gift (V) → Luke's Hunting Rifle (V).
Line 50 Boushh crossed; Bothan, RLD kept as Bothan Spy (V).
Line 60 AFA (V) empty.
""".strip()


if __name__ == "__main__":
    assert len(ANGELO_D2_DS_RESERVE) == 60, len(ANGELO_D2_DS_RESERVE)
    assert len(ANGELO_D2_DS_SHIELDS) == 15, len(ANGELO_D2_DS_SHIELDS)
    assert len(ANGELO_D2_LS_RESERVE) == 60, len(ANGELO_D2_LS_RESERVE)
    assert len(ANGELO_D2_LS_SHIELDS) == 15, len(ANGELO_D2_LS_SHIELDS)
    print("transcribe_angelo_day2.py", PLAYER)
    print("  Dark Slavers reserve", len(ANGELO_D2_DS_RESERVE), "shields", len(ANGELO_D2_DS_SHIELDS), "unread", ANGELO_D2_DS_UNREAD, "no_dest", ANGELO_D2_DS_NO_DEST)
    print("  Light QMC reserve", len(ANGELO_D2_LS_RESERVE), "shields", len(ANGELO_D2_LS_SHIELDS), "unread", ANGELO_D2_LS_UNREAD, "no_dest", ANGELO_D2_LS_NO_DEST)
