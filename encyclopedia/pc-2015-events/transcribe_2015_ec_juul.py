#!/usr/bin/env python3
"""2015 European Championship Day 2: Rasmus Juul (place 14).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p30 Dark / p31 Light typed sheets.
"""
from __future__ import annotations

PLAYER = "Rasmus Juul"
USERNAME = "Rebel Beer Runner"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 31
DS_PAGE = 30
LS_SCAN = "2015 European Championship Rasmus Juul LS.png"
DS_SCAN = "2015 European Championship Rasmus Juul DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 14. Name Rasmus on both sheets. Username Rebel Beer Runner (LS lowercase rebel beer runner). "
    "Sheet deck names: DS Bubble, LS Steady. STEADY. DS 1:3 / LS 3:1 handwritten. "
    "Both sides start with a starting interrupt, no objective."
)
LS_NOTE = (
    "Typed + handwritten p31. TITLE MISMATCH: wiki says Watch Your Step, sheet starts Heading For The Medical Frigate "
    "(line 2, no objective/Watch Your Step on sheet). "
    "Posted Naboo : Boss nass chambers dested Naboo: Boss Nass' Chambers. Posted Klor Slug dested K'lor'slug. "
    "Posted na chada wind chimes / out of order dested Nar Shaddaa Wind Chimes & Out Of Somewhere. "
    "Posted han cewie and the falcon dested Han, Chewie, And The Falcon. Posted Capt. TArpals dested Captain Tarpals. "
    "Posted Barganing table dested Bargaining Table. Posted Gungan Worrior dested Gungan Warrior. "
    "Posted Anger fear aggression (V checked) dested Anger, Fear, Aggression True. "
    "Posted planetary def. dested Planetary Defenses. Posted do or do not dested Do, Or Do Not. "
    "Steady, Steady and Bargaining Table listed as separate lines. Main 60, shields 15."
)
DS_NOTE = (
    "Typed p30. TITLE MISMATCH: wiki says Endor Operations, sheet starts Operational As Planned (line 2, no objective). "
    "Posted DS 2 dested Death Star II. Posted Knowledge and def dested Knowledge And Defense. "
    "Posted spaceport DB dested Spaceport Docking Bay. Posted Endor DB dested Endor: Landing Platform (Docking Bay). "
    "Posted DS2 DB / coolant shaft / capacitators / reactor core dested Death Star II: Docking Bay / Coolant Shaft / Capacitors / Reactor Core. "
    "Posted Blocake flagship DB dested Blockade Flagship: Docking Bay. Posted Scyte 3 dested Scythe 3. "
    "Posted Dreadnoughtg cruiser dested Dreadnaught-Class Heavy Cruiser. Posted Watch your back dested Watch Your Back!. "
    "Posted Fighters commin in dested Fighters Coming In. Posted Mara jades saber dested Mara Jade's Lightsaber. "
    "Posted VAders saber dested Darth Vader's Lightsaber. Posted Super laser MK 2 dested Superlaser Mark II. "
    "Posted SFS l-s7 Cannon (+ditto) dested SFS L-s7.2 TIE Cannon x2. Posted Mara Jade EMP hand dested Mara Jade, The Emperor's Hand. "
    "Posted ozzel dested Admiral Ozzel. Posted ADM Motti dested Admiral Motti. Posted DS- 4 / DS- 5 / DS -2 dested DS-61-4 / DS-61-5 / DS-61-2. "
    "Posted Major Minda dested Major Mianda. Posted Maarek stele T.E.R dested Maarek Stele, The Emperor's Reach. "
    "Posted DVDLOTS dested Darth Vader, Dark Lord Of The Sith. Posted Gran moff tarkin dested Grand Moff Tarkin. "
    "Posted leutenant Tanbris dested Lieutenant Tanbris. Posted Alligations of corruption dested Allegations Of Corruption. "
    "Posted Resistence dested Resistance. Posted Come here u big coward dested Come Here You Big Coward. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Heading For The Medical Frigate"
LS_CARDS = [
    n("Naboo: Boss Nass' Chambers"),
    n("Heading For The Medical Frigate"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Wokling", True),
    n("Rebel Artillery", qty=2),
    n("No Giben Up, General Jar Jar!", qty=2),
    n("K'lor'slug", True),
    n("Blast The Door, Kid!"),
    n("Nabrun Leids"),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("Kaadu"),
    n("Fambaa", qty=3),
    n("Draw Their Fire"),
    n("Ambush"),
    n("Han, Chewie, And The Falcon"),
    n("Naboo: Otoh Gunga Entrance"),
    n("Naboo: Swamp"),
    n("Naboo: Battle Plains"),
    n("Electropole", qty=4),
    n("Jar Jar's Electropole"),
    n("Captain Tarpals' Electropole", qty=2),
    n("Wesa Ready To Do Our-sa Part"),
    n("Steady, Steady"),
    n("Bargaining Table"),
    n("Gungan Energy Shield", qty=2),
    n("Brisky Morning Munchen"),
    n("Boss Nass", qty=2),
    n("Rep Been"),
    n("Jar Jar Binks"),
    n("General Jar Jar"),
    n("Captain Tarpals", qty=2),
    n("Aayla Secura"),
    n("Gungan General", qty=3),
    n("Gungan Guard", qty=2),
    n("Gungan Warrior", qty=9),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Republic No Longer Functions"),
    n("Planetary Defenses"),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Another Pathetic Lifeform"),
    n("Your Ship?"),
    n("Yavin Sentry"),
    n("Goldenrod"),
    n("Battle Plan"),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Operational As Planned"
DS_CARDS = [
    n("Endor"),
    n("Operational As Planned"),
    n("Death Star II"),
    n("Desperate Counter"),
    n("Moff Jerjerrod"),
    n("Knowledge And Defense"),
    n("Kashyyyk"),
    n("Spaceport Docking Bay"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Death Star II: Docking Bay"),
    n("Blockade Flagship: Docking Bay"),
    n("Death Star II: Coolant Shaft"),
    n("Death Star II: Capacitors"),
    n("Death Star II: Reactor Core"),
    n("That Thing's Operational"),
    n("Blizzard 4"),
    n("Onyx 2", True),
    n("Black 5", True),
    n("Black 6", True),
    n("Scythe 3"),
    n("Scythe 1"),
    n("Black 2", True),
    n("Black 4"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Imperial Barrier"),
    n("Force Field", True),
    n("Imbalance & Kintan Strider", True),
    n("Cold Feet", True),
    n("We Must Accelerate Our Plans"),
    n("Watch Your Back!"),
    n("All Power To Weapons", qty=2),
    n("TIE Sentry Ships", True),
    n("Imperial Arrest Order"),
    n("Imperial Decree", True),
    n("Imperial Domination", True),
    n("First Strike"),
    n("Combat Response", True),
    n("Lost In Space", True),
    n("Fighters Coming In"),
    n("Mara Jade's Lightsaber"),
    n("Darth Vader's Lightsaber"),
    n("Superlaser Mark II"),
    n("SFS L-s7.2 TIE Cannon", qty=2),
    n("Mara Jade, The Emperor's Hand"),
    n("Admiral Ozzel"),
    n("Admiral Motti"),
    n("DS-61-4"),
    n("Lord Vader"),
    n("Ysanne Isard", True),
    n("Major Mianda"),
    n("Stormtrooper Garrison"),
    n("Grand Moff Tarkin", True),
    n("Lieutenant Tanbris"),
    n("Maarek Stele, The Emperor's Reach", True),
    n("DS-61-5", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Lieutenant Hebsly"),
    n("DS-61-2"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("Firepower"),
    n("Resistance"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("Fanfare"),
    n("A Useless Gesture"),
    n("Imperial Detention"),
    n("I Find Your Lack Of Faith Disturbing"),
]
DS_ADD = []
