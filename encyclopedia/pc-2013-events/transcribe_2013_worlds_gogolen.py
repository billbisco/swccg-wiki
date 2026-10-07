#!/usr/bin/env python3
"""2013 World Championship Day 2: Chris Gogolen typed Communing + Wookiee Slaving."""
from __future__ import annotations

PLAYER = "Chris Gogolen"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 38
DS_PAGE = 39
LS_SCAN = "2013 Worlds Day 2 p38 Chris Gogolen LS.png"
DS_SCAN = "2013 Worlds Day 2 p39 Chris Gogolen DS.png"
LS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Chris Gogolen. Username blank. Deck title Respect My Authori-ty!. LIGHT. "
    "Communing from Tatooine: Slave Quarters. "
    "Commando Training/K'lor Slug dested Commando Training & K'lor'slug. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Antilles Maneuver/Rebel Reinforcements dested "
    "Antilles Maneuver & Rebel Reinforcements. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Let the Wookiee Win dested Let The Wookiee Win. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Bith Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Hear me baby hold together dested Hear Me Baby, Hold Together. "
    "Run Luke Run dested Run Luke, Run!. "
    "Home 1 War Room dested Home One: War Room. "
    "Yoda stew/You do have your moments dested Yoda Stew & You Do Have Your Moments. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Tatooine(ep1) dested Tatooine (Coruscant). "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Han with heavy blaster pistol dested Han With Heavy Blaster Pistol. "
    "Tat: Obi's Hut dested Tatooine: Obi-Wan's Hut. "
    "Threepio with parts showing dested Threepio With His Parts Showing. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Let's Keep a little optimism dested Let's Keep A Little Optimism Here. "
    "Simple Tricks and Nonsense dested Simple Tricks And Nonsense. "
    "Do or do Not dested Do, Or Do Not. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Chris Gogolen. Username blank. DARK. Worlds Day 2. "
    "Wookiee Slaving Operations dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Kashyyyk Slaving Camp HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Special Delivery/Den of Thieves dested Den Of Thieves & Special Delivery. "
    "Father of Fett dested Jango Fett, The Assassin. "
    "Bossk w/ Mortar gun dested Bossk With Mortar Gun. "
    "Dengar with Blaster carbine dested Dengar With Blaster Carbine. "
    "Ket Maliss Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Mara jade with lightsaber dested Mara Jade With Lightsaber. "
    "Begin Landing Troops/Dark Path dested Begin Landing Your Troops & The Dark Path. "
    "Scum & Villainy dested Scum And Villainy. "
    "Breached Defenses/Molator dested Breached Defenses & Molator. "
    "They're still coming through dested They're Still Coming Through!. "
    "Defensive Fire/Hutt Smooch dested Defensive Fire & Hutt Smooch. "
    "Ghhhk/Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Kashyyyk Skyhook Platform dested Kashyyyk: Skyhook Platform. "
    "Kashyyyk Wookiee Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Sail barge passenger deck dested Jabba's Sail Barge: Passenger Deck. "
    "nal hutta dested Nal Hutta. "
    "Slave 1 SOF dested Slave I, Symbol Of Fear. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "I find your lack of faith disturbing dested I Find Your Lack Of Faith Disturbing. "
    "You cannot hide forever dested You Cannot Hide Forever. "
    "Come here you big coward dested Come Here You Big Coward. "
    "Imp Detention dested Imperial Detention. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug", True),
    n("Wedge Antilles", True),
    n("Corran Horn"),
    n("Yoda, Great Warrior"),
    n("Rebel Leadership", True, qty=3),
    n("Tatooine: Beggar's Canyon"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Lando Calrissian, Scoundrel", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Chewie, Enraged", True, qty=3),
    n("The Bith Shuffle & Desperate Reach"),
    n("Hear Me Baby, Hold Together", True),
    n("Run Luke, Run!"),
    n("Escape Pod", True, qty=2),
    n("Home One: War Room"),
    n("Use The Force", qty=2),
    n("Luke", True, qty=3),
    n("Much To Learn, You Still Have"),
    n("Yoda Stew & You Do Have Your Moments", qty=2),
    n("Home One"),
    n("Redeemed Apprentice"),
    n("Strikeforce", True),
    n("Rebel Gunrunner"),
    n("Luke's T-16 Skyhopper", qty=2),
    n("Houjix", qty=2),
    n("Old Ben", qty=2),
    n("Leia, Rebel Princess"),
    n("Tatooine (Coruscant)"),
    n("Mantellian Savrip"),
    n("Chewbacca's Bowcaster"),
    n("Han With Heavy Blaster Pistol"),
    n("Launching The Assault"),
    n("Inconsequential Barriers"),
    n("Republic Gunship Wing"),
    n("Artoo-Detoo In Red 5"),
    n("Imperial Atrocity", True, qty=2),
    n("Admiral Ackbar", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Rebel Barrier"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("The Professor"),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not", True),
    n("Planetary Defenses", True),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Jabba's Haven"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Garindan", True),
    n("Ephant Mon"),
    n("Ponda Baba", True),
    n("Bossk With Mortar Gun", True),
    n("Jabba The Hutt", True),
    n("Mercenary Pilot", qty=2),
    n("Prince Xizor"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Vigo", qty=2),
    n("Outer Rim Scout", qty=5),
    n("Dengar With Blaster Carbine", True),
    n("Ket Maliss, Shadow Killer"),
    n("Mara Jade With Lightsaber"),
    n("Probot"),
    n("P-59"),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Scum And Villainy"),
    n("Breached Defenses & Molator"),
    n("Something Special Planned For Them", True),
    n("Hutt Bounty", True),
    n("Imperial Propaganda", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Imperial Barrier", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("They're Still Coming Through!"),
    n("Cold Feet", True),
    n("Elis Helrot"),
    n("Abyssin Ornament", qty=3),
    n("Defensive Fire & Hutt Smooch"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Jabba's Space Cruiser", True),
    n("Jabba's Sail Barge", True),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Imperial Detention"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
