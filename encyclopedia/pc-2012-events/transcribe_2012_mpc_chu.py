#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Jonny Chu.

Source: 2012mpcday1.pdf pages 19–20 (2010 form, 12 shields).
Name Jonny Chu dested Jonny Chu. Username blank.
p19 Light Grimtaash. p20 Dark Mando.
Skip p17–p18 Keith Brown other-event bound-in.
"""
from __future__ import annotations

PLAYER = "Jonny Chu"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2012 Match Play Championship Day 1 Jonny Chu LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Jonny Chu DS.png"
LS_DECK_NAME = "Grimtaash"
DS_DECK_NAME = "Mando"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jonny Chu dested Jonny Chu. Username blank. "
    "Event MPC Day 1. Deck Name Grimtaash. LIGHT. "
    "Communing dested Communing. Master Kenobi dested Master Kenobi. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "Anger Fear Aggres dested Anger, Fear, Aggression. "
    "Commando Train. + K'lor'slug dested Commando Training & K'lor'slug. "
    "Chewie, Enraged dested Chewie, Enraged. "
    "Chewbacca of Kashyyyk dested Chewbacca Of Kashyyyk. "
    "Chewbacca dested Chewbacca. "
    "Luke Skywalker, Rebel Hero dested Luke Skywalker, Rebel Hero. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Captain Hutton / Yutani w/ Blaster Cannon dested Captain Yutani With Blaster Cannon. "
    "Threepio w/ Parts Showing dested Threepio With His Parts Showing. "
    "Shmi Skywalker dested Shmi Skywalker. Ackbar dested Admiral Ackbar. "
    "Captain Verrack dested Captain Verrack. Padmé Naberrie dested Padmé Naberrie. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Corran Horn dested Corran Horn. Home One dested Home One. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Home One: War Room dested Home One: War Room. "
    "Tatooine: Obi-Wan's Hut dested Tatooine: Obi-Wan's Hut. "
    "Tatooine: Cantina dested Tatooine: Cantina. "
    "Tatooine (Coruscant) dested Tatooine (Coruscant). "
    "Chewbacca's Bowcaster dested Chewbacca's Bowcaster. "
    "Luke's Blaster Pistol dested Luke's Blaster Pistol. "
    "Use The Force dested Use The Force. Rebel Leadership dested Rebel Leadership. "
    "Let The Wookiee Win dested Let The Wookiee Win. Escape Pod dested Escape Pod. "
    "Houjix dested Houjix. Grimtaash dested Grimtaash. "
    "Run Luke Run dested Run Luke, Run!. Jedi Levitation dested Jedi Levitation. "
    "Hear Me Baby, Hold Together dested Hear Me Baby, Hold Together. "
    "The Bith Shuffle / Desp Reach dested The Bith Shuffle & Desperate Reach. "
    "Wookiee Roar dested Wookiee Roar. "
    "Slight Weapons Malfunction dested Slight Weapons Malfunction. "
    "Draw Their Fire dested Draw Their Fire. "
    "Let's Keep A Little Optimism Here in main 60 form 55 True and shields form 12 True dested both. "
    "Honor of the Jedi dested Honor Of The Jedi. "
    "Launching The Assault dested Launching The Assault. "
    "Hindsight dested Hindsight. Rebel Barrier dested Rebel Barrier. "
    "Antilles Maneuver + Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Shields: Affect Mind dested Affect Mind. "
    "Form 2 crossed with replacement Do or Do Not dested Do, Or Do Not. "
    "He Can Go About His Business dested He Can Go About His Business. "
    "Aim High dested Aim High. Don't Do That Again dested Don't Do That Again. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Battle Plan dested Battle Plan. A Tragedy Has Occurred dested A Tragedy Has Occurred. "
    "The Professor dested The Professor. Weapons Display dested Weapons Display. "
    "Your Insight Serves You Well dested Your Insight Serves You Well. "
    "Unique overcounts sheet-accurate (Chewie, Enraged x2, Luke Skywalker, Rebel Hero x3, "
    "Artoo-Detoo In Red 5 x2, Use The Force x2, Rebel Leadership x3, Let The Wookiee Win x2, "
    "Escape Pod x2, Run Luke, Run! x2, The Bith Shuffle & Desperate Reach x2, "
    "Wookiee Roar x2, Slight Weapons Malfunction x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jonny Chu dested Jonny Chu. Username blank. "
    "Event MPC Day 1. Deck Name Mando. DARK. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Prepared Defenses dested Prepared Defenses. "
    "Hunt Down Objective dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Coruscant (SE) dested Coruscant. Endor Shield dested Endor Shield. "
    "Ni Chuba Na dested Ni Chuba Na??. Gift of the Master dested Gift Of The Master. "
    "Coruscant: Imperial City dested Coruscant: Imperial City. "
    "A Sith's Plans dested A Sith's Plans. "
    "Darth Vader, Betrayer of the Jedi dested Darth Vader, Betrayer Of The Jedi. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Garindan dested Garindan. Dr Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Emperor Palpatine dested Emperor Palpatine. Grand Moff Tarkin dested Grand Moff Tarkin. "
    "Grand Admiral Thrawn dested Grand Admiral Thrawn. P-59 dested P-59. "
    "General Nevar dested General Nevar. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber. "
    "4-LOM w/ Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Blaster Rack form 28 empty and form 38 True kept separate. "
    "Naboo: Theed Palace Generator Core dested Naboo: Theed Palace Generator Core. "
    "Blockade Flagship: Bridge dested Blockade Flagship: Bridge. "
    "Blockade Flagship: Hallway dested Blockade Flagship: Hallway. "
    "Endor dested Endor. Search and Destroy dested Search And Destroy. "
    "Revenge of the Sith dested Revenge Of The Sith. Discord dested Discord. "
    "Protocol Failure dested Protocol Failure. No Escape dested No Escape. "
    "Wipe Them Out, All Of Them dested Wipe Them Out, All Of Them. "
    "Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "According To My Design dested According To My Design. "
    "We Must Accelerate Our Plans dested We Must Accelerate Our Plans. "
    "Lightsaber Deficiency dested Lightsaber Deficiency. "
    "Ghhhk / Those Rebels Won't Escape dested Ghhhk & Those Rebels Won't Escape Us. "
    "One Beautiful Thing dested One Beautiful Thing. "
    "Sniper / Dark Strike dested Sniper & Dark Strike. "
    "Stunning Leader dested Stunning Leader. Imperial Barrier dested Imperial Barrier. "
    "Force Push dested Force Push. Force Field dested Force Field. "
    "Vader's Lightsaber dested Vader's Lightsaber. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Galen's Fighter dested Rogue Shadow. Victory dested Victory. "
    "Shields: Allegations Of Corruption dested Allegations Of Corruption. "
    "Battle Order dested Battle Order. Come Here You Big Coward dested Come Here You Big Coward. "
    "Secret Plans dested Secret Plans. Weapon Of A Sith dested Weapon Of A Sith. "
    "Fanfare dested Fanfare. Abyss dested Abyss. Resistance dested Resistance. "
    "A Useless Gesture dested A Useless Gesture. "
    "Oppressive Enforcement dested Oppressive Enforcement. "
    "You Cannot Hide Forever dested You Cannot Hide Forever. "
    "Do They Have A Code Clearance? dested Do They Have A Code Clearance?. "
    "Unique overcounts sheet-accurate (Darth Vader, Betrayer Of The Jedi x4, "
    "Galen, Secret Apprentice x3, Grievous, Hunter Of Jedi x2, Revenge Of The Sith x2, "
    "Discord x2, We Must Accelerate Our Plans x3, Force Field x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Master Kenobi"),
    n("Tatooine: Slave Quarters"),
    n("Wokling", True),
    n("Anger, Fear, Aggression"),
    n("Commando Training & K'lor'slug"),
    n("Chewie, Enraged", True, qty=2),
    n("Chewbacca Of Kashyyyk", True),
    n("Chewbacca", True),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Lando Calrissian, Scoundrel", True),
    n("Captain Yutani With Blaster Cannon"),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Admiral Ackbar", True),
    n("Captain Verrack", True),
    n("Padmé Naberrie", True),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Tatooine (Coruscant)"),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Use The Force", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("Run Luke, Run!", True, qty=2),
    n("Jedi Levitation", True),
    n("Hear Me Baby, Hold Together", True),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Wookiee Roar", True, qty=2),
    n("Slight Weapons Malfunction", qty=2),
    n("Draw Their Fire"),
    n("Let's Keep A Little Optimism Here", True),
    n("Honor Of The Jedi"),
    n("Launching The Assault"),
    n("Hindsight", True),
    n("Rebel Barrier"),
    n("Antilles Maneuver & Rebel Reinforcements"),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Do, Or Do Not", True),
    n("He Can Go About His Business", True),
    n("Aim High", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Prepared Defenses", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Darth Vader, Betrayer Of The Jedi", qty=4),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Garindan", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("General Nevar"),
    n("Mara Jade With Lightsaber", True),
    n("4-LOM With Concussion Rifle", True),
    n("Blaster Rack"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Endor"),
    n("Search And Destroy"),
    n("Revenge Of The Sith", qty=2),
    n("Discord", qty=2),
    n("Blaster Rack", True),
    n("Protocol Failure"),
    n("No Escape"),
    n("Wipe Them Out, All Of Them", True),
    n("Masterful Move & Endor Occupation"),
    n("According To My Design"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("One Beautiful Thing"),
    n("Sniper & Dark Strike"),
    n("Stunning Leader"),
    n("Imperial Barrier"),
    n("Force Push", True),
    n("Force Field", True, qty=2),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Rogue Shadow"),
    n("Victory"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("Secret Plans", True),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Abyss", True),
    n("Resistance", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
