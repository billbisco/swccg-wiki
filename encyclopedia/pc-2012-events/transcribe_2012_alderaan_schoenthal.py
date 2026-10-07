#!/usr/bin/env python3
"""2012 Alderaan Regionals leftover Xerox: Chris Schoenthal.

Source: 2012AlderaanRegionals.pdf pages 5–6 (handwritten 2010 Xerox).
Name Chris Schoenthal dested Chris Schoenthal analog leftover 2012 Nats /
2012 MPC / 2013 Alderaan / 2014 TMW / pages/Chris_Schoenthal.wiki.
Username imrahil327 analog leftover 2012 Nats CANON. p05 Light Infiltration.
p06 Dark Kessel. Date 7/7/12. Do not dest as a new person. Do not dest as
Chris Haglund. Do not dest 2012 Nats / 2012 MPC / 2013 Alderaan / 2014 TMW
Schoenthal 60s again.
"""
from __future__ import annotations

PLAYER = "Chris Schoenthal"
USERNAME = "imrahil327"
STAGE = ""
PDF = "2012 Alderaan Regionals.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2012 Alderaan Regionals Chris Schoenthal LS.png"
DS_SCAN = "2012 Alderaan Regionals Chris Schoenthal DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p05 Light / p06 Dark. "
    "Name Chris Schoenthal dested Chris Schoenthal analog leftover 2012 Nats / "
    "2012 MPC / 2013 Alderaan / 2014 TMW. Username imrahil327 analog leftover "
    "2012 Nats CANON. Event Alderaan Regionals 7/7/12. "
    "Do not dest as a new person. Do not dest as Chris Haglund. "
    "Do not dest 2012 Nats / 2012 MPC / 2013 Alderaan / 2014 TMW Schoenthal 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p05 Light. Name Chris Schoenthal dested Chris Schoenthal. "
    "Username imrahil327. LIGHT checked. Deck Name This Deck Is Probably Bad dested off the article. "
    "Infiltration / Unlikely Allies empty dested Infiltration / Unlikely Allies analog leftover Martin. "
    "Nar Shaddaa : Undercity dested Nar Shaddaa: Undercity. "
    "Scoundrel's Luck Ingenuity / Bravado / Charm dested Scoundrel's Luck: Ingenuity / Bravado / Charm. "
    "A Good Blaster At Your Sale dested A Good Blaster At Your Side analog leftover. "
    "Krayt Dragon Howl & Armed And Danger dested Armed And Dangerous & Krayt Dragon Howl analog leftover combo. "
    "Escape Pod True (line 16) and Escape Pod empty (line 17) kept separate. "
    "Let The Wookiee Win True (line 22) and empty (line 23) kept separate. "
    "SATM/Blaster Prof dested Sorry About The Mess & Blaster Proficiency qty=2 analog leftover (lines 24 and 59). "
    "The Birth Shuffle & Desperate Reach dested as written. "
    "Han's Blaster, So Uncivilized dested Han's Blaster, So Uncivilized analog leftover Nelson. "
    "Booster's Star Destroyer dested Booster's Star Destroyer analog leftover Shannon. "
    "Booster In Pulsar Skate dested Booster In Pulsar Skate qty=2 (printed 38 plus extra 37 ditto). "
    "Extra misnumbered left 37–38 dest all written lines. "
    "Obi-Wan In Radiant VII dested Obi-Wan In Radiant VII analog leftover Gardner. "
    "Lando Calrissian, Scoundrel dested Lando Calrissian, Scoundrel analog leftover. "
    "Chewbacca, Walking Carpet dested Chewbacca, Walking Carpet analog leftover. "
    "Spaceport Scoundrel's Guild dested Scoundrel's Guild analog leftover. "
    "Nar Shaddaa: Scoundrel's Rest dested Nar Shaddaa: Scoundrel's Rest. "
    "Nar Shaddaa : Undercity Streets dested Nar Shaddaa: Undercity Streets. "
    "Do or Do Not dested Do, Or Do Not analog leftover. "
    "Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p06 Dark. Name Chris Schoenthal dested Chris Schoenthal. "
    "Username imrahil327. DARK checked. Deck Name 4 AM Thanks, Keith dested off the article. "
    "Kessel empty dested Kessel. Combat Readiness True IN THE 60. "
    "Kessel: Spice Mines-Admin Office dested Kessel: Spice Mines - Administrator's Office analog leftover Brady. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back! analog leftover combo. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider analog leftover combo. "
    "Sonic Bombardment True (line 13) and empty (line 14) kept separate. "
    "Masterful Move & Endor Oc dested Masterful Move & Endor Occupation analog leftover Atkin. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready & Imperial Propaganda analog leftover Jellison. "
    "The Mandalorian Father of Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Extra misnumbered left 37–38 dest all written lines (Boba Fett, Prepared Hunter / Admiral Kellaeen dested as written). "
    "Grotto Weibee dested Grotto Werribee analog leftover TMW Joe. "
    "Kessel: Spice Mines Extraction dested Kessel: Spice Mines - Extraction Facility analog leftover Brady. "
    "Knowledge & Defense dested Knowledge And Defense True IN THE 60. "
    "CHYBC dested Come Here You Big Coward analog leftover. "
    "YCHF dested You Cannot Hide Forever True analog leftover. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "Allegations of Corruption dested Allegations Of Corruption analog leftover. "
    "Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck"),
    n("Scoundrel's Luck: Ingenuity"),
    n("Scoundrel's Luck: Bravado"),
    n("Scoundrel's Luck: Charm"),
    n("A Good Blaster At Your Side"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Heading For The Medical Frigate"),
    n("Mirax Terrik"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Draw Their Fire"),
    n("Double Agent"),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("We Wish To Board At Once", qty=2),
    n("The Birth Shuffle & Desperate Reach"),
    n("Houjix"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Imperial Navigation Charts"),
    n("Advantage", True),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Flash Of Insight", True),
    n("Landing Claw"),
    n("Han's Blaster, So Uncivilized"),
    n("Leia's Blaster Rifle"),
    n("Rebel Agent's Blaster Rifle"),
    n("Chewbacca's Bowcaster"),
    n("Booster's Star Destroyer"),
    n("Booster In Pulsar Skate", qty=2),
    n("Obi-Wan In Radiant VII"),
    n("Boushh", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Rebel Agent", qty=3),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Corran Horn", qty=2),
    n("Sergeant Doallyn"),
    n("R2-D2", True),
    n("Scoundrel's Guild"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Nar Shaddaa: Undercity Streets"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Combat Response", True),
    n("Endor Shield", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Special Delivery", True),
    n("Alter", True),
    n("Much Anger In Him"),
    n("Imbalance & Kintan Strider"),
    n("Imperial Barrier"),
    n("Sonic Bombardment", True),
    n("Sonic Bombardment"),
    n("Close Call", True),
    n("Trample"),
    n("Lightsaber Deficiency", True),
    n("Imperial Command"),
    n("Cold Feet"),
    n("Why Didn't You Tell Me?"),
    n("Masterful Move & Endor Occupation"),
    n("Operational As Planned", True),
    n("Ghhhk"),
    n("Force Push", True),
    n("Imperial Decree", True),
    n("Lateral Damage"),
    n("Protocol Failure"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Battle Deployment", qty=2),
    n("Spice Mines Operations"),
    n("Kessel Surveillance System"),
    n("Darth Vader", True),
    n("The Emperor", True),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Admiral Kellaeen"),
    n("General Nevar"),
    n("Baron Soontir Fel"),
    n("General Veers", True),
    n("Grotto Werribee", True),
    n("Spice Mine Administrator", qty=2),
    n("Garindan", True, qty=2),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Slave I, Symbol Of Fear"),
    n("Vader's Personal Shuttle", True),
    n("Justifier"),
    n("Saber 1"),
    n("Maul's Sith Infiltrator"),
    n("Kashyyyk"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
