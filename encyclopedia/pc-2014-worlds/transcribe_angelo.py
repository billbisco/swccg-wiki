# Angelo Consoli (sheet Name: Angelo), 2014 Worlds Day 3 (2013 form).
# Xerox: extract/day3_r_p09.png (DS ASM), day3_r_p10.png (LS WHT(v)).
# Tuples are (name_or_None, is_v). Ditto expanded. (V) True only if the sheet box is checked.

ANGELO_DS_RESERVE = [
    ("A Stunning Move / A Valuable Hostage", False),
    ("Coruscant: Palpatine's Quarters", False),
    ("Coruscant: Private Platform (Docking Bay)", False),
    ("Imperial Propaganda", False),
    ("Prepared Defenses", True),
    ("Gift Of The Master", False),
    ("Ni Chuba Na??", True),
    ("Jabba's Haven", False),
    ("Darth Maul, Young Apprentice", False),
    ("They're Still Coming Through!", False),
    ("Sniper & Dark Strike", False),
    ("Dr. Evazan & Ponda Baba", False),
    ("Dooku's Lightsaber", False),
    ("Maul's Double-Bladed Lightsaber", False),
    ("Masterful Move", False),
    ("Battle Droid Squad", False),
    ("Count Dooku", False),
    ("Count Dooku", False),
    ("Masterful Move & Endor Occupation", False),
    ("Darth Maul, Young Apprentice", False),
    ("Darth Maul, Young Apprentice", False),
    ("Boba Fett In Slave I", True),
    ("P-59", False),
    ("Garindan", True),  # scrawl; Garindan (V) not a second Jango
    ("Zuckuss In Mist Hunter", False),
    ("Control & Set For Stun", False),
    ("Something Special Planned For Them", True),  # SS P, FT (V)
    ("A Dark Time For The Rebellion", True),
    ("Broken Concentration", True),
    ("Imperial Barrier", False),
    ("Victory", False),
    ("Imperial Propaganda", True),
    ("Jango Fett", False),
    ("Blockade Flagship: Docking Bay", False),
    ("Monnok", False),
    ("Elis Helrot", False),
    ("Oh, Switch Off", False),
    ("Battle Droid Squad", False),
    ("Imbalance & Kintan Strider", False),  # Imbalance Combo
    ("Disarmed", False),
    ("Force Field", True),
    ("Force Field", True),
    ("Blaster Rack", True),
    ("Blockade Flagship: Hallway", False),
    ("Operational As Planned", False),  # 45 OPM
    ("Force Push", True),  # 46
    ("OOM-9", True),  # 47
    ("Cold Feet", True),  # 48
    ("Nute Gunray", False),  # 49
    ("Dengar With Blaster Carbine", True),  # 50
    ("Sebulba", False),  # 51 S-scrawl; reads Sebulba
    ("Cyborg Commander", False),  # 52
    ("Cyborg Commander", False),  # 53
    ("IG-Bodyguard Droid", False),
    ("No Escape", False),
    ("Search And Destroy", False),
    ("Blockade Flagship: Bridge", False),
    ("Force Lightning", False),
    ("Dark Jedi Lightsaber", True),
    ("Knowledge And Defense", False),
]  # 60 tuples (name_or_None, is_v)
# NOTES DS reserve:
# 1  ASM — A Stunning Move / A Valuable Hostage; (V) empty.
# 2  Coruscant: Palp. QR. — Coruscant: Palpatine's Quarters.
# 3  Coruscant: PP DB — Coruscant: Private Platform (Docking Bay).
# 4  Imp. Prop. — Imperial Propaganda; (V) empty (line 32 is the (V) copy).
# 5  Prep. Def. (V) — Prepared Defenses.
# 6  Gift of the Maker — Gift Of The Master (vb4); last word reads Maker.
# 7  Ni Chu (V) — Ni Chuba Na (printed Ni Chuba Na??).
# 8  Jabba's Haven.
# 9  Darth Maul YH — Darth Maul, Young Apprentice; (V) empty.
# 10 They're Still Coming Through!
# 11 Sniper Combo — Sniper & Dark Strike.
# 12 Dr. Evazan Combo — Dr. Evazan & Ponda Baba.
# 13 Dooken's LS — Dooku's Lightsaber.
# 14 Maul's Double Bladed LS — Maul's Double-Bladed Lightsaber.
# 15 MM — Masterful Move.
# 16 Battle Droid Squad.
# 17–18 Count Dooku — sheet looks like "Civil Pooh"; ditto on 18. Expanded via Dooku's Lightsaber + unique Count Dooku. Uncertain.
# 19 MM Combo — Masterful Move & Endor Occupation (printed combo).
# 20–21 crossed-out title then Darth Maul YH + "non-V"; (V) boxes checked. Followed the written non-V (is_v False).
# 22 Boba in SI (V) — Boba Fett In Slave I.
# 23 P-59.
# 24 Jango (V) — Jango Fett; one-word scrawl. Alternate Garindan (V). Line 33 is Jango Fett with (V) empty (possibly Jango Fett, The Assassin vs Jango Fett).
# 25 Zuckuss in MH — Zuckuss In Mist Hunter.
# 26 Control Combo — Control & Set For Stun.
# 27 SS P, FT (V) — unread; not uniquely expanded (possibly Sith Fury).
# 28 Bad Time (V) — A Dark Time For The Rebellion; first letter looks like B not D.
# 29 Broken Concentration (V).
# 30 Imp. Barrier — Imperial Barrier.
# 31 Victory.
# 32 Imp. Propaganda (V) — Imperial Propaganda.
# 33 Jango Fett; (V) empty.
# 34 BF: DB — Blockade Flagship: Docking Bay.
# 35 Monnok (looks like Maulok).
# 36 Elis Helrot.
# 37 Oh Switch Off — Oh, Switch Off.
# 38 Battle Droid Squad (2nd).
# 39 Turbulence Combo — clearly written; no unique printed title in the 2014 pool.
# 40 Disarmed.
# 41–42 Force Field (V); ditto.
# 43 Blaster Rack (V).
# 44 BF: Hallway — Blockade Flagship: Hallway.
# 45 OOM — OOM-9; (V) empty. Alternate OOM Command Battle Droid (line 47 writes OOM-9).
# 46 Force Push (V).
# 47 OOM-9 (V).
# 48 Cold Feet (V).
# 49 Nute Gunray.
# 50 Dengar w/Gun (V) — Dengar With Blaster Carbine.
# 51 S-scrawl — unread (possibly Sebulba).
# 52–53 Cyborg Commander — clearly written; no printed title. Ditto on 53.
# 54 IG-Bodyguard Droid — clearly written; no printed title (possibly IG-88).
# 55 No Escape.
# 56 Search + Destroy — Search And Destroy.
# 57 BF: Bridge — Blockade Flagship: Bridge.
# 58 Force Lightning.
# 59 Dark Jedi LS (V) — Dark Jedi Lightsaber.
# 60 K+D — Knowledge And Defense.

