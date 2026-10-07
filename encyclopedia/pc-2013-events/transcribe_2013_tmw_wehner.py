#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1 typed slang printout: Matt Wehner LS+DS."""
from __future__ import annotations

PLAYER = "Matt Wehner"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 40
DS_PAGE = 41
LS_SCAN = "2013 Texas Mini Worlds Day 1 p40 Matt Wehner LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p41 Matt Wehner DS.png"
LS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name matt wehner. Username blank (no Username box). "
    "LIGHT/DARK boxes empty; dest Light from the list. "
    "Do not dest as a new person. Do not rewrite TMW Schroeder leftover. "
    "a jedi's plans dested A Jedi's Plans. "
    "imperial atrocity v dested Imperial Atrocity. "
    "booster in pulsar skate dested Booster In Pulsar Skate. "
    "scrambled transmission v dested Scrambled Transmission. "
    "ackbar v dested Admiral Ackbar. "
    "corellian slip v dested Corellian Slip. "
    "lando, unlikely hero dested Lando Calrissian, Unlikely Hero. "
    "alter (coruscant) v dested Alter (Coruscant). "
    "wedge in red squadron 1 dested Wedge In Red Squadron 1. "
    "daughter v dested Daughter Of Skywalker. "
    "home one war room dested Home One: War Room. "
    "yoda's hut dested Dagobah: Yoda's Hut. "
    "dagobah training area dested Dagobah: Training Area. "
    "tat podracer arena dested Tatooine: Podrace Arena. "
    "i did it dested I Did It!. "
    "mind what you have learned dested Mind What You Have Learned / "
    "Save You It Can without True (no v; dual title required so lookup "
    "does not hit the (V) reprint). "
    "han, chewie, falcon dested Han, Chewie, And The Falcon. "
    "let the wookiee win v dested Let The Wookiee Win. "
    "artoo in red 5 dested Artoo-Detoo In Red 5. "
    "luke skywalker v dested Luke Skywalker. "
    "yoda v dested Yoda. "
    "out of commission and trans terminated dested "
    "Out Of Commission & Transmission Terminated. "
    "afa v dested Anger, Fear, Aggression. "
    "your insight v dested Your Insight Serves You Well. "
    "do or do not dested Do, Or Do Not. "
    "lets keep a little v dested Let's Keep A Little Optimism Here. "
    "Handwritten extras 11-15 dested He Can Go About His Business, "
    "Your Ship?, Simple Tricks And Nonsense, Battle Plan, "
    "A Tragedy Has Occurred. "
    "Unique overcounts sheet-accurate: Imperial Atrocity x2, "
    "Corellian Slip x2, Han, Chewie, And The Falcon x3, "
    "Let The Wookiee Win x2, Artoo-Detoo In Red 5 x2, Luke Skywalker x2, "
    "Escape Pod x2, Rebel Leadership x3, Projection Of A Skywalker x2, "
    "Don't Get Cocky x2, Out Of Commission & Transmission Terminated x2. "
    "v tags on the printout are Holotable virtual versions. "
    "Dittos inherit the first named line including v."
)
DS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Matt Wehner. Username blank. DARK SIDE checked. "
    "Do not dest as a new person. Do not rewrite TMW Schroeder leftover "
    "or Kirkpatrick SYCFA leftover. "
    "Set your course dested Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe without True (no v). "
    "A million voices cry out dested A Million Voices Crying Out. "
    "Flagship v dested Flagship as written. "
    "Image of the dark lord v dested Image Of The Dark Lord. "
    "something special planned for them v dested "
    "Something Special Planned For Them. "
    "kuat drive yards v dested Kuat Drive Yards. "
    "tarkins bounty v dested Tarkin's Bounty. "
    "they've shut down the main reactor dested "
    "They've Shut Down The Main Reactor. "
    "i can't shake him dested I Can't Shake Him!. "
    "Death star: war room v dested Death Star: War Room. "
    "death star: central core v dested Death Star: Central Core. "
    "tarkin doctrine v dested Tarkin Doctrine. "
    "commence primary ignition v dested Commence Primary Ignition. "
    "knowledge and defense v dested Knowledge And Defense. "
    "death star: docking bay 327 dested Death Star: Docking Bay 327. "
    "control & set for stun dested Control & Set For Stun. "
    "Intensify the forward batteries dested Intensify The Forward Batteries. "
    "Leave them to me v dested Leave Them To Me. "
    "offensive enforcement dested Oppressive Enforcement. "
    "do they havge a code clearance dested Do They Have A Code Clearance?. "
    "a useless gesture v dested A Useless Gesture. "
    "Handwritten extras 11-12 and 14-15 dested Come Here You Big Coward, "
    "Secret Plans, Fanfare, Abyss. Extra 13 unreadable, skipped. "
    "Unique overcounts sheet-accurate: Tractor Beam x3, Darth Sidious x2, "
    "In Range x4, They've Shut Down The Main Reactor x2, "
    "I Can't Shake Him! x2, Imperial Propaganda x2, "
    "Control & Set For Stun x2, Flawless Marksmanship x2, "
    "Masterful Move x2, Judicator x2, Intensify The Forward Batteries x3, "
    "Emperor Palpatine x2, Secret Plans x2. "
    "v tags on the printout are Holotable virtual versions. "
    "Dittos inherit the first named line including v."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("A Jedi's Plans"),
    n("Imperial Atrocity", True, qty=2),
    n("Booster In Pulsar Skate"),
    n("Scrambled Transmission", True),
    n("Strikeforce", True),
    n("Admiral Ackbar", True),
    n("Corellian Slip", True, qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Alter (Coruscant)", True),
    n("Republic Logistics", True),
    n("Luke's Backpack"),
    n("Wedge In Red Squadron 1"),
    n("Daughter Of Skywalker", True),
    n("Home One: War Room"),
    n("Dagobah: Yoda's Hut"),
    n("Han's Toolkit"),
    n("Yoda's Hope"),
    n("Dagobah"),
    n("Great Warrior"),
    n("Dagobah: Training Area"),
    n("Grimtaash"),
    n("Houjix"),
    n("Tatooine: Podrace Arena"),
    n("I Did It!"),
    n("Losing Track"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Mind What You Have Learned / Save You It Can"),
    n("Han, Chewie, And The Falcon", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Podrace Prep"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Logistical Delay", True),
    n("Escape Pod", True, qty=2),
    n("Yoda", True),
    n("Rebel Leadership", True, qty=3),
    n("Home One"),
    n("Kiffex"),
    n("Projection Of A Skywalker", qty=2),
    n("We're Doomed"),
    n("It Could Be Worse"),
    n("Don't Get Cocky", qty=2),
    n("Kessel"),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business"),
    n("Your Ship?"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Superlaser"),
    n("Monnok"),
    n("Kiffex"),
    n("Tractor Beam", qty=3),
    n("Laser Cannon Battery"),
    n("Naboo"),
    n("A Million Voices Crying Out"),
    n("Darth Sidious", qty=2),
    n("Devastator"),
    n("Flagship", True),
    n("Stalker"),
    n("Image Of The Dark Lord", True),
    n("Something Special Planned For Them", True),
    n("Kuat Drive Yards", True),
    n("Tarkin's Bounty", True),
    n("Masterful Move"),
    n("Rendili"),
    n("In Range", qty=4),
    n("They've Shut Down The Main Reactor", qty=2),
    n("I Can't Shake Him!", qty=2),
    n("Broken Concentration", True),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Victory", True),
    n("Imperial Stockpile", True),
    n("Tarkin Doctrine", True),
    n("Commence Primary Ignition", True),
    n("Imperial Propaganda", True, qty=2),
    n("Knowledge And Defense", True),
    n("Emperor Palpatine"),
    n("Tyrant"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Lateral Damage"),
    n("Control & Set For Stun", qty=2),
    n("Flawless Marksmanship", qty=2),
    n("Masterful Move"),
    n("Dominator"),
    n("Avenger"),
    n("Prepared Defenses"),
    n("Chimaera"),
    n("Judicator", qty=2),
    n("Intensify The Forward Batteries", qty=3),
    n("Emperor Palpatine"),
]
DS_SHIELDS = [
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Abyss", True),
]
DS_ADD = []
