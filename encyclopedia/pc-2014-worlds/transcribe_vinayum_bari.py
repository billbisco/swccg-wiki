#!/usr/bin/env python3
"""Day 2 Xerox transcription: Vinayum Bari Light (p19) + Dark (p20).

Source scans: extract/day2/d2p1_p19.png (Light, name blank, deck Obj.)
and extract/day2/d2p1_p20.png (Dark, I Saw it Burn). 2010 form.
Facing-page dest: p19 Name blank Light between Matt Sokol (p17–p18) and
Greg Shaw (p21–p22); p20 named Vinayum Bari / DVDRCTS. (V) follows the
sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


# --- Light: d2p1_p19.png. LIGHT checked. Name blank. Deck Obj. ---

LS_PLAYER = "Vinayum Bari"
LS_USERNAME = ""
LS_DECK_NAME = "Obj."
LS_SIDE = "Light"
LS_FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p1_p19.png"
LS_PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 19
LS_STARTING = ("Yavin 4: Massassi Throne Room", False)

LS_RESERVE = [
    n("Yavin 4: Massassi Throne Room"),  # 1
    n("Anger, Fear, Aggression", True),  # 2
    n("Yavin 4: Massassi War Room", True),  # 3
    n("Home One: War Room"),  # 4
    n("Naboo: Boss Nass' Chambers"),  # 5  N Boss Nass' Chambers
    n("Naboo: Battle Plains"),  # 6  N: Battle Plains
    n("Coruscant: Jedi Council Chambers", True),  # 7  C: Jedi Council
    n("Naboo"),  # 8  N Sys
    n("Mace Windu, Master Of The Order"),  # 9
    n("Qui-Gon Jinn With Lightsaber"),  # 10
    n("Qui-Gon Jinn With Lightsaber"),  # 11
    n("Obi-Wan With Lightsaber"),  # 12
    n("Obi-Wan With Lightsaber"),  # 13
    n("Luke With Lightsaber"),  # 14
    n("Luke Skywalker", True),  # 15
    n("Jaina Solo"),  # 16
    n("Wedge Antilles, Red Squadron Leader"),  # 17  Wedge Antilles, RSL
    n("Dash Rendar", True),  # 18
    n("Corran Horn"),  # 19
    n("Admiral Ackbar", True),  # 20
    n("General Bel Iblis"),  # 21
    n("Lando Calrissian, Scoundrel"),  # 22
    n("Lando Calrissian, Scoundrel"),  # 23
    n("Leia, Rebel Princess"),  # 24
    n("Threepio With His Parts Showing"),  # 25
    n("Padme Naberrie", True),  # 26
    n("Don't Tread On Me", True),  # 27
    n("Hear Me Baby, Hold Together", True),  # 28
    n("Corellian Retort", True),  # 29  written Corellian Rescue
    n("You Will Come With Me"),  # 30
    n("Gift Of The Mentor"),  # 31
    n("Houjix"),  # 32
    n("Escape Pod", True),  # 33
    n("Escape Pod", True),  # 34
    n("Impressive, Most Impressive", True),  # 35
    n("Control & Tunnel Vision"),  # 36  Control & T.V.
    n("Speak With The Jedi Council"),  # 37  Senator w/ the Jedi Council
    n("Wesa Gotta Grand Army"),  # 38
    n("Wesa Gotta Grand Army"),  # 39
    n("Jedi Lightsaber", True),  # 40
    n("Rebel Leadership", True),  # 41
    n("Rebel Leadership", True),  # 42
    n("Rebel Leadership", True),  # 43
    n("Let The Wookiee Win", True),  # 44
    n("Let The Wookiee Win", True),  # 45
    n("A Jedi's Resilience"),  # 46
    n(None),  # 47  blank
    n(None),  # 48  blank
    n("Han, Chewie, And The Falcon"),  # 49  Han, Chewie &
    n("Tantive IV", True),  # 50
    n("Home One"),  # 51
    n("Imperial Atrocity", True),  # 52
    n("Imperial Atrocity", True),  # 53
    n("Mantellian Savrip"),  # 54
    n("Mechanical Failure"),  # 55
    n("Scrambled Transmission", True),  # 56
    n("Draw Their Fire"),  # 57
    n("Strikeforce", True),  # 58
    n("Seeking An Audience", True),  # 59
    n("Artoo-Detoo In Red 5"),  # 60
]

LS_SHIELDS = [
    n("Wise Advice"),  # 1
    n("Another Pathetic Lifeform"),  # 2
    n("He Can Go About His Business", True),  # 3
    n("Your Insight Serves You Well", True),  # 4
    n("Yavin Sentry", True),  # 5
    n("Weapons Display"),  # 6
    n("Ultimatum"),  # 7
    n("The Professor"),  # 8
    n("Simple Tricks And Nonsense"),  # 9
    n("Let's Keep A Little Optimism Here", True),  # 10
    n("Don't Do That Again", True),  # 11
    n("Battle Plan"),  # 12
]

LS_ADD = [
    n("Do, Or Do Not"),  # 1
    n("Aim High"),  # 2
    n("A Tragedy Has Occurred"),  # 3
]

LS_UNREAD = [47, 48]
LS_NO_DEST: list[str] = []


# --- Dark: d2p1_p20.png. DARK checked. I Saw it Burn. DVDRCTS. ---

DS_PLAYER = "Vinayum Bari"
DS_USERNAME = "DVDRCTS"
DS_DECK_NAME = "I Saw it Burn"
DS_SIDE = "Dark"
DS_FORM = "xerox_2010"
DS_SCAN = "extract/day2/d2p1_p20.png"
DS_PDF = "2014 Worlds Day 2 Part 1.pdf"
DS_PDF_PAGE = 20
DS_STARTING = (
    "Set Your Course For Alderaan / The Ultimate Power In The Universe",
    False,
)

DS_RESERVE = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),  # 1  SYCFA / TUPIU
    n("Knowledge And Defense", True),  # 2
    n("Executor"),  # 3
    n("Death Star"),  # 4
    n("Death Star: Docking Bay 327"),  # 5  Death Star: DB
    n("Prepared Defenses", True),  # 6
    n("Kuat Drive Yards", True),  # 7
    n("A Million Voices Crying Out"),  # 8
    n("Imperial Stockpile"),  # 9
    n("Laser Cannon Battery"),  # 10
    n("Death Star: Central Core", True),  # 11
    n("Death Star: War Room", True),  # 12
    n("Commence Primary Ignition", True),  # 13
    n("Superlaser"),  # 14
    n("Coruscant"),  # 15
    n("Nal Hutta"),  # 16
    n("Emperor Palpatine"),  # 17
    n("Emperor Palpatine"),  # 18
    n("Darth Sidious"),  # 19
    n("Arica"),  # 20
    n("Darth Vader, Dark Lord Of The Sith"),  # 21  Vader The Sith
    n("IG-88"),  # 22
    n("Judicator"),  # 23
    n("Judicator"),  # 24
    n("Victory"),  # 25
    n("Accuser"),  # 26
    n("Conquest", True),  # 27
    n("Devastator", True),  # 28
    n("Thunderflare"),  # 29
    n("Tyrant"),  # 30
    n("Vengeance"),  # 31
    n("Visage"),  # 32
    n("Lateral Damage"),  # 33
    n("Lateral Damage"),  # 34
    n("He Is Not Ready", True),  # 35
    n("Tarkin Doctrine"),  # 36
    n("Dreaded Imperial Starfleet", True),  # 37  Dedicated / Dreaded
    n("Flawless Marksmanship"),  # 38
    n("Naval Valor"),  # 39
    n("Naval Valor"),  # 40
    n("Crossfire"),  # 41  Crash Fire
    n("Crossfire"),  # 42
    n("Crossfire"),  # 43
    n("Imperial Barrier"),  # 44
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 45  Ghhhk & Those
    n("TIE Sentry Ships", True),  # 46  The Sentry Ships
    n("Relentless Pursuit"),  # 47
    n("Relentless Pursuit"),  # 48
    n("Open Fire!"),  # 49  Ozzel's DD scrawl
    n("Open Fire!"),  # 50
    n("Force Push", True),  # 51
    n("We're In Attack Position Now"),  # 52
    n("We're In Attack Position Now"),  # 53
    n("Lightsaber Deficiency", True),  # 54
    n("A Bright Center To The Universe"),  # 55
    n("We Must Accelerate Our Plans"),  # 56
    n("Force Lightning"),  # 57
    n("Imperial Command", True),  # 58
    n("Something Special Planned For Them", True),  # 59  SS & FT
    n("Monnok"),  # 60
]

DS_SHIELDS = [
    n("Allegations Of Corruption"),  # 1
    n("Come Here You Big Coward"),  # 2
    n("Do They Have A Code Clearance?", True),  # 3
    n("Imperial Detention", True),  # 4
    n("Leave Them To Me"),  # 5
    n("We'll Let Fate-a Decide, Huh?"),  # 6
    n("You Cannot Hide Forever", True),  # 7
    n("A Useless Gesture"),  # 8
    n("Battle Order"),  # 9
    n("Resistance"),  # 10
    n("Firepower", True),  # 11
    n("I Find Your Lack Of Faith Disturbing", True),  # 12
]

DS_ADD = [
    n("Abyss", True),  # 1
    n("Secret Plans"),  # 2
    n("There Is No Try"),  # 3
]

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []

NOTES = """
Unnamed Light d2p1_p19.png (2010 form, LIGHT checked). Name/username blank.
Deck name Obj. Yavin 4 Massassi Throne Room start (no Restore Freedom title
on the sheet). Possible pair with p20 Vinayum Bari / DVDRCTS.

