#!/usr/bin/env python3
"""2013 Alderaan Regionals: Chris Schoenthal handwritten 2010 Xerox LS+DS.

Name field Chris Schowthyl. Username imrhil327 as written. Dest Chris Schoenthal.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Chris Schoenthal"
USERNAME = "imrhil327"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2013 Alderaan Regionals p21 Chris Schoenthal LS.png"
DS_SCAN = "2013 Alderaan Regionals p22 Chris Schoenthal DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). Name Chris Schowthyl "
    "dested Chris Schoenthal. Username imrhil327 as written. Event Ald Regionals 7/13/13. "
    "LIGHT checked. Deck Name WYS. WYS/TPCBALR empty dested Watch Your Step / "
    "This Place Can Be A Little Rough without True. I Must Be Allowed To Speak dested "
    "I Must Be Allowed To Speak True. Tatooine: C dested Tatooine: City. Tatooine: DB 94 dested "
    "Tatooine: Docking Bay 94. Lars Farm dested Tatooine: Lars' Moisture Farm True. "
    "Flash of Insight dested Flash Of Insight True. Wookiee Strangle dested Wookiee Strangle True. "
    "Han Solo Courageous Smuggler dested Han Solo, Courageous Smuggler as written. "
    "AWRI & Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Fallen Hero dested Fallen Hero as written. "
    "I'll Take The Leader dested I'll Take The Leader. And Then Some crossed, skipped. "
    "Chewie's Bowcaster dested Chewbacca's Bowcaster True. Chewie PRO dested Chewie, Protector as written. "
    "Sergeant Dolleyn dested Sergeant Dolleyn as written. Rayce Ryioda dested Rayce as written. "
    "LE-BO2D9 (Leeby) dested LE-BO2D9. Old Ben dested Old Ben as written. "
    "BoShek's Mad Freighter dested BoShek's Mad Freighter as written. Bespin Tank dested "
    "Bespin Tank as written. Moving to Attack Position dested Moving To Attack Position. "
    "K'lor Slug dested K'lor'slug True. Blast The Door Kid dested Blast The Door, Kid!. "
    "Control/TV dested Control & Tunnel Vision. Cassin Brent dested Cassin Brent as written. "
    "X-wing Cannons dested X-wing Laser Cannon. HFTMF dested Heading For The Medical Frigate. "
    "AFA dested Anger, Fear, Aggression True. Unique overcounts sheet-accurate "
    "(Houjix x2, Artoo-Detoo In Red 5 x2, Fallen Hero x2, Melas x2, AWRI combo x2, Dash Rendar x2, "
    "Control combo x2). Main 59 after crossed line 28 skipped. (V) from the checkbox; dittos inherit "
    "the first named line except where the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). Name Chris Schowthyl "
    "dested Chris Schoenthal. Username imrhil327 as written. Event Ald Regionals 7/13/13. "
    "DARK checked. Deck Name Rops. Line 1 objective empty dested Ralltiir Operations / "
    "In The Hands Of The Empire from Deck Name. See dested See as written. Kren dested Kren as written. "
    "Shannons dested Shannons as written. 13 from dested 13 from as written. "
    "Scribbled lines 14-16 crossed, skipped. RIDE dested RIDE as written. "
    "Right column empty. Shields empty. Additional empty. Sparse sheet dested as written."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Wokling", True),
    n("I Must Be Allowed To Speak", True),
    n("Get To Your Ships"),
    n("Tatooine: City"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Cantina"),
    n("Imperial Atrocity"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Kessel"),
    n("Flash Of Insight", True),
    n("Wookiee Strangle", True),
    n("Lando With Blaster Rifle"),
    n("Rebel Barrier"),
    n("Han Solo, Courageous Smuggler", True),
    n("Luke Skywalker"),
    n("All Wings Report In & Darklighter Spin"),
    n("Seeking An Audience", True),
    n("Artoo-Detoo In Red 5"),
    n("Artoo-Detoo In Red 5"),
    n("Dodge"),
    n("Fallen Hero"),
    n("Chewbacca", True),
    n("Houjix"),
    n("Houjix"),
    n("BoShek, Brash Smuggler"),
    n("I'll Take The Leader"),
    n("Chewbacca's Bowcaster", True),
    n("Chewie, Protector"),
    n("Melas", True),
    n("Sergeant Dolleyn", True),
    n("Fallen Hero"),
    n("Kessel Run"),
    n("Obi-Wan Kenobi"),
    n("Dash Rendar"),
    n("Rayce", True),
    n("LE-BO2D9"),
    n("All Wings Report In & Darklighter Spin"),
    n("Old Ben"),
    n("BoShek's Mad Freighter"),
    n("Millennium Falcon"),
    n("Bespin Tank"),
    n("Moving To Attack Position"),
    n("Wedge Antilles", True),
    n("Pulsar Skate"),
    n("K'lor'slug", True),
    n("Melas", True),
    n("Blast The Door, Kid!"),
    n("Mirax Terrik"),
    n("Escape Pod", True),
    n("Control & Tunnel Vision"),
    n("Control & Tunnel Vision"),
    n("Cassin Brent"),
    n("Antilles Maneuver"),
    n("Dash Rendar"),
    n("Corellia", True),
    n("X-wing Laser Cannon"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Jabba's Prize", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("See"),
    n("Kren"),
    n("Shannons"),
    n("13 from"),
    n("RIDE"),
]
DS_SHIELDS = []
DS_ADD = []
