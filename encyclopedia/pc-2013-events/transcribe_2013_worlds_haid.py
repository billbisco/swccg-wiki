#!/usr/bin/env python3
"""2013 World Championship Day 2: Tom Haid Xerox Profit + Wookiee Slaving."""
from __future__ import annotations

PLAYER = "Tom Haid"
USERNAME = "Xenth"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 40
DS_PAGE = 41
LS_SCAN = "2013 Worlds Day 2 p40 Tom Haid LS.png"
DS_SCAN = "2013 Worlds Day 2 p41 Tom Haid DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Tom Haid. Username Xenth. "
    "Deck title Inspired By Schmaltz!. LIGHT. Worlds 2013, dated 8/11/13. "
    "You Can Either Profit By This... dested You Can Either Profit By This... / Or Be Destroyed. "
    "JP: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Tat: Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Ltan dested Lando Calrissian. "
    "Luke Skywalker, SitForce dested Son Of Skywalker. "
    "Boss Nass' Chambers dested Naboo: Boss Nass' Chambers. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Lando Cal, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Obi's Lightsaber dested Obi-Wan's Lightsaber. "
    "Tat Utility Belt dested Tatooine Utility Belt. "
    "Speak w/ JCC dested Speak With The Jedi Council. "
    "Armed & Dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "N00000000000! dested NOOOOOOOOOOOO!. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army. "
    "Form left column reprints 37-38 on lines 39-40 are Sense / Inconsequential Barriers. "
    "Additional A Tragedy / Aim High / Chasm moved to Light shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Tom Haid. Username Xenth. "
    "Deck title I'm Sorry Everybody. DARK. Worlds 2013, dated 8/11/13. "
    "Wookiee Slaving Op dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Kash: Slaving Camp HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Den Of Thieves combo dested Den Of Thieves & Special Delivery. "
    "Sail Barge: Passenger Deck dested Jabba's Sail Barge: Passenger Deck. "
    "Kash: Skyhook Platform dested Kashyyyk: Skyhook Platform. "
    "Kash: Wookiee Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Breached Defenses combo dested Breached Defenses & Molator. "
    "Ability x3 dested Ability, Ability, Ability. "
    "Merc. Pilot dested Mercenary Pilot. "
    "Reegesk dested Ree-Yees. "
    "Velken Tezeri dested Velken Tezeri. "
    "Slave 1, SoFear dested Slave I, Symbol Of Fear. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "We'll Let Fate Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Additional I Find Your Lack / Resistance / Secret Plans moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Dr. Evazan / Ponda Baba. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Lando Calrissian", True),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Son Of Skywalker", True, qty=3),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Yoda, Great Warrior", True, qty=2),
    n("Corran Horn"),
    n("Chewbacca, Protector"),
    n("Padme Naberrie", True),
    n("Threepio With His Parts Showing"),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Dash Rendar", True),
    n("Boushh"),
    n("Home One"),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Tatooine Utility Belt", True),
    n("A Gift"),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Disarmed"),
    n("Swing-And-A-Miss"),
    n("Sense", qty=2),
    n("Inconsequential Barriers"),
    n("Clash Of Sabers", qty=2),
    n("Blaster Deflection"),
    n("Lucky Shot", True),
    n("Jedi Levitation", True, qty=3),
    n("Speak With The Jedi Council"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Rebel Leadership", True, qty=3),
    n("NOOOOOOOOOOOO!", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=4),
    n("Double Agent"),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Ultimatum"),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Aim High", True),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Den Of Thieves & Special Delivery", True),
    n("Wookiee Subjugation", True),
    n("Power Of The Hutt"),
    n("Mercenary Slavers", True),
    n("Jabba's Haven", True),
    n("Knowledge And Defense", True),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Skyhook Platform", True),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Breached Defenses & Molator", True),
    n("Scum And Villainy"),
    n("Hutt Bounty", True),
    n("Protocol Failure", True),
    n("Ability, Ability, Ability"),
    n("Outer Rim Scout", qty=5),
    n("Mercenary Pilot", True),
    n("P-59"),
    n("Lady Valarian", True),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Probot", True),
    n("Garindan", True),
    n("Ket Maliss, Shadow Killer", True),
    n("Dengar With Blaster Carbine", True),
    n("Bossk With Mortar Gun", True),
    n("Ree-Yees", True),
    n("Prince Xizor", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Velken Tezeri", True),
    n("Dr. Evazan"),
    n("Ponda Baba", True),
    n("4-LOM With Concussion Rifle"),
    n("Jabba's Sail Barge", True),
    n("Slave I, Symbol Of Fear", True),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Space Cruiser", True),
    n("Laser Cannon Battery"),
    n("Look Sir, Droids", True),
    n("Force Push", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True, qty=3),
    n("Lightsaber Deficiency", True, qty=3),
    n("Imperial Barrier", qty=3),
    n("Abyssin Ornament", qty=2),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Battle Order", True),
    n("A Useless Gesture"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
]
DS_ADD = []
