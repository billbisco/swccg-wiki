#!/usr/bin/env python3
"""Day 2 Xerox transcription: Chris Terwilliger (Twigg) Light only.

Source scan: extract/day2_upright/d2p3_p17.png (Light, Y4 / It's The Future You See).
2010 form. Name field Twigg 'Hile' plus Chris. Light/Dark unchecked; cards are Light.
Do not invent a Dark Day 2 60 — it is not in Parts 1–3.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Chris Terwilliger"
USERNAME = ""
FORM = "xerox_2010"
PDF = "2014 Worlds Day 2 Part 3.pdf"

CHRIS_D2_PLAYER = PLAYER
CHRIS_D2_LS_DECK_NAME = "Y4"


# --- Light: day2_upright/d2p3_p17.png. Y4 / Communing. ---

CHRIS_D2_LS_SCAN = "extract/day2_upright/d2p3_p17.png"
CHRIS_D2_LS_PDF_PAGE = 17
CHRIS_D2_LS_SIDE = "Light"
CHRIS_D2_LS_STARTING = n("It Is The Future You See", True)

CHRIS_D2_LS_RESERVE = [
    n("It Is The Future You See", True),  # 1  It's the Future you see
    n("Do, Or Do Not & Wise Advice"),  # 2
    n("Battle Plan & Draw Their Fire"),  # 3
    n("Quick Draw", True),  # 4
    n("Projection Of A Skywalker"),  # 5
    n("Seeking An Audience", True),  # 6
    n("Mechanical Failure"),  # 7
    n("Sai'torr Kal Fas", True),  # 8
    n("Imperial Atrocity", True),  # 9
    n("Imperial Atrocity", True),  # 10
    n("Speak With The Jedi Council"),  # 11
    n("Rebel Leadership", True),  # 12
    n("Rebel Leadership", True),  # 13
    n("Rebel Leadership", True),  # 14
    n("Let The Wookiee Win", True),  # 15
    n("Let The Wookiee Win", True),  # 16
    n("Escape Pod", True),  # 17
    n("Escape Pod", True),  # 18
    n("Smoke Screen"),  # 19
    n("Wesa Gotta Grand Army"),  # 20
    n("Wesa Gotta Grand Army"),  # 21
    n("Control & Tunnel Vision"),  # 22  careful / tunnel vision
    n("Clash Of Sabers"),  # 23
    n("Clash Of Sabers"),  # 24
    n("Houjix"),  # 25
    n("Were You Looking For Me?"),  # 26
    n("All Wings Report In & Darklighter Spin"),  # 27
    n("Grappling Hook"),  # 28
    n("Nabrun Leids"),  # 29
    n("Blaster Deflection"),  # 30
    n("Sorry About The Mess & Blaster Proficiency"),  # 31
    n("Jedi Levitation", True),  # 32
    n("Sense"),  # 33
    n("Either Way, You Win"),  # 34
    n("Naboo: Battle Plains"),  # 35
    n("Coruscant: Jedi Council Chamber", True),  # 36  Jedi Chamber
    n("Yavin 4: Massassi War Room", True),  # 37  Yavin 4 War Room
    n("Naboo: Boss Nass' Chambers"),  # 38
    n("Hoth: Echo Command Center (War Room)"),  # 39  Hoth: War Room
    n("Home One: War Room"),  # 40
    n("Qui-Gon Jinn's Lightsaber"),  # 41
    n("Luke's Lightsaber"),  # 42
    n("Home One"),  # 43
    n("Han, Chewie, And The Falcon", True),  # 44
    n("Lady Luck", True),  # 45
    n("Threepio With His Parts Showing"),  # 46
    n("Luke Skywalker, Strong In The Force", True),  # 47
    n("Luke Skywalker, Jedi Knight"),  # 48
    n("Luke Skywalker, Jedi Knight"),  # 49
    n("Mace Windu, Master Of The Order", True),  # 50
    n("Mace Windu", True),  # 51  slash-check
    n("Master Qui-Gon", True),  # 52
    n("Master Qui-Gon"),  # 53  ditto; (V) empty
    n("Anakin Skywalker, Padawan Learner", True),  # 54
    n("Corran Horn"),  # 55
    n("Admiral Ackbar", True),  # 56
    n("Leia, Rebel Princess"),  # 57
    n("Lando Calrissian, Unlikely Hero", True),  # 58
    n("Jedi Lightsaber"),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

CHRIS_D2_LS_SHIELDS = [
    n("He Can Go About His Business", True),  # 1
    n("Yavin Sentry", True),  # 2
    n("Only Jedi Carry That Weapon"),  # 3
    n("Weapons Display", True),  # 4
    n("The Professor", True),  # 5
    n("Let's Keep A Little Optimism Here", True),  # 6
    n("Your Insight Serves You Well", True),  # 7
    n("Affect Mind", True),  # 8
    n("There Is Another", True),  # 9
    n("Chasm", True),  # 10
    n("Ultimatum"),  # 11
    n("Simple Tricks And Nonsense", True),  # 12
]

CHRIS_D2_LS_ADD = [
    n("Aim High"),  # 1
    n("Don't Do That Again", True),  # 2
    n("A Tragedy Has Occurred"),  # 3
]


CHRIS_D2_LS_UNREAD: list[int] = []
CHRIS_D2_LS_NO_DEST: list[str] = []

NOTES = """
Chris Terwilliger / Twigg, 2014 Worlds Day 2 Light only, 2010 form.
Name field Twigg 'Hile' plus Chris in the top margin. Light/Dark unchecked;
cards are Light (It's The Future You See / Y4 / Jedi Council).
Dark/Hoth (V) is not in Parts 1–3.

Line 1 It's the Future you see (V) → It Is The Future You See (V).
Line 22 Control & Tunnel Vision.
Line 28 Grappling Hook.
Line 36 Coruscant: Jedi Chamber (V) → Coruscant: Jedi Council Chamber.
Line 39 Hoth: War Room → Hoth: Echo Command Center (War Room). Home One: War Room is 40.
Line 51 Mace Windu slash-check counted (V).
Line 53 Master Qui-Gon ditto; (V) empty.
Shield 1 He can go about his business (V).
Shield 9 There is Another (V).
""".strip()


if __name__ == "__main__":
    assert len(CHRIS_D2_LS_RESERVE) == 60, len(CHRIS_D2_LS_RESERVE)
    assert len(CHRIS_D2_LS_SHIELDS) == 12, len(CHRIS_D2_LS_SHIELDS)
    print("transcribe_chris_day2_ls.py", PLAYER)
    print("  Light Y4 reserve", len(CHRIS_D2_LS_RESERVE), "shields", len(CHRIS_D2_LS_SHIELDS), "add", len(CHRIS_D2_LS_ADD), "unread", CHRIS_D2_LS_UNREAD, "no_dest", CHRIS_D2_LS_NO_DEST)
