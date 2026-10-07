#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Aaron Nelson Xerox WYS + NMNPND."""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 Texas Mini Worlds Day 1 p03 Aaron Nelson LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p04 Aaron Nelson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Aaron Nelson. Username Airdog2003. "
    "Deck Name SoCal WYS Mains. LIGHT. Event Texas Mini Worlds 2013. "
    "Do not rewrite the 2013 MPC Aaron Nelson leftover. Do not dest as Jake Nelson. "
    "WYS/TPCBACR dested Watch Your Step / This Place Can Be A Little Rough. "
    "Captain Solo dested Captain Han Solo. "
    "Houjix Combo dested Houjix & Out Of Nowhere. "
    "Padme Naberrie dested Padme Naberrie. "
    "HMBHT dested Hear Me Baby, Hold Together. "
    "Antilles Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Obi's Journal dested Obi-Wan's Journal. "
    "Boss Nass it's really dested Naboo: Boss Nass' Chambers. "
    "Have You Seen These dested Have You Seen These Stormtroopers? as written. "
    "Mace Master of the Order dested Mace Windu, Master Of The Order. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Qui-Gon w/ Saber dested Qui-Gon Jinn With Lightsaber. "
    "Leia RP dested Leia, Rebel Princess. "
    "Naboo BNC dested Naboo: Boss Nass' Chambers. "
    "S&TM Combo dested All Wings Report In & Darklighter Spin. "
    "Executor Backdoor dested Executor: Docking Bay as written. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Nobility dested Nobility as written. "
    "DDTA dested Don't Do That Again. "
    "YISYW dested Your Insight Serves You Well. "
    "LKALOH dested Let's Keep A Little Optimism Here. "
    "Additional Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "Unique overcounts sheet-accurate: Luke JK x3, Rebel Leadership x3. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Aaron Nelson. Username Airdog2003. "
    "Deck Name West Coast Waiters. DARK. Event Texas Mini Worlds 2013. "
    "Do not rewrite the 2013 MPC Aaron Nelson leftover. Do not dest as Jake Nelson. "
    "No Money, No Parts, No Deal dested No Money, No Parts, No Deal! / You're A Slave?. "
    "Boba Fett Bounty Hunter dested Boba Fett, Bounty Hunter. "
    "The Mandalorian, Father of Fett dested The Mandalorian as written. "
    "Myn Kyromach dested Myn Kyneugh. "
    "4-LOM With Rifle dested 4-LOM With Concussion Rifle. "
    "Dr E & Ponda dested Dr. Evazan & Ponda Baba. "
    "Darth Sidious dested Darth Sidious. "
    "Fear Comes Naturally dested Fear Is My Ally. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me?. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "Protocol Failure dested Protocol Failure. "
    "Masterful Combo dested Masterful Move & Endor Occupation. "
    "Evader Concentrate dested Evader & Concentrate Fire as written. "
    "Surface Bombardment dested Surface Bombardment as written. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "What Have You Done dested What Have You Done? as written. "
    "Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "CHYBC dested Come Here You Big Coward. "
    "TINT dested There Is No Try. "
    "AUG dested A Useless Gesture. "
    "YCHFF dested You Cannot Hide Forever. "
    "We'll let fate dested We'll Let Fate-a Decide, Huh?. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Captain Han Solo", True),
    n("Millennium Falcon", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Menace Fades"),
    n("Padme Naberrie", True),
    n("Hear Me Baby, Hold Together", True),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Obi-Wan's Journal"),
    n("Chewie", True),
    n("Disarmed"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Desperate Reach", True),
    n("Jedi Lightsaber", True),
    n("Han's Toolkit"),
    n("Sai'torr Kal Fas", True),
    n("Naboo: Boss Nass' Chambers", qty=2),
    n("Have You Seen These Stormtroopers?"),
    n("Sense", qty=2),
    n("Corran Horn"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Let The Wookiee Win", True),
    n("Rebel Leadership", True, qty=3),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Punch It!"),
    n("Leia, Rebel Princess"),
    n("That's One", True),
    n("Mace Windu", True),
    n("Blaster Deflection", qty=2),
    n("Imperial Atrocity", True),
    n("Obi-Wan's Lightsaber"),
    n("Home One"),
    n("All Wings Report In & Darklighter Spin"),
    n("Executor: Docking Bay"),
    n("Lightsaber Proficiency"),
    n("Seeking An Audience", True),
    n("Admiral Ackbar", True),
    n("Luke's Lightsaber"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Nobility", True),
    n("Rycar Ryjerd", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
]
LS_ADD = [
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Your Ship?"),
]


DS_START = "No Money, No Parts, No Deal! / You're A Slave?"
DS_CARDS = [
    n("No Money, No Parts, No Deal! / You're A Slave?"),
    n("Tatooine: Watto's Junkyard", True),
    n("Tatooine: Mos Espa"),
    n("Darth Vader With Lightsaber"),
    n("Boba Fett, Bounty Hunter"),
    n("The Mandalorian"),
    n("Myn Kyneugh", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("The Emperor", True),
    n("Lightsaber Proficiency", True),
    n("Watto", True, qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle"),
    n("General Veers", True),
    n("Aurra Sing"),
    n("Darth Sidious"),
    n("Grand Moff Tarkin", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Trample", qty=3),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Maul's Sith Infiltrator"),
    n("Fear Is My Ally"),
    n("Why Didn't You Tell Me?"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Endor"),
    n("Kashyyyk"),
    n("Imperial Decree", True, qty=2),
    n("Protocol Failure"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Imperial Barrier", qty=2),
    n("Evader & Concentrate Fire", True),
    n("Close Call"),
    n("Cease Fire!"),
    n("According To My Design"),
    n("Surface Bombardment", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Force Push", True),
    n("Ghhhk"),
    n("We Must Accelerate Our Plans"),
    n("Prepared Defenses"),
    n("What Have You Done?", True),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("Tatooine: Jabba's Palace"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
]
DS_ADD = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Battle Order", True),
]
