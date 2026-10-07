#!/usr/bin/env python3
"""Day 2 Xerox transcription: Mitch Nieland.

Source scans: extract/day2/d2p2_p01.png (Light, Dos mas!) and
extract/day2/d2p2_p02.png (Dark, Tilt-a-whirl). 2013 form, Worlds 2014.
Plead My Case / Senate and Endor Operations. (V) follows the sheet checkbox.
Dittos expanded; ditto is_v follows that line's own box.
"""
from __future__ import annotations

# --- helpers ---

def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Mitch Nieland"
USERNAME = ""
PDF = "2014 Worlds Day 2 Part 2.pdf"


# --- Light: d2p2_p01.png, 2013 form. LIGHT checked. ---

LS_DECK_NAME = "Dos mas!"
LS_SIDE = "Light"
LS_FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p2_p01.png"
LS_PDF_PAGE = 1
LS_STARTING = ("Plead My Case To The Senate / Sanity And Compassion", False)

LS_RESERVE = [
    n("Plead My Case To The Senate / Sanity And Compassion"),  # 1  Plead my case to Senate
    n("Coruscant: Galactic Senate"),  # 2  Coruscant: Senate
    n("Coruscant: Jedi Council Chamber"),  # 3  Coruscant: JCC
    n("Heading For The Medical Frigate"),  # 4
    n("Wokling", True),  # 5  written Wokling / looks like Landing
    n("Rogue Squadron Tactics"),  # 6
    n("Strike Planning"),  # 7
    n("Dressel"),  # 8
    n("Kashyyyk: Forest Depths"),  # 9  Kashyyyk: Forest Depths
    n("So This Is How Liberty Dies"),  # 10
    n("Sneak Preview"),  # 11
    n("Home One: War Room"),  # 12  Home one: war room
    n("Wedge Antilles, Red Squadron Leader"),  # 13  Wedge Antilles: RSL
    n("Jaina Solo"),  # 14
    n("Mas Amedda"),  # 15
    n("Senator Mon Mothma"),  # 16
    n("Bail Organa"),  # 17
    n("General Airen Cracken"),  # 18  General Airen Cracken
    n("General Solo", True),  # 19
    n("Admiral Ackbar", True),  # 20
    n("Luke Skywalker, Rebel Scout", True),  # 21  Luke Skywalker, RS
    n("Alderaan Consular Ship"),  # 22  Alderaan Consular Ship
    n("Senator Leia Organa"),  # 23
    n("Lando Calrissian, Scoundrel"),  # 24
    n("Commander Vanden Willard"),  # 25  Commander Willard
    n("Field Dressing"),  # 26
    n("Rebel Leadership", True),  # 27
    n("Let The Wookiee Win", True),  # 28
    n("Imperial Atrocity", True),  # 29
    n("It Could Be Worse"),  # 30
    n("Rebel Leadership", True),  # 31
    n("Senator Padme Amidala"),  # 32  Senator Padme
    n("Sense"),  # 33
    n("Might Of The Republic"),  # 34
    n("Luke Skywalker, Rebel Scout", True),  # 35  Luke Skywalker RS
    n("Let The Wookiee Win", True),  # 36  LTWW
    n("Bail Organa, Father Of Rebellion"),  # 37  Bail Organa, Dad
    n("Might Of The Republic"),  # 38
    n("Sense"),  # 39
    n("Might Of The Republic"),  # 40
    n("Rebel Leadership", True),  # 41
    n("Jedi Survivor"),  # 42
    n("Endor: Back Door"),  # 43  Endor: back door
    n("Nabrun Leids"),  # 44
    n("Bail Organa"),  # 45
    n("Bail Organa, Father Of Rebellion"),  # 46  Bail Organa, Dad
    n("Wyron Serper", True),  # 47
    n("Queen Amidala, Ruler Of Naboo"),  # 48  Queen & Born Lao
    n("Home One"),  # 49
    n("Obi-Wan Kenobi", True),  # 50
    n("Wrist Comlink"),  # 51  Comm horn
    n("Captain Yutani With Blaster Cannon"),  # 52  Captain Yutani w/ Blaster; (V) empty
    n("Chewbacca, Protector", True),  # 53
    n("It Could Be Worse"),  # 54
    n("Rebel Barrier"),  # 55
    n("Rebel Barrier"),  # 56  ditto
    n("Nabrun Leids"),  # 57
    n("Narrow Escape"),  # 58
    n("Menace Fades"),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("Chasm"),  # 1
    n("A Tragedy Has Occurred"),  # 2
    n("Simple Tricks And Nonsense"),  # 3  Simple Tricks
    n("Aim High"),  # 4
    n("Don't Do That Again", True),  # 5
    n("Planetary Defenses", True),  # 6
    n("He Can Go About His Business", True),  # 7
    n("Weapons Display", True),  # 8
    n("Battle Plan"),  # 9
    n("Ultimatum"),  # 10
    n("There is Another"),  # 11  There is Another
    n("Your Insight Serves You Well"),  # 12
    n("The Professor"),  # 13
    n("Let's Keep A Little Optimism Here"),  # 14  Optimism
    n("Wise Advice"),  # 15
]

