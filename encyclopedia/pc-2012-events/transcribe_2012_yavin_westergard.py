#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Chris Westergard.

Source: Yavin42012.pdf pages 1–2.
p01 Light handwritten 2010 Xerox / p02 Dark handwritten 2010 Xerox.
Name blank Username blank. Deck Name C West dested Chris Westergard analog leftover
generate_2012_nats.py CANON Chris West / player-stubs/Chris_Westergard.wiki /
transcribe_2012_mpc_westergard.py. LIGHT/DARK empty dest facing pair analog leftover Cooleo.
Event Date blank dest both as Yavin 4 facing pair analog leftover Cooleo.
Pack player-stubs/Chris_Westergard.wiki.
Do not dest as Jan Westergard. Do not dest as a new person.
Do not dest 2012 MPC Day 1 Chris Westergard 60s again.
"""
from __future__ import annotations

PLAYER = "Chris Westergard"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2012 Yavin 4 Regionals Chris Westergard LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Chris Westergard DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p01 Light handwritten 2010 Xerox / p02 Dark handwritten 2010 Xerox. "
    "Name blank Username blank. Deck Name C West dested Chris Westergard analog leftover "
    "generate_2012_nats.py CANON Chris West / player-stubs/Chris_Westergard.wiki. "
    "LIGHT/DARK empty dest facing pair analog leftover Cooleo. "
    "Event Date blank dest both as Yavin 4 facing pair analog leftover Cooleo. "
    "Do not dest as Jan Westergard. Do not dest as a new person. "
    "Do not dest 2012 MPC Day 1 Chris Westergard 60s again. "
    "Pack player-stubs/Chris_Westergard.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p01 Light. Name blank Username blank. Deck Name C West dested Chris Westergard. "
    "LIGHT/DARK empty dest Light from the 60 analog leftover Cooleo. Event Date blank. "
    "There Is Good In Him dested analog leftover Kurten. "
    "Endor Chief Chirpas Hut dested Endor: Chief Chirpa's Hut analog leftover typical. "
    "End. Docking Bay dested Endor: Docking Bay analog leftover typical. "
    "Luke Rebel Scout dested Luke Skywalker, Rebel Scout analog leftover typical. "
    "Coruscant JCC dested Coruscant: Jedi Council Chamber analog leftover typical. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover Hanson. "
    "Naboo Battle Order dested Naboo: Battle Plains analog leftover Hanson. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Walseth. "
    "Mace Windu empty lines 12–13 dest qty=2 at first. "
    "Luke Jedi Knight dested Luke Skywalker, Jedi Knight analog leftover Hanson. "
    "Qui-Gon w/ lightsaber empty line 15 and Qui-Gon Jinn w/ stick empty line 19 dest Qui-Gon Jinn With Lightsaber qty=2 at first analog leftover non-consecutive. "
    "Yoda MOTF empty lines 16–17 dest Yoda, Master Of The Force qty=2 analog leftover typical. "
    "Obi w/ stick dested Obi-Wan With Lightsaber analog leftover Hanson. "
    "Padme Naberrie dested analog leftover Hanson. "
    "Lt. Blount dested Lieutenant Blount analog leftover typical. "
    "3PO w/ parts dested Threepio With His Parts Showing analog leftover Hanson. "
    "Don't Tread on me dested Don't Tread On Me analog leftover typical. "
    "Jedi Lev dested Jedi Levitation analog leftover typical. "
    "Nabrun dested Nabrun Leids analog leftover Cooleo. "
    "Sense & Recoil empty lines 31–33 dest qty=3 at first. "
    "Wessa dested Wesa Gotta Grand Army analog leftover Hanson qty=2. "
    "Smoke Screen empty lines 38–40 dest qty=3 at first. "
    "Sorry & BP dested Sorry About The Mess & Blaster Proficiency analog leftover Hanson qty=2. "
    "Speak w/ the Jedi Council dested Speak With The Jedi Council analog leftover typical. "
    "A Jedi's Resilience empty lines 46–47 dest qty=2 analog leftover Hanson. "
    "Starship Lev dested Starship Levitation analog leftover typical. "
    "I'm w/ You too dested I'm With You Too analog leftover nats Walseth. "
    "Ewok Cat dested Ewok Catapult analog leftover typical. "
    "Leia's Blaster Rifle dested analog leftover Walseth. "
    "Imp. Atrocity True lines 55–56 ditto dest qty=2 analog leftover nats Walseth. "
    "Tatooine IV dested Tatooine analog leftover typical. "
    "Proj Hope dested Projection Of A Skywalker analog leftover Hanson. "
    "GL dested Gift Of The Mentor analog leftover typical. "
    "Shields 1–12 empty skip analog leftover empty. Unique 60 shields 0."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p02 Dark. Name blank Username blank. Deck Name C West dested Chris Westergard. "
    "LIGHT/DARK empty dest Dark from the 60 analog leftover Cooleo. Event Date blank. "
    "Endor Ops dested Endor Operations / Imperial Outpost analog leftover Walseth. "
    "Endor Docking Bay dested Endor: Landing Platform (Docking Bay) analog leftover Walseth. "
    "Op as planned dested Operational As Planned analog leftover typical. "
    "Imp. Arrest Order dested Imperial Arrest Order analog leftover Mike. "
    "That Things Operational dested That Thing's Operational analog leftover typical. "
    "DS II Coolant Shaft dested Death Star II: Coolant Shaft analog leftover typical. "
    "DS II Capacitors dested Death Star II: Capacitors analog leftover typical. "
    "DS II Reactor Core dested Death Star II: Reactor Core analog leftover typical. "
    "DS II Docking Bay dested Death Star II: Docking Bay analog leftover typical. "
    "Tempest 1 dested Tempest Scout 1 analog leftover Walseth. "
    "Emp-Class SD dested Executor analog leftover typical. "
    "Emp. Palp. empty lines 28–29 dest Emperor Palpatine qty=2 analog leftover Walseth. "
    "Bria dested Bria Tharen analog leftover typical. "
    "Comm Merijk dested Commander Merijk analog leftover typical. "
    "Gen. Veers dested General Veers analog leftover typical. "
    "Comm Igar dested Commander Igar analog leftover TYPE_OVERRIDE. "
    "Lt. Grond dested Lieutenant Grond analog leftover Mike. "
    "Were In Attack Position empty lines 37–38 dest We're In Attack Position Now qty=2 analog leftover typical. "
    "Dreaded Imp. Starfleet dested Dreaded Imperial Starfleet analog leftover nats Walseth. "
    "Imp. Prop dested Imperial Propaganda analog leftover nats. "
    "Lat Dam dested Lateral Damage analog leftover nats. "
    "End. Shield dested Endor Shield analog leftover Walseth. "
    "AAA dested According To My Design analog leftover Hanson. "
    "Imp. Decree dested Imperial Decree analog leftover Anderson. "
    "We Must Accelerate Our Plans empty lines 48–49 dest qty=2 at first. "
    "Control empty lines 50–51 dest qty=2 at first. "
    "Imp. Command empty lines 52–54 dest Imperial Command qty=3 analog leftover Walseth. "
    "Control & Set for Stun dested Control & Set For Stun analog leftover nats Walseth. "
    "Wounded Warrior dested analog leftover TYPE_OVERRIDE. "
    "Knowledge & Defence dested Knowledge And Defense analog leftover nats Hanson IN THE 60. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance? analog leftover nats. "
    "Opp. Enf dested Oppressive Enforcement analog leftover typical. "
    "Allegations of Corp dested Allegations Of Corruption analog leftover Hanson. "
    "Shield 12 Secret Plans dested analog leftover extra S clip. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him"
LS_CARDS = [
    n("There Is Good In Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Docking Bay"),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Rebel Scout", True),
    n("I Feel The Conflict"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Rendezvous Point"),
    n("Lando Calrissian, Scoundrel"),
    n("Mace Windu", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Corran Horn"),
    n("Boushh"),
    n("Princess Leia", True),
    n("Padme Naberrie", True),
    n("Lieutenant Blount", True),
    n("Threepio With His Parts Showing"),
    n("Ki-Adi-Mundi", True),
    n("Don't Tread On Me", True),
    n("Jedi Levitation", True),
    n("Nabrun Leids"),
    n("Were You Looking For Me"),
    n("Sense & Recoil", qty=3),
    n("A Jedi's Patience", True),
    n("Our Only Hope", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Smoke Screen", qty=3),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Double Agent", True),
    n("Blaster Deflection"),
    n("Speak With The Jedi Council"),
    n("A Jedi's Resilience", qty=2),
    n("Starship Levitation", True),
    n("Clash Of Sabers"),
    n("I'm With You Too", True),
    n("Ewok Catapult", True),
    n("Jedi Lightsaber", True),
    n("Leia's Blaster Rifle", True),
    n("Draw Their Fire"),
    n("Imperial Atrocity", True, qty=2),
    n("Tatooine", True),
    n("Projection Of A Skywalker", True),
    n("Gift Of The Mentor"),
    n("Signal"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Bunker"),
    n("Endor"),
    n("Operational As Planned"),
    n("Moff Jerjerrod"),
    n("Death Star II"),
    n("Imperial Arrest Order"),
    n("That Thing's Operational"),
    n("Death Star II: Coolant Shaft"),
    n("Death Star II: Capacitors"),
    n("Death Star II: Reactor Core"),
    n("Naboo"),
    n("Tatooine"),
    n("Death Star II: Docking Bay"),
    n("Blizzard 1"),
    n("Blizzard 2"),
    n("Tempest Scout 1"),
    n("Chimaera"),
    n("Executor", True),
    n("Conquest", True),
    n("Devastator", True),
    n("Accuser", True),
    n("Dominator", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Chiraneau"),
    n("Darth Vader", True),
    n("Emperor Palpatine", qty=2),
    n("Bria Tharen"),
    n("General Nevar", True),
    n("Commander Merijk"),
    n("Admiral Piett"),
    n("General Veers", True),
    n("Commander Igar", True),
    n("Lieutenant Grond", True),
    n("We're In Attack Position Now", qty=2),
    n("Dreaded Imperial Starfleet", True),
    n("No Escape"),
    n("Imperial Propaganda", True),
    n("Lateral Damage"),
    n("We Shall Double Our Efforts"),
    n("Endor Shield", True),
    n("According To My Design", True),
    n("Imperial Decree", True),
    n("Limited Resources"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Control", qty=2),
    n("Imperial Command", qty=3),
    n("Control & Set For Stun"),
    n("Wounded Warrior"),
    n("Cold Feet"),
    n("Surface Defense"),
    n("Spaceport Docking Bay"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?"),
    n("Resistance"),
    n("There Is No Try"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
