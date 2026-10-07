#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Adam Howland.

Source: 2012mpcday1.pdf pages 87–88.
Name Adam Howland dested Adam Howland (analog generate empty).
p87 Light Hidden Base notebook. p88 Dark Agents Of Black Sun 2010 Xerox.
Username MASTERJEDIADAM. Pack player-stubs/Adam_Howland.wiki.
"""
from __future__ import annotations

PLAYER = "Adam Howland"
USERNAME = "MASTERJEDIADAM"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 87
DS_PAGE = 88
LS_SCAN = "2012 Match Play Championship Day 1 Adam Howland LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Adam Howland DS.png"
LS_DECK_NAME = "My Base Is Hidden (TYHT)"
DS_DECK_NAME = "The Surgeon's Shadow (TYJAN)"
NOTE = "p87 handwritten notebook 60. p88 handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten notebook. Name Adam Howland dested Adam Howland. "
    "Username MASTER JEDI ADAM. LIGHT checked. Deck Name My Base Is Hidden (TYHT). "
    "Event 11 Feb 12 / 2012 MPC. Analog generate empty. "
    "Line 1 cropped remnant Hidden Base / Systems dested Hidden Base / Systems Will Slip Through Your Fingers. "
    "(V) written dest True. Polite dested Polite True. "
    "Luke Skywalker, JK dested Luke Skywalker, Jedi Knight x4. "
    "Mace Windu dested Mace Windu True x2. Hail Scff dested Han With Heavy Blaster Pistol True. "
    "Boshek, Blash Smuggler dested BoShek, Brash Smuggler. "
    "Boshek's Mod. Light Freighter dested BoShek's Modified Freighter. "
    "Wedge in Red Sqdn 1 dested Wedge In Red Squadron 1. "
    "Sorry About The Mess & BP dested Sorry About The Mess & Blaster Proficiency x2. "
    "All Wings Report In & DS dested All Wings Report In & Darklighter Spin x4. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas True. Evac Control dested Evacuation Control True. "
    "Only Jedi Carry dested Only Jedi Carry That Weapon. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name ADAM HOWLAND dested Adam Howland. "
    "Username MASTERJEDIADAM. DARK checked. Deck Name The Surgeon's Shadow (TYJAN). "
    "Event Date 11/Feb/12 Event Name 2012 MPC. Analog generate empty. "
    "Line 1 cropped AOBS dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Coruscant (SE) dested Coruscant (Dark). C: Imperial City dested Coruscant: Imperial City. "
    "Prep Defences dested Prepared Defenses True. Destinic Tattoo dested Tatooine True. "
    "DS: WR dested Death Star: War Room True. C: Imperial Square dested Coruscant: Imperial Square. "
    "Prince Xizor True then empty kept separate. Guri dested Guri True x2. "
    "Ponda Baba True and Dr. Evazan empty kept separate. "
    "Veliken dested Velken Tezeri True. Emperor Palpatine dested Emperor Palpatine x4. "
    "Boba Fett, BH dested Boba Fett, Bounty Hunter x2. 4-LOM w/ Gun dested 4-LOM With Concussion Rifle True. "
    "Dengar w/ Blaster dested Dengar With Blaster Carbine True x2. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun. Mauls Enfiltrator dested Maul's Sith Infiltrator. "
    "Bossk in Bus dested Bossk In Hound's Tooth True. IHO dested I Have You Now. "
    "Imbalance & Kintan dested Imbalance. YPAW dested Your Powers Are Weak, Old Man True. "
    "Unexpected Interrogat dested Unexpected Interruption x2. "
    "Ommni Box & It's dested Ommni Box & It's Worse. "
    "CHYBC dested Come Here You Big Coward. Code Clearance dested Do They Have A Code Clearance? True. "
    "Line 40 cropped; dest unique 59. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Squadron Assignments"),
    n("Rycar Ryjerd", True),
    n("Cloud City: Lower Corridor"),
    n("Dressel"),
    n("Polite", True),
    n("Kessel"),
    n("Corulag"),
    n("Naboo"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Han With Heavy Blaster Pistol", True),
    n("BoShek, Brash Smuggler"),
    n("Mirax Terrik"),
    n("Captain Han Solo"),
    n("Chewie", True),
    n("Luke's Bionic Hand", qty=2),
    n("Obi-Wan's Journal"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("X-Wing Laser Cannon"),
    n("BoShek's Modified Freighter"),
    n("Millennium Falcon"),
    n("Booster In Pulsar Skate"),
    n("Overseer"),
    n("Spiral"),
    n("Wedge In Red Squadron 1"),
    n("Alderaan Consular Ship"),
    n("On The Edge"),
    n("Harvest", True),
    n("Hear Me Baby, Hold Together", True),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Are You Brain Dead?!"),
    n("All Wings Report In & Darklighter Spin", qty=4),
    n("Rebel Artillery", qty=2),
    n("Blaster Deflection"),
    n("Rebel Barrier"),
    n("Meditation"),
    n("Lightsaber Proficiency"),
    n("Sai'torr Kal Fas", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True, qty=2),
    n("Restraining Bolt"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Weapons Display"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Prince Xizor", True),
    n("Prepared Defenses", True),
    n("Shadows Of The Empire"),
    n("Jabba's Haven"),
    n("Tatooine", True),
    n("You Cannot Hide Forever"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Nal Hutta"),
    n("Coruscant: Imperial Square"),
    n("Prince Xizor"),
    n("P-59"),
    n("P-60"),
    n("Guri", True, qty=2),
    n("Ponda Baba", True),
    n("Dr. Evazan"),
    n("Velken Tezeri", True),
    n("Emperor Palpatine", qty=4),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Vigo"),
    n("4-LOM With Concussion Rifle", True),
    n("Dengar With Blaster Carbine", True, qty=2),
    n("IG-88 With Riot Gun"),
    n("Restraining Bolt"),
    n("Maul's Sith Infiltrator"),
    n("Elis In Hinthra"),
    n("Bossk In Hound's Tooth", True),
    n("Zuckuss In Mist Hunter"),
    n("Disarmed", qty=2),
    n("I Have You Now"),
    n("Presence Of The Force", qty=2),
    n("No Escape"),
    n("Oh, Switch Off", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imbalance"),
    n("Your Powers Are Weak, Old Man", True),
    n("ComScan Detection", True),
    n("Unexpected Interruption", qty=2),
    n("Cease Fire!"),
    n("Sense", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Force Lightning"),
    n("Ommni Box & It's Worse"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Reactor Terminal", True),
    n("After Her!", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
]
DS_ADD = []
