#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Keith Brown typed Holotable LS+DS."""
from __future__ import annotations

PLAYER = "Keith Brown"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 17
DS_PAGE = 18
LS_SCAN = "2013 Match Play Championship p17 Keith Brown LS.png"
DS_SCAN = "2013 Match Play Championship p18 Keith Brown DS.png"
LS_NOTE = "Typed Holotable printout. Handwritten: Redeemed Apprentice struck from Effects; Only Jedi Carry That Weapon struck from Shields and replaced with Wise Advice."
DS_NOTE = "Typed Holotable printout. Handwritten 'Combo' next to Imperial Propaganda (V) is dested as Imperial Propaganda (V) as printed."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Jedi Survivor"),
    n("Lando Calrissian, Unlikely Hero"),
    n("IL-19"),
    n("Mace Windu, Master Of The Order (AI)"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Princess Leia", True),
    n("Han With Heavy Blaster Pistol"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Chewie, Enraged"),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Ki-Adi-Mundi", True),
    n("Fallen Jedi"),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience"),
    n("Smoke Screen", qty=2),
    n("It's Not My Fault!", True),
    n("Desperate Reach", True),
    n("Dark Approach", True, qty=2),
    n("Odin Nesloor & First Aid"),
    n("Rebel Leadership", True),
    n("Sense", qty=2),
    n("Blaster Deflection", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Speak With The Jedi Council", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Alderaan Consular Ship"),
    n("Tantive IV", True),
    n("Lando's Luxury Yacht"),
    n("Wedge In Red Squadron 1"),
    n("Elegant Lightsaber"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Mercenary Slavers"),
    n("Breached Defenses & Molator"),
    n("Jabba's Haven"),
    n("Chevin", True, qty=4),
    n("Boba Fett, Prepared Hunter"),
    n("The Mandalorian, Father Of Fett", qty=2),
    n("Gela Yeens", True),
    n("Prince Xizor"),
    n("Bossk With Mortar Gun", True, qty=2),
    n("Grotto Werribbee", True),
    n("Dengar With Blaster Carbine", True),
    n("Jabba The Hutt", True),
    n("Ponda Baba", True),
    n("Trandoshan", qty=6),
    n("Probot"),
    n("4-LOM With Concussion Rifle"),
    n("IG-88 With Riot Gun"),
    n("P-59"),
    n("Scum And Villainy"),
    n("Tarkin's Bounty", True),
    n("T'doshok Hunting Vow"),
    n("Imperial Propaganda", True),
    n("Where Are You Taking This ... Thing?"),
    n("Protocol Failure"),
    n("Cold Feet", True),
    n("Lana Dobreed & Sacrifice"),
    n("Lightsaber Deficiency", True),
    n("Why Didn't You Tell Me?", True),
    n("Operational As Planned", True),
    n("Abyssin Ornament"),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament & Wounded Wookiee"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Forest Maze"),
    n("Kashyyyk: Skyhook Platform"),
    n("Nal Hutta"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
