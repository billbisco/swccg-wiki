#!/usr/bin/env python3
"""2014 European Championship hub (Legacy Open main event).

No published Xerox/HTML lists were found for the main event. Champion is
Casper Jørgensen on the Players Committee major-event-winners page. The
Reset Beta side event is a separate Open hub.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2015_2016 as g15  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC_IDX = PAGES / "European_Championships.wiki"
TSV = ROOT / "y2014-ec-titles.tsv"

EVENT = "2014 European Championship"
DATES = "12–14 September 2014"
FORMAT = "[[Legacy Open]]"
PC_WIN = "https://www.starwarsccg.org/major-event-winners/"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WINNER = "Casper Jørgensen"


def write(title: str, text: str) -> str:
    fn = wiki_fname(title)
    if not fn.endswith(".wiki"):
        fn += ".wiki"
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return f"pages/{fn}"


def write_hub() -> None:
    body = f"""'''2014 European Championship''' was a Players Committee constructed major, 12–14 September 2014, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="winners">{PC_WIN}</ref> [[Casper Jørgensen]] is the published European Champion. No decklist PDF or typed HTML wrap for the main event is on the Players Committee tournament-decklists desk; the published lists from that weekend are the post-reset [[2014 European Championship Reset Beta]] side event.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' [[{WINNER}]]

== Published lists ==

No main-event lists are published. The Reset Beta side event lists are on [[2014 European Championship Reset Beta]].

== See also ==

