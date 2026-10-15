#!/usr/bin/env python3
"""2015 European Championship Day 2: Floris de Vries (place 35).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p37 Dark / p38 Light typed category lists.
"""
from __future__ import annotations

PLAYER = "Floris de Vries"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 38
DS_PAGE = 37
LS_SCAN = "2015 European Championship Floris de Vries LS.png"
DS_SCAN = "2015 European Championship Floris de Vries DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18-35 p37 Dark / p38 Light typed category lists, circled 35. "
    "Header Floris de Vries Netherlands; no username. "
    "Deck labels DS \"Walkers\", LS \"Profit\" (kept off DECK_NAME). DS 0:4 / LS 1:3 handwritten."
)
LS_NOTE = (
    "START You Can Either Profit By This.../Or Be Destroyed. "
    "Posted Sai Tor Kal Fas v dested Sai'torr Kal Fas True. "
    "Posted Lando With Vibro-Axe dested Lando With Vibro-Ax. "
    "Posted Threepio With Parts Showing dested Threepio With His Parts Showing. "
    "Posted R2-D2 v dested R2-D2 (Artoo-Detoo) True. "
    "Handwritten '+ Yoxgit' after Leesub Sirln -> Yoxgit added (needed for 60). "
    "Weapon Levitation struck through -> not in deck. "
    "Posted Hear Me Baby Hold Together dested Hear Me Baby, Hold Together. "
    "Posted Speak With The Council dested Speak With The Jedi Council qty 3. "
    "Posted Run, Luke, Run! dested Run Luke, Run!. "
    "Posted Tatooine: Lars Moisture Farm dested Tatooine: Lars' Moisture Farm. "
    "Posted I Hope She's Alright dested I Hope She's All Right. "
    "Posted Do Or Do not dested Do, Or Do Not. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Combat Readiness v (V box) dested Combat Readiness True; wiki title Combat Readiness (V) matches. "
    "Posted Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Posted Hoth: 3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Posted Hoth: Echo Base Docking Bay dested Hoth: Echo Docking Bay. "
    "Posted Marek Steele, Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Posted Dr Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Posted Boba Fett in Slave One v dested Boba Fett In Slave I True. "
    "Posted Twilek Advisor dested Twi'lek Advisor. "
    "Posted We Must Accellerate Our Plans dested We Must Accelerate Our Plans. "
    "Walker Garrison listed under Interrupts on sheet (it is an Effect). Takeel qty 4. "
    "Posted We'll Let Fate-a-decide huh? dested We'll Let Fate-a Decide, Huh?. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Heading For The Medical Frigate"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("I Must Be Allowed To Speak", True),
    n("Master Luke", qty=3),
    n("Ben Kenobi", qty=2),
    n("Yoda, Keeper Of The Peace", qty=2),
    n("Leia, Rebel Princess"),
    n("Princess Leia", True),
    n("Chewbacca, Protector"),
    n("Lando With Vibro-Ax"),
    n("Threepio With His Parts Showing"),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Mirax Terrik"),
    n("Leesub Sirln", True),
    n("Yoxgit"),
    n("Booster In Pulsar Skate"),
    n("Obi-Wan's Journal", qty=2),
    n("Landing Claw"),
    n("Luke's Bionic Hand", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Free Ride & Endor Celebration", qty=2),
    n("Dodge", qty=2),
    n("Nabrun Leids", qty=2),
    n("Double Agent", qty=2),
    n("Hear Me Baby, Hold Together", True, qty=2),
    n("Tunnel Vision", qty=2),
    n("Speak With The Jedi Council", qty=3),
    n("Impressive, Most Impressive", True),
    n("Run Luke, Run!"),
    n("Skywalkers"),
    n("Under Attack"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Coruscant: Jedi Council Chamber"),
    n("Obi-Wan's Lightsaber"),
    n("Anakin's Lightsaber", True),
    n("Leia's Blaster Rifle"),
    n("I Hope She's All Right"),
    n("A Good Blaster At Your Side"),
    n("A Gift"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Planetary Defenses"),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("The Republic No Longer Functions"),
    n("Goldenrod"),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Combat Readiness"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hoth"),
    n("Combat Readiness", True),
    n("Hoth: Ice Plains (5th Marker)"),
    n("You May Start Your Landing"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Kuat Drive Yards", True),
    n("Prepare For A Surface Attack"),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("Imperial Justice", True, qty=2),
    n("Rebel Base Occupation", qty=2),
    n("Ice Storm"),
    n("Presence Of The Force", qty=2),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Echo Docking Bay"),
    n("Coruscant: Docking Bay"),
    n("Fondor"),
    n("Darth Vader", True),
    n("DS-61-2"),
    n("DS-61-5"),
    n("Grand Moff Tarkin", True),
    n("General Veers", True),
    n("Commander Igar"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Mara Jade, The Emperor's Hand"),
    n("Prince Xizor"),
    n("Dr. Evazan & Ponda Baba"),
    n("Lieutenant Cabbel"),
    n("Boba Fett In Slave I", True),
    n("Thunderflare"),
    n("Tyrant"),
    n("Devastator"),
    n("Conquest", True),
    n("Stalker", True),
    n("Tempest 1"),
    n("Blizzard 4"),
    n("Blizzard 2", True),
    n("Blizzard 1"),
    n("Blizzard Scout 1", True),
    n("Blizzard Walker", qty=3),
    n("Imperial Walker", qty=2),
    n("Walker Garrison", qty=2),
    n("Twi'lek Advisor"),
    n("We Must Accelerate Our Plans"),
    n("Takeel", qty=4),
    n("Close Call", True, qty=2),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Vote Of No Confidence"),
    n("Resistance"),
    n("Imperial Detention", True),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?", True),
]
DS_ADD = []
