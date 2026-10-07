#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Joe Pinto Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Joe Pinto"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 71
DS_PAGE = 72
LS_SCAN = "2013 Match Play Championship p71 Joe Pinto LS.png"
DS_SCAN = "2013 Match Play Championship p72 Joe Pinto DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Joe Pinto. Light. Starting Plead My Case. "
    "Plead My Case dested Plead My Case To The Senate / Sanity And Compassion. "
    "Senate dested Coruscant: Galactic Senate. Heading for Medical dested Heading For The Medical Frigate. "
    "Bail Organa Father dested Bail Organa, Father Of Rebellion. K3P0 dested K-3PO (Kay-Threepio). "
    "Chew. Protector dested Chewbacca, Protector. Reb leadership dested Rebel Leadership. "
    "Cor. Night Club dested Coruscant: Night Club. So this is how lib. dies dested So This Is How Liberty Dies. "
    "Derek Hobbie dested Derek 'Hobbie' Klivian. H1 War Room dested Home One: War Room. "
    "Mace Windu MOTO dested Mace Windu, Master Of The Order. Yoda MOTO dested Yoda, Master Of The Force. "
    "Senator Padme Amid. dested Senator Padme Amidala. Found Someone you have/Combo dested Found Someone You Have & Higher Ground. "
    "Ald. Cons. Ship dested Alderaan Consular Ship. Senate Hover cam dested Senate Hovercam. "
    "Might of Rep. dested Might Of The Republic. Mag. Haash'n dested Major Haash'n. "
    "Jedi Council Cham. dested Coruscant: Jedi Council Chamber. Screaming Lando dested Lando Calrissian, Scoundrel. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Hear me Baby dested Hear Me Baby, Hold Together. "
    "EL-19 dested Incom T-16 Skyhopper. Dressel dested Dressel. Emp. Atrocity dested Imperial Atrocity. "
    "Coruscant. ep1 dested Coruscant. Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Tycho dested Tycho Celchu. General Solo dested General Solo. Tantive dested Tantive IV. "
    "Senator Leia Organe dested Senator Leia Organa. 1st Officer Thaneespi dested First Officer Thaneespi. "
    "The Prof. dested The Professor. Let's keep a little opt. dested Let's Keep A Little Optimism Here. "
    "Simple Tricks dested Simple Tricks And Nonsense. A Tragedy dested A Tragedy Has Occurred. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Joe Pinto. Dark. Deck title The Responsibility of Command. "
    "CCT dested Carbon Chamber Testing / My Favorite Decoration. Knowledge & D dested Knowledge And Defense. "
    "Jabba's Prize as written. GA Thrawn dested Grand Admiral Thrawn. Dr. E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Emp. Propaganda dested Imperial Propaganda. Weapon Lev dested Weapon Levitation. Emp Artillery dested Imperial Artillery. "
    "Maul w/ Saber dested Darth Maul With Lightsaber. DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "P o t F dested Presence Of The Force. Lightsaber Def. dested Lightsaber Deficiency. "
    "Mara Jade w/ Saber dested Mara Jade With Lightsaber. We must accel dested We Must Accelerate Our Plans. "
    "Slave I Symbol dested Slave I, Symbol Of Fear. Control / Set For Stun dested Control & Set For Stun. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. Battle Droid Squad dested Battle Droid Squad. "
    "Hoth Echo Com. Center dested Hoth: Echo Command Center (War Room). Cloud City Sec. Tower dested Cloud City: Security Tower. "
    "Jabba's Palace Dungeon dested Jabba's Palace: Dungeon. JP Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "CC Carbonite Chamber dested Cloud City: Carbonite Chamber. Blockade Bridge dested Blockade Flagship: Bridge. "
    "IG 88 Neural Inhibitor dested IG-88's Neural Inhibitor. FG-88 dested IG-88. "
    "Mandalorian Father dested Jango Fett, The Assassin. Boba Fett Prepared dested Boba Fett, Prepared Hunter. "
    "Image of DL dested Image Of The Dark Lord. Emp. Barrier dested Imperial Barrier. "
    "4-lom w/ Conc. Rifle dested 4-LOM With Concussion Rifle. The Emperor dested Emperor Palpatine. "
    "Where you taking this thing dested Where Are You Taking This ... Thing?. "
    "CHYBC dested Come Here You Big Coward. Useless Gesture dested A Useless Gesture. "
    "You Cannot Hide Forever as written. Do they have a code dested Do They Have A Code Clearance?. "
    "Abyssin in the shield box dested Abyssin Ornament. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Anger, Fear, Aggression", True),
    n("Coruscant: Galactic Senate"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Rogue Squadron Tactics"),
    n("Strike Planning"),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Bail Organa"),
    n("K-3PO (Kay-Threepio)", True),
    n("Chewbacca, Protector", True),
    n("Chewbacca, Protector"),
    n("Sense"),
    n("Rebel Leadership", True, qty=2),
    n("Coruscant: Night Club"),
    n("Field Dressing"),
    n("So This Is How Liberty Dies"),
    n("Derek 'Hobbie' Klivian", True),
    n("Home One: War Room"),
    n("Mas Amedda"),
    n("Mace Windu, Master Of The Order"),
    n("Senator Padme Amidala"),
    n("Found Someone You Have & Higher Ground"),
    n("Yoda, Master Of The Force"),
    n("Alderaan Consular Ship"),
    n("Senate Hovercam"),
    n("Might Of The Republic", qty=3),
    n("Major Haash'n"),
    n("Home One"),
    n("Coruscant: Jedi Council Chamber"),
    n("Jedi Presence"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Houjix"),
    n("Menace Fades"),
    n("Escape Pod", True),
    n("Seeking An Audience", True),
    n("Hear Me Baby, Hold Together", True),
    n("Incom T-16 Skyhopper"),
    n("Dressel"),
    n("Luke Skywalker", True),
    n("Imperial Atrocity", True),
    n("Coruscant"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Senator Mon Mothma"),
    n("Tycho Celchu", True),
    n("General Solo", True),
    n("Obi-Wan Kenobi", True),
    n("Tantive IV", True),
    n("Senator Leia Organa"),
    n("First Officer Thaneespi"),
    n("Grimtaash"),
]
LS_SHIELDS = [
    n("Aim High", True),
    n("Another Pathetic Lifeform", True),
    n("Wise Advice", True),
    n("The Professor"),
    n("Let's Keep A Little Optimism Here"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("Battle Plan", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Yavin Sentry"),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Knowledge And Defense", True),
    n("Jabba's Prize"),
    n("Grand Admiral Thrawn"),
    n("Much Anger In Him"),
    n("Dr. Evazan & Ponda Baba"),
    n("Imperial Propaganda", True, qty=2),
    n("Weapon Levitation"),
    n("Protocol Failure"),
    n("Imperial Artillery"),
    n("Sneak Attack", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Victory"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Any Methods Necessary"),
    n("Operational As Planned", True),
    n("Carbonite Chamber Console", True),
    n("Responsibility Of Command"),
    n("Despair", True),
    n("Something Special Planned For Them", True),
    n("Zuckuss In Mist Hunter"),
    n("Presence Of The Force"),
    n("Force Lightning", qty=2),
    n("Lightsaber Deficiency", True),
    n("Mara Jade With Lightsaber"),
    n("We Must Accelerate Our Plans"),
    n("No Escape"),
    n("Sense"),
    n("Stunning Leader"),
    n("Slave I, Symbol Of Fear"),
    n("Control & Set For Stun"),
    n("Why Didn't You Tell Me", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Defensive Fire", True),
    n("Battle Droid Squad"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Palace: Dungeon"),
    n("Jabba's Palace: Audience Chamber"),
    n("Cloud City: Carbonite Chamber"),
    n("Blockade Flagship: Bridge"),
    n("Cold Feet", True),
    n("IG-88's Neural Inhibitor", True),
    n("IG-88", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Image Of The Dark Lord", True),
    n("Imperial Barrier"),
    n("4-LOM With Concussion Rifle", True),
    n("Emperor Palpatine", True, qty=2),
    n("Sith Fury", True),
    n("Surprise"),
    n("Where Are You Taking This ... Thing?"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Abyssin Ornament", True),
    n("Come Here You Big Coward", True),
    n("Resistance"),
    n("Secret Plans", True),
    n("Fanfare", True),
    n("Battle Order", True),
    n("Allegations Of Corruption", True),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement", True),
]
DS_ADD = []