* [[2014 European Championship Reset Beta]]
* [[European Championships]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_WIN} Major Event Winners], starwarsccg.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2014]]
"""
    write(EVENT, body)


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    row = (
        f"| 2014-09-12 || [[2014 European Championship|European Championship]] "
        f"|| 12–14 September 2014 || — || [[Legacy Open]] || [[{WINNER}]]"
    )
    if "[[2014 European Championship|European Championship]]" in text:
        return
    needle = (
        "| 2014-09-12 || [[2014 European Championship Reset Beta|European Championship Reset Beta]] "
        "|| 12–14 September 2014 || — || [[Open]] || [[Cedrik Vanderhaegen]]"
    )
    if needle in text:
        text = text.replace(needle, needle + "\n|- \n" + row, 1)
        LIST.write_text(text, encoding="utf-8", newline="\n")


def patch_ec_index() -> None:
    text = EC_IDX.read_text(encoding="utf-8")
    old = "| 2014 || 2014 European Championship || — || [[Legacy Open]] || [[Casper Jørgensen]]"
    new = "| 2014 || [[2014 European Championship]] || — || [[Legacy Open]] || [[Casper Jørgensen]]"
    if old in text:
        EC_IDX.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def patch_winners() -> list[tuple[str, str]]:
    """Fill published champions on 2014 Nats / MPC / TMW hubs and the List."""
    out: list[tuple[str, str]] = []
    jobs = [
        (
            PAGES / "2014_US_Nationals.wiki",
            "The PDFs do not name a champion.",
            "[[Matthew Harrison-Trainor]] is the published US National Champion.<ref name=\"winners\">https://www.starwarsccg.org/major-event-winners/</ref>",
            "* '''Winner:''' —",
            "* '''Winner:''' [[Matthew Harrison-Trainor]]",
        ),
        (
            PAGES / "2014_Match_Play_Championship.wiki",
            "The Holotable zip does not name a champion.",
            "[[Kevin Shannon]] is the published Match Play Champion.<ref name=\"winners\">https://www.starwarsccg.org/major-event-winners/</ref>",
            "* '''Winner:''' —",
            "* '''Winner:''' [[Kevin Shannon]]",
        ),
        (
            PAGES / "2014_Texas_Mini_Worlds.wiki",
            "The PDFs do not name a champion.",
            "[[Greg Shaw]] is the published Texas Mini Worlds champion.<ref name=\"winners\">https://www.starwarsccg.org/major-event-winners/</ref>",
            "* '''Winner:''' —",
            "* '''Winner:''' [[Greg Shaw]]",
        ),
    ]
    for path, old_lead, new_lead, old_w, new_w in jobs:
        text = path.read_text(encoding="utf-8")
        text = text.replace(old_lead, new_lead, 1)
        text = text.replace(old_w, new_w, 1)
        if "major-event-winners" not in text:
            text = text.replace(
                "* [https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org",
                "* [https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org\n"
                "* [https://www.starwarsccg.org/major-event-winners/ Major Event Winners], starwarsccg.org",
                1,
            )
        path.write_text(text, encoding="utf-8", newline="\n")
        title = path.stem.replace("_", " ")
        if title.startswith("2014 Match"):
            title = "2014 Match Play Championship"
        out.append((title, f"pages/{path.name}"))

    text = LIST.read_text(encoding="utf-8")
    repls = [
        (
            "| 2014-06-13 || [[2014 US Nationals|US Nationals]] || 13–15 June 2014 || — || [[Legacy Open]] || —",
            "| 2014-06-13 || [[2014 US Nationals|US Nationals]] || 13–15 June 2014 || — || [[Legacy Open]] || [[Matthew Harrison-Trainor]]",
        ),
        (
            "| 2014-05-02 || [[2014 Texas Mini Worlds|Texas Mini Worlds]] || 2–4 May 2014 || Texas || [[Legacy Open]] || —",
            "| 2014-05-02 || [[2014 Texas Mini Worlds|Texas Mini Worlds]] || 2–4 May 2014 || Texas || [[Legacy Open]] || [[Greg Shaw]]",
        ),
        (
            "| 2014-01-24 || [[2014 Match Play Championship|Match Play Championship]] || 24–26 January 2014 || — || [[Legacy Open]] || —",
            "| 2014-01-24 || [[2014 Match Play Championship|Match Play Championship]] || 24–26 January 2014 || — || [[Legacy Open]] || [[Kevin Shannon]]",
        ),
    ]
    for a, b in repls:
        text = text.replace(a, b, 1)
    LIST.write_text(text, encoding="utf-8", newline="\n")
    return out


def main() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    titles: list[tuple[str, str]] = []
    write_hub()
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_WIN,
        "format": FORMAT,
    }
    row = (
        f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
        f"|| 1 || — || —"
    )
    got = g15.upsert_player(WINNER, [row], meta)
    if got:
        titles.append(got)
        for cand in (
            PAGES / wiki_fname(WINNER),
            STUBS / (WINNER.replace(" ", "_") + ".wiki"),
        ):
            if cand.exists():
                tidy_player_page(cand)

    # Patch finish / add champion rows on the full stubs (do not touch
    # stale pages/Greg_Shaw.wiki or pages/Matthew_Harrison-Trainor.wiki).
    mht = PAGES / "player-stubs" / "Matthew_Harrison-Trainor.wiki"
    if mht.exists():
        t = mht.read_text(encoding="utf-8")
        t = t.replace(
            "| 13–15 June 2014 || [[2014 US Nationals]] (Day 2) || [[Legacy Open]] || — ||",
            "| 13–15 June 2014 || [[2014 US Nationals]] (Day 2) || [[Legacy Open]] || 1 ||",
            1,
        )
        mht.write_text(t, encoding="utf-8", newline="\n")
        titles.append(("Matthew Harrison-Trainor", "pages/player-stubs/Matthew_Harrison-Trainor.wiki"))

    ks = PAGES / "Kevin_Shannon.wiki"
    if ks.exists():
        t = ks.read_text(encoding="utf-8")
        t = t.replace(
            "| 24–26 January 2014 || [[2014 Match Play Championship]] (Holotable) || [[Legacy Open]] || — ||",
            "| 24–26 January 2014 || [[2014 Match Play Championship]] (Holotable) || [[Legacy Open]] || 1 ||",
            1,
        )
        ks.write_text(t, encoding="utf-8", newline="\n")
        titles.append(("Kevin Shannon", "pages/Kevin_Shannon.wiki"))

    gs = PAGES / "player-stubs" / "Greg_Shaw.wiki"
    if gs.exists():
        t = gs.read_text(encoding="utf-8")
        needle = (
            "| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || "
            "[[Legacy Open]] || — || [[2014 Worlds Day 2 Greg Shaw DS Hunt Down|"
            "Hunt Down And Destroy The Jedi (V)]] || [[2014 Worlds Day 2 Greg Shaw LS Yavin 4|"
            "Yavin 4: Massassi Throne Room]]\n|- \n"
        )
        insert = (
            needle
            + "| 2–4 May 2014 || [[2014 Texas Mini Worlds]] || [[Legacy Open]] "
            "|| 1 || — || —\n|- \n"
        )
        if "[[2014 Texas Mini Worlds]]" not in t and needle in t:
            t = t.replace(needle, insert, 1)
            gs.write_text(t, encoding="utf-8", newline="\n")
        titles.append(("Greg Shaw", "pages/player-stubs/Greg_Shaw.wiki"))

    titles.extend(patch_winners())
    patch_list()
    patch_ec_index()
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("European Championships", "pages/European_Championships.wiki"))

    seen = {}
    ordered = []
    for title, rel in titles:
        if title in seen:
            ordered[seen[title]] = (title, rel)
        else:
            seen[title] = len(ordered)
            ordered.append((title, rel))
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ordered), encoding="utf-8", newline="\n"
    )
    print("tsv", TSV, "n", len(ordered))
    for t, r in ordered:
        print(" ", t, r)


if __name__ == "__main__":
    main()
