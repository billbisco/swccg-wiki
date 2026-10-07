#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Wayne Cullen.

Source: MPC-2014-Day-1-Main-Event.pdf pages 35–36 (2013 form, 15 shields).
Username KissmyWookiee.
"""
from __future__ import annotations

PLAYER = "Wayne Cullen"
USERNAME = "KissmyWookiee"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 35
DS_PAGE = 36
LS_SCAN = "2014 Match Play Championship Day 1 Wayne Cullen LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Wayne Cullen DS.png"
LS_DECK_NAME = "Mr. Smith goes to Washington"
DS_DECK_NAME = "Spicy Sarumans"
NOTE = "Printed 2013 Xerox form."
LS_NOTE = (
    "Printed 2013 Xerox. Username KissmyWookiee. LIGHT checked. Deck Mr. Smith goes "
    "to Washington. Plead my case dested Plead My Case To The Senate / Sanity And "
    "Compassion. Lando, unlikely hero dested Lando Calrissian, Unlikely Hero. Luke SITF "
    "dested Luke Skywalker, Strong In The Force. Bail, father of rebellion dested Bail "
    "Organa. SATM & blaster prof dested Sorry About The Mess & Blaster Proficiency. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. Heading for the medical "
    "dested Heading For The Medical Frigate. Artoo in red 5 dested Artoo-Detoo In Red 5. "
    "Unique overcounts sheet-accurate (Mace Windu (V) x2, Obi-Wan Kenobi (V) x2, Luke "
    "Skywalker, Strong In The Force x3, Bail Organa x3, Might Of The Republic x3, Rebel "
    "Leadership (V) x3, Sense x2). (V) from checkbox."
)
DS_NOTE = (
    "Printed 2013 Xerox. Username Kissmywookiee. DARK checked. Deck Spicy Sarumans. "
    "Kessel line 1; Spice Mine Operations line 55 dested Spice Mine Operations. Jango "
    "fett, the assassin dested Jango Fett, The Assassin. Dr. E & ponda dested Dr. Evazan "
    "& Ponda Baba. 4-lom with gun dested 4-LOM With Concussion Rifle. Galen marek dested "
    "Galen Marek, Starkiller. Darth maul with saber dested Darth Maul With Lightsaber. "
    "Kessel survelence system dested Kessel (unique overcount). Ni chumba na dested Ni "
    "Chuba Na??. Sniper & dak strike dested Sniper & Dark Strike. Short range & watch "
    "your back dested Short Range Fighters & Watch Your Back!. Moruth Doole dested "
    "Moruth Doole, Kessel Administrator. Spice mine sites dested Kessel: Spice Mines - "
    "Administrator's Office / Extraction Facility / Prison. Galen's lightsaber dested "
    "Galen's Lightsaber, Vader's Gift. Slave I, symbol of fear dested Slave I, Symbol Of "
    "Fear. Unique overcounts sheet-accurate (Count Dooku x2, Lord Sidious x2, Galen Marek, "
    "Starkiller x3, Darth Maul With Lightsaber x2, Sense x2, Sonic Bombardment (V) x3, "
    "Short Range Fighters & Watch Your Back! x3, Force Field (V) x2, Kessel x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("General Airen Cracken"),
    n("Corran Horn"),
    n("General Solo", True),
    n("Admiral Ackbar", True),
    n("Chewbacca, Protector"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Senator Mon Mothma"),
    n("Bail Organa", qty=3),
    n("Senator Leia Organa"),
    n("Senator Padme Amidala"),
    n("Mas Amedda"),
    n("Luke's Bionic Hand"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Senate Hovercam"),
    n("Strike Planning"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("Much To Learn, You Still Have"),
    n("Imperial Atrocity", True),
    n("So This Is How Liberty Dies"),
    n("Anger, Fear, Aggression", True),
    n("Sense", qty=2),
    n("Might Of The Republic", qty=3),
    n("Nabrun Leids"),
    n("Rebel Leadership", True, qty=3),
    n("Grimtassh"),
    n("Jedi Levitation", True),
    n("Blaster Deflection"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Alter", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Heading For The Medical Frigate"),
    n("Kashyyyk: Forest Depths"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant"),
    n("Home One"),
    n("Lady Luck"),
    n("Artoo-Detoo In Red 5"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("The Professor", True),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Moruth Doole, Kessel Administrator"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Count Dooku", qty=2),
    n("Lord Sidious", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Kessel"),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Presence Of The Force"),
    n("I'll Take Them Myself"),
    n("Blaster Rack", True),
    n("Ni Chuba Na??", True),
    n("Imperial Justice", True),
    n("Gift Of The Master"),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
    n("Force Push", True),
    n("You Are Beaten"),
    n("Sniper & Dark Strike"),
    n("Combat Readiness", True),
    n("Dark Maneuvers"),
    n("Sense", qty=2),
    n("Cold Feet", True),
    n("Blow Parried"),
    n("Imperial Barrier"),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True),
    n("Sonic Bombardment", True, qty=3),
    n("Stop Motion", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Alter", True),
    n("Force Lightning"),
    n("Force Field", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Close Call", True),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Prison"),
    n("Spice Mine Operations"),
    n("Slave I, Symbol Of Fear"),
    n("Sidious' Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Force Field", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("After Her!", True),
]
DS_ADD = []
