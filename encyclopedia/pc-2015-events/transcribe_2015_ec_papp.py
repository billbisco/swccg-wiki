#!/usr/bin/env python3
"""2015 European Championship Day 2: Tamas Papp (place 26).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p19 DS / p20 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Tamas Papp"
USERNAME = "Yoda 007"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2015 European Championship Tamas Papp LS.png"
DS_SCAN = "2015 European Championship Tamas Papp DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #26. Forms signed 'PAPP, Tamas', event 'EC', date 10/17/15, username 'Yoda 007' on both "
    "(standings: Tamas (yoda007) Papp). DS deck name 'Check out Emil's Dark at Worlds', DS 1:3. "
    "LS deck name 'TRM by World Champs', LS 2:2."
)
LS_NOTE = (
    "Form 60 lines + 15 shields. START Yavin 4: Massassi Throne Room (sheet 'Y4:TR'). "
    "Posted H4TMF dested Heading For The Medical Frigate. Posted LS JK x4 dested Luke Skywalker, Jedi Knight. "
    "Posted Leia, RP dested Leia, Rebel Princess. Posted Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "REVIEWED: AS-WRITTEN line 15 \"DTF\" (Draw Their Fire vs Don't Forget The Droids undecidable). "
    "Posted Luke Skywalker (V box) kept as Luke Skywalker (V). "
    "Posted AWRI combo dested All Wings Report In & Darklighter Spin. Posted Corran Horn x2 kept. "
    "Posted Artoo in Red 5 x2 dested Artoo-Detoo In Red 5. Posted Mace's LS dested Mace Windu's Lightsaber. "
    "Posted Qui-Gon's LS dested Qui-Gon Jinn's Lightsaber. Posted Anakin's LS dested Anakin's Lightsaber. "
    "Posted SATM & BP dested Sorry About The Mess & Blaster Proficiency. Posted HCF dested Han, Chewie, And The Falcon. "
    "Posted Cor: JCC dested Coruscant: Jedi Council Chamber. Posted Threepio w/ Parts Showing dested Threepio With His Parts Showing. "
    "Posted Anakin Skywalker, PL x2 dested Anakin Skywalker, Padawan Learner. "
    "Posted OOC & TT dested Out Of Commission & Transmission Terminated. "
    "Posted Do Or Do Not dested Do, Or Do Not. Posted Planetary Defences dested Planetary Defenses. "
    "Unique overcounts sheet-accurate (LSJK x4, Wesa Gotta Grand Army x4)."
)
DS_NOTE = (
    "Form 60 lines + 15 shields. START Endor Operations / Imperial Outpost. "
    "Posted D*2 dested Death Star II; D*2: Coolant Shaft / Reactor Core / Capacitor dested Death Star II: Coolant Shaft / Reactor Core / Capacitors. "
    "REVIEWED: CONFIRM line 11 \"WMAOP\" (M looks like H) dested We Must Accelerate Our Plans. "
    "Posted Z in MH dested Zuckuss In Mist Hunter. Posted DV with LS dested Darth Vader With Lightsaber. "
    "Posted BF BH dested Boba Fett, Bounty Hunter. Posted Imbalance & Kintan Strider kept. "
    "Posted Control & SFS dested Control & Set For Stun. "
    "REVIEWED: CONFIRM line 33 \"MM\" in Endor Ops dested Masterful Move & Endor Occupation. "
    "Posted That's Thing's Op dested That Thing's Operational. Posted Elis in Hinthra dested Elis In Hinthra. "
    "Posted Tatooine (EP1) dested Tatooine (Coruscant). "
    "REVIEWED: CONFIRM line 44 cursive \"Ghhhk\" dested Ghhhk. "
    "Posted Omni Box & It's Worse dested Ommni Box & It's Worse. "
    "REVIEWED: CONFIRM line 49 \"Black 6\" (6 looks like C) dested Black 6 (V Set 2, Jul 2015). Posted DV (Premiere) (V box) dested Darth Vader. "
    "Posted A Dark Time... x2 dested A Dark Time For The Rebellion. "
    "Posted SRF & WYB dested Short Range Fighters & Watch Your Back!. Posted GM Tarkin dested Grand Moff Tarkin. "
    "Posted Maul's Sith Infiltrator x2 kept. Posted YCHF dested You Cannot Hide Forever. "
    "Posted I Find Your Lack Of Faith Disturbing kept."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Like My Father Before Me"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Kiffex"),
    n("DTF"),
    n("Luke Skywalker", True),
    n("A Jedi's Concentration", qty=2),
    n("Honor Of The Jedi"),
    n("Speak With The Jedi Council", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("Houjix"),
    n("All Wings Report In & Darklighter Spin"),
    n("Under Attack"),
    n("Corran Horn", qty=2),
    n("Were You Looking For Me?", qty=2),
    n("Anakin's Lightsaber"),
    n("Tantive IV", True),
    n("Clash Of Sabers"),
    n("Master Qui-Gon", True, qty=2),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Free Ride & Endor Celebration"),
    n("Wesa Gotta Grand Army", qty=4),
    n("Escape Pod", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Mace Windu's Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Han, Chewie, And The Falcon"),
    n("Civil Disorder", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Threepio With His Parts Showing"),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Barrier"),
    n("Luke's Lightsaber"),
    n("Yoda, Keeper Of The Peace"),
    n("Out Of Commission & Transmission Terminated"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Your Ship?"),
    n("Goldenrod"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Planetary Defenses"),
    n("Only Jedi Carry That Weapon"),
    n("He Can Go About His Business"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Operational As Planned"),
    n("Combat Response", True),
    n("Death Star II"),
    n("Moff Jerjerrod"),
    n("Sense"),
    n("Death Star II: Coolant Shaft"),
    n("We Must Accelerate Our Plans"),
    n("Count Dooku"),
    n("Darth Maul", qty=2),
    n("Neimoidian Advisor", qty=2),
    n("Jango Fett"),
    n("Force Push", True),
    n("Stormtrooper Garrison"),
    n("Zuckuss In Mist Hunter"),
    n("Darth Vader With Lightsaber"),
    n("Endor Shield", True),
    n("Maul's Sith Infiltrator", qty=2),
    n("Arica"),
    n("Close Call", True),
    n("Image Of The Dark Lord", True),
    n("Boba Fett, Bounty Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Imbalance & Kintan Strider"),
    n("P-59"),
    n("Control & Set For Stun"),
    n("We Shall Double Our Efforts!"),
    n("Masterful Move & Endor Occupation"),
    n("Dark Maneuvers", qty=2),
    n("That Thing's Operational"),
    n("Elis In Hinthra"),
    n("Imperial Decree", True),
    n("Unsalvageable"),
    n("Tatooine (Coruscant)"),
    n("Black Sun Fleet", qty=3),
    n("Ghhhk"),
    n("No Escape"),
    n("Ommni Box & It's Worse"),
    n("Wooof", True),
    n("Death Star II: Reactor Core"),
    n("Black 6"),
    n("Darth Vader", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Surface Defense", True),
    n("Vader's Personal Shuttle", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Grand Moff Tarkin", True),
    n("Death Star II: Capacitors"),
    n("Admiral Ozzel"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Vote Of No Confidence"),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Resistance"),
]
DS_ADD = []
