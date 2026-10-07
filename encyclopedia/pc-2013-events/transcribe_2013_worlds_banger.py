#!/usr/bin/env python3
"""2013 World Championship Day 2: Amar Banger informal overlay LS+DS."""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2013 Worlds Day 2 p14 Amar Banger LS.png"
DS_SCAN = "2013 Worlds Day 2 p13 Amar Banger DS.png"
LS_NOTE = (
    "Informal typed overlay (file Scoundrels.html), not a 2010 Xerox Print Form. "
    "Player name Amar Banger. Username blank. Event Worlds 2013. Date 8/10. "
    "Deck title Scoundrels Space. LIGHT. (Vn) tags are Holotable virtual versions. "
    "Line 2 Set To Your Ships struck dested Squadron Assignments. "
    "Line 4 Infiltration/Unlikely Allies dested Infiltration / Unlikely Allies. "
    "Line 32 It Could Be Worse struck dested Scrambled Transmission. "
    "Line 49 R2-D2 (Artoo-Detoo) struck dested Artoo, Brave Little Droid. "
    "LE-BO2D9 (Leebo) dested LE-BO2D9 (Leebo). "
    "Nar Shaddaa: Undercity dested Nar Shaddaa: Undercity. "
    "Nar Shaddaa: Undercity Street dested Nar Shaddaa: Undercity Street. "
    "All Wings Report In & Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Armed And Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Sorry About The Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "15 defensive-shield slots on this overlay."
)
DS_NOTE = (
    "Informal typed overlay (file TTDv.html), not a 2010 Xerox Print Form. "
    "Player name Amar Banger. Username blank. Event Worlds 2013. Date 8/10. "
    "Deck title HDv. DARK. (Vn) tags are Holotable virtual versions. "
    "Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe dested "
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Line 60 Wipe Them Out, All Of Them struck dested The Circle Is Now Complete. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: North Ridge dested Hoth: North Ridge (4th Marker). "
    "After Her! dested After Her!. "
    "Sense & Uncertain Is The Future dested Sense & Uncertain Is The Future. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. "
    "Weapon Levitation & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "15 defensive-shield slots on this overlay."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Squadron Assignments"),
    n("Heading For The Medical Frigate"),
    n("Infiltration / Unlikely Allies", True),
    n("Luke, Trust Me", True),
    n("Nar Shaddaa", True),
    n("Nar Shaddaa: Undercity", True),
    n("Scoundrel's Bravado", True),
    n("Scoundrel's Charm", True),
    n("Scoundrel's Ingenuity", True),
    n("Scoundrel's Luck", True),
    n("Wokling", True),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Boushh"),
    n("Captain Han Solo"),
    n("Chewbacca, Walking Carpet", True),
    n("Corran Horn", qty=2),
    n("Dash Rendar"),
    n("Flash Of Insight", True),
    n("Han's Toolkit"),
    n("I Can't Believe He's Gone", True),
    n("I'll Take The Leader", qty=3),
    n("Imperial Atrocity", True, qty=3),
    n("Scrambled Transmission", True),
    n("Kessel"),
    n("Kessel Run", True),
    n("Kyle Katarn", True, qty=4),
    n("Kyle Katarn's Blaster Rifle", True),
    n("LE-BO2D9 (Leebo)", True),
    n("Lady Luck", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Millennium Falcon"),
    n("Mirax Terrik"),
    n("Nar Shaddaa: Undercity Street", True),
    n("Obi-Wan In Radiant VII", True),
    n("Outrider"),
    n("Pulsar Skate"),
    n("Artoo, Brave Little Droid"),
    n("Red Squadron 7", True),
    n("Run Luke, Run!", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Spaceport Scoundrels Guild", True),
    n("Strikeforce", True),
    n("We Wish To Board At Once", qty=3),
    n("Weapon Levitation"),
    n("Yoda's Gimer Stick"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("There Is Another", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("A Sith's Plans", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Knowledge And Defense", True),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses"),
    n("A Sith's Weapon", True),
    n("Battle Droid Squad", True),
    n("Blaster Rack", True),
    n("Blizzard 4", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Emperor Palpatine", qty=2),
    n("Endor"),
    n("Force Lightning"),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Garindan", True, qty=2),
    n("General Nevar", True),
    n("Ghhhk"),
    n("Grand Admiral Thrawn"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: North Ridge (4th Marker)"),
    n("I've Lost Artoo!", True),
    n("Imperial Justice", True),
    n("Imperial Reinforcements", True),
    n("Juno Eclipse, Black Leader", True),
    n("Mara Jade's Lightsaber", True),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Masterful Move", qty=2),
    n("One Beautiful Thing", True, qty=2),
    n("P-59"),
    n("Restraining Bolt"),
    n("Revenge Of The Sith", True),
    n("Rogue Shadow", True),
    n("Sense & Uncertain Is The Future"),
    n("Sniper & Dark Strike"),
    n("Trophy Of A Kill", True, qty=2),
    n("Vader's Lightsaber"),
    n("Vader's Obsession"),
    n("Victory", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Weapon Levitation & The Empire's Back", True),
    n("The Circle Is Now Complete"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("After Her!", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
