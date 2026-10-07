#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Chris O'Hara Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Chris O'Hara"
USERNAME = "Fullensith"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 68
DS_PAGE = 67
LS_SCAN = "2013 Match Play Championship p68 Chris O'Hara LS.png"
DS_SCAN = "2013 Match Play Championship p67 Chris O'Hara DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Chris O'Hara (username Fullensith). Light. "
    "Deck title Pile. Event MPC 2013, 26 January 2013. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Houjix + Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Sense + Recoil In Fear dested Sense & Recoil In Fear. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army. "
    "Speak w/ the Jedi Council dested Speak With The Jedi Council. "
    "LTWW dested Let The Wookiee Win. "
    "Sorry About the Mess / BP dested Sorry About The Mess & Blaster Proficiency. "
    "AJTR dested A Jedi's Resilience. Control / TV dested Control & Tunnel Vision. "
    "FSYH / HG dested Found Someone You Have & Higher Ground. "
    "Strike Force dested Strikeforce. Seek an Audience dested Seeking An Audience. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas. LS, JK dested Luke Skywalker, Jedi Knight. "
    "LS SITF dested Luke Skywalker, Strong In The Force. "
    "Qui-Gon w/ stick dested Qui-Gon Jinn With Lightsaber. "
    "Lando Calrissian, Scoundrel (nonV) dested Lando Calrissian, Scoundrel. "
    "3PO w/ parts dested Threepio With His Parts Showing. "
    "Coruscant: Jedi Chamber dested Coruscant: Jedi Council Chamber. "
    "Naboo: Boss Nass's dested Naboo: Boss Nass' Chambers. "
    "Home 1: WR dested Home One: War Room. Obi-Wan Journal dested Obi-Wan's Journal. "
    "Obi-Wan's Lightsaber (Prem) dested Obi-Wan's Lightsaber. "
    "HC + TF (nonV) dested Han, Chewie, And The Falcon. "
    "Y4: War Room dested Yavin 4: Massassi War Room. AFA dested Anger, Fear, Aggression. "
    "Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "LKALOH dested Let's Keep A Little Optimism Here. "
    "YISYW dested Your Insight Serves You Well. "
    "Simple Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "PDTA dested Don't Do That Again. Do or Do Not dested Do, Or Do Not. "
    "Form left column reprints 37–38 on lines 39–40 are Obi-Wan Kenobi. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Chris O'Hara (username Fullensith). Dark. "
    "Deck title Pile of Spice. Event MPC 2013, 26 January 2013. "
    "Kessel + CR dested Kessel and Combat Readiness. "
    "Kessel: Spice mines ADMIN office dested Kessel: Spice Mines - Administrator's Office. "
    "A Sith's Plans dested A Sith's Plans. I'll Take Them Myself dested I'll Take Them Myself. "
    "Admiral ditto Ozzel dested Admiral Ozzel. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle. "
    "Spice Mine Admin dested Moruth Doole, Kessel Administrator. "
    "Maul w/ Stick dested Darth Maul With Lightsaber. "
    "Mara w/ Stick dested Mara Jade With Lightsaber. "
    "U-3PO dested U-3PO (Yoo-Threepio). Imp Command dested Imperial Command. "
    "MM / EO dested Masterful Move & Endor Occupation. "
    "Imp. Barrier dested Imperial Barrier. Imp. Decree dested Imperial Decree. "
    "S.S.P.F.T. dested Something Special Planned For Them. "
    "DTHACC? dested Do They Have A Code Clearance?. "
    "HINR / IP dested He Is Not Ready (combo title is not in the 2013 pool). "
    "WAYTT, … T? dested Where Are You Taking This ... Thing?. "
    "WIAPN dested We're In Attack Position Now. "
    "Kessel: Spice Mines Ext. Facility dested Kessel: Spice Mines - Extraction Facility. "
    "Spice Mines Op dested Spice Mine Operations. "
    "Kessel Surveillance System dested Kessel Surveillance System. "
    "K+D dested Knowledge And Defense. CHYBC dested Come Here You Big Coward. "
    "You Cannot Hide Forever dested You Cannot Hide Forever. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40 are Where Are You Taking This ... Thing? "
    "and Lateral Damage. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Clash Of Sabers"),
    n("Houjix & Out Of Nowhere"),
    n("Sense & Recoil In Fear"),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi Council"),
    n("Let The Wookiee Win", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Control & Tunnel Vision"),
    n("Found Someone You Have & Higher Ground", True),
    n("Imperial Atrocity", True, qty=2),
    n("Mantellian Savrip", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Civil Disorder", True),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Admiral Ackbar", True),
    n("Mace Windu", True, qty=3),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", True),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Threepio With His Parts Showing"),
    n("Kiffex"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Home One"),
    n("Spiral"),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Battle Plains"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("The Professor", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("A Sith's Plans", True),
    n("Endor Shield", True),
    n("I'll Take Them Myself", True),
    n("Admiral Chiraneau"),
    n("Admiral Ozzel"),
    n("Grand Moff Tarkin", True),
    n("Admiral Piett"),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Grand Admiral Thrawn"),
    n("General Veers"),
    n("Darth Vader", True),
    n("4-LOM With Concussion Rifle", True),
    n("Moruth Doole, Kessel Administrator", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Mara Jade With Lightsaber", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Imperial Command", qty=3),
    n("Control"),
    n("Close Call", True),
    n("Masterful Move & Endor Occupation"),
    n("Trample"),
    n("Cold Feet", True),
    n("Overwhelmed"),
    n("Monnok"),
    n("Imperial Barrier"),
    n("Ghhhk"),
    n("Imperial Decree"),
    n("Protocol Failure"),
    n("Image Of The Dark Lord", True),
    n("Something Special Planned For Them", True),
    n("Do They Have A Code Clearance?"),
    n("He Is Not Ready", True),
    n("Where Are You Taking This ... Thing?", True),
    n("Lateral Damage"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Tempest 1"),
    n("Conquest", True),
    n("Tyrant"),
    n("Devastator", True),
    n("Thunderflare"),
    n("Victory", True),
    n("Blockade Support Ship", True),
    n("We're In Attack Position Now", qty=3),
    n("Kessel: Spice Mines - Extraction Facility", True),
    n("Kashyyyk"),
    n("Endor"),
    n("Spice Mine Operations", True),
    n("Kessel Surveillance System", True),
    n("Imperial Justice", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Firepower", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Imperial Detention", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
