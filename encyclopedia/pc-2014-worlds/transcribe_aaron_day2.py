#!/usr/bin/env python3
"""Day 2 Xerox transcription: Aaron Kingery (Archmage08).

Source scans: extract/day2/d2p2_p07.png (Light, Pimpin') and
extract/day2/d2p2_p08.png (Dark, Why you hate Me?). 2010 form,
Worlds Day 2. Hidden Base / Mon Calamari and Separatist Uprising /
Muunilinst. (V) follows the sheet checkbox. Dittos: none used as
card copies (Tatooine line 52 has stray quotes, not a ditto of 51).
"""
from __future__ import annotations

# --- helpers ---

def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


AARON_D2_PLAYER = "Aaron Kingery"
AARON_D2_USERNAME = "Archmage08"
AARON_D2_LS_DECK_NAME = "Pimpin'"
AARON_D2_DS_DECK_NAME = "Why you hate Me?"


# --- Light: d2p2_p07.png, 2010 form. LIGHT checked. ---
# Name box blank / stray K in the # slot. Username Archmage08.

AARON_D2_LS_RESERVE = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),  # 1  Hidden Base; (V) empty
    n("Rendezvous Point"),  # 2
    n("Republic Logistics", True),  # 3
    n("Mon Calamari Dockyards", True),  # 4  written Mon Calamari Dock Yards
    n("Superficial Damage", True),  # 5
    n("Mon Calamari"),  # 6
    n("Naboo"),  # 7
    n("Nar Shaddaa", True),  # 8
    n("Projection Of A Skywalker"),  # 9
    n("TK-422"),  # 10
    n("A Jedi's Plans", True),  # 11
    n("Kiffex", True),  # 12
    n("Luke Skywalker", True),  # 13
    n("Dack Ralter"),  # 14  written like Dark Baitr
    n("Mon Calamari Star Cruiser", True),  # 15
    n("Heavy Turbolaser Battery"),  # 16  written Heavy Turbo Laser Battery
    n("Mon Calamari Star Cruiser", True),  # 17
    n("Threepio With His Parts Showing", True),  # 18
    n("Liberty"),  # 19
    n("Strikeforce", True),  # 20  written Strike Force
    n("Heavy Turbolaser Battery"),  # 21
    n("Choke"),  # 22
    n("Admiral Ackbar", True),  # 23
    n("Let The Wookiee Win", True),  # 24
    n("On Target"),  # 25
    n("Alter", True),  # 26
    n("Defiance"),  # 27
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 28  truncated Rebel R
    n("Heavy Turbolaser Battery"),  # 29
    n("On Target"),  # 30
    n("Heading For The Medical Frigate"),  # 31  written Medical Frig
    n("Mon Calamari Star Cruiser", True),  # 32
    n("Yoda Stew & You Do Have Your Moments"),  # 33  Yoda's site + You do have Your moments
    n("Luke Skywalker", True),  # 34
    n("Hear Me Baby, Hold Together", True),  # 35
    n("Stay Sharp!"),  # 36  written Stay Sharp
    n("Red 5"),  # 37  5 looks like Kaw/Five
    n("Boushh"),  # 38
    n("Imperial Atrocity", True),  # 39
    n("Projection Of A Skywalker"),  # 40
    n("Power Pivot"),  # 41
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 42
    n("Escape Pod", True),  # 43
    n("It Could Be Worse"),  # 44
    n("Power Pivot"),  # 45
    n("Escape Pod", True),  # 46
    n("On Target"),  # 47
    n("Out Of Commission & Transmission Terminated"),  # 48
    n("Rebel Barrier"),  # 49  written Rebel Reinforcement + Barrier; see NOTES
    n("Imperial Atrocity", True),  # 50
    n("Mon Calamari Star Cruiser", True),  # 51
    n("Tatooine"),  # 52  stray quotes after title, not a ditto of 51
    n("Clouds"),  # 53  written Tatooine (C)
    n("Stay Sharp!"),  # 54
    n("Let The Wookiee Win", True),  # 55
    n("Flash Of Insight", True),  # 56
    n("Defiance"),  # 57
    n("Imperial Atrocity", True),  # 58  extra Propaganda-shaped word; see NOTES
    n("We're Doomed"),  # 59  written Were Doomed
    n("Anger, Fear, Aggression", True),  # 60
]

AARON_D2_LS_SHIELDS = [
    n("Ounee Ta"),  # 1  written Oance Ta
    n("Let's Keep A Little Optimism Here"),  # 2  Here omitted
    n("Planetary Defenses"),  # 3
    n("Your Insight Serves You Well", True),  # 4
    n("Traffic Control", True),  # 5
    n("Ultimatum"),  # 6
    n("The Professor", True),  # 7
    n("Simple Tricks And Nonsense", True),  # 8
    n("Aim High", True),  # 9  written Aim High
    n("Battle Plan"),  # 10
    n("Chasm", True),  # 11
    n("A Tragedy Has Occurred"),  # 12
]

