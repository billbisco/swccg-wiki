#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Roy Bordier.

Source: 2012mpcday1.pdf pages 51–52 (2010 form, 12 shields).
Name Roy Bordier dested Roy Bordier. Username Spectre.
p51 Light Profit. p52 Dark Bring Him Before Me.
Do not dest as a new person if a later analog identifies him.
"""
from __future__ import annotations

PLAYER = "Roy Bordier"
USERNAME = "Spectre"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 51
DS_PAGE = 52
LS_SCAN = "2012 Match Play Championship Day 1 Roy Bordier LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Roy Bordier DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Roy Bordier. Username Spectre. LIGHT checked. "
    "Event Date 02/11/12. Event Name MPC 2012. Deck Name blank. "
    "You Can Either Profit By This... dested You Can Either Profit By This... / Or Be Destroyed. "
    "Luke Skywalker, Strong in the Force dested Luke Skywalker, Strong In The Force True x4. "
    "Leia dested Leia True. Leia, Rebel Princess dested Leia, Rebel Princess. "
    "Captain Han dested Captain Han Solo. Naked Threepio dested Threepio With His Parts Showing. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Watto's Junkyard dested Tatooine: Watto's Junkyard. "
    "Strike Force dested Strikeforce True. SATM combo dested Sorry About The Mess & Blaster Proficiency. "
    "Rycar Ryjerd dested Rycar Ryjerd True. JP: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Han dested Han True. Only Jedi Lose Their Weapons dested Only Jedi Carry That Weapon. "
    "Form left 37–40 unique. Dittos inherit (V). Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Roy Bordier. Username Spectre. DARK checked. "
    "Event Date 2/11/12. Event Name MPC 2012. Deck Name blank. "
    "Bring Him Before Me dested Bring Him Before Me / Take Your Father's Place. "
    "Masterful Move / Endor Occ dested Masterful Move & Endor Occupation. "
    "He is not Ready / Propaganda dested He Is Not Ready & Imperial Propaganda (no combo (V) reprint). "
    "Imperial Scepter dested Imperial Scepter (no (V) reprint). Ghhhk dested Ghhhk. "
    "U-3PO dested U-3PO (U-3PO (V) would steal E-3PO). "
    "Boba Fett in Slave I dested Boba Fett In Slave I True. IT-O dested IT-O True. "
    "4-LOM / Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Kir Kanos (Force Pike) dested Kir Kanos With Force Pike True. "
    "Elis Helrot dested Elis Helrot True. Imperial Arrest Order / Secret Plans dested "
    "Imperial Arrest Order & Secret Plans. Battle Order / First Strike dested "
    "Battle Order & First Strike. Form left 37–40 unique. Dittos inherit (V). Unique 60. "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Luke Skywalker, Strong In The Force", True, qty=4),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Leia", True),
    n("Leia, Rebel Princess"),
    n("Padmé Naberrie", True),
    n("Captain Han Solo"),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Chewbacca, Protector"),
    n("Artoo-Detoo In Red 5"),
    n("Home One"),
    n("Obi-Wan's Journal"),
    n("Tatooine: Lars Moisture Farm", True, qty=2),
    n("Luke's Bionic Hand", True),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Obi-Wan's Lightsaber"),
    n("Home One: War Room"),
    n("Tatooine: Watto's Junkyard"),
    n("Lightsaber Proficiency"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True, qty=2),
    n("Scrambled Transmission", True),
    n("Strikeforce", True),
    n("Imperial Atrocity", True, qty=3),
    n("The Force Is Strong With This One"),
    n("Run Luke, Run!", qty=2),
    n("Weesa Gotta Grand Army", qty=2),
    n("Weapon Levitation"),
    n("Skywalkers"),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Nabrun Leids"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Hear Me Baby, Hold Together", True),
    n("I Must Be Allowed To Speak", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Heading For The Medical Frigate"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Sith Fury", True, qty=2),
    n("Projective Telepathy", qty=2),
    n("Imperial Barrier", qty=2),
    n("Control"),
    n("Alter"),
    n("Sense", qty=4),
    n("Trample"),
    n("Always Thinking With Your Stomach"),
    n("Force Lightning"),
    n("The Circle Is Now Complete"),
    n("Masterful Move & Endor Occupation"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Search And Destroy"),
    n("Lateral Damage"),
    n("Imperial Scepter"),
    n("IG-88 With Riot Gun"),
    n("Blizzard 4"),
    n("Arica", True),
    n("Ghhhk"),
    n("Emperor Palpatine", qty=2),
    n("U-3PO"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Jabba's Space Cruiser", True),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Executor"),
    n("Blizzard 2", True),
    n("Lord Vader", qty=3),
    n("General Veers", True),
    n("IT-O", True),
    n("4-LOM With Concussion Rifle"),
    n("Kir Kanos With Force Pike", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Elis Helrot", True),
    n("Prince Xizor"),
    n("Grand Admiral Thrawn"),
    n("Vader's Lightsaber", qty=2),
    n("Fondor"),
    n("Cloud City: East Platform"),
    n("Spaceport Docking Bay"),
    n("Death Star II: Docking Bay"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Establish Control", True),
    n("Battle Order & First Strike"),
    n("Prepared Defenses"),
    n("Death Star II: Throne Room"),
    n("Your Destiny"),
    n("Insignificant Rebellion"),
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("Imperial Detention", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
]
DS_ADD = []
