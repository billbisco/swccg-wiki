#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Carl Buck Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Carl Buck"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2013 Match Play Championship p19 Carl Buck LS.png"
DS_SCAN = "2013 Match Play Championship p20 Carl Buck DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title This is Good. Light. "
    "There is Good in Him / I Can Save Him. DTOM → Don't Tread On Me. "
    "Out of Commission & Transmission Terminated as written. "
    "Odin Nesler & First Aid dested Odin Nesloor & First Aid. "
    "Sorry About The Mess + Blaster Proficiency as written. "
    "Yavin 4: War Room dested Yavin 4: Massassi War Room. "
    "Obi Wan Lightsaber dested Obi-Wan's Lightsaber (weapon, with Jedi Lightsaber and Qui-Gon's Lightsaber). "
    "Chewie, Enraged as written. Mace Windu / Master of the Order as written. "
    "Eh-16 / Ch-19 dested R2-D2. Threepio w/ Parts Showing → Threepio With His Parts Showing. "
    "AFA → Anger, Fear, Aggression. OJCTW dested Only Jedi Carry That Weapon. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title Hunt Down. Dark. "
    "Hunt Down / Fire Come out dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Executor Meditation Chamber / Holotheatre as written. "
    "Com Sien De'clen dested Combat Readiness. Dark Time dested A Dark Time For The Rebellion. "
    "Sith Fury & End This Destructive Conflict as written. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "Pratical Failure dested Protocol Failure. Where are you taking this thing as written. "
    "Ability, Ability, Ability as written. Cyborg Commander's Saber dested Darth Vader's Lightsaber. "
    "Galen's Saber dested Galen's Lightsaber, Vader's Gift. "
    "Darth Vader Dark Lord of Sith / Betrayer of Jedi as written. "
    "Galen Secret Apprentice dested Galen Marek, Starkiller. "
    "Cyborg Commander, Hunter of Jedi dested Darth Vader. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Shield 1 Imperial Fallen dested Imperial Decree. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Endor: Landing Platform"),
    n("Endor: Chief Chirpa's Hut"),
    n("Don't Tread On Me", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas"),
    n("Draw Their Fire"),
    n("Imperial Atrocity", True, qty=2),
    n("Seeking An Audience", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi Council"),
    n("Were You Looking For Me?"),
    n("Houjix"),
    n("Odin Nesloor & First Aid", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True),
    n("On The Edge"),
    n("Let The Wookiee Win", True),
    n("Blaster Deflection"),
    n("Control & Tunnel Vision"),
    n("Sense"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Yavin 4: Massassi War Room", True),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Home One"),
    n("Spiral"),
    n("Tantive IV", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order", True),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight"),
    n("R2-D2", True),
    n("Threepio With His Parts Showing"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
]
LS_ADD = [
    n("Jabba's Prize", True),
]

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor"),
    n("Surface Defense", True),
    n("Lightsaber Deficiency", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Ghhhk"),
    n("Combat Readiness", True),
    n("A Dark Time For The Rebellion", True),
    n("Force Push", True),
    n("Close Call", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("Sonic Bombardment", True),
    n("You Are Beaten"),
    n("Force Field", True, qty=2),
    n("Sith Fury & End This Destructive Conflict", True),
    n("He Is Not Ready", True),
    n("Protocol Failure", True),
    n("Where Are You Taking This ... Thing?", True),
    n("Image Of The Dark Lord", True),
    n("First Strike"),
    n("Imperial Justice", True),
    n("Something Special Planned For Them", True),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Gift Of The Master", True),
    n("Ability, Ability, Ability", True),
    n("Visage Of The Emperor", qty=2),
    n("Vader's Lightsaber"),
    n("Darth Vader's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True, qty=2),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Darth Vader", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Prince Xizor"),
    n("P-59"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear", True),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Cloud City: Security Tower", True),
    n("Death Star: War Room", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Decree", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Firepower", True),
    n("Wipe Them Out, All Of Them", True),
]
DS_ADD = []
