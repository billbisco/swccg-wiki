#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Robbie Hendon.

Source: 2012TMWDay1.pdf pages 11–12 (typed slang printout, not a handwritten
Xerox form). Name Robbie Hendon dested Robbie Hendon analog leftover 2013 TMW
/ 2015 TMW / 2016 TMW / player-stubs/Robbie_Hendon.wiki. Username blank
(typed dump has no Username field; analog leftover 2013 TMW /hendon stays
off THIS transcribe). p11 Light. p12 Dark. Do not dest as a new person.
Do not dest 2013 TMW Hendon 60s again.
"""
from __future__ import annotations

PLAYER = "Robbie Hendon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2012 Texas Mini Worlds Day 1 Robbie Hendon LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Robbie Hendon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Robbie Hendon dested Robbie Hendon analog leftover 2013 TMW. "
    "Username blank. Do not dest as a new person. Do not dest 2013 TMW Hendon 60s again."
)
LS_NOTE = (
    "Typed slang printout. Name Robbie Hendon dested Robbie Hendon. Username blank. "
    "Tat: Slave Quarters dested Tatooine: Slave Quarters analog leftover Shaw. "
    "Communing dested Communing analog leftover Shaw. "
    "Commando Training/K'lor'slug dested Commando Training & K'lor'slug analog leftover Shaw. "
    "Tat: Obi's Hut True dested Tatooine: Obi-Wan's Hut analog leftover Shaw True. "
    "3P0 w/ Parts dested Threepio With His Parts Showing analog leftover. "
    "Leia, RP dested Leia, Rebel Princess analog leftover Shaw. "
    "Han w/ Blaster dested Han With Heavy Blaster Pistol analog leftover Anis/Cullen qty=2. "
    "The Bith Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach analog leftover Shaw qty=2. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Shaw qty=2. "
    "Let the Wookie Win True dested Let The Wookiee Win analog leftover True qty=2. "
    "Antilles Maneuver/Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements analog leftover. "
    "Wookie Roar True dested Wookiee Roar analog leftover Shaw True qty=2. "
    "Chewbacca of Kashyyk True dested Chewbacca Of Kashyyyk analog leftover Lingrell True. "
    "Strikeforce True dested Strike Force analog leftover Barnes True. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel analog leftover. "
    "Home 1 dested Home One analog leftover Shaw. "
    "Chewie Enraged True dested Chewie, Enraged analog leftover Shaw True qty=2. "
    "Home 1 War Room dested Home One: War Room analog leftover. "
    "Run Luke Run True dested Run Luke, Run! analog leftover Shaw True qty=2. "
    "Hear Me Baby Hold Together True dested Hear Me Baby, Hold Together analog leftover Shaw True. "
    "Houjix dested Houjix analog leftover Shaw (sheet writes Houjix only). "
    "Anger Fear Aggression True dested Anger, Fear, Aggression True analog leftover Barnes IN THE 60. "
    "Shield Simple Tricks and Nonsense dested Simple Tricks And Nonsense analog leftover Shaw. "
    "Shield Do or Do Not dested Do, Or Do Not analog leftover Barnes. "
    "Shield Yavin Sentry True dested Massassi Base Sentry analog leftover Shaw True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed slang printout. Name Robbie Hendon dested Robbie Hendon. Username blank. "
    "Hunt Down and Destroy the Jedi True dested Hunt Down And Destroy The Jedi analog leftover True. "
    "Cor: Imp City dested Coruscant: Imperial City analog leftover. "
    "Gift of the Master dested Gift Of The Master analog leftover. "
    "We Must Accelerate our Plans dested We Must Accelerate Our Plans analog leftover qty=3. "
    "Kir Kanos W/ Force Pike dested Kir Kanos With Force Pike analog leftover Alperstein. "
    "4Lom W/ Conc True dested 4-LOM With Concussion Rifle analog leftover Alperstein True. "
    "P59 dested P-59 analog leftover. "
    "Masterful Move/Endor Occupation dested Masterful Move & Endor Occupation analog leftover Barnes. "
    "Dr. E/Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Shaw. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi analog leftover qty=2. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover. "
    "Galen's Fighter dested Rogue Shadow analog leftover. "
    "Darth Vader, Betrayer of Jedi dested Darth Vader, Betrayer Of Jedi analog leftover Shaw. "
    "Vader's Lightsaber dested Darth Vader's Lightsaber analog leftover Shaw. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Shaw. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber analog leftover Shaw. "
    "Boba Fett, Bounty Hunter dested Boba Fett, Renowned Bounty Hunter analog leftover Shaw. "
    "Ghhhk/Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us analog leftover Shaw. "
    "Dengar w/ Blaster dested Dengar With Blaster Carbine analog leftover Alperstein. "
    "Knowledge and Defense True dested Knowledge And Defense analog leftover Barnes True IN THE 60. "
    "Shield There is No Try dested There Is No Try analog leftover Shaw. "
    "Shield I Find Your Lack of Faith Disturbing True dested I Find Your Lack Of Faith Disturbing analog leftover. "
    "Shield Allegations of Corruption dested Allegations Of Corruption analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Threepio With His Parts Showing"),
    n("Tatooine"),
    n("Launching The Assault"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Padme Naberrie", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Chewbacca", True),
    n("Yoda, Great Warrior"),
    n("Shmi Skywalker"),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Rebel Leadership", True, qty=2),
    n("Hindsight", True),
    n("Wookiee Roar", True, qty=2),
    n("Slight Weapons Malfunction", qty=2),
    n("Chewbacca Of Kashyyyk", True),
    n("Draw Their Fire"),
    n("Security Breach"),
    n("Strike Force", True),
    n("Lando Calrissian, Scoundrel"),
    n("Home One"),
    n("Luke's Blaster Pistol", True),
    n("Chewie, Enraged", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Admiral Ackbar", True),
    n("Grimtaash"),
    n("Home One: War Room"),
    n("Honor Of The Jedi"),
    n("Run Luke, Run!", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("Flash Of Insight", True),
    n("Corran Horn"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Another Pathetic Lifeform", True),
    n("Don't Do That Again"),
    n("Your Insight Serves You Well", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Massassi Base Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Lightsaber Deficiency", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Kir Kanos With Force Pike"),
    n("Force Lightning"),
    n("4-LOM With Concussion Rifle", True),
    n("Blockade Flagship: Hallway"),
    n("P-59"),
    n("Revenge Of The Sith"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Blizzard 4"),
    n("Masterful Move & Endor Occupation"),
    n("Wipe Them Out, All Of Them", True),
    n("General Nevar"),
    n("Force Field", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Disarmed", qty=2),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Grand Moff Tarkin", True),
    n("Victory", True),
    n("Galen, Secret Apprentice", qty=3),
    n("Force Push", True),
    n("Imperial Barrier", qty=2),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Generator Core"),
    n("Grand Admiral Thrawn"),
    n("Juno Eclipse, Black Leader"),
    n("Rogue Shadow"),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("Search And Destroy"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("No Escape"),
    n("One Beautiful Thing"),
    n("Protocol Failure"),
    n("Dengar With Blaster Carbine"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
