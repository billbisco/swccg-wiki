#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Wayne Cullen typed 2010 Print Form LS+DS."""
from __future__ import annotations

PLAYER = "Wayne Cullen"
USERNAME = "KissMyWookiee"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2013 Match Play Championship p26 Wayne Cullen LS.png"
DS_SCAN = "2013 Match Play Championship p25 Wayne Cullen DS.png"
LS_NOTE = "Typed 2010 Xerox Print Form. (V) from the checkbox. Deck title Should have played RTP."
DS_NOTE = "Typed 2010 Xerox Print Form. (V) from the checkbox. Deck title Set Your Course for Uranus."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Corran Horn"),
    n("Chewie, Enraged", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Chewbacca, Protector"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Padme Naberrie", True),
    n("Luke's Bionic Hand"),
    n("Seeking An Audience", True),
    n("I Hope She's All Right"),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Rebel Gunrunner"),
    n("Draw Their Fire"),
    n("Flash Of Insight", True),
    n("Lightsaber Proficiency"),
    n("Imperial Atrocity", True, qty=2),
    n("Houjix"),
    n("Impressive, Most Impressive", True, qty=2),
    n("Rug Hug"),
    n("Use The Force", qty=2),
    n("Sense", qty=2),
    n("Alter"),
    n("Escape Pod", True),
    n("Run Luke, Run!", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Blaster Deflection"),
    n("Let The Wookiee Win", True, qty=3),
    n("Tatooine: Cantina", True),
    n("Tatooine: Obi-Wan's Hut"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Mos Eisley"),
    n("Lando's Luxury Yacht"),
    n("Artoo-Detoo In Red 5"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Chewie's Bowcaster"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Intensify The Forward Batteries", qty=2),
    n("Garindan", True),
    n("Darth Sidious", qty=3),
    n("U-3PO"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Imperial Decree", True),
    n("Tarkin Doctrine"),
    n("The Phantom Menace"),
    n("Tarkin's Bounty"),
    n("Protocol Failure"),
    n("Lateral Damage"),
    n("Commence Primary Ignition", True),
    n("Relentless Pursuit", qty=2),
    n("Overwhelmed", qty=2),
    n("Control & Set For Stun", qty=2),
    n("Force Push", True),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True),
    n("TIE Sentry Ships", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Close Call", True, qty=2),
    n("You Swindled Me", True, qty=2),
    n("Fury Fury", True),
    n("Force Field", True, qty=2),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Kiffex"),
    n("Rendili"),
    n("Nal Hutta"),
    n("Visage Of The Emperor"),
    n("Tyrant"),
    n("Devastator", True),
    n("Conquest", True),
    n("Accuser"),
    n("Victory"),
    n("Thunderflare"),
    n("Judicator", qty=2),
    n("Superlaser"),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