ANGELO_DS_SHIELDS = [
    ("Weapon Of A Sith", False),
    ("I Find Your Lack Of Faith Disturbing", True),
    ("Do They Have A Code Clearance?", True),
    ("A Useless Gesture", True),
    ("Battle Order", False),
    ("You Cannot Hide Forever", True),
    ("Fanfare", True),
    ("Resistance", False),
    ("Imperial Detention", False),
    ("There Is No Try", True),
    ("Secret Plans", False),
    ("Firepower", True),
    ("Come Here You Big Coward", True),
    ("Allegations Of Corruption", False),
    ("Abyss", True),
]  # 15 tuples
# NOTES DS shields:
# 1  Weapon of a Sith — Weapon Of A Sith; (V) empty.
# 2  I Find Your Lack… (V) — I Find Your Lack Of Faith Disturbing.
# 3  Code Clearance (V) — Do They Have A Code Clearance?
# 4  A Useless Gesture (V).
# 5  Battle Order.
# 6  You Cannot Hide Forever (V).
# 7  Fanfare (V).
# 8  Resistance.
# 9  Imp. Det — Imperial Detention (vsh); not Imperial Decree.
# 10 There Is No Try — slash/tick in (V) box.
# 11 Secret Plans.
# 12 Firepower (V).
# 13 CHYBC (V) — Come Here You Big Coward.
# 14 Allegations — Allegations Of Corruption.
# 15 Abyss (V).

