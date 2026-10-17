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
TAT_RELEASE = "2001-05-30"  # 16248 (27 May 2001): Tatooine due out "Wednesday" = 30 May
_set = {}

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
        if d.get("format") != "Premiere - Tatooine" or d["date"] >= TAT_RELEASE:
            continue
        tat = [r[1] for r in d["cards"] if r[2] != "UNKNOWN" and card_set(r[1]).startswith("Tatooine")]
        if tat:
            print(pid, d["date"], "keeps Premiere - Tatooine (Tatooine cards:", ", ".join(tat[:3]) + ")")
            continue
        print(pid, d["date"], "-> Premiere - Reflections II")
        if apply:
            d["format"] = "Premiere - Reflections II"
            ind = 1 if raw.startswith('{\n "') else 2
            p.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main(sys.argv[1:])
