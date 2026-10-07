#!/usr/bin/env python3
"""Day 2 Xerox transcription: Brian Terwilliger (Twigg).

Source scans: extract/day2_upright/d2p3_p03.png (Light, Where Did You Go?)
and extract/day2_upright/d2p3_p04.png (Dark, slavers / Come get some).
2010 form, Worlds 2014. (V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


BRIAN_D2_PLAYER = "Brian Terwilliger"
BRIAN_D2_LS_DECK_NAME = "Where Did You Go?"
BRIAN_D2_DS_DECK_NAME = "Come get some!"


# --- Light: d2p3_p03.png upright. LIGHT checked. Hidden Base / Mon Cal. ---

BRIAN_D2_LS_RESERVE = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),  # 1
    n("Rendezvous Point"),  # 2
    n("Mon Calamari Dockyards", True),  # 3
    n("Superficial Damage", True),  # 4
    n("Republic Logistics", True),  # 5
    n("Heading For The Medical Frigate", True),  # 6
    n("Nar Shaddaa", True),  # 7
    n("Tatooine"),  # 8
    n("Naboo"),  # 9
    n("Kiffex"),  # 10
    n("Mon Calamari"),  # 11
    n("Liberty"),  # 12
    n("Mon Calamari Star Cruiser", True),  # 13
    n("Mon Calamari Star Cruiser", True),  # 14
    n("Mon Calamari Star Cruiser", True),  # 15
    n("Mon Calamari Star Cruiser", True),  # 16
    n("Mon Calamari Star Cruiser", True),  # 17
    n("Defiance"),  # 18
    n("Defiance"),  # 19
    n("Heavy Turbolaser Battery"),  # 20
    n("Heavy Turbolaser Battery"),  # 21
    n("Heavy Turbolaser Battery"),  # 22
    n("Luke Skywalker", True),  # 23
    n("Luke Skywalker", True),  # 24
    n("Boushh"),  # 25
    n("TK-422"),  # 26
    n("Dack Ralter"),  # 27
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 28  Chewie line crossed
    n("Kin Kian"),  # 29
    n("Admiral Ackbar", True),  # 30
    n("Threepio With His Parts Showing"),  # 31
    n("We're Doomed"),  # 32
    n("Choke"),  # 33
    n("Imperial Atrocity", True),  # 34
    n("Imperial Atrocity", True),  # 35
    n("Imperial Atrocity", True),  # 36
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 37
    n("It Could Be Worse"),  # 38  ICBW
    n("Alter", True),  # 39
    n("Yoda Stew & You Do Have Your Moments"),  # 40
    n("Strikeforce", True),  # 41  Day 3 OUT
    n("A Jedi's Plans", True),  # 42
    n("On Target"),  # 43
    n("On Target"),  # 44
    n("On Target"),  # 45
    n("Let The Wookiee Win", True),  # 46
    n("Let The Wookiee Win", True),  # 47
    n("Stay Sharp!"),  # 48
    n("Stay Sharp!"),  # 49
    n("Escape Pod", True),  # 50
    n("Escape Pod", True),  # 51
    n("Projection Of A Skywalker"),  # 52  POAS
    n("Projection Of A Skywalker"),  # 53
    n("Power Pivot"),  # 54
    n("Power Pivot"),  # 55
    n("Rebel Barrier"),  # 56
    n("Grimtaash"),  # 57
    n("Were You Looking For Me?"),  # 58  Day 3 OUT
    n("Hear Me Baby, Hold Together", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

BRIAN_D2_LS_SHIELDS = [
    n("Affect Mind", True),  # 1
    n("Simple Tricks And Nonsense", True),  # 2
    n("Aim High"),  # 3
    n("Wise Advice"),  # 4
    n("Do, Or Do Not", True),  # 5
    n("The Professor"),  # 6  written The sauton
    n("Your Insight Serves You Well", True),  # 7
    n("Jabba's Prize", True),  # 8  shield box; not a shield printing
    n("Let's Keep A Little Optimism Here", True),  # 9  long title
    n("Yavin Sentry", True),  # 10
    n("Ultimatum"),  # 11
    n("Don't Do That Again", True),  # 12
]

BRIAN_D2_LS_ADD = [
    n("Battle Plan"),  # 1
    n("A Tragedy Has Occurred"),  # 2
    n("Chasm", True),  # 3
]


# --- Dark: d2p3_p04.png upright. DARK checked. Wookiee Slaving Operation. ---

BRIAN_D2_DS_RESERVE = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),  # 1
    n("Jabba's Sail Barge: Passenger Deck"),  # 2
    n("Kashyyyk: Slaving Camp Headquarters"),  # 3
    n("Kashyyyk: Skyhook Platform"),  # 4
    n("Kashyyyk: Wookiee Slaving Camp"),  # 5
    n("Kashyyyk"),  # 6
    n("Nal Hutta"),  # 7
    n("Jabba's Haven", True),  # 8
    n("Den Of Thieves & Special Delivery", True),  # 9
    n("Power Of The Hutt"),  # 10
    n("Mercenary Slavers", True),  # 11
    n("Zuckuss In Mist Hunter"),  # 12
    n("Slave I, Symbol Of Fear", True),  # 13
    n("Jabba's Space Cruiser", True),  # 14
    n("Jabba's Sail Barge", True),  # 15
    n("IG-88 In IG-2000", True),  # 16  written Elis in Hunter / IG in Hunter
    n("P-59"),  # 17
    n("Dengar With Blaster Carbine", True),  # 18
    n("Mara Jade With Lightsaber", True),  # 19
    n("Jango Fett, The Assassin", True),  # 20
    n("Garindan", True),  # 21
    n("Boba Fett, Prepared Hunter", True),  # 22
    n("Boba Fett"),  # 23
    n("Dr. Evazan"),  # 24
    n("Guri"),  # 25
    n("4-LOM With Concussion Rifle"),  # 26
    n("Lady Valarian", True),  # 27
    n("Ponda Baba", True),  # 28
    n("Ponda Baba", True),  # 29
    n("Ghhhk", True),  # 30
    n("Bossk With Mortar Gun", True),  # 31
    n("Jabba The Hutt", True),  # 32
    n("Ephant Mon"),  # 33
    n("Prince Xizor"),  # 34
    n("Outer Rim Scout"),  # 35
    n("Outer Rim Scout"),  # 36
    n("Outer Rim Scout"),  # 37
    n("Hutt Bounty", True),  # 38
    n("Wookiee Subjugation", True),  # 39
    n("Force Push", True),  # 40
    n("Short Range Fighters & Watch Your Back!"),  # 41
    n(None),  # 42  Ability x 3 — unread
    n("Cold Feet", True),  # 43
    n("Sunsdown & Too Cold For Speeders"),  # 44  Day 3 OUT
    n("We Must Accelerate Our Plans", True),  # 45  Operational As Planned crossed
    n("Disarmed"),  # 46
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 47
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 48
    n("Elis Helrot"),  # 49
    n("Sonic Bombardment", True),  # 50
    n("Sonic Bombardment", True),  # 51
    n("Sonic Bombardment", True),  # 52
    n("Crush The Rebellion"),  # 53
    n("Imperial Barrier"),  # 54
    n("Open Fire!"),  # 55
    n("Open Fire!"),  # 56
    n("Scum And Villainy"),  # 57
    n("Search And Destroy"),  # 58
    n("Oo-ta Goo-ta, Solo?"),  # 59  Day 3 OUT
    n("Knowledge And Defense", True),  # 60
]

BRIAN_D2_DS_SHIELDS = [
    n("Leave Them To Me", True),  # 1
    n("Secret Plans", True),  # 2
    n("You Cannot Hide Forever", True),  # 3
    n("Firepower", True),  # 4
    n("Come Here You Big Coward", True),  # 5
    n("Oppressive Enforcement", True),  # 6
    n("Resistance", True),  # 7
    n("Battle Order"),  # 8
    n("There Is No Try", True),  # 9
    n("Wipe Them Out, All Of Them", True),  # 10
    n("Abyss", True),  # 11
    n("Allegations Of Corruption"),  # 12
]

BRIAN_D2_DS_ADD = [
    n("Death Star Sentry", True),  # 1
    n("I Find Your Lack Of Faith Disturbing", True),  # 2
    n("Imperial Detention", True),  # 3
]


NOTES = """
Brian Terwilliger / Twigg, 2014 Worlds Day 2, 2010 form.
Light d2p3_p03 Where Did You Go? (LIGHT checked). Hidden Base / Mon Cal.
Dark d2p3_p04 slavers (DARK checked). Day 3 Dark deck name Come get some!

