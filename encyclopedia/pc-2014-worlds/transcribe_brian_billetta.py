#!/usr/bin/env python3
"""Day 2 Xerox transcription: Brian Billetta.

Source scans: extract/day2/d2p1_p07.png (Dark, Vader's Scum) and
extract/day2/d2p1_p08.png (Light, Blue Milk). 2010 form, Worlds 2014.
(V) follows the sheet checkbox. Dittos expanded. Left-column numbering
on both sheets repeats 37/38 for form slots 37-40.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Brian Billetta"
USERNAME = ""
LS_DECK_NAME = "Blue Milk"
DS_DECK_NAME = "Vader's Scum"
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p1_p08.png"
DS_SCAN = "extract/day2/d2p1_p07.png"
PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 8
DS_PDF_PAGE = 7
LS_STARTING = ("We'll Handle This / Duel Of The Fates", True)
DS_STARTING = ("This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further", False)


# --- Dark: d2p1_p07.png. DARK checked. Vader's Scum. ---

DS_RESERVE = [
    n("This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further"),  # 1
    n("Nevar Yalnal"),  # 2  written Nivar Yalnal
    n("Masterful Move"),  # 3
    n("I Can't Shake Him!", True),  # 4
    n("ComScan Detection", True),  # 5
    n("Cold Feet", True),  # 6
    n("Stop Motion", True),  # 7
    n("Ghhhk"),  # 8
    n("Probot"),  # 9  Proloat
    n("Boba Fett, Bounty Hunter"),  # 10
    n(None),  # 11  Pawne Izzard — unread
    n("Danz Borin", True),  # 12
    n("Feltipern Trevagg"),  # 13
    n("Those Rebels Won't Escape Us", True),  # 14
    n("He Hasn't Come Back Yet"),  # 15
    n("Sergeant Merril"),  # 16  written Sergeant Meril
    n("Close Call", True),  # 17
    n("Evader"),  # 18
    n("Prince Xizor"),  # 19
    n("Prepared Defenses"),  # 20
    n("Galen Marek, Starkiller"),  # 21
    n("Garindan"),  # 22  Gyriadan / Gurdian scrawl; DS chars around it
    n("Lord Vader"),  # 23
    n("Darth Vader, Betrayer Of The Jedi"),  # 24
    n("Oo-ta Goo-ta, Solo?"),  # 25
    n("Control & Set For Stun"),  # 26
    n("Imperial Propaganda", True),  # 27
    n("Program Trap"),  # 28
    n("Protocol Failure"),  # 29
    n("Cloud City: Upper Walkway"),  # 30
    n("Hoth: Wampa Cave (7th Marker)"),  # 31
    n("Cloud City: Interrogation Room"),  # 32
    n("DSD1 Dwarf Spider Droid"),  # 33  DSP1 Dwarf Spider Droid
    n("Stinger"),  # 34
    n("Force Field", True),  # 35
    n("Dr. Evazan & Ponda Baba"),  # 36
    n("Count Dooku"),  # 37
    n("Galen Marek, Starkiller"),  # 38  player numbered 38
    n("Count Dooku"),  # 39  player numbered 37
    n("Grand Moff Tarkin", True),  # 40  player numbered 38
    n("Tentacle"),  # 41
    n("Gift Of The Master"),  # 42
    n("I'm Sorry"),  # 43
    n("Blaster Rack"),  # 44
    n("IG-88 With Riot Gun"),  # 45
    n("Come With Me"),  # 46
    n("Guri"),  # 47
    n("Blizzard 4"),  # 48
    n("Dooku's Lightsaber"),  # 49  Dooku's Saber Staff
    n("Fanblade Starfighter"),  # 50
    n("Keder The Black"),  # 51  Kedar the Black
    n("Virago"),  # 52
    n("Bossk In Hound's Tooth"),  # 53
    n("Zuckuss In Mist Hunter"),  # 54
    n("Dooku's Lightsaber"),  # 55
    n("Restraining Bolt"),  # 56
    n("Dengar In Punishing One"),  # 57
    n("Vader's Lightsaber"),  # 58  Darth Vader's Lightsaber
    n("Galen's Lightsaber, Vader's Gift"),  # 59  Galen's Lightsaber
    n("Knowledge And Defense"),  # 60  AFA also scrawled; Dark so K&D
]

DS_SHIELDS = [
    n("Weapon Of A Sith"),  # 1
    n("Secret Plans"),  # 2
    n("Come Here You Big Coward"),  # 3
    n("There Is No Try"),  # 4
    n("Battle Order"),  # 5
    n("Oppressive Enforcement"),  # 6
    n("Death Star Sentry"),  # 7
    n("Firepower"),  # 8
    n("Allegations Of Corruption"),  # 9
    n("Abyss"),  # 10
    n("Fanfare"),  # 11
]

DS_ADD: list[tuple[str | None, bool]] = []


# --- Light: d2p1_p08.png. LIGHT/DARK unchecked. Blue Milk. ---

LS_RESERVE = [
    n("We'll Handle This / Duel Of The Fates", True),  # 1
    n("Yoda, You Seek Yoda"),  # 2
    n("Double Agent"),  # 3
    n("Under Attack"),  # 4
    n("Sorry About The Mess & Blaster Proficiency"),  # 5  SATM SBlas
    n("Droid Shutdown"),  # 6
    n("Levitation", True),  # 7
    n("Mirax Terrik"),  # 8
    n("Obi-Wan Kenobi, Jedi Knight", True),  # 9  Obi-Wan JK
    n("Yoda, Senior Council Member", True),  # 10
    n("Jedi Advisor"),  # 11
    n("Jedi Advisor"),  # 12
    n("Dash Rendar"),  # 13
    n("Qui-Gon Jinn With Lightsaber"),  # 14
    n("Clone Pilot"),  # 15
    n("R2-D2 (Artoo-Detoo)", True),  # 16
    n("Senator Padme Amidala"),  # 17  Padme Amidala
    n("Obi-Wan Kenobi, Padawan Learner"),  # 18
    n("Jedi Guardian"),  # 19
    n("Yaddle"),  # 20  Yaddle Mann; no 2014 dest
    n("Alter"),  # 21
    n("Odin Nesloor"),  # 22  reads Qui-Gon; persona already on 14
    n("Republic Gunship Wing"),  # 23  Republic Gunship
    n("Eject! Eject!", True),  # 24
    n("Escape Pod", True),  # 25
    n("Jedi Levitation", True),  # 26
    n("Hear Me Baby, Hold Together", True),  # 27
    n("Jedi Lightsaber"),  # 28
    n("Jedi Lightsaber"),  # 29
    n("Jedi Lightsaber"),  # 30
    n("Vaporator"),  # 31  Evaporator
    n("Anger, Fear, Aggression", True),  # 32  Battle Plan crossed
    n("Let The Wookiee Win", True),  # 33
    n("Booster Terrik"),  # 34
    n("Acclamator-Class Assault Ship"),  # 35
    n("Booster In Pulsar Skate"),  # 36
    n("Errant Venture"),  # 37
    n("Tatooine: Jabba's Palace"),  # 38  Tatooine: I'att / Jabba's
    n("Jabba's Palace: Audience Chamber"),  # 39  player numbered 37
    n("Coruscant: Jedi Council Chamber"),  # 40  player numbered 38
    n("Kessel"),  # 41
    n("Return Of The Jedi"),  # 42
    n("Out Of Commission"),  # 43
    n("Quick Draw"),  # 44
    n("Sai'torr Kal Fas", True),  # 45
    n("The Signal", True),  # 46  written (starting)
    n("No Questions Asked", True),  # 47
    n("A Jedi's Plans"),  # 48
    n("Away Put Your Weapon", True),  # 49
    n("Commence Training"),  # 50  written (starting); Jedi Test
    n("A Gift"),  # 51
    n("C-3PO (See-Threepio)"),  # 52
    n("Houjix"),  # 53
    n("Moving To Attack Position"),  # 54
    n("I Can't Believe He's Gone"),  # 55
    n("Imperial Atrocity", True),  # 56
    n("Civil Disorder"),  # 57
    n("Obi-Wan's Lightsaber"),  # 58
    n(None, True),  # 59  Advancing — unread
    n("Rebel Barrier"),  # 60
]

LS_SHIELDS = [
    n("A Tragedy Has Occurred"),  # 1
    n("Simple Tricks And Nonsense"),  # 2
    n("Aim High"),  # 3
    n("Battle Plan"),  # 4
    n("Chasm"),  # 5
    n("Weapons Display"),  # 6
    n("Ultimatum"),  # 7
    n("Do, Or Do Not"),  # 8
    n("The Professor"),  # 9
    n("Don't Do That Again"),  # 10
    n("Only Jedi Carry That Weapon"),  # 11  Only Jedi
]

LS_ADD: list[tuple[str | None, bool]] = []


LS_UNREAD = [59]
DS_UNREAD = [11]
LS_NO_DEST: list[str] = []
DS_NO_DEST: list[str] = []

NOTES = """
Brian Billetta, 2014 Worlds, 2010 form.
DS d2p1_p07 Vader's Scum (DARK checked). Event Worlds 2014.
1 This Deal Is Getting Worse -> TDIGWATT / Pray I Don't Alter It Any Further.
2 Nivar Yalnal -> Nevar Yalnal. 9 Proloat -> Probot.
11 Pawne Izzard unread (no 2014 dest for Paw'ak / Izzard).
16 Sergeant Meril -> Sergeant Merril.
22 Gyriadan / Gurdian dested Garindan (Dark Side alien; (V) empty).
Cluster is Galen Marek, Starkiller / Garindan / Lord Vader / Darth Vader, Betrayer.
Not the Light interrupt Guardian.
31 Hoth: Wampa Cave -> Hoth: Wampa Cave (7th Marker).
32 Cloud City: Interrogation -> Interrogation Room.
33 DSP1 Dwarf Spider Droid -> DSD1 Dwarf Spider Droid.
51 Kedar the Black -> Keder The Black.
59 Galen's Lightsaber -> Galen's Lightsaber, Vader's Gift.
60 Knowledge And Defense; Anger, Fear, Aggression also scrawled (Light card).
Left-column last four form slots numbered 37, 38, 37, 38.
Shield 12 blank. Additional empty.

LS d2p1_p08 Blue Milk. LIGHT/DARK unchecked; LS from cards.
5 Sorry About The Mess SBlas -> SATM & Blaster Proficiency.
10 Yoda, Senior Council Member (written Senior Council).
17 Padme Amidala -> Senator Padme Amidala.
20 Yaddle Mann -> Yaddle (no 2014 dest).
22 reads Qui-Gon; Qui-Gon Jinn With Lightsaber already on 14 (same persona)
so taken as Odin Nesloor (Blue Milk smuggler).
23 Republic Gunship -> Republic Gunship Wing.
31 Evaporator -> Vaporator.
32 Battle Plan crossed; Anger, Fear, Aggression kept.
38 Tatooine site taken as Tatooine: Jabba's Palace (next line is JP Audience).
46 The Signal and 50 Commence Training marked (starting) in reserve.
50 Commence Training is Jedi Test 1 (2010 form has no Jedi Tests box).
55 I Can't Believe He's Gone (written I Can't Draw/Believe).
59 Advancing unread (no Advancing title; Advance Preparation possible).
Shield 11 Only Jedi -> Only Jedi Carry That Weapon (effect in shield box).
Shield 12 blank. Additional empty.
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    print("file", __file__)
    print("LS", PLAYER, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", PLAYER, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
