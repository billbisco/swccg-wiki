#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Clayton Atkin.

Source: MPC-2014-Day-1-Main-Event.pdf pages 9–10 (2013 form, 15 shields).
Username blank.
"""
from __future__ import annotations

PLAYER = "Clayton Atkin"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2014 Match Play Championship Day 1 Clayton Atkin LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Clayton Atkin DS.png"
LS_DECK_NAME = "QMC"
DS_DECK_NAME = "Rops"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. LIGHT checked. QMC dested Quiet Mining "
    "Colony / Independent Operation. H.F.T.M.F. dested Heading For The Medical Frigate. "
    "All My Uncles/Celebration dested All My Urchins & Cloud City Celebration. AWRI/"
    "Darklighter Spin dested All Wings Report In & Darklighter Spin. Grave dested Choke. "
    "Hideous in the Garbage dested Hiding In The Garbage. Path of Least Resistance/"
    "Revealed dested Path Of Least Resistance & Revealed. Dayla Stott dested Aayla Secura. "
    "Tee-Jee Binks dested Senator Jar Jar Binks. Lando's Luxury Yacht dested Lady Luck. "
    "Trooper Utris M'Toc dested Trooper Utris M'Toc. Houjix/Out of Nowhere dested Houjix "
    "& Out Of Nowhere. Shield Odin's Prize dested Odin's Prize as written (NO_DEST). "
    "Unique overcounts sheet-accurate (Choke x2, Rebel Barrier x2, "
    "Imperial Atrocity (V) x2, Houjix & Out Of Nowhere x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. DARK checked. ROPS dested Ralltiir "
    "Operations / In The Hands Of The Empire. Ice-Heart dested Ysanne Isard. The "
    "Mandalorian, Father of Fett dested Jango Fett, The Assassin. Insign Point "
    "Rebellions dested Insignificant Rebellion. SRF/Watch Your Back dested Short Range "
    "Fighters & Watch Your Back!. Masterful Move/Endor Occ dested Masterful Move & "
    "Endor Occupation. Limited Resources dested Limited Resources (crossed replacement). "
    "Daine Jir dested Commander Daine Jir. Unique overcounts sheet-accurate (Blizzard 4 "
    "x2, Imperial Command x2, Imperial Barrier x2, Sonic Bombardment (V) x2). (V) from "
    "checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Infinity"),
    n("All Wings Report In & Darklighter Spin"),
    n("Choke", qty=2),
    n("Blast The Door, Kid!"),
    n("Hiding In The Garbage", True),
    n("Rebel Barrier", qty=2),
    n("Cloud City: West Gallery"),
    n("Sergeant Edian", True),
    n("Redeemed Apprentice"),
    n("Dash Rendar", True),
    n("Tanus Spijek", True),
    n("Tawss Khaa"),
    n("Alter"),
    n("Imperial Atrocity", True, qty=2),
    n("Melas", True),
    n("Path Of Least Resistance & Revealed"),
    n("Foul Moudama"),
    n("Ellorrs Madak", True),
    n("Harc Seff", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Aayla Secura"),
    n("Nien Nunb, Sullustan Smuggler"),
    n("Artoo, Brave Little Droid"),
    n("It's A Hit!"),
    n("Cloud City: Platform 327"),
    n("Senator Jar Jar Binks"),
    n("Chewbacca, Walking Carpet"),
    n("It's A Trap!"),
    n("Path Of Least Resistance"),
    n("Mirax Terrik"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Kebyc", True),
    n("Dark Approach", True),
    n("Cloud City: North Corridor"),
    n("Booster In Pulsar Skate"),
    n("Leslomy Tacema", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("I'll Take The Leader"),
    n("Overseer"),
    n("Lady Luck"),
    n("Trooper Utris M'Toc", True),
    n("Leia, Rebel Princess"),
    n("Han Solo, Innocent Scoundrel"),
    n("Caldera Righim"),
    n("Desperate Reach", True),
    n("Luke With Lightsaber"),
    n("Menace Fades"),
    n("BoShek, Brash Smuggler"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Odin's Prize", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Wise Advice"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Kashyyyk"),
    n("Endor"),
    n("Spaceport Prefect's Office"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Ralltiir: Spaceport Financial District"),
    n("Cloud City: Security Tower", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Janus Greejatus"),
    n("The Emperor", True),
    n("Emperor Palpatine"),
    n("Garindan", True),
    n("Colonel Davod Jon"),
    n("Ysanne Isard"),
    n("Arica"),
    n("General Veers", True),
    n("Commander Daine Jir"),
    n("Admiral Ozzel"),
    n("Emperor's Personal Shuttle"),
    n("Zuckuss In Mist Hunter"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Blizzard 4", qty=2),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Limited Resources"),
    n("He Hasn't Come Back Yet"),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("Outflank", True),
    n("Close Call", True),
    n("Imperial Command", qty=2),
    n("Imperial Barrier", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Something Special Planned For Them", True),
    n("Astromech Shortage", True),
    n("Imperial Justice", True),
    n("Image Of The Dark Lord", True),
    n("Special Delivery", True),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("After Her!", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Fanfare", True),
]
DS_ADD = []
