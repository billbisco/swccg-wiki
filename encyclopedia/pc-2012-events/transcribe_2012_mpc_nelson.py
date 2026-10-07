#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Aaron Nelson.

Source: 2012mpcday1.pdf pages 23–24 (2010 form, 12 shields).
Name Aaron Nelson dested Aaron Nelson. Username Airdog 2003 dested Airdog2003.
p23 Dark Local Space Mains / Kessel. p24 Light SoCal WYS.
Do not dest as Jake Nelson. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 24
DS_PAGE = 23
LS_SCAN = "2012 Match Play Championship Day 1 Aaron Nelson LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Aaron Nelson DS.png"
LS_DECK_NAME = "SoCal WYS"
DS_DECK_NAME = "Local Space Mains"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson. "
    "Username Airdog 2003 dested Airdog2003. Event MPC Day 1. Deck Name SoCal WYS. LIGHT. "
    "Do not dest as Jake Nelson. Do not rewrite 2013 leftovers. "
    "Watch Your Step / This Place Can Be A Little Rough checkbox empty dested empty. "
    "Tatooine (ep1) dested Tatooine (Coruscant). Cantina dested Tatooine: Cantina. "
    "Docking Bay 94 dested Tatooine: Docking Bay 94. Han Solo, CS dested Captain Han Solo. "
    "Wedge Antilles dested Wedge Antilles. Pulsar Skate dested Pulsar Skate. "
    "Talon Karrde dested Talon Karrde. Dash Rendar dested Dash Rendar. "
    "Odinith dested Odin Ith. Boshek BS dested BoShek, Brash Smuggler. "
    "Boshek's Modified Freighter dested BoShek's Modified Freighter. "
    "Pulse Generator dested Pulse Generator. Corran dested Corran Horn. "
    "Sgt. Doallyn dested Sergeant Doallyn. Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Landing Claw dested Landing Claw. All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Chewie dested Chewie. Han's Toolkit dested Han's Toolkit. "
    "Imperial Atrocity dested Imperial Atrocity. Sense dested Sense. "
    "Mirax Terrik dested Mirax Terrik. It's a Hit! dested It's A Hit!. "
    "Escape Pod dested Escape Pod. Scrambled Transmission dested Scrambled Transmission. "
    "Chewbacca dested Chewbacca. That Mysterious Planet dested as written. "
    "Evacuation Control dested Evacuation Control. Scramble Combo dested Scramble. "
    "ETDN dested as written. Many Bothans dested Many Bothans Died To Bring Us This Information. "
    "Fallen Jedi Combo Padawan dested Fallen Jedi. Sabotage dested Sabotage. "
    "Mercenary Armor dested Mercenary Armor. Fallen Portal dested Fallen Portal. "
    "Corellia dested Corellia. Wedge Smuggler dested as written. "
    "Capture Beam dested Capture Beam. Houjix dested Houjix. "
    "Chewie's AT-ST dested Chewie's AT-ST. Rycar Ryjerd dested Rycar Ryjerd. "
    "Melas dested Melas. HFTMF form 55 empty and form 60 True kept separate. "
    "Blue Slug dested as written. Wokling dested Wokling. "
    "LTWW x3 dested Let The Wookiee Win True qty=3. "
    "Squadron Assignments dested Squadron Assignments. "
    "Unique overcounts sheet-accurate (Captain Han Solo x2, Dash Rendar x2, "
    "Artoo-Detoo In Red 5 x2, Imperial Atrocity x3, All Wings Report In & Darklighter Spin x2, "
    "Escape Pod x2, Pulse Generator x2, Chewbacca x2, Let The Wookiee Win x3, "
    "Heading For The Medical Frigate x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson. "
    "Username Airdog 2003 dested Airdog2003. Event MPC Day 1. Deck Name Local Space Mains. DARK. "
    "Do not dest as Jake Nelson. Do not rewrite 2013 leftovers. "
    "Kessel dested Kessel. Kessel: Administrator's Office dested "
    "Kessel: Spice Mines - Administrator's Office. "
    "Spice Mine Admin dested Spice Mine Administrator. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "TPM dested The Phantom Menace. Garindan dested Garindan. "
    "Force Push dested Force Push. Ghhhk dested Ghhhk. "
    "Protocol Failure dested Protocol Failure. Grand Moff Tarkin dested Grand Moff Tarkin. "
    "Blaster Rack dested Blaster Rack. Death Squadron dested Death Squadron. "
    "Conquest dested Conquest. Victory dested Victory. "
    "Maul's Ship dested Maul's Sith Infiltrator. Force Field dested Force Field. "
    "Imperial Justice dested Imperial Justice. Cold Feet dested Cold Feet. "
    "Darth Maul w/ Saber dested Darth Maul With Lightsaber. "
    "The Emperor dested The Emperor. Galen Secret Apprentice dested Galen, Secret Apprentice. "
    "Kessel: Spice Mines Prison dested Kessel: Spice Mines - Prison. "
    "Where Are You Taking This Thing dested Where Are You Taking This ... Thing?. "
    "Spice Mine Ops dested Spice Mine Operations. "
    "Masterful Combo dested Masterful Move & Endor Occupation. "
    "SSRFT dested Short Range Fighters & Watch Your Back!. "
    "Imperial Command from Executor dested Imperial Command. "
    "Grand Admiral Thrawn dested Grand Admiral Thrawn. "
    "Turbolaser Combo dested Turbolaser Battery. "
    "Maul's Sith Infiltrator dested Maul's Sith Infiltrator. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "Kessel Spice Mines DB dested Kessel: Spice Mines - Docking Bay. "
    "Form 40 Black Sun Castles dested as written. "
    "P-59 dested P-59. Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Arica dested Arica. Imperial Command dested Imperial Command. "
    "Kessel Surveillance System dested Kessel Surveillance System. "
    "Much Anger In Him dested Much Anger In Him. "
    "Sidious Lightsaber dested Sidious' Lightsaber. "
    "Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "You are Beaten dested You Are Beaten. Vader's Lightsaber dested Vader's Lightsaber. "
    "Myn Kyneugh dested Myn Kyneugh. Combat Readiness dested Combat Readiness. "
    "Ni Chuba Na dested Ni Chuba Na??. Gift of the Master dested Gift Of The Master. "
    "I'll Take Them Myself dested I'll Take Them Myself. K&D dested Knowledge And Defense. "
    "Come Here dested Come Here You Big Coward. AUG dested A Useless Gesture. "
    "YCHTF dested You Cannot Hide Forever. TINT dested There Is No Try. "
    "CHYBC form 5 empty kept separate from form 1 True. "
    "Weapon of a Sith dested Weapon Of A Sith. Battle Order dested Battle Order. "
    "Allegations of Corruption dested Allegations Of Corruption. "
    "Secret Plans dested Secret Plans. Firepower dested Firepower. "
    "Resistance dested Resistance. Abyss dested Abyss. "
    "Unique overcounts sheet-accurate (We Must Accelerate Our Plans x3, "
    "Darth Vader, Dark Lord Of The Sith x2, Death Squadron x2, Victory x2, "
    "Force Field x2, Darth Maul With Lightsaber x2, Galen, Secret Apprentice x2, "
    "Spice Mine Administrator x2, Grand Moff Tarkin x2, Imperial Command x2, "
    "Maul's Sith Infiltrator x2). "
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
    n("Captain Han Solo", qty=2),
    n("Millennium Falcon"),
    n("Wedge Antilles", True),
    n("Pulsar Skate"),
    n("Talon Karrde"),
    n("Dash Rendar", qty=2),
    n("Odin Ith"),
    n("BoShek, Brash Smuggler"),
    n("BoShek's Modified Freighter"),
    n("Pulse Generator", True, qty=2),
    n("Corran Horn", True),
    n("Sergeant Doallyn", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Landing Claw"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Chewie"),
    n("Han's Toolkit", True),
    n("Imperial Atrocity", True, qty=3),
    n("Sense", True),
    n("Kessel"),
    n("Mirax Terrik"),
    n("It's A Hit!"),
    n("Escape Pod", True, qty=2),
    n("Scrambled Transmission", True),
    n("Chewbacca", True, qty=2),
    n("That Mysterious Planet", True),
    n("Evacuation Control"),
    n("Scramble", True),
    n("ETDN"),
    n("Many Bothans Died To Bring Us This Information"),
    n("Fallen Jedi"),
    n("Sabotage", True),
    n("Mercenary Armor"),
    n("Fallen Portal"),
    n("Corellia"),
    n("Wedge Smuggler", True),
    n("Capture Beam"),
    n("Houjix"),
    n("Chewie's AT-ST", True),
    n("Rycar Ryjerd", True),
    n("Melas", True),
    n("Heading For The Medical Frigate"),
    n("Blue Slug", True),
    n("Wokling", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Squadron Assignments"),
    n("Heading For The Medical Frigate", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("The Professor", True),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Spice Mine Administrator", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("The Phantom Menace"),
    n("Garindan", True),
    n("Force Push", True),
    n("Ghhhk"),
    n("Protocol Failure"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Blaster Rack", True),
    n("Death Squadron", qty=2),
    n("Conquest", True),
    n("Victory", qty=2),
    n("Maul's Sith Infiltrator", qty=2),
    n("Force Field", True, qty=2),
    n("Imperial Justice", True),
    n("Cold Feet", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("The Emperor", True),
    n("Galen, Secret Apprentice", qty=2),
    n("Kessel: Spice Mines - Prison"),
    n("Where Are You Taking This ... Thing?"),
    n("Spice Mine Operations"),
    n("Masterful Move & Endor Occupation"),
    n("Short Range Fighters & Watch Your Back!", True),
    n("Imperial Command", True),
    n("Grand Admiral Thrawn"),
    n("Turbolaser Battery"),
    n("Blockade Flagship: Bridge"),
    n("Kessel: Spice Mines - Docking Bay"),
    n("Black Sun Castles"),
    n("P-59"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Arica"),
    n("Imperial Command"),
    n("Kessel Surveillance System"),
    n("Much Anger In Him"),
    n("Sidious' Lightsaber"),
    n("Alert My Star Destroyer!"),
    n("You Are Beaten"),
    n("Vader's Lightsaber"),
    n("Myn Kyneugh", True),
    n("Combat Readiness", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("I'll Take Them Myself"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Battle Order", True),
    n("Allegations Of Corruption", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Resistance"),
    n("Abyss", True),
]
DS_ADD = []
