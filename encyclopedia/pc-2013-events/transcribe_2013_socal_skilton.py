#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Steve Skilton Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 35
DS_PAGE = 36
LS_SCAN = "2013 SoCal Grand Prix Day 1 p35 Steve Skilton LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p36 Steve Skilton DS.png"
LS_NOTE = (
    "Handwritten Print Form. Deck Name Desa's Sunn V. "
    "It is the Future you see → It Is The Future You See. "
    "Lando, Unlikely → Lando Calrissian, Unlikely Hero. "
    "Master Qui Gon → Master Qui-Gon. Mace MOTO → Mace Windu, Master Of The Order. "
    "Luke SITF → Luke Skywalker, Strong In The Force. Leia RP → Leia, Rebel Princess. "
    "LSJK → Luke Skywalker, Jedi Knight. Battle Plan Combo → Battle Plan & Draw Their Fire. "
    "Wise Advice Combo → Do, Or Do Not & Wise Advice. Seeking → Seeking An Audience. "
    "Strike Force → Strikeforce. Sai'torr → Sai'torr Kal Fas. Atrocity → Imperial Atrocity. "
    "Mech Failure → Mechanical Failure. Battle Plains → Naboo: Battle Plains. "
    "AJR → A Jedi's Resilience. Clash → Clash Of Sabers. Hear Me Baby → Hear Me Baby, Hold Together. "
    "Jedi Lev → Jedi Levitation. SATM combo → Sorry About The Mess & Blaster Proficiency. "
    "Speak w/ Council → Speak With The Jedi Council. LTWW → Let The Wookiee Win. "
    "GCC → Coruscant: Jedi Council Chamber. Slave Quarters → Jabba's Palace: Slave Quarters. "
    "Y4: WR → Yavin 4: War Room. Nass' Chambers → Naboo: Boss Nass' Chambers. "
    "Home 1: WR → Home One: War Room. HCF → Han, Chewie, And The Falcon. "
    "ITG → I Thought They Smelled Bad On The Outside. R2 in R5 → Artoo-Detoo In Red 5. "
    "Qui's Biii Saber → Qui-Gon Jinn's Lightsaber. (V) from the checkbox. Shields empty."
)
DS_NOTE = (
    "Handwritten Print Form. HD → Hunt Down And Destroy The Jedi / "
    "Their Fire Has Gone Out Of The Universe. Executor: Med Chamber → Executor: Meditation Chamber. "
    "Prepared Def → Prepared Defenses. MM combo → Masterful Move. WMAOP → We Must Accelerate Our Plans. "
    "Boba Fett, BH → Boba Fett, Bounty Hunter. Line 11 struck (why not in margin); "
    "4-LOM With Concussion Rifle remains dested as the 60th card. "
    "Cum Scum → Scum And Villainy. Sonic B → Sonic Bombardment. "
    "GHHHHHHHHHHK → Ghhhk. Super Combo → Superlaser. Gift of the Master → Gift Of The Mentor. "
    "Phantom Menace → The Phantom Menace. Visage of the Emp → Visage Of The Emperor. "
    "RotS → Revenge Of The Sith. Ni Clube Na → Ni Chuba Na?. "
    "Emp Maul → Darth Maul. Duelots → Dual Laser Cannon. "
    "Vader betrayer → Darth Vader, Betrayer Of The Jedi. D-59 → P-59. "
    "Emp Mara → Mara Jade With Lightsaber. Emp Palp → Emperor Palpatine. "
    "Dr E combo → Dr. Evazan & Ponda Baba. Back Door → Endor: Back Door. "
    "DS: WR → Death Star: War Room. CC: Security Tower → Cloud City: Security Tower. "
    "BF: Bridge → Blockade Flagship: Bridge. Blizz 4 → Blizzard 4. "
    "Sidious' Saber → Darth Sidious' Lightsaber. K+D → Knowledge And Defense. "
    "(V) from the checkbox. Shields empty."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("It Is The Future You See", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Seeking An Audience", True),
    n("Strikeforce", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Imperial Atrocity", True, qty=2),
    n("Mechanical Failure"),
    n("Naboo: Battle Plains"),
    n("A Jedi's Resilience", qty=2),
    n("Houjix"),
    n("Clash Of Sabers"),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("Jedi Levitation", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Speak With The Jedi Council", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Coruscant: Jedi Council Chamber", True),
    n("Jabba's Palace: Slave Quarters"),
    n("Yavin 4: War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", True),
    n("I Thought They Smelled Bad On The Outside", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Lady Luck"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Prepared Defenses"),
    n("Force Field", True),
    n("Force Lightning"),
    n("Masterful Move"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Scum And Villainy", True),
    n("Sonic Bombardment", True, qty=2),
    n("Ghhhk"),
    n("Superlaser"),
    n("Force Push", True),
    n("Gift Of The Mentor"),
    n("A Sith's Weapon"),
    n("The Phantom Menace"),
    n("Visage Of The Emperor", qty=3),
    n("Emperor's Power", True),
    n("Conduct Your Search"),
    n("Revenge Of The Sith"),
    n("No Escape"),
    n("Ni Chuba Na?", True),
    n("Blaster Rack", True),
    n("Blast Door Control"),
    n("First Strike"),
    n("Darth Maul", qty=3),
    n("Dual Laser Cannon", qty=3),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("P-59"),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine", qty=3),
    n("Darth Sidious", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan"),
    n("Janus Greejatus"),
    n("Endor: Back Door"),
    n("Death Star: War Room", True),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Blizzard 4", qty=2),
    n("No Escape"),
    n("Vader's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = []
DS_ADD = []
