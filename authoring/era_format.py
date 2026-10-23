"""Pick the period format for a DeckTech deck from its post date and the sets of its cards (2026-10-17).

  python3 era_format.py [--apply] ID...

Tatooine was released Wednesday 30 May 2001; Coruscant about early Aug 2001. A deck posted before Tatooine's release
whose list has no Tatooine-set card is "Premiere - Reflections II"; with a Tatooine card (pre-release lists) it stays
"Premiere - Tatooine". Episode I Closed Environment and Coruscant/later formats are left alone.
"""
import json, re, sys
from pathlib import Path
import regen_gemp_from_wiki as R

DECKS = Path(__file__).resolve().parent / "decktech-decks"
TAT_RELEASE = "2001-05-30"
REF3_RELEASE = "2001-10-31"  # Reflections III: first Defensive Shields  # 16248 (27 May 2001): Tatooine due out "Wednesday" = 30 May
_set = {}
# (release of the later set, format before it, card-set prefix of the later set), newest first
ERAS = [("2001-01-10", "Premiere - Death Star II", "Reflections II"),
        ("2000-07-19", "Premiere - Endor", "Death Star II"),
        ("1999-06-01", "Premiere - Special Edition", "Endor")]

def card_set(title):
    if title in _set:
        return _set[title]
    x = R.page_texts([title]).get(title) or ""
    m = re.match(r"#REDIRECT\s*\[\[([^\]|#]+)", x, re.I)
    if m:
        x = R.page_texts([m.group(1).strip()]).get(m.group(1).strip()) or ""
    s = re.search(r"^\|set=([^\n|]+)", x, re.M)
    _set[title] = s.group(1).strip() if s else ""
    return _set[title]

def main(argv):
    apply = "--apply" in argv
    for pid in [a for a in argv if a.isdigit()]:
        p = DECKS / f"{pid}.json"
        raw = p.read_text(encoding="utf-8"); d = json.loads(raw)
        # Defensive Shields start with Reflections III (31 Oct 2001): before that, a shield-typed row is the older
        # Effect of the same title (Secret Plans, Wise Advice, Oppressive Enforcement, ...). Claude 2026-10-22.
        if d["date"] < REF3_RELEASE and any(r[2] == "DEFENSIVE_SHIELD" for r in d["cards"]):
            fixed = [r[1] for r in d["cards"] if r[2] == "DEFENSIVE_SHIELD"]
            print(pid, d["date"], "shield rows -> EFFECT:", ", ".join(fixed))
            if apply:
                for r in d["cards"]:
                    if r[2] == "DEFENSIVE_SHIELD":
                        r[2] = "EFFECT"
                p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        # the drafter's default is "Premiere - Original VS1" (a 2002 pool); pre-Tatooine posts are re-dated here too
        if d.get("format") not in ("Premiere - Tatooine", "Premiere - Original VS1", "Premiere - Reflections II", "Premiere - Death Star II", "Premiere - Endor") or d["date"] >= TAT_RELEASE:
            continue
        tat = [r[1] for r in d["cards"] if r[2] != "UNKNOWN" and card_set(r[1]).startswith("Tatooine")]
        if tat:
            print(pid, d["date"], "-> Premiere - Tatooine (Tatooine cards:", ", ".join(tat[:3]) + ")")
            if apply and d["format"] != "Premiere - Tatooine":
                d["format"] = "Premiere - Tatooine"
                ind = 1 if raw.startswith('{\n "') else 2
                p.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")
            continue
        fmt = "Premiere - Reflections II"
        # Earlier pools by post date (Bill 2026-10-22): Reflections II came out 10 Jan 2001, Death Star II 19 Jul 2000.
        # A list holding a card from the next set (pre-release lists) moves up to that set's format.
        for rel, prev, nxt in ERAS:
            if d["date"] >= rel:
                break
            late = [r[1] for r in d["cards"] if r[2] != "UNKNOWN" and card_set(r[1]).startswith(nxt)]
            if late:
                break
            fmt = prev
        print(pid, d["date"], "->", fmt)
        if apply and d["format"] != fmt:
            d["format"] = fmt
            ind = 1 if raw.startswith('{\n "') else 2
            p.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
