#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Greg Shaw.

Source: Yavin42012.pdf pages 27–28.
p27 Dark typed 2010 Xerox / p28 Light handwritten 2010 Xerox.
Name Gregory Shaw dested Greg Shaw analog leftover generate_2012_nats.py
CANON Gregory Shaw / player-stubs/Greg_Shaw.wiki / transcribe_2013_tmw_shaw.py.
Username blank. Pack player-stubs/Greg_Shaw.wiki.
Do not dest as a new person. Do not dest 2012 TMW / Nats / MPC /
2013 TMW / SoCal / Alderaan Greg Shaw 60s again.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2012 Yavin 4 Regionals Greg Shaw LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p27 Dark typed 2010 Xerox / p28 Light handwritten 2010 Xerox. "
    "Name Gregory Shaw dested Greg Shaw analog leftover generate_2012_nats.py "
    "CANON / player-stubs/Greg_Shaw.wiki. Username blank. "
    "Event Date 06/30/12 Event Name Yavin IV Regionals dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name BAM HuntDown / Hippie Lawyer dested off article. "
    "Do not dest as a new person. Do not dest 2012 TMW / Nats / MPC / "
    "2013 TMW / SoCal / Alderaan Greg Shaw 60s again. "
    "Pack player-stubs/Greg_Shaw.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p28 Light. Name GREGORY SHAW Username blank. "
    "Event Date 06/30/12 Event Name YAVIN IV REGIONALS dest Yavin 4 facing pair. LIGHT checked. "
    "Infiltration dested analog leftover Skilton empty. "
    "Nar Shadda dested Nar Shaddaa analog leftover dest as written slang. "
    "Boss Nass Chambers dested analog leftover dest as written Haid. "
    "Booster In Pulsar Skate dested analog leftover dest as written. "
    "Rebel Agent's Blaster dested Rebel Agent's Blaster Rifle analog leftover TYPE_OVERRIDE. "
    "Rebel Agent empty qty=3 analog leftover consecutive ditto. "
    "BoShek empty qty=2 analog leftover consecutive TYPE_OVERRIDE. "
    "Corran Horn empty qty=2 analog leftover consecutive. "
    "Lando Calrissian, Scoundrel empty qty=2 analog leftover consecutive Westergard. "
    "Chewdacca Walking Carpet dested Chewbacca, Walking Carpet analog leftover dest as written slang. "
    "Wyron Serper dested Wyrn Serper analog leftover dest as written slang. "
    "Lt Blount dested Lieutenant Blount analog leftover dest as written slang. "
    "Klorslug dested K'lor'slug analog leftover dest as written slang. "
    "Seekers An Audience dested Seeking An Audience analog leftover dest as written slang. "
    "Escape Pod True qty=2 analog leftover consecutive. "
    "Wesa Gotta Grand Army empty qty=2 analog leftover consecutive. "
    "Speak With The Jedi empty qty=2 analog leftover consecutive. "
    "Let The Wookiee Win True qty=2 analog leftover consecutive. "
    "Rebel Barrier empty qty=2 analog leftover consecutive. "
    "Houtix dested Houjix analog leftover dest as written slang. "
    "Contro & Tunnel Vision dested Control & Tunnel Vision analog leftover dest as written combo. "
    "Sabotage True qty=2 analog leftover consecutive. "
    "Leadon Levitation dested Weapon Levitation analog leftover dest as written slang. "
    "All Wings Report & DS dested All Wings Report In & Darklighter Spin analog leftover dest as written combo qty=2 consecutive. "
    "Antilles Man & Rebel Re dested Antilles Maneuver & Rebel Reinforcements analog leftover Cooleo. "
    "He Can Go About His Business crossed dest Chasm True analog leftover dest as written replacement. "
    "Only Jedi Carry dested Only Jedi Carry That Kind Of Firepower analog leftover dest as written slang. "
    "Simple Tricks dested Simple Tricks And Nonsense analog leftover dest as written slang Brummett. "
    "Let's Keep Optimism dested Let's Keep A Little Optimism Here analog leftover TYPE_OVERRIDE. "
    "Wise Advice dested analog leftover dest as written slang. "
    "Shields 1–12 filled. Unique 60 shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox p27 Dark. Name Gregory Shaw Username blank. "
    "Event Date 06/30/12 Event Name Yavin IV Regionals dest Yavin 4 facing pair. DARK checked. "
    "Hunt Down and Destroy the Jedi dested Hunt Down And Destroy The Jedi empty analog leftover dest as written. "
    "Executer dested Executor analog leftover dest as written slang. "
    "Darth Vader, Betrayer of the Jedi empty qty=4 analog leftover consecutive dest as written. "
    "Emperor Palpatine empty qty=3 analog leftover consecutive. "
    "Galen, Secret Apprentice empty qty=3 analog leftover consecutive dest as written. "
    "Darth Maul with Lightsaber empty qty=2 analog leftover consecutive; line 19 crossed dest Sith Fury True analog leftover crossed-with-replacement. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin analog leftover Nieland. "
    "Garindan True qty=2 analog leftover consecutive dest as written. "
    "Blizzard 4 empty qty=2 analog leftover consecutive. "
    "Force Field True qty=2 analog leftover consecutive. "
    "Imbalance & Kintan Strider dested analog leftover dest as written combo. "
    "Sonic Bombardment True qty=3 analog leftover consecutive. "
    "We Must Accelerate Our Plans empty qty=2 analog leftover consecutive. "
    "Luke? Luuuuke! crossed dest Sith Fury True dest qty=2 at first lines 19/47 analog leftover non-consecutive. "
    "Tarkin's Bounty crossed dest Wipe Them Out, All Of Them True analog leftover Schmaltz. "
    "Revenge of the Sith empty qty=2 analog leftover consecutive dest as written. "
    "Ni Chuba Na?? dested Ni Chuba Na? analog leftover TYPE_OVERRIDE. "
    "Visage of the Emperor empty qty=2 analog leftover consecutive dest as written. "
    "Knowledge and Defense dested Knowledge And Defense True analog leftover Anderson IN THE 60. "
    "We'll Let Fate-a Decide, HUH? dested We'll Let Fate Decide, Huh analog leftover TYPE_OVERRIDE. "
    "Shields 1–12 filled. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration"
