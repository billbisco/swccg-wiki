#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Tom Haid.

Source: MPC-2014-Day-1-Main-Event.pdf pages 49–50 (2013 form, 15 shields).
Username Xonth.
"""
from __future__ import annotations

PLAYER = "Tom Haid"
USERNAME = "Xonth"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 49
DS_PAGE = 50
LS_SCAN = "2014 Match Play Championship Day 1 Tom Haid LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Tom Haid DS.png"
LS_DECK_NAME = "Hyperdrive has the best art ever"
DS_DECK_NAME = "Not Slavers"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username Xonth. Hyperdrive dested The Hyperdrive Generator's "
    "Gone / We'll Need A New One. HFTMF dested Heading For The Medical Frigate (V). Remote "
    "Planet dested A Remote Planet (V). Control & TV dested Control & Tunnel Vision. OOC & "
    "TT dested Out Of Commission & Transmission Terminated. Yoda Stew combo dested Yoda "
    "Stew. Sat Mess dested Sorry About The Mess. Alter (EP1) dested Alter (V). Into the "
    "Garbage Chute dested Into The Garbage Chute, Flyboy (V). (V) from checkbox. Unique "
    "overcounts sheet-accurate (Mace Windu, Master Of The Order (V) x2, Obi-Wan Kenobi, "
    "Padawan Learner (V) x2, Master Qui-Gon (V) x2, Imperial Atrocity (V) x2, A Jedi's "
    "Resilience x3, Rebel Barrier x2, Wesa Gotta Grand Army x3, Sorry About The Mess x2, "
    "Clash Of Sabers x2, Blaster Deflection x2, Into The Garbage Chute, Flyboy (V) x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username Xonth. Court of the Vile Gangster dested Court Of "
    "The Vile Gangster. Ni Chuba Na?? dested Ni Chuba Na?? (V). Myo K'ynugh dested Myo. "
    "Cloud City Engineer LOYWAT dested Cloud City Engineer. Dr E Combo dested Dr. Evazan "
    "& Ponda Baba. Jango Fett the Assassin dested Jango Fett, The Assassin (V). Slave I "
    "SoF dested Slave I, Symbol Of Fear (V). Sniper combo dested Sniper & Dark Strike. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. Short Range Fighters combo "
    "dested Short Range Fighters & Watch Your Back!. P-59 dested P-59. (V) from checkbox. "
    "Unique overcounts sheet-accurate (Emperor Palpatine x2, EPP Maul x2, Mara Jade x2, "
    "Blizzard 4 x2, Lightsaber Deficiency (V) x2, Force Field (V) x2, Sith Fury (V) x2, "
    "None Shall Pass (V) x2, Imperial Barrier x2, Nevar Yalnal x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Credits Will Do Fine"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("A Remote Planet", True),
    n("Heading For The Medical Frigate", True),
    n("Anger, Fear, Aggression", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Senator Palpatine", True),
    n("Senator Jar Jar Binks", True),
    n("Dorme", True),
    n("Meris Bood", True),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Guardian's Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Disarmed"),
    n("Advantage"),
    n("Imperial Atrocity", True, qty=2),
    n("Sorry About The Mess"),
    n("Surprise Assault"),
    n("Might Of The Republic"),
    n("A Jedi's Resilience", qty=3),
    n("Mechanical Failure"),
    n("Dark Approach", True),
    n("Rebel Barrier", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Sorry About The Mess", qty=2),
    n("Nabrun Leids"),
    n("Out Of Commission & Transmission Terminated"),
    n("Yoda Stew"),
    n("Clash Of Sabers", qty=2),
    n("Blaster Deflection", qty=2),
    n("Control & Tunnel Vision"),
    n("Sense"),
    n("Alter", True),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Lucky Shot", True),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Aim High"),
    n("He Can Go About His Business"),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Court Of The Vile Gangster / I Shall Enjoy Watching You Die"
DS_CARDS = [
    n("Court Of The Vile Gangster / I Shall Enjoy Watching You Die"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Tatooine: Great Pit Of Carkoon"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven", True),
    n("I've Lost Artoo!", True),
    n("Knowledge And Defense", True),
    n("Kir Kanos With Force Pike", True),
    n("Myo", True),
    n("Rodian", True),
    n("Garindan", True),
    n("Emperor Palpatine", qty=2),
    n("Darth Sidious"),
    n("Cloud City Engineer"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Mara Jade", qty=2),
    n("Nal Hutta"),
    n("Coruscant: Docking Bay"),
    n("Executor: Docking Bay"),
    n("Death Star II: Docking Bay"),
    n("Disarmed"),
    n("Protocol Failure", True),
    n("Maul's Cape", True),
    n("Trophy Of A Kill", True),
    n("Mara Jade's Lightsaber", True),
    n("Blizzard 4", qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Sniper & Dark Strike"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Push", True),
    n("Force Field", True, qty=2),
    n("Sith Fury", True, qty=2),
    n("Sonic Bombardment", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("None Shall Pass", True, qty=2),
    n("Imperial Barrier", qty=2),
    n("Force Lightning"),
    n("Nevar Yalnal", qty=2),
    n("Abyssin Ornament"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Resistance"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
]
DS_ADD = []
