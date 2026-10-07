#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matt Paragano.

Source: MPC-2014-Day-1-Main-Event.pdf pages 84–85 (2013 form, 15 shields).
Username SugarStyle.
"""
from __future__ import annotations

PLAYER = "Matt Paragano"
USERNAME = "SugarStyle"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 85
DS_PAGE = 84
LS_SCAN = "2014 Match Play Championship Day 1 Matt Paragano LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matt Paragano DS.png"
LS_DECK_NAME = "Hyperdrive"
DS_DECK_NAME = "A stunning Maul"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username SugarStyle. Deck name Hyperdrive. LIGHT checked. "
    "Event MPC 14 01/25/14. Hyperdrive dested The Hyperdrive Generator's Gone. "
    "Odin Nesloor & FA dested Odin Nesloor & First Aid. SATM dested Sorry About The Mess. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. Clash of the Sabers dested "
    "Clash Of Sabers. Into The Garbage Chute dested Into The Garbage Chute, Flyboy!. "
    "Senator Padme dested Senator Padme Amidala. Senator Jar Jar dested Senator Jar Jar Binks. "
    "Obi-Wan Padawan dested Obi-Wan Kenobi, Padawan Learner. Capt. Rex dested Captain Rex. "
    "Mace Windu MOTO dested Mace Windu, Master Of The Order. Guardian's Saber dested "
    "Guardian's Lightsaber. Lightsaber Prof. dested Lightsaber Proficiency. Meditation dested "
    "Meditation. Advantage dested Advantage. Unique overcounts sheet-accurate "
    "(Escape Pod (V) x2, Wesa Gotta Grand Army x2, Blaster Deflection x2, Either Way, You Win (V) x2, "
    "Old Ben x2, Sense x2, Sorry About The Mess x2, Jedi Levitation (V) x3, Obi-Wan Kenobi, "
    "Padawan Learner (V) x2, Mace Windu, Master Of The Order (V) x2, Master Qui-Gon (V) x2, "
    "Anakin Skywalker, Padawan Learner (V) x2). NO_DEST The Hyperdrive Generator's Gone; Maris Brood (V); Captain Rex (V). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username SugarStyle. Deck name A stunning Maul. DARK checked. "
    "A Stunning Move / --- (V) dested A Stunning Move (V) / A Valuable Hostage (V). "
    "Cor: Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Cor: Private Landing Platform dested Coruscant: Private Platform. "
    "Cyborg Commander's Saber dested Grievous' Lightsabers. Slave I, SOF dested "
    "Slave I, Symbol Of Fear. Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. Galen, Starkiller dested "
    "Galen Marek, Starkiller. K&D dested Knowledge And Defense. "
    "I've Lost Artoo dested I've Lost Artoo!. Join Me dested Join Me!. "
    "Imbalance & Kintan dested Imbalance & Kintan Strider. Unique overcounts sheet-accurate "
    "(Sonic Bombardment (V) x2, Grievous, Hunter Of Jedi (V) x3, Galen Marek, Starkiller (V) x3, "
    "Count Dooku (V) x2, Battle Droid Squad (V) x2, IG-100 MagnaGuard (V) x2, Darth Maul x2). "
    "NO_DEST Resonating Box. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone"),
    n("Rycar Ryjerd", True),
    n("A Remote Planet", True),
    n("Quick Draw", True),
    n("Credits Will Do Fine"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Heading For The Medical Frigate", True),
    n("Rebel Barrier"),
    n("Odin Nesloor & First Aid", True),
    n("It's Not My Fault", True),
    n("Escape Pod", True, qty=2),
    n("A Jedi's Resilience"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Blaster Deflection", qty=2),
    n("Might Of The Republic"),
    n("Houjix"),
    n("Either Way, You Win", True, qty=2),
    n("Old Ben", qty=2),
    n("Sense", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Jedi Levitation", True, qty=3),
    n("Clash Of Sabers"),
    n("Into The Garbage Chute, Flyboy!", True),
    n("Aayla Secura", True),
    n("Maris Brood", True),
    n("Senator Padme Amidala", True),
    n("Senator Jar Jar Binks", True),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Captain Rex", True),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Dorme", True),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan's Lightsaber"),
    n("Guardian's Lightsaber", True),
    n("Anakin's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True),
    n("Advantage"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon", True),
    n("Do, Or Do Not"),
    n("Yavin Sentry"),
    n("Let's Keep A Little Optimism Here"),
    n("He Can Go About His Business", True),
    n("Battle Plan"),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Private Platform", True),
    n("Kashyyyk"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower", True),
    n("Hoth: Ice Plains"),
    n("The Phantom Menace"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("A Sith's Weapon", True),
    n("A Sith's Plans", True),
    n("Imperial Justice", True),
    n("Something Special Planned For Them", True),
    n("Gift Of The Master", True),
    n("I've Lost Artoo!", True),
    n("Trophy Of A Kill", True),
    n("Resonating Box"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Dooku's Lightsaber", True),
    n("Grievous' Lightsabers", True),
    n("Slave I, Symbol Of Fear", True),
    n("Maul's Sith Infiltrator"),
    n("A Dark Time For The Rebellion", True),
    n("I Have You Now"),
    n("Prepared Defenses", True),
    n("Join Me!", True),
    n("Sonic Bombardment", True, qty=2),
    n("Imbalance & Kintan Strider", True),
    n("Insidious Prisoner"),
    n("Force Push", True),
    n("Cold Feet", True),
    n("You Are Beaten"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Force Field", True),
    n("Dr. Evazan & Ponda Baba", True),
    n("Grievous, Hunter Of Jedi", True, qty=3),
    n("Dengar With Blaster Carbine", True),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Count Dooku", True, qty=2),
    n("P-59"),
    n("Battle Droid Squad", True, qty=2),
    n("IG-100 MagnaGuard", True, qty=2),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Darth Maul, Young Apprentice"),
    n("Darth Maul", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("Wipe Them Out, All Of Them"),
    n("You Cannot Hide Forever"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Fanfare", True),
    n("After Her!", True),
    n("Battle Order"),
]
DS_ADD = []
