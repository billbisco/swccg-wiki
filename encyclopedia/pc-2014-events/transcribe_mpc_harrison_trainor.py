#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matthew Harrison-Trainor.

Source: MPC-2014-Day-1-Main-Event.pdf pages 51–52 (2013 form, 15 shields).
Matt HT dested Matthew Harrison-Trainor. Holotable analog for slang.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 51
DS_PAGE = 52
LS_SCAN = "2014 Match Play Championship Day 1 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matthew Harrison-Trainor DS.png"
LS_DECK_NAME = "QMC."
DS_DECK_NAME = "Slavers"
NOTE = "Handwritten 2013 Xerox form. Holotable analog for slang."
LS_NOTE = (
    "Handwritten 2013 Xerox. Matt HT dested Matthew Harrison-Trainor. QMC dested Quiet "
    "Mining Colony / Independent Operation. Ellors Madak dested Ellors Madak (V). Lando "
    "UH dested Lando Calrissian, Unlikely Hero. Houjix + OON dested Houjix & Out Of "
    "Nowhere. All Wings Report In & DS dested All Wings Report In & Darklighter Spin. "
    "Alter Non-V with checkbox checked dested Alter (V) from checkbox; Non-V noted. "
    "Jabba's Prize listed as shield 1 dested Jabba's Prize (V) shield. Holotable analog "
    "for Foul Moudama, Nien Nunb, Sullustan Smuggler, Trooper Utris M'Toc, Kal'Falnl "
    "C'ndros, Uutkik, Leslomy Tacema, Sergeant Edian, Han Solo, Innocent Scoundrel, "
    "Chewbacca, Walking Carpet. (V) from checkbox. Unique overcounts sheet-accurate "
    "(Imperial Atrocity x2, Rebel Barrier x2, Houjix & Out Of Nowhere x2, Path Of Least "
    "Resistance x2, Let The Wookiee Win (V) x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Slavers dested Wookiee Slaving Operation / Indentured To The "
    "Empire. IG-88, Renegade Droid dested IG-88, Renegade Droid. Jango Fett, The Assassin "
    "dested Jango Fett, The Assassin. Slave I SoF dested Slave I, Symbol Of Fear. P-59 "
    "dested P-59. Short Range Fighters Combo dested Short Range Fighters & Watch Your "
    "Back!. Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. Outer Rim Scout x4 "
    "unique overcount. Holotable analog. (V) from checkbox. Unique overcounts "
    "sheet-accurate (Lightsaber Deficiency x2, Outer Rim Scout x4, Sneak Attack (V) x2, "
    "Sonic Bombardment x3, Scum And Villainy x2, Short Range Fighters & Watch Your Back! "
    "x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Hiding In The Garbage", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("Imperial Atrocity", True),
    n("Imperial Atrocity"),
    n("Menace Fades"),
    n("Ellors Madak", True),
    n("Lee-Sub Sirln", True),
    n("Aayla Secura"),
    n("Kebyc", True),
    n("Overseer", True),
    n("Harc Seff", True),
    n("Lady Luck"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Cloud City: North Corridor"),
    n("Cloud City: West Gallery"),
    n("Foul Moudama"),
    n("Nien Nunb, Sullustan Smuggler"),
    n("Bespin"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: Guest Quarters"),
    n("Leslomy Tacema", True),
    n("Jar Jar Binks"),
    n("Uutkik", True),
    n("Chewbacca, Walking Carpet"),
    n("Leia, Rebel Princess"),
    n("Rebel Barrier", qty=2),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Choke"),
    n("Path Of Least Resistance", qty=2),
    n("Melas", True),
    n("Yoxgit"),
    n("Booster In Pulsar Skate"),
    n("Dark Approach", True),
    n("Alter", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Sergeant Edian", True),
    n("Mirax Terrik"),
    n("Kal'Falnl C'ndros"),
    n("Dash Rendar", True),
    n("It's A Hit"),
    n("All Wings Report In & Darklighter Spin"),
    n("Let The Wookiee Win", True, qty=2),
    n("Desperate Reach", True),
    n("Trooper Utris M'Toc", True),
    n("Blast The Door, Kid!"),
    n("Alternatives To Fighting"),
    n("Errant Venture"),
    n("It's A Trap!"),
    n("Luke With Lightsaber"),
    n("Tanus Spijek", True),
    n("Heading For The Medical Frigate", True),
    n("Cloud City: Incinerator", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Chasm", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Den Of Thieves & Special Delivery"),
    n("IG-88, Renegade Droid"),
    n("Jango Fett, The Assassin"),
    n("Imbalance & Kintan Strider"),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency"),
    n("Outer Rim Scout", qty=4),
    n("Sneak Attack", True, qty=2),
    n("Velken Tezeri", True),
    n("Jabba's Space Cruiser", True),
    n("Jabba's Sail Barge", True),
    n("Hutt Bounty", True),
    n("Sonic Bombardment", True),
    n("Sonic Bombardment", qty=2),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle"),
    n("P-59"),
    n("Protocol Failure"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Scum And Villainy", qty=2),
    n("Mercenary Slavers"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Boba Fett, Prepared Hunter"),
    n("Power Of The Hutt"),
    n("Slave I, Symbol Of Fear"),
    n("Jabba's Haven"),
    n("Kashyyyk"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Mercenary Pilot"),
    n("Ephant Mon"),
    n("Something Special Planned For Them", True),
    n("Dengar With Blaster Carbine", True),
    n("Bossk", True),
    n("Oh, Switch Off"),
    n("Tarkin's Orders"),
    n("Probot"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Wookiee Subjugation"),
    n("Imperial Barrier"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Jabba The Hutt", True),
    n("Look Sir Droids"),
    n("Weapon Levitation"),
    n("OOM-9", True),
    n("Ponda Baba", True),
    n("Maul's Sith Infiltrator"),
    n("Mara Jade With Lightsaber"),
    n("Prince Xizor"),
    n("Abyssin Ornament"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Fanfare", True),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("There Is No Try", True),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
]
DS_ADD = []
