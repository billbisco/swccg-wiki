#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Sokol Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Sokol"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 91
DS_PAGE = 92
LS_SCAN = "2013 Match Play Championship p91 Sokol LS.png"
DS_SCAN = "2013 Match Play Championship p92 Sokol DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sokol. Deck title Shannon's light. Light. "
    "Communing as written. "
    "Tat: Slave Quarters dested Tatooine: Slave Quarters. "
    "Commando Training & K'lor's dested Commando Training & K'lor'slug. "
    "Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Chewbacca Protector dested Chewbacca, Protector. "
    "Luke with Lightsaber dested Luke With Lightsaber. "
    "Tat: Obi-Wan's Hut dested Tatooine: Obi-Wan's Hut. "
    "Chewie, Enraged dested Chewie, Enraged. "
    "Han with Gun dested Han With Heavy Blaster Pistol. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Flush of Insights dested Flash Of Insight. "
    "OOC & Trans Terminated dested Out Of Commission & Transmission Terminated. "
    "Senator Leia Organa dested Senator Leia Organa. "
    "Let The Wookiee Win dested Let The Wookiee Win. "
    "Run Luke, Run! dested Run Luke, Run!. "
    "Bail Organa, Father dested Bail Organa, Father Of Rebellion. "
    "Tat: Cantina dested Tatooine: Cantina. "
    "Threepio with his dested Threepio With His Parts Showing. "
    "A Jedi's Resilience dested A Jedi's Resilience. "
    "Home One: War Room dested Home One: War Room. "
    "Seeking An Audience dested Seeking An Audience. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Inconsequential Barriers as written. "
    "Artoo-Detoo In Red 5 dested Artoo-Detoo In Red 5. "
    "AFA dested Anger, Fear, Aggression. "
    "Let's keep A Little dested Let's Keep A Little Optimism Here. "
    "Your Insights Serves dested Your Insight Serves You Well. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Jabba's Prize dested Jabba's Prize. "
    "Don't do that Again dested Don't Do That Again. "
    "A Tragedy has occurred dested A Tragedy Has Occurred. "
    "Chasm dested Chasm. "
    "Form left column reprints 37–38 on lines 39–40 are Rebel Gunrunner and Weapon Levitation. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sokol. Deck title Dark. Dark checkbox unchecked; "
    "first card Contract Killers. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Coruscant: Sub city lair dested Coruscant: Sub City Lair. "
    "Coruscant: Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Cloud City: Security Tower dested Cloud City: Security Tower. "
    "Mara Jade's Lightsaber dested Mara Jade's Lightsaber. "
    "Aurra Sing's Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Galen's Lightsaber, Vader's dested Galen's Lightsaber, Vader's Gift. "
    "Trophy of A Kill dested Trophy Of A Kill. "
    "One Beautiful Thing as written. "
    "Stunning Leader dested Stunning Leader. "
    "Abyssin Ornament dested Abyssin Ornament. "
    "You Are Beaten dested You Are Beaten. "
    "Line 27 scribble then Rodian dested Rodian. "
    "Blaster Rack dested Blaster Rack. "
    "Death Mark & Hutt Bounty dested Death Mark & Hutt Bounty. "
    "On The Hunt as written. "
    "Jabba's Haven dested Jabba's Haven. "
    "Gift of the Master dested Gift Of The Master. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "The Mandalorian, Father dested Jango Fett, The Assassin. "
    "Boba Fett, Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Keder The Black dested Keder The Black. "
    "Aurra Sing, Deadly Assassin dested Aurra Sing, Deadly Assassin. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "J'Quille dested J'Quille. "
    "Guild of Assassins dested Guild Of Assassins. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider. "
    "Ket Maliss, Shadow Hunter dested Ket Maliss, Shadow Killer. "
    "Bane Malar dested Bane Malar. "
    "4-LOM With Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "I've Lost Artoo! dested I've Lost Artoo!. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "After her! dested After Her!. "
    "CHYBC dested Come Here You Big Coward. "
    "Weapon of A Sith dested Weapon Of A Sith. "
    "Form left column reprints 37–38 on lines 39–40 are Guri and Jango Fett, The Assassin. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Master Kenobi"),
    n("Tatooine: Slave Quarters"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Admiral Ackbar", True),
    n("Chewbacca, Protector", True),
    n("Imperial Atrocity", True),
    n("Luke With Lightsaber", qty=3),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Chewie, Enraged", True),
    n("Alderaan Consular Ship"),
    n("Han With Heavy Blaster Pistol"),
    n("Chewbacca, Protector", True),
    n("Houjix", qty=2),
    n("Lady Luck"),
    n("Tatooine"),
    n("Use The Force", qty=2),
    n("Home One"),
    n("Flash Of Insight", True, qty=2),
    n("Yoda, Great Warrior"),
    n("Out Of Commission", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Senator Leia Organa"),
    n("Let The Wookiee Win", True, qty=2),
    n("Wedge Antilles", True),
    n("Chewbacca's Bowcaster"),
    n("Run Luke, Run!", True, qty=2),
    n("Grimtaash"),
    n("Rebel Gunrunner"),
    n("Weapon Levitation"),
    n("Tantive IV", True),
    n("Bail Organa, Father Of Rebellion"),
    n("Tatooine: Cantina"),
    n("Draw Their Fire"),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("A Jedi's Resilience"),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=3),
    n("Home One: War Room"),
    n("Seeking An Audience", True),
    n("Corran Horn"),
    n("Maris Brood, Fallen Jedi"),
    n("Inconsequential Barriers"),
    n("Artoo-Detoo In Red 5"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Jabba's Prize"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Coruscant: Sub City Lair"),
    n("Coruscant"),
    n("Coruscant: Palpatine's Quarters"),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Coruscant: Casino"),
    n("Mara Jade's Lightsaber", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Trophy Of A Kill", qty=2),
    n("Prepared Defenses"),
    n("One Beautiful Thing", qty=2),
    n("Imperial Barrier"),
    n("Stunning Leader", qty=2),
    n("Abyssin Ornament", True, qty=3),
    n("Force Field", True),
    n("Sonic Bombardment", True, qty=3),
    n("You Are Beaten"),
    n("Rodian", True),
    n("Nevar Yalnal", qty=2),
    n("Disarmed", qty=2),
    n("Blaster Rack", True),
    n("Protocol Failure"),
    n("Death Mark & Hutt Bounty"),
    n("On The Hunt"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Slave I, Symbol Of Fear"),
    n("Guri"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Keder The Black"),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Arica", True, qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("J'Quille", True),
    n("Trophy Of A Kill"),
    n("Guild Of Assassins"),
    n("Imbalance & Kintan Strider"),
    n("Ket Maliss, Shadow Killer"),
    n("Bane Malar", True),
    n("4-LOM With Concussion Rifle", True),
    n("Force Push", True),
    n("I've Lost Artoo!", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("After Her!", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Resistance", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Weapon Of A Sith"),
]
DS_ADD = []
