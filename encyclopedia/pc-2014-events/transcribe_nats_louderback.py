#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Nate Louderback.

Source: Nationals-2014-day-1.pdf pages 3–4 (2010 form).
Name Nate L. Username dorshe1. Dest Nate Louderback.
"""
from __future__ import annotations

PLAYER = "Nate Louderback"
USERNAME = "dorshe1"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 US Nationals Day 1 p03 Nate Louderback LS.png"
DS_SCAN = "2014 US Nationals Day 1 p04 Nate Louderback DS.png"
NOTE = "Handwritten 2010 Xerox. Name Nate L.; username dorshe1 dested Nate Louderback."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Nate L. Username dorshe1. Deck name Don't Eratta Me Bro! LIGHT. "
    "RAW/AN dested Republic At War / Aggressive Negotiations. "
    "Geo: Forward Command Center dested Geonosis: Forward Command Center. "
    "Begun, the Clone War Has dested Begun, The Clone War Has. HFTMF dested Heading For The Medical Frigate. "
    "AOM dested Assault On Muunilinst. Mun sites dested Muunilinst: Harnaidan Plains / City Of Harnaidan / Republic Landing Site. "
    "RC: Hidden Landing Site dested Rebel Cell / Hidden Landing Site. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Anakin Skywalker-Padawan dested Anakin Skywalker, Padawan Learner. "
    "Obi-Wan-JK dested Obi-Wan Kenobi, Jedi Knight. All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Sorry About The Mess Combo dested Sorry About The Mess & Blaster Proficiency. AFA dested Anger, Fear, Aggression. "
    "Your Insight dested Your Insight Serves You Well. Unique overcounts sheet-accurate "
    "(AT-RT x10, Dual Laser Cannon x5, Acclamator-Class Assault Ship x2). (V) from checkbox. "
    "NO_DEST (2014 index): Orrin Gart."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Nate L. Username dorshe1. Deck name DS Senate. DARK. "
    "Is That Legal/I Will Make It Legal dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Cor: Senate dested Coruscant: Galactic Senate. Flagship Bridge dested Blockade Flagship: Bridge. "
    "CC: Security Tower dested Cloud City: Security Tower. Naboo: TP Generator Core dested Naboo: Theed Palace Generator Core. "
    "Slave I, SoF dested Slave I, Symbol Of Fear. AKS MOE dested Aks Moe. "
    "ARN FREE TAA dested Orn Free Taa. Yeb Yeb dested Yeb Yeb Maash. "
    "Toonbuck Toora dested Toonbuck Toora. Passel Argente dested Passel Argente. "
    "Edcel Bar Gane dested Edcel Bar Gane. Baskol Yeersam dested Baskol Yeersam. "
    "Tikkes dested Tikkes. Boba Fett, PH dested Boba Fett, Prepared Hunter. "
    "Jango Fett, Assassin dested Jango Fett, The Assassin. EPP Vader dested Darth Vader With Lightsaber. "
    "EPP Darth Maul dested Darth Maul With Lightsaber. Dark Waters dested Dark Waters. "
    "Senate Hover Cam dested Senate Hovercam. SRF Combo dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. GHHHK Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "O Switch Off dested Oh, Switch Off. K+D dested Knowledge And Defense. "
    "CHYBC dested Come Here You Big Coward. IFYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "Unique overcounts sheet-accurate (Lott Dod x3, Orn Free Taa x2, Toonbuck Toora x2, "
    "Baskol Yeersam x2, Darth Maul With Lightsaber x2, Senate Hovercam x2, "
    "Short Range Fighters & Watch Your Back! x2, We Must Accelerate Our Plans x2, "
    "Sonic Bombardment x2, Squabbling Delegates x3, Those Rebels Won't Escape Us x2). (V) from checkbox. "
    "NO_DEST (2014 index): Surprise Assault (V); Yeb Yeb Maash; Baskol Yeersam."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / Aggressive Negotiations"
LS_CARDS = [
    n("Republic At War / Aggressive Negotiations"),
    n("Geonosis: Forward Command Center"),
    n("Begun, The Clone War Has"),
    n("Heading For The Medical Frigate"),
    n("Rogue Squadron Tactics"),
    n("Nick Of Time", True),
    n("Wokling", True),
    n("Assault On Muunilinst"),
    n("Dressel"),
    n("Muunilinst: Harnaidan Plains"),
    n("Muunilinst: City Of Harnaidan"),
    n("Muunilinst: Republic Landing Site"),
    n("Rebel Cell / Hidden Landing Site"),
    n("Azure Angel"),
    n("Alderaan Consular Ship"),
    n("Lady Luck"),
    n("Acclamator-Class Assault Ship", qty=2),
    n("AT-RT", qty=10),
    n("Dual Laser Cannon", True, qty=5),
    n("Anakin Skywalker, Padawan Learner"),
    n("Jaina Solo"),
    n("Phylo Gandish", True),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Chewbacca, Walking Carpet"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Orrin Gart"),
    n("Seeking An Audience", True),
    n("Projection Of A Skywalker"),
    n("Imperial Atrocity"),
    n("Rebel Barrier"),
    n("Weapon Levitation"),
    n("Grimtaash"),
    n("Rebel Artillery"),
    n("It's Not My Fault", True),
    n("Lucky Shot", True),
    n("Houjix"),
    n("Dark Approach", True),
    n("Escape Pod", True),
    n("Slight Weapons Malfunction"),
    n("Away Put Your Weapon", True),
    n("Desperate Tactics"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sorry About The Mess"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Affect Mind", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Aim High"),
]


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Surprise Assault", True),
    n("Blockade Flagship: Bridge"),
    n("Naboo"),
    n("Cloud City: Security Tower"),
    n("Naboo: Theed Palace Generator Core"),
    n("Slave I, Symbol Of Fear"),
    n("Dengar In Punishing One", qty=2),
    n("Stinger"),
    n("Fighters Coming In"),
    n("Black Sun Fleet"),
    n("Lott Dod", qty=3),
    n("Aks Moe"),
    n("Orn Free Taa", qty=2),
    n("Yeb Yeb Maash"),
    n("Toonbuck Toora", qty=2),
    n("Passel Argente"),
    n("Edcel Bar Gane"),
    n("Baskol Yeersam", qty=2),
    n("Tikkes"),
    n("Boba Fett, Prepared Hunter"),
    n("Guri"),
    n("Jango Fett, The Assassin"),
    n("U-3PO (Yoo-Threepio)"),
    n("Darth Vader With Lightsaber"),
    n("Arica"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Dark Waters"),
    n("Image Of The Dark Lord", True),
    n("Jabba's Haven"),
    n("Senate Hovercam", qty=2),
    n("Imperial Propaganda", True),
    n("Our Blockade Is Perfectly Legal"),
    n("Accepting Trade Federation Control"),
    n("This Is Outrageous!"),
    n("Motion Supported"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Sonic Bombardment", qty=2),
    n("Squabbling Delegates", qty=3),
    n("Cold Feet", True),
    n("Those Rebels Won't Escape Us", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Oh, Switch Off"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
]
DS_ADD = [
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
]
