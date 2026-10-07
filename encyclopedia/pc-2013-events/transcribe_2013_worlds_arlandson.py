#!/usr/bin/env python3
"""2013 World Championship Day 2: Charles Arlandson Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Charlie Arlandson"
USERNAME = "Brazen"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2013 Worlds Day 2 p09 Charles Arlandson LS.png"
DS_SCAN = "2013 Worlds Day 2 p10 Charles Arlandson DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form with handwritten replacements. "
    "Name field Charles Arlandson dested Charlie Arlandson. Username Brazen. "
    "Event Worlds Day 2. Deck name QMC. LIGHT. "
    "Quiet Mining Colony/Independent Operation dested Quiet Mining Colony / Independent Operation. "
    "Line 9 Aayla Secura struck dested Weapon Levitation. "
    "Line 10 Aayla Secura struck Sat. Donillyn dested Sergeant Doallyn. "
    "Line 12 Lando Calrissian, Unlikely Hero struck Chewie, Wook dested Chewbacca Of Kashyyyk. "
    "Line 17 Dash Rendar struck dested Choke. Line 28 Melas struck dested Booster Terrik. "
    "Line 33 Gas Tar Girls dested as written. Line 26 Uutik dested as written. "
    "Line 36 struck dested Choke. Line 38 Booster In Pulsar Skate struck dested It's A Trap!. "
    "Line 41 Cloud City: Upper Plaza Corridor struck dested Cloud City: Lower Corridor. "
    "Line 46 Much To Learn, You Still Have struck dested Luke, Trust Me. "
    "Line 47 struck dested Strikeforce. Line 53 Houjix combo dested Houjix & Out Of Nowhere. "
    "Line 56 Hear Me Baby, Hold Together struck dested Flash Of Insight. "
    "Line 59 Either Way You Win struck dested Ounee Ta. "
    "Shield 5 Planetary Defenses struck dested Do, Or Do Not. "
    "Shield 6 Only Jedi Carry That Weapon struck dested Wise Advice. "
    "Additional Jabba's Prize struck omitted. (There Is Another) dested There Is Another. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form with handwritten replacements. "
    "Charles Arlandson. Username Brazen. "
    "No Money, No Parts, No Deal!/You're a Slave? dested "
    "No Money, No Parts, No Deal! / You're A Slave?. "
    "Line 43 Outflank struck dested Imperial Barrier. "
    "Line 47 Masterful Move & Endor Occupation struck dested First Strike. "
    "Line 51 Sith Fury & End This Destructive Conflict struck dested Wipe Them Out, All Of Them. "
    "Line 54 Lightsaber Deficiency struck dested He Hasn't Come Back Yet. "
    "Line 57 Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Line 59 According To My Design struck dested I Have You Now. "
    "Ice-Heart dested Iceheart. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("All My Urchins & Cloud City Celebration", True),
    n("Keeping The Empire Out Forever"),
    n("Aayla Secura", True),
    n("Weapon Levitation", True),
    n("Sergeant Doallyn", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Chewbacca Of Kashyyyk", True),
    n("Luke With Lightsaber", True, qty=2),
    n("Caldera Righim", True),
    n("Han Solo, Innocent Scoundrel", True),
    n("Choke"),
    n("Kal'falnl C'ndros"),
    n("Landing Claw"),
    n("Pucumir Thryss"),
    n("Tanus Spijek", True),
    n("Lobot", True),
    n("Leia, Rebel Princess"),
    n("Sergeant Edian", True),
    n("Trooper Utris M'Toc", True),
    n("Uutik", True),
    n("Leslomy Tacema", True),
    n("Booster Terrik", True),
    n("Harc Seff", True),
    n("Kebyc", True),
    n("Yoxgit"),
    n("2-1B", True),
    n("Gas Tar Girls", True),
    n("Leesub Sirln", True),
    n("Overseer"),
    n("Choke"),
    n("Lady Luck", True),
    n("It's A Trap!", True),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Lower Corridor", True),
    n("Down With The Emperor!", True),
    n("Ellors Madak", True),
    n("Lando's Not A System, He's A Man"),
    n("Menace Fades"),
    n("Luke, Trust Me", True),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Rebel Barrier", qty=2),
    n("Path Of Least Resistance"),
    n("Path Of Least Resistance & Revealed"),
    n("Houjix & Out Of Nowhere"),
    n("Clash Of Sabers"),
    n("Rug Hug", True),
    n("Flash Of Insight", True),
    n("Dark Approach", True),
    n("Alter", True),
    n("Ounee Ta", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Aim High", True),
    n("Battle Plan", True),
    n("Do, Or Do Not", True),
    n("Wise Advice", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("There Is Another", True),
    n("It's A Trap!"),
]


DS_START = "No Money, No Parts, No Deal! / You're A Slave?"
DS_CARDS = [
    n("No Money, No Parts, No Deal! / You're A Slave?"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Mos Espa"),
    n("Prepared Defenses"),
    n("You Cannot Hide Forever"),
    n("Endor Shield"),
    n("Watto", True, qty=3),
    n("Darth Maul With Lightsaber", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Mara Jade With Lightsaber", True),
    n("Grand Admiral Thrawn", True),
    n("General Nevar"),
    n("Emperor Palpatine", True),
    n("Garindan"),
    n("J'Quille", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Velken Tezeri"),
    n("Jango Fett, The Assassin", True),
    n("Iceheart", True),
    n("Dr. Evazan & Ponda Baba", True),
    n("P-59"),
    n("Ket Maliss, Shadow Killer"),
    n("Executor", True),
    n("Executor"),
    n("Blizzard 4"),
    n("Jabba's Palace: Dungeon"),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("The Phantom Menace"),
    n("Search And Destroy"),
    n("Ability, Ability, Ability"),
    n("Special Delivery"),
    n("Ni Chuba Na?", True),
    n("Protocol Failure", True),
    n("Outflank"),
    n("Outflank", True),
    n("Imperial Barrier", True),
    n("Outflank", True),
    n("Imperial Command"),
    n("Imperial Command"),
    n("First Strike"),
    n("Masterful Move & Endor Occupation"),
    n("Imperial Barrier", qty=2),
    n("Wipe Them Out, All Of Them", True),
    n("Sith Fury & End This Destructive Conflict", True),
    n("Lightsaber Deficiency", True),
    n("He Hasn't Come Back Yet", True),
    n("Force Push", True),
    n("Imbalance & Kintan Strider", True),
    n("Ghhhk & Those Rebels Won't Escape Us", True),
    n("Limited Resources"),
    n("I Have You Now", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Battle Order", True),
    n("Death Star Sentry", True),
    n("After Her", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Resistance", True),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Abyss", True),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
]
