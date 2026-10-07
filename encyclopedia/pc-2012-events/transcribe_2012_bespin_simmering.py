#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Conrad Simmering.

Source: 2012BespinRegionals.pdf pages 7–8.
p07 Dark typed 2010 Xerox Name Conrad Simmering Username Maul12555.
p08 Light handwritten 2010 Xerox Name Conrad Simmering dested Conrad Simmering
analog leftover 2012 Nats / 2013 Worlds / player-stubs/Conrad_Simmering.wiki.
Do not dest as a new person. Do not dest 2012 Nats / 2013 Worlds Simmering 60s again.
"""
from __future__ import annotations

PLAYER = "Conrad Simmering"
USERNAME = "Maul12555"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2012 Bespin Regionals Conrad Simmering LS.png"
DS_SCAN = "2012 Bespin Regionals Conrad Simmering DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p07 Dark typed 2010 Xerox / p08 Light handwritten 2010 Xerox. "
    "Name Conrad Simmering dested Conrad Simmering analog leftover 2012 Nats / 2013 Worlds / "
    "player-stubs/Conrad_Simmering.wiki. Username Maul12555. Date 7/14/12 Event Bespin Regional. "
    "Do not dest as a new person. Do not dest 2012 Nats / 2013 Worlds Simmering 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p08 Light. Name Conrad Simmering dested Conrad Simmering. Username blank on Light. "
    "LIGHT checked. Deck Name Watch You Step dested off article. "
    "Watch You Step dested Watch Your Step True analog leftover Gardner. "
    "Heading To The Medical Frigate dested Heading For The Medical Frigate analog leftover. "
    "Palejo Resha dested Palejo Reshad analog leftover. "
    "Boshek, Brash Smuggler dested BoShek, Brash Smuggler analog leftover Massung. "
    "Boshek's Modified Light Freighter dested BoShek's Modified Freighter analog leftover Atkin. "
    "It's Not My Fault! dested It's Not My Fault True analog leftover Arlandson. "
    "Anger, Fear, Aggression True IN THE 60. "
    "Antilles Maneuver & Rebel Reinforcements qty=3. Rebel Barrier qty=3. No Questions Asked True qty=3. "
    "Shield 12 empty skip unique 11 sheet-accurate."
)
DS_NOTE = (
    "Typed 2010 Xerox p07 Dark. Name Conrad Simmering dested Conrad Simmering. Username Maul12555. "
    "DARK checked. Deck Name Bad Ass Bombers dested off article. "
    "Hunt Down dested Hunt Down And Destroy The Jedi True analog leftover 2012 Nats Simmering. "
    "Inconsequential losses dested Inconsequential Losses True analog leftover Gogolen. "
    "Coruscant dested Coruscant (Dark) analog leftover Simmering Nats. "
    "Fire Power dested Firepower True analog leftover. "
    "All Power To Weapons qty=7 unique overcount. TIE Bomber qty=7 unique overcount. "
    "Relentless Pursuit empty qty=4 at first occurrence (17 covering 18, 19, 45). "
    "I Can't Shake Him! qty=4. They're Coming In Too Fast! qty=3. "
    "A Dark Time For The Rebellion True qty=4. Scimitar Squadron TIE qty=3. Proton Bombs qty=4. "
    "Knowledge And Defense True IN THE 60. "
    "Shield 12 empty skip unique 11 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("Heading For The Medical Frigate"),
    n("General Solo", True),
    n("Millennium Falcon", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Chewie", True),
    n("Corran Horn"),
    n("Palejo Reshad"),
    n("Harc Seff"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Sergeant Doallyn"),
    n("BoShek, Brash Smuggler"),
    n("Wedge Antilles"),
    n("Laudica", True),
    n("Mirax Terrik"),
    n("Dash Rendar"),
    n("Luke's Lightsaber"),
    n("X-wing Laser Cannon"),
    n("No Questions Asked", True, qty=3),
    n("Menace Fades"),
    n("Home One: Docking Bay"),
    n("Kiffex"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("BoShek's Modified Freighter"),
    n("Outrider"),
    n("Red Squadron 1"),
    n("Dodge"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=3),
    n("Rebel Barrier", qty=3),
    n("Jedi Levitation", True),
    n("Corellian Retort", True, qty=2),
    n("Punch It!", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Life Debt", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("A Few Maneuvers"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Run Luke, Run"),
    n("It's Not My Fault", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Planetary Subjugation"),
    n("Inconsequential Losses", True),
    n("Imperial Stockpile"),
    n("Concussion Missiles"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Coruscant (Dark)"),
    n("Prepared Defenses"),
    n("All Power To Weapons", qty=7),
    n("Relentless Pursuit", qty=4),
    n("I Can't Shake Him!", qty=4),
    n("They're Coming In Too Fast!", qty=3),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("TIE Bomber", qty=7),
    n("Scimitar Squadron TIE", qty=3),
    n("Proton Bombs", qty=4),
    n("Bombing Run", qty=3),
    n("Dreadnaught-Class Heavy Cruiser", qty=3),
    n("Fighter Cover", qty=2),
    n("Naboo"),
    n("Yavin 4"),
    n("Tatooine"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Lateral Damage"),
    n("Overload"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Imperial Detention"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
]
DS_ADD = []
