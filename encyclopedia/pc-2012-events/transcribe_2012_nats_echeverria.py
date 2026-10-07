#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jessica Echeverria.

Source: 2012NationalsDay1.pdf pages 15–16 (typed 2010 Xerox, Dark remainder handwritten).
Name Jessica Echeverria dested Jessica Echeverria as written. Username blank.
p15 Light Liberation Twist / Communing.
p16 Dark Bring him before me / Bring Him Before Me.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Jessica Echeverria"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2012 US Nationals Day 1 Jessica Echeverria LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jessica Echeverria DS.png"
LS_DECK_NAME = "Liberation Twist"
DS_DECK_NAME = "Bring him before me/Take you father's place"
NOTE = "Typed 2010 Xerox form. Dark remainder 34–60 handwritten. Username blank."
LS_NOTE = (
    "Typed 2010 Xerox. Name Jessica Echeverria dested Jessica Echeverria as written. Username blank. "
    "LIGHT checked. Deck Name Liberation Twist. Event Date blank Event Name Nationals handwritten. "
    "Do not dest as a new person. Analog generate empty dest as written. "
    "Communing dested Communing True analog leftover Chu. "
    "Master Kenobi dested analog leftover SAN. "
    "Squadron Assignments dested analog leftover Richards. "
    "The Camp dested analog leftover Pierre. "
    "Yavin 4: Massassi War room dested Yavin 4: Massassi War Room analog leftover Pinto. "
    "Yavin 4: Briefing room dested Yavin 4: Briefing Room analog leftover Grant. "
    "Kashyyk dested Kashyyyk analog leftover. "
    "Obi-Wan's hut dested Tatooine: Obi-Wan's Hut analog leftover Chu. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements True analog leftover Grant. "
    "Booster in Pulsar Skate dested Booster In Pulsar Skate analog leftover Veasey. "
    "All Wings Report in dested All Wings Report In analog leftover Veasey. "
    "Eject combo dested Eject! Eject! Eject! & Imperial Atrocity analog leftover Grant. "
    "BoShek dested BoShek, Brash Smuggler analog leftover Shannon. "
    "Luke with Lightsaber dested Luke With Lightsaber analog leftover Cullen. "
    "BoShek's Modified Light Freighter dested BoShek's Modified Freighter analog leftover Howland. "
    "5-foils dested A Few Maneuvers True analog leftover Srodoski. "
    "Jek porkins dested Jek Porkins analog leftover Srodoski. "
    "chewbacca, Protector dested Chewbacca, Protector analog leftover Marty. "
    "Restore Freedom dested Restore Freedom To The Galaxy True analog leftover Grant. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression True analog leftover Bali. "
    "Shield Let's keep optimism dested Let's Keep A Little Optimism Here analog leftover. "
    "Shield Wise Advise dested Wise Advice analog leftover. "
    "Shield Do, or do not dested Do, Or Do Not analog leftover. "
    "Gold 4 dested leftover_xerox. Skull dested leftover_xerox. Hol Okland dested leftover_xerox. "
    "True vs empty kept separate. Unique 60. Shields 6 slots 7–12 blank skip."
)
DS_NOTE = (
    "Typed 2010 Xerox remainder handwritten 34–60. Name Jessica Echeverria dested as written. "
    "Username blank. DARK checked. Deck Name Bring him before me/Take you father's place. "
    "Event Date blank Event Name Nationals. Do not dest as a new person. Analog generate empty dest as written. "
    "Bring him before me dested Bring Him Before Me / Take Your Father's Place empty analog leftover Ziagos. "
    "Prepared Defences dested Prepared Defenses analog leftover. "
    "I've lost artoo dested I've Lost Artoo! analog leftover Ziagos. "
    "Ability Ability ability dested Ability, Ability, Ability analog leftover. "
    "Rector terminal dested Reactor Terminal analog leftover. "
    "Limeted resorces dested Limited Resources analog leftover. "
    "The empire's back True vs empty kept separate. "
    "victory dested Victory True analog leftover without extra (V). "
    "Counter assult dested Counter Assault analog leftover. "
    "It's worse dested It's Worse analog leftover. "
    "Evacuate dested analog leftover Kinsey. "
    "Blast Door Controls dested analog leftover Baroni. "
    "Vader dested Darth Vader analog leftover Alex W. "
    "Boba Fett dested Boba Fett, Bounty Hunter analog leftover Anderson. "
    "Battle Order & First Strike dested analog leftover Bordier. "
    "IG-88 in IG-2000 dested IG-88 In IG-2000 analog leftover Hodur. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover walker. "
    "Ice-Heart dested Ysanne Isard analog leftover Dubreuil. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover walker. "
    "Hoth's Defensive Perimeter dested Hoth: Defensive Perimeter analog leftover. "
    "Dengar in Punishing One dested Dengar In Punishing One analog leftover Dubreuil. "
    "His Worse dested It's Worse analog leftover. "
    "Imbalance & Infiltrator dested Imbalance & Kintan Strider analog leftover Consoli. "
    "Bossk in Hound's Tooth dested Bossk In Hound's Tooth analog leftover. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover walker. "
    "Knowledge and defences dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield Death star sentry dested Death Star Sentry analog leftover Buck. "
    "True vs empty kept separate. Unique 60. Shields 8 slots 9–12 blank skip."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing", True),
    n("Master Kenobi", True),
    n("Squadron Assignments"),
    n("The Camp", True),
    n("Yavin 4", True),
    n("Tatooine"),
    n("Ralltiir"),
    n("Yavin 4: Massassi War Room", True),
    n("Yavin 4: Briefing Room"),
    n("Kashyyyk"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Chadra-Fan"),
    n("Gold 4"),
    n("Elyhek Rue"),
    n("Booster In Pulsar Skate", True),
    n("Projection Of A Skywalker"),
    n("Skull", qty=2),
    n("Blind Jedi"),
    n("Lieutenant Lepria"),
    n("All Wings Report In"),
    n("It Could Be Worse", qty=2),
    n("The Signal"),
    n("Escape Pod"),
    n("I've Got A Bad Feeling About This"),
    n("Ryle Torsyn"),
    n("Organized Attack", qty=2),
    n("Eject! Eject! Eject! & Imperial Atrocity", qty=4),
    n("Mirax Terrik", True),
    n("BoShek, Brash Smuggler", True),
    n("Spiral"),
    n("Captain Antilles"),
    n("General Dodonna"),
    n("Luke With Lightsaber"),
    n("Worrt"),
    n("BoShek's Modified Freighter", True),
    n("Power Pivot", True),
    n("Power Pivot"),
    n("Honor Of The Jedi"),
    n("Traffic Control"),
    n("Collision!"),
    n("A Few Maneuvers", True),
    n("Jek Porkins", True),
    n("Chewbacca, Protector", True),
    n("Rebel Planner"),
    n("Gold 6"),
    n("Red 6"),
    n("Gold 3"),
    n("Hol Okland"),
    n("X-wing Laser Cannon"),
    n("Red 7"),
    n("Massassi Base Sentry", True),
    n("Restore Freedom To The Galaxy", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Chasm"),
    n("Weapons Display"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Your Destiny"),
    n("Insignificant Rebellion"),
    n("Death Star II: Throne Room"),
    n("Prepared Defenses"),
    n("I've Lost Artoo!"),
    n("Gift Of The Master"),
    n("Ability, Ability, Ability"),
    n("Emperor's Power"),
    n("Blaster Rack", True),
    n("Reactor Terminal"),
    n("Tatooine: Jabba's Palace"),
    n("Nal Hutta"),
    n("Imperial-Class Star Destroyer"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Limited Resources"),
    n("Fear"),
    n("Vengeance"),
    n("Probe Telemetry", True),
    n("Restraining Bolt"),
    n("You Are Beaten"),
    n("The Empire's Back", True),
    n("The Empire's Back"),
    n("Twi'lek Advisor"),
    n("Death Star II: Docking Bay"),
    n("Victory", True, qty=2),
    n("Counter Assault"),
    n("It's Worse"),
    n("Sith Probe Droid", True),
    n("Katana"),
    n("Elis Helrot"),
    n("Evacuate"),
    n("Blast Door Controls"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Darth Vader", True),
    n("Torture"),
    n("Boba Fett, Bounty Hunter", True),
    n("Battle Order & First Strike", True),
    n("IG-88 In IG-2000"),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Lord Sidious"),
    n("Captain Yorr", True),
    n("The Emperor", True),
    n("Ysanne Isard"),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader's Lightsaber", True),
    n("Elis Helrot"),
    n("Collateral Damage"),
    n("A Sith's Plans", True),
    n("Hoth: Defensive Perimeter"),
    n("Dengar In Punishing One"),
    n("It's Worse"),
    n("Imbalance & Kintan Strider", True),
    n("Information Exchange"),
    n("Bossk In Hound's Tooth"),
    n("Grievous' Lightsabers", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Firepower"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Death Star Sentry"),
]
DS_ADD = []
