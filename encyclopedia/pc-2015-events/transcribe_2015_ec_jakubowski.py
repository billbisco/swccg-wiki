#!/usr/bin/env python3
"""2015 European Championship Day 2: Jonas Jakubowski (place 20).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p07 DS typed list / p08 LS deck list form.
"""
from __future__ import annotations

PLAYER = "Jonas Jakubowski"
USERNAME = "JackuLebowski"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2015 European Championship Jonas Jakubowski LS.png"
DS_SCAN = "2015 European Championship Jonas Jakubowski DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 20 circled. DS p07 typed list 'DS - That Thing's Operational', header 'TTO Euro's 2015', DS 3:1. "
    "LS p08 form deck name 'WYS', event date 10/17/15, LS 1:3. "
    "Username DS 'JackuLebowski'; LS form 'Jacku Lebowsk(i)'."
)
LS_NOTE = (
    "Form 60 lines + 15 shields. "
    "Posted Watch Your Step/ TPCBALR dested Watch Your Step / This Place Can Be A Little Rough. "
    "Tatooine (Coruscant) kept as written (Coruscant-set Tatooine system). "
    "Heading For The Medical Frigate (+3Effects) dested Heading For The Medical Frigate; +3 effects note only. "
    "Posted Pulsar Skate dested Booster In Pulsar Skate. "
    "Posted All Wings combo dested All Wings Report In & Darklighter Spin. "
    "Posted Free Ride combo dested Free Ride & Endor Celebration. "
    "Posted Out Of Commission combo dested Out Of Commission & Transmission Terminated. "
    "Posted The Bith Shuffle combo dested The Bith Shuffle & Desperate Reach. "
    "Line 46 Grimtaash crossed out, replaced by Dejarik Hologameboard. "
    "Posted Do or do Not dested Do, Or Do Not. Posted Jabba's Price dested Jabba's Prize. "
    "Luke Skywalker, Jedi Knight x3 sheet-accurate."
)
DS_NOTE = (
    "Typed list 60 + 15 shields. Objective Endor Operations / Imperial Outpost; deck labelled That Thing's Operational. "
    "Operational As Planned (+Jerjerrod, Death Star II, and 1 effect) dested Operational As Planned. "
    "Posted Endor: Landing Platform (Docking Bay) dested Endor: Landing Platform. "
    "Posted Colonel Jendon in Onyx 1 dested Colonel Jendon In Onyx 1. "
    "Posted Short Range Fighters & Watch Your Back! dested Short-Range Fighters & Watch Your Back. "
    "Posted Come Here You Big Coward! dested Come Here You Big Coward. "
    "Posted Do The Have A Code Clearance? dested Do They Have A Code Clearance?. "
    "Posted Whipe The Out, All Of Them dested Wipe Them Out, All Of Them."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Kessel"),
    n("Like My Father Before Me"),
    n("Squadron Assignments"),
    n("I Must Be Allowed To Speak", True),
    n("K'lor'slug", True),
    n("Strikeforce", True),
    n("Mechanical Failure"),
    n("I'll Take The Leader"),
    n("Luke's Lightsaber"),
    n("Captain Han Solo"),
    n("Chewbacca"),
    n("Chewbacca, Protector"),
    n("Dash Rendar"),
    n("Han With Heavy Blaster Pistol"),
    n("Lando Calrissian", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Melas", True, qty=2),
    n("Mirax Terrik"),
    n("Owen Lars & Beru Lars"),
    n("Talon Karrde", qty=2),
    n("Wedge Antilles", True, qty=2),
    n("Yotts Orren"),
    n("Millennium Falcon"),
    n("Outrider"),
    n("Booster In Pulsar Skate"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Dodge"),
    n("Escape Pod", True, qty=2),
    n("Fallen Portal"),
    n("Free Ride & Endor Celebration"),
    n("Dejarik Hologameboard"),
    n("Harvest"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("It Could Be Worse"),
    n("It's A Hit!"),
    n("It's A Trap!"),
    n("Moving To Attack Position"),
    n("Out Of Commission & Transmission Terminated"),
    n("Perimeter Scan", True),
    n("Rebel Barrier"),
    n("The Bith Shuffle & Desperate Reach"),
    n("The Force Is Strong With This One"),
    n("Alternatives To Fighting"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Goldenrod"),
    n("Jabba's Prize", True),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("Operational As Planned"),
    n("Death Star II"),
    n("Death Star II: Capacitors"),
    n("Death Star II: Coolant Shaft"),
    n("Death Star II: Docking Bay"),
    n("Death Star II: Reactor Core"),
    n("Kashyyyk"),
    n("Spaceport Docking Bay"),
    n("Admiral Piett"),
    n("Baron Soontir Fel"),
    n("Commander Merrejk"),
    n("DS-61-2"),
    n("Darth Maul With Lightsaber"),
    n("Darth Vader", True),
    n("Emperor Palpatine", qty=2),
    n("General Veers", True),
    n("Grand Moff Tarkin", True),
    n("Major Turr Phennir"),
    n("Moff Jerjerrod"),
    n("Black 2", True),
    n("Colonel Jendon In Onyx 1"),
    n("Onyx 2", True),
    n("Saber 1"),
    n("Saber 2"),
    n("Emperor's Personal Shuttle"),
    n("Vader's Personal Shuttle", True),
    n("Blizzard 1"),
    n("Blizzard 2", True),
    n("Blizzard Scout 1", True),
    n("Tempest 1"),
    n("Tempest Scout 6"),
    n("SFS L-s9.3 Laser Cannons", qty=2),
    n("Fighters Coming In", qty=2),
    n("Combat Response"),
    n("Desperate Counter"),
    n("Endor Shield", True),
    n("Imperial Arrest Order & Secret Plans"),
    n("We Shall Double Our Efforts!"),
    n("Pride Of The Empire"),
    n("All Power To Weapons"),
    n("Control & Set For Stun"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Ghhhk"),
    n("Imperial Artillery"),
    n("Imperial Barrier"),
    n("Imperial Command"),
    n("Masterful Move"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Trample"),
    n("That Thing's Operational"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("Wipe Them Out, All Of Them"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
