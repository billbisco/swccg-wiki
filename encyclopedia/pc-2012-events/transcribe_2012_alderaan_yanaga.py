#!/usr/bin/env python3
"""2012 Alderaan Regionals leftover Xerox: Camden Yanaga dested Ganden Yanaga.

Source: 2012AlderaanRegionals.pdf pages 11–12 (handwritten 2010 Xerox).
Name Camden Yanaga dested Ganden Yanaga analog leftover encyclopedia /
generate CANON Camden Yanaga / Cam Solusar → Ganden Yanaga /
player-stubs/Ganden_Yanaga.wiki. Username Cam Solusar.
p11 Light We Have A Plan. p12 Dark Contract Killers.
Do not dest as a new person Camden. Do not dest 2013 Alderaan / 2013 SoCal /
2014 TMW / 2014 Alderaan Yanaga 60s again.
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = ""
PDF = "2012 Alderaan Regionals.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2012 Alderaan Regionals Ganden Yanaga LS.png"
DS_SCAN = "2012 Alderaan Regionals Ganden Yanaga DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p11 Light / p12 Dark. "
    "Name Camden Yanaga dested Ganden Yanaga analog leftover encyclopedia / generate CANON / "
    "player-stubs/Ganden_Yanaga.wiki. Username Cam Solusar. Date 7/7/12. "
    "Deck Name Light That's A Wrap / Dark Treadstone dested off article. "
    "Do not dest as a new person Camden. Do not dest 2013 Alderaan / 2013 SoCal / "
    "2014 TMW / 2014 Alderaan Yanaga 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p11 Light. Name Camden Yanaga dested Ganden Yanaga. "
    "Username Cam Solusar. LIGHT checked. Deck Name That's A Wrap dested off article. "
    "We Have A Plan / Lost And Confused dested We Have A Plan / They Will Be Lost And Confused analog leftover 2014 Alderaan Yanaga. "
    "Panaka, Protector dested Panaka, Protector Of The Queen analog leftover mpc_light_frank. "
    "Obi-Wan Kenobi, JK dested Obi-Wan Kenobi, Jedi Knight analog leftover Nathan. "
    "Mace Windu, MOTO dested Mace Windu analog leftover. "
    "Jerns Jannick dest as written. Artoo BLD dest as written. TWHPS dest as written. "
    "AJR dested A Jedi's Resilience analog leftover Atkin. "
    "Blaster Deflection qty=2 at first occurrence (31 covering 43). "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency analog leftover combo. "
    "Qui-Gon's Lightsaber (Tat) dested Qui-Gon Jinn's Lightsaber. "
    "Obi-Wan's Lightsaber (R3) dested Obi-Wan's Lightsaber analog leftover Atkin. "
    "C: JCC dested Coruscant: Jedi Council Chamber True analog leftover Kafer. "
    "YISYW dested Your Insight Serves You Well True analog leftover. "
    "Unique 60 shields 12 sheet-accurate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p12 Dark. Name Camden Yanaga dested Ganden Yanaga. "
    "Username Cam Solusar. DARK checked. Deck Name Treadstone dested off article. "
    "Contract Killers / Feared... dested Contract Killers / Feared Throughout The Galaxy analog leftover 2013 mpc dambrosio. "
    "Galen dested Galen analog leftover Atkin. "
    "Aurra Sing, District Attorney dest as written. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Deder the Black dested Dengar analog leftover. "
    "4-LOM with Rifle dested 4-LOM With Concussion Rifle analog leftover Atkin. "
    "Slave One, Symbol of Fear dested Slave I, Symbol Of Fear analog leftover Atkin. "
    "ZIMH dested Zuckuss In Mist Hunter analog leftover. "
    "Hutt Bounty & Death Mark dested combo analog leftover. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover Atkin. "
    "Lana Dobreed & Sacrifice dested combo analog leftover alderaan_gabe. "
    "K&D dested Knowledge And Defense empty IN THE 60. "
    "Allegations dested Allegations Of Corruption analog leftover. "
    "CHYBC dested Come Here You Big Coward analog leftover. "
    "Unique 60 shields 12 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Throne Room"),
    n("Scomp Link Access", True),
    n("We'll Take The Long Way"),
    n("Quick Draw", True),
    n("Queen Amidala", qty=3),
    n("Panaka, Protector Of The Queen", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Mace Windu", qty=2),
    n("Fallen Jedi"),
    n("Jerns Jannick"),
    n("Artoo BLD", True),
    n("TWHPS"),
    n("2-1B", True),
    n("Bravo Fighter", True),
    n("Landing Claw"),
    n("Ascension Guns", True),
    n("Control & Tunnel Vision", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Blaster Deflection", qty=2),
    n("We're Doomed"),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Clash Of Sabers"),
    n("Speak With The Jedi Council"),
    n("Let The Wookiee Win", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("I've Decided To Go Back", True),
    n("Return Of A Jedi", True),
    n("Dodge"),
    n("Dark Approach", True),
    n("Nabrun Leids"),
    n("Smoke Screen"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Imperial Atrocity", True, qty=4),
    n("Advantage"),
    n("Sai'torr Kal Fas", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hindsight", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Chasm"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Don't Do That Again"),
    n("Only Jedi Carry That Weapon"),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("On The Hunt"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Guild Of Assassins"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Casino"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Arica", True, qty=2),
    n("Galen", qty=2),
    n("Aurra Sing, District Attorney", qty=2),
    n("Bane Malar, Spice Addict"),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer"),
    n("Dengar", True),
    n("Velken Tezeri", True),
    n("4-LOM With Concussion Rifle", True),
    n("Guri"),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing's Blaster Rifle", qty=2),
    n("Trophy Of A Kill", qty=3),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Hutt Bounty & Death Mark"),
    n("Disarmed", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra"),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Force Push", True),
    n("They're Still Coming Through!"),
    n("Imperial Barrier"),
    n("Stunning Leader"),
    n("Sniper & Dark Strike"),
    n("Imbalance & Kintan Strider"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("We Must Accelerate Our Plans"),
    n("Sith Fury", True),
    n("Lana Dobreed & Sacrifice"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
]
DS_ADD = []
