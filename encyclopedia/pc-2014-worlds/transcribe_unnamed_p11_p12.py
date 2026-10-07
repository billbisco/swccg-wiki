#!/usr/bin/env python3
"""Day 2 Xerox transcription: unnamed p11 Light + p12 Dark pair.

Source scans: extract/day2/d2p1_p11.png (Light, deck name M) and
extract/day2/d2p1_p12.png (Dark, BHU Syndicate). 2010 form. Name / username
/ event blank on both; treated as a pair. Light is It Is The Future You See
/ Communing mains. Dark is Separatist Uprising / Geonosis droids.
(V) follows the sheet checkbox. Dittos expanded. Cross-outs keep the
replacement that remains.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = None
USERNAME = ""
PDF = "2014 Worlds Day 2 Part 1.pdf"


# --- Light: d2p1_p11.png, 2010 form. LIGHT checked. Deck name M. ---

LS_PLAYER = None
LS_DECK_NAME = "M"
LS_SIDE = "Light"
LS_FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p1_p11.png"
LS_PDF_PAGE = 11
LS_STARTING = ("It Is The Future You See", True)

LS_RESERVE = [
    n("It Is The Future You See", True),  # 1  It's the future...
    n("Do, Or Do Not & Wise Advice"),  # 2  Do or Do Not / WA
    n("Battle Plan & Draw Their Fire"),  # 3  BP / DTF
    n("Quick Draw", True),  # 4
    n("Projection Of A Skywalker"),  # 5  POS
    n("Were You Looking For Me?", True),  # 6
    n("Let The Wookiee Win", True),  # 7  LTWW
    n("Let The Wookiee Win"),  # 8  ditto; (V) empty
    n("Let The Wookiee Win"),  # 9  ditto; (V) empty
    n("Rebel Leadership", True),  # 10  Rebel Leader-Ship
    n("Rebel Leadership"),  # 11  ditto
    n("Rebel Leadership"),  # 12  ditto
    n("Lando Calrissian, Unlikely Hero"),  # 13
    n("Lady Luck"),  # 14
    n("Imperial Atrocity", True),  # 15
    n("Imperial Atrocity", True),  # 16  ditto (V)
    n("Luke Skywalker, Jedi Knight"),  # 17  Luke JK
    n("Luke Skywalker, Jedi Knight"),  # 18  ditto
    n("Wesa Gotta Grand Army"),  # 19
    n("Seeking An Audience", True),  # 20
    n("Sai'torr Kal Fas", True),  # 21
    n("All Wings Report In & Darklighter Spin", True),  # 22  prior title crossed
    n("Grimtaash"),  # 23
    n("Sorry About The Mess & Blaster Proficiency"),  # 24  SATM / BP
    n("Blaster Deflection"),  # 25
    n("Clash Of Sabers"),  # 26
    n("Clash Of Sabers"),  # 27  ditto
    n("Jedi Levitation", True),  # 28
    n("Sense"),  # 29
    n("Sense"),  # 30  ditto
    n("Sense"),  # 31  ditto
    n(None),  # 32  fully crossed; (V) had been checked
    n("Threepio With His Parts Showing"),  # 33  A3PO / Threepio w/ Parts
    n("Threepio With His Parts Showing"),  # 34  ditto
    n("Houjix"),  # 35
    n("Escape Pod", True),  # 36
    n("Escape Pod", True),  # 37  ditto (V)
    n("Qui-Gon Jinn's Lightsaber"),  # 38
    n("Luke's Lightsaber", True),  # 39
    n("Leia's Lightsaber"),  # 40
    n("Home One"),  # 41
    n("Han, Chewie, And The Falcon", True),  # 42  HCF
    n("Artoo-Detoo In Red 5"),  # 43  Ackbar in RS / Artoo in R5
    n("Mace Windu"),  # 44
    n("Mace Windu", True),  # 45  ditto (V)
    n("Mace Windu", True),  # 46  ditto (V)
    n("Leia, Rebel Princess"),  # 47  Leia RP
    n("Admiral Ackbar", True),  # 48
    n("Corran Horn", True),  # 49
    n("Luke Skywalker, Strong In The Force"),  # 50  Luke SITF
    n("Luke Skywalker, Strong In The Force"),  # 51  ditto
    n("Master Qui-Gon", True),  # 52
    n("Master Qui-Gon", True),  # 53  ditto (V)
    n("Coruscant: Jedi Council Chamber", True),  # 54  Coruscant JCC
    n("Yavin 4: Massassi War Room", True),  # 55  Y4 War Room
    n("Hoth: Echo Command Center (War Room)"),  # 56  Hoth War Room
    n("Naboo: Boss Nass' Chambers"),  # 57
    n("Naboo: Battle Plains"),  # 58
    n("General Airen Cracken"),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA
]

LS_SHIELDS = [
    n("Aim High"),  # 1
    n("Affect Mind", True),  # 2  Affect Mind (looks like Another Scan)
    n("Your Insight Serves You Well", True),  # 3  YISYW
    n("Let's Keep A Little Optimism Here", True),  # 4
    n("Simple Tricks And Nonsense"),  # 5  Small Victories & Non-Shv
    n("Ultimatum"),  # 6
    n("A Tragedy Has Occurred"),  # 7
    n("Chasm"),  # 8  Chaos / Chasm
    n("Weapons Display"),  # 9
    n("Only Jedi Carry That Weapon"),  # 10  Battle Plan crossed
    n("There Is Another"),  # 11
    n("Yavin Sentry", True),  # 12
]

LS_ADD = [
    n("He Can Go About His Business", True),  # 1
    n("The Professor", True),  # 2  The Power Of / The Professor
    n("Don't Do That Again", True),  # 3
]

LS_UNREAD = [32]
LS_NO_DEST = ["Leia's Lightsaber"]


# --- Dark: d2p1_p12.png, 2010 form. DARK checked. BHU Syndicate. ---

DS_PLAYER = None
DS_DECK_NAME = "BHU Syndicate"
DS_SIDE = "Dark"
DS_FORM = "xerox_2010"
DS_SCAN = "extract/day2/d2p1_p12.png"
DS_PDF_PAGE = 12
DS_STARTING = ("Separatist Uprising / At War With Itself", False)

DS_RESERVE = [
    n("Separatist Uprising / At War With Itself"),  # 1  At War w/ itself
    n("Rally For Our Cause"),  # 2
    n("Droid Racks"),  # 3  Droid Holos / Droid Racks
    n("Battle Order & First Strike"),  # 4
    n("An Entire Legion Of My Best Troops"),  # 5
    n("War Has Begun"),  # 6
    n("Imperial Propaganda", True),  # 7
    n("OOM Command Battle Droid"),  # 8  DWO-9 UU Backup
    n("OOM Command Battle Droid"),  # 9  ditto
    n("We Must Accelerate Our Plans"),  # 10  WMAOP
    n("We Must Accelerate Our Plans"),  # 11  ditto
    n("We Must Accelerate Our Plans"),  # 12  ditto
    n("Blockade Flagship: Bridge"),  # 13
    n("Infantry Battle Droid"),  # 14
    n("Battle Droid Blaster Rifle"),  # 15
    n("Battle Droid Blaster Rifle"),  # 16  ditto
    n("Battle Droid Blaster Rifle"),  # 17
    n("Battle Droid Blaster Rifle"),  # 18
    n("Battle Droid Blaster Rifle"),  # 19
    n("Battle Droid Blaster Rifle"),  # 20
    n("Battle Droid Blaster Rifle"),  # 21
    n("Battle Droid Blaster Rifle"),  # 22
    n("Battle Droid Blaster Rifle"),  # 23
    n("Battle Droid Blaster Rifle"),  # 24
    n("3B3-888"),  # 25
    n("Jango Fett, The Assassin"),  # 26
    n("B2 Super Battle Droid"),  # 27
    n("B2 Super Battle Droid"),  # 28  ditto
    n("B2 Super Battle Droid"),  # 29  ditto
    n("Geonosis: Separatist Council Room"),  # 30  Geonosis Separatist Council
    n("Imperial Artillery"),  # 31
    n("Imperial Artillery"),  # 32  ditto
    n("Boba Fett, Prepared Hunter"),  # 33
    n("Sonic Bombardment", True),  # 34
    n("Sonic Bombardment", True),  # 35  ditto (V)
    n("Sonic Bombardment", True),  # 36  ditto (V)
    n("Cloud City: Security Tower", True),  # 37
    n("Blast Door Controls"),  # 38
    n("Everything Is Going As Planned", True),  # 39
    n("Payback"),  # 40
    n("Lightsaber Deflection", True),  # 41
    n("Death Star: War Room", True),  # 42
    n(None),  # 43  written SSA-1015; unread
    n("Wounded Warrior"),  # 44
    n("Ghhhk"),  # 45
    n("Ghhhk"),  # 46  ditto
    n("Oh, Switch Off"),  # 47  Oh Switch Off
    n("Oh, Switch Off"),  # 48  ditto
    n("Short Range Fighters & Watch Your Back!"),  # 49  SRF / WYB
    n("3B3-888"),  # 50
    n("3B3-888"),  # 51  ditto
    n("Slave I, Symbol Of Fear"),  # 52
    n("Masterful Move & Endor Occupation"),  # 53  Masterful Move / EO
    n("Geonosis: Rocky Plains"),  # 54
    n("OOM-9", True),  # 55
    n("Geonosis"),  # 56
    n("Something Special Planned For Them", True),  # 57
    n("Force Lightning", True),  # 58
    n("Counter Assault"),  # 59
    n("Knowledge And Defense", True),  # 60  KAD
]

DS_SHIELDS = [
    n("Secret Plans", True),  # 1
    n("We'll Let Fate-a Decide, Huh?", True),  # 2  We'll Not Dare Decide
    n("You Cannot Hide Forever", True),  # 3  YCHF
    n("A Useless Gesture", True),  # 4
    n("There Is No Try"),  # 5  Resistance crossed; TINT on next slot kept here as remaining
    n("After Her!", True),  # 6  After Her; Oppressive Enforcement crossed on this band
    n("Firepower", True),  # 7
    n("Do They Have A Code Clearance?", True),  # 8
    n("Imperial Detention"),  # 9
    n("Abyss", True),  # 10
    n("Come Here You Big Coward", True),  # 11  CHYBC
]

DS_ADD = [
    n("Fanfare", True),  # 1
    n("Allegations Of Corruption"),  # 2
    n("Oppressive Enforcement"),  # 3  Death Star Sentry crossed; Enforcement remains
]

DS_UNREAD = [43]
DS_NO_DEST = ["Rally For Our Cause", "Payback", "Lightsaber Deflection (V)"]

NOTES = (
    "Unnamed pair (name boxes blank): Light d2p1_p11 deck M / It Is The Future You See; "
    "Dark d2p1_p12 BHU Syndicate / Separatist Uprising. LS 32 fully crossed. "
    "DS 43 written SSA-1015 unread. DS 8–9 written DWO-9 UU Backup."
)

assert len(LS_RESERVE) == 60, len(LS_RESERVE)
assert len(DS_RESERVE) == 60, len(DS_RESERVE)

if __name__ == "__main__":
    print("unnamed p11 LS", len(LS_RESERVE), "sh", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD)
    print("unnamed p12 DS", len(DS_RESERVE), "sh", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD)