AARON_D2_LS_ADD = [
    n("Do, Or Do Not"),  # 1
    n("Wise Advice"),  # 2
    n("Don't Do That Again"),  # 3
]


# --- Dark: d2p2_p08.png, 2010 form. DARK checked. ---
# Name Aaron Kingery. Username Archmage08. Worlds D2.

AARON_D2_DS_RESERVE = [
    n("Separatist Uprising / At War With Itself", True),  # 1  sheet / Muunilinst
    n("Geonosis: Separatist Council Room", True),  # 2  written Council Rm
    n("Everything Is Going As Planned", True),  # 3  written going as Planned
    n("Deployment Orders", True),  # 4
    n("Baktoid Armor Workshop"),  # 5
    n("Droid Racks"),  # 6  written Droid Rack
    n("Ni Chuba Na??", True),  # 7
    n("War Has Begun"),  # 8
    n("Defense Of Muunilinst", True),  # 9
    n("Muunilinst: Separatist Command Center"),  # 10  written Command Ctr
    n("Muunilinst: City Of Harnaidan", True),  # 11
    n("Muunilinst: Banking Clan Headquarters", True),  # 12  written Banking Clan HQ
    n("Maul's Sith Infiltrator"),  # 13
    n("Darth Maul"),  # 14
    n("AAT Assault Leader", True),  # 15
    n("Outflank", True),  # 16
    n("OOM Command Battle Droid", True),  # 17
    n("3B3-888"),  # 18
    n("Armored Attack Tank"),  # 19
    n("AAT Laser Cannon"),  # 20
    n("Tank Commander"),  # 21
    n("Armored Attack Tank"),  # 22
    n("Tank Commander"),  # 23
    n("Open Fire!"),  # 24
    n("AAT Laser Cannon"),  # 25
    n("Jango Fett", True),  # 26  written The Mandalorian, Father of Fett
    n("OOM Command Battle Droid", True),  # 27
    n("Imperial Barrier"),  # 28
    n("Sneak Attack", True),  # 29
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 30
    n("Armored Attack Tank"),  # 31
    n("4-LOM With Concussion Rifle", True),  # 32  written 4-Lom w/
    n("Armored Attack Tank"),  # 33  written Armored Assault Tank
    n("Defensive Fire", True),  # 34
    n("Maul's Sith Infiltrator"),  # 35
    n("Imperial Artillery"),  # 36
    n("Cold Feet", True),  # 37
    n("Heavy Fire Zone"),  # 38
    n("AAT Laser Cannon"),  # 39  written AAT Cannon
    n("OOM-9", True),  # 40
    n("Imperial Artillery"),  # 41
    n("Maul's Sith Infiltrator"),  # 42
    n("Imperial Artillery"),  # 43
    n("Imperial Propaganda", True),  # 44
    n("Imperial Artillery"),  # 45
    n("Tank Commander"),  # 46
    n("U-3PO (Yoo-Threepio)"),  # 47  written U 3PO
    n("Outflank", True),  # 48
    n("Image Of The Dark Lord", True),  # 49
    n("Self-Destruct Mechanism"),  # 50
    n("Darth Maul"),  # 51
    n("Defensive Fire", True),  # 52
    n("Imperial Barrier"),  # 53
    n("Imperial Artillery"),  # 54
    n("Heavy Fire Zone"),  # 55
    n("Self-Destruct Mechanism"),  # 56
    n("Masterful Move & Endor Occupation"),  # 57  written Masterful Move & Endor Occ
    n("OWO-1 With Backup"),  # 58
    n("Imperial Barrier"),  # 59
    n("Knowledge And Defense", True),  # 60
]

AARON_D2_DS_SHIELDS = [
    n("You Cannot Hide Forever", True),  # 1
    n("Resistance", True),  # 2
    n("Firepower", True),  # 3
    n("Battle Order"),  # 4
    n("There Is No Try"),  # 5
    n("Come Here You Big Coward"),  # 6
    n("Oppressive Enforcement"),  # 7
    n("A Useless Gesture"),  # 8
    n("Restricted Access"),  # 9
    n("Wipe Them Out, All Of Them", True),  # 10  written Wipe them all out
    n("Leave Them To Me"),  # 11
    n("Reactor Terminal", True),  # 12
]

AARON_D2_DS_ADD = [
    n("Secret Plans", True),  # 1  (V) box has a blob/tick; see NOTES
    n("Fanfare"),  # 2
    n("Allegations Of Corruption"),  # 3
]


