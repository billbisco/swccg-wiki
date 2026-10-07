#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Clayton Atkin.

Source: 2012mpcday1.pdf pages 41–42 (2010 form, 12 shields).
Name Clayton Atkin dested Clayton Atkin. Username blank (quotes).
p41 Light crap / Watch Your Step. p42 Dark more crap / Hunt Down (V).
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Clayton Atkin"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 41
DS_PAGE = 42
LS_SCAN = "2012 Match Play Championship Day 1 Clayton Atkin LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Clayton Atkin DS.png"
LS_DECK_NAME = "crap"
DS_DECK_NAME = "more crap"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Clayton Atkin dested Clayton Atkin. "
    "Username quotes dested blank. Event Name blank. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "WYS/TPBALR dested Watch Your Step / This Place Can Be A Little Rough empty. "
    "Tat: DB 94 dested Tatooine: Docking Bay 94. "
    "HFTMF dested Heading For The Medical Frigate. "
    "YISYW/Staging areas dested Your Insight Serves You Well & Staging Areas. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. "
    "Control/TV dested Control & Tunnel Vision x2. "
    "Boshek's Mod. Light Freighter dested BoShek's Modified Freighter. "
    "Han w/ Blaster dested Han With Heavy Blaster Pistol. "
    "AWR/DS dested All Wings Report In & Darklighter Spin x3. "
    "Falcon parts dested Falcon Parts as written. "
    "Sergeant Bruckman dested as written. "
    "Phylo Gandish dested as written. Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Clayton Atkin dested Clayton Atkin. "
    "Username blank. Event Name blank. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Hunt Down/TFHGOOTU True dested Hunt Down And Destroy The Jedi / "
    "Their Fire Has Gone Out Of The Universe True. "
    "Galen's fighter dested Rogue Shadow. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Cyborg Commander HOJ dested Grievous, Hunter Of Jedi x2. "
    "Cyborg Commander's lightsabers dested Grievous' Lightsabers. "
    "Galen, Secret Apprentice dested as written x3. "
    "DLOTS dested Darth Vader, Dark Lord Of The Sith x3. "
    "Weapon Lev/Empire's Back dested Weapon Levitation & The Empire's Back. "
    "WMAOP dested We Must Accelerate Our Plans x2. "
    "Shield 10 crossed, Resistance dest replacement (arrow to Additional). "
    "CHYBC dested Come Here You Big Coward. YCHF dested You Cannot Hide Forever True. "
    "Unique 60. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Your Insight Serves You Well & Staging Areas"),
    n("Insurrection & Aim High"),
    n("Squadron Assignments"),
    n("Imperial Atrocity", True),
    n("Ommni Box"),
    n("Menace Fades"),
    n("Out Of Commission & Transmission Terminated"),
    n("Control & Tunnel Vision", qty=2),
    n("Pulsar Skate"),
    n("I'll Take The Leader"),
    n("Escape Pod", True, qty=2),
    n("Luke Skywalker", True),
    n("Houjix"),
    n("BoShek's Modified Freighter"),
    n("It's A Hit!"),
    n("Han With Heavy Blaster Pistol"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Melas", True, qty=2),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Mirax Terrik"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Han's Toolkit", True),
    n("Scrambled Transmission", True),
    n("Alternatives To Fighting"),
    n("Corellia", True),
    n("It's A Trap!"),
    n("Draw Their Fire"),
    n("Sabotage", True),
    n("Wedge Antilles", True),
    n("Revealed"),
    n("K'lor'slug", True),
    n("Han Solo, Courageous Smuggler"),
    n("BoShek, Brash Smuggler"),
    n("Honor Of The Jedi"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Kessel"),
    n("Chewie, Enraged"),
    n("Falcon Parts"),
    n("Talon Karrde", qty=2),
    n("Dash Rendar"),
    n("Millennium Falcon"),
    n("Rycar Ryjerd", True),
    n("Spaceport Docking Bay"),
    n("Chewbacca, Protector"),
    n("Life Debt"),
    n("Sergeant Bruckman", True),
    n("Phylo Gandish"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Another Pathetic Lifeform", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Ghhhk"),
    n("Victory", qty=2),
    n("General Nevar"),
    n("Rogue Shadow"),
    n("Grand Admiral Thrawn"),
    n("Juno Eclipse, Black Leader"),
    n("Endor"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Push", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Blockade Flagship: Bridge"),
    n("Dr. Evazan & Ponda Baba"),
    n("Trophy Of A Kill", qty=2),
    n("Kir Kanos With Force Pike"),
    n("A Sith's Weapon"),
    n("Blast Door Controls"),
    n("Force Field", True, qty=2),
    n("Revenge Of The Sith"),
    n("Naboo: Theed Palace Generator Core"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Darth Vader's Lightsaber"),
    n("Elis Helrot"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Battle Droid Squad", qty=2),
    n("Sniper & Dark Strike"),
    n("Dengar With Blaster Carbine", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Garindan", True),
    n("Imperial Justice", True),
    n("Blockade Flagship: Hallway"),
    n("Force Lightning"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
