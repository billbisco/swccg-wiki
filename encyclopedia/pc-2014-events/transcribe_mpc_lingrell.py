#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 typed GEMP: Scott Lingrell.

Source: MPC-2014-Day-1-Main-Event.pdf pages 71–74 (typed GEMP HTML, 2 pages/side).
Holotable (Vn) dests v=True.
"""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 73
DS_PAGE = 71
LS_SCAN = "2014 Match Play Championship Day 1 Scott Lingrell LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Scott Lingrell DS.png"
LS_DECK_NAME = "HyperPod"
DS_DECK_NAME = "Surface DeFozec"
NOTE = "Typed GEMP HTML. Page 2 of 2 is shields 14–15."
LS_NOTE = (
    "Typed GEMP HTML HyperPod. Page 1 of 2 p73, page 2 of 2 p74 shields 14–15 "
    "Yavin Sentry (V1) and Your Insight Serves You Well (V1). Holotable (Vn) "
    "dests v=True. Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "The Hyperdrive Generator's Gone/We'll Need A New One dested The Hyperdrive "
    "Generator's Gone / We'll Need A New One. Tatooine (EP1) dested Tatooine (EP1). "
    "Unique overcounts sheet-accurate (Alderaan Consular Ship (V) x2, Fallen Jedi "
    "(V) x2, Imperial Atrocity (V) x2, Into The Garbage Chute, Flyboy (V) x2, Jedi "
    "Pilot (V) x2, Lando Calrissian, Unlikely Hero (V) x2, Let The Wookiee Win (V) "
    "x3, Master Qui-Gon (V) x2, Obi-Wan Kenobi, Padawan Learner (V) x2, Rebel "
    "Barrier x2, Sense x2, Wesa Gotta Grand Army x3)."
)
DS_NOTE = (
    "Typed GEMP HTML Surface DeFozec. Page 1 of 2 p71, page 2 of 2 p72 shields "
    "14–15 We'll Let Fate-a Decide, Huh? (V1) and You Cannot Hide Forever (V1). "
    "Holotable (Vn) dests v=True. Endor Operations/Imperial Outpost dested Endor "
    "Operations / Imperial Outpost. U-3PO (Yoo-Threepio) dested U-3PO (Yoo-Threepio). "
    "Slave I, Symbol of Fear (V) dested Slave I, Symbol Of Fear (V). Unique "
    "overcounts sheet-accurate (Black Sun Fleet x2, Fozec (V) x3, Imbalance & "
    "Kintan Strider (V) x2, Nevar Yalnal x3, Short Range Fighters & Watch Your "
    "Back! x3, Sonic Bombardment x2, Undercover (V) x3, We Must Accelerate Our "
    "Plans x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("A Remote Planet", True),
    n("Anakin's Podracer"),
    n("Anger, Fear, Aggression", True),
    n("Boonta Eve Podrace"),
    n("Credits Will Do Fine"),
    n("Podrace Prep"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Podrace Arena"),
    n("Tatooine: Watto's Junkyard"),
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Advantage"),
    n("Alderaan Consular Ship", True, qty=2),
    n("Artoo, Brave Little Droid", True),
    n("Blaster Deflection"),
    n("Clash Of Sabers"),
    n("Escape Pod", True),
    n("Fallen Jedi", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("I Did It!"),
    n("I Hope She's All Right"),
    n("Imperial Atrocity", True, qty=2),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Jedi Lightsaber", True),
    n("Jedi Pilot", True, qty=2),
    n("Lando Calrissian, Unlikely Hero", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order", True),
    n("Master Qui-Gon", True, qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Old Ben"),
    n("Out Of Commission & Transmission Terminated"),
    n("Lady Luck", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Rebel Barrier", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Senator Jar Jar Binks", True),
    n("Senator Leia Organa", True),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tatooine (EP1)"),
    n("Weapon Levitation"),
    n("Wesa Gotta Grand Army", qty=3),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor"),
    n("Endor Operations / Imperial Outpost"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Knowledge And Defense", True),
    n("Surface Defense", True),
    n("4-LOM With Concussion Rifle", True),
    n("According To My Design", True),
    n("Black 2", True),
    n("Black Sun Fleet", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Boba Fett, Prepared Hunter", True),
    n("Bossk", True),
    n("Cloud City: Security Tower"),
    n("Combat Response", True),
    n("Corporal Drelosyn"),
    n("DS-61-2"),
    n("Darth Maul"),
    n("Darth Vader", True),
    n("Dengar", True),
    n("Endor Shield", True),
    n("Establish Secret Base", True),
    n("Force Push", True),
    n("Fozec", True, qty=3),
    n("General Nevar", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Grand Admiral Thrawn"),
    n("Hound's Tooth", True),
    n("Imbalance & Kintan Strider", True, qty=2),
    n("Imperial Propaganda", True),
    n("Lightsaber Deficiency", True),
    n("Maul's Sith Infiltrator"),
    n("Mist Hunter", True),
    n("Naboo"),
    n("Nevar Yalnal", qty=3),
    n("Ominous Rumors"),
    n("Protocol Failure", True),
    n("Punishing One", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Slave I, Symbol Of Fear", True),
    n("Sonic Bombardment", qty=2),
    n("The Emperor", True),
    n("Jango Fett, The Assassin", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Undercover", True, qty=3),
    n("Vader's Personal Shuttle", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Zuckuss", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
