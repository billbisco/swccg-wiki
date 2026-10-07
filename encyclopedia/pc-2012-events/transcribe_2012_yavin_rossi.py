#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Vincent Rossi.

Source: Yavin42012.pdf pages 9–13 typed LIGHT SIDE / DARK SIDE DECK LIST.
p09–p11 Light / p11–p13 Dark. Name Vincent Rossi dested Vincent Rossi analog leftover
dest as written / file_player Rossi. Username blank.
Pack player-stubs/Vincent_Rossi.wiki.
Do not dest as Vinny Rossi. Do not dest as a new last-name Rossi.
"""
from __future__ import annotations

PLAYER = "Vincent Rossi"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 9
DS_PAGE = 11
LS_SCAN = "2012 Yavin 4 Regionals Vincent Rossi LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Vincent Rossi DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p09–p11 Light / p11–p13 Dark typed deck lists. Name Vincent Rossi dested Vincent Rossi "
    "analog leftover dest as written. Username blank. "
    "Do not dest as Vinny Rossi. Pack player-stubs/Vincent_Rossi.wiki."
)
LS_NOTE = (
    "Typed LIGHT SIDE DECK LIST p09–p11. Name Vincent Rossi dested Vincent Rossi. "
    "Username blank. Do not dest as Vinny Rossi. "
    "Defensive Shields dested LS_SHIELDS analog leftover dump. "
    "STARTING EFFECT Anger, Fear, Aggression (v) dested IN THE 60 True analog leftover Skilton. "
    "USED OR STARTING Heading For The Medical Frigate dested IN THE 60 analog leftover Skilton. "
    "I'll Try Spinning dested analog leftover Scott. "
    "Qui-Gon Jinn, Jedi Master dested analog leftover dump. "
    "Yoda MOTF x2 dested qty=2 analog leftover Westergard. "
    "Jedi Pilot (v) x2 dested True qty=2 analog leftover Scott. "
    "Ki-Adi-Mundi (v) dested True analog leftover Westergard. "
    "Obi-Wan Kenobi, Jedi Knight dested analog leftover dump. "
    "Padme Naberrie x2 dested analog leftover Hanson. "
    "Ric Olie dested analog leftover Scott. "
    "Sai'torr Kal Fas (v) dested True analog leftover Virtual Block. "
    "We'll Take The Long Way (v) dested True analog leftover Scott. "
    "Wokling (v) dested True analog leftover Skilton. "
    "I've Decided To Go Back (v) x2 dested True qty=2 analog leftover dump. "
    "Sense & Recoil In Fear dested Sense & Recoil analog leftover Westergard. "
    "Sorry About The Mess & Blaster Proficiency x2 dested qty=2 analog leftover Westergard. "
    "Naboo Defense Fighter x3 dested qty=3 analog leftover dump. "
    "Proton Torpedos (Theed Palace) dested analog leftover dump. "
    "We Have A Plan/They Will Be Lost And Confused dested We Have A Plan / They Will Be Lost And Confused analog leftover Yanaga. "
    "Locations dested title case analog leftover typical. "
    "Unique 60 shields 12."
)
DS_NOTE = (
    "Typed DARK SIDE DECK LIST p11–p13. Name Vincent Rossi dested Vincent Rossi facing Light analog leftover Cooleo. "
    "Username blank. Do not dest as Vinny Rossi. "
    "Defensive Shields dested DS_SHIELDS analog leftover dump. "
    "STARTING EFFECT Knowledge And Defense dested IN THE 60 analog leftover Skilton. "
    "USED OR STARTING Any Methods Necessary dested IN THE 60 analog leftover dump. "
    "Bane, The Bounty Hunter (v) dested True analog leftover dump. "
    "Boba Fett, Restless Bounty Hunter (v) dested True analog leftover dump. "
    "Dr. Evazan & Ponda Baba dested analog leftover combo. "
    "Gela Yeens (v) dested True analog leftover dump. "
    "Mara Jade, The Emporer's Hand dested Mara Jade, The Emperor's Hand analog leftover typical. "
    "3B3-888 dested analog leftover dump. "
    "Sense (Premiere) x2 dested Sense qty=2 analog leftover dest as written Premiere dest notes. "
    "Oo-to Goo-ta, Solo? (v) dested True analog leftover dump. "
    "GALL dested Gall analog leftover typical. "
    "Carbon Chamber Testing/My Favorite Decoration dested Carbon Chamber Testing / My Favorite Decoration analog leftover typical. "
    "Bossk In Hound's Tooth dested analog leftover typical. "
    "IG-88 In IG-2000 dested analog leftover typical. "
    "Elis Helrot x2 dested qty=2 analog leftover Westergard. "
    "Imperial Barrier x2 dested qty=2 analog leftover Scott. "
    "No Escape (v) dested True analog leftover dest True when (v) written shield. "
    "Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("I'll Try Spinning"),
    n("Mace Windu"),
    n("Qui-Gon Jinn, Jedi Master"),
    n("Yoda, Master Of The Force", qty=2),
    n("Corporal Rushing"),
    n("Jedi Pilot", True, qty=2),
    n("Jerus Jannick"),
    n("Ki-Adi-Mundi", True),
    n("Lieutenant Chamberlyn"),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Padme Naberrie", qty=2),
    n("Panaka, Protector Of The Queen"),
    n("Ric Olie"),
    n("Sabe"),
    n("Sache"),
    n("Sio Bibble"),
    n("Obi-Wan's Journal"),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Obi-Wan's Cape", True),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("We'll Take The Long Way", True),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
    n("Ambush"),
    n("A Jedi's Resilience"),
    n("Control & Tunnel Vision"),
    n("Impressive, Most Impressive", True),
    n("I've Decided To Go Back", True, qty=2),
    n("Noble Sacrifice"),
    n("Alter"),
    n("Nabrun Leids"),
    n("Rebel Barrier"),
    n("Slight Weapons Malfunction"),
    n("Ascension Guns", True),
    n("Sense & Recoil"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Heading For The Medical Frigate"),
    n("Naboo"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Throne Room"),
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo Defense Fighter", qty=3),
    n("Amidala's Blaster"),
    n("Jawa Ion Gun"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
    n("Proton Torpedos (Theed Palace)"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Stun Blaster"),
]
LS_SHIELDS = [
    n("Affect Mind"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("Ounee Ta", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Weapons Display"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Aurra Sing"),
    n("Bane Malar", True),
    n("Bane, The Bounty Hunter", True),
    n("Beedo"),
    n("Boba Fett, Restless Bounty Hunter", True),
    n("Chokk"),
    n("Djas Puhr"),
    n("Dr. Evazan & Ponda Baba"),
    n("Feltipern Trevagg"),
    n("Gela Yeens", True),
    n("Greedo", True),
    n("Judo Kast"),
    n("Lando Calrissian", True),
    n("Ree-Yees"),
    n("Snoova"),
    n("Arica", True),
    n("Mara Jade, The Emperor's Hand"),
    n("3B3-888"),
    n("Guri"),
    n("P-59"),
    n("Jabba's Prize"),
    n("Carbonite Chamber Console"),
    n("A Sith's Plans", True),
    n("A Sith's Weapon", True),
    n("Desilijic Tattoo", True),
    n("Despair", True),
    n("Establish Control"),
    n("Imperial Stockpile", True),
    n("Scum And Villainy"),
    n("Special Delivery", True),
    n("The Dark Path", True),
    n("Trophy Of A Bounty Hunter", True),
    n("Knowledge And Defense"),
    n("Sniper"),
    n("Elis Helrot", qty=2),
    n("Imperial Barrier", qty=2),
    n("Sense", qty=2),
    n("Oo-to Goo-ta, Solo?", True),
    n("Any Methods Necessary"),
    n("Gall"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Bossk In Hound's Tooth"),
    n("Dengar In Punishing One"),
    n("IG-88 In IG-2000"),
    n("Jabba's Space Cruiser", True),
    n("Zuckuss In Mist Hunter"),
    n("Aurra Sing's Blaster Rifle"),
    n("Fett's Blaster Rifle", True),
    n("Mara Jade's Lightsaber", True),
    n("Naboo Blaster"),
    n("Naboo Blaster Rifle"),
    n("Vibro-Ax"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Imperial Detention"),
    n("No Escape", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Wipe Them Out, All Of Them", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
