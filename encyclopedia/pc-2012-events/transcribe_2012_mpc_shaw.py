#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Greg Shaw.

Source: 2012mpcday1.pdf pages 13–14 (2010 form, 12 shields).
Name Greg Shaw Dark / Greg Shaw Light dested Greg Shaw. Username blank.
Both LIGHT/DARK empty dested from the 60s.
p13 Dark A Stunning Move. p14 Light Communing.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2012 Match Play Championship Day 1 Greg Shaw LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Shaw dested Greg Shaw. Username blank. "
    "LIGHT/DARK empty dested Light from Communing 60. Deck Name empty. "
    "Communing dested Communing. Slave Quart dested Tatooine: Slave Quarters. "
    "Anger Fear dested Anger, Fear, Aggression. Master Kenobi dested Master Kenobi. "
    "Commando Training Combo dested Commando Training & K'lor'slug. "
    "Obi's Hut dested Tatooine: Obi-Wan's Hut. H1 WR dested Home One: War Room. "
    "Cantina dested Tatooine: Cantina. Tatooine ep1 dested Tatooine (Coruscant). "
    "Luke's Gun dested Luke's Blaster Pistol. Chew Bowcaster dested Chewbacca's Bowcaster. "
    "Honor dested Honor Of The Jedi. Gunganner dested Gunganator. "
    "R2 in R5 dested Artoo-Detoo In Red 5. Home 1 dested Home One. "
    "Run Luke Run dested Run Luke, Run!. The Force Is Strong dested The Force Is Strong With This One. "
    "Bith Shuffle Combo dested The Bith Shuffle & Desperate Reach. "
    "Use the Force form 33 True and form 34 empty kept separate. "
    "Let The Wookiee Win form 35 True and form 36 empty kept separate. "
    "Slight Weapon Malfunction dested Slight Weapons Malfunction. "
    "Hear me Baby dested Hear Me Baby, Hold Together. "
    "Antilles Maneuver Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "OOC combo dested Out Of Commission & Transmission Terminated. "
    "Ring Thing dested as written. Vetrack dested Captain Verrack. "
    "Chewie Enraged dested Chewie, Enraged "
    "(form 47 True, form 54 empty, form 55 True kept separate). "
    "Luke Skywalker, Rebel dested Luke Skywalker, Rebel Scout. "
    "Leia RP dested Leia, Rebel Princess. Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Naked 3PO dested Threepio With His Parts Showing. "
    "COX V dested Corran Horn True; form 59 Corran empty kept separate. "
    "Yoda GW dested Yoda, Great Warrior. Ackbar dested Admiral Ackbar. "
    "Shmi dested Shmi Skywalker. Simple Tricks dested Simple Tricks And Nonsense. "
    "Insight dested Your Insight Serves You Well. Optimism dested Let's Keep A Little Optimism Here. "
    "Pathetic Lifeform dested Another Pathetic Lifeform. DDTA dested Don't Do That Again. "
    "Additional The Professor crossed, skipped. "
    "Unique overcounts sheet-accurate (Artoo-Detoo In Red 5 x2, Run Luke, Run! x2, "
    "Rebel Leadership x3, Escape Pod x2, The Bith Shuffle & Desperate Reach x2, Houjix x2, "
    "Wookiee Roar x2, Chewie, Enraged x3, Luke Skywalker, Rebel Scout x3, Corran Horn x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Shaw dested Greg Shaw. Username blank. "
    "LIGHT/DARK empty dested Dark from A Stunning Move 60. Deck Name empty. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage. "
    "Cor: Private Platform dested Coruscant: Private Platform. "
    "Cor: Nightclub dested Coruscant: Night Club. "
    "Gift of Master dested Gift Of The Master. Ni Chuba Na dested Ni Chuba Na??. "
    "3Z70 41 dested 3,720 To 1. Elis in Unction dested Elis Helrot. "
    "Cyborg's Lightsabers dested Grievous' Lightsabers. "
    "Galen's Saber Gift dested Galen's Lightsaber, Vader's Gift. "
    "Maul's Double Saber dested Maul's Double-Bladed Lightsaber. "
    "BF Bridge dested Blockade Flagship: Bridge. BF DB dested Blockade Flagship: Docking Bay. "
    "BF Hallway dested Blockade Flagship: Hallway. Oh Switch Off dested Oh, Switch Off. "
    "Maul Strikes dested Maul Strikes. Force Field form 21 empty and form 22 True kept separate. "
    "Sniper Dark Strike dested Sniper & Dark Strike. "
    "A Dark Time For Reb dested A Dark Time For The Rebellion. "
    "Self Destruct Mechanism dested Self-Destruct Mechanism. "
    "Masterful Move dested Masterful Move. "
    "Weapon Lev Combo dested Weapon Levitation & The Empire's Back. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "Darth Maul YA dested Darth Maul, Young Apprentice. "
    "Dr E PB dested Dr. Evazan & Ponda Baba. "
    "Galen Apprentice dested Galen, Secret Apprentice. "
    "IG Bodyguard dested IG-100 MagnaGuard. P59 dested P-59. P60 dested P-60. "
    "Ability x3 dested Ability, Ability, Ability. "
    "Where are you taking dested Where Are You Taking This ... Thing?. "
    "Wipe Them Out dested Wipe Them Out, All Of Them. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "YCHTF dested You Cannot Hide Forever. We'll Let Fate dested We'll Let Fate-a Decide, Huh?. "
    "Unique overcounts sheet-accurate (Oh, Switch Off x2, Force Field x2, "
    "A Dark Time For The Rebellion x2, Battle Droid Squad x3, Grievous, Hunter Of Jedi x2, "
    "Darth Maul, Young Apprentice x3, Galen, Secret Apprentice x3, IG-100 MagnaGuard x3, "
    "The Phantom Menace x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Master Kenobi"),
    n("Communing"),
    n("Commando Training & K'lor'slug"),
    n("Wokling", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Tatooine: Cantina"),
    n("Tatooine (Coruscant)"),
    n("Luke's Blaster Pistol", True),
    n("Chewbacca's Bowcaster"),
    n("Honor Of The Jedi"),
    n("Draw Their Fire"),
    n("Hindsight", True),
    n("Gunganator", True),
    n("Launching The Assault"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Run Luke, Run!", True, qty=2),
    n("The Force Is Strong With This One"),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Houjix", qty=2),
    n("Use The Force", True),
    n("Use The Force"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Jedi Levitation", True),
    n("Slight Weapons Malfunction", True),
    n("Hear Me Baby, Hold Together", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Wookiee Roar", True, qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Sabotage", True),
    n("Ring Thing"),
    n("Captain Verrack"),
    n("Chewie, Enraged", True),
    n("Luke Skywalker, Rebel Scout", True, qty=3),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Threepio With His Parts Showing"),
    n("Chewie, Enraged"),
    n("Chewie, Enraged", True),
    n("Corran Horn", True),
    n("Yoda, Great Warrior", True),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Shmi Skywalker"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Another Pathetic Lifeform", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Coruscant: Night Club"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("3,720 To 1", True),
    n("Elis Helrot"),
    n("Victory"),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Oh, Switch Off", qty=2),
    n("Maul Strikes"),
    n("Ghhhk"),
    n("Force Field"),
    n("Force Field", True),
    n("Operational As Planned", True),
    n("Force Push", True),
    n("Sniper & Dark Strike"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Self-Destruct Mechanism"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Masterful Move"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Battle Droid Squad", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Galen, Secret Apprentice", qty=3),
    n("IG-100 MagnaGuard", qty=3),
    n("P-59"),
    n("P-60"),
    n("A Sith's Weapon"),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Forced Servitude"),
    n("No Escape"),
    n("Tarkin's Bounty", True),
    n("The Phantom Menace", qty=2),
    n("Where Are You Taking This ... Thing?"),
    n("Wipe Them Out, All Of Them", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