LS_ADD = []  # Hidden Fortress empty

LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []


# --- Dark: d2p2_p02.png, 2013 form. DARK checked. ---

DS_DECK_NAME = "Tilt-a-whirl"
DS_SIDE = "Dark"
DS_FORM = "xerox_2013"
DS_SCAN = "extract/day2/d2p2_p02.png"
DS_PDF_PAGE = 2
DS_STARTING = ("Endor Operations / Imperial Outpost", False)

DS_RESERVE = [
    n("Endor Operations / Imperial Outpost"),  # 1  Endor Operations
    n("Endor"),  # 2
    n("Endor: Bunker"),  # 3
    n("Endor: Landing Platform (Docking Bay)"),  # 4  Endor: Landing Platform
    n("Prepared Defenses"),  # 5
    n("I'm Sorry", True),  # 6
    n("Krayt Dragon Bones", True),  # 7
    n("Crossfire", True),  # 8
    n("Captain Sarkli", True),  # 9
    n("Captain Sarkli"),  # 10  ditto; (V) empty
    n("Captain Sarkli"),  # 11  ditto; (V) empty
    n("Fanblade Starfighter"),  # 12
    n("Fanblade Starfighter"),  # 13  ditto
    n("Dengar In Punishing One"),  # 14
    n("The Emperor's Shield"),  # 15  The Emperor Shield
    n("DS-61-4"),  # 16  DS-61-4 in Black 4
    n("Obsidian 7"),  # 17
    n("Obsidian 8"),  # 18
    n("Colonel Jendon In Onyx 1"),  # 19  Colonel Jendon in Onyx 1
    n("Onyx 2", True),  # 20
    n("Broken Concentration"),  # 21
    n("Endor Shield", True),  # 22
    n("Lateral Damage"),  # 23
    n("Lateral Damage"),  # 24
    n("Ability, Ability, Ability"),  # 25
    n("Dark Maneuvers"),  # 26  written Dark Dealers; 3-of
    n("Dark Maneuvers"),  # 27  ditto
    n("Dark Maneuvers"),  # 28  ditto
    n("Presence Of The Force"),  # 29
    n("Presence Of The Force"),  # 30  ditto
    n("All Power To Weapons"),  # 31
    n("All Power To Weapons"),  # 32  ditto
    n("All Power To Weapons"),  # 33  ditto
    n("Operational As Planned", True),  # 34
    n("Operational As Planned", True),  # 35  ditto (V)
    n("Operational As Planned", True),  # 36
    n("Operational As Planned", True),  # 37
    n("Operational As Planned", True),  # 38
    n("Force Push", True),  # 39
    n("Force Push", True),  # 40  ditto (V)
    n("Sleen"),  # 41
    n("Sleen"),  # 42  ditto
    n("Sleen"),  # 43
    n("Sleen"),  # 44
    n("Sleen"),  # 45
    n("Sleen"),  # 46
    n("Sleen"),  # 47
    n("Sleen"),  # 48
    n("Sleen"),  # 49
    n("Sleen"),  # 50
    n("Sleen"),  # 51
    n("Sleen"),  # 52
    n("Sleen"),  # 53
    n("Sleen"),  # 54
    n("Sleen"),  # 55
    n("Sleen"),  # 56
    n("Sleen"),  # 57
    n("Sleen"),  # 58
    n("Bubo"),  # 59
    n("Knowledge And Defense", True),  # 60
]

