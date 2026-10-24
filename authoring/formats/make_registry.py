#!/usr/bin/env python3
"""Source of truth for wiki formats (Bill 2026-10-24). Edit this file, then run it to write registry.json.
type: constructed | closed | sealed | draft | cube | casual
family: decipher-pool | decipher-special | pc-championship | pc-alternate | gemp | wiki
years: when the format was played or defined (text). gemp_pc / gemp_ours: the GEMP display name on each site (None = absent).
"""
import json
from pathlib import Path

def F(title, type_, family, pool, years, decipher=False, pc=False, code=None, gemp_pc=None, gemp_ours=None, also=(), note=""):
    return dict(title=title, type=type_, family=family, pool=pool, years=years, decipher=decipher, pc=pc,
                code=code, gemp_pc=gemp_pc, gemp_ours=gemp_ours, also=list(also), note=note)

G = lambda name: (name, name)  # same GEMP name on both sites
R = []
# --- Decipher era: the legal constructed pool after each set (wiki names; Decipher just said "all sets legal")
for t, pool, yrs, code, gname in [
    ("Premiere (format)", "Premiere (with the Jedi Pack, Rebel Leader cards and Introductory Two-Player Game)", "Dec 1995 – Jul 1996", "premiere", "Premiere"),
    ("Premiere - A New Hope", "Premiere through A New Hope", "Jul – Nov 1996", "premiere_anh", "Premiere - A New Hope"),
    ("Premiere - Hoth", "Premiere through Hoth", "Nov 1996 – Apr 1997", "premiere_hoth", "Premiere - Hoth"),
    ("Premiere - Dagobah", "Premiere through Dagobah (and First Anthology)", "Apr – Nov 1997", "premiere_dagobah", "Premiere - Dagobah"),
    ("Premiere - Cloud City", "Premiere through Cloud City", "Nov 1997 – Apr 1998", "premiere_cc", "Premiere - Cloud City"),
    ("Premiere - Jabba's Palace", "Premiere through Jabba's Palace (and Official Tournament Sealed Deck)", "Apr – Nov 1998", "premiere_jp", "Premiere - Jabba's Palace"),
    ("Premiere - Special Edition", "Premiere through Special Edition (and Enhanced Premiere)", "Nov 1998 – Jun 1999", "premiere_se", "Premiere - Special Edition"),
    ("Premiere - Endor", "Premiere through Endor (and Enhanced Cloud City / Jabba's Palace, Reflections, Third Anthology)", "Jun 1999 – Jul 2000", "premiere_endor", "Premiere - Endor"),
    ("Premiere - Death Star II", "Premiere through Death Star II", "Jul – Oct 2000", "premiere_ds2", "Premiere - Death Star II"),
    ("Premiere - Jabba's Palace Sealed Deck", "Premiere through the Jabba's Palace Sealed Deck product", "Oct 2000 – Jan 2001", "premiere_jpsd", "Premiere - JPSD"),
    ("Premiere - Reflections II", "Premiere through Reflections II", "Jan – May 2001", "premiere_ref2", "Premiere - Reflections II"),
    ("Premiere - Tatooine", "Premiere through Tatooine", "May – Aug 2001", "premiere_tatooine", "Premiere - Tatooine"),
    ("Premiere - Coruscant", "Premiere through Coruscant", "Aug – Oct 2001", None, None),
    ("Premiere - Reflections III", "Premiere through Reflections III (first Defensive Shields)", "Oct – Dec 2001", None, None),
    ("Premiere - Theed Palace", "every Decipher-printed card", "Dec 2001 – Mar 2002", "open_no_virtual", "Decipher Cards Only"),
]:
    R.append(F(t, "constructed", "decipher-pool", pool, yrs, decipher=True, pc=bool(gname), code=code, gemp_pc=gname, gemp_ours=gname))
# --- Decipher special formats (fixed definitions; Decipher's own names)
R += [
    F("Death Star II Closed Environment", "closed", "decipher-special", "Endor and Death Star II cards plus the Death Star II Starter Deck reprints", "2000", decipher=True, pc=True, also=["Battle of Endor Environment (Players Committee)"]),
    F("Episode I Closed Environment", "closed", "decipher-special", "only cards with the Episode I icon", "2001 – 2002", decipher=True, pc=True, also=["Type II (players)", "Episode I Only Environment"]),
    F("First Anthology Sealed", "sealed", "decipher-special", "one First Anthology box per player", "1997", decipher=True),
]
# --- Players Committee championship constructed
for n, d in [(1, "9 March 2002"), (2, "1 June 2002"), (3, "20 September 2002"), (4, "5 February 2003"), (5, "June 2003"), (6, "12 January 2004"),
             (7, "4 December 2006"), (8, "4 December 2006"), (13, "6 August 2007"), (16, "15 August 2008"), (17, "6 February 2009")]:
    R.append(F(f"Premiere - Original VS{n}", "constructed", "pc-championship", f"every Decipher card plus original Virtual Sets 1–{n}" if n > 1 else "every Decipher card plus original Virtual Set 1",
               f"from {d}", pc=True, also=[f"POVS{n}"] + (["Original Virtual Open"] if n == 17 else [])))
