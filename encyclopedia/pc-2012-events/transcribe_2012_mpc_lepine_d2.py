#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Cole Lepine.

Source: 2012mpcday2.pdf pages 13–14 (handwritten notebook 60s).
Name Cole Lepine dested Cole Lepine analog leftover. Username Clepines dested clepine analog leftover Day 1.
p13 Dark IO/IC (V) walkers. p14 Light WYS (V).
Do not dest as a new person. Do not rewrite Day 1 leftover Imperial Occupation / Watch Your Step.
Pack player-stubs/Cole_Lepine.wiki.
"""
from __future__ import annotations

PLAYER = "Cole Lepine"
USERNAME = "clepine"
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2012 Match Play Championship Day 2 Cole Lepine LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Cole Lepine DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten notebook 60 bound into 2012mpcday2.pdf."
LS_NOTE = (
    "Handwritten notebook. Name Cole Lepine dested Cole Lepine analog leftover. "
    "Username Clepines dested clepine analog leftover Day 1. Event MPC Day 2. LIGHT. "
    "Do not dest as a new person. Do not rewrite Day 1 leftover Watch Your Step. "
    "WYS (v) dested Watch Your Step / This Place Can Be A Little Rough True analog leftover Lepine IN THE 60 AND START. "
    "Corellia (v) dested analog leftover. "
    "Falcon (v) dested Millennium Falcon True analog leftover Day 1. "
    "Cap'n H->S dested Captain Han Solo analog leftover Day 1. "
    "The City dested Spaceport City analog leftover Day 1. "
    "HFTMF dested Heading For The Medical Frigate analog leftover IN THE 60. "
    "CEC (v) dested Corellian Engineering Corporation True analog leftover Day 1. "
    "I & AH dested Insurrection & Aim High analog leftover Day 1. "
    "Wokling (v) dested analog leftover. "
    "YGW (v) dested Yoda, Great Warrior True analog leftover Day 1 unique overcount. "
    "Wedge, RSL dested Wedge Antilles, Red Squadron Leader analog leftover Day 1. "
    "Dash R.(v) dested Dash Rendar True analog leftover Hodur. "
    "P. Reshad dested Palejo Reshad analog leftover Day 1. "
    "Mirax dested Mirax Terrik analog leftover Day 1. "
    "C. Horn and Mr. Horn dested Corran Horn analog leftover Day 1 unique overcount. "
    "Commando Slug (v) dested Commando Training & K'lor'slug True analog leftover Chu. "
    "S. Transmission (v) dested Scrambled Transmission True analog leftover Bordier. "
    "Merc Sunlet (v) dested analog leftover Day 1. "
    "Seeking (v) dested Seeking An Audience True analog leftover Day 1. "
    "M. Fades dested Menace Fades analog leftover Day 1. "
    "NQA (v) dested No Questions Asked True analog leftover Day 1 unique overcount. "
    "Houjix Combo dested Houjix & Out Of Nowhere analog leftover Foth. "
    "H2: DB dested Home One: Docking Bay analog leftover Day 1. "
    "The Guild (v) dested Spaceport Scoundrels Guild True analog leftover Day 1. "
    "The Street dested Spaceport Street analog leftover Day 1. "
    "The diamond Docking Bay dested Spaceport Docking Bay analog leftover Day 1. "
    "LTWW (v) dested Let The Wookiee Win True analog leftover unique overcount. "
    "HMB, HT (v) dested Hear Me Baby, Hold Together True analog leftover. "
    "Yub Yub, Commander (v) dested analog leftover Day 1. "
    "Corellian Retort (v) dested analog leftover Day 1. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin analog leftover Day 1. "
    "Desperate Reach (v) dested analog leftover Amato. "
    "Antman Combo (v) dested Antilles Maneuver & Rebel Reinforcements True analog leftover Day 1 unique overcount. "
    "Sense dested analog leftover Day 1. "
    "Antman (v) dested Antilles Maneuver True analog leftover Day 1. "
    "Boshek, BS (v) dested BoShek, Brash Smuggler True analog leftover Day 1. "
    "Lando C, Scoundrel dested Lando Calrissian, Scoundrel analog leftover Day 1. "
    "Chewie (v) dested Chewie True analog leftover Day 1. "
    "Leia (v) dested Princess Leia True analog leftover Day 1. "
    "Leia, RP dested Leia, Rebel Princess analog leftover Day 1. "
    "Atrocity (v) dested Imperial Atrocity True analog leftover Day 1 unique overcount. "
    "BIPS (v) dested Booster In Pulsar Skate True analog leftover Day 1. "
    "Spiral dested analog leftover Day 1. "
    "Tantive IV (v) dested analog leftover Day 1. "
    "Boshek's MLF (v) dested BoShek's Modified Freighter True analog leftover Harpster. "
    "Padmé Naberrie (v) dested analog leftover Day 1. "
    "Fallen Jedi (v) dested Maris Brood, Fallen Jedi True analog leftover Day 1. "
    "LSJK dested Luke Skywalker, Jedi Knight analog leftover Day 1 unique overcount. "
    "Sergeant Bruckman dested analog leftover Veasey. "
    "General Crix Madine dested analog leftover Jankowski. "
    "Rebel Leadership (v) dested analog leftover Chu. "
    "Obi-Wan Kenobi (v) dested analog leftover Alex W. "
    "AFA (v) dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "Shield Professor (v) dested The Professor True analog leftover Day 1. "
    "Shield Sentry (v) dested Yavin Sentry True analog leftover Day 1. "
    "Shield LKALOH (v) dested Let's Keep A Little Optimism Here True analog leftover Day 1. "
    "Shield OODN dested Do, Or Do Not analog leftover Day 1. "
    "Shield DDTA (v) dested Don't Do That Again True analog leftover Day 1. "
    "Shield Ultimatum dested analog leftover Day 1. "
    "Shield Weapons Display (v) dested analog leftover Day 1. "
    "Shield B. Plan dested Battle Plan analog leftover Day 1. "
    "Shield STAN (v) dested Simple Tricks And Nonsense True analog leftover Day 1. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover Day 1. "
    "Shield Chasm (v) dested analog leftover Day 1. "
    "Shield Jabba's Prize (v) dested analog leftover Day 1. "
    "Unique overcounts sheet-accurate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten notebook. Name Cole Lepine dested Cole Lepine analog leftover. "
    "Username Clepines dested clepine analog leftover Day 1. Event MPC Day 2. DARK. "
    "Do not dest as a new person. Do not rewrite Day 1 leftover Imperial Occupation. "
    "IO/IC (v) dested Imperial Occupation / Imperial Control True analog leftover Lepine IN THE 60 AND START. "
    "Hoth dested analog leftover. "
    "Hoth: IP (v) dested Hoth: Ice Plains True analog leftover. "
    "Hoth: MPG dested Hoth: Main Power Generators analog leftover. "
    "I. Decree empty and I. Decree (v) kept separate analog leftover. "
    "P. Def (v) dested Prepared Defenses True analog leftover IN THE 60. "
    "E. shield (v) dested Endor Shield True analog leftover. "
    "NCN?? (v) dested Ni Chuba Na?? True analog leftover. "
    "YMSYL dested You May Start Your Landing analog leftover. "
    "Stop Motion (v) dested analog leftover Brodsky. "
    "GMT (v) dested Grand Moff Tarkin True analog leftover Day 1 unique overcount. "
    "Omni Box & It's Worse dested Ommni Box & It's Worse analog leftover Day 1. "
    "He hasn't come back yet dested He Hasn't Come Back Yet analog leftover 2014 Tom H. "
    "The Sith Infiltrator dested Maul's Sith Infiltrator analog leftover Day 1. "
    "Victory (v) dested analog leftover unique overcount. "
    "ADTFTR (v) dested A Dark Time For The Rebellion True analog leftover Day 1 unique overcount. "
    "GA Thrawn dested Grand Admiral Thrawn analog leftover. "
    "TTMG dested Target The Main Generator analog leftover. "
    "Ad. Piett dested Admiral Piett analog leftover. "
    "Hoth: DP dested Hoth: Defensive Perimeter (3rd Marker) analog leftover. "
    "Hoth Mountains dested Hoth: Mountains (6th Marker) analog leftover. "
    "Darth Vader (v) dested Darth Vader, Dark Lord Of The Sith True analog leftover Day 1. "
    "The Igar (v) dested Commander Igar True analog leftover Day 1. "
    "WIAPN dested We're In Attack Position Now analog leftover Day 1 unique overcount. "
    "Darth Maul dested analog leftover. "
    "Veers (v) dested analog leftover. "
    "I. Propaganda (v) dested Imperial Propaganda True analog leftover. "
    "The Reach (v) dested Maarek Stele, The Emperor's Reach True analog leftover. "
    "Garindan (v) dested analog leftover unique overcount. "
    "Hoth Blockade (v) dested analog leftover. "
    "Image of The Dark Lord (v) dested Image Of The Dark Lord True analog leftover. "
    "Conquest (v) dested analog leftover Wirfs. "
    "G. Nevar (v) dested General Nevar True analog leftover. "
    "OTHACC? dested Do They Have A Code Clearance? analog leftover Day 1 IN THE 60. "
    "No Escape dested analog leftover. "
    "I. Command dested Imperial Command analog leftover unique overcount. "
    "Blizzard 2 (v) dested analog leftover. "
    "Tempest 1 CROSSED skipped. "
    "M. In Blizzard 6 (v) dested Marquand In Blizzard 6 True analog leftover Day 1. "
    "Blizzard 4 dested analog leftover. "
    "Control & SFS dested Control & Set For Stun analog leftover. "
    "AT-AT Cannon (v) dested analog leftover. "
    "Cold Feet (v) dested analog leftover. "
    "Flagship Executor dested analog leftover. "
    "B. Leader (v) dested Juno Eclipse, Black Leader True analog leftover. "
    "I. Justice (v) dested Imperial Justice True analog leftover. "
    "MM & EO dested Masterful Move & Endor Occupation analog leftover. "
    "Trample dested analog leftover unique overcount. "
    "Control (Ep. 1) dested Control analog leftover Anderson. "
    "Walker Garrison dested analog leftover. "
    "Blizzard 1 (v) dested analog leftover. "
    "K+D (v) dested Knowledge And Defense True analog leftover Murray IN THE 60. "
    "Shield IFYLOFD (v) dested I Find Your Lack Of Faith Disturbing True analog leftover. "
    "Shield AUG (v) dested A Useless Gesture True analog leftover. "
    "Shield Sentry (v) dested Death Star Sentry True analog leftover Baroni. "
    "Shield CHYBC dested Come Here You Big Coward analog leftover. "
    "Shield Resistance dested analog leftover. "
    "Shield YCHF (v) dested You Cannot Hide Forever True analog leftover. "
    "Shield Firepower (v) dested analog leftover. "
    "Shield Fanfare (v) dested analog leftover. "
    "Shield TINT dested There Is No Try analog leftover. "
    "Shield BO dested Battle Order analog leftover. "
    "Shield S. Plans dested Secret Plans analog leftover. "
    "Shield Allegations dested Allegations Of Corruption analog leftover. "
    "Unique overcounts sheet-accurate. Unique 59 sheet-accurate (Tempest 1 crossed skipped). Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Yoda, Great Warrior", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Dash Rendar", True),
    n("Palejo Reshad"),
    n("Mirax Terrik"),
    n("Corran Horn", qty=2),
    n("Commando Training & K'lor'slug", True),
    n("Scrambled Transmission", True),
    n("Merc Sunlet", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("No Questions Asked", True, qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Home One: Docking Bay"),
    n("Spaceport Scoundrels Guild", True),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Let The Wookiee Win", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Yub Yub, Commander", True),
    n("Corellian Retort", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Desperate Reach", True),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Sense"),
    n("Antilles Maneuver", True),
    n("BoShek, Brash Smuggler", True),
    n("Lando Calrissian, Scoundrel"),
    n("Chewie", True),
    n("Princess Leia", True),
    n("Leia, Rebel Princess"),
    n("Imperial Atrocity", True, qty=2),
    n("Booster In Pulsar Skate", True),
    n("Spiral"),
    n("Tantive IV", True),
    n("BoShek's Modified Freighter", True),
    n("Padmé Naberrie", True),
    n("Maris Brood, Fallen Jedi", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Sergeant Bruckman"),
    n("General Crix Madine"),
    n("Rebel Leadership", True),
    n("Obi-Wan Kenobi", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Imperial Decree"),
    n("Imperial Decree", True),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing"),
    n("Stop Motion", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("Ommni Box & It's Worse"),
    n("He Hasn't Come Back Yet"),
    n("Maul's Sith Infiltrator"),
    n("Victory", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Grand Admiral Thrawn"),
    n("Target The Main Generator"),
    n("Admiral Piett"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Commander Igar", True),
    n("We're In Attack Position Now", qty=2),
    n("Darth Maul"),
    n("Veers", True),
    n("Imperial Propaganda", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Garindan", True, qty=2),
    n("Hoth Blockade", True),
    n("Image Of The Dark Lord", True),
    n("Conquest", True),
    n("General Nevar", True),
    n("Do They Have A Code Clearance?"),
    n("No Escape"),
    n("Imperial Command", qty=2),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6", True),
    n("Blizzard 4"),
    n("Control & Set For Stun"),
    n("AT-AT Cannon", True),
    n("Cold Feet", True),
    n("Flagship Executor"),
    n("Juno Eclipse, Black Leader", True),
    n("Imperial Justice", True),
    n("Masterful Move & Endor Occupation"),
    n("Trample", qty=2),
    n("Control"),
    n("Walker Garrison"),
    n("Blizzard 1", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