LS_CARDS = [
    n("Infiltration"),
    n("Nar Shaddaa"),
    n("Undercity"),
    n("Scoundrel's Den"),
    n("Undercity Street"),
    n("Boss Nass Chambers"),
    n("Jedi Council Chamber", True),
    n("Scoundrel's Luck"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Ingenuity"),
    n("Booster's Star Destroyer"),
    n("Booster In Pulsar Skate"),
    n("Millennium Falcon", True),
    n("Rebel Agent's Blaster Rifle"),
    n("Leia's Blaster Rifle"),
    n("Rebel Agent", qty=3),
    n("BoShek", qty=2),
    n("Corran Horn", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Captain Han Solo"),
    n("Chewbacca, Walking Carpet"),
    n("Talon Karrde"),
    n("Mirax Terrik"),
    n("Dash Rendar", True),
    n("Wyrn Serper", True),
    n("Tycho Celchu", True),
    n("Lieutenant Blount", True),
    n("Imperial War Charts"),
    n("K'lor'slug", True),
    n("Hindsight", True),
    n("Flash Of Insight", True),
    n("Undercover", True),
    n("Seeking An Audience", True),
    n("Escape Pod", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Houjix"),
    n("Control & Tunnel Vision"),
    n("Sabotage", True, qty=2),
    n("Double Agent"),
    n("Weapon Levitation"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Don't Tread On Me", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Kind Of Firepower"),
    n("Aim High"),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("You Cannot Hide Forever", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Chasm", True),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Endor: Back Door"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader, Betrayer Of The Jedi", qty=4),
    n("Emperor Palpatine", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Sith Fury", True, qty=2),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Bane Malar", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Garindan", True, qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Blizzard 4", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Cold Feet", True),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Force Lightning"),
    n("They're Still Coming Through"),
    n("Prepared Defenses", True),
    n("Masterful Move"),
    n("Imbalance & Kintan Strider"),
    n("Sonic Bombardment", True, qty=3),
    n("We Must Accelerate Our Plans", qty=2),
    n("First Strike"),
    n("Emperor's Power", True),
    n("Wipe Them Out, All Of Them", True),
    n("Revenge Of The Sith", qty=2),
    n("No Escape"),
    n("A Sith's Weapon"),
    n("Conduct Your Search"),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("Visage Of The Emperor", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Leave Them To Me", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate Decide, Huh"),
    n("Abyss", True),
    n("Resistance"),
]
DS_ADD = []
