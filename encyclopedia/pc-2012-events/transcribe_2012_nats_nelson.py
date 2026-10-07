#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Aaron Nelson.

Source: 2012NationalsDay1.pdf pages 46–47 (handwritten 2010 Xerox, 12 shields).
p46 Dark other-event bound-in Event Name Nationals 2013 skip.
p47 Light Name Airdog 2003 / Aaron Nelson dested Aaron Nelson analog leftover
2012 MPC / 2013 TMW. Username box blank; Name-box handle dested Airdog2003.
Do not dest as Jake Nelson. Do not dest as Brian Herold.
Do not rewrite 2012 MPC / 2013 TMW / 2013 Worlds / 2013 MPC Nelson leftovers.
Pack player-stubs/Aaron_Nelson.wiki.
"""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 47
DS_PAGE = 46
LS_SCAN = "2012 US Nationals Day 1 Aaron Nelson LS.png"
DS_SCAN = ""
LS_DECK_NAME = "SoCal Scoundrel's"
DS_DECK_NAME = "SoCal RalOps... Version #3720"
NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson analog leftover "
    "2012 MPC / 2013 TMW. Username Airdog2003. p46 Dark Event Name Nationals 2013 "
    "other-event bound-in skip."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Airdog 2003 / Aaron Nelson dested Aaron Nelson "
    "analog leftover 2012 MPC / 2013 TMW. Username box blank; Name-box handle dested "
    "Airdog2003. LIGHT checked. Deck Name SoCal Scoundrel's. Event Name Nationals 2012. "
    "Do not dest as Jake Nelson. Do not dest as Brian Herold. "
    "Do not rewrite 2012 MPC / 2013 TMW / 2013 Worlds / 2013 MPC Nelson leftovers. "
    "Infiltration / Unlikely Allies dested Infiltration / Unlikely Allies analog leftover Martin. "
    "Sgt. Doallyn dested Sergeant Doallyn True analog leftover MPC Nelson. "
    "SATM / BP dested Sorry About The Mess & Blaster Proficiency analog leftover Ziagos. "
    "Han's Blaster, So Uncivilized dested Han's Blaster, So Uncivilized analog leftover Pierre. "
    "Rebel Agent dested Rebel Agent analog leftover Martin x3. "
    "Rebel Agent's Crazy-ass gun dested Rebel Agent's Blaster Rifle analog leftover Martin. "
    "The Bith Shuffle Combo dested The Bith Shuffle & Desperate Reach analog leftover. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Martin x2. "
    "Booster dested Boushh analog leftover x2. "
    "Drawn Their Fire dested Draw Their Fire analog leftover. "
    "Chewie's Bowcaster dested Chewbacca's Bowcaster analog leftover. "
    "Anakin's Saber dested Anakin's Lightsaber True analog leftover. "
    "Booster's Destroyer dested Booster's Star Destroyer analog leftover Martin. "
    "Imperial Nav. Charts dested Imperial Navigation Charts analog leftover Martin. "
    "Obi-Wan in Red VII dested Obi-Wan In Radiant VII analog leftover Chris. "
    "Armed & Dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl analog leftover. "
    "HFAMF dested Heading For The Medical Frigate analog leftover. "
    "I Hope She's All Right dested I Hope She's All Right analog leftover Frafjord. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson Username Airdog 2003. DARK checked. "
    "Deck Name SoCal RalOps... Version #3720. Event Name Nationals 2013. "
    "Other-event bound-in skip. Do not dest this Dark 60 onto 2012 US Nationals. "
    "Do not dest as Jake Nelson. Do not dest as Brian Herold."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Nar Shaddaa: Undercity Street"),
    n("Scoundrel's Guild"),
    n("Mirax Terrik"),
    n("R2-D2", True),
    n("Chewbacca, Walking Carpet"),
    n("Let The Wookiee Win", True),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sergeant Doallyn", True),
    n("Third Sight", True),
    n("Han's Blaster, So Uncivilized"),
    n("Double Agent"),
    n("Booster In Pulsar Skate", qty=2),
    n("Landing Claw"),
    n("I Hope She's All Right"),
    n("Rebel Agent", qty=3),
    n("Rebel Agent's Blaster Rifle"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Imperial Atrocity", True),
    n("Corran Horn", qty=2),
    n("Houjix"),
    n("Seeking An Audience", True),
    n("Who's Born To Beat At Once", qty=2),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Escape Pod", True, qty=2),
    n("K'lor'slug", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Flash Of Insight", True),
    n("Let The Wookiee Win", True),
    n("Boushh", qty=2),
    n("Draw Their Fire"),
    n("Chewbacca's Bowcaster"),
    n("Anakin's Lightsaber", True),
    n("Booster's Star Destroyer"),
    n("Imperial Navigation Charts"),
    n("I Can't Believe He's Gone", True),
    n("Obi-Wan In Radiant VII"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Chewbacca, Walking Carpet"),
    n("Scoundrel's Trick"),
    n("Scoundrel's Ingenuity"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Bravado"),
    n("Heading For The Medical Frigate"),
    n("A Good Blaster At Your Side"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("There Is Another"),
]
LS_ADD = []

DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
