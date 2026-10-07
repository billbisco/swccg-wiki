#!/usr/bin/env python3
"""Day 2 Xerox transcription: John Anderson (puck71).

Source scans: extract/day2/d2p1_p09.png (Light, RAW) and
extract/day2/d2p1_p10.png (Dark, HD). 2013 form, Worlds Day 2 8/23/14.
Typed list with handwritten substitutions on Dark. (V) follows checkbox.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "John Anderson"
USERNAME = "puck71"
LS_DECK_NAME = "RAW"
DS_DECK_NAME = "HD"
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p1_p09.png"
DS_SCAN = "extract/day2/d2p1_p10.png"
PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 9
DS_PDF_PAGE = 10
LS_STARTING = ("Republic At War / Aggressive Negotiations", False)
DS_STARTING = ("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", False)


# --- Light: d2p1_p09.png. LIGHT checked. RAW. ---

LS_RESERVE = [
    n("Republic At War / Aggressive Negotiations"),  # 1  Republic At War
    n("Geonosis: Forward Command Center"),  # 2
    n("Begun, The Clone War Has"),  # 3
    n("Heading For The Medical Frigate"),  # 4
    n("Wokling", True),  # 5
    n("Nick Of Time", True),  # 6
    n("Rogue Squadron Tactics"),  # 7
    n("Desperate Tactics"),  # 8
    n("Desperate Tactics"),  # 9
    n("Rebel Artillery"),  # 10
    n("Let The Wookiee Win", True),  # 11
    n("Let The Wookiee Win", True),  # 12
    n("Guardian's Lightsaber"),  # 13
    n("Weapon Levitation"),  # 14
    n("Mace Windu, Master Of The Order"),  # 15
    n("Sorry About The Mess & Blaster Proficiency"),  # 16
    n("Sorry About The Mess & Blaster Proficiency"),  # 17
    n("Hear Me Baby, Hold Together", True),  # 18
    n("Lucky Shot"),  # 19
    n("Dark Approach", True),  # 20
    n("Houjix", True),  # 21
    n("Obi-Wan Kenobi, Jedi Knight"),  # 22
    n("Rebel Artillery"),  # 23
    n("Chewbacca, Walking Carpet"),  # 24
    n("Control & Tunnel Vision"),  # 25
    n("Clone Pilot"),  # 26
    n("Anakin Skywalker, Padawan Learner"),  # 27
    n("Lando Calrissian, Unlikely Hero"),  # 28
    n("Han Solo, Innocent Scoundrel"),  # 29
    n("Jaina Solo"),  # 30
    n("Anakin Solo"),  # 31
    n("Seeking An Audience", True),  # 32
    n("Strikeforce", True),  # 33
    n("Imperial Atrocity", True),  # 34
    n("Lady Luck"),  # 35
    n("Acclamator-Class Assault Ship"),  # 36
    n("Acclamator-Class Assault Ship"),  # 37
    n("Alderaan Consular Ship"),  # 38
    n("Rebel Cell - Hidden Landing Site"),  # 39
    n("Muunilinst: Republic Landing Site"),  # 40
    n("Muunilinst: City Of Harnaidan"),  # 41
    n("Muunilinst: Harnaidan Plains"),  # 42
    n("Dressel"),  # 43
    n("Dual Laser Cannon", True),  # 44
    n("Dual Laser Cannon", True),  # 45
    n("Dual Laser Cannon", True),  # 46
    n("Dual Laser Cannon", True),  # 47
    n("AT-RT"),  # 48
    n("AT-RT"),  # 49
    n("AT-RT"),  # 50
    n("AT-RT"),  # 51
    n("AT-RT"),  # 52
    n("AT-RT"),  # 53
    n("AT-RT"),  # 54
    n("AT-RT"),  # 55
    n("AT-RT"),  # 56
    n("Assault On Muunilinst"),  # 57
    n("Hear Me Baby, Hold Together", True),  # 58
    n("Escape Pod", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("Do, Or Do Not"),  # 1
    n("Your Insight Serves You Well", True),  # 2
    n("Simple Tricks And Nonsense"),  # 3
    n("The Professor", True),  # 4
    n("Battle Plan"),  # 5
    n("Weapons Display", True),  # 6
    n("Wise Advice"),  # 7
    n("Ultimatum"),  # 8
    n("A Tragedy Has Occurred"),  # 9
    n("Chasm", True),  # 10
    n("Don't Do That Again", True),  # 11
    n("Aim High"),  # 12
    n("He Can Go About His Business"),  # 13
    n("Your Ship?"),  # 14
    n("Yavin Sentry", True),  # 15
]

LS_ADD: list[tuple[str | None, bool]] = []


# --- Dark: d2p1_p10.png. DARK checked. HD. Handwritten subs. ---

DS_RESERVE = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),  # 1
    n("Executor: Meditation Chamber"),  # 2
    n("Executor: Holotheatre"),  # 3
    n("Visage Of The Emperor"),  # 4
    n("Prepared Defenses"),  # 5
    n("Ni Chuba Na??", True),  # 6
    n("Conduct Your Search"),  # 7
    n("Gift Of The Master"),  # 8
    n("Emperor Palpatine"),  # 9
    n("Boba Fett, Prepared Hunter"),  # 10  handwritten sub
    n("Force Field", True),  # 11
    n("Force Field", True),  # 12
    n("Force Lightning"),  # 13
    n("Ghhhk"),  # 14
    n("Force Lightning"),  # 15
    n("Vader's Lightsaber"),  # 16
    n("Blaster Rack", True),  # 17
    n("We Must Accelerate Our Plans"),  # 18
    n("We Must Accelerate Our Plans"),  # 19
    n("We Must Accelerate Our Plans"),  # 20
    n("Dr. Evazan & Ponda Baba"),  # 21
    n("Mara Jade With Lightsaber"),  # 22
    n("You Are Beaten"),  # 23
    n("I Have You Now"),  # 24
    n("Revenge Of The Sith", True),  # 25  handwritten sub
    n("Endor: Back Door"),  # 26
    n("No Escape"),  # 27
    n("Revenge Of The Sith"),  # 28
    n("First Strike"),  # 29
    n("Dooku's Lightsaber"),  # 30
    n("Cloud City: Security Tower", True),  # 31
    n("Galen Marek, Starkiller"),  # 32
    n("Galen Marek, Starkiller"),  # 33
    n("Darth Vader, Dark Lord Of The Sith"),  # 34
    n("Darth Vader, Dark Lord Of The Sith"),  # 35
    n("Darth Vader, Dark Lord Of The Sith"),  # 36
    n("Darth Vader, Dark Lord Of The Sith"),  # 37
    n("Visage Of The Emperor"),  # 38
    n("Visage Of The Emperor"),  # 39
    n("Galen Marek, Starkiller"),  # 40
    n("Darth Maul With Lightsaber"),  # 41
    n("Darth Maul With Lightsaber"),  # 42
    n("Blizzard 4"),  # 43
    n("Evader & Monnok"),  # 44
    n("Maul's Sith Infiltrator"),  # 45
    n("Blast Door Controls"),  # 46
    n("Darth Sidious"),  # 47
    n("Count Dooku"),  # 48
    n("Count Dooku"),  # 49
    n("Masterful Move"),  # 50
    n("Sonic Bombardment", True),  # 51
    n("Sonic Bombardment", True),  # 52
    n("Galen's Lightsaber, Vader's Gift"),  # 53
    n("Blockade Flagship: Bridge"),  # 54
    n("Force Push", True),  # 55
    n("Blizzard 4"),  # 56
    n("Count Dooku"),  # 57
    n("Crush The Rebellion"),  # 58
    n("Sith Fury & End This Destructive Conflict"),  # 59
    n("Knowledge And Defense", True),  # 60
]

DS_SHIELDS = [
    n("A Useless Gesture", True),  # 1
    n("Abyss", True),  # 2
    n("Allegations Of Corruption"),  # 3
    n("Battle Order"),  # 4
    n("Come Here You Big Coward"),  # 5
    n("Do They Have A Code Clearance?", True),  # 6
    n("Resistance"),  # 7
    n("Secret Plans"),  # 8
    n("Weapon Of A Sith"),  # 9
    n("You Cannot Hide Forever", True),  # 10
    n("We'll Let Fate-a Decide, Huh?", True),  # 11
    n("Leave Them To Me", True),  # 12  box filled
    n("Death Star Sentry", True),  # 13
    n("Firepower", True),  # 14
    n("After Her!", True),  # 15
]

DS_ADD: list[tuple[str | None, bool]] = []


LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []
DS_NO_DEST: list[str] = []

NOTES = """
John Anderson / puck71, 2014 Worlds Day 2 8/23/14, 2013 form.
LS d2p1_p09 RAW (LIGHT checked). Typed.
DS d2p1_p10 HD (DARK checked). Typed with handwritten substitutions:
10 crossed printed name, Boba Fett, Prepared Hunter kept (index; written
Bounty/Prepared Hunter).
25 crossed printed name, Revenge Of The Sith (V) kept. Line 28 is a second
Revenge Of The Sith without (V).
Hidden Fortress and Jedi Tests empty both sides.
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 15, len(DS_SHIELDS)
    print("file", __file__)
    print("LS", PLAYER, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", PLAYER, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