ANGELO_LS_RESERVE = [
    ("We'll Handle This / Duel Of The Fates", True),
    ("Coruscant: Jedi Council Chamber", True),
    ("Heading For The Medical Frigate", False),
    ("Republic Logistics", False),
    ("Quick Draw", True),
    ("Wokling", True),
    ("Coruscant: Jedi Archives", False),
    ("Coruscant: Night Club", False),
    ("Kashyyyk: Forest Depths", False),
    ("Obi-Wan's Lightsaber", False),
    ("Jedi Lightsaber", True),
    ("Jedi Lightsaber", True),
    ("Sai'torr Kal Fas", True),
    ("A Jedi's Resilience", False),
    ("Menace Fades", False),
    ("Disarmed", False),
    ("Your Insight Serves You Well", False),
    ("Honor Of The Jedi", False),
    ("Mace Windu", True),
    ("Mace Windu, Master Of The Order", False),
    ("Qui-Gon Jinn With Lightsaber", False),
    ("Qui-Gon Jinn With Lightsaber", False),
    ("Obi-Wan Kenobi, Jedi Knight", True),
    ("Obi-Wan Kenobi, Jedi Knight", True),
    ("Maris Brood, Fallen Jedi", False),
    ("Ki-Adi-Mundi", True),
    ("Jedi Advisor", False),
    ("Jedi Advisor", False),
    ("Depa Billaba", False),
    ("Plo Koon", False),
    ("Yoda, Senior Council Member", True),
    ("Threepio With His Parts Showing", False),
    ("Imperial Atrocity", True),
    ("Imperial Atrocity", True),
    ("Under Attack", False),
    ("Under Attack", False),
    ("Impressive, Most Impressive", True),
    ("Desperate Reach", True),
    ("A Jedi's Resilience", False),
    ("A Jedi's Resilience", False),
    ("Sense", False),
    ("Sense", False),
    ("Alter (Coruscant)", True),
    ("Hear Me Baby, Hold Together", True),
    ("Sorry About The Mess", False),
    ("Sorry About The Mess & Blaster Proficiency", False),
    ("Shady Jedi Combo", False),
    ("Nabrun Leids", False),
    ("Nabrun Leids", False),
    ("Blaster Deflection", False),
    ("Blaster Deflection", False),
    ("Speak With The Jedi Council", False),
    ("It Could Be Worse", False),
    ("We're Doomed", False),
    ("Let The Wookiee Win", True),
    ("Let The Wookiee Win", True),
    ("Are You Brain Dead?!", False),
    ("Mandalorian Mishap & Jedi Mind Trick", False),
    ("It's A Trap!", False),
    ("Anger, Fear, Aggression", True),
]  # 60 tuples (name_or_None, is_v)
# NOTES LS reserve:
# 1  WHT (V) — We'll Handle This / Duel Of The Fates. Deck name WHT(v). Not Watch Your Step (no Tatooine/cantina; Coruscant Jedi Council + Wokling + Sai'torr).
# 2  Cor.: CC (V) — Coruscant: Jedi Council Chamber.
# 3  Heading For The Med — Heading For The Medical Frigate.
# 4  Rep. logistics — Republic Logistics (vb6); not legislation.
# 5  Quick Draw (V).
# 6  Wokling (V).
# 7  Cor.: Jedi Arch — Coruscant: Jedi Archives.
# 8  Cor.: Night Club — Coruscant: Night Club.
# 9  Kashyyyk: For. Depths — Kashyyyk: Forest Depths.
# 10 Obi's LS (green) — Obi-Wan's Lightsaber; (green) as written (blade/printing note).
# 11–12 Jedi LS (V) — Jedi Lightsaber; ditto.
# 13 Sai'torr KF (V) — Sai'torr Kal Fas.
# 14 AJR — A Jedi's Resilience; (V) empty. Copies also at 39–40.
# 15 Menace Fades.
# 16 Disarmed.
# 17 Your Insight S.Y.W — Your Insight Serves You Well (Effect in reserve); (V) empty. Shield 3 is the (V) shield.
# 18 Honor — Honor Of The Jedi.
# 19 Mace Windu (V).
# 20 Mace Windu, MOTO — Mace Windu, Master Of The Order.
# 21–22 Qui-Gon W/LS — Qui-Gon Jinn With Lightsaber; ditto.
# 23–24 Obi-Wan Ken., JK (V) — Obi-Wan Kenobi, Jedi Knight; ditto.
# 25 Fallen Jedi — Maris Brood, Fallen Jedi (unique Fallen Jedi title).
# 26 Ki-Adi-Mundi (V).
# 27–28 Jedi Adv — Jedi Advisor; ditto.
# 29 Depa — Depa Billaba.
# 30 Plo Koon.
# 31 Yoda, SCM (V) — Yoda, Senior Council Member.
# 32 Threepio, WHPS — Threepio With His Parts Showing.
# 33–34 Atrocity (V) — Imperial Atrocity; ditto.
# 35–36 Under Attack; ditto.
# 37 Impressive, MI (V) — Impressive, Most Impressive.
# 38 Desp. Reach (V) — Desperate Reach; filled blob before the title.
# 39–40 AJR — A Jedi's Resilience; ditto. Third/fourth copies with line 14.
# 41–42 Sense (prem) — Sense (Premiere); ditto.
# 43 Alter (corr) (V) — Alter (Coruscant).
# 44 HMB, HT (V) — Hear Me Baby, Hold Together. Second letter messy (HMB vs HBT).
# 45 Sorry — Sorry About The Mess.
# 46 Sorry Combo — Sorry About The Mess & Blaster Proficiency.
# 47 Shady Jedi Combo — clearly written; no unique printed combo in the 2014 pool.
# 48–49 Nabrun — Nabrun Leids; ditto.
# 50–51 Blaster Defl. — Blaster Deflection; ditto.
# 52 Speak — Speak With The Jedi Council.
# 53 It Could Be Worse.
# 54 We're Doomed.
# 55–56 LTWW (V) — Let The Wookiee Win; ditto.
# 57 Are You Brain Dead — Are You Brain Dead?!
# 58 Mandalorian Mishap Combo — Mandalorian Mishap & Jedi Mind Trick (vb9 combo; 9.2 tentatively legal).
# 59 It's A Trap — It's A Trap!
# 60 AFA (V) — Anger, Fear, Aggression.

