#!/usr/bin/env python3
"""2015 European Championship Day 2: Kevin Jaap (place 30).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p27 DS / p28 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Kevin Jaap"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2015 European Championship Kevin Jaap LS.png"
DS_SCAN = "2015 European Championship Kevin Jaap DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #30 (circled). Forms signed 'Kevin Jaap', no username, no deck names. DS 1:3, LS 1:3."
)
LS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Main = 59: line 48 Blaster Deflection crossed out (line 49 ditto of it kept as 1 Blaster Deflection). "
    "Posted Sanity and Compassion dested Plead My Case To The Senate / Sanity And Compassion. "
    "Posted Artoo (V box) kept. Posted Coruscant JC dested Coruscant: Jedi Council Chamber. "
    "Posted Senate Hovercam (sheet 'Senate Mixwercam') dested Senate Hovercam. Posted Ki-Adi Mundi dested Ki-Adi-Mundi. "
    "Posted Yoda, Master Of dested Yoda, Master Of The Force. Posted Obi One + Radiant VII dested Obi-Wan In Radiant VII. "
    "Posted Nar Shadda dested Nar Shaddaa. Posted Luke Skywalker J/K x4 dested Luke Skywalker, Jedi Knight. "
    "Posted Near/Hear Me Baby x2 dested Hear Me Baby, Hold Together. Posted Antilles Manuever dested Antilles Maneuver. "
    "Posted Corran in Rouge 9 dested Corran Horn In Rogue 9. Posted Green Leader in dested Green Leader In Green Squadron 1. "
    "Posted Yarue dested Yarua. Posted Lando Cal Scoundrel x2 dested Lando Calrissian, Scoundrel. "
    "Posted Gold Leader in Gold 1 dested Gold Leader In Gold 1. Posted Anikin Skywalker PL dested Anakin Skywalker, Padawan Learner. "
    "Posted Coruscant NC dested Coruscant: Night Club. Posted Draw There Fire dested Draw Their Fire. "
    "Posted X-wing laser cann dested X-wing Laser Cannon. Posted Sorry about + BP dested Sorry About The Mess & Blaster Proficiency. "
    "Posted Quigon + stick x2 dested Qui-Gon Jinn With Lightsaber. Posted R 3PO dested R-3PO (Ar-Threepio). "
    "Posted A Jedis Concentration x2 dested A Jedi's Concentration. Posted Lukes stick / Lukes light saber dested Luke's Lightsaber. "
    "Posted Control + TV dested Control & Tunnel Vision. Posted Han, Chewie + Falcon dested Han, Chewie, And The Falcon. "
    "Posted What you trying to dested What're You Tryin' To Push On Us?. "
    "REVIEWED: CONFIRM line 50 \"PLEA MY COURT?\" dested Plea To The Court (political Effect in Plead My Case deck). "
    "Posted Wedge in Red 1 dested Wedge In Red Squadron 1. Posted Green in Green 1 dested Green Squadron 1. "
    "Posted 3PO parts dested Threepio With His Parts Showing. Posted Horox Ryyder kept. Posted Leia, RP dested Leia, Rebel Princess. "
    "Shield 3 'Your Insight No Longer' dested Your Insight Serves You Well. Posted Yavin Sentry kept. "
    "Posted Do Do Not dested Do, Or Do Not. Posted Goldon Rod dested Goldenrod."
)
DS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Line 1 Knowledge And Defense (V) box partially marked, taken as (V). "
    "Posted Bring Him Before Me dested Bring Him Before Me / Take Your Father's Place. "
    "Posted Omni Box + Its Worse dested Ommni Box & It's Worse. Posted We Must Accelerate Our x3 dested We Must Accelerate Our Plans. "
    "Posted A Dark Time / A Dark Time For (V boxes) dested A Dark Time For The Rebellion x2. "
    "Posted Control + SFS dested Control & Set For Stun. Posted Black 6 (V box) kept. "
    "Posted Masterfull Move + EO dested Masterful Move & Endor Occupation. Posted Blockade FS Hallway dested Blockade Flagship: Hallway. "
    "Posted Ability Ability x3 dested Ability, Ability, Ability (one card, one line). "
    "Posted Insignificant Rebellion kept. Posted Maul Sith Infiltrator x2 dested Maul's Sith Infiltrator. "
    "Posted Kuat Drive Yards (V box) kept. Posted Vaders Shuttle dested Vader's Personal Shuttle. "
    "Posted Ghhhk kept. Posted Short Range Fighters kept as written. "
    "Posted Turn It Off dested Turn It Off! Turn It Off!. Posted Slave One (V box) dested Slave I (V). "
    "Posted Imbalance + K S dested Imbalance & Kintan Strider. Posted Black Sun Fleet x3 kept. "
    "Posted Darth Vader + Stick dested Darth Vader With Lightsaber. Posted Ellis Helrot dested Elis Helrot. "
    "REVIEWED: AS-WRITTEN line 46 \"Bump\" (clearly written BUMP; no such card, Bubo was a guess). Posted Prepared Deff dested Prepared Defenses. "
    "Posted Admiral Ozzel kept. Posted Boba Fett Bounty H dested Boba Fett, Bounty Hunter. "
    "Posted Stormtrooper Gar dested Stormtrooper Garrison. Posted Dengar with Blaster (V box) dested Dengar With Blaster Carbine. "
    "Posted Emperor Palpatine kept. Posted Death Star 2 TM Room dested Death Star II: Throne Room. "
    "Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "REVIEWED: CONFIRM shield 14 \"COWARD\" scrawl dested Come Here You Big Coward (only fitting DS shield; Bukkehave also writes \"Coward\"). "
    "Posted Well Let Fate Decide dested We'll Let Fate-a Decide, Huh?."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Artoo", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Senate Hovercam"),
    n("Wokling"),
    n("A New Secret Base"),
    n("Like My Father Before Me", True),
    n("Ki-Adi-Mundi", True),
    n("Yoda, Master Of The Force"),
    n("Obi-Wan In Radiant VII"),
    n("Nar Shaddaa"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Hear Me Baby, Hold Together", True, qty=2),
    n("We're Doomed"),
    n("Antilles Maneuver"),
    n("Corran Horn In Rogue 9", True),
    n("Were You Looking For Me?"),
    n("Green Leader In Green Squadron 1", True),
    n("Yarua"),
    n("Luke's Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Gold Leader In Gold 1", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Coruscant: Night Club", True),
    n("Draw Their Fire"),
    n("X-wing Laser Cannon"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Mas Amedda"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("R-3PO (Ar-Threepio)", True),
    n("Escape Pod", True),
    n("Might Of The Republic", qty=2),
    n("A Jedi's Concentration", qty=2),
    n("Senator Palpatine"),
    n("Control & Tunnel Vision"),
    n("Han, Chewie, And The Falcon"),
    n("What're You Tryin' To Push On Us?"),
    n("Blaster Deflection"),
    n("Plea To The Court"),
    n("Wedge In Red Squadron 1"),
    n("Green Squadron 1"),
    n("Heading For The Medical Frigate"),
    n("Threepio With His Parts Showing"),
    n("Horox Ryyder"),
    n("Houjix"),
    n("Leia, Rebel Princess"),
    n("Liana Merian"),
    n("Fly Casual"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Affect Mind"),
    n("The Republic No Longer Functions"),
    n("Your Insight Serves You Well"),
    n("Yavin Sentry"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Goldenrod"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Ommni Box & It's Worse"),
    n("Tatooine"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Grand Moff Tarkin"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun"),
    n("Black 6", True),
    n("Masterful Move & Endor Occupation"),
    n("Blockade Flagship: Hallway"),
    n("Your Destiny"),
    n("Ability, Ability, Ability"),
    n("Insignificant Rebellion"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Darth Maul", qty=2),
    n("Endor Shield", True),
    n("Combat Response", True),
    n("Kuat Drive Yards", True),
    n("Vader's Personal Shuttle", True),
    n("Ghhhk"),
    n("Short Range Fighters"),
    n("Expand The Empire"),
    n("Darth Vader", True, qty=2),
    n("Imperial Decree", True),
    n("Turn It Off! Turn It Off!", True),
    n("Close Call", True),
    n("Slave I", True),
    n("Wooof", True),
    n("Dark Maneuvers", qty=2),
    n("Count Dooku"),
    n("Imbalance & Kintan Strider", True),
    n("Force Push", True),
    n("Black Sun Fleet", qty=3),
    n("P-59"),
    n("Darth Vader With Lightsaber"),
    n("Jango Fett"),
    n("Elis Helrot"),
    n("Bump"),
    n("Prepared Defenses"),
    n("No Escape"),
    n("Arica"),
    n("Admiral Ozzel"),
    n("Elis In Hinthra"),
    n("Boba Fett, Bounty Hunter"),
    n("Stormtrooper Garrison"),
    n("Dengar With Blaster Carbine", True),
    n("Emperor Palpatine"),
    n("Death Star II: Throne Room"),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever"),
    n("Vote Of No Confidence"),
    n("Do They Have A Code Clearance?"),
    n("Resistance"),
    n("Firepower"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Fanfare"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture"),
]
DS_ADD = []
