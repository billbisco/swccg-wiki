#!/usr/bin/env python3
"""2013 World Championship Day 3: Jonny Chu Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Jonny Chu"
USERNAME = "mryellow"
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2013 Worlds Day 3 p06 Jonny Chu LS.png"
DS_SCAN = "2013 Worlds Day 3 p05 Jonny Chu DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jonny Chu. Username mryellow. "
    "Event Worlds Day 3. Deck title Chu Communing. LIGHT/DARK boxes empty. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "Fire Extinguisher dested Fire Extinguisher. "
    "Coro 2187 dested TK-422. "
    "All My Urdines dested All My Urchins. "
    "Seeking An Audience dested Seeking An Audience. "
    "Nar Shaddaa dested Nar Shaddaa. "
    "Artoo dested Artoo-Detoo In Red 5. "
    "Chewbacca Of Kashyyyk dested Chewbacca Of Kashyyyk. "
    "Han Solo dested Han Solo. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Booster dested Booster Terrik; unique overcount kept sheet-accurate. "
    "Strike Blocked dested Strike Blocked. "
    "Trooper Sabacc dested Trooper Sabacc. "
    "Either Way, You Win dested Either Way, You Win. "
    "Control / TV dested Control & Tunnel Vision. "
    "Nar Shaddaa Wind Chimes dested Nar Shaddaa Wind Chimes. "
    "Dual Shutdown dested Dual Laser Cannon. "
    "Use The Force dested Use The Force. "
    "Free Ride / Endor Celebration dested Free Ride & Endor Celebration. "
    "Your Ship? dested Your Ship?. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jonny Chu. Username mryellow. "
    "Event Worlds Day 3. Deck title Spice Thief. DARK checked. "
    "Kessel: Spice Mines - Admin Office dested "
    "Kessel: Spice Mines - Administrator's Office. "
    "I'll Take Them Myself dested I'll Take Them Myself. "
    "I'm Sorry dested I'm Sorry. "
    "Saber 1 dested Saber 1. Saber 4 dested Saber 4. "
    "Obsidian 16 dested Obsidian 16. "
    "Tibanna Floating Refinery dested Tibanna Floating Refinery. "
    "Kessel Surveillance System dested Kessel Surveillance System. "
    "SFS L-s9.3 Laser Cannons dested SFS L-s9.3 Laser Cannons. "
    "Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Jango Fett The Assassin dested Jango Fett, The Assassin. "
    "Keder The Black dested Keder The Black. "
    "Baron Soontir Fel dested Baron Soontir Fel. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "All Power To Weapons dested All Power To Weapons. "
    "Short Range Fighters / Watch Your Back dested "
    "Short Range Fighters & Watch Your Back!. "
    "Sonic Bombardment dested Sonic Bombardment. "
    "Abyssin Ornament dested Abyssin Ornament. "
    "Masterful Move / Endor Occ dested Masterful Move & Endor Occupation. "
    "Wipe Them Out, All Of Them dested Wipe Them Out, All Of Them. "
    "Image Of The Dark Lord dested Image Of The Dark Lord. "
    "After Her dested After Her!. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "We'll Let Fate-A Decide Huh dested We'll Let Fate-A Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Master Kenobi"),
    n("Communing"),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Home One"),
    n("Alderaan Consular Ship"),
    n("Fire Extinguisher", qty=5),
    n("Imperial Atrocity", True, qty=3),
    n("TK-422", True),
    n("All My Urchins"),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Nar Shaddaa", True),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: City Outskirts"),
    n("Artoo-Detoo In Red 5", True),
    n("Threepio With His Parts Showing"),
    n("Luke Skywalker", True, qty=2),
    n("Yoda, Great Warrior"),
    n("Chewbacca Of Kashyyyk"),
    n("Han With Heavy Blaster Pistol"),
    n("Han Solo"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Padme Naberrie", True),
    n("Shmi Skywalker"),
    n("Booster Terrik", qty=3),
    n("Strike Blocked"),
    n("Rebel Leadership", True, qty=4),
    n("Trooper Sabacc"),
    n("Either Way, You Win", True, qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Nar Shaddaa Wind Chimes"),
    n("Dual Laser Cannon"),
    n("Use The Force", True, qty=2),
    n("Lucky Shot", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Free Ride & Endor Celebration", qty=2),
    n("Inconsequential Barriers"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
]
LS_ADD = [
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well"),
    n("Your Ship?"),
]


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Combat Response", True),
    n("I'm Sorry", True),
    n("Combat Readiness", True),
    n("Spice Mine Operations"),
    n("Saber 1", qty=2),
    n("Saber 4"),
    n("Saber Squadron TIE", qty=3),
    n("Obsidian 16", True),
    n("Storm Clouds"),
    n("Clouds"),
    n("Tibanna Floating Refinery"),
    n("Kessel Surveillance System"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jango Fett, The Assassin"),
    n("Saber Squadron Pilot", qty=3),
    n("Keder The Black", qty=2),
    n("Baron Soontir Fel", qty=2),
    n("Arica"),
    n("U-3PO (Yoo-Threepio)", qty=2),
    n("OS-72-10"),
    n("All Power To Weapons", qty=5),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", True, qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Limited Resources"),
    n("Ghhhk", qty=2),
    n("Monnok"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Wipe Them Out, All Of Them", True),
    n("Protocol Failure", qty=2),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("After Her!", True),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Secret Plans", True),
]
DS_ADD = [
    n("There Is No Try"),
    n("We'll Let Fate-A Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
]
