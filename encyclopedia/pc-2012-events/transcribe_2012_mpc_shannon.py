#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Kevin Shannon.

Source: 2012mpcday1.pdf pages 9–10 (2010 form, 12 shields).
Name Shannon dested Kevin Shannon. Username blank.
p09 LIGHT/DARK empty; dest Dark from Hunt Down 60. Deck Name empty.
p10 LIGHT/DARK empty; dest Light from Watch Your Step 60. Deck Name empty.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2012 Match Play Championship Day 1 Kevin Shannon LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Kevin Shannon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon. Username blank. "
    "LIGHT/DARK empty; dest Light from Watch Your Step 60. Deck Name empty. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Tatooine (E1) dested Tatooine (Coruscant). Cantina dested Tatooine: Cantina. "
    "Docking Bay 94 dested Tatooine: Docking Bay 94. "
    "Lars Moisture Farm dested Tatooine: Lars' Moisture Farm. "
    "Han Solo Courageous Smuggler dested Han Solo, Courageous Smuggler. "
    "Tallon Karde dested Talon Karrde. Mirax dested Mirax Terrik. "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler. "
    "Rane Raujiid dested Rycar Ryjerd. Lando with Blaster dested Lando With Blaster Rifle. "
    "Antilles Maneuver + Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "BoShek's Modified Freighter dested as written. "
    "All Wings Report in + Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Control + Tunnel Vision dested Control & Tunnel Vision. "
    "It's A Hit dested It's A Hit!. Blast The Door Kid dested Blast The Door, Kid!. "
    "Klor Slug dested K'lor'slug. "
    "Wookiee Strangle form 46 empty and form 47 True kept separate. "
    "Shield Compassion crossed, A Tragedy Has Occurred dested as replacement. "
    "Unique overcounts sheet-accurate (Luke Skywalker x2, Dash Rendar x2, "
    "Han Solo, Courageous Smuggler x2, Chewbacca x2, Melas x2, Talon Karrde x2, "
    "Outrider x2, Artoo-Detoo In Red 5 x2, All Wings Report In & Darklighter Spin x3, "
    "Escape Pod x2, Choke x2, Moving To Attack Position x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon. Username blank. "
    "LIGHT/DARK empty; dest Dark from Hunt Down 60. Deck Name empty. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Sith's Plans dested A Sith's Plans. Gift of Master dested Gift Of The Master. "
    "Ni Chuba dested Ni Chuba Na??. Imperial City dested Coruscant: Imperial City. "
    "Theed generator Core dested Naboo: Theed Palace Generator Core. "
    "Flagship Hallway dested Blockade Flagship: Hallway. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "DVDLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice. "
    "General Nevar dested as written. Black leader dested Juno Eclipse, Black Leader. "
    "Thrawn dested Grand Admiral Thrawn. Galens Fighter dested Rogue Shadow. "
    "Cyborg Commanders Lightsabers dested Grievous' Lightsabers. "
    "Galens Lightsaber Vaders gift dested Galen's Lightsaber, Vader's Gift. "
    "One Beautiful Thing dested as written. "
    "Masterful Move + Endor Occ dested Masterful Move & Endor Occupation. "
    "Weapon Levitation + The Empires Back dested Weapon Levitation & The Empire's Back. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. Ellis Helrot dested Elis Helrot. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Do they have a code clear dested Do They Have A Code Clearance?. "
    "Come here Big Coward dested Come Here You Big Coward. "
    "Unique overcounts sheet-accurate (Grievous, Hunter Of Jedi x2, Emperor Palpatine x2, "
    "Galen, Secret Apprentice x3, Darth Vader, Dark Lord Of The Sith x3, Battle Droid Squad x2, "
    "Victory x2, Trophy Of A Kill x3, Masterful Move & Endor Occupation x2, Force Field x2, "
    "We Must Accelerate Our Plans x2, Weapon Levitation & The Empire's Back x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("I Must Be Allowed To Speak"),
    n("Kessel"),
    n("Corellia", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Luke Skywalker", True, qty=2),
    n("Dash Rendar", qty=2),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Chewbacca", True, qty=2),
    n("Melas", True, qty=2),
    n("Talon Karrde", qty=2),
    n("Wedge Antilles", True),
    n("Mirax Terrik"),
    n("BoShek, Brash Smuggler"),
    n("Rycar Ryjerd", True),
    n("Sergeant Doallyn", True),
    n("Lando With Blaster Rifle"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Pulsar Skate"),
    n("Outrider", qty=2),
    n("Millennium Falcon"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("BoShek's Modified Freighter"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Choke", qty=2),
    n("Wookiee Strangle"),
    n("Wookiee Strangle", True),
    n("Sabotage", True),
    n("Inconsequential Barriers"),
    n("Control & Tunnel Vision"),
    n("It's A Hit!"),
    n("Blast The Door, Kid!"),
    n("Moving To Attack Position", qty=2),
    n("K'lor'slug", True),
    n("Scrambled Transmission", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Weapons Display"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred", True),
    n("Jabba's Prize", True),
    n("Let's Keep A Little Optimism Here"),
    n("The Professor"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans"),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Hallway"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Garindan", True),
    n("Battle Droid Squad", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("General Nevar"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Victory", qty=2),
    n("Rogue Shadow"),
    n("Grievous' Lightsabers"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Trophy Of A Kill", qty=3),
    n("One Beautiful Thing"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Weapon Levitation & The Empire's Back", qty=2),
    n("Force Field", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Elis Helrot"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imperial Justice", True),
    n("A Sith's Weapon"),
    n("Revenge Of The Sith"),
    n("Blast Door Controls"),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Resistance"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
