#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 typed GEMP: Ross Littauer.

Source: MPC-2014-Day-1-Main-Event.pdf pages 75–76 (typed GEMP).
"""
from __future__ import annotations

PLAYER = "Ross Littauer"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 76
DS_PAGE = 75
LS_SCAN = "2014 Match Play Championship Day 1 Ross Littauer LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Ross Littauer DS.png"
NOTE = "Typed GEMP list."
LS_NOTE = (
    "Typed GEMP. It Is The Future You See (V). Gift Of The Mentor dested Gift Of "
    "The Master. Tanus Spijek (V) crossed, skipped. Precise Hit (V) crossed, skipped. "
    "Flash Of Insight (V) crossed, Scrambled Transmission (V) dested Scrambled "
    "Transmission (V). Admiral Ackbar (V) handwritten dested Admiral Ackbar (V). "
    "Home One handwritten in ships dested Home One. Unique * is uniqueness, not (V). "
    "(V) from written (V). Unique overcounts sheet-accurate (Yoda, Great Warrior x2, "
    "Chewbacca, Protector x2, Obi-Wan Kenobi (V) x2, Jedi Presence x2, Courage Of A "
    "Skywalker x2, Rebel Leadership (V) x2, NOOOOOOOOOOOO! (V) x2, You Will Go To "
    "The Dagobah System (V) x4, Escape Pod (V) x2, Wesa Gotta Grand Army x3, Let The "
    "Wookiee Win (V) x2, Stone Pile x2)."
)
DS_NOTE = (
    "Typed GEMP. Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The "
    "Universe (V). Omni Box dested Omni Box & It's Worse. Galen's Lightsaber, "
    "Vader's Gift dested Galen's Lightsaber, Vader's Gift. Unique overcounts "
    "sheet-accurate (Emperor Palpatine x2, Darth Vader, Dark Lord Of The Sith x2, "
    "Grand Moff Tarkin (V) x2, Galen Marek, Starkiller x3, We Must Accelerate Our "
    "Plans x2, Force Field (V) x2). (V) from written (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Treva Horme"),
    n("Threepio With His Parts Showing"),
    n("IL-19"),
    n("Yoda, Great Warrior", qty=2),
    n("Chewbacca, Protector", qty=2),
    n("Luke Skywalker, Rebel Scout", True),
    n("Corran Horn"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Admiral Ackbar", True),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Stone Pile", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Lightsaber Proficiency"),
    n("Anger, Fear, Aggression", True),
    n("Mechanical Failure"),
    n("Scrambled Transmission", True),
    n("It Is The Future You See", True),
    n("Gift Of The Master"),
    n("Jedi Presence", qty=2),
    n("Control & Tunnel Vision"),
    n("Houjix"),
    n("Courage Of A Skywalker", qty=2),
    n("Clash Of Sabers"),
    n("Rebel Leadership", True, qty=2),
    n("NOOOOOOOOOOOO!", True, qty=2),
    n("Nabrun Leids"),
    n("You Will Go To The Dagobah System", True, qty=4),
    n("Escape Pod", True, qty=2),
    n("Sense"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Either Way, You Win", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Dagobah: Yoda's Hut"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Jedi Lightsaber", True),
    n("Chewbacca's Bowcaster"),
    n("Luke's Lightsaber"),
    n("Home One"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Boba Fett, Bounty Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Dengar With Blaster Carbine", True),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine", qty=2),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Galen Marek, Starkiller", qty=3),
    n("Blaster Rack", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("No Escape"),
    n("A Sith's Weapon"),
    n("Endor Shield", True),
    n("A Sith's Plans"),
    n("Revenge Of The Sith"),
    n("Something Special Planned For Them", True),
    n("Astromech Shortage", True),
    n("Wipe Them Out, All Of Them", True),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
    n("Ghhhk"),
    n("You Are Beaten"),
    n("Force Push", True),
    n("Lightsaber Deficiency", True),
    n("Imbalance & Kintan Strider"),
    n("We Must Accelerate Our Plans", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("One Beautiful Thing"),
    n("Force Lightning"),
    n("Weapon Levitation & The Empire's Back"),
    n("Omni Box & It's Worse"),
    n("Force Field", True, qty=2),
    n("Prepared Defenses", True),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Generator Core"),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Endor"),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Victory"),
    n("Rogue Shadow"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
    n("After Her!", True),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
