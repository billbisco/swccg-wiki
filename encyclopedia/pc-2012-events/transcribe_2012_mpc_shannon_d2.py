#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Kevin Shannon.

Source: 2012mpcday2.pdf pages 15–16 (2010 form, 12 shields).
Name Kevin Shannon dested Kevin Shannon analog leftover. Username blank.
p15 LIGHT empty checkbox dest Light from Watch Your Step 60. p16 DARK checked Hunt Down.
Do not dest as a new person. Do not rewrite Day 1 leftover Hunt Down / Watch Your Step.
Pack player-stubs/Kevin_Shannon.wiki.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2012 Match Play Championship Day 2 Kevin Shannon LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Kevin Shannon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form bound into 2012mpcday2.pdf."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Kevin Shannon dested Kevin Shannon analog leftover. "
    "Username blank. Event MPC 2012. LIGHT/DARK empty dest Light from Watch Your Step 60. "
    "Do not dest as a new person. Do not rewrite Day 1 leftover Watch Your Step. "
    "WYS / TPCBPLR dested Watch Your Step / This Place Can Be A Little Rough analog leftover Shannon. "
    "AFA (v) dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "Tatooine (Coruscant) dested analog leftover Day 1. "
    "Tatooine: Docking Bay 94 dested analog leftover. "
    "Tatooine: Cantina dested analog leftover. "
    "HFTMF dested Heading For The Medical Frigate analog leftover IN THE 60. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin analog leftover unique overcount. "
    "Moving To Attack Position dested analog leftover unique overcount. "
    "Sabotage (v) dested analog leftover. "
    "Escape Pod dested analog leftover unique overcount. "
    "Houjix dested analog leftover. "
    "It's A Hit! dested analog leftover. "
    "It's A Trap! dested analog leftover Alex W. "
    "Antilles Maneuver & Rebel Reinforcements dested analog leftover. "
    "Inconsequential Barriers dested analog leftover. "
    "Wookiee Strangle (v) dested analog leftover. "
    "Choke dested analog leftover. "
    "Control & Tunnel Vision dested analog leftover. "
    "Luke Skywalker (v) dested analog leftover unique overcount. "
    "Dash Rendar dested analog leftover unique overcount. "
    "Han Solo, Courageous Smuggler dested analog leftover unique overcount. "
    "Chewbacca (v) dested analog leftover unique overcount. "
    "Talon Karrde dested analog leftover unique overcount. "
    "Melas dested analog leftover unique overcount. "
    "BoShek, Brash Smuggler dested analog leftover. "
    "Wedge Antilles dested analog leftover. "
    "Mirax Terrik dested analog leftover. "
    "Lando w/ Blaster Pistol dested Lando With Blaster Pistol analog leftover Veasey. "
    "Rycar Ryjerd dested analog leftover Day 1. "
    "Sergeant Doallyn (v) dested analog leftover. "
    "Captain Yutani w/ Blaster Cannon dested Captain Yutani With Blaster Cannon analog leftover Fred as written. "
    "Tatooine: Lars' Moisture Farm (v) dested analog leftover. "
    "Corellia (v) dested analog leftover. "
    "Kessel dested analog leftover. "
    "Outrider dested analog leftover unique overcount. "
    "Artoo-Detoo In Red 5 dested analog leftover unique overcount. "
    "BoShek's Modified Freighter dested analog leftover. "
    "Millennium Falcon dested analog leftover. "
    "Pulsar Skate dested analog leftover. "
    "Squadron Assignments dested analog leftover. "
    "I Must Be Allowed To Speak dested analog leftover. "
    "Menace Fades dested analog leftover. "
    "Wokling dested analog leftover. "
    "Seeking An Audience dested analog leftover. "
    "Civil Disorder dested analog leftover leftover_xerox Effect. "
    "K'lor'slug dested analog leftover. "
    "Imperial Atrocity dested analog leftover unique overcount. "
    "Shield Professor dested The Professor analog leftover. "
    "Shield Aim High dested analog leftover. "
    "Shield Insight (v) dested Your Insight Serves You Well True analog leftover. "
    "Shield LKALOH dested Let's Keep A Little Optimism Here analog leftover. "
    "Shield Ultimatum dested analog leftover. "
    "Shield Weapons Display dested analog leftover. "
    "Shield Battle Plan dested analog leftover. "
    "Shield DDTA dested Don't Do That Again analog leftover. "
    "Shield STAN dested Simple Tricks And Nonsense analog leftover. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover. "
    "Shield Chasm dested analog leftover. "
    "Shield 12 blank skipped. Additional Jabba's Prize (v) dested Jabba's Prize True analog leftover Day 1 shield. "
    "Unique overcounts sheet-accurate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Kevin Shannon dested Kevin Shannon analog leftover. "
    "Username blank. Event MPC 2012. DARK checked. "
    "Do not dest as a new person. Do not rewrite Day 1 leftover Hunt Down. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe empty analog leftover empty checkbox dest dual without True. "
    "K&D (v) dested Knowledge And Defense True analog leftover Murray IN THE 60. "
    "Emperor Palpatine dested analog leftover unique overcount. "
    "Darth Vader, Dark Lord Of The Sith dested analog leftover unique overcount. "
    "Galen, Secret Apprentice dested analog leftover unique overcount. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover unique overcount. "
    "Mara Jade With Lightsaber dested analog leftover. "
    "Dr. Evazan & Ponda Baba dested analog leftover. "
    "Battle Droid Squad dested analog leftover. "
    "Garindan (v) dested analog leftover. "
    "4-LOM w/ Concussion Rifle (v) dested 4-LOM With Concussion Rifle True analog leftover Foth. "
    "Myn Kyneugh (v) dested analog leftover Philippe. "
    "Grand Moff Tarkin dested analog leftover. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover. "
    "Grand Admiral Thrawn dested analog leftover. "
    "General Nevar dested analog leftover. "
    "Coruscant (SE) dested Coruscant analog leftover Foth. "
    "Coruscant: Imperial City dested analog leftover. "
    "Endor dested analog leftover. "
    "Blockade Flagship: Bridge dested analog leftover. "
    "Blockade Flagship: Hallway dested analog leftover. "
    "Naboo Theed Palace Generator Core dested Naboo: Theed Palace Generator Core analog leftover. "
    "Victory dested analog leftover unique overcount. "
    "Galen's Fighter dested Rogue Shadow analog leftover Day 1 Shannon. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover. "
    "Vader's Lightsaber dested analog leftover. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover. "
    "Trophy Of A Kill dested analog leftover unique overcount. "
    "Prepared Defenses (v) dested analog leftover IN THE 60. "
    "We Must Accelerate Our Plans dested analog leftover unique overcount. "
    "Cold Feet (v) dested analog leftover. "
    "Vader's Obsession dested analog leftover Field. "
    "Elis Helrot dested analog leftover. "
    "Sniper & Dark Strike dested analog leftover. "
    "Force Field dested analog leftover unique overcount. "
    "Weapon Levitation & The Empire's Back dested analog leftover unique overcount. "
    "Masterful Move & Endor Occupation dested analog leftover unique overcount. "
    "Force Push dested analog leftover. "
    "Ghhhk dested analog leftover. "
    "A Sith's Plans dested analog leftover. "
    "Endor Shield dested analog leftover. "
    "Gift Of The Master dested analog leftover. "
    "Ni Chuba Na (v) dested Ni Chuba Na?? True analog leftover. "
    "A Sith's Weapon dested analog leftover. "
    "Revenge Of The Sith dested analog leftover. "
    "Imperial Justice (v) dested analog leftover. "
    "No Escape dested analog leftover. "
    "Blaster Rack (v) dested analog leftover. "
    "Shield Abyss dested analog leftover. "
    "Shield CHYBC dested Come Here You Big Coward analog leftover. "
    "Shield YCHF (v) dested You Cannot Hide Forever True analog leftover. "
    "Shield AUG (v) dested A Useless Gesture True analog leftover. "
    "Shield Resistance dested analog leftover. "
    "Shield DTHACC (v) dested Do They Have A Code Clearance? True analog leftover. "
    "Shield Secret Plans dested analog leftover. "
    "Shield Battle Order dested analog leftover. "
    "Shield Weapon Of A Sith dested analog leftover. "
    "Shield Firepower (v) dested analog leftover. "
    "Shield There Is No Try dested analog leftover. "
    "Shield Allegations dested analog leftover. "
    "Unique overcounts sheet-accurate. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Cantina"),
    n("Heading For The Medical Frigate"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Moving To Attack Position", qty=2),
    n("Sabotage", True),
    n("Escape Pod", qty=2),
    n("Houjix"),
    n("It's A Hit!"),
    n("It's A Trap!"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Inconsequential Barriers"),
    n("Wookiee Strangle", True),
    n("Choke"),
    n("Control & Tunnel Vision"),
    n("Luke Skywalker", True, qty=2),
    n("Dash Rendar", qty=2),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Chewbacca", True, qty=2),
    n("Talon Karrde", qty=2),
    n("Melas", qty=2),
    n("BoShek, Brash Smuggler"),
    n("Wedge Antilles"),
    n("Mirax Terrik"),
    n("Lando With Blaster Pistol"),
    n("Rycar Ryjerd"),
    n("Sergeant Doallyn", True),
    n("Captain Yutani With Blaster Cannon"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Corellia", True),
    n("Kessel"),
    n("Outrider", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("BoShek's Modified Freighter"),
    n("Millennium Falcon"),
    n("Pulsar Skate"),
    n("Squadron Assignments"),
    n("I Must Be Allowed To Speak"),
    n("Menace Fades"),
    n("Wokling"),
    n("Seeking An Audience"),
    n("Civil Disorder"),
    n("K'lor'slug"),
    n("Imperial Atrocity", qty=2),
]
LS_SHIELDS = [
    n("The Professor"),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Knowledge And Defense", True),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Battle Droid Squad"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Myn Kyneugh", True),
    n("Grand Moff Tarkin"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Naboo: Theed Palace Generator Core"),
    n("Victory", qty=2),
    n("Rogue Shadow"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Trophy Of A Kill", qty=2),
    n("Prepared Defenses", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Cold Feet", True),
    n("Vader's Obsession"),
    n("Elis Helrot"),
    n("Sniper & Dark Strike"),
    n("Force Field", qty=2),
    n("Weapon Levitation & The Empire's Back", qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Force Push"),
    n("Ghhhk"),
    n("A Sith's Plans"),
    n("Endor Shield"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("A Sith's Weapon"),
    n("Revenge Of The Sith"),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Blaster Rack", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