NOTES = """
Aaron Kingery / Archmage08, 2014 Worlds Day 2, 2010 form.
Light d2p2_p07.png deck Pimpin' (LIGHT checked). Name field blank; a K sits
in the # slot. Username Archmage08 (LS 08 can read as PO).
Dark d2p2_p08.png deck Why you hate Me? (DARK checked). Name Aaron Kingery.

LS uncertain:
- 1 Hidden Base (V) empty so original SE objective, expanded to full 7-side.
  Only five systems listed (Mon Calamari, Naboo, Nar Shaddaa, Kiffex, Tatooine);
  Hidden Base usually wants seven. Not inventing two more.
- 4 Dock Yards → Mon Calamari Dockyards (vb6). (V) checked; title is not (V).
- 14 Dack Ralter: handwriting looks like Dark Baitr; Hoth pilot, (V) empty
  (vb7 Dack Ralter (V) exists; box not checked).
- 20 Strike Force → Strikeforce (V).
- 28 Antilles Maneuver + Rebel R (V) → same combo as 42 (vb6, not a (V) card).
- 33 Yoda's site + You do have Your moments → Yoda Stew & You Do Have Your
  Moments (Reflections II combo). (V) empty.
- 37 Red 5: second glyph is a messy 5 (reads Kaw/Five). (V) empty; original
  Hoth Red 5, not Red 5 (V) / Artoo-Detoo In Red 5.
- 49 Rebel Reinforcement + Barrier (V) empty. No mapped combo. Taken as Rebel
  Barrier (space staple); could be Rebel Reinforcements or a non-card combo.
- 52 Tatooine with stray quotes; not a ditto of 51 Mon Calamari Star Cruiser.
- 53 Tatooine (C) → Clouds (sector). Cantina is the other (C) expansion;
  space Hidden Base wants Clouds.
- 58 Imperial Propaganda Atrocity (V) checked. Light has Imperial Atrocity (V)
  (already on 39 and 50); Propaganda is Dark. Read as a third Imperial Atrocity
  with a Dark-list slip, not Imperial Propaganda.
- 16/21/29 Heavy Turbo Laser Battery → Heavy Turbolaser Battery.
- Several (V) boxes checked on non-(V) titles (Republic Logistics, Dockyards,
  Nar Shaddaa, Kiffex, A Jedi's Plans, Threepio With His Parts Showing, Alter).
  Checkbox followed.

DS uncertain:
- 1 sheet Separatist Uprising / Muunilinst → official Separatist Uprising /
  At War With Itself (vb9). Muunilinst is the starting system, not the back.
- 3 Everything is going as Planned (V) box is a filled square (counted checked).
- 6 Droid Rack → Droid Racks. (V) empty (vb6 Droid Racks (V) exists).
- 26 The Mandalorian, Father of Fett (V) → Jango Fett (vb5 lore nickname).
  Not Jango Fett, The Assassin.
- 32 4-Lom w/ (V) → 4-LOM With Concussion Rifle (V) (vb6).
- 33 Armored Assault Tank → Armored Attack Tank (same card as 19/22/31).
- 39 AAT Cannon → AAT Laser Cannon (third copy; 20 and 25 spell it out).
  Not AT-AT Cannon (wrong archetype).
- 57 Masterful Move & Endor Occ → Masterful Move & Endor Occupation.
  Not Emperor's Power (no such combo).
- 47 U 3PO → U-3PO (Yoo-Threepio).
- Shield 10 Wipe them all out (V) in the shields block; mapped as Wipe Them
  Out, All Of Them (V). Not in vsh title map (effect, not a shield printing).
- Add 1 Secret Plans (V) box has a blob/tick; counted checked. No vsh
  Secret Plans (V); SE Secret Plans is the usual shield.
- (V) checked on several non-(V) titles (Council Room, Deployment Orders,
  Defense Of Muunilinst, City Of Harnaidan, Banking Clan HQ, AAT Assault
  Leader, OOM Command Battle Droid). Checkbox followed.
""".strip()


if __name__ == "__main__":
    assert len(AARON_D2_LS_RESERVE) == 60, len(AARON_D2_LS_RESERVE)
    assert len(AARON_D2_LS_SHIELDS) == 12, len(AARON_D2_LS_SHIELDS)
    assert len(AARON_D2_DS_RESERVE) == 60, len(AARON_D2_DS_RESERVE)
    assert len(AARON_D2_DS_SHIELDS) == 12, len(AARON_D2_DS_SHIELDS)
    print("LS reserve", len(AARON_D2_LS_RESERVE), "shields", len(AARON_D2_LS_SHIELDS), "add", len(AARON_D2_LS_ADD))
    print("DS reserve", len(AARON_D2_DS_RESERVE), "shields", len(AARON_D2_DS_SHIELDS), "add", len(AARON_D2_DS_ADD))
    print(AARON_D2_PLAYER, AARON_D2_USERNAME, AARON_D2_LS_DECK_NAME, AARON_D2_DS_DECK_NAME)