LS: line 28 Chewie crossed, kept Antilles Maneuver & Rebel Reinforcements (V).
Line 41 Strikeforce (V) and 58 Were You Looking For Me? are Day 3 OUTs.
Day 3 also OUTs Darklighter Spin and Out Of Commission (not on this 60).
Shield 8 Jabba's Prize is written in the shield box (not a shield printing).
Shield 9 long title taken as Let's Keep A Little Optimism Here.

DS: line 2 Jabba site taken as Passenger Deck (vehicle is line 15).
Line 16 IG-88 In IG-2000 (Hunter scrawl).
Line 42 Ability x 3 unread.
Line 45 Operational As Planned crossed; We Must Accelerate Our Plans kept.
Lines 44 and 59 are the Day 3 Dark OUTs.
""".strip()


if __name__ == "__main__":
    assert len(BRIAN_D2_LS_RESERVE) == 60, len(BRIAN_D2_LS_RESERVE)
    assert len(BRIAN_D2_LS_SHIELDS) == 12, len(BRIAN_D2_LS_SHIELDS)
    assert len(BRIAN_D2_DS_RESERVE) == 60, len(BRIAN_D2_DS_RESERVE)
    assert len(BRIAN_D2_DS_SHIELDS) == 12, len(BRIAN_D2_DS_SHIELDS)
    print("LS", len(BRIAN_D2_LS_RESERVE), len(BRIAN_D2_LS_SHIELDS), len(BRIAN_D2_LS_ADD))
    print("DS", len(BRIAN_D2_DS_RESERVE), len(BRIAN_D2_DS_SHIELDS), len(BRIAN_D2_DS_ADD))
