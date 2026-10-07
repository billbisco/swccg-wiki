#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Matt Fink Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Matt Fink"
USERNAME = "Foxhome"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 29
DS_PAGE = 30
LS_SCAN = "2013 Match Play Championship p29 Matt Fink LS.png"
DS_SCAN = "2013 Match Play Championship p30 Matt Fink DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Matt Fink. Light. Username Foxhome. "
    "Deck title Inflator. Event name Big Hotel Party. Starting Communing. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Gold leader in Gold 1 dested Gold Leader In Gold 1. "
    "Big Boomer dested Booma. Jedi Lev dested Jedi Levitation. "
    "Lando (V) Scoundrel dested Lando Calrissian, Scoundrel. "
    "Cortina dested Coruscant. Obi Hut dested Tatooine: Obi-Wan's Hut. "
    "Were you leaving me dested Were You Looking For Me. "
    "Alde Counselor Ship dested Alderaan Consular Ship. "
    "Luke Rebel Hero dested Luke Skywalker, Rebel Hero. "
    "SATM Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Chewie Enraged dested Chewie, Enraged. Run Luke Run dested Run Luke, Run!. "
    "Wedge Rogue Squadron Leader dested Wedge Antilles, Red Squadron Leader. "
    "Antilles man / Rebel Reinfor dested Antilles Maneuver & Rebel Reinforcements. "
    "Control Combo dested Control & Tunnel Vision. Tatooine (EP1) dested Tatooine. "
    "Atrocity dested Imperial Atrocity. Yoda's hut dested Dagobah: Yoda's Hut. "
    "Obi's App dested Anakin Skywalker, Padawan Learner. "
    "Furtative dested as written Furtive Squeeze. "
    "Reprint 37 Were not make one year dested as written. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Matt Fink. Dark. Username Foxhome. "
    "Deck title Pimp Corn Truck Suit. Starting Cloud City: Security Tower. "
    "Ket maless shadow hunter dested Ket Maliss, Shadow Killer. "
    "Hutting bounty dested Hutt Bounty. "
    "Breached Defenses / Molator dested Breached Defenses & Molator. "
    "Spice Administrator's office dested Kessel: Spice Mines - Administrator's Office. "
    "I'll take them myself dested I'll Take Them Myself. "
    "Kessel Extraction Facility dested Kessel: Spice Mines - Extraction Facility. "
    "The Dark Path dested The Dark Path. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "4lom with concussion rifle dested 4-LOM With Concussion Rifle. "
    "Short range combo dested Short Range Fighters & Watch Your Back. "
    "The Mandalorian FoF dested Jango Fett, The Assassin. "
    "You Swindled Me dested You Swindled Me!. "
    "Galen Secret Apprentice dested Galen Marek, Starkiller. "
    "Cyborg Commander's Lightsaber dested as written. "
    "Spice Mine ops dested Spice Mine Operations. "
    "Sniper combo dested Sniper & Dark Strike. "
    "Galen's Lightsaber V Gift dested Galen's Lightsaber, Vader's Gift. "
    "Form left column reprints 37–38 on lines 39–40 are You Swindled Me and Galen. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Wokling", True),
    n("Battle Plan"),
    n("Communing"),
    n("Seeking An Audience", True),
    n("Gold Leader In Gold 1", True),
    n("Flash Of Insight", True),
    n("Too Close For Comfort", True),
    n("Either Way, You Win", True),
    n("Booma"),
    n("Yoda, Great Warrior"),
    n("Jedi Levitation"),
    n("Draw Their Fire"),
    n("Leia With Blaster Rifle", qty=2),
    n("Tatooine: Mos Eisley"),
    n("Lando Calrissian, Scoundrel", True),
    n("Coruscant", True),
    n("Threepio With His Parts Showing"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Spiral"),
    n("Were You Looking For Me"),
    n("Goo Nee Tay"),
    n("Alderaan Consular Ship", qty=2),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Chewie, Enraged", True, qty=3),
    n("Antilles Maneuver", True),
    n("Run Luke, Run!", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("We Wish To Board At Once", qty=2),
    n("Rebel Barrier"),
    n("Were not make one year"),
    n("Stone Pile", qty=2),
    n("Furtive Squeeze", True),
    n("Houjix"),
    n("Use The Force", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Wookiee Roar"),
    n("Control & Tunnel Vision"),
    n("Luke's Blaster Pistol"),
    n("Tatooine"),
    n("Chewbacca's Bowcaster"),
    n("Imperial Atrocity", True),
    n("Rebel Gunrunner"),
    n("Dagobah: Yoda's Hut"),
    n("Master Kenobi"),
    n("Anakin Skywalker, Padawan Learner", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Do Or Do Not"),
    n("He Can Go About His Business"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Cloud City: Security Tower"
DS_CARDS = [
    n("Cloud City: Security Tower", True),
    n("Ket Maliss, Shadow Killer"),
    n("Hutt Bounty"),
    n("Breached Defenses & Molator"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Trophy Of A Kill"),
    n("Force Field", True),
    n("A Dark Time For The Rebellion", True, qty=3),
    n("Kessel"),
    n("Combat Readiness", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("I'll Take Them Myself"),
    n("Knowledge And Defense", True),
    n("Kessel Prison"),
    n("Emperor Palpatine"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("The Dark Path", True),
    n("Boba Fett, Prepared Hunter"),
    n("Nal Hutta"),
    n("Blaster Rack"),
    n("Slave I, Symbol Of Fear", qty=2),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True, qty=3),
    n("Arica", True, qty=2),
    n("Bossk In Hound's Tooth", True),
    n("Control & Set For Stun"),
    n("4-LOM With Concussion Rifle", True),
    n("Projective Telepathy"),
    n("Short Range Fighters & Watch Your Back"),
    n("Presence Of The Force"),
    n("Jango Fett, The Assassin", qty=2),
    n("Sense"),
    n("Garindan", True),
    n("Sith Fury", True),
    n("You Swindled Me", True),
    n("Galen Marek, Starkiller", qty=2),
    n("Protocol Failure"),
    n("Cyborg Commander's Lightsaber"),
    n("Moruth Doole, Kessel Administrator"),
    n("Victory"),
    n("Force Lightning"),
    n("Mara Jade With Lightsaber", True),
    n("You Are Beaten"),
    n("Imperial Barrier"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Sniper & Dark Strike"),
    n("Spice Mine Operations"),
    n("Control"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("A Useless Gesture"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("You've Never Won A Race"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
