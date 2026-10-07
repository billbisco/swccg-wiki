#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Brian Herold Xerox Hyperdrive / Contract Killers."""
from __future__ import annotations

PLAYER = "Brian Herold"
LS_USERNAME = "Carly Rae Cyrus"
DS_USERNAME = "Psy Snootles"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 26
DS_PAGE = 27
LS_SCAN = "2013 Texas Mini Worlds Day 1 p26 Brian Herold LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p27 Brian Herold DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Brian Herold. "
    "Username Carly Rae Cyrus. Deck Name Achy Breaky, Maybe?. "
    "Event Date 4/20/13. Event Name Texas Mini-Worlds. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC / Worlds / SoCal "
    "Brian Herold leftovers. "
    "Hyperdrive dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Mace Master of The Order dested Mace Windu, Master Of The Order. "
    "Qui-Gon Sinn w Saber dested Master Qui-Gon. "
    "Advantage crossed, Lando w/Ax dested Lando With Vibro-Ax. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "It's Not My Fault dested It's Not My Fault!. "
    "YISYW dested Your Insight Serves You Well. "
    "Simple Trix & Nonsense dested Simple Tricks And Nonsense. "
    "Let's Keep A Lil Optimism dested Let's Keep A Little Optimism Here. "
    "Don't Do That Again on Additional crossed, Wise Advice dested Wise Advice. "
    "Form left column reprints 37-38 on extra 37-38 are Rebel Barrier. "
    "Unique overcounts sheet-accurate: Mace Windu, Master Of The Order x2, "
    "Master Qui-Gon x2, Disarmed x2, Imperial Atrocity x3, Blaster Deflection x3, "
    "Clash Of Sabers x2, Rebel Barrier x4, Nabrun Leids x6, Sorry About The Mess x3, "
    "Sorry About The Mess & Blaster Proficiency x3, It's Not My Fault! x4, "
    "Rycar Ryjerd x2. "
    "(V) from a written v after the name; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Brian Herold. "
    "Username Psy Snootles. Deck Name WHOOPAH! Goo Nee Style. "
    "Event Date 4/20/13. Event Name Texas Mini-Worlds. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC / Worlds / SoCal "
    "Brian Herold leftovers or the TMW Steve Izzo Contract Killers leftover. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Coruscant (Special Ed) dested Coruscant. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice as written. "
    "Ket Maliss, Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Aurra Sing, (Silent but) Deadly Assassin dested Aurra Sing, Deadly Assassin. "
    "Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Mara Jade's Saber dested Mara Jade's Lightsaber. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Slave I (Direction), Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Weapon lev & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "YCHTF dested You Cannot Hide Forever. "
    "We'll let Fate-a Decide, Huh dested We'll Let Fate-a Decide, Huh?. "
    "Weapon of A Sith dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate: Arica x3, Galen, Secret Apprentice x3, "
    "Aurra Sing, Deadly Assassin x2, Trophy Of A Kill x3, Disarmed x2, "
    "Sonic Bombardment x3, Abyssin Ornament x3, Nevar Yalnal x2. "
    "(V) from a written v after the name; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Watto's Junkyard"),
    n("Credits Will Do Fine"),
    n("Krayt Dragon Howl", True),
    n("Obi-Wan Kenobi, Padawan Learner", True),
    n("Tatooine: Queen's Landing Site"),
    n("Obi-Wan's Lightsaber"),
    n("Obi-Wan's Cape", True),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Master Qui-Gon", qty=2),
    n("Senator Padme Amidala"),
    n("Bron Burs", True),
    n("Tawss Khaa", True),
    n("Guardian's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Disarmed", qty=2),
    n("Scrambled Transmission", True),
    n("Lando With Vibro-Ax"),
    n("I Hope She's All Right"),
    n("Yoda's Gimer Stick"),
    n("Advantage"),
    n("Lightsaber Proficiency"),
    n("Temporary Foothold"),
    n("Entrenchment", True),
    n("Imperial Atrocity", True, qty=3),
    n("Blaster Deflection", qty=3),
    n("Clash Of Sabers", qty=2),
    n("Rebel Barrier", qty=4),
    n("Might Of The Republic"),
    n("Nabrun Leids", qty=6),
    n("Sorry About The Mess", qty=3),
    n("Sorry About The Mess & Blaster Proficiency", qty=3),
    n("It's Not My Fault!", True, qty=4),
    n("Rycar Ryjerd", True, qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = [
    n("Wise Advice"),
    n("He Can Go About His Business", True),
    n("Do, Or Do Not"),
]

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("On The Hunt"),
    n("Prepared Defenses", True),
    n("Guild Of Assassins"),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Nal Hutta"),
    n("Coruscant: Casino"),
    n("Coruscant: Palpatine's Quarters"),
    n("Cloud City: Security Tower", True),
    n("Arica", True, qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Bane Malar", True),
    n("J'Quille", True),
    n("Keder The Black"),
    n("Greedo With Blaster Pistol"),
    n("Ket Maliss, Shadow Killer"),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Guri"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing's Blaster Rifle"),
    n("Trophy Of A Kill", qty=3),
    n("Slave I, Symbol Of Fear"),
    n("Disarmed", qty=2),
    n("Tarkin's Bounty", True),
    n("Imperial Propaganda", True),
    n("Blaster Rack", True),
    n("I've Lost Artoo!", True),
    n("Death Mark & Hutt Bounty"),
    n("One Beautiful Thing"),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", True, qty=3),
    n("Operational As Planned", True),
    n("Ghhhk"),
    n("Nevar Yalnal", qty=2),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Masterful Move"),
    n("Imbalance & Kintan Strider"),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Field", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Battle Order", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Abyss", True),
]
DS_ADD = [
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing"),
]
