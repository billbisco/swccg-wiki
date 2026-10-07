#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Matt Paragano Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Matt Paragano"
USERNAME = "GunganStyle"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 70
DS_PAGE = 69
LS_SCAN = "2013 Match Play Championship p70 Matt Paragano LS.png"
DS_SCAN = "2013 Match Play Championship p69 Matt Paragano DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Matt Paragano. Username GunganStyle. "
    "Event MPC Day 1, dated 1/26/13. Light. Deck title I didn't playtest this at all. "
    "Starting Leia, Rebel Princess; Threepio w/ cape; SATM. "
    "Threepio w/ cape dested C-3PO (See-Threepio). "
    "Blind Jedi dested Rahm Kota, Blind Jedi. "
    "Padme dested Padme Naberrie. Luke's Blaster dested Luke's Blaster Pistol. "
    "Booster in Pulsar Skate dested Booster In Pulsar Skate. "
    "A Good Blaster -- dested A Good Blaster At Your Side. "
    "Light Eject & TA dested Eject! Eject!. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas. AFA dested Anger, Fear, Aggression. "
    "SATM dested Sorry About The Mess. "
    "Yoda stew & YIHTYM dested Yoda Stew & You Do Have Your Moments. "
    "Houjix & OON dested Houjix & Out Of Nowhere. "
    "Bith Shuffle & Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Control & Tunnel Vision dested Control & Tunnel Vision. "
    "He can go about his business dested He Can Go About His Business. "
    "Your Insight Serves dested Your Insight Serves You Well. "
    "Simple Tricks and Nonsense dested Simple Tricks And Nonsense. "
    "Jabbas Prize dested Jabba's Prize. "
    "Line 36 writes Tatooine and Coruscant on one line; dested Tatooine (Coruscant squeezed on the same slot). "
    "Form left column reprints 37–38 on lines 39–40 are Tatooine: Slave Quarters and The Bith Shuffle & Desperate Reach. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Matt Paragano. Username GunganStyle. "
    "Event MPC Day 1, dated 1/26/13. Dark. Deck title My wife picked these out for me. "
    "Starting On The Hunt (V); Knowledge And Defense (V); Trophy Of A Kill (V). "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift "
    "(Gift overflows onto the Aurra Blaster Rifle line). "
    "Aurra Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Weapon Levitation & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider. "
    "Slave I, Symbol of fear dested Slave I, Symbol Of Fear. "
    "Ket Maliss, Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Keeper The Black dested Keder The Black. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Coruscant: Sub City layer dested Coruscant: Private Platform (Docking Bay). "
    "Nall Itutta dested Nal Hutta. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Death Mark & Hutt Bounty dested Death Mark & Hutt Bounty. "
    "I've lost Artoo dested I've Lost Artoo!. "
    "Mara Jade's Lightsaber dested Mara Jade's Lightsaber. "
    "I Find Your Lack of faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "Do They have a Code Clearance dested Do They Have A Code Clearance?. "
    "Come Here you big Coward dested Come Here You Big Coward. "
    "Form left column reprints 37–38 on lines 39–40 are Arica and Mara Jade's Lightsaber. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Leia, Rebel Princess"
LS_CARDS = [
    n("Leia, Rebel Princess"),
    n("C-3PO (See-Threepio)"),
    n("Shmi Skywalker"),
    n("Rahm Kota, Blind Jedi", True),
    n("Yoda, Great Warrior", True, qty=2),
    n("Princess Leia", True),
    n("Padme Naberrie", True, qty=3),
    n("Luke Skywalker, Rebel Hero", True, qty=2),
    n("Han Solo", True, qty=2),
    n("Talon Karrde"),
    n("Mirax Terrik"),
    n("Master Kenobi"),
    n("Luke's Blaster Pistol", True),
    n("Naboo Blaster Rifle", qty=2),
    n("Stun Blaster"),
    n("Jedi Lightsaber", True),
    n("Leia's Blaster Rifle"),
    n("Han's Heavy Blaster Pistol", True),
    n("Home One"),
    n("Booster In Pulsar Skate", True),
    n("A Good Blaster At Your Side", True),
    n("Eject! Eject!", True),
    n("Sai'torr Kal Fas"),
    n("Superficial Damage", True),
    n("Advantage"),
    n("Thrown Back", True),
    n("Anger, Fear, Aggression", True),
    n("Communing", True),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Tosche Station"),
    n("Tatooine: Slave Quarters"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Sorry About The Mess"),
    n("Use The Force", True, qty=3),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Rebel Barrier"),
    n("It Can Wait"),
    n("Slight Weapons Malfunction"),
    n("Don't Forget The Droids", True),
    n("A Jedi's Concentration"),
    n("Nabrun Leids"),
    n("Houjix & Out Of Nowhere"),
    n("Alter", True),
    n("Sense"),
    n("Changing The Odds"),
    n("Jedi Presence"),
    n("Weapon Levitation"),
    n("Control & Tunnel Vision"),
    n("Blaster Proficiency", qty=2),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense", True),
    n("Affect Mind"),
    n("Another Pathetic Lifeform", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "On The Hunt"
DS_CARDS = [
    n("On The Hunt", True),
    n("Knowledge And Defense", True),
    n("Blaster Rack", True),
    n("Disarmed", qty=2),
    n("A Sith's Weapon", True),
    n("Guild Of Assassins", True),
    n("Jabba's Haven", True),
    n("I've Lost Artoo!", True),
    n("Trophy Of A Kill", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Prepared Defenses", True),
    n("Masterful Move"),
    n("Operational As Planned", True),
    n("Weapon Levitation & The Empire's Back", True),
    n("Cold Feet", True),
    n("Nevar Yalnal", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Force Field", True),
    n("Lightsaber Deficiency", True),
    n("Force Push", True),
    n("Ghhhk"),
    n("Abyssin Ornament", True, qty=3),
    n("Imbalance & Kintan Strider", True, qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Ket Maliss, Shadow Killer", True),
    n("Bane Malar", True),
    n("Keder The Black"),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Arica", True, qty=3),
    n("Mara Jade's Lightsaber"),
    n("Death Mark & Hutt Bounty", True),
    n("Gift Of The Master", True),
    n("Coruscant"),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Rodian", True),
    n("J'Quille", True),
    n("Guri"),
    n("Aurra Sing, Deadly Assassin", True, qty=2),
    n("Cloud City: Security Tower", True),
    n("Coruscant: Casino", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Nal Hutta"),
    n("Contract Killers / Feared Throughout The Galaxy", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
