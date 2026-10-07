# Greg Shaw, 2014 Worlds Day 3 (2013 form). Xerox: extract/day3_r_p03.png (DS), day3_r_p04.png (LS).
# Tuples are (name_or_None, is_v). Ditto expanded. (V) True only if the sheet box is checked.

SHAW_DS_RESERVE = [
    ("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    ("Knowledge And Defense", True),
    ("Coruscant", False),
    ("Coruscant: Imperial City", False),
    ("A Sith's Plans", False),
    ("Endor Shield", True),
    ("Ni Chuba Na??", True),
    ("Gift Of The Master", False),
    ("Prepared Defenses", True),
    ("Endor", False),
    ("Blockade Flagship: Bridge", False),
    ("Naboo: Theed Palace Generator Core", False),
    ("Probot", False),
    ("P-59", False),
    ("Galen Marek, Starkiller", False),
    ("Galen Marek, Starkiller", False),
    ("Galen Marek, Starkiller", False),
    ("Dengar With Blaster Carbine", True),
    ("Garindan", True),
    ("Dr. Evazan & Ponda Baba", False),
    ("Darth Vader, Dark Lord Of The Sith", False),
    ("Darth Vader, Dark Lord Of The Sith", False),
    ("Darth Vader, Dark Lord Of The Sith", False),
    ("Juno Eclipse, Black Leader", False),
    ("Juno Eclipse, Black Leader", False),
    ("General Nevar", False),
    ("Grand Moff Tarkin", True),
    ("Boba Fett, Bounty Hunter", False),
    ("Mara Jade With Lightsaber", False),
    ("Admiral Ozzel", False),
    ("Emperor Palpatine", False),
    ("Emperor Palpatine", False),
    ("Vader's Lightsaber", False),
    ("Galen's Lightsaber, Vader's Gift", False),
    ("Victory", False),
    ("Rogue Shadow", False),  # sheet Galen's Fighter
    ("Blizzard 4", False),
    ("Ghhhk", False),
    ("Force Lightning", False),
    ("Cold Feet", True),
    ("One Beautiful Thing", False),
    ("One Beautiful Thing", False),
    ("Stop Motion", True),
    ("We Must Accelerate Our Plans", False),
    ("We Must Accelerate Our Plans", False),
    ("We Must Accelerate Our Plans", False),
    ("Weapon Levitation & The Empire's Back", False),
    ("Masterful Move", False),
    ("Force Field", True),
    ("Force Push", True),
    ("Blaster Rack", True),
    ("Revenge Of The Sith", False),
    ("Combat Response", True),
    ("Imperial Propaganda", True),
    ("Blast Door Controls", False),
    ("No Escape", False),
    ("Emperor's Power", True),
    ("Presence Of The Force", False),
    ("Masterful Move", False),
    ("Close Call", True),
]  # 60 tuples (name_or_None, is_v)
# NOTES DS reserve:
# 1  Hunt Down... / TFHG (V) checked; expanded 7-side.
# 12 Naboo: Theed Palace Generator Core — last word squeezed against (V) box; read CORE not Generator.
# 28 Boba Fett, Bounty Hunter — left "have" tick missing; title present, (V) empty.
# 36 Galen's Fighter — clearly written; no SWCCG printed title (likely Rogue Shadow).
# 38 Ghhhk — short scrawl GHHHK.
# 47 Weapon Levitation & The Empire's Back — last words cramped; Empire's not Emperor's.
# 50 Force Push (V) — slash-check.
# 60 Close Call (V) — X in box.

SHAW_DS_SHIELDS = [
    ("Fanfare", True),
    ("There Is No Try", False),
    ("I Find Your Lack Of Faith Disturbing", True),
    ("Resistance", False),
    ("You Cannot Hide Forever", True),
    ("Firepower", True),
    ("Do They Have A Code Clearance?", True),
    ("Death Star Sentry", True),
    ("Battle Order", False),
    ("Allegations Of Corruption", False),
    ("Weapon Of A Sith", False),
    ("Abyss", True),
    ("Come Here You Big Coward", False),
    ("Secret Plans", False),
    ("Oppressive Enforcement", False),
]  # 15 tuples
# NOTES DS shields:
# 2  There Is No Try — (V) empty (not the combo).
# 12 Abyss (V) — box filled; Come Here You Big Coward / Secret Plans / Oppressive Enforcement empty.

SHAW_LS_RESERVE = [
    ("Tatooine: Slave Quarters", False),
    ("It Is The Future You See", True),
    ("Battle Plan & Draw Their Fire", False),
    ("Do, Or Do Not & Wise Advice", False),
    ("Quick Draw", True),
    ("Coruscant: Jedi Council Chamber", True),
    ("Home One: War Room", False),
    ("Naboo: Boss Nass' Chambers", False),
    ("Naboo: Battle Plains", False),
    ("Yavin 4: Massassi War Room", True),
    ("Luke Skywalker, Jedi Knight", False),
    ("Luke Skywalker, Jedi Knight", False),
    ("Luke Skywalker, Strong In The Force", False),
    ("Luke Skywalker, Strong In The Force", False),
    ("Mace Windu", True),
    ("Mace Windu", True),
    ("Mace Windu", True),
    ("Lando Calrissian, Unlikely Hero", False),
    ("Lando Calrissian, Unlikely Hero", False),
    ("Master Qui-Gon", True),
    ("Master Qui-Gon", True),
    ("Corran Horn", False),
    ("Leia, Rebel Princess", False),
    ("Admiral Ackbar", True),
    ("Anakin Skywalker, Padawan Learner", False),
    ("Jaina Solo", False),
    ("Obi-Wan Kenobi", True),
    ("Luke's Lightsaber", False),
    ("Jedi Lightsaber", True),
    ("Qui-Gon's Lightsaber", False),
    ("Artoo-Detoo In Red 5", False),
    ("Artoo-Detoo In Red 5", False),
    ("Han, Chewie, And The Falcon", True),
    ("Han, Chewie, And The Falcon", True),
    ("Lady Luck", False),
    ("Home One", False),
    ("Imperial Atrocity", True),
    ("Imperial Atrocity", True),
    ("Mechanical Failure", False),
    ("Sai'torr Kal Fas", True),
    ("Seeking An Audience", True),
    ("What're You Tryin' To Push On Us?", False),
    ("Escape Pod", True),
    ("Escape Pod", True),
    ("Houjix", False),
    ("Rebel Leadership", True),
    ("Rebel Leadership", True),
    ("Rebel Leadership", True),
    ("Blaster Deflection", False),
    ("A Jedi's Resilience", False),
    ("A Jedi's Resilience", False),
    ("Sorry About The Mess & Blaster Proficiency", False),
    ("Wesa Gotta Grand Army", False),
    ("Wesa Gotta Grand Army", False),
    ("Wesa Gotta Grand Army", False),
    ("Speak With The Jedi Council", False),
    ("Let The Wookiee Win", True),
    ("Let The Wookiee Win", True),
    ("Let The Wookiee Win", True),
    ("Anger, Fear, Aggression", True),
]  # 60 tuples (name_or_None, is_v)
# NOTES LS reserve:
# 4  Do, Or Do Not & Wise Advice — ampersand combo (Reflections).
# 7  Home One: War Room — left "have" tick missing; title present.
# 15-17 Mace Windu (V) — wrote "Mace Windu" not Master Of The Order; X-checks.
# 25 Anakin Skywalker, Padawan Learner — sheet "Anakin Skywalker, Padawan"; (V) empty.
# 27 Obi-Wan Kenobi (V) — "Obi Wan Kenobi", not Master Kenobi.
# 39 Mechanical Failure — sheet "Mech Failure".
# 42 What're You Tryin' To Push On Us? — truncated after Push.
# 44 Escape Pod (V) — slash-check (ditto of 43).
# 48 Rebel Leadership (V) — slash-check (ditto of 46-47).
# 51 A Jedi's Resilience — ditto of 50; left tick scribbled, (V) empty.
# 52 Sorry About The Mess & Blaster Proficiency — "BlasterProf" cut off.
# 56 Speak With The Jedi Council — sheet "Speak with the Jedi!".
# 59 Let The Wookiee Win (V) — slash-check (ditto of 57-58).

SHAW_LS_SHIELDS = [
    ("Let's Keep A Little Optimism Here", True),
    ("Chasm", True),
    ("Planetary Defenses", True),
    ("A Tragedy Has Occurred", False),
    ("Only Jedi Carry That Weapon", False),
    ("Don't Do That Again", True),
    ("Simple Tricks And Nonsense", False),
    ("Weapons Display", True),
    ("Ultimatum", False),
    ("Your Insight Serves You Well", True),
    ("Another Pathetic Lifeform", False),
    ("Affect Mind", True),
    ("The Professor", True),
    ("Aim High", False),
    ("Yavin Sentry", True),
]  # 15 tuples
# NOTES LS shields:
# 1  Let's Keep A Little Optimism Here — sheet "Let's Keep Optimism".
# 2  Chasm (V) — short scrawl; Aim High is line 14.
# 5  Only Jedi Carry That Weapon — abbreviated "Only Jedi Carry"; (V) empty.
# 11 Another Pathetic Lifeform — long title; (V) empty (Affect Mind on 12 is checked).
