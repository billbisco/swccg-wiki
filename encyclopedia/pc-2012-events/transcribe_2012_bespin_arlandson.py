#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Charles A. dested Charlie Arlandson.

Source: 2012BespinRegionals.pdf pages 3–4 (handwritten 2010 Xerox).
p03 Dark Name Charles. p04 Light Name Charles A. dested Charlie Arlandson
analog leftover 2013 Worlds CANON Charles Arlandson → Charlie Arlandson /
pages/Charlie_Arlandson.wiki. Username blank. Date 7/14/12.
Do not dest as a new person Charles. Do not dest 2013 Worlds / 2014 Worlds Arlandson 60s again.
"""
from __future__ import annotations

PLAYER = "Charlie Arlandson"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2012 Bespin Regionals Charlie Arlandson LS.png"
DS_SCAN = "2012 Bespin Regionals Charlie Arlandson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p03 Dark / p04 Light. "
    "Name Charles / Charles A. dested Charlie Arlandson analog leftover 2013 Worlds CANON / "
    "pages/Charlie_Arlandson.wiki. Username blank. Date 7/14/12 Event 2012 Bespin Regional. "
    "Do not dest as a new person Charles. Do not dest 2013 Worlds / 2014 Worlds Arlandson 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p04 Light. Name Charles A. dested Charlie Arlandson. Username blank. "
    "LIGHT/DARK empty dest Light from Naboo / Jedi card list. "
    "Line 1 Naboo: Boss Nass' Chambers dested starting location analog leftover Nathan no-objective. "
    "It is the Future You See dested It Is The Future You See True analog leftover. "
    "Battle Plan & Draw Their Fire dested combo analog leftover Atkin 2013. "
    "Do or Do Not & Wise Advice dested Do, Or Do Not & Wise Advice analog leftover Atkin 2013. "
    "A Good Blaster dested A Good Blaster At Your Side True analog leftover Schoenthal. "
    "Han's Blaster, Scoundrel dested Han With Heavy Blaster Pistol True analog leftover 2014 Alderaan Nathan. "
    "AZGO Rifle dest as written True. Obi's Mistake dest as written True. MVC Suit dest as written True. "
    "SATM & Blaster Prof dested Sorry About The Mess & Blaster Proficiency analog leftover Yanaga. "
    "Houjix & OON dested Houjix & Out Of Nowhere analog leftover Nieland. "
    "Fallen Portal dested Falling Portal analog leftover TMW Hendon. "
    "Buff Belos dested Boushh analog leftover Kafer. "
    "ITH & Aim High dest as written. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin analog leftover Kafer qty=3. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Wehner qty=2. "
    "Anger, Fear, Aggression empty IN THE 60. Unique 60 shields 12 sheet-accurate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p03 Dark. Name Charles dested Charlie Arlandson. Username blank. "
    "DARK checked. Set Your Course dested Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover Kafer. "
    "Knowledge And Defense True IN THE 60. "
    "CPI dested Commence Primary Ignition True analog leftover Kafer. "
    "Imperial Trooper Guard Diansom dested Imperial Trooper Guard analog leftover nats nieland. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us analog leftover nats nieland combo. "
    "Relentless Pursuit empty qty=4 at first occurrence (36 covering 40, 45, 48). "
    "Operational As Planned True line 39 and empty line 54 kept separate. "
    "I Did It My Way dested I Did It! True analog leftover jespar. "
    "LIEIA dest as written. Return dested Return Fire True analog leftover. "
    "Enter The Unknown dest as written. Enter The Boma dest as written. "
    "Weapon dested A Sith's Weapon analog leftover alderaan TYPE_OVERRIDE. "
    "Sneak Attack dested Sneak Attack analog leftover 2012 mpc gogolen. "
    "Intensify The Batteries dested Intensify The Forward Batteries analog leftover Kafer qty=2. "
    "Unique 60 shields 12 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Naboo: Boss Nass' Chambers"
LS_CARDS = [
    n("Naboo: Boss Nass' Chambers"),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("A Good Blaster At Your Side", True),
    n("Han With Heavy Blaster Pistol", True),
    n("Scrambled Transmission", True),
    n("AZGO Rifle", True),
    n("Hindsight", True),
    n("It's Not My Fault", True),
    n("Obi's Mistake", True),
    n("Noooooooooooo", True, qty=2),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Boss Nass"),
    n("Death Star: Trench"),
    n("MVC Suit", True),
    n("Qui-Gon Jinn"),
    n("Master Luke"),
    n("Luke Skywalker", True),
    n("Wedge Antilles"),
    n("Naboo: Battlefield"),
    n("Tatooine: Watto's Junkyard"),
    n("We're Doomed"),
    n("Millennium Falcon", True),
    n("Houjix & Out Of Nowhere"),
    n("Control & Tunnel Vision"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Landing Claw"),
    n("Portable Scanner"),
    n("Enhanced Proton Torpedoes", True),
    n("Chewie's Bowcaster"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Count Me In", True),
    n("Han Solo", True),
    n("Padme Naberrie", True),
    n("Boushh"),
    n("Leia, Rebel Princess"),
    n("Phylo Gandish"),
    n("Luke Skywalker, Jedi Knight"),
    n("Bantha Fodder", True),
    n("Falling Portal"),
    n("Imperial Atrocity", True, qty=2),
    n("I Hope She's All Right"),
    n("Weapon Levitation"),
    n("ITH & Aim High"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Attack Run", qty=2),
    n("Death Star: Docking Bay 327", qty=2),
    n("Yavin 4: Massassi Headquarters"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Aim High", qty=2),
    n("Don't Do That Again", qty=2),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Chasm"),
    n("Yavin Sentry"),
    n("Your Crew"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense", True),
    n("Conquest", True, qty=2),
    n("Protocol Failure", qty=2),
    n("Alderaan"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room"),
    n("Death Star: Docking Bay 327"),
    n("Death Star"),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Tarkin's Doctrine", qty=2),
    n("Rendili"),
    n("Carida"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Imperial Justice", True),
    n("Kuat Drive Yards", True),
    n("No Escape"),
    n("Laser Cannon Battery"),
    n("Dreaded Imperial Starfleet", True),
    n("Stalker", True),
    n("Tyrant"),
    n("Imperial Trooper Guard"),
    n("Chimaera"),
    n("Avenger"),
    n("Devastator", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Enter The Unknown"),
    n("Image Of The Dark Lord"),
    n("A Dark Time For The Rebellion"),
    n("Accuser"),
    n("Relentless Pursuit", qty=4),
    n("Thunderflare"),
    n("Lightsaber Proficiency", True, qty=2),
    n("Operational As Planned", True),
    n("Trap Door"),
    n("I Did It!", True),
    n("Flawless Marksmanship", qty=3),
    n("LIEIA"),
    n("Return Fire", True),
    n("Lateral Damage"),
    n("Intensify The Forward Batteries", qty=2),
    n("Enter The Boma"),
    n("Operational As Planned"),
    n("A Sith's Weapon"),
    n("Limited Resources"),
    n("Sneak Attack"),
    n("Control & Set For Stun", qty=2),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Imperial Decree"),
    n("Firepower", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
