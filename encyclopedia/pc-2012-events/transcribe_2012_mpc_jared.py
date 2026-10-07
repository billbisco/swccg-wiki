#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Jared.

Source: 2012mpcday1.pdf pages 105–106 (typed GEMP dumps).
Handwritten Jarad dested Jared (2013 leftover PLAYER=Jared;
2014 leftover PLAYER=Jarrod CANON Jared; generate_2014_mpc Jarrod→Jared).
p105 Light Watch Your Step (V). p106 Dark Hunt Down.
Username blank. Pack player-stubs/Jared.wiki.
Do not dest as Jarad Konsker / Jared Napolitano / Jared Greenwald.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Jared"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 105
DS_PAGE = 106
LS_SCAN = "2012 Match Play Championship Day 1 Jared LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Jared DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "p105 typed GEMP dump WYS; p106 typed GEMP dump Hunt Down. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Handwritten Jarad dested Jared. Username blank. "
    "Do not dest as Jarad Konsker. Do not dest as a new person. "
    "Watch Your Step/This Place Can Be A Little Rough (V) dested dual True. "
    "AFA (V) (1 starting) dested Anger, Fear, Aggression True in the 60. "
    "Starting locations/characters/interrupts dested in the 60. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Blind Jedi dested as written. Chewie (V) dested Chewie True. "
    "Jabba prize handwritten dested Jabba's Prize in shields. Unique 60. Shields 13."
)
DS_NOTE = (
    "Typed GEMP dump. Handwritten Jarad dested Jared. Username blank. "
    "Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe "
    "dested dual without True. "
    "K&D (V) (1 starting) dested Knowledge And Defense True in the 60. "
    "Dr Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Do They Have A Code Clearance? crossed skipped. "
    "We'll Let Fate Decide (V) handwritten dested as written. "
    "Visage Of The Emperor starting plus interrupt x2 dested x3 sheet-accurate. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("No Questions Asked", True, qty=3),
    n("Laudica", True),
    n("Palejo Reshad"),
    n("Mirax Terrik"),
    n("Dash Rendar", True),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Chewie", True),
    n("Romas 'Lock' Navander"),
    n("Sergeant Bruckman"),
    n("General Crix Madine"),
    n("Corran Horn"),
    n("Wedge Antilles", True),
    n("Blind Jedi"),
    n("Maris Brood, Fallen Jedi"),
    n("Evacuation Control", True),
    n("K'lor'slug", True),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("Hindsight", True),
    n("Houjix"),
    n("Antilles Maneuver", True, qty=2),
    n("Escape Pod", True),
    n("Lucky Shot", True),
    n("Desperate Reach", True),
    n("We Wish To Board At Once"),
    n("Rebel Barrier", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Corellian Retort", True),
    n("Weapon Levitation"),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Alderaan Consular Ship"),
    n("Booster In Pulsar Skate"),
    n("Red Squadron 7", True),
    n("Obi-Wan In Radiant VII"),
    n("Enhanced Proton Torpedoes", True, qty=2),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Jabba's Prize"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor", qty=3),
    n("Executor: Meditation Chamber"),
    n("Surface Defense", True),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine", qty=2),
    n("Battle Droid Squad", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Janus Greejatus"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Ni Chuba Na??", True),
    n("Revenge Of The Sith"),
    n("Jabba's Haven"),
    n("Broken Concentration", True),
    n("Ability, Ability, Ability", True),
    n("Presence Of The Force"),
    n("Blast Door Controls"),
    n("Search And Destroy"),
    n("No Escape"),
    n("First Strike"),
    n("Imperial Justice", True),
    n("Protocol Failure"),
    n("Where Are You Taking This ... Thing?"),
    n("Force Push", True),
    n("We Must Accelerate Our Plans", qty=4),
    n("Why Didn't You Tell Me?", True),
    n("A Dark Time For The Rebellion", True),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("ComScan Detection", True, qty=2),
    n("Force Lightning"),
    n("Force Field", True, qty=2),
    n("Sith Fury", True, qty=2),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Hallway"),
    n("Nal Hutta"),
    n("Victory", qty=2),
    n("Boba Fett In Slave I", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Resistance"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Imperial Detention"),
    n("Leave Them To Me", True),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate Decide", True),
]
DS_ADD = []
