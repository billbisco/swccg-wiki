#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Greg Shaw.

Source: 2012mpcday2.pdf pages 3–4 (2010 form, 12 shields).
Name GREG SHAW dested Greg Shaw. Username blank.
p03 Dark A Stunning Move. p04 Light Communing.
Do not dest as a new person. Do not rewrite 2013 leftovers.
Do not rewrite Day 1 leftover A Stunning Move / Communing.
Pack player-stubs/Greg_Shaw.wiki.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2012 Match Play Championship Day 2 Greg Shaw LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name GREG SHAW dested Greg Shaw. Username blank. "
    "Event MPC Day 2. Deck Name empty. LIGHT. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover Communing. "
    "Communing dested Communing analog leftover Shaw IN THE 60 AND START. "
    "Slave Quarters dested Tatooine: Slave Quarters analog leftover Shaw. "
    "Anger Fear Aggro True dested Anger, Fear, Aggression True analog leftover Shaw. "
    "Commando Training & Klorslug dested Commando Training & K'lor'slug analog leftover Shaw. "
    "Obi's Hut True dested Tatooine: Obi-Wan's Hut True analog leftover Shaw. "
    "Tatooine (ep1) dested Tatooine (Coruscant) analog leftover Shaw. "
    "Home One War Room dested Home One: War Room analog leftover Shaw. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Shaw. "
    "Luke Rebel Hero dested Luke Skywalker, Rebel Scout analog leftover Shaw. "
    "Chewie Enraged True dested Chewie, Enraged True analog leftover Shaw. "
    "Chewbacca of Kashyyyk True dested Chewbacca Of Kashyyyk True analog leftover. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Shaw. "
    "Lando Scoundrel True dested Lando Calrissian, Scoundrel True analog leftover Shaw. "
    "Threepio with his parts dested Threepio With His Parts Showing analog leftover Shaw. "
    "Chewbacca's Revenge dested as written. "
    "Luke's Blaster True dested Luke's Blaster Pistol True analog leftover Shaw. "
    "Rebel Gunrunner dested analog leftover Anderson. "
    "Lets Keep Optimism True dested Let's Keep A Little Optimism Here True analog leftover Shaw IN THE 60. "
    "Grimtaash dested Grimtaash analog leftover TMW Shaw. "
    "Hear Me Baby True dested Hear Me Baby, Hold Together True analog leftover Shaw. "
    "Slight Weapons Malfunction dested analog leftover Shaw. "
    "The Force Is Strong With This dested The Force Is Strong With This One analog leftover Shaw. "
    "Run Luke empty AND Run Luke Run True kept separate analog leftover Shaw. "
    "OOC & TT dested Out Of Commission & Transmission Terminated analog leftover Shaw. "
    "The Bith Shuffle & Desp Reach dested The Bith Shuffle & Desperate Reach analog leftover Shaw. "
    "Antilles Maneuver & RR dested Antilles Maneuver & Rebel Reinforcements analog leftover Shaw. "
    "Shield Another Lifeform True dested Another Pathetic Lifeform True analog leftover Shaw. "
    "Shield Your Insight True dested Your Insight Serves You Well True analog leftover Shaw. "
    "Shield A Tragedy dested A Tragedy Has Occurred analog leftover Shaw. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense analog leftover Shaw. "
    "Unique overcounts sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name GREG SHAW dested Greg Shaw. Username blank. "
    "Event MPC Day 2. Deck Name empty. DARK. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover A Stunning Move. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage analog leftover Shaw IN THE 60 AND START. "
    "Coruscant: Private Platform dested analog leftover Shaw. "
    "Coruscant: Palpatine's Quarters dested analog leftover Anderson. "
    "3720 to 1 True dested 3,720 To 1 True analog leftover Shaw. "
    "Ni Chuba Na True dested Ni Chuba Na?? True analog leftover Shaw. "
    "Prepared Defenses True dested Prepared Defenses True analog leftover Foth IN THE 60. "
    "Knowledge And Defense True dested Knowledge And Defense True analog leftover Murray IN THE 60. "
    "BF Bridge/Hallway/Docking Bay dested Blockade Flagship analog leftover Shaw. "
    "Darth Maul, Young Apprentice dested analog leftover Shaw. "
    "Galen Secret Appr dested Galen, Secret Apprentice analog leftover Shaw. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover Shaw. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard analog leftover Shaw. "
    "Dengar with Gun True dested Dengar With Blaster Carbine True analog leftover HT. "
    "V3PO dested U-3PO analog leftover Amato. "
    "4LOM with rifle True dested 4-LOM With Concussion Rifle True analog leftover Foth. "
    "Dr E & PB dested Dr. Evazan & Ponda Baba analog leftover Shaw. "
    "Victory dested Victory analog leftover Shaw. "
    "Elis in Huttna dested Elis Helrot analog leftover Shaw. "
    "Maul Double Saber dested Maul's Double-Bladed Lightsaber analog leftover Shaw. "
    "Galen Saber Gift dested Galen's Lightsaber, Vader's Gift analog leftover Shaw. "
    "Cyborg Sabers dested Grievous' Lightsabers analog leftover Shaw. "
    "Wipe Them Out True dested Wipe Them Out, All Of Them True analog leftover Shaw. "
    "Ability x3 True dested Ability, Ability, Ability True analog leftover Shaw. "
    "Sniper DS dested Sniper & Dark Strike analog leftover Shaw. "
    "Self Destruct Mechanism dested Self-Destruct Mechanism analog leftover Shaw. "
    "Shield Coward dested Come Here You Big Coward analog leftover Lepine. "
    "Shield Code Clearance True dested Do They Have A Code Clearance? True analog leftover Shaw. "
    "Shield YCHF True dested You Cannot Hide Forever True analog leftover Shaw. "
    "Shield Let Fate Decide dested We'll Let Fate-a Decide, Huh? analog leftover Shaw. "
    "Unique overcounts sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Anger, Fear, Aggression", True),
    n("Commando Training & K'lor'slug"),
    n("Wokling", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Tatooine (Coruscant)"),
    n("Home One: War Room"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke Skywalker, Rebel Scout", qty=3),
    n("Chewie, Enraged", True, qty=3),
    n("Chewbacca Of Kashyyyk", True),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Captain Verrack", True),
    n("Yoda, Great Warrior"),
    n("Chewbacca's Revenge"),
    n("Luke's Blaster Pistol", True),
    n("Rebel Gunrunner"),
    n("Let's Keep A Little Optimism Here", True),
    n("Draw Their Fire"),
    n("Launching The Assault"),
    n("Escape Pod", True, qty=2),
    n("Houjix", qty=2),
    n("Grimtaash"),
    n("Hear Me Baby, Hold Together", True),
    n("Slight Weapons Malfunction"),
    n("The Force Is Strong With This One"),
    n("Run Luke, Run!"),
    n("Use The Force", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Wookiee Roar", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Jedi Levitation", True),
    n("Sabotage", True),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Another Pathetic Lifeform", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("3,720 To 1", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("Knowledge And Defense", True),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Battle Droid Squad", qty=3),
    n("IG-100 MagnaGuard", qty=3),
    n("P-59"),
    n("P-60"),
    n("Dengar With Blaster Carbine", True),
    n("U-3PO"),
    n("4-LOM With Concussion Rifle", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Victory"),
    n("Elis Helrot"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Forced Servitude"),
    n("No Escape"),
    n("Wipe Them Out, All Of Them", True),
    n("The Phantom Menace", qty=2),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Monnok"),
    n("Masterful Move"),
    n("Oh, Switch Off", qty=2),
    n("Operational As Planned", True),
    n("Maul Strikes"),
    n("Force Field", True, qty=2),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Force Push", True),
    n("Ghhhk"),
    n("Self-Destruct Mechanism"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Weapon Of A Sith"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
