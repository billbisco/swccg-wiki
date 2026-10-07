#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Greg Shaw Xerox Agents / TIGIH (second pair)."""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2013 Texas Mini Worlds Day 1 p10 Greg Shaw LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p09 Greg Shaw DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Greg Shaw. Username blank. "
    "Deck Name Good Luck Choosing Four. LIGHT. Event TMW 04/20/13. "
    "Second Day 1 pair; keep Hunt Down leftover live. "
    "Do not rewrite the 2013 MPC, Worlds, or SoCal Greg Shaw leftovers. "
    "There Is Good in Him dested There Is Good In Him / I Can Save Him. "
    "Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Landing Platform (Docking Bay) dested Endor: Landing Platform (Docking Bay). "
    "Heading For The Medical Frig dested Heading For The Medical Frigate. "
    "Colo Claw Fish crossed, Grimtaash dested Grimtaash. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Home One War Room dested Home One: War Room. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Battle Plains dested Naboo: Battle Plains. "
    "Qui Gon's Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "Mace Windu Master of Order dested Mace Windu, Master Of The Order. "
    "Master Qui Gon dested Master Qui-Gon. "
    "Yoda Master of the Force dested Yoda, Master Of The Force. "
    "Obi with Lightsaber dested Obi-Wan With Lightsaber. "
    "Scrambled Transmission crossed with no replacement, skipped. "
    "Saitor Kal Fas dested Sai'torr Kal Fas. "
    "Impressive Most Impressive dested Impressive, Most Impressive. "
    "The Bith Shuffle & Desperoke dested The Bith Shuffle & Desperate Reach. "
    "Sorry About The Mess & Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Let's Keep A Little Optimism dested Let's Keep A Little Optimism Here. "
    "Never Wise Advice: Never crossed, dested Wise Advice. "
    "Shield line 5 crossed, skipped. "
    "Form left column reprints 37-38 on lines 39-40 are Impressive, Most Impressive "
    "and The Bith Shuffle & Desperate Reach. "
    "Unique overcounts sheet-accurate: Han, Chewie, And The Falcon x2, "
    "Mace Windu x2, Master Qui-Gon x2, Lando Calrissian, Scoundrel x2, "
    "Escape Pod x2, Rebel Leadership x3, Wesa Gotta Grand Army x3, "
    "Let The Wookiee Win x2, Sense x3. "
    "Main 59 after the crossed Scrambled Transmission. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Greg Shaw. Username blank. "
    "Deck Name Werewolf Tech. DARK. Event TMW 04/20/13. "
    "Second Day 1 pair; keep Hunt Down leftover live. "
    "Do not rewrite the 2013 MPC, Worlds, or SoCal Greg Shaw leftovers. "
    "Agents of Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Coruscant (SE) dested Coruscant. Imperial City dested Coruscant: Imperial City. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "Cloud City Security Tower dested Cloud City: Security Tower. "
    "Spaceport Docking Bay dested Spaceport Docking Bay. "
    "Coruscant Docking Bay (E1) dested Coruscant: Docking Bay. "
    "IG-88 with Riot Gun dested IG-88 With Riot Gun. "
    "4lom with Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Dengar with Blaster Carbine dested Dengar With Blaster Carbine. "
    "Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Dr Evazan dested Dr. Evazan. "
    "Jabba the Hutt dested Jabba The Hutt. "
    "Elis in Hinthra dested Elis In Hinthra. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Oh Switch Off dested Oh, Switch Off. "
    "They're Still Coming Through dested They're Still Coming Through!. "
    "Look Sir Droids dested Look Sir, Droids. "
    "Cease Fire dested Cease Fire!. "
    "Ghhhk & Those Rebels Won't Escape dested Ghhhk & Those Rebels Won't Escape Us. "
    "Lana Dobreed & Sacrifice dested Lana Dobreed & Sacrifice. "
    "Lightsaber Proficiency dested Lightsaber Proficiency as written. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "We'll Let Fate-a Decide Huh? dested We'll Let Fate-a Decide, Huh?. "
    "I Find Your Lack of Faith Dist dested I Find Your Lack Of Faith Disturbing. "
    "Form left column reprints 37-38 on lines 39-40 are Protocol Failure "
    "and Jabba's Haven. "
    "Unique overcounts sheet-accurate: Vigo x2, Jodo Kast x2, Disarmed x2, "
    "Hidden Weapons x2, Sonic Bombardment x2, We Must Accelerate Our Plans x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Grimtaash"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Home One"),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Yoda, Master Of The Force"),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber"),
    n("Princess Leia", True),
    n("Corran Horn"),
    n("Seeking An Audience", True),
    n("Draw Their Fire"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("Impressive, Most Impressive", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council"),
    n("Houjix"),
    n("Escape Pod", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense", qty=3),
    n("Weapon Levitation"),
    n("A Jedi's Resilience"),
    n("Blaster Deflection"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Wise Advice"),
]


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prince Xizor", True),
    n("Twi'lek Advisor", True),
    n("Den Of Thieves", True),
    n("Ket Maliss", True),
    n("Scum And Villainy"),
    n("Information Exchange", True),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Spaceport Docking Bay", True),
    n("Coruscant: Docking Bay"),
    n("Vigo", True, qty=2),
    n("Guri"),
    n("OOM-9", True),
    n("IG-88 With Riot Gun"),
    n("4-LOM With Concussion Rifle"),
    n("Dengar With Blaster Carbine", True),
    n("Bossk", True),
    n("Jodo Kast", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Dr. Evazan"),
    n("Ponda Baba", True),
    n("Wooof", True),
    n("Jabba The Hutt", True),
    n("Ree-Yees", True),
    n("Garindan", True),
    n("Elis In Hinthra"),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Feltipern Trevagg's Stun Rifle", True),
    n("Mandalorian Armor", True),
    n("Disarmed", qty=2),
    n("Protocol Failure"),
    n("Jabba's Haven"),
    n("Lightsaber Proficiency", True),
    n("Unexpected Interruption"),
    n("Oh, Switch Off"),
    n("Imperial Barrier"),
    n("Hidden Weapons", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("They're Still Coming Through!"),
    n("Jabba's Through With You"),
    n("Lana Dobreed & Sacrifice"),
    n("A Dark Time For The Rebellion", True),
    n("Control & Set For Stun"),
    n("Blow Parried"),
    n("Look Sir, Droids"),
    n("Cease Fire!"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("There Is No Try"),
]
DS_ADD = [
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Resistance"),
]
