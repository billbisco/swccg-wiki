#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matt Schmaltz.

Source: MPC-2014-Day-1-Main-Event.pdf pages 92–93 (2013 form, 15 shields).
Name Schmaltz dested Matt Schmaltz. Username blank.
"""
from __future__ import annotations

PLAYER = "Matt Schmaltz"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 93
DS_PAGE = 92
LS_SCAN = "2014 Match Play Championship Day 1 Matt Schmaltz LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matt Schmaltz DS.png"
LS_DECK_NAME = "Your"
DS_DECK_NAME = "HDL"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Schmaltz dested Matt Schmaltz. Username blank. "
    "LIGHT checked. Deck name Your. IITFYS (V) dested It Is The Future You See (V) / "
    "A Tremor In The Force (V). Slave Quarters dested Tatooine: Slave Quarters. "
    "JCC (V) dested Coruscant: Jedi Council Chamber (V). H1 WR dested Home One: War Room. "
    "BNC dested Naboo: Boss Nass' Chambers. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. R2 R5 dested Artoo-Detoo In Red 5. "
    "BP + DTF dested Battle Plan & Draw Their Fire. DODN + WA dested Do, Or Do Not & Wise Advice. "
    "Sai'torr KF dested Sai'torr Kal Fas. Unique overcounts sheet-accurate (Mace Windu (V) x2, "
    "Luke Skywalker, Strong In The Force x2, Master Qui-Gon (V) x2, Artoo-Detoo In Red 5 x2, "
    "Clash Of Sabers x2, Blaster Deflection x2, Rebel Leadership (V) x3, Wesa Gotta Grand Army x3, "
    "Let The Wookiee Win (V) x4, A Jedi's Resilience x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Schmaltz dested Matt Schmaltz. Username blank. DARK checked. "
    "Deck name HDL. HD (V) dested Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V). "
    "Lord Vader dested Darth Vader. Galen dested Galen Marek, Starkiller. Dr + PB dested "
    "Dr. Evazan & Ponda Baba. Galen's Saber Gift dested Galen's Lightsaber, Vader's Gift. "
    "Galen's Fighter dested Rogue Shadow. SSPFT dested Something Special Planned For Them. "
    "MM + EO dested Masterful Move & Endor Occupation. One Beautiful Thing dested One Beautiful Thing. "
    "They're Still Coming Through dested They're Still Coming Through!. Seinar DS dested Sienar Fleet Systems. "
    "Imperial Barrier crossed, One Beautiful Thing replacement. Unique overcounts sheet-accurate "
    "(Darth Vader x2, Galen Marek, Starkiller x3, Emperor Palpatine x2, Blizzard 4 x2, "
    "Circle Is Now Complete x2, We Must Accelerate Our Plans x3, Force Field (V) x2). "
    "NO_DEST Thrawn; Circle Is Now Complete. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Tatooine: Slave Quarters"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Battle Plan"),
    n("Luke's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Jaina Solo"),
    n("Admiral Ackbar", True),
    n("Han, Chewie, And The Falcon", True),
    n("Lady Luck"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Anger, Fear, Aggression", True),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True),
    n("Mechanical Failure"),
    n("Strike Planning", True),
    n("What're You Tryin' To Push On Us"),
    n("Houjix"),
    n("Clash Of Sabers", qty=2),
    n("Speak With The Jedi Council"),
    n("Inconsequential Barriers"),
    n("Weapon Levitation"),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Let The Wookiee Win", True, qty=4),
    n("Hear Me Baby, Hold Together", True),
    n("Escape Pod", True),
    n("Impressive, Most Impressive", True),
    n("A Jedi's Resilience", qty=2),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("He Can Go About His Business", True),
    n("Weapons Display", True),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Chasm", True),
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader", qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Galen Marek, Starkiller", qty=3),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber"),
    n("General Nevar"),
    n("Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Bounty Hunter"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blizzard 4", qty=2),
    n("Rogue Shadow"),
    n("Victory"),
    n("Something Special Planned For Them", True),
    n("No Escape"),
    n("Revenge Of The Sith"),
    n("Protocol Failure"),
    n("Wipe Them Out, All Of Them", True),
    n("A Sith's Weapon"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("A Sith's Plans"),
    n("Circle Is Now Complete", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True),
    n("Force Lightning"),
    n("Force Push", True),
    n("Cold Feet", True),
    n("One Beautiful Thing"),
    n("Force Field", True, qty=2),
    n("One Beautiful Thing"),
    n("They're Still Coming Through!"),
    n("Sienar Fleet Systems"),
    n("Ghhhk"),
    n("Prepared Defenses", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Abyss", True),
]
DS_ADD = []
