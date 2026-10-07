#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: JW Millet Xerox TIGIH / A Stunning Move."""
from __future__ import annotations

PLAYER = "JW Millet"
USERNAME = "Asphalizo"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 20
DS_PAGE = 21
LS_SCAN = "2013 Texas Mini Worlds Day 1 p20 JW Millet LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p21 JW Millet DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name JW Millet. Username Asphalizo. "
    "Deck Name What Else?!. Event Richard's Tourney. LIGHT checked. Date 4/20/13. "
    "There's Good In Him dested There Is Good In Him / I Can Save Him. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Wooooooooooo dested Wookiee Roar. "
    "Odin Nesloor + First Aid dested Odin Nesloor & First Aid. "
    "Out of Commission + Transmission Terminated dested "
    "Out Of Commission & Transmission Terminated. "
    "Speak with The Jedi Council dested Speak With The Jedi Council. "
    "Naboo: Boss' Nass Chamber dested Naboo: Boss Nass' Chambers. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. "
    "Echo Command Center dested Hoth: Echo Command Center. "
    "Unique overcounts sheet-accurate: Lando Calrissian, Scoundrel x2, "
    "Master Qui-Gon x2, A Jedi's Resilience x2, Either Way, You Win x2, "
    "Wookiee Roar x2, Rebel Leadership x2, Han, Chewie, And The Falcon x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name JW Millet. Username Asphalizo. "
    "Deck Name Hunt's Deck. Event Richard's Tourney. DARK checked. Date 4/20/13. "
    "A Stunning Move / A Valuable Hostage dested "
    "A Stunning Move / A Valuable Hostage. "
    "Sebulba's Haven dested Jabba's Haven. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Cyborg Commander, Hunter of the Jedi dested Grievous, Hunter Of Jedi. "
    "Darth Maul, YA dested Darth Maul, Young Apprentice. "
    "Dr Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice as written. "
    "IG Body Guard Droid dested IG-100 MagnaGuard. "
    "Lurke dested Lurke as written. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "He is not Ready + Imperial Propaganda dested "
    "He Is Not Ready & Imperial Propaganda as written. "
    "Control + Set For Stun dested Control & Set For Stun. "
    "Ghhhk + Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Short Range Fighters + Watch Your Back dested "
    "Short Range Fighters & Watch Your Back!. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Slave 1, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Galen's Lightsaber dested Galen's Lightsaber, Vader's Gift. "
    "After Her dested After Her!. "
    "We'll Let Fate dested We'll Let Fate-A Decide, Huh?. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Do not rewrite the 2013 MPC Barry Alperstein A Stunning Move leftover. "
    "Unique overcounts sheet-accurate: Battle Droid Squad x2, "
    "Boba Fett, Prepared Hunter x2, Grievous, Hunter Of Jedi x2, "
    "Darth Maul, Young Apprentice x3, Dr. Evazan & Ponda Baba x2, "
    "Galen, Secret Apprentice x2, IG-100 MagnaGuard x2, The Phantom Menace x2, "
    "Force Field x2, Imperial Barrier x2, Sith Fury x2, Sonic Bombardment x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Quick Draw", True),
    n("Anger, Fear, Aggression", True),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Jar Jar Binks"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi", True),
    n("Senator Leia Organa"),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("A Jedi's Resilience", qty=2),
    n("Blaster Deflection"),
    n("Clash Of Sabers"),
    n("Either Way, You Win", True, qty=2),
    n("Escape Pod", True),
    n("Houjix"),
    n("Impressive, Most Impressive", True),
    n("Jedi Levitation", True),
    n("Let The Wookiee Win", True),
    n("Wookiee Roar", True, qty=2),
    n("Odin Nesloor & First Aid"),
    n("Out Of Commission & Transmission Terminated"),
    n("Rebel Barrier"),
    n("Rebel Leadership", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council"),
    n("Wesa Gotta Grand Army"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hoth: Echo Command Center"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Alderaan Consular Ship", True),
    n("Bright Hope", True),
    n("Gold Leader In Gold 1", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Tantive IV", True),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon", True),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum"),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Prepared Defenses"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("Battle Droid Squad", qty=2),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba", qty=2),
    n("Galen, Secret Apprentice", qty=2),
    n("IG-100 MagnaGuard", qty=2),
    n("Lurke"),
    n("Jango Fett, The Assassin"),
    n("A Sith's Weapon"),
    n("Blaster Rack", True),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("The Phantom Menace", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("Control & Set For Stun"),
    n("Force Field", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Barrier", qty=2),
    n("Maul Strikes"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sith Fury", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Sonic Bombardment", True, qty=2),
    n("Weapon Levitation"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Blockade Support Ship"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Dark Jedi Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("After Her!", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("Firepower", True),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
]
DS_ADD = [
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-A Decide, Huh?", True),
]
