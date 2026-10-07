#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Josh handwritten Print Form LS+DS.

Name field Josh. Username Renmaker. Dest Josh as written (first name only).
Do not dest as Josh Mack.
"""
from __future__ import annotations

PLAYER = "Josh"
USERNAME = "Renmaker"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 25
DS_PAGE = 26
LS_SCAN = "2013 SoCal Grand Prix Day 1 p25 Josh LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p26 Josh DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Josh dested as written. Username Renmaker. "
    "Deck Name You guys are playing STAR WARS?? Event SoCal '13. "
    "LIGHT/DARK empty; dest Light from Communing. "
    "Tatooine: Slave Qtrs dested Tatooine: Slave Quarters. "
    "Commando Training Combo dested Commando Training & K'lor'slug. "
    "Chewbacca Enraged line 17 True / lines 18-20 empty kept split. "
    "Flash of Insight dested Flash Of Insight. "
    "Bail Organa FoR dested Bail Organa, Father Of Rebellion. "
    "Wedge Antilles dested Wedge Antilles True. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. "
    "Escape Pod line 33 True / lines 34-35 empty kept split. "
    "Rebel Leadership line 45 True / lines 46-47 empty kept split. "
    "Run Luke Run line 52 True / lines 53-54 empty kept split. "
    "LTWW line 57 True / line 58 empty kept split. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Josh dested as written. Username Renmaker. "
    "Deck Name It Moos. Event SoCal '13. "
    "LIGHT/DARK empty; dest Dark from Kessel (Spice Mine Operations in the 60). "
    "Kessel Spice Mines sites dested Kessel: Spice Mines - Extraction Facility / "
    "Prison / Administrator's Office. "
    "Galkn dested Galen Marek, Starkiller. "
    "Maul Saber dested Darth Maul's Lightsaber as written. "
    "Young Maul w/stick dested Darth Maul With Lightsaber. "
    "Jango Fett Father of Fett dested Jango Fett, The Assassin. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Sniper combo dested Sniper & Dark Strike. "
    "B1-ZED dested B1-ZED as written. "
    "ELD dested ELD as written. "
    "Force Field line 35 True / line 36 empty kept split. "
    "Sonic Bombardment line 49 True / lines 50-51 empty kept split. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Draw Their Fire"),
    n("Commando Training & K'lor'slug"),
    n("Imperial Atrocity", True),
    n("Rebel Gunrunner"),
    n("Seeking An Audience", True),
    n("Redeemed Apprentice"),
    n("Home One"),
    n("Lady Luck"),
    n("Artoo-Detoo In Red 5"),
    n("Artoo-Detoo In Red 5"),
    n("Luke With Lightsaber"),
    n("Luke With Lightsaber"),
    n("Luke With Lightsaber"),
    n("Chewie, Enraged", True),
    n("Chewie, Enraged"),
    n("Chewie, Enraged"),
    n("Chewie, Enraged"),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel"),
    n("Imperial Atrocity", True),
    n("Flash Of Insight", True),
    n("Chewbacca's Bowcaster"),
    n("Tatooine: Cantina"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Houjix"),
    n("Houjix"),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("Escape Pod"),
    n("Corran Horn"),
    n("Tatooine"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Bail Organa, Father Of Rebellion"),
    n("Wedge Antilles", True),
    n("Dash Rendar", True),
    n("Use The Force"),
    n("Use The Force"),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Rebel Leadership"),
    n("Leia, Rebel Princess"),
    n("A Jedi's Resilience"),
    n("Wookiee Roar", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Run Luke, Run!", True),
    n("Run Luke, Run!"),
    n("Run Luke, Run!"),
    n("Clash Of Sabers"),
    n("Clash Of Sabers"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Han With Heavy Blaster Pistol"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("The Way Of Things"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Spice Mine Operations"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel: Spice Mines - Prison"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Kessel Surveillance System"),
    n("Galen Marek, Starkiller"),
    n("Galen Marek, Starkiller"),
    n("Galen Marek, Starkiller"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul's Lightsaber"),
    n("Darth Maul's Lightsaber"),
    n("Emperor Palpatine"),
    n("Emperor Palpatine"),
    n("Lord Sidious"),
    n("Lord Sidious"),
    n("Arica"),
    n("Spice Mine Administrator"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Garindan", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Gift Of The Master"),
    n("Imperial Justice"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
    n("Sense"),
    n("Darth Maul With Lightsaber"),
    n("Force Field", True),
    n("Force Field"),
    n("Force Lightning"),
    n("Force Push"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Combat Readiness", True),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("B1-ZED"),
    n("B1-ZED"),
    n("Lightsaber Deficiency"),
    n("Cold Feet", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sonic Bombardment", True),
    n("Sonic Bombardment"),
    n("Sonic Bombardment"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sniper & Dark Strike"),
    n("Dark Strike"),
    n("Dark Maneuvers"),
    n("Dark Maneuvers"),
    n("Close Call", True),
    n("I Have You Now", True),
    n("I'll Take Them Myself"),
    n("ELD", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Battle Order"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Resistance"),
    n("There Is No Try"),
    n("Death Star Sentry", True),
]
DS_ADD = []