R += [
    F("Legacy Open", "constructed", "pc-championship", "Decipher cards plus the pre-2014 Virtual Block cards", "2009 – 2014", pc=True, code="legacy", gemp_pc="Legacy", gemp_ours="Legacy", also=["Legacy"]),
    F("Open", "constructed", "pc-championship", "Decipher cards plus current Virtual Sets and Defensive Shields", "2014 –", pc=True, code="open", gemp_pc="Open", gemp_ours="Open", also=["Standard (Players Committee, from 2014)"]),
    F("Open (40 cards)", "constructed", "pc-alternate", "the Open pool, 40-card decks", "", pc=True, code="open40card", gemp_pc="Open (40 cards)", gemp_ours="Open (40 cards)"),
    F("Open (45 cards)", "constructed", "pc-alternate", "the Open pool, 45-card decks", "", pc=True, code="open_45_card", gemp_pc="Open (45 cards)", gemp_ours="Open (45 cards)"),
    F("Open (100 cards)", "constructed", "pc-alternate", "the Open pool, 100-card decks", "", pc=True, code="open_100_card", gemp_pc="Open (100 cards)", gemp_ours="Open (100 cards)", also=["100 Card Deck Format"]),
    F("Open (no shields)", "constructed", "pc-alternate", "the Open pool without Defensive Shields", "", pc=True, code="open_no_shields", gemp_pc="Open (no shields)", gemp_ours="Open (no shields)"),
    F("Open (no shields / no v-cards)", "constructed", "pc-alternate", "Decipher cards only, no Defensive Shields", "", pc=True, code="open_no_shields_no_virtual", gemp_pc="Open (no shields / no v-cards)", gemp_ours="Open (no shields / no v-cards)"),
    F("Open (no Episode VII)", "constructed", "pc-alternate", "the Open pool without Episode VII icon cards", "", pc=True, code="open_no_episodevii", gemp_pc="Open (no Episode VII)", gemp_ours="Open (no Episode VII)"),
    F("Classic", "constructed", "pc-alternate", "Decipher and current virtual cards, without Defensive Shield, Episode I or Maintenance icon cards", "", pc=True, code="classic", gemp_pc="Classic", gemp_ours="Classic"),
    F("Classic (no v-cards)", "constructed", "pc-alternate", "Classic with Decipher cards only", "", pc=True, code="classic_no_virtual", gemp_pc="Classic (no v-cards)", gemp_ours="Classic (no v-cards)", also=["Classic No-V"]),
    F("Classic (no v-cards) (Modified)", "constructed", "pc-alternate", "Classic (no v-cards) with 14 Defensive Shields allowed", "", pc=True, code="classic_no_virtual_m", gemp_pc="Classic (no v-cards) (Modified)", gemp_ours="Classic (no v-cards) (Modified)"),
    F("Premiere - Cloud City (Modified)", "constructed", "pc-alternate", "Premiere through Cloud City with a ban list", "", pc=True, code="premiere_cc_m", gemp_pc="Premiere - Cloud City (Modified)", gemp_ours="Premiere - Cloud City (Modified)"),
    F("Premiere - Reflections II (Modified)", "constructed", "pc-alternate", "Premiere through Reflections II with a ban list", "", pc=True, code="premiere_ref2_m", gemp_pc="Premiere - Reflections II (Modified)", gemp_ours="Premiere - Reflections II (Modified)"),
    F("Decipher Cards Only (Modified)", "constructed", "pc-alternate", "every Decipher card with a ban list", "", pc=True, code="open_no_virtual_m", gemp_pc="Decipher Cards Only (Modified)", gemp_ours="Decipher Cards Only (Modified)"),
    F("Premiere - Virtual Set 3", "constructed", "pc-alternate", "every Decipher card plus current Virtual Sets 0–3", "", pc=True, code="premiere_set3", gemp_pc="Premiere - Virtual Set 3", gemp_ours="Premiere - Virtual Set 3"),
    F("Jawa Format", "constructed", "pc-alternate", "a ban list that removes the top of the power curve", "2019 –", pc=True, code="jawa", gemp_pc="Jawa", gemp_ours="Jawa"),
    F("Scavenger Format", "constructed", "pc-alternate", "Decipher cards of common rarities only (Premiere – Death Star II)", "", pc=True, code="scavenger_premiere_ds2", gemp_pc="Scavenger", gemp_ours="Scavenger"),
    F("Utinni! (Jawas Only)", "constructed", "pc-alternate", "characters restricted to Jawas", "", pc=True, code="utinni", gemp_pc="Utinni! (Jawas Only)", gemp_ours="Utinni! (Jawas Only)"),
    F("Limited Resources Format", "constructed", "pc-alternate", "Decipher cards minus the most abusive, plus some virtual cards", "", pc=True, code="limited_resources", gemp_pc="Limited Resources", gemp_ours="Limited Resources"),
    F("Sealed", "sealed", "pc-alternate", "GEMP sealed league product, 40-card decks", "", pc=True, code="sealed", gemp_pc="Sealed", gemp_ours="Sealed"),
    F("Cube", "cube", "pc-alternate", "Watto's Chance Cube pool (45-card decks on the PC; 40 on play.swccg.com)", "", pc=True, code="cube", gemp_pc="Cube", gemp_ours="Cube", also=["Watto's Chance Cube"]),
    F("Playtesting", "casual", "gemp", "the Open pool plus the Playtesting set", "", pc=True, code="playtesting", gemp_pc="Playtesting", gemp_ours="Playtesting"),
    F("Dream Cards", "casual", "gemp", "the Open pool plus the Dream Cards set", "", pc=True, code="dream_cards", gemp_pc="Dream Cards", gemp_ours="Dream Cards"),
]
# --- formats only on play.swccg.com
for t, ty, pool, code, gname in [
    ("Anything Goes", "casual", "every set, 40–60 cards (default casual and AI format)", "anything_goes", "Anything Goes"),
    ("Ewok Format", "constructed", "Premiere – Death Star II with a long ban list (PC forum: Premiere - Death Star II (Ewok))", "ewok", "Ewok"),
    ("Premiere - A New Hope Sealed", "sealed", "Premiere and A New Hope product", "premiere_anh_sealed", "Premiere - A New Hope Sealed"),
    ("Endor - Death Star II Sealed", "sealed", "Endor and Death Star II product", "endor_dsII_sealed", "Endor - Death Star II Sealed"),
    ("Reflections Sealed", "sealed", "Reflections product", "reflections_sealed", "Reflections Sealed"),
    ("Episode I Sealed", "sealed", "Episode I product", "episode_i_sealed", "Episode I Sealed"),
    ("All Of The Jedi Sealed", "sealed", "All Of The Jedi product", "all_of_the_jedi_sealed", "All Of The Jedi Sealed"),
    ("Novelty - Space Sealed", "sealed", "space-only novelty product", "novelty_sealed", "Novelty - Space Sealed"),
    ("Premiere - Death Star II Draft", "draft", "Premiere – Death Star II booster draft", "basic_premds2_draft", "Premiere - Death Star II Draft"),
    ("Premiere - Virtual Set 13 Draft", "draft", "Premiere – Virtual Set 13 booster draft", "basic_premv13_draft", "Premiere - Virtual Set 13 Draft"),
    ("Premiere - Virtual Set 25 Draft", "draft", "Premiere – Virtual Set 25 booster draft", "holocron_premv25_draft", "Premiere - Virtual Set 25 Draft"),
    ("Cube v7 + Objectives Draft", "draft", "Cube v7 with objective packs", "c7obj_draft", "Cube v7 + Objectives Draft"),
    ("Watto's Cube with objective packs Cube", "cube", "Watto's Cube with objective packs", "wattos_cube_with_objective", "Watto's Cube with objective packs Cube"),
    ("Watto's Cube with fixed pack Cube", "cube", "Watto's Cube with a fixed pack", "wattos_cube_with_fixed", "Watto's Cube with fixed pack Cube"),
]:
    R.append(F(t, ty, "gemp", pool, "", code=code, gemp_ours=gname))
# --- pools this wiki named for a single event
R.append(F("Premiere to Virtual Set 3", "constructed", "wiki", "Decipher cards plus Virtual Sets through Virtual Set 3, as used by the 2025 Online Retro Event for Charity", "2025", pc=True))
# drafted pages (formats/drafts/registry_final.jsonl) and field corrections (registry_suggestions.jsonl)
D = Path(__file__).with_name("drafts")
have = {r["title"] for r in R}
for l in open(D / "registry_final.jsonl", encoding="utf-8"):
    x = json.loads(l)
    if x["title"] not in have:
        R.append(F(x["title"], x["type"], x["family"], x["pool"], x.get("years", ""), x.get("decipher", False), x.get("pc", False),
                   x.get("code"), x.get("gemp_pc"), x.get("gemp_ours"), x.get("also", []), x.get("note", "")))
by = {r["title"]: r for r in R}
for l in open(D / "registry_suggestions.jsonl", encoding="utf-8"):
    x = json.loads(l)
    if x["title"] in by:
        by[x["title"]].update({k: v for k, v in x.items() if k != "title"})
Path(__file__).with_name("registry.json").write_text(json.dumps(R, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(R), "formats")
