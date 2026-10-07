#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Amar Banger typed Print Form LS+DS."""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2013 Match Play Championship p09 Amar Banger LS.png"
DS_SCAN = "2013 Match Play Championship p10 Amar Banger DS.png"
LS_NOTE = "Typed 2010 Xerox Print Form. Deck title TRM. (Vn) tags on the printout are Holotable virtual versions."
DS_NOTE = "Typed 2010 Xerox Print Form. Deck title CPI v. (Vn) tags on the printout are Holotable virtual versions."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Yavin 4: Massassi Throne Room"),
    n("A Jedi's Resilience"),
    n("Admiral Ackbar", True),
    n("Advantage"),
    n("Alter", True, qty=2),
    n("Artoo-Detoo In Red 5"),
    n("Clash Of Sabers"),
    n("Control & Tunnel Vision"),
    n("Corran Horn"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Dark Approach", True),
    n("Either Way, You Win", True),
    n("Han, Chewie, And The Falcon"),
    n("Home One"),
    n("Home One: War Room"),
    n("I'm With You Too", True),
    n("IL-19", True),
    n("Jedi Lightsaber", True),
    n("Ki-Adi-Mundi", True),
    n("Kiffex"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Luke's Bionic Hand", True),
    n("Luke's Lightsaber"),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order", True),
    n("Master Qui-Gon", True, qty=2),
    n("NOOOOOOOOOOOO!", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Nabrun Leids"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Rebel Leadership", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Sense"),
    n("Speak With The Jedi Council"),
    n("Strikeforce", True),
    n("Tantive IV", True),
    n("The Force Is Strong With This One"),
    n("Under Attack"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Yavin 4: Massassi War Room", True),
    n("Yoda, Master Of The Force"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Ounee Ta"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("A Million Voices Crying Out"),
    n("Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Dreaded Imperial Starfleet", True),
    n("Inconsequential Losses", True),
    n("Knowledge And Defense", True),
    n("Prepared Defenses", True),
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("A Dark Time For The Rebellion", True),
    n("Accuser"),
    n("Arica"),
    n("Commence Primary Ignition", True),
    n("Conquest", True),
    n("Control & Set For Stun"),
    n("Corulag"),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber"),
    n("Darth Sidious"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Devastator", True),
    n("Dominator", True),
    n("Emperor Palpatine"),
    n("Flagship Executor"),
    n("Force Field", True),
    n("Force Push", True),
    n("Garindan", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Artillery"),
    n("Imperial Justice", True),
    n("Imperial Propaganda", True),
    n("Intensify The Forward Batteries", qty=3),
    n("Judicator", qty=2),
    n("Laser Cannon Battery", qty=3),
    n("Lateral Damage"),
    n("Lightsaber Deficiency", True),
    n("Lord Sidious", True),
    n("Masterful Move"),
    n("Myn Kyneugh", True),
    n("Operational As Planned", True),
    n("Overwhelmed"),
    n("Protocol Failure", True),
    n("Relentless Pursuit"),
    n("Rendili"),
    n("Sense & Uncertain Is The Future"),
    n("Something Special Planned For Them", True),
    n("Superlaser"),
    n("TIE Sentry Ships", True),
    n("Tarkin Doctrine", True),
    n("The Phantom Menace"),
    n("They've Shut Down The Main Reactor"),
    n("Tyrant"),
    n("Victory", True),
    n("Why Didn't You Tell Me?", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
