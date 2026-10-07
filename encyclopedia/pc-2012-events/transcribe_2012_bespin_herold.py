#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Brian Herold.

Source: 2012BespinRegionals.pdf pages 25–26.
p25 Dark 2002 Print Form / p26 Light 2002 Print Form.
Name Brian Herold dested Brian Herold analog leftover 2012 Nats/TMW/MPC /
player-stubs/Brian_Herold.wiki. USERNAME blank (2002 form has no Username box).
Do not dest as Aaron Nelson. Do not dest 2012 Nats / TMW / MPC Herold 60s again.
Do not dest p12 as Brian Herold Bespin (AirDog 2003 is Nelson's handle).
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2012 Bespin Regionals Brian Herold LS.png"
DS_SCAN = "2012 Bespin Regionals Brian Herold DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p25 Dark 2002 Print Form / p26 Light 2002 Print Form. "
    "Name Brian Herold dested Brian Herold analog leftover 2012 Nats/TMW/MPC / "
    "player-stubs/Brian_Herold.wiki. USERNAME blank. "
    "p25 Event Bespin Regionals Date Some day in July Deck Title 17 Time Grand Slam Champ dested off article. "
    "p26 Event Bespin Sectionals Date ??? Deck Title The GOAT dested joke Event/Date/Deck Name off article "
    "analog leftover TMW Herold joke usernames; dest both as Bespin facing pair. "
    "Do not dest as Aaron Nelson. Do not dest 2012 Nats / TMW / MPC Herold 60s again. "
    "Do not dest p12 as Brian Herold Bespin."
)
LS_NOTE = (
    "2002 Print Form p26 Light. Name Brian Herold dested Brian Herold. USERNAME blank. "
    "Event Bespin Sectionals Date ??? Deck Title The GOAT dested joke off article. "
    "Infiltration dested Infiltration / Unlikely Allies analog leftover Schoenthal. "
    "Spaceport Scoundrel's Guild dested Scoundrel's Guild analog leftover Schoenthal. "
    "Chewbacca Walking Carpet dested Chewbacca, Walking Carpet analog leftover Nelson qty=2. "
    "Let That Wookiee Win dested Let The Wookiee Win True analog leftover qty=2. "
    "Han Solo (Not That) Innocent Scoundrel dested Han Solo, Innocent Scoundrel analog leftover Nelson qty=2. "
    "Corran Horny dest joke dest Corran Horn analog leftover qty=2. "
    "WW TBA O / WW TBA D dested We Wish To Board At Once analog leftover Schoenthal qty=2. "
    "Armed And Dangerous & Don't Get Cocky crossed dest skip analog leftover crossed without replacement. "
    "SATM & Blaster Prof dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "Han's Blaster, SUe dested Han's Blaster, So Uncivilized analog leftover Nelson. "
    "Lando Clan dested Lando Calrissian. Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover qty=2. "
    "Obi in Rad 7 dested Obi-Wan In Radiant VII analog leftover Nelson. "
    "Sea King An Audience dested Seeking An Audience True analog leftover. "
    "I Can't Believe That He's Gone dested I Can't Believe He's Gone True analog leftover. "
    "K'lor'slug True dested analog leftover. Anger, Fear, Aggression True IN THE 60. "
    "Unique 59 sheet-accurate (Armed crossed skip) shields 12."
)
DS_NOTE = (
    "2002 Print Form p25 Dark. Name Brian Herold dested Brian Herold. USERNAME blank. "
    "Event Bespin Regionals Date Some day in July Deck Title 17 Time Grand Slam Champ dested off article. "
    "Combat Readiness v dested Combat Readiness / Full Scale Alert True analog leftover Nats Herold. "
    "Kessel Starting Location dested Kessel analog leftover Nats Herold. "
    "Kessel: Spice Mines Administration Office dested Kessel: Spice Mines - Administrator's Office analog leftover. "
    "Spice Mines Administrator dested Moruth Doole, Kessel Administrator analog leftover Nats Herold. "
    "Mandalorian, Father of Farts dest joke dest Jango Fett, The Assassin analog leftover Atkin qty=2. "
    "Sonic (the hedgehog) Bombardment dested Sonic Bombardment True analog leftover Nats qty=3. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover qty=3. "
    "Darth Maul empty qty=2 kept separate from Darth Maul, Young Apprentice qty=2. "
    "Garidan dested Garindan True analog leftover. Admiral Palleon dested Admiral Pellaeon analog leftover. "
    "Gift Of The Master dested analog leftover Nats. 4-LOM With Concussion Rifle True dested analog leftover. "
    "Knowledge And Defense True IN THE 60. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck"),
    n("Scoundrel's Luck: Ingenuity"),
    n("Scoundrel's Luck: Charm"),
    n("Scoundrel's Luck: Bravado"),
    n("Heading For The Medical Frigate"),
    n("A Good Blaster At Your Side"),
    n("Sai'torr Kal Fas", True),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Corran Horn", qty=2),
    n("Houjix"),
    n("Booster In Pulsar Skate", qty=2),
    n("Scoundrel's Guild"),
    n("Mirax Terrik"),
    n("Booster's Star Destroyer"),
    n("Boushh", qty=2),
    n("I Hope She's All Right"),
    n("Nar Shaddaa: Undercity Street"),
    n("Sergeant Doallyn", True),
    n("Lando Calrissian"),
    n("R2-D2", True),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Imperial Atrocity", True),
    n("Draw Their Fire"),
    n("Rebel Agent", qty=3),
    n("Han's Blaster, So Uncivilized"),
    n("Leia's Blaster Rifle"),
    n("Hindsight", True),
    n("Chewbacca's Bowcaster"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("I Can't Believe He's Gone", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Flash Of Insight", True),
    n("Obi-Wan In Radiant VII"),
    n("Double Agent"),
    n("Rebel Agent's Blaster Rifle"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Seeking An Audience", True),
    n("Escape Pod", True, qty=2),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("K'lor'slug", True),
    n("Imperial Navigation Charts"),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("The Professor", True),
    n("Jabba's Prize", True),
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
    n("Ghhhk"),
    n("Boba Fett, Prepared Hunter"),
    n("Arica"),
    n("Sonic Bombardment", True, qty=3),
    n("Kessel Surveillance System"),
    n("Close Call", True),
    n("Control & Set For Stun"),
    n("Alter", True),
    n("Darth Sidious", qty=2),
    n("Kessel: Spice Mines - Prison"),
    n("Spice Mine Operations"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Sniper & Dark Strike"),
    n("Moruth Doole, Kessel Administrator"),
    n("Maul's Sith Infiltrator"),
    n("Jango Fett, The Assassin", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Imperial Command"),
    n("Lightsaber Deficiency", True),
    n("Sense", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Disarmed"),
    n("Grievous' Lightsabers"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Slave I, Symbol Of Fear"),
    n("Cold Feet", True),
    n("Garindan", True),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Darth Vader With Lightsaber"),
    n("Protocol Failure"),
    n("You Are Beaten"),
    n("Blaster Rack", True),
    n("Cloud City: Security Tower", True),
    n("Sidious' Lightsaber"),
    n("Justifier"),
    n("Weapon Levitation"),
    n("Force Field", True),
    n("Darth Maul", qty=2),
    n("Admiral Pellaeon"),
    n("Imperial Barrier"),
    n("Tarkin's Bounty", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("Firepower", True),
]
DS_ADD = []
