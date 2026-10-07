#!/usr/bin/env python3
"""2013 World Championship Day 2: Matt Paragano Xerox Contract Killers + Hyperdrive."""
from __future__ import annotations

PLAYER = "Matt Paragano"
USERNAME = "GunganStyle"
LS_USERNAME = "GunganStyle"
DS_USERNAME = "GunganStyle"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 73
DS_PAGE = 72
LS_SCAN = "2013 Worlds Day 2 p73 Matt Paragano LS.png"
DS_SCAN = "2013 Worlds Day 2 p72 Matt Paragano DS.png"
LS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Matt Paragano. Username GunganStyle. "
    "Do not rewrite the 2013 MPC Matt Paragano leftover (On The Hunt / Leia, Rebel Princess). "
    "Deck title Hyperdrive. LIGHT. "
    "Hyperdrive / We'll need-- dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "Qui-Gon Jinn's Saber dested Qui-Gon Jinn's Lightsaber. "
    "Robots Rebel dested Rycar Ryjerd. "
    "Robots will do the dested Credits Will Do Fine. "
    "Obi-Wan, Padawan dested Obi-Wan Kenobi, Padawan Learner. "
    "Mace Windu, MOTO dested Mace Windu, Master Of The Order. "
    "Senator Jar Jar dested Senator Jar Jar Binks. "
    "Senator Padme Amidala dested Senator Padme Amidala. "
    "Inconsequential Barriers dested Inconsequential Barriers. "
    "After dested Alter. "
    "Line 41 fully struck omitted. "
    "Either Way you Win dested Either Way, You Win. "
    "Houjix & OON dested Houjix & Out Of Nowhere. "
    "Into the Garbage Chute dested Into The Garbage Chute, Flyboy. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Obi-Wan's Cape dested Obi-Wan's Cape. "
    "Hidden Fortress empty. Jedi Tests empty. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Matt Paragano. Username GunganStyle. "
    "Do not rewrite the 2013 MPC Matt Paragano leftover. "
    "Deck title Contract Killers. DARK. "
    "Contract Killers/Feared dested Contract Killers / Feared Throughout The Galaxy. "
    "Coruscant: Sub City Lair dested Coruscant: Sub City Lair. "
    "Coruscant Sp (DB) dested Coruscant: Docking Bay. "
    "Slave I, Symbol of fear dested Slave I, Symbol Of Fear. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. "
    "Galen Marek, Starkiller dested Galen Marek, Starkiller. "
    "Boba Fett, Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Mara Jade's Saber dested Mara Jade's Lightsaber. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "I've lost Artoo dested I've Lost Artoo!. "
    "Slo Motion dested Stop Motion. "
    "Nenin Yalnal dested Nevar Yalnal. "
    "Abyss in Ornament dested Abyssin Ornament. "
    "Land Debreed & Sacafie dested Lana Dobreed & Sacrifice. "
    "Inaccurate? dested as written. "
    "Short range fighters & WYB dested Short Range Fighters & Watch Your Back!. "
    "Ghhhk & Those rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Shield 10 Wipe Them Out, All Of Them kept as extra Effect. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "We'll Let Fate-a Decide, huh? dested We'll Let Fate-a Decide, Huh?. "
    "Hidden Fortress empty. Jedi Tests empty. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Coruscant: Jedi Council Chamber"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Watto's Junkyard"),
    n("Naboo: Boss Nass' Chambers"),
    n("Guardian's Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Elegant Lightsaber", True),
    n("Rycar Ryjerd", True),
    n("A Remote Planet", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Anger, Fear, Aggression", True),
    n("Credits Will Do Fine", True),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("Meditation"),
    n("Lightsaber Proficiency"),
    n("Advantage"),
    n("Obi-Wan's Cape", True),
    n("Much To Learn, You Still Have", True),
    n("Aayla Secura", True, qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Lando With Vibro-Ax"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Master Qui-Gon", True, qty=2),
    n("Maris Brood, Fallen Jedi", True, qty=2),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Ki-Adi-Mundi", True),
    n("Senator Jar Jar Binks", True),
    n("Senator Padme Amidala", True),
    n("Inconsequential Barriers"),
    n("Alter"),
    n("Heading For The Medical Frigate", True),
    n("Either Way, You Win", True),
    n("Houjix & Out Of Nowhere"),
    n("Dodge", True),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Blaster Deflection", qty=3),
    n("Corellian Slip", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Jedi Levitation", True, qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense", True),
    n("Planetary Defenses", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Casino", True),
    n("Coruscant: Sub City Lair", True),
    n("Coruscant: Docking Bay"),
    n("Slave I, Symbol Of Fear", True),
    n("Zuckuss In Mist Hunter"),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Aurra Sing, Deadly Assassin", True, qty=2),
    n("Arica", True, qty=3),
    n("Jango Fett, The Assassin", True),
    n("J'Quille", True, qty=2),
    n("Ket Maliss, Shadow Killer", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Bane Malar", True),
    n("Guri"),
    n("Aurra Sing's Blaster Rifle"),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Trophy Of A Kill", True, qty=3),
    n("A Sith's Weapon", True),
    n("I've Lost Artoo!", True),
    n("Knowledge And Defense", True),
    n("Blaster Rack", True),
    n("Gift Of The Master", True),
    n("Death Mark & Hutt Bounty", True),
    n("Jabba's Haven", True),
    n("Guild Of Assassins", True),
    n("On The Hunt", True),
    n("Stop Motion", True),
    n("Force Push", True),
    n("Imbalance & Kintan Strider", True, qty=2),
    n("Nevar Yalnal", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Abyssin Ornament", True, qty=3),
    n("Lightsaber Deficiency", True),
    n("Prepared Defenses"),
    n("Lana Dobreed & Sacrifice", True),
    n("Force Lightning"),
    n("Inaccurate?", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Cold Feet", True),
    n("Dark Maneuvers"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("After Her", True),
    n("Abyss", True),
    n("There Is No Try", True),
    n("Come Here You Big Coward"),
    n("Resistance", True),
    n("Fanfare"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans", True),
    n("Allegations Of Corruption"),
    n("Death Star Sentry", True),
]
DS_ADD = [
    n("Wipe Them Out, All Of Them"),
]