Dark d2p1_p20.png (2010 form, DARK checked). Vinayum Bari, username DVDRCTS,
deck I Saw it Burn, Worlds 2014. Objective written SYCFA/TUPIU (index read
You Can Run But You Cannot Hide; 2014 dest is Set Your Course For Alderaan).

LS: 5-8 abbreviated N/C sites (Boss Nass' Chambers, Battle Plains, Jedi
Council Chambers, Naboo system) matching Shaw Day 2 Y4/Jedi Council shape.
29 Corellian Rescue → Corellian Retort (V). 30 You Will Come With Me as
written. 37 Speak With The Jedi Council (Senator w/ the Jedi Council).
47-48 blank.

DS: 7 Kuat Drive Yards (V). 13 Commence Primary Ignition (V). 21 Vader The
Sith → Darth Vader, Dark Lord Of The Sith. 37 Dedicated → Dreaded Imperial
Starfleet (V). 41 Crash Fire → Crossfire. 46 The Sentry Ships → TIE Sentry
Ships (V). 49-50 Open Fire! (Ozzel scrawl). 52-53 We're In Attack Position
Now. 59 SS & FT → Something Special Planned For Them (V).
""".strip()


def _dump(side: str, reserve, shields, add) -> None:
    rows = []
    for name, v in reserve:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}")
    for name, v in shields:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}\tsh")
    for name, v in add:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}")
    print("\n".join(rows))


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    print(
        "transcribe_vinayum_bari.py",
        "LS",
        LS_PLAYER,
        LS_SIDE,
        "reserve",
        len(LS_RESERVE),
        "shields",
        len(LS_SHIELDS),
        "unread",
        LS_UNREAD,
        "no_dest",
        LS_NO_DEST,
    )
    print(
        "transcribe_vinayum_bari.py",
        "DS",
        DS_PLAYER,
        DS_SIDE,
        "reserve",
        len(DS_RESERVE),
        "shields",
        len(DS_SHIELDS),
        "unread",
        DS_UNREAD,
        "no_dest",
        DS_NO_DEST,
    )
    _dump("Light", LS_RESERVE, LS_SHIELDS, LS_ADD)
    _dump("Dark", DS_RESERVE, DS_SHIELDS, DS_ADD)
