#!/usr/bin/env python3
"""2015 European Championship Day 2: Ralf Wachowiak (place 34).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p35 Dark / p36 Light (2015 PC forms, handwritten).
"""
from __future__ import annotations

PLAYER = "Ralf Wachowiak"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 36
DS_PAGE = 35
LS_SCAN = "2015 European Championship Ralf Wachowiak LS.png"
DS_SCAN = "2015 European Championship Ralf Wachowiak DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18-35 p35 Dark / p36 Light, handwritten PC forms, circled 34. "
    "Name written Wachowiak Ralf. Username blank. Event Europeans 2015, date blank. "
    "Deck Name boxes 'Stupiest Deckname ever' (joke, kept off DECK_NAME). DS 2:1 / LS 0:3 handwritten. "
    "Repeated cards written as ditto marks; counted as copies."
)
LS_NOTE = (
    "START Yavin 4 Throne Room dested Yavin 4: Massassi Throne Room. "
    "Posted Anger Fear Aggression dested Anger, Fear, Aggression True. "
    "Luke Skywalker, Jedi Knight qty 5 and Corran Horn qty 2 sheet-accurate overcounts. "
    "Posted Leia, Rebel Princess / Wedge Antilles, Red Squadron Leader / Threepio with his parts showing as titles. "
    "Line 24 Qui Gon's Light saber dested Qui-Gon's Lightsaber as written (could be Qui-Gon Jinn's Lightsaber). "
    "Posted Hoojix dested Houjix. Posted Grimtash dested Grimtaash. "
    "Posted Free Ride & Endor Occupation dested Free Ride & Endor Celebration. "
    "Posted Out of Commission & TT dested Out Of Commission & Transmission Terminated. "
    "Posted Sorry about the Mess & Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Posted The Bith Shuffle & Desperate Reach as title. "
    "Posted Sai'torr Kal Fas (Saltorr Kal Fon on sheet) dested Sai'torr Kal Fas. Posted Woolkin dested Wokling. "
    "Posted Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5 qty 2. "
    "Posted Obi Wan in Radiant VII dested Obi-Wan In Radiant VII (wiki page exists; not in GEMP file). "
    "Shields: Planday Defenses dested Planetary Defenses; Wise admin dested Wise Advice; Do or do not dested Do, Or Do Not. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Hunt Down and Destroy the Jedi dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Posted Executor Holotheatre dested Executor: Holotheatre. "
    "Posted CC: Security Tower dested Cloud City: Security Tower. "
    "Posted Endor Back Door dested Endor: Back Door. Posted Imperial Holotable as title. "
    "Posted 4Lom with Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Posted Darth Vader, DLotS dested Darth Vader, Dark Lord Of The Sith qty 3. "
    "Count Dooku qty 3, Darth Maul With Lightsaber qty 3, Emperor Palpatine qty 3 sheet-accurate. "
    "Posted Dr E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Posted Ability Ability Ability dested Ability, Ability, Ability. "
    "Posted Masterful Move & Endor Celebration dested Masterful Move & Endor Occupation qty 2. "
    "Visage Of The Emperor qty 3 (lines 5, 42, 43). "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Mace Windu", True, qty=2),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Corran Horn", qty=2),
    n("Luke Skywalker", True),
    n("Luke Skywalker, Jedi Knight", qty=5),
    n("Yoda, Keeper Of The Peace", True),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Threepio With His Parts Showing"),
    n("Luke's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Mace Windu's Lightsaber", True),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("A Few Maneuvers"),
    n("Escape Pod", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Free Ride & Endor Celebration"),
    n("Out Of Commission & Transmission Terminated"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Weapon Levitation"),
    n("Clash Of Sabers"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber"),
    n("Nar Shaddaa", True),
    n("Get To Your Ships!"),
    n("Crash Site Memorial"),
    n("Draw Their Fire"),
    n("Like My Father Before Me", True),
    n("Civil Disorder", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Azure Angel", True),
    n("Han, Chewie, And The Falcon"),
    n("Red Squadron 1"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses"),
    n("Weapons Display", True),
    n("The Republic No Longer Functions", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Goldenrod"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Visage Of The Emperor", qty=3),
    n("Prepared Defenses"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Endor: Back Door"),
    n("Imperial Holotable"),
    n("4-LOM With Concussion Rifle", True),
    n("Boba Fett, Bounty Hunter"),
    n("Count Dooku", True, qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=3),
    n("Grand Moff Tarkin", True),
    n("Janus Greejatus"),
    n("Blizzard 4", qty=2),
    n("Dooku's Lightsaber", True),
    n("Vader's Lightsaber"),
    n("Ability, Ability, Ability", True),
    n("Blast Door Controls"),
    n("Blaster Rack", True),
    n("Conduct Your Search"),
    n("First Strike"),
    n("The Phantom Menace", qty=3),
    n("No Escape"),
    n("Force Field", True, qty=2),
    n("Force Lightning", qty=2),
    n("Ghhhk"),
    n("Maul Strikes"),
    n("I Have You Now"),
    n("Masterful Move"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Sonic Bombardment", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Weapon Levitation"),
    n("You Are Beaten"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence", True),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
]
DS_ADD = []
