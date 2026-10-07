#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Jan Westergard.

Source: 2014-TMW-Day-1.pdf pages 9–10 (2013 form).
Name Jan dested Jan Westergard (informed 99.9%; same DANGER ZONE Watch Your Step
as 2013 SoCal Jan Westergard / Ghosttrain). Username blank. No Changes on Day 2
(Day 2 p11–p12 skip card text).
"""
from __future__ import annotations

PLAYER = "Jan Westergard"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2014 Texas Mini Worlds Day 1 p09 Jan Westergard LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p10 Jan Westergard DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields). No Changes on Day 2."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Jan dested Jan Westergard. Username blank. LIGHT/DARK both empty; cards are Light. "
    "No Changes on Day 2. "
    "WATCH YO STEP dested Watch Your Step / This Place Can Be A Little Rough. "
    "DANGER ZONE (cantina) dested Tatooine: Cantina. "
    "DB94 dested Tatooine: Docking Bay 94. "
    "IMBATS dested I Must Be Allowed To Speak. "
    "Squass dested Squadron Assignments. "
    "AIR5 dested Artoo-Detoo In Red 5. "
    "Carpet Chewie dested Chewbacca, Walking Carpet. "
    "Han & Gun dested Han With Heavy Blaster Pistol. "
    "Pulsar Skate dested Booster In Pulsar Skate. "
    "BoShek's Boat dested BoShek's Mad Freighter. "
    "BoShek, BS dested BoShek, Brash Smuggler. "
    "Lando's Yacht dested Lady Luck. "
    "Leebo dested LE-BO2D9. "
    "Doallyn dested Sergeant Doallyn. "
    "Nien Nunb crossed, Chewbacca, Walking Carpet dested Chewbacca, Walking Carpet. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "C & TV dested Control & Tunnel Vision. "
    "Houjix & OON dested Houjix & Out Of Nowhere. "
    "ICBW dested It Could Be Worse. "
    "NQA dested No Questions Asked. "
    "STAN dested Simple Tricks And Nonsense. "
    "Your Ship dested Your Ship?. "
    "WD dested Weapons Display. "
    "Unique overcounts sheet-accurate (Tatooine Celebration x2, Artoo-Detoo In Red 5 x2, "
    "Luke Skywalker x2, Imperial Atrocity x2, Kyle Katarn x2, All Wings Report In & Darklighter Spin x2, "
    "Control & Tunnel Vision x2, Rebel Barrier x2, Lando Calrissian, Unlikely Hero x2, "
    "Han With Heavy Blaster Pistol x2, Chewbacca, Walking Carpet x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Jan dested Jan Westergard. Username blank. LIGHT/DARK both empty; cards are Dark. "
    "No Changes on Day 2. "
    "CCT/IG-88 dested Carbon Chamber Testing / Cat And Mouse. "
    "Victory dested Victory as written. "
    "Mandalorian FoF dested Jango Fett, The Assassin. "
    "Slave 1 SoF dested Slave I, Symbol Of Fear. "
    "Control & SFS dested Control & Set For Stun. "
    "LS Deficiency crossed, Darth Maul With Lightsaber dested Darth Maul With Lightsaber. "
    "He Is Not Ready crossed, He Is Not Ready dested as the replacement combo line. "
    "The Emperor dested Emperor Palpatine. "
    "G&D dested Knowledge And Defense. "
    "IHYN dested I Have You Now. "
    "CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "Line 14 empty skipped. "
    "Unique overcounts sheet-accurate (Force Lightning x2, Sense x2, Defensive Fire x2, "
    "Imperial Artillery x2, Victory x2, Darth Vader x2, Emperor Palpatine x3). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Tatooine: Mos Eisley"),
    n("Corellia", True),
    n("Heading For The Medical Frigate"),
    n("I Must Be Allowed To Speak", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Menace Fades"),
    n("Tatooine Celebration", qty=2),
    n("Bacta Tank"),
    n("Projection Of A Skywalker"),
    n("Strikeforce", True),
    n("Imperial Atrocity", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Millennium Falcon"),
    n("Chewbacca, Walking Carpet"),
    n("Han With Heavy Blaster Pistol"),
    n("Booster In Pulsar Skate"),
    n("Mirax Terrik"),
    n("Outrider"),
    n("Dash Rendar"),
    n("BoShek's Mad Freighter"),
    n("BoShek, Brash Smuggler"),
    n("Lady Luck"),
    n("Lando Calrissian, Unlikely Hero"),
    n("LE-BO2D9"),
    n("Melas", True),
    n("Talon Karrde"),
    n("Sergeant Doallyn", True),
    n("Wedge Antilles", True),
    n("Kyle Katarn", qty=2),
    n("Chewbacca, Walking Carpet"),
    n("Dodge"),
    n("Melas", True),
    n("It's A Hit"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Rebel Barrier", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("A Few Maneuvers"),
    n("It Could Be Worse"),
    n("Desperate Reach", True),
    n("No Questions Asked"),
    n("Han With Heavy Blaster Pistol"),
    n("Melas", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Chasm"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / Cat And Mouse"
DS_CARDS = [
    n("Carbon Chamber Testing / Cat And Mouse"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Carbonite Chamber Console", True),
    n("Cloud City: Security Tower", True),
    n("Jabba's Prize"),
    n("IG-88", True),
    n("Neural Inhibitor", True),
    n("Jabba's Palace: Dungeon"),
    n("Special Modification"),
    n("All My Urchins"),
    n("Force Lightning", qty=2),
    n("Stunning Leader", qty=2),
    n("Sense", qty=2),
    n("Defensive Fire", True, qty=2),
    n("Imperial Artillery", qty=2),
    n("Darth Maul With Lightsaber"),
    n("I Have You Now"),
    n("Victory", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("A Dark Time For The Rebellion", True),
    n("Darth Vader", True, qty=2),
    n("Imperial Command", True),
    n("Luuke"),
    n("Darth Maul With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Grand Admiral Thrawn"),
    n("Slave I, Symbol Of Fear"),
    n("Despair", True),
    n("Cold Feet", True),
    n("Blaster Rack"),
    n("First Strike"),
    n("Death Star: War Room", True),
    n("Superlaser Mark II"),
    n("Control & Set For Stun"),
    n("Special Delivery", True),
    n("Lateral Damage"),
    n("No Escape"),
    n("Coruscant: Imperial City", True),
    n("Grand Moff Tarkin"),
    n("Imperial Barrier"),
    n("He Is Not Ready", True),
    n("Boba Fett, Prepared Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Kashyyyk"),
    n("Count Dooku"),
    n("Jango Fett, The Assassin"),
    n("Blockade Flagship: Bridge"),
    n("Emperor Palpatine", True, qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Abyss", True),
    n("Fanfare"),
    n("Restricted Access", True),
    n("Firepower", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
