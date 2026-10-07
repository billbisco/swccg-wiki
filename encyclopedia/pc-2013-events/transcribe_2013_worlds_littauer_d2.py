#!/usr/bin/env python3
"""2013 World Championship Day 2: Ross Littauer Xerox Norsense + Stuff."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_worlds_littauer import (  # noqa: E402
    DS_ADD as D1_DS_ADD,
    DS_CARDS as D1_DS_CARDS,
    DS_SHIELDS as D1_DS_SHIELDS,
    DS_START as D1_DS_START,
    n,
)

PLAYER = "Ross Littauer"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 61
DS_PAGE = 60
LS_SCAN = "2013 Worlds Day 2 p61 Ross Littauer LS.png"
DS_SCAN = "2013 Worlds Day 2 p60 Ross Littauer DS.png"
DS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 1 p05 Ross Littauer DS.png",
        "Page 5 of [[:File:2013 Worlds Day 1.pdf]].",
    )
]
DS_PUBLIC_NOTE = (
    "Day 2 Dark is the same as the Day 1 Hunt Down list, with the substitutions "
    "written on the Day 2 sheet."
)
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Ross Littauer. Username blank. "
    "Email [redacted]. Event worlds Day 2, dated 08/10/13. "
    "Deck title Stuff. LIGHT. "
    "Do not rewrite the Day 1 Ross Littauer leftover. "
    "Infiltration / Unlikely Allies dested Infiltration / Unlikely Allies. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Saitorr Kal Fas dested Sai'torr Kal Fas. "
    "Chewie walking carpet dested Chewbacca, Walking Carpet. "
    "Obi in Radiant VII dested Obi-Wan In Radiant VII. "
    "Inconsequential Barriers dested Inconsequential Barriers. "
    "Han, Innocent Scoundrel dested Han Solo, Innocent Scoundrel. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Lando's Yacht dested Lando's Luxury Yacht. "
    "Boushh dested Boushh. Rebel Agent dested Kyle Katarn. "
    "Leia's blaster rifle dested Leia's Blaster Rifle. "
    "Either way you win dested Either Way, You Win. "
    "Sergeant Doallyn dested Sergeant Doallyn. "
    "Much to learn you still have dested Much To Learn, You Still Have. "
    "Imp atrocity dested Imperial Atrocity. "
    "Spaceport Scoundrel's guild dested Spaceport Scoundrels Guild. "
    "Nar Shaddaa: Scoundrel's Rest dested Nar Shaddaa: Scoundrel's Rest. "
    "Nar Shaddaa: Undercity Street dested Nar Shaddaa: Undercity Street. "
    "I can't believe he's gone dested I Can't Believe He's Gone. "
    "Han's blaster, so uncivilized dested Han's Blaster, So Uncivilized. "
    "Rebel agent's blaster rifle dested Kyle Katarn's Blaster Rifle. "
    "Imp nav charts dested Imperial Navigation Charts. "
    "Booster's star destroyer dested Booster In Pulsar Skate. "
    "AWRI / Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "K'lor slug dested K'lor'slug. ICBZ dested ICBZ. "
    "SATM / blaster proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Additional Let's Keep A Little Optimism Here / Ultimatum / Affect Mind "
    "moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Ross Littauer. Username blank. "
    "Email [redacted]. Event worlds day 2, dated 08/10/13. "
    "Deck title Norsense. DARK. Same as Yesterday with substitutions. "
    "Do not rewrite the Day 1 Ross Littauer leftover. "
    "OUT Emperor's Power, Boba Fett, Bounty Hunter (both copies), "
    "Dr. Evazan & Ponda Baba. "
    "IN Force Field (V), Weapon Lev Combo, Jango Fett, Vader's Obsession. "
    "The Day 2 sheet is otherwise a copy of Day 1 page 5."
)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Anger, Fear, Aggression", True),
    n("Scoundrel's Luck"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Ingenuity"),
    n("Scoundrel's Charm"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("A Good Blaster At Your Side"),
    n("Sai'torr Kal Fas", True),
    n("Chewbacca, Walking Carpet"),
    n("Obi-Wan In Radiant VII"),
    n("Inconsequential Barriers"),
    n("We Wish To Board At Once", qty=2),
    n("Lando's Luxury Yacht"),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Corran Horn", qty=2),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Landing Claw"),
    n("Chewbacca, Walking Carpet"),
    n("Boushh", qty=2),
    n("Leia's Blaster Rifle"),
    n("Either Way, You Win", True),
    n("Sergeant Doallyn", True),
    n("Much To Learn, You Still Have"),
    n("Han's Toolkit"),
    n("Mirax Terrik"),
    n("Imperial Atrocity", True, qty=2),
    n("Kyle Katarn", qty=3),
    n("Spaceport Scoundrels Guild"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Nar Shaddaa: Undercity Street"),
    n("I Can't Believe He's Gone", True),
    n("Han's Blaster, So Uncivilized"),
    n("Kyle Katarn's Blaster Rifle"),
    n("Imperial Navigation Charts"),
    n("Booster In Pulsar Skate"),
    n("All Wings Report In & Darklighter Spin"),
    n("K'lor'slug", True),
    n("ICBZ", True),
    n("Chewbacca's Bowcaster"),
    n("Let The Wookiee Win", True),
    n("Seeking An Audience", True),
    n("Redeemed Apprentice"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Mechanical Failure"),
    n("Sorry About The Mess & Blaster Proficiency"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Weapons Display", True),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Affect Mind", True),
]
LS_ADD = []


def _d2_norsense():
    out = []
    skip_boba = False
    for qty, name, v in D1_DS_CARDS:
        if name == "Emperor's Power":
            continue
        if name == "Dr. Evazan & Ponda Baba":
            continue
        if name == "Boba Fett, Bounty Hunter":
            skip_boba = True
            continue
        if name == "Force Field":
            out.append((qty + 1, name, v))
            continue
        if name == "Weapon Levitation & The Empire's Back":
            out.append((qty + 1, name, v))
            continue
        out.append((qty, name, v))
    out.append(n("Jango Fett"))
    out.append(n("Vader's Obsession"))
    return out


DS_START = D1_DS_START
DS_CARDS = _d2_norsense()
DS_SHIELDS = list(D1_DS_SHIELDS)
DS_ADD = list(D1_DS_ADD)
