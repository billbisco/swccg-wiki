#!/usr/bin/env python3
"""2013 World Championship Day 2: Mitch Wieland Xerox QMC + NMNPND."""
from __future__ import annotations

PLAYER = "Mitch Wieland"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 70
DS_PAGE = 71
LS_SCAN = "2013 Worlds Day 2 p70 Mitch Wieland LS.png"
DS_SCAN = "2013 Worlds Day 2 p71 Mitch Wieland DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields). Mitch Wieland. Username blank. "
    "Deck title 24 Characters and a Bitch ain't one. LIGHT. "
    "Quiet Mining Colony dested Quiet Mining Colony / Independent Operation. "
    "All my Urchins : Cloud City Celebration dested All My Urchins & Cloud City Celebration. "
    "Ellors Madak dested Ellorrs Madak. Houjix : out of Nowhere dested Houjix & Out Of Nowhere. "
    "Kebyc dested Kebyc. Leesub Sirln dested Leesub Sirln. "
    "Path of least resistance : Revealed dested Path Of Least Resistance & Revealed. "
    "Rug Hug dested Rug Hug. Chewbacca- Walking Carpet dested Chewbacca, Walking Carpet. "
    "Harc Seff dested Harc Seff. Yoxgit dested Yoxgit. "
    "Lando's not a system, He is a man dested Lando's Not A System, He's A Man. "
    "Down with the Emperor dested Down With The Emperor!. "
    "It could be worse written over struck dested It Could Be Worse. "
    "Aayla Secura x3, Lando Calrissian Unlikely Hero x2, Imperial Atrocity x2, "
    "and Rug Hug x2 left sheet-accurate. "
    "Shield 11 Planetary Occupation struck; Weapons Display dested Weapons Display. "
    "Additional Simple Tricks And Nonsense and He Can Go About His Business moved to Light shields. "
    "Jabba's Prize kept as extra Character. "
    "Form left column reprints 37-38 on lines 39-40 are Luke With Lightsaber and Rug Hug. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Mitch Wieland. Username blank. "
    "Deck title That Deck is SO STUPID. DARK. "
    "No Money, No Parts, No Deal dested No Money, No Parts, No Deal! / You're A Slave?. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Tatooine JP: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Darth Maul w/ saber dittos dested Darth Maul With Lightsaber x4. "
    "Darth Vader with lightsaber dittos dested Darth Vader With Lightsaber x3. "
    "J'quille dested J'Quille. P-59 dested P-59. "
    "42-AS dested IG-88. "
    "The Mandalorian, Father of Fett dested The Mandalorian. "
    "Lukesir Dragus dested Lord Sidious. "
    "Sniper : Dark Strike dested Sniper & Dark Strike. "
    "Ghhhk : Those rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "You Are Beaten written over struck dested You Are Beaten. "
    "Lightsaber Deficiency dittos dested Lightsaber Deficiency x3. "
    "Outflank x4 left sheet-accurate. "
    "Sense written over struck dested Sense. "
    "We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Your Ship? dested Your Ship?. "
    "Additional Allegations Of Corruption, Come Here You Big Coward, and Fanfare "
    "moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Imperial Barrier / Imperial Command. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Rebel Barrier"),
    n("Ellorrs Madak", True),
    n("Houjix & Out Of Nowhere"),
    n("Leslomy Tacema", True),
    n("Aayla Secura"),
    n("Sergeant Edian", True),
    n("Menace Fades"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Path Of Least Resistance"),
    n("Lady Luck"),
    n("Melas", True),
    n("Aayla Secura"),
    n("Kal'falnl C'ndros"),
    n("2-1B", True),
    n("Down With The Emperor!", True),
    n("Kebyc", True),
    n("Leesub Sirln", True),
    n("Lando's Not A System, He's A Man"),
    n("Path Of Least Resistance & Revealed"),
    n("Desperate Reach", True),
    n("Rug Hug", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Luke With Lightsaber"),
    n("Chewbacca, Walking Carpet"),
    n("Rebel Barrier"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Overseer"),
    n("Harc Seff", True),
    n("Imperial Atrocity", True),
    n("Luke With Lightsaber"),
    n("Rug Hug", True),
    n("Trooper Utris M'Toc", True),
    n("Aayla Secura"),
    n("Pucumir Thryss"),
    n("Tanus Spijek", True),
    n("Leia, Rebel Princess"),
    n("Yoxgit"),
    n("Caldera Righim"),
    n("Landing Claw"),
    n("Jar Jar Binks"),
    n("Bacta Tank"),
    n("Choke"),
    n("It Could Be Worse"),
    n("Dark Approach", True),
    n("Flash Of Insight", True),
    n("Choke"),
    n("Weapon Levitation"),
    n("Alter"),
    n("No Questions Asked"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Don't Do That Again"),
    n("Aim High"),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
    n("Ultimatum"),
    n("There Is Another"),
    n("Weapons Display"),
    n("The Professor"),
    n("Simple Tricks And Nonsense"),
    n("He Can Go About His Business"),
]
LS_ADD = [
    n("Jabba's Prize"),
]


DS_START = "No Money, No Parts, No Deal! / You're A Slave?"
DS_CARDS = [
    n("No Money, No Parts, No Deal! / You're A Slave?"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Mos Espa"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("You Cannot Hide Forever"),
    n("Endor Shield", True),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Darth Maul With Lightsaber", qty=4),
    n("Darth Vader With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Darth Sidious"),
    n("Emperor Palpatine"),
    n("Admiral Ozzel"),
    n("General Nevar"),
    n("Velken Tezeri", True),
    n("Ket Maliss, Shadow Killer"),
    n("J'Quille", True),
    n("P-59"),
    n("Watto", True, qty=3),
    n("IG-88", True),
    n("The Mandalorian"),
    n("Executor", qty=2),
    n("Sniper & Dark Strike"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lord Sidious", True),
    n("Imperial Barrier", qty=2),
    n("Imperial Command", qty=2),
    n("You Are Beaten", True),
    n("Limited Resources"),
    n("I Have You Now", qty=2),
    n("Lightsaber Deficiency", True, qty=3),
    n("Outflank", True, qty=4),
    n("Search And Destroy"),
    n("Sense", True),
    n("Special Delivery", True),
    n("First Strike"),
    n("Crossfire", True),
    n("Protocol Failure"),
    n("Wipe Them Out, All Of Them", True),
    n("The Phantom Menace"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Your Ship?", True),
    n("After Her", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Imperial Detention"),
    n("Firepower"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
]
DS_ADD = []
