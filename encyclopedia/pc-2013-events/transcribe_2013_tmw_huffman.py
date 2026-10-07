#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Blake Huffman Xerox CCT / Hyperdrive."""
from __future__ import annotations

PLAYER = "Blake Huffman"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 29
DS_PAGE = 28
LS_SCAN = "2013 Texas Mini Worlds Day 1 p29 Blake Huffman LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p28 Blake Huffman DS.png"
LS_NOTE = (
    "Handwritten 2009 Print Form (12 shields, left 1-36 / right 37-60). "
    "Name Blake Huffman. Username blank. Deck Name blank. "
    "Event Date and Event Name blank. LIGHT/DARK boxes empty. "
    "Do not dest as a new person. "
    "Hyperdrive dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Master Quigon dested Master Qui-Gon. "
    "Han Solo: Innocent Scoundrel dested Han Solo, Innocent Scoundrel. "
    "Heading to the Medical Frigate dested Heading For The Medical Frigate. "
    "Cor: Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Obiwan, Padawan Learner dested Obi-Wan Kenobi, Padawan Learner. "
    "Into the Garbage Chute dested Into The Garbage Chute, Flyboy!. "
    "Jedi Lightsaber dested Jedi Lightsaber. "
    "Armed & dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "Yarua dested Yarua. "
    "Weapon Lev dested Weapon Levitation. "
    "Jedi Lev dested Jedi Levitation. "
    "Clash of the Sabers dested Clash Of Sabers. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Sorry about the mess Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Chewbacca, Walking Carpet dested Chewbacca, Walking Carpet. "
    "Mace dested Mace Windu. "
    "Maris Brood dested Maris Brood, Fallen Jedi. "
    "Yoda, Senior Council Member dested Yoda, Senior Council Member. "
    "Simple tricks dested Simple Tricks And Nonsense. "
    "Your insight dested Your Insight Serves You Well. "
    "Lets Keep a little Optimism dested Let's Keep A Little Optimism Here. "
    "He can go about his bus dested He Can Go About His Business. "
    "Unique overcounts sheet-accurate: Speak With The Jedi Council x2, "
    "Rebel Barrier x2, Into The Garbage Chute, Flyboy! x3, Blaster Deflection x2, "
    "Wesa Gotta Grand Army x2, A Jedi's Resilience x2, Master Qui-Gon x2, "
    "Obi-Wan Kenobi, Padawan Learner x2, Alderaan Consular Ship x2, Mace Windu x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2009 Print Form (12 shields, left 1-36 / right 37-60). "
    "Name Blake Huffman. Username blank. Deck Name blank. "
    "Event Date and Event Name blank. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Pinto CCT leftover. "
    "CCT dested Carbon Chamber Testing / My Favorite Decoration. "
    "JP: Dungeon dested Jabba's Palace: Dungeon. "
    "CC: Carbonite Chamber dested Cloud City: Carbonite Chamber. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Carbonite Console dested Carbonite Chamber Console. "
    "IG-88 Neural Inhibitor dested IG-88's Neural Inhibitor. "
    "Jabba's Prize dested Jabba's Prize as written. "
    "Control Combo dested Control & Set For Stun. "
    "I have you now dested I Have You Now. "
    "Lightsaber Def dested Lightsaber Deficiency. "
    "Maul w Saber dested Darth Maul With Lightsaber. "
    "Ponda Baba & Dr E dested Dr. Evazan & Ponda Baba. "
    "Vader w Saber dested Darth Vader With Lightsaber. "
    "Mara w Saber dested Mara Jade With Lightsaber. "
    "A Dark Time For The Rebellion dested A Dark Time For The Rebellion. "
    "Grand Moff Tarkin dested Grand Moff Tarkin. "
    "Sniper Combo dested Sniper & Dark Strike. "
    "The Circle is now Complete dested The Circle Is Now Complete. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. "
    "The Emperor dested Emperor Palpatine. "
    "Luke, Luuke dested Luuke. "
    "4-lom with Gun dested 4-LOM With Concussion Rifle. "
    "Short Range Fighters Combo dested Short Range Fighters & Watch Your Back!. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Coward dested Come Here You Big Coward. "
    "You Can't Hide Forever dested You Cannot Hide Forever. "
    "I Find Your Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Unique overcounts sheet-accurate: Stunning Leader x2, "
    "Darth Maul With Lightsaber x2, Darth Vader With Lightsaber x2, "
    "Force Lightning x2, Victory x2, Imperial Artillery x2, Imperial Barrier x2, "
    "Sense x2, Emperor Palpatine x3. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Credits Will Do Fine"),
    n("Quick Draw", True),
    n("A Remote Planet", True),
    n("Rycar Ryjerd", True),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Heading For The Medical Frigate"),
    n("Master Qui-Gon", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Disarmed"),
    n("Coruscant: Jedi Council Chamber"),
    n("Han Solo, Innocent Scoundrel"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Barrier", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Into The Garbage Chute, Flyboy!", True, qty=3),
    n("Jedi Lightsaber", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Yarua", True),
    n("Imperial Atrocity", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Weapon Levitation"),
    n("Ki-Adi-Mundi", True),
    n("Senator Leia Organa"),
    n("Clash Of Sabers"),
    n("Alderaan Consular Ship", qty=2),
    n("Lucky Shot", True),
    n("Jedi Levitation", True),
    n("Senator Mon Mothma"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Demotion", True),
    n("Obi-Wan's Lightsaber"),
    n("Sai'torr Kal Fas", True),
    n("Lady Luck"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Coruscant"),
    n("Aayla Secura"),
    n("Guardian's Lightsaber"),
    n("Lightsaber Proficiency"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Chewbacca, Walking Carpet"),
    n("Mace Windu", True, qty=2),
    n("Maris Brood, Fallen Jedi"),
    n("Yoda, Senior Council Member", True),
    n("Obi-Wan's Journal"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Jabba's Palace: Dungeon"),
    n("Despair", True),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Carbonite Chamber Console", True),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Jabba's Prize"),
    n("Force Lightning", qty=2),
    n("Stunning Leader", qty=2),
    n("Control & Set For Stun"),
    n("Any Methods Necessary"),
    n("I Have You Now"),
    n("Garindan", True),
    n("Lightsaber Deficiency", True),
    n("Disarmed"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Kashyyyk"),
    n("Jabba's Palace: Audience Chamber"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Imperial Barrier", qty=2),
    n("Imperial Artillery", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Sense", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Grand Moff Tarkin", True),
    n("Boba Fett, Prepared Hunter"),
    n("Tarkin's Bounty", True),
    n("Sniper & Dark Strike"),
    n("No Escape"),
    n("Defensive Fire", True),
    n("The Circle Is Now Complete"),
    n("Special Delivery", True),
    n("Lateral Damage"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Victory", qty=2),
    n("Grand Admiral Thrawn"),
    n("Emperor Palpatine", True, qty=3),
    n("Protocol Failure"),
    n("Imperial Command"),
    n("Death Star: War Room", True),
    n("Death Star"),
    n("Luuke", True),
    n("Black Sun Fleet"),
    n("4-LOM With Concussion Rifle", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
]
DS_ADD = []