ANGELO_LS_SHIELDS = [
    ("Yavin Sentry", True),
    ("Let's Keep A Little Optimism Here", True),
    ("Your Insight Serves You Well", True),
    ("The Professor", False),
    ("Ultimatum", False),
    ("Don't Do That Again", True),
    ("Simple Tricks And Nonsense", False),
    ("Battle Plan", False),
    ("Do, Or Do Not", False),
    ("Weapons Display", True),
    ("Aim High", True),
    ("A Tragedy Has Occurred", False),
    ("Chasm", False),
    ("Only Jedi Carry That Weapon", False),
    ("Wise Advice", False),
]  # 15 tuples
# NOTES LS shields:
# 1  Yavin Sentry (V).
# 2  Let's Keep a Little… (V) — Let's Keep A Little Optimism Here.
# 3  Insight (V) — Your Insight Serves You Well (shield).
# 4  Professor — The Professor; (V) empty.
# 5  Ultimatum.
# 6  DDTA (V) — Don't Do That Again.
# 7  Simple Tricks — Simple Tricks And Nonsense.
# 8  Battle Plan.
# 9  DODN — Do, Or Do Not.
# 10 Weapons Display (V).
# 11 Aim High — (V) box looks filled.
# 12 Tragedy — A Tragedy Has Occurred.
# 13 Chasm; (V) empty.
# 14 Only Jedi… — Only Jedi Carry That Weapon.
# 15 Wise Advice.

assert len(ANGELO_DS_RESERVE) == 60, len(ANGELO_DS_RESERVE)
assert len(ANGELO_DS_SHIELDS) == 15, len(ANGELO_DS_SHIELDS)
assert len(ANGELO_LS_RESERVE) == 60, len(ANGELO_LS_RESERVE)
assert len(ANGELO_LS_SHIELDS) == 15, len(ANGELO_LS_SHIELDS)
