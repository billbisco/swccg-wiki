#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Steve Baroni.

Source: 2012mpcday1.pdf pages 25–26 (2010 form, 12 shields).
Name Baroni dested Steve Baroni. Username blank.
p25 Dark Innovation.dec / Hunt Down (V). p26 Light Choo-Chooomuning / Communing.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2012 Match Play Championship Day 1 Steve Baroni LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Steve Baroni DS.png"
LS_DECK_NAME = "Choo-Chooomuning"
DS_DECK_NAME = "Innovation.dec"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Baroni dested Steve Baroni. Username blank. "
    "Event box empty dested MPC Day 1 by pairing. Deck Name Choo-Chooomuning. "
    "LIGHT/DARK empty dested Light from 60s. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Communing checkbox True dested Communing without (V) in title. "
    "Home One dested Home One. Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Luke Rebel Hero dested Luke Skywalker, Rebel Hero. "
    "Form 5 True and forms 6–7 empty dittos kept separate. "
    "Form 8 crossed, AFA dested Anger, Fear, Aggression. "
    "Captain Verrack dested Captain Verrack. LOK dested Look Sir, Droids. "
    "Chewie Enraged dested Chewie, Enraged. Shmi dested Shmi Skywalker. "
    "Yoda Great Warrior dested Yoda, Great Warrior. Ackbar dested Admiral Ackbar. "
    "Master Kenobi dested Master Kenobi. Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Threepio w Parts dested Threepio With His Parts Showing. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Home One War Room dested Home One: War Room. "
    "Obi's Hut dested Tatooine: Obi-Wan's Hut. "
    "Slave Quarters dested Tatooine: Slave Quarters. "
    "Cantina dested Tatooine: Cantina. Tatooine EP1 dested Tatooine (Coruscant). "
    "Chewbacca Bowcaster dested Chewbacca's Bowcaster. "
    "Luke's Blaster Pistol dested Luke's Blaster Pistol. "
    "Commando Train / Klor Slug dested Commando Training & K'lor'slug. "
    "Bith Shuffle / Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Launching Assault dested Launching The Assault. "
    "Antilles Man / Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "Hear Me Baby dested Hear Me Baby, Hold Together. "
    "OOC/TT dested Out Of Commission & Transmission Terminated. "
    "Grimtaash dested Grimtaash. Force is Strong W dested The Force Is Strong With This One. "
    "Slight Weapon Mal dested Slight Weapons Malfunction. "
    "Strike Cover dested Strikeforce. Run Luke Run dested Run Luke, Run!. "
    "Rug Hug dested Rug Hug. "
    "Insight dested Your Insight Serves You Well. "
    "Keep Optimism dested Let's Keep A Little Optimism Here. "
    "Go about Business dested He Can Go About His Business. "
    "Do or Do Not dested Do, Or Do Not. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Baroni dested Steve Baroni. Username blank. "
    "Event box empty dested MPC Day 1 by pairing. Deck Name Innovation.dec. "
    "LIGHT/DARK empty dested Dark from 60s. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "HD V dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Naboo Generator Core dested Naboo: Theed Palace Generator Core. "
    "Executor dested Flagship Executor. Blockade Bridge dested Blockade Flagship: Bridge. "
    "Coruscant SE dested Coruscant. Blockade Hallway dested Blockade Flagship: Hallway. "
    "Imp City dested Coruscant: Imperial City. "
    "Cyborg Commander Lightsaber dested Grievous' Lightsabers. "
    "Galen's Saber Vader dested Galen's Lightsaber, Vader's Gift. "
    "Galen Secret App dested Galen, Secret Apprentice. "
    "Cyborg Commander Hunter Jedi dested Grievous, Hunter Of Jedi. "
    "Darth Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Mara w Saber dested Mara Jade With Lightsaber. "
    "Dr E Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter. "
    "4 Lom w Concussion dested 4-LOM With Concussion Rifle. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Blizzard 4 dested Blizzard 4. Viper dested Viper Probe Droid. "
    "Galen's Fighter dested Rogue Shadow. "
    "Ghhhk / Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Masterful Move / EO dested Masterful Move & Endor Occupation. "
    "We Must Accel dested We Must Accelerate Our Plans. "
    "Prep Defense dested Prepared Defenses. Search & Destroy dested Search And Destroy. "
    "Gift of Master dested Gift Of The Master. Ni Chuba Na dested Ni Chuba Na??. "
    "Endor Shield dested Endor Shield. Our Battler dested as written. "
    "Revenge of Sith dested Revenge Of The Sith. A Sith's Plans dested A Sith's Plans. "
    "Sith Fury dested Sith Fury. End Rejoicements dested End This Destructive Conflict. "
    "Wipe Them Out All dested Wipe Them Out, All Of Them. K&D dested Knowledge And Defense. "
    "OPE Enforcement dested Oppressive Enforcement. Coward dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. Useless Gesture dested A Useless Gesture. "
    "Allegations dested Allegations Of Corruption. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing", True),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke Skywalker, Rebel Hero", True),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Anger, Fear, Aggression"),
    n("Captain Verrack", True),
    n("Look Sir, Droids", True),
    n("Chewbacca", True),
    n("Chewie, Enraged", True, qty=2),
    n("Shmi Skywalker"),
    n("Yoda, Great Warrior", True),
    n("Admiral Ackbar", True),
    n("Master Kenobi", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Threepio With His Parts Showing"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Slave Quarters"),
    n("Tatooine: Cantina"),
    n("Tatooine (Coruscant)"),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Commando Training & K'lor'slug", True),
    n("Escape Pod", True, qty=2),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Hindsight", True),
    n("Sabotage", True),
    n("Draw Their Fire"),
    n("Launching The Assault"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Hear Me Baby, Hold Together", True),
    n("Wokling", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Grimtaash"),
    n("Houjix"),
    n("The Force Is Strong With This One"),
    n("Rebel Gunrunner", True),
    n("Jedi Levitation", True),
    n("Slight Weapons Malfunction"),
    n("Strikeforce", True),
    n("Use The Force", True, qty=2),
    n("Wookiee Roar", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Rug Hug"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred", True),
    n("Battle Plan", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Affect Mind", True),
    n("Do, Or Do Not", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Naboo: Theed Palace Generator Core", True),
    n("Flagship Executor"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant"),
    n("Blockade Flagship: Hallway"),
    n("Coruscant: Imperial City"),
    n("Grievous' Lightsabers", True),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True, qty=3),
    n("Mara Jade With Lightsaber", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Bounty Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("Juno Eclipse, Black Leader", True),
    n("Admiral Motti", True),
    n("Grand Moff Tarkin", True),
    n("Blizzard 4"),
    n("Viper Probe Droid", True),
    n("Rogue Shadow", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Lightning"),
    n("Imperial Barrier", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Disarmed", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Push"),
    n("Lightsaber Deficiency", True),
    n("Prepared Defenses", True),
    n("Search And Destroy"),
    n("Blaster Rack", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Our Battler", True),
    n("Force Field", True),
    n("Revenge Of The Sith", True),
    n("No Escape"),
    n("A Sith's Plans", True),
    n("Protocol Failure", True),
    n("Sith Fury", True),
    n("End This Destructive Conflict", True),
    n("Wipe Them Out, All Of Them", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Fanfare", True),
]
DS_ADD = []