DS_SHIELDS = [
    n("Secret Plans"),  # 1
    n("Come Here You Big Coward"),  # 2  Coward
    n("Imperial Detention"),  # 3
    n("Allegations Of Corruption"),  # 4  Allegations of Corrupn
    n("Abyss"),  # 5
    n("Do They Have A Code Clearance?"),  # 6  Code Clearance
    n("You Cannot Hide Forever"),  # 7
    n("There Is No Try"),  # 8
    n("Battle Order"),  # 9
    n("Fanfare"),  # 10
    n("Resistance"),  # 11
    n("Death Star Sentry"),  # 12
    n("A Useless Gesture"),  # 13  Useless Gesture
    n("We'll Let Fate-a Decide, Huh?"),  # 14  We'll Take Fate Decide
    n("After Her!"),  # 15  After Her
]

DS_ADD = []  # Hidden Fortress empty

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []


NOTES = """
Mitch Nieland, 2014 Worlds Day 2, 2013 form. Username blank.
Light d2p2_p01.png deck Dos mas! (LIGHT checked). Plead My Case / Senate.
Dark d2p2_p02.png deck Tilt-a-whirl (DARK checked). Endor Operations.

LS uncertain:
- 5 Wokling (V): earlier crop reads Landing; band is Wokling (vb4). Senate
  staple with Dressel / Kashyyyk renegade planets.
- 12 Home one: war room -> Home One: War Room (not Royal Naboo: Theed Palace
  War Room). Home One the cruiser is line 49.
- 37/46 Bail Organa, Dad -> Bail Organa, Father Of Rebellion (vb7). 17/45 are
  the vb5 Bail Organa.
- 48 Queen & Born Lao -> Queen Amidala, Ruler Of Naboo.
- 51 Comm horn -> Wrist Comlink.
- 52 Captain Yutani w/ Blaster, (V) empty. Written virtual title
  Captain Yutani With Blaster Cannon (vb7); checkbox not checked.
- Shield 11 There is Another (vsh), not Dark This Is Just Wrong.

DS uncertain:
- 1 Endor Operations expanded to Endor Operations / Imperial Outpost.
- 9 Captain Sarkli (V); dittos 10-11 have empty boxes so is_v=False.
- 16 DS-61-4 in Black 4 -> DS-61-4.
- 19 Colonel Jendon in Onyx 1 -> Colonel Jendon In Onyx 1 (vb6).
- 26-28 Dark Dealers (3-of). Unique Dark Deal cannot be a 3-of. Read as
  Dark Maneuvers (Premiere interrupt; Pierre also lists multiples).
- 41-58 eighteen Sleen dittos as written (Tilt-a-whirl).
- Shield 5 Abyss (not Doors; earlier crop was misaligned).
- Shield 14 We'll Take Fate Decide -> We'll Let Fate-a Decide, Huh? (vsh).
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 15, len(DS_SHIELDS)
    print("file", __file__)
    print("player", PLAYER, "username", USERNAME or "-")
    print("LS", LS_DECK_NAME, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", DS_DECK_NAME, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
