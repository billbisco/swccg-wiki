#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Alex W.

Source: MPC-2014-Day-1-Main-Event.pdf pages 118–119 (2013 form).
Name Alex W dested as written. Email [redacted].
"""
from __future__ import annotations

PLAYER = "Alex W"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 119
DS_PAGE = 118
LS_SCAN = "2014 Match Play Championship Day 1 Alex W LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Alex W DS.png"
LS_DECK_NAME = "Diet Dining Colony"
DS_DECK_NAME = "Droids gone Wild"
NOTE = "Light typed 2013 Xerox; Dark handwritten 2013 Xerox."
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Typed 2013 Xerox. Name Alex W dested as written. Email [redacted]. LIGHT checked. "
    "Deck name Diet Dining Colony. Quiet Mining Colony / Independent Operation dested "
    "Quiet Mining Colony / Independent Operation. Ellors Madak dested Ellor's Madak (V). "
    "Choke dested Choke. Path of Least Resistance & Revealed dested Path Of Least Resistance & Recovered. "
    "Shield 13 Chasm handwritten. Unique overcounts sheet-accurate (Aayla Secura x2, "
    "Luke With Lightsaber x2, Rebel Barrier x2, Houjix & Out Of Nowhere (V) x2). NO_DEST Path Of Least Resistance & Recovered. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Alex W dested as written. DARK 60. Deck name Droids gone Wild. "
    "Invasion / In Complete Control dested Invasion / In Complete Control. "
    "Where are Those Droidekas dested Where Are Those Droidekas?!. "
    "Destroyer Droid replaces Disarmed. P-59 dested P-59. Unique overcounts sheet-accurate "
    "(Maul's Sith Infiltrator x2, Operational As Planned (V) x2, Master Destroyers x2, "
    "Oh, Switch Off x2, Self-Destruct Mechanism x2, Rolling, Rolling, Rolling x2, "
    "Darth Maul x2, P-60 x2, P-59 x2, Destroyer Droid x6, Why Didn't You Tell Me? (V) x2, "
    "Those Rebels Won't Escape Us (V) x2). 14 shields, line 15 empty. NO_DEST Master Destroyers. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Guest Quarters"),
    n("Cloud City: West Gallery"),
    n("Bespin"),
    n("Errant Venture"),
    n("Overseer"),
    n("Lady Luck"),
    n("Guardian's Lightsaber"),
    n("No Questions Asked"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Kebyc", True),
    n("Yoxgit"),
    n("Caldera Righim"),
    n("Kal'Falnl C'ndros"),
    n("Chewbacca, Walking Carpet"),
    n("Harc Seff", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Leesub Sirln", True),
    n("Leslomy Tacema", True),
    n("Uutik", True),
    n("Aayla Secura", qty=2),
    n("Trooper Utris M'Toc", True),
    n("Tanus Spijek", True),
    n("Sergeant Edian", True),
    n("Mirax Terrik"),
    n("Melas", True),
    n("Foul Moudama"),
    n("2-1B", True),
    n("R-3PO", True),
    n("Luke With Lightsaber", qty=2),
    n("Landing Claw"),
    n("Draw Their Fire"),
    n("Beldon's Eye", True),
    n("Menace Fades"),
    n("Keeping The Empire Out Forever"),
    n("Seeking An Audience", True),
    n("Ellor's Madak", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Redeemed Apprentice"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
    n("Rug Hug", True),
    n("Blast The Door, Kid!"),
    n("Choke"),
    n("Path Of Least Resistance & Recovered"),
    n("Path Of Least Resistance"),
    n("Rebel Barrier", qty=2),
    n("Desperate Reach", True),
    n("Dark Approach", True),
    n("Inconsequential Barriers"),
    n("Houjix & Out Of Nowhere", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Heading For The Medical Frigate", True),
    n("Alter", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("Traffic Control", True),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice", True),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Blockade Flagship", True),
    n("Naboo: Swamp"),
    n("Naboo"),
    n("Where Are Those Droidekas?!", True),
    n("At Last We Are Getting Results", True),
    n("Droid Racks", True),
    n("Prepared Defenses", True),
    n("Stinger", True),
    n("Maul's Sith Infiltrator", qty=2),
    n("Blockade Support Ship"),
    n("Naboo: Battle Plains"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Generator"),
    n("Operational As Planned", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Elis Helrot"),
    n("Destroyer Droid"),
    n("Stunning Leader"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Master Destroyers", qty=2),
    n("First Strike"),
    n("Outflank", True),
    n("Oh, Switch Off", qty=2),
    n("Self-Destruct Mechanism", qty=2),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Imperial Barrier"),
    n("Combat Response"),
    n("Search And Destroy"),
    n("4-LOM With Concussion Rifle"),
    n("Guri"),
    n("Darth Maul", qty=2),
    n("Daultay Dofine", True),
    n("Tey How"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("P-60", qty=2),
    n("P-13 & P-14"),
    n("P-59", qty=2),
    n("Destroyer Droid", qty=6),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Force Push", True),
    n("Those Rebels Won't Escape Us", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Abyss"),
    n("You Cannot Hide Forever"),
    n("A Useless Gesture"),
    n("Fanfare"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing"),
]
DS_ADD = []
