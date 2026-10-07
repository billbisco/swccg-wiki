#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Joe Orthner.

Source: Yavin42012.pdf pages 14–15.
p14 Dark handwritten 2010 Xerox / p15 Light handwritten 2010 Xerox.
Name Joe Orthner both sides dested Joe Orthner analog leftover
generate/transcribe/file_player empty dest as written.
Username blank. Pack player-stubs/Joe_Orthner.wiki.
Event Date 6/30/2012 Event Name Yavin IV 2012 on Light; Dark Event Date/Name
blank dest facing pair analog leftover Cooleo.
Do not dest as Charley Joe. Do not dest as a new last-name Orthner.
"""
from __future__ import annotations

PLAYER = "Joe Orthner"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 15
DS_PAGE = 14
LS_SCAN = "2012 Yavin 4 Regionals Joe Orthner LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Joe Orthner DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p14 Dark handwritten 2010 Xerox / p15 Light handwritten 2010 Xerox. "
    "Name Joe Orthner both sides dested Joe Orthner analog leftover "
    "generate/transcribe/file_player empty dest as written. "
    "Username blank. Event Date 6/30/2012 Event Name Yavin IV 2012 on Light; "
    "Dark Event Date/Name blank dest facing pair analog leftover Cooleo. "
    "Do not dest as Charley Joe. Do not dest as a new last-name Orthner. "
    "Pack player-stubs/Joe_Orthner.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p15 Light. Name Joe Orthner Username blank. "
    "Event Date 6/30/2012 Event Name Yavin IV 2012 dest Yavin 4 facing pair. "
    "Hidden Base / Systems Will Slip Through Your Fingers dested analog leftover Scott. "
    "The Time For Our Attack Has Come empty then ditto True KEEP SEPARATE analog leftover McCune. "
    "Luke Skywalker With Lightsaber True then ditto empty KEEP SEPARATE analog leftover McCune. "
    "Qui-Gon Jinn With Lightsaber empty qty=2 at first. "
    "Gold Squadron Y-Wing dested dest as written qty=4. "
    "Rebel Barrier consecutive ditto empty qty=2. "
    "It's A Hit dested It's A Hit! analog leftover Scott. "
    "Biggs, Rouge Legend Leader crossed dested Biggs, Red Squadron Leader analog leftover typical. "
    "R2-D2 empty lines 30/44 dest qty=2 at first analog leftover non-consecutive. "
    "Leia, Rebel Princess dested analog leftover Brady. "
    "Keir Santage dested analog leftover TYPE_OVERRIDE Character. "
    "Gold Leader In Gold 1 True line 34 KEEP SEPARATE from line 52 empty analog leftover McCune. "
    "Antilles Maneuver & Rebel Reinforcement dested Antilles Maneuver & Rebel Reinforcements analog leftover Cooleo. "
    "Houjix & Out Of Nowhere dested analog leftover Scott. "
    "All Wings Report In qty=2 dest as written (not combo). "
    "Ralltiir Freighter Captain dested analog leftover typical. "
    "Strikeforce True dested analog leftover TYPE_OVERRIDE Effect. "
    "Projection Of A Skywalker dested analog leftover Westergard. "
    "Rebel Aces dested analog leftover TYPE_OVERRIDE Effect. "
    "Shields 1–10 filled shields 11–12 empty skip analog leftover Dwyer. Unique 60 shields 10."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p14 Dark. Name Joe Orthner Username blank. "
    "Event Date/Name blank dest Dark facing pair analog leftover Cooleo. "
    "Court Of Vile Gangsters dested Court Of The Vile Gangster analog leftover Banger. "
    "Elis Helrot empty lines 11/44/58 dest qty=3 at first analog leftover non-consecutive. "
    "Vibro-Ax empty lines 13/41 dest qty=2 at first. "
    "Imperial Barrier empty lines 15/34 dest qty=2 at first. "
    "Lateral Damage empty lines 18/24 dest qty=2 at first. "
    "Hidden Weapons empty lines 19/22 dest qty=2 at first. "
    "Bubo empty lines 21/51 dest qty=2 at first. "
    "Double Laser Cannon dested analog leftover typical. "
    "J'Quille True qty=2 lines 25/29 dest qty at first. "
    "Potc dested Pote Snitkin analog leftover TMW Joe Poteet. "
    "IG-88 In IG-2000 dested replacement of crossed Fett analog leftover crossed-with-replacement. "
    "Wounded Wookiee empty qty=2 dest as written not Abyssin Ornament combo analog leftover TMW Joe. "
    "Boba Fett True KEEP SEPARATE from Boba Fett, Bounty Hunter analog leftover McCune. "
    "Boba Fett With Blaster Rifle dested analog leftover Fett w/ rifle. "
    "Scum And Villainy empty lines 48/54 dest qty=2 at first. "
    "Jabba's Sail Barge: Passenger Deck dested analog leftover typical. "
    "Endor: Landing Platform (Docking Bay) dested analog leftover typical. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Draw Their Fire", True),
    n("Hidden Fortress"),
    n("Luke, Trust Me"),
    n("Anger, Fear, Aggression", True),
    n("Masanya"),
    n("R2-X2"),
    n("The Time For Our Attack Has Come"),
    n("The Time For Our Attack Has Come", True),
    n("Luke Skywalker With Lightsaber", True),
    n("Luke Skywalker With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Gold Squadron Y-Wing", qty=4),
    n("Rebel Barrier", qty=2),
    n("Organized Attack", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("It's A Hit!"),
    n("Rebel Reinforcements"),
    n("Biggs, Red Squadron Leader"),
    n("Kessel Run", qty=2),
    n("R2-D2", qty=2),
    n("Koensayr Manufacturing"),
    n("Leia, Rebel Princess"),
    n("Keir Santage"),
    n("Gold Leader In Gold 1", True),
    n("Yavin 4"),
    n("Spiral"),
    n("Dressel"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Han With Heavy Blaster Pistol"),
    n("Theron Nett"),
    n("Lando With Vibro-Ax"),
    n("Houjix & Out Of Nowhere"),
    n("Hoth"),
    n("Y-Wing Squadron"),
    n("Mirax Terrik"),
    n("Colonel Salm"),
    n("All Wings Report In", qty=2),
    n("R5-D4"),
    n("Chewie With Blaster Pistol"),
    n("Gold Leader In Gold 1"),
    n("Ralltiir Freighter Captain"),
    n("Strikeforce", True),
    n("Commander Narra"),
    n("Honor Of The Jedi"),
    n("Projection Of A Skywalker"),
    n("Rebel Aces"),
    n("Evacuation Control", True),
    n("Wedge Antilles"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("A Tragedy Has Occurred"),
    n("A Close Race"),
    n("Planetary Defenses"),
    n("The Professor", True),
    n("Aim High", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Court Of The Vile Gangster"
DS_CARDS = [
    n("Court Of The Vile Gangster"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Tatooine: Great Pit Of Carkoon"),
    n("Prepared Defenses"),
    n("Krayt Dragon Bones", True),
    n("Jabba's Haven", True),
    n("Power Of The Hutt"),
    n("Knowledge And Defense"),
    n("Stop Motion"),
    n("Elis Helrot", qty=3),
    n("Sarlacc"),
    n("Vibro-Ax", qty=2),
    n("Jabba's Sail Barge", True),
    n("Imperial Barrier", qty=2),
    n("Fett's Blaster Rifle"),
    n("Elephant Men"),
    n("Lateral Damage", qty=2),
    n("Hidden Weapons", qty=2),
    n("Snoova"),
    n("Bubo", qty=2),
    n("Double Laser Cannon"),
    n("J'Quille", True, qty=2),
    n("Bib Fortuna", True),
    n("Pote Snitkin"),
    n("Hutt Bounty", True),
    n("Jabba The Hutt", True),
    n("Boelo"),
    n("Boba Fett, Bounty Hunter"),
    n("4-LOM"),
    n("IG-88 In IG-2000"),
    n("Bossk In Hound's Tooth"),
    n("Mara Jade"),
    n("Cloud City: East Platform"),
    n("Wounded Wookiee", qty=2),
    n("Dengar In Punishing One"),
    n("Boba Fett", True),
    n("Boba Fett With Blaster Rifle"),
    n("Zuckuss"),
    n("No Escape"),
    n("Scum And Villainy", qty=2),
    n("Force Push", True),
    n("Thok & Thug", True),
    n("Sebulba's Podracer"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Tatooine: Docking Bay 94"),
    n("Jabba's Space Cruiser", True),
    n("Cold Feet"),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("You've Never Won A Race"),
    n("Battle Order"),
    n("Abyss"),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("Secret Plans"),
]
DS_ADD = []
