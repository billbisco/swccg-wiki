#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Bentley Boyd.

Source: Yavin42012.pdf pages 33–34.
p33 Light handwritten 2010 Xerox / p34 Dark handwritten 2010 Xerox.
Name BENTLEY BOYD dested Bentley Boyd analog leftover dest as written /
player-stubs/Bentley_Boyd.wiki / Boyd.wiki redirect.
Username blank. Pack player-stubs/Bentley_Boyd.wiki.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Bentley Boyd"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 33
DS_PAGE = 34
LS_SCAN = "2012 Yavin 4 Regionals Bentley Boyd LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Bentley Boyd DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p33 Light handwritten 2010 Xerox / p34 Dark handwritten 2010 Xerox. "
    "Name BENTLEY BOYD dested Bentley Boyd analog leftover dest as written / "
    "player-stubs/Bentley_Boyd.wiki. Username blank. "
    "Event Date 6/30/12 Event Name blank dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name Hyperdrive Generator's Gone / Let Them Make The First Move dested off article. "
    "Do not dest as a new person. Pack player-stubs/Bentley_Boyd.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p33 Light. Name BENTLEY BOYD Username blank. "
    "Event Date 6/30/12 Event Name blank dest Yavin 4 facing pair. LIGHT checked. "
    "Hyperdrive Generator's Gone dested The Hyperdrive Generator's Gone analog leftover dest as written. "
    "START dested from line 1 analog leftover Nathan no-objective. "
    "Credits Will Do Fine dested analog leftover dest as written slang Credits Will Do Fine. "
    "Clone Pilot True qty=2 at first lines 6/15 analog leftover non-consecutive. "
    "Lando w/ Vibro-Ax dested Lando With Vibro-Ax analog leftover dest as written slang qty=2 at first lines 8/22 analog leftover non-consecutive. "
    "Jedi Pilot True qty=2 at first lines 11/27 analog leftover non-consecutive. "
    "Republic Trooper w/ Blaster Rifle dested Republic Trooper With Blaster Rifle analog leftover dest as written slang qty=2 consecutive. "
    "Lt. Williams dested Lieutenant Williams analog leftover dest as written slang Capt. Madakor qty=2 at first lines 21/38 analog leftover non-consecutive. "
    "Republic Starfighter True qty=2 at first lines 30/33 analog leftover non-consecutive. "
    "Let's Keep A Little Optimism Here True dested analog leftover TYPE_OVERRIDE IN THE 60. "
    "Yarua empty qty=2 at first lines 45/52 analog leftover non-consecutive. "
    "Phylo Gandish dested analog leftover TYPE_OVERRIDE. "
    "Sorry About The Mess/Blaster Prof dested Sorry About The Mess & Blaster Proficiency analog leftover dest as written combo. "
    "Obi-Wan Kenobi, Padawan Learner empty qty=2 at first lines 56/58 analog leftover non-consecutive. "
    "Lira Merian dested analog leftover dest as written. "
    "Shields 1–12 filled. Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p34 Dark. Name BENTLEY BOYD Username blank. "
    "Event Date 6/30/12 Event Name blank dest Yavin 4 facing pair. DARK checked. "
    "Let Them Make + 1st Move dested Let Them Make The First Move analog leftover dest as written. "
    "START dested from line 1 analog leftover Nathan. "
    "Maul's Sith Infiltrator empty qty=2 at first lines 10/15 analog leftover non-consecutive. "
    "Darth Vader w/ Lightsaber dested Darth Vader With Lightsaber analog leftover dest as written slang qty=2 consecutive lines 40/41. "
    "Darth Sidious empty qty=2 at first lines 44/46 analog leftover non-consecutive KEEP SEPARATE from Lord Sidious True. "
    "Crossed dest U-3PO True analog leftover crossed-with-replacement. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi analog leftover Morgan. "
    "Elis in Huttese dested Elis Helrot analog leftover dest as written slang TYPE_OVERRIDE. "
    "Reegeek dested Reegesk analog leftover dest as written slang. "
    "Sgt. Major Bursk dested Sergeant Major Bursk analog leftover dest as written slang. "
    "Knowledge And Defense True dested analog leftover Anderson IN THE 60. "
    "Wipe Them Out, All Of Them dested as written as shield analog leftover dest as written Schmaltz. "
    "Imperial Detention dested as written as shield analog leftover dest as written. "
    "Shields 1–12 filled. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone"),
    n("Credits Will Do Fine"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Queen's Landing Site", True),
    n("Tatooine: City Outskirts"),
    n("Clone Pilot", True, qty=2),
    n("Fallen Jedi", True),
    n("Lando With Vibro-Ax", qty=2),
    n("Qui-Gon Jinn"),
    n("Queen Amidala"),
    n("Jedi Pilot", True, qty=2),
    n("Wookiee Strangle", True),
    n("Queen's Royal Starship"),
    n("Tatooine"),
    n("Republic Trooper With Blaster Rifle", True, qty=2),
    n("Jedi Lightsaber"),
    n("Honor Of The Jedi"),
    n("Tanus Spijek", True),
    n("Lieutenant Williams", True, qty=2),
    n("Flash Of Insight", True),
    n("2-1B", True),
    n("Master Qui-Gon", True),
    n("Ki-Adi-Mundi", True),
    n("Obi-Wan's Cape", True),
    n("Senator Padme Amidala", True),
    n("Republic Starfighter", True, qty=2),
    n("Firefight", True),
    n("Jedi Survival", True),
    n("Jedi Starfighter", True),
    n("Chewbacca", True),
    n("It's Not My Fault", True),
    n("Into The Garbage Chute, Flyboy", True),
    n("Elegant Lightsaber", True),
    n("Lobot", True),
    n("Krayt Dragon Howl", True),
    n("Republic Corvette", True),
    n("Clone Trooper", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yarua", qty=2),
    n("Horox Ryyder"),
    n("Phylo Gandish", True),
    n("Alderaan Consular Ship", True),
    n("Ric Olie"),
    n("Senator Palpatine"),
    n("Captain Madakor"),
    n("Alter & Friendly Fire"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Obi-Wan's Lightsaber"),
    n("Obi-Wan Kenobi, Padawan Learner", qty=2),
    n("Lira Merian"),
    n("Lightsaber Proficiency"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Affect Mind", True),
    n("A Close Race"),
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Let Them Make The First Move"
DS_CARDS = [
    n("Let Them Make The First Move"),
    n("Surface Defense", True),
    n("Deep Hatred"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Twi'lek Advisor", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Ghhhk"),
    n("4-LOM With Concussion Rifle"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Masterful Move"),
    n("Cane Ading", True),
    n("Force Field", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("We're All Gonna Be A Lot Thinner"),
    n("Weapon Of An Ungrateful Son"),
    n("Imperial Propaganda", True),
    n("I Blow Palpified"),
    n("Image Of The Dark Lord", True),
    n("Binders"),
    n("Presence Of The Force"),
    n("Desperate Counter", True),
    n("Revenge Of The Sith", True),
    n("The Emperor's Prize", True),
    n("Katana", True),
    n("Grand Admiral Thrawn"),
    n("Zuckuss In Mist Hunter"),
    n("Victory", True),
    n("Bossk In Hound's Tooth"),
    n("Chimaera"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Gift Of The Mentor", True),
    n("Elis Helrot", True),
    n("Boba Fett, Bounty Hunter"),
    n("The Empire's Back", True),
    n("Galen, Secret Apprentice", True),
    n("Darth Maul, Young Apprentice"),
    n("Darth Maul With Lightsaber"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Sidious' Lightsaber", True),
    n("The Emperor", True),
    n("Darth Sidious", qty=2),
    n("Lord Sidious", True),
    n("U-3PO", True),
    n("Arica", True),
    n("IG-88 With Riot Gun"),
    n("Keder The Black"),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Dr. Evazan & Ponda Baba"),
    n("Janus Greejatus"),
    n("Grievous, Hunter Of Jedi", True),
    n("Reegesk", True),
    n("Sergeant Major Bursk", True),
    n("Aurra Sing", True),
    n("Moten"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Abyss", True),
    n("Firepower", True),
    n("Wipe Them Out, All Of Them", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
