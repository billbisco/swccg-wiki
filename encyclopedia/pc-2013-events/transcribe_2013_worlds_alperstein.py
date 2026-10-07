#!/usr/bin/env python3
"""2013 World Championship Day 2: Barry Alperstein Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Barry Alperstein"
USERNAME = "MrFromMars"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2013 Worlds Day 2 p04 Barry Alperstein LS.png"
DS_SCAN = "2013 Worlds Day 2 p03 Barry Alperstein DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username MrFromMars. Event Worlds 2013. "
    "Deck title Big Fish Little Fish Cardboard Box. LIGHT. "
    "Beat Slavers / Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "Jabba's Place dested Jabba's Palace. Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Han dested Han With Heavy Blaster Pistol. HFTMF dested Heading For The Medical Frigate. "
    "Seeking dested Seeking An Audience. Incon Barriers dested as written. "
    "H1: War Room dested Home One: War Room. Luke, SITF dested Luke Skywalker, Strong In The Force. "
    "Speak With The Jedis dested Speak With The Jedi Council. "
    "Armed and Dang + KDH dested Armed And Dangerous & Krayt Dragon Howl. "
    "LTWW dested Let The Wookiee Win. Wesg dested Wesa Gotta Grand Army. "
    "Luke's Stick dested Luke's Lightsaber. Jedi Lev dested Jedi Levitation. "
    "Swing + a miss dested Swing-And-A-Miss. Tat Utility Belt dested Tatooine Utility Belt. "
    "Shoooooooot dested Shoo! Shoo!. Yoda, GW dested Yoda, Great Warrior. "
    "Corran Horn (Engblom) dested Corran Horn. 3PO Parts dested Threepio With His Parts Showing. "
    "ACKbar dested Admiral Ackbar. Boss Nass Chamber dested Naboo: Boss Nass' Chambers. "
    "Form left column reprints 37–38 on lines 39–40. TCC dested Tatooine Celebration. "
    "AFA dested Anger, Fear, Aggression. HCGAHB dested He Can Go About His Business. "
    "Insight dested Your Insight Serves You Well. DDTA dested Don't Do That Again. "
    "Tragedy dested A Tragedy Has Occurred. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username MrFromMars. "
    "Deck title Sorry I left my lightsaber in my other space pants. DARK. "
    "Slaving / Empire dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Slaving Camp Headquarters dested Kashyyyk: Slaving Camp Headquarters. "
    "Merc Slavers dested Mercenary Slavers. DoT + SD dested Den Of Thieves & Special Delivery. "
    "SS: Passenger Deck dested Jabba's Sail Barge: Passenger Deck. "
    "Breached Def + Molator dested Breached Defenses & Molator. "
    "Dr. E dested Dr. Evazan. 4-LOM w Rifle dested 4-LOM With Concussion Rifle. "
    "Ghhhk + TRUEV dested Ghhhk & Those Rebels Won't Escape Us. "
    "Lightsaber D dested Lightsaber Deficiency. Slave I, SoF dested Slave I, Symbol Of Fear. "
    "Kash: Wookiee Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "A, A, A dested Ability, Ability, Ability. Kash: Skyhook Platform dested Kashyyyk: Skyhook Platform. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. Merc Pilot dested Mercenary Pilot. "
    "Ket Maliss, SK dested Ket Maliss, Shadow Killer. Dengar w/ Carbine dested Dengar With Blaster Carbine. "
    "Bossk w/ Mortar Gun dested Bossk With Mortar Gun. Igeegee dested IG-88 With Riot Gun. "
    "Jango lorian, FoF dested Jango Fett, The Assassin. "
    "Bound By The Force struck dested Stunned Brawls as written. K+D dested Knowledge And Defense. "
    "Form left column reprints 37–38 on lines 39–40. Dittos inherit the first named line. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han With Heavy Blaster Pistol", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Incon Barriers"),
    n("Home One: War Room"),
    n("Luke Skywalker, Strong In The Force"),
    n("Rebel Leadership", True),
    n("Obi-Wan's Lightsaber"),
    n("Padme Naberrie", True),
    n("Speak With The Jedi Council"),
    n("Clash Of Sabers"),
    n("Disarmed"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Boushh"),
    n("Let The Wookiee Win", True),
    n("Wesa Gotta Grand Army"),
    n("A Gift"),
    n("Luke's Lightsaber"),
    n("Jedi Levitation", True),
    n("Swing-And-A-Miss"),
    n("Rebel Leadership", True),
    n("Let The Wookiee Win", True),
    n("Jedi Levitation", True),
    n("Tatooine Utility Belt", True),
    n("Chewbacca, Protector"),
    n("Shoo! Shoo!", True),
    n("Dash Rendar", True),
    n("Yoda, Great Warrior"),
    n("Corran Horn"),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Sense"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan Kenobi", True),
    n("Let The Wookiee Win", True),
    n("Jedi Lightsaber", True),
    n("Rebel Leadership", True),
    n("Shoo! Shoo!", True),
    n("Blaster Deflection"),
    n("Double Agent"),
    n("Lucky Shot", True),
    n("Wesa Gotta Grand Army"),
    n("Yoda, Great Warrior"),
    n("Obi-Wan Kenobi", True),
    n("Clash Of Sabers"),
    n("Lando Calrissian, Scoundrel"),
    n("Sense"),
    n("Let The Wookiee Win", True),
    n("Home One"),
    n("Tatooine Celebration"),
    n("Imperial Atrocity", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Sai'torr Kal Fas", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
]
LS_ADD = [
    n("Aim High"),
    n("Chasm", True),
    n("Weapons Display", True),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt", True),
    n("Den Of Thieves & Special Delivery"),
    n("Jabba's Haven"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Breached Defenses & Molator"),
    n("Scum And Villainy"),
    n("Velken Tezeri", True),
    n("Dr. Evazan"),
    n("Ponda Baba", True),
    n("4-LOM With Concussion Rifle"),
    n("Wookiee Subjugation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True, qty=3),
    n("Lightsaber Deficiency", True, qty=3),
    n("Imperial Barrier", qty=3),
    n("Abyssin Ornament", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Nal Hutta"),
    n("Zuckuss In Mist Hunter"),
    n("Laser Cannon Battery"),
    n("Jabba's Space Cruiser", True),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Hutt Bounty", True),
    n("Protocol Failure"),
    n("Ability, Ability, Ability"),
    n("Kashyyyk: Skyhook Platform"),
    n("Jabba's Sail Barge", True),
    n("P-59"),
    n("Outer Rim Scout", qty=5),
    n("Boba Fett, Prepared Hunter"),
    n("Lady Valarian"),
    n("Mercenary Pilot"),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Probot"),
    n("Garindan", True),
    n("Ket Maliss, Shadow Killer"),
    n("Dengar With Blaster Carbine", True),
    n("Bossk With Mortar Gun", True),
    n("IG-88 With Riot Gun", True),
    n("Prince Xizor"),
    n("Jango Fett, The Assassin"),
    n("Force Push", True),
    n("Stunned Brawls"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("We'll Let Fate Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance", True),
    n("Secret Plans"),
]
