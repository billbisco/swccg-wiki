#!/usr/bin/env python3
"""Day 3 Xerox transcription: unnamed P01 Dark 60 + P11–P14 change sheets.

Source scans: extract/day3_r_p01.png and day3_r_p11.png–day3_r_p14.png
(2014 Day 3 PDF, rotated). (V) follows the sheet checkbox, or a handwritten
(V) on change sheets that leave the box empty. Dittos: none on these pages.
"""
from __future__ import annotations

# --- helpers ---

def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


def c(name: str | None, v: bool = False, qty: int = 1) -> tuple[str | None, bool, int]:
    return (name, v, qty)


# --- TASK A: day3_r_p01.png, 2010 Dark form, unnamed ---
# Deck name HDv. Name / Username / E-mail boxes blank.
# Objective line is Imperial Occupation, not Hunt Down.

P01_DECK_NAME = "HDv"
P01_PLAYER_NAME = None  # name field blank

P01_DS_RESERVE = [
    n("Imperial Occupation / Imperial Control", True),  # 1
    n("Hoth: Main Power Generators", True),  # 2
    n("Blizzard 4"),  # 3
    n("AT-AT Commander", True),  # 4
    n("Control & Set For Stun"),  # 5
    n("Hoth: Defensive Perimeter (3rd Marker)"),  # 6  written Hoth: 3rd Marker
    n("A Dark Time For The Rebellion", True),  # 7
    n("Cease Fire!"),  # 8
    n("No Escape"),  # 9
    n("Cyclone Walker", True),  # 10
    n("Admiral Piett"),  # 11
    n("Juno Eclipse, Black Leader", True),  # 12  written Juno Eclipse, Blk Leader
    n("Imperial Command"),  # 13
    n("Maarek Stele, The Emperor's Reach", True),  # 14
    n("AT-AT Deployment Platform", True),  # 15
    n("Prepared Defenses", True),  # 16
    n("Victory", True),  # 17  vb7 virtual-only; box checked
    n("Alert My Star Destroyer!"),  # 18
    n("AT-AT Deployment Platform", True),  # 19
    n("Cyclone Walker", True),  # 20
    n("Grand Moff Tarkin", True),  # 21
    n("Sniper & Dark Strike"),  # 22  written Sniper + Dark Strike
    n("Do They Have A Code Clearance?", True),  # 23
    n("General Veers", True),  # 24  written Veers
    n("Admiral Motti", True),  # 25
    n("General Nevar"),  # 26  box empty-ish; virtual-only
    n("Hoth Blockade", True),  # 27
    n("Flagship Executor"),  # 28
    n("Cyclone Walker", True),  # 29
    n("Hoth: Ice Plains", True),  # 30
    n("We're In Attack Position Now"),  # 31
    n("AT-AT Cannon", True),  # 32
    n("Blizzard 1"),  # 33
    n("U-3PO (Yoo-Threepio)"),  # 34  written U-3PO
    n("You May Start Your Landing", True),  # 35
    n("Stop Motion", True),  # 36
    n("A Dark Time For The Rebellion", True),  # 37
    n("Tempest 1"),  # 38
    n("Commander Igar"),  # 39
    n("Hoth"),  # 40
    n("Conquest", True),  # 41
    n("Fleet Security Protocols", True),  # 42  written Fleet Security Controls
    n("Hoth: Mountains (6th Marker)"),  # 43  written Hoth: 6th Marker
    n("Imperial Decree"),  # 44
    n("Endor Shield", True),  # 45
    n("Target The Main Generator"),  # 46
    n("Image Of The Dark Lord", True),  # 47
    n("Coruscant", True),  # 48  box checked; no Coruscant (V) system in 2014
    n("We're In Attack Position Now"),  # 49
    n("Grand Admiral Thrawn"),  # 50
    n("Darth Vader", True),  # 51
    n("Force Push", True),  # 52
    n("Trample"),  # 53
    n("Walker Garrison"),  # 54
    n("Jango Fett, The Assassin", True),  # 55
    n("Cold Feet", True),  # 56
    n("Imperial Command"),  # 57
    n("Control & Set For Stun"),  # 58
    n("Conquest", True),  # 59
    n("Knowledge And Defense", True),  # 60
]

P01_DS_SHIELDS = [
    n("Come Here You Big Coward"),  # 1
    n("Abyss", True),  # 2
    n("Allegations Of Corruption"),  # 3
    n("Secret Plans"),  # 4
    n("Battle Order"),  # 5
    n("Fanfare", True),  # 6
    n("Firepower", True),  # 7
    n("You Cannot Hide Forever", True),  # 8
    n("A Useless Gesture", True),  # 9
    n("Leave Them To Me", True),  # 10
    n("Oppressive Enforcement"),  # 11
    n("Resistance"),  # 12
]

P01_DS_ADD = [
    n("There Is No Try"),  # 1
    n("Death Star Sentry", True),  # 2
    n("Imperial Detention", True),  # 3
]


# --- TASK B: change sheets only ---

# day3_r_p11.png — Aaron Kingery, 2013 form. LIGHT/DARK boxes both empty.
# Cards are Light (Fearlessness, Strikeforce, Grimtaash, Don't Do That Again).
AARON_P11 = {
    "side": "Light",
    "player": "Aaron Kingery",
    "deck_name": None,
    "out": [
        c("Fearlessness"),  # minus; (V) box empty
        c("Strikeforce", True),  # written Strike Force (V)
    ],
    "in": [
        c("Grimtaash"),
        c("Don't Do That Again"),  # written DontDoAgn; (V) box empty
    ],
}

