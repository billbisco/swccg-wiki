#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Brian Herold.

Source: 2012NationalsDay1.pdf pages 30–31 (handwritten 2010 Xerox, 12 shields).
Name Brian Herold dested Brian Herold analog leftover 2013 Worlds/MPC/TMW/SoCal.
p30 Light Hidden Base. p31 Dark Combat Readiness.
Username Light AirDog 2003 / Dark Kevbezz2.
Do not dest as Aaron Nelson. Do not dest as a new person.
Pack player-stubs/Brian_Herold.wiki existing stub.
"""
from __future__ import annotations

PLAYER = "Brian Herold"
LS_USERNAME = "AirDog 2003"
DS_USERNAME = "Kevbezz2"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 30
DS_PAGE = 31
LS_SCAN = "2012 US Nationals Day 1 Brian Herold LS.png"
DS_SCAN = "2012 US Nationals Day 1 Brian Herold DS.png"
LS_DECK_NAME = "HB MonCals"
DS_DECK_NAME = "If you wanna be my luvah, you gotta get with my friends"
NOTE = "Handwritten 2010 Xerox. Name Brian Herold. Username Light AirDog 2003 Dark Kevbezz2."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Herold dested Brian Herold analog leftover 2013. "
    "Username AirDog 2003. LIGHT checked. Deck Name HB MonCals. "
    "Event Date 6/9/12 Event Name Livin' it up at the Days Inn. "
    "Do not dest as Aaron Nelson. Do not dest as a new person. "
    "Do not rewrite 2012 MPC leftover Yavin 4 / Agents Of Black Sun. "
    "Hidden Base True dested Hidden Base / Systems Will Slip Through Your Fingers True analog leftover light_frank. "
    "Tatooine (Coruscant) dested analog leftover Cullen. "
    "Rebel Cell Hidden Lando Site dested Rebel Cell - Hidden Landing Site analog leftover light_frank. "
    "Unchartered Settlements dested Uncharted Settlements analog leftover light_frank. "
    "Heading 4 The Medical Frigate dested Heading For The Medical Frigate analog leftover. "
    "Colo Claw Fish dested analog leftover TMW Shaw. "
    "Wokling True dested analog leftover. "
    "Superficial Damage True dested analog leftover. "
    "Commander Wedge Antilles True dested analog leftover Jellison. "
    "Commander Luke Skywalker True dested analog leftover Kinser. "
    "Roche True dested Roche analog leftover Hidden Base. "
    "Nar Shaddaa dested analog leftover. "
    "Rebel Cell Monitoring Station dested Rebel Cell - Monitoring Station analog leftover Jankowski. "
    "Rebel Cell Situation Room dested Rebel Cell - Situation Room analog leftover. "
    "Home 1 dested Home One analog leftover Hanson. "
    "Han, Chewie, & The Falcon True dested Han, Chewie, And The Falcon True analog leftover Booker. "
    "Blue Squadron B-wing x6 unique overcount sheet-accurate. "
    "Sandspeeder x8 unique overcount sheet-accurate. "
    "Dual Laser Cannons dested Dual Laser Cannon True analog leftover 2012 MPC Herold. "
    "Enhanced Proton Torpedoes True dested analog leftover 2012 MPC Herold. "
    "Incom Corp & Koensayer Manufacturing dested Incom Corporation & Koensayr Manufacturing analog leftover combo. "
    "Slayn & Korpil Phacilittes dested Slayn & Korpil Facilities analog leftover. "
    "Hindsight True dested analog leftover Wirfs. "
    "Imp Atrocity dested Imperial Atrocity True analog leftover TMW Herold. "
    "Stay Sharp! dested analog leftover Grant. "
    "Noooooooo! dested NOOOOOOOOOOOO! True analog leftover Heine. "
    "Dash In Rogue 10 dested analog leftover Banger. "
    "AFA dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Simple Trix & Nonsense dested Simple Tricks And Nonsense analog leftover TMW Herold. "
    "He Can Go About His Business True dested analog leftover TMW Herold. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Herold dested Brian Herold analog leftover 2013. "
    "Username Kevbezz2. DARK checked. Deck Name If you wanna be my luvah, you gotta get with my friends. "
    "Event Date 6/9/12 Event Name Nationals? or Continentals?? The one at Minnesota Days Inn. "
    "Do not dest as Aaron Nelson. Do not dest as a new person. "
    "Combat Readiness True dested Combat Readiness / Full Scale Alert True analog leftover Richards. "
    "Kessel Spice Mines Admin Office dested Kessel: Spice Mines - Administrator's Office analog leftover 2013 MPC Herold. "
    "Gift of The Master dested Gift Of The Master analog leftover TMW Herold. "
    "I'll Take Them Myself dested analog leftover Burgt. "
    "Kessel Spice Mines Prison dested Kessel: Spice Mines - Prison analog leftover Finley. "
    "Kessel Spice Mines Extraction Phacility dested Kessel: Spice Mines - Extraction Facility analog leftover Finley. "
    "CC: Security Tower dested Cloud City: Security Tower True analog leftover TMW Herold. "
    "Admiral Palleon dested Admiral Pellaeon analog leftover Pinto. "
    "The Mandalorian, Father of Fart dested Jango Fett, The Assassin analog leftover. "
    "Spice Mines Administrator dested Moruth Doole, Kessel Administrator analog leftover 2013 MPC Herold. "
    "Dr. E & Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover 2013 Worlds Herold. "
    "4-Lom with Concussion Rifle dested 4-LOM With Concussion Rifle True analog leftover 2012 MPC Herold. "
    "Darth Vader w saber dested Darth Vader With Lightsaber analog leftover 2013 MPC Herold. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi analog leftover. "
    "Darth Maul, Young Apprentice dested analog leftover Booker. "
    "Slave 1, Symbol of Fear dested Slave I, Symbol Of Fear analog leftover TMW Herold. "
    "Retraining Belt dested Restraining Bolt analog leftover 2012 MPC Herold. "
    "Kessel Surveillance System dested analog leftover Pinto. "
    "Maul's Double Bladed Lightsaber dested Maul's Double-Bladed Lightsaber analog leftover. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsaber analog leftover. "
    "Sidious' Lightsaber dested analog leftover Nelson. "
    "Much Anger In Him crossed dest Boba Fett, Prepared Hunter dested Boba Fett, Bounty Hunter analog leftover Anderson. "
    "Disarmed crossed dest Protocol Failure analog leftover. "
    "Sonic (the Hedgehog) Bombardment dested Sonic Bombardment True analog leftover unique overcount. "
    "MM & EO dested Masterful Move & Endor Occupation analog leftover Marlow. "
    "Sniper & Dark Strike dested analog leftover Alperstein. "
    "A Dark Time 4 The Rebellion dested A Dark Time For The Rebellion True analog leftover SAN. "
    "Control & Set 4 Stun dested Control & Set For Stun analog leftover 2012 MPC Herold. "
    "Knowledge & Defense dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Weapon of A Sith dested Weapon Of A Sith analog leftover TMW Herold. "
    "Shield 12 dested Come Here You Big Coward analog leftover 2013 MPC Herold. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Tatooine (Coruscant)"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Uncharted Settlements"),
    n("Heading For The Medical Frigate"),
    n("Colo Claw Fish"),
    n("Wokling", True),
    n("Superficial Damage", True),
    n("Corran Horn"),
    n("Commander Wedge Antilles", True, qty=2),
    n("Commander Luke Skywalker", True, qty=2),
    n("Roche", True),
    n("Nar Shaddaa"),
    n("Rebel Cell - Monitoring Station"),
    n("Rebel Cell - Situation Room"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Blue Squadron B-wing", qty=6),
    n("Sandspeeder", qty=8),
    n("Intruder Missile", qty=3),
    n("Dual Laser Cannon", True, qty=2),
    n("Enhanced Proton Torpedoes", True, qty=2),
    n("Tatooine Celebration", qty=2),
    n("Incom Corporation & Koensayr Manufacturing"),
    n("Slayn & Korpil Facilities"),
    n("Hindsight", True),
    n("Imperial Atrocity", True),
    n("Rebel Artillery"),
    n("Stay Sharp!", qty=2),
    n("Power Pivot", qty=3),
    n("T-47 Battle Formation"),
    n("Rebel Barrier", qty=2),
    n("NOOOOOOOOOOOO!", True, qty=2),
    n("Dash In Rogue 10"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Aim High"),
    n("Battle Plan", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
]
LS_ADD = []

DS_START = "Combat Readiness / Full Scale Alert"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness / Full Scale Alert", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Security Precautions"),
    n("Gift Of The Master"),
    n("I'll Take Them Myself"),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Cloud City: Security Tower", True),
    n("Admiral Pellaeon"),
    n("Jango Fett, The Assassin", qty=2),
    n("Garindan", True),
    n("Moruth Doole, Kessel Administrator"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Darth Vader With Lightsaber"),
    n("Darth Sidious", qty=2),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Darth Maul", qty=2),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Justifier"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Restraining Bolt"),
    n("Kessel Surveillance System"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Spice Mine Operations"),
    n("Disarmed"),
    n("Blaster Rack", True),
    n("Boba Fett, Bounty Hunter"),
    n("Protocol Failure"),
    n("Imperial Command"),
    n("You Are Beaten"),
    n("Sonic Bombardment", True, qty=3),
    n("Cold Feet", True),
    n("Force Field", True),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True),
    n("Sniper & Dark Strike"),
    n("Ghhhk"),
    n("Imperial Barrier"),
    n("Close Call", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun"),
    n("Sense", qty=2),
    n("Alter", True),
    n("Arica"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Abyss", True),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
]
DS_ADD = []
