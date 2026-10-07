#!/usr/bin/env python3
"""2013 World Championship Day 2: Thomas Whaley Senate + Hunt Down."""
from __future__ import annotations

PLAYER = "Thomas Whaley"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 115
DS_PAGE = 116
LS_SCAN = "2013 Worlds Day 2 p115 Thomas Whaley LS.png"
DS_SCAN = "2013 Worlds Day 2 p116 Thomas Whaley DS.png"
LS_NOTE = (
    "Handwritten 2009 Xerox Print Form (uniqueness dots, 12 shields). "
    "Name Thomas Whaley. Username blank. Email blank. LIGHT. "
    "Dated 8/10/13. Deck title Luke's Hope. Event Day 2. "
    "Plead My Case To The Senate dested Plead My Case To The Senate / Sanity And Compassion. "
    "Coruscant: Senate dested Coruscant: Galactic Senate. "
    "Yuk Yub, Commander dested Yub Yub, Commander. "
    "Lt. Blount dested Lieutenant Blount. "
    "Biggs RL dested Biggs Darklighter. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Oack Raider dested Palace Raider. "
    "Capt. Yutani with Gun dested Captain Yutani With Blaster Cannon. "
    "Senator Mothma dested Senator Mon Mothma. "
    "Senator Leia Organa dested Senator Leia Organa. "
    "Threepio WIPS dested Threepio With His Parts Showing. "
    "Col. Cracken dested Colonel Cracken. "
    "Odin Nesloor First Aid dested Odin Nesloor & First Aid. "
    "Hobbie dested Derek 'Hobbie' Klivian. "
    "Out Of Commission & TT dested Out Of Commission & Transmission Terminated. "
    "Antilles Maneuver & RR dested Antilles Maneuver & Rebel Reinforcements. "
    "Form left column reprints 37-38 on lines 39-40 are Lady Luck and Home One. "
    "Senator Padme Amidala / Might Of The Republic / Rebel Leadership / "
    "Escape Pod / Bail Organa / Out Of Commission unique overcounts kept sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2009 Xerox Print Form (uniqueness dots, 12 shields). "
    "Name Thomas Whaley. Username blank. Email blank. DARK. "
    "Dated 8/10/13. Deck title Luke's Love Bone. Event Day 2. "
    "Hunt Down And Destroy The Jedi dested Hunt Down And Destroy The Jedi (V) / "
    "Their Fire Has Gone Out Of The Universe (V). "
    "A Sith's Plan dested A Sith's Plans. "
    "Vader's Limbs dested Vader's Bionic Limbs. "
    "Imperial Arrest Order & Secret Plans dested Imperial Arrest Order & Secret Plans. "
    "Coruscant: Sub City Lair dested Coruscant: Sub City Lair. "
    "Galen Marek dested Galen Marek, Starkiller. "
    "Galen's Lightsaber, VG dested Galen's Lightsaber, Vader's Gift. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. "
    "Slave I, SOF dested Slave I, Symbol Of Fear. "
    "Juno Eclipse dested Juno Eclipse, Black Leader. "
    "The Mandalorian, FOF dested Jango Fett, The Assassin. "
    "Darth Vader, Dark Lord dested Darth Vader, Dark Lord Of The Sith. "
    "Sith Fury combo dested Sith Fury & End This Destructive Conflict. "
    "Weapon Levitation & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Luvlse dested Sense. "
    "Sniper & DS dested Sniper & Dark Strike. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "4-LOM with concussion rifle dested 4-LOM With Concussion Rifle. "
    "Form left column reprints 37-38 on lines 39-40 are Trophy Of A Kill and "
    "Weapon Levitation & The Empire's Back. "
    "Shield 8 Secret Plans struck; Battle Order kept. "
    "Galen Marek / Darth Vader / Arica / Trophy / Weapon Levitation combo / "
    "Sith Fury combo / Sonic Bombardment / Force Field / Unsalvageable unique "
    "overcounts kept sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Strike Planning"),
    n("Wokling", True),
    n("Insurrection"),
    n("K'lor'slug", True),
    n("Senator Padme Amidala", qty=2),
    n("Senate Hovercam"),
    n("Corran Horn"),
    n("Might Of The Republic", qty=2),
    n("Yub Yub, Commander", True),
    n("Lieutenant Blount", True),
    n("Biggs Darklighter", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Palace Raider", True),
    n("Yoda", True),
    n("Chewbacca, Protector", True),
    n("Owen Lars & Beru Lars"),
    n("Admiral Ackbar", True),
    n("Captain Yutani With Blaster Cannon", True),
    n("Bail Organa", True, qty=2),
    n("Senator Mon Mothma", True),
    n("Senator Leia Organa", True),
    n("Naboo: Theed Palace Generator"),
    n("Threepio With His Parts Showing"),
    n("Home One: War Room"),
    n("Coruscant: Night Club", True),
    n("So This Is How Liberty Dies", True),
    n("Field Dressing", True),
    n("Colonel Cracken"),
    n("Honor Of The Jedi"),
    n("Odin Nesloor & First Aid", True),
    n("Escape Pod", True, qty=2),
    n("Lando Calrissian, Scoundrel", True),
    n("Lady Luck", True),
    n("Home One"),
    n("Tycho Celchu", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Free Ride & Endor Celebration"),
    n("Rebel Leadership", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Tantive IV", True),
    n("Commander Narra", True),
    n("Luke Skywalker", True),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Obi-Wan In Radiant VII", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Bright Hope", True),
    n("Double Agent"),
    n("Jedi Presence"),
    n("Rahm Kota, Blind Jedi", True),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("Aim High"),
    n("A Tragedy Has Occurred", True),
    n("Ultimatum", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("A Sith's Plans", True),
    n("Rise Of The Dark Lord", True),
    n("Vader's Helmet", True),
    n("Vader's Bionic Limbs", True),
    n("Vader's Cape"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Gift Of The Master", True),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Sub City Lair", True),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Boba Fett, Prepared Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Arica", True, qty=2),
    n("Mara Jade's Lightsaber", True),
    n("Rogue Shadow", True),
    n("Juno Eclipse, Black Leader", True),
    n("Jango Fett, The Assassin", True),
    n("Darth Vader, Dark Lord Of The Sith", True, qty=3),
    n("Vader's Lightsaber"),
    n("Stop Motion", True),
    n("Sith Fury & End This Destructive Conflict", True, qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Unsalvageable", qty=2),
    n("Trophy Of A Kill", True, qty=2),
    n("Weapon Levitation & The Empire's Back", True, qty=2),
    n("Cold Feet", True),
    n("Sense", True),
    n("Force Field", True, qty=2),
    n("Always Thinking With Your Stomach"),
    n("Force Push", True),
    n("Force Lightning"),
    n("Sniper & Dark Strike"),
    n("One Beautiful Thing", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("4-LOM With Concussion Rifle", True),
    n("No Escape"),
    n("Ability, Ability, Ability", True),
    n("Drop!"),
    n("Blast Door Controls"),
    n("Blaster Rack", True),
    n("First Strike"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("There Is No Try", True),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Reactor Terminal", True),
]
DS_ADD = []
