#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Greg Shaw.

Source: 2012TMWDay1.pdf pages 7–8 (handwritten 2010 Xerox, 12 shields).
Name Gregory Shaw dested Greg Shaw analog leftover generate_2012_nats/mpc CANON
and player-stubs/Greg_Shaw.wiki. Username blank. p07 DARK checked Deck Name
Steve Baroni skip. p08 LIGHT checked Deck Name Cole Lepine skip. Event TMW.
Do not dest as a new person. Do not dest 2012 MPC Shaw 60s again.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2012 Texas Mini Worlds Day 1 Greg Shaw LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Gregory Shaw dested Greg Shaw analog leftover "
    "generate_2012_nats CANON. Username blank. Event TMW. Date blank. "
    "Do not dest as a new person. Do not dest 2012 MPC Shaw 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Gregory Shaw dested Greg Shaw. Username blank. "
    "LIGHT checked. Deck Name Cole Lepine skip. Event TMW. "
    "Watch Your Step True dested Watch Your Step analog leftover grouty. "
    "Corellian Eng Corp dested Corellian Engineering Corporation analog leftover True. "
    "Insurrection & Aim High dested analog leftover Atkin. "
    "Spaceport Scoundrels Guild dested Scoundrel's Guild analog leftover Brady. "
    "Luke Skywalker Jedi Knight dested Luke Skywalker, Jedi Knight analog leftover Cullen qty=2. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi analog leftover Ojala qty=2. "
    "Yoda Great Warrior dested Yoda, Great Warrior analog leftover qty=2. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover qty=2. "
    "Dasil Rendar dested Dash Rendar analog leftover True. "
    "Paleso Rashad dested leftover_xerox as written. "
    "Meizan Terrik dested Mezian Terrik leftover_xerox. "
    "Boshek Brash Smuggler dested BoShek, Brash Smuggler analog leftover. "
    "Romas Lock Navander dested Romas \"Lock\" Navander analog leftover. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Shaw. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Shaw. "
    "Boshek's Modified Freighter dested BoShek's Modified Freighter analog leftover Atkin. "
    "Merc Sunset dested Mercenary Sunset leftover_xerox True. "
    "Yub Yub Cmdr dested Yub Yub, Commander analog leftover. "
    "Let The Wookiee Win dested analog leftover True qty=3. "
    "Hear Me Baby dested Hear Me Baby, Hold Together analog leftover Shaw True. "
    "Leia dested Princess Leia analog leftover Veasey True. "
    "Klor Slug dested K'lor'slug analog leftover True. "
    "Sense (PRE) dested Sense analog leftover. "
    "Ant Man & Reb Re dested Antilles Maneuver & Rebel Reinforcements analog leftover Shaw qty=2. "
    "All Wings & Darklighter dested All Wings Report In & Darklighter Spin analog leftover qty=2. "
    "Anger Fear Aggression dested Anger, Fear, Aggression analog leftover True IN THE 60. "
    "Shield Yavin Sentry dested Massassi Base Sentry analog leftover Anderson True. "
    "Shield He Can Go About His Biz dested He Can Go About His Business analog leftover True. "
    "Shield Let's Keep A Little Opt dested Let's Keep A Little Optimism Here analog leftover True. "
    "Shield Jabba's Prize dested analog leftover grouty True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Gregory Shaw dested Greg Shaw. Username blank. "
    "DARK checked. Deck Name Steve Baroni skip. Event TMW. "
    "Hunt Down And Stuff dested Hunt Down And Destroy The Jedi analog leftover True. "
    "Coruscant (SE) dested Coruscant (Dark) analog leftover Simmering. "
    "Imperial City dested Coruscant: Imperial City analog leftover Lingrell. "
    "A Sith's Plans dested analog leftover Alperstein. "
    "Ni Chuba Na dested Ni Chuba Na?? analog leftover True. "
    "Gift of The Master dested Gift Of The Master analog leftover. "
    "Darth Vader Betrayer dested Darth Vader, Betrayer Of Jedi analog leftover qty=3. "
    "Dr Evazan & Ponda Baba dested analog leftover. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice analog leftover Shaw qty=3. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Nelson. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover qty=2. "
    "Cyborg's Lightsabers dested Grievous' Lightsabers analog leftover. "
    "Vader's Saber dested Darth Vader's Lightsaber analog leftover. "
    "Galen's Saber Gift dested Galen's Lightsaber, Vader's Gift analog leftover Shaw. "
    "Galen's Fighter dested Rogue Shadow analog leftover. "
    "Naboo: Theed Palace Gen Core dested Naboo: Theed Palace Generator Core analog leftover Herold. "
    "BF Bridge dested Blockade Flagship: Bridge analog leftover. "
    "BF Hallway dested Blockade Flagship: Hallway analog leftover. "
    "4 LOM With Rifle dested 4-LOM With Rifle analog leftover True. "
    "Wipe Them Out dested Wipe Them Out, All Of Them analog leftover Shaw True. "
    "Mara Jade With Saber dested Mara Jade With Lightsaber analog leftover. "
    "Boba Fett Bounty Hunter dested Boba Fett, Renowned Bounty Hunter analog leftover. "
    "We Must Accelerate Plans dested We Must Accelerate Our Plans analog leftover qty=3. "
    "Ghhhk & Those Rebels Won't dested Ghhhk & Those Rebels Won't Escape Us analog leftover. "
    "One Beautiful Thing dested analog leftover alex_w. "
    "Shield Weapon Of A Sith dested analog leftover Herold TMW. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Scoundrel's Guild"),
    n("Spaceport Streets"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Maris Brood, Fallen Jedi", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Corran Horn", qty=2),
    n("Dash Rendar", True),
    n("Paleso Rashad"),
    n("Mezian Terrik"),
    n("Chewbacca", True),
    n("BoShek, Brash Smuggler"),
    n("Romas \"Lock\" Navander"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Spiral"),
    n("Tantive IV", True),
    n("Booster In Pulsar Skate"),
    n("BoShek's Modified Freighter"),
    n("No Questions Asked", True, qty=2),
    n("Seeking An Audience", True),
    n("Mercenary Sunset", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True),
    n("Yub Yub, Commander"),
    n("Let The Wookiee Win", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Princess Leia", True),
    n("Menace Fades"),
    n("K'lor'slug", True),
    n("Sense"),
    n("Corellian Retort", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Antilles Maneuver", True),
    n("Padme Naberrie", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Massassi Base Sentry", True),
    n("Another Pathetic Lifeform", True),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Knowledge And Defense", True),
    n("Blaster Rack", True),
    n("Darth Vader, Betrayer Of Jedi", qty=3),
    n("The Emperor", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Galen, Secret Apprentice", qty=3),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Blizzard 4"),
    n("Grievous' Lightsabers"),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Endor"),
    n("4-LOM With Rifle", True),
    n("Wipe Them Out, All Of Them", True),
    n("Search And Destroy"),
    n("Mara Jade With Lightsaber"),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("We Must Accelerate Our Plans", qty=3),
    n("No Escape"),
    n("Revenge Of The Sith"),
    n("Tarkin's Bounty", True),
    n("Imperial Reinforcements", True),
    n("Sith Fury", True),
    n("Masterful Move"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure"),
    n("According To My Design"),
    n("Disarmed", qty=2),
    n("Imperial Barrier", qty=2),
    n("Force Push", True),
    n("Force Field", True),
    n("One Beautiful Thing"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
]
DS_ADD = []
