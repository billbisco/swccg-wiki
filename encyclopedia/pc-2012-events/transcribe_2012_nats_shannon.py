#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Kevin Shannon.

Source: 2012NationalsDay1.pdf pages 68–69 (handwritten 2010 Xerox, 12 shields).
p68 Dark / p69 Light Name Shannon Username blank dested Kevin Shannon analog leftover
2013 Alderaan / 2013 Worlds / 2013 SoCal / 2014 TMW / 2014 MPC.
Pack pages/Kevin_Shannon.wiki. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 69
DS_PAGE = 68
LS_SCAN = "2012 US Nationals Day 1 Kevin Shannon LS.png"
DS_SCAN = "2012 US Nationals Day 1 Kevin Shannon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover 2013 Alderaan. "
    "Username blank. Event Name Nats. Do not dest as a new person."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover 2013 Alderaan. "
    "Username blank. LIGHT checked. Event Name Nats. Deck Name blank. "
    "LS_START Infiltration / Unlikely Allies analog leftover Nelson. "
    "Light 60 dested analog leftover Nelson Infiltration (same 60). "
    "Line 40 Let The Wookiee Win True second copy analog leftover Nelson unique overcount. "
    "Boeshh dested Boushh analog leftover Nelson x2. "
    "Flash Of Insight dested Flash Of Insight True analog leftover Nelson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Nelson IN THE 60. "
    "Shield 12 There Is Another dested analog leftover Nelson. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Shannon dested Kevin Shannon analog leftover 2013 Alderaan. "
    "Username blank. DARK checked. Event Name Nats. Deck Name blank. "
    "DS_START Ral Ops / This Side Is So Good dested Ralltiir Operations / In The Hands Of The Empire analog leftover dual-title. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation analog leftover. "
    "Imperial Just-ASS dested Imperial Justice True analog leftover. "
    "Admiral Ozzel-nator dested Admiral Ozzel analog leftover. "
    "Embrace Combo dested Embrace Your Hatred analog leftover dest-as-written slang. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith analog leftover. "
    "The Mandalorian, FOF dested Jango Fett, The Assassin analog leftover TMW Shannon. "
    "Sith Bombardment True + empty stay separate. "
    "Lt. Commander Arden dested Lieutenant Commander Arden Lace analog leftover. "
    "Ice Heart dested Ysanne Isard analog leftover. "
    "SSPT dested Something Special Planned For Them True analog leftover Fernando. "
    "Darth Vader, Betrayer dested Darth Vader, Betrayer Of Jedi analog leftover. "
    "Endor the Best System dested Endor analog leftover. "
    "Boba, Prepared Hunter dested Boba Fett, Prepared Hunter analog leftover TMW Shannon. "
    "WAYTTT dested Why Didn't You Tell Me? analog leftover. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Line 41 We Haven't Lost Much Yet dested He Hasn't Come Back Yet analog leftover. "
    "Shield TINT dested There Is No Try analog leftover. "
    "Shield Coward dested Come Here You Big Coward analog leftover. "
    "Shield YCNHF dested You Cannot Hide Forever True analog leftover. "
    "Shield 12 Fanfare dested Fanfare True analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Nar Shaddaa: Undercity Street"),
    n("Scoundrel's Guild"),
    n("Mirax Terrik"),
    n("R2-D2", True),
    n("Chewbacca, Walking Carpet"),
    n("Let The Wookiee Win", True),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sergeant Doallyn", True),
    n("Third Sight", True),
    n("Han's Blaster, So Uncivilized"),
    n("Double Agent"),
    n("Booster In Pulsar Skate", qty=2),
    n("Landing Claw"),
    n("I Hope She's All Right"),
    n("Rebel Agent", qty=3),
    n("Rebel Agent's Blaster Rifle"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Imperial Atrocity", True),
    n("Corran Horn", qty=2),
    n("Houjix"),
    n("Seeking An Audience", True),
    n("Who's Born To Beat At Once", qty=2),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Escape Pod", True, qty=2),
    n("K'lor'slug", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Flash Of Insight", True),
    n("Let The Wookiee Win", True),
    n("Boushh", qty=2),
    n("Draw Their Fire"),
    n("Chewbacca's Bowcaster"),
    n("Anakin's Lightsaber", True),
    n("Booster's Star Destroyer"),
    n("Imperial Navigation Charts"),
    n("I Can't Believe He's Gone", True),
    n("Obi-Wan In Radiant VII"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Chewbacca, Walking Carpet"),
    n("Scoundrel's Trick"),
    n("Scoundrel's Ingenuity"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Bravado"),
    n("Heading For The Medical Frigate"),
    n("A Good Blaster At Your Side"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("There Is Another"),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Blizzard 1", True),
    n("Arica"),
    n("Masterful Move & Endor Occupation"),
    n("Imperial Justice", True),
    n("Admiral Ozzel"),
    n("Embrace Your Hatred"),
    n("Special Delivery", True),
    n("Outflank", True),
    n("Victory", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jango Fett, The Assassin"),
    n("Sith Bombardment", True),
    n("Sith Bombardment"),
    n("Emperor Palpatine", qty=2),
    n("Lieutenant Commander Arden Lace"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Spaceport Prefect's Office"),
    n("Imperial Barrier"),
    n("Kashyyyk"),
    n("General Nevar"),
    n("Blizzard 4", True),
    n("Imperial Command", qty=2),
    n("Tempest 1"),
    n("Spaceport Street"),
    n("2 FMT"),
    n("Emperor's Shuttle"),
    n("Close Call", True),
    n("A Dark Time For The Rebellion", True),
    n("Young Skywalker"),
    n("Colonel Davod Jon"),
    n("Slave I, Symbol Of Fear"),
    n("Ghhhk"),
    n("Search And Destroy"),
    n("Grand Moff Tarkin", True),
    n("Ralltiir: Spaceport Prefabricated District"),
    n("He Hasn't Come Back Yet"),
    n("General Veers", True),
    n("Gerendel", True, qty=2),
    n("Cloud City: Security Tower", True),
    n("Blizzard 2", True),
    n("Something Special Planned For Them", True),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Endor"),
    n("Boba Fett, Prepared Hunter"),
    n("Spaceport Docking Bay"),
    n("Ysanne Isard"),
    n("Imperial Propaganda", True),
    n("Grand Admiral Thrawn"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("We'll Call It Even", True),
    n("Why Didn't You Tell Me?"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Abyss"),
    n("Firepower"),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
]
DS_ADD = []