# day3_r_p12.png — Aaron Kingery, 2013 form. LIGHT/DARK both empty.
# Cards are Dark (Imperial Artillery, Sneak Attack, Garrison).
AARON_P12 = {
    "side": "Dark",
    "player": "Aaron Kingery",
    "deck_name": None,
    "out": [
        c("Imperial Artillery"),  # minus
        c("Sneak Attack", True),  # handwritten (V)
        c("Walker Garrison", True),  # written Garrison (V)
    ],
    "in": [
        c("MWCS"),  # plus; abbreviation unexpanded
    ],
}

# day3_r_p13.png — Brian Twigg Dark "Come get some!"  DARK checked.
# Forum (eltwigg, t56104): OUT Oo-ta Goo-ta, Solo? and Too Cold combo;
# IN 2nd Garindan (V) and Hutt Smooch combo. Sheet agrees on the pairings;
# Garindan (V) box is empty on the Xerox.
BRIAN_DS_P13 = {
    "side": "Dark",
    "player": "Brian Terwilliger",
    "deck_name": "Come get some!",
    "out": [
        c("Sunsdown & Too Cold For Speeders"),  # minus; split Sunsdown | Too Cold
        c("Oo-ta Goo-ta, Solo?"),  # minus; written OOTA Goota / Solo
    ],
    "in": [
        c("Garindan"),  # plus; forum says Garindan (V)
        c("Defensive Fire & Hutt Smooch"),  # plus; DefensFire + Hutt Smooch
    ],
}

# day3_r_p14.png — Brian Light "What some?"  LIGHT checked. Worlds Day 3.
BRIAN_LS_P14 = {
    "side": "Light",
    "player": "Brian Terwilliger",
    "deck_name": "What some?",
    "out": [
        c("Darklighter Spin"),  # minus line DARKLIGHTER/OCC — see NOTES
        c("Out Of Commission"),  # same minus-line, written OCC
        c("Were You Looking For Me?"),  # minus; Were you / looking for me
        c("Strikeforce", True),  # minus; Strike Force (V)
    ],
    "in": [
        c("Flash Of Insight", True),  # plus; FlashIns / Insight (V)
        c("Escape Pod", True),  # plus, heavily scribbled; may be voided
    ],
}


NOTES = """
P01 name-field: blank. Username and E-mail blank. Deck name HDv (not Hunt Down;
objective is Imperial Occupation). A stray T sits in the small box right of
Deck Name — form artifact, not a player initial.

P01 uncertain:
- Line 26 General Nevar: (V) box looks empty (photocopy speckle). Card is
  virtual-only (vb7); other virtual-only lines on this sheet are checked.
- Line 38 Tempest 1: (V) box empty/faint; no Tempest 1 (V) in 2014 virtual.
- Line 48 Coruscant: (V) checked. No Coruscant (V) system in Blocks 1–9;
  Decipher Coruscant system is the match.
- Line 42 written Fleet Security Controls → Fleet Security Protocols.
- Line 22 written Sniper + Dark Strike → Sniper & Dark Strike (not Search
  And Destroy).
- Line 51 Darth Vader (V) left as Darth Vader, not Dark Lord Of The Sith.
- Line 24 Veers → General Veers.
- Add 3 Imperial Detention (shield listed under Additional Cards).

AARON_P11: LIGHT/DARK checkboxes empty; side inferred Light. Fearlessness is
not in card_title_map.json (sheet reading). Don't Do That Again confirmed
(DontDoAgn; not Don't Tread On Me). Strikeforce (V) written Strike Force (V).

AARON_P12: LIGHT/DARK empty; side inferred Dark. MWCS unexpanded (plus).
Could be Mara Jade With Lightsaber if the third letter is L (MWLS); the
stroke reads as C. Faint 'cyan when' under MWCS is bleed-through, ignored.
Line 27 is a lone plus with no title (not counted). Garrison (V) → Walker
Garrison (V).

BRIAN_DS_P13: Forum t56104 eltwigg matches the OUT/IN pair. Garindan (V) is
forum-only; Xerox does not check (V). Lines 20–23 are a scribbled first try
at the Hutt Smooch combo; the kept write is Defensive Fire + Hutt Smooch.

BRIAN_LS_P14: DARKLIGHTER/OCC is one minus-line with a slash (same style as
P13 Sunsdown|Too Cold). Split as Darklighter Spin + Out Of Commission; the
combo All Wings Report In & Darklighter Spin is the other Darklighter
expansion. Escape Pod (V) plus is under heavy scribble (lines 14–18) and
may have been voided. Were You Looking For Me? not Were You Trying To Warn
Them?
""".strip()


if __name__ == "__main__":
    assert len(P01_DS_RESERVE) == 60, len(P01_DS_RESERVE)
    assert len(P01_DS_SHIELDS) == 12, len(P01_DS_SHIELDS)
    assert len(P01_DS_ADD) == 3, len(P01_DS_ADD)
    print("P01 reserve", len(P01_DS_RESERVE), "shields", len(P01_DS_SHIELDS), "add", len(P01_DS_ADD))
    for label, d in (
        ("P11", AARON_P11),
        ("P12", AARON_P12),
        ("P13", BRIAN_DS_P13),
        ("P14", BRIAN_LS_P14),
    ):
        print(label, d["side"], "out", d["out"], "in", d["in"])
