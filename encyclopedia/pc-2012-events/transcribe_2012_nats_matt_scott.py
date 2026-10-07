#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Matt Scott.

Source: 2012NationalsDay1.pdf pages 66–67 (typed 2010 Xerox, 12 shields).
p66 Light / p67 Dark Name L. Matt Scott Username blank dested Matt Scott analog leftover
player-stubs/Matt_Scott.wiki. Analog leftover encyclopedia empty.
Pack player-stubs/Matt_Scott.wiki. Do not dest as a new person L. Matt Scott.
"""
from __future__ import annotations

PLAYER = "Matt Scott"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 66
DS_PAGE = 67
LS_SCAN = "2012 US Nationals Day 1 Matt Scott LS.png"
DS_SCAN = "2012 US Nationals Day 1 Matt Scott DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox. Name L. Matt Scott dested Matt Scott analog leftover player-stubs. "
    "Username blank. Event Date 6/9/12 Event Name blank. Do not dest as a new person L. Matt Scott."
)
LS_NOTE = (
    "Typed 2010 Xerox. Name L. Matt Scott dested Matt Scott analog leftover player-stubs. "
    "Username blank. LIGHT checked. Event Date 6/9/12 Event Name blank. "
    "Deck Name as taught as a jedi stays off the article. "
    "LS_START Endor. "
    "Wesa Ready To Do Our-sa Part dested Wesa Ready To Do Our-Sa Part True analog leftover Fernando. "
    "Obi-wan in Radiant VII dested Obi-Wan In Radiant VII True analog leftover Nelson. "
    "Noooooooooooo! dested NOOOOOOOOOOOO! True analog leftover Kurten x3 unique overcount. "
    "AFA dested Anger, Fear, Aggression analog leftover Cooleo IN THE 60. "
    "Shield Do, or Do Not dested Do Or Do Not analog leftover 2013 MPC. "
    "Shield 12 dested The Professor True analog leftover Schoenthal. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name L. Matt Scott dested Matt Scott analog leftover player-stubs. "
    "Username blank. DARK checked. Event Date 6/9/12 Event Name blank. "
    "Deck Name Bantha mafia: stays off the article. "
    "DS_START Hoth. "
    "Hoth: defensive perimeter dested Hoth: Defensive Perimeter analog leftover Rambo. "
    "Im Sorry dested I'm Sorry True analog leftover 2012 MPC Thornton. "
    "Combat Readiness dested Combat Readiness True analog leftover Grouty. "
    "Tie Interceptor dested TIE Interceptor analog leftover Burgt x4. "
    "All power to weapons dested All Power To Weapons analog leftover Haglund x3. "
    "Sunsdowm dested Sunsdown True analog leftover Fernando (separate line from Too Cold For Speeders). "
    "Imperial Decree True + empty stay separate. "
    "Bantha True x9 unique overcount sheet-accurate. "
    "K&D dested Knowledge And Defense analog leftover Cooleo IN THE 60. "
    "Shield Come Here You Big Coward! dested Come Here You Big Coward True analog leftover. "
    "Shield There is No Try dested There Is No Try analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Endor"
LS_CARDS = [
    n("Endor"),
    n("Endor: Rebel Landing Site (Forest)"),
    n("Careful Planning", True),
    n("Strike Planning"),
    n("Ewok Celebration"),
    n("Take The Initiative", qty=2),
    n("Civil Disorder"),
    n("Nar Shaddaa Wind Chimes", qty=3),
    n("Ewok Sentry", qty=11),
    n("Sound The Attack", qty=4),
    n("Yub Yub!", qty=2),
    n("Ewok Catapult", qty=3),
    n("Projection Of A Skywalker", qty=2),
    n("Liberty"),
    n("Spiral"),
    n("Wicket"),
    n("Endor: Hidden Forest Trail"),
    n("Endor: Back Door"),
    n("General Crix Madine"),
    n("Artoo-Detoo In Red 5"),
    n("General Solo"),
    n("Kazak"),
    n("Endor: Chief Chirpa's Hut"),
    n("Logray"),
    n("Graak"),
    n("Romba"),
    n("Wookiee Guide"),
    n("Wuta"),
    n("Anger, Fear, Aggression"),
    n("I Hope She's All Right", True),
    n("Wokling", True),
    n("Wesa Ready To Do Our-Sa Part", True),
    n("Obi-Wan In Radiant VII", True),
    n("Bravo Fighter", True),
    n("NOOOOOOOOOOOO!", True, qty=3),
    n("Luke Skywalker", True),
    n("Chief Chirpa", True),
    n("Endor: Ewok Village", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Weapons Display", True),
    n("Do Or Do Not"),
    n("A Close Race"),
    n("Your Insight Serves You Well"),
    n("Another Pathetic Lifeform"),
    n("Yavin Sentry", True),
    n("Aim High", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred", True),
    n("Battle Plan"),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Hoth"
DS_CARDS = [
    n("Hoth"),
    n("Hoth: Defensive Perimeter"),
    n("Inconsequential Losses", True),
    n("Breached Defenses", True),
    n("I'm Sorry", True),
    n("Combat Readiness", True),
    n("SFS L-s9.3 Laser Cannons", qty=4),
    n("Twi'lek Advisor", qty=4),
    n("Ghhhk", qty=4),
    n("TIE Interceptor", qty=4),
    n("Bantha", True, qty=9),
    n("Bantha Fodder", qty=3),
    n("All Power To Weapons", qty=3),
    n("Frostbite", qty=2),
    n("Image Of The Dark Lord", True),
    n("Imperial Decree", True),
    n("Clouds", qty=2),
    n("Flawless Marksmanship", qty=2),
    n("Limited Resources"),
    n("Presence Of The Force", qty=2),
    n("Floating Refinery", True, qty=3),
    n("Ice Storm", qty=4),
    n("Imperial Decree"),
    n("Sunsdown", True),
    n("Too Cold For Speeders"),
    n("Overload"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("Come Here You Big Coward", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("No Escape"),
    n("Fanfare"),
    n("Allegations Of Corruption"),
    n("Secret Plans", True),
    n("Battle Order"),
    n("Resistance"),
]
DS_ADD = []
