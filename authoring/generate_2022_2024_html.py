#!/usr/bin/env python3
"""HTML-only 2022–2024 decks + hub tables + player stubs."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2026_euro as ge  # noqa: E402
import generate_html_missing as hm  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402
from generate_2026_remaining import upsert_stub  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
DECKS = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024-decks")
URL_FILE = ROOT / "encyclopedia" / "y2022-2024-html-deck-urls.txt"
TSV = ROOT / "y2022-2024-html-titles.tsv"

PREFIXES = [
    ("2024-ocs-playoff-finals-", "2024 Online Championship Series Playoffs", "Finals", True, "2024"),
    ("2024-ocs-playoff-semifinals-", "2024 Online Championship Series Playoffs", "Semifinals", True, "2024"),
    ("2024-ocs-playoff-quarterfinals-", "2024 Online Championship Series Playoffs", "Quarterfinals", True, "2024"),
    ("2024-ocs-playoff-top-16-", "2024 Online Championship Series Playoffs", "Top 16", True, "2024"),
    ("2024-retro-online-championship-series-finals-", "2024 Retro Online Championship Series Playoffs", "Finals", True, "2024"),
    ("2024-retro-online-championship-series-semi-finals-", "2024 Retro Online Championship Series Playoffs", "Semifinals", True, "2024"),
    ("2024-retro-online-championship-series-semifinals-", "2024 Retro Online Championship Series Playoffs", "Semifinals", True, "2024"),
    ("2024-retro-online-championship-series-quarterfinals-", "2024 Retro Online Championship Series Playoffs", "Quarterfinals", True, "2024"),
    ("2024-retro-online-championship-series-quarter-finals-", "2024 Retro Online Championship Series Playoffs", "Quarterfinals", True, "2024"),
    ("2024-retro-online-championship-series-", "2024 Retro Online Championship Series Playoffs", "constructed", False, "2024"),
    ("2024-champions-league-finals-", "2024 Champions League", "Finals", True, "2024"),
    ("2024-champions-league-semi-finals-", "2024 Champions League", "Semifinals", True, "2024"),
    ("2024-champions-league-semifinals-", "2024 Champions League", "Semifinals", True, "2024"),
    ("2024-champions-league-quarterfinals-", "2024 Champions League", "Quarterfinals", True, "2024"),
    ("2024-champions-league-quarter-finals-", "2024 Champions League", "Quarterfinals", True, "2024"),
    ("2024-champions-league-", "2024 Champions League", "constructed", False, "2024"),
    ("2024-european-championship-top-8-", "2024 European Championship", "Top 8", True, "2024"),
    ("2024-european-championship-top-4-", "2024 European Championship", "Top 4", True, "2024"),
    ("2024-european-championships-", "2024 European Championship", "Day 1", False, "2024"),
    ("2024-european-championship-", "2024 European Championship", "Day 1", False, "2024"),
    ("2024-ec-", "2024 European Championship", "Day 1", False, "2024"),
    ("2024-jawa-cup-top-8-", "2024 Jawa Cup", "Top 8", True, "2024"),
    ("2024-jawa-cup-finals-", "2024 Jawa Cup", "Finals", True, "2024"),
    ("2024-jawa-cup-", "2024 Jawa Cup", "Swiss", False, "2024"),
    ("8th-annual-gempc-finals-", "2024 Eighth Annual GEMPC", "Finals", True, "2024"),
    ("8th-annual-gempc-top-8-", "2024 Eighth Annual GEMPC", "Top 8", True, "2024"),
    ("8th-annual-gempc-", "2024 Eighth Annual GEMPC", "constructed", False, "2024"),
    ("2024-8th-annual-gempc-", "2024 Eighth Annual GEMPC", "constructed", False, "2024"),
    ("2024-gempc-finals-", "2024 Eighth Annual GEMPC", "Finals", True, "2024"),
    ("2024-gempc-semi-finals-", "2024 Eighth Annual GEMPC", "Semifinals", True, "2024"),
    ("2024-gempc-semifinals-", "2024 Eighth Annual GEMPC", "Semifinals", True, "2024"),
    ("2024-gempc-quarterfinals-", "2024 Eighth Annual GEMPC", "Quarterfinals", True, "2024"),
    ("2024-gempc-quarter-finals-", "2024 Eighth Annual GEMPC", "Quarterfinals", True, "2024"),
    ("2024-gempc-", "2024 Eighth Annual GEMPC", "constructed", False, "2024"),
    ("2023-european-championship-top-8-", "2023 European Championship", "Top 8", True, "2023"),
    ("2023-european-championships-", "2023 European Championship", "Day 1", False, "2023"),
    ("2023-european-championship-", "2023 European Championship", "Day 1", False, "2023"),
    ("champions-league-finals-", "2023 Champions League", "Finals", True, "2023"),
    ("champions-league-semi-finals-", "2023 Champions League", "Semifinals", True, "2023"),
    ("champions-league-semifinals-", "2023 Champions League", "Semifinals", True, "2023"),
    ("champions-league-quarter-finals-", "2023 Champions League", "Quarterfinals", True, "2023"),
    ("champions-league-quarterfinals-", "2023 Champions League", "Quarterfinals", True, "2023"),
    ("2023-champions-league-", "2023 Champions League", "constructed", False, "2023"),
    ("2023-san-diego-super-open-day-2-", "2023 San Diego Super Open", "Day 2", True, "2023"),
    ("2023-san-diego-super-open-day-1-", "2023 San Diego Super Open", "Day 1", False, "2023"),
    ("2023-san-diego-super-open-", "2023 San Diego Super Open", "Day 1", False, "2023"),
    ("san-diego-super-open-day-2-", "2023 San Diego Super Open", "Day 2", True, "2023"),
    ("san-diego-super-open-day-1-", "2023 San Diego Super Open", "Day 1", False, "2023"),
    ("san-diego-super-open-", "2023 San Diego Super Open", "Day 1", False, "2023"),
    ("2022-ocs-playoff-finals-", "2022 Online Championship Series Playoffs", "Finals", True, "2022"),
    ("2022-ocs-playoffs-finals-", "2022 Online Championship Series Playoffs", "Finals", True, "2022"),
    ("2022-ocs-playoff-semi-finals-", "2022 Online Championship Series Playoffs", "Semifinals", True, "2022"),
    ("2022-ocs-playoff-semifinals-", "2022 Online Championship Series Playoffs", "Semifinals", True, "2022"),
    ("2022-ocs-playoff-quarter-finals-", "2022 Online Championship Series Playoffs", "Quarterfinals", True, "2022"),
    ("2022-ocs-playoff-quarterfinals-", "2022 Online Championship Series Playoffs", "Quarterfinals", True, "2022"),
    ("2022-ocs-playoff-top-16-", "2022 Online Championship Series Playoffs", "Top 16", True, "2022"),
    ("2022-ocs-top-16-", "2022 Online Championship Series Playoffs", "Top 16", True, "2022"),
    ("2022-ocs-playoff-", "2022 Online Championship Series Playoffs", "constructed", False, "2022"),
    ("2022-ocs-playoffs-", "2022 Online Championship Series Playoffs", "constructed", False, "2022"),
    ("2022-ocs-", "2022 Online Championship Series Playoffs", "constructed", False, "2022"),
    ("2022-european-championship-top-8-", "2022 European Championship", "Top 8", True, "2022"),
    ("2022-european-championships-", "2022 European Championship", "Day 1", False, "2022"),
    ("2022-european-championship-", "2022 European Championship", "Day 1", False, "2022"),
    ("2022-ec-", "2022 European Championship", "Day 1", False, "2022"),
    ("2022-retro-event-dco-top-4-", "2022 Decipher Cards Only Retro Event", "Top 4", True, "2022"),
    ("2022-retro-event-dco-", "2022 Decipher Cards Only Retro Event", "constructed", False, "2022"),
    ("2022-jawa-cup-final-confrontation-", "2022 Jawa Cup", "Finals", True, "2022"),
    ("2022-jawa-cup-top-4-", "2022 Jawa Cup", "Top 4", True, "2022"),
    ("2022-jawa-cup-top-8-", "2022 Jawa Cup", "Top 8", True, "2022"),
    ("2022-jawa-cup-", "2022 Jawa Cup", "constructed", False, "2022"),
    ("2021-jawa-cup-top-8-", "2022 Jawa Cup", "Top 8", True, "2022"),
]

SHORT = {
    "2024 Online Championship Series Playoffs": "2024 OCS",
    "2024 Retro Online Championship Series Playoffs": "2024 ROCS",
    "2024 Champions League": "2024 Champions League",
    "2024 European Championship": "2024 European Championship",
    "2024 Jawa Cup": "2024 Jawa Cup",
    "2024 Eighth Annual GEMPC": "2024 GEMPC",
    "2024 Regional Championships": "2024 Regionals",
    "2023 European Championship": "2023 European Championship",
    "2023 Champions League": "2023 Champions League",
    "2023 San Diego Super Open": "2023 SDSO",
    "2023 Regional Championships": "2023 Regionals",
    "2022 Online Championship Series Playoffs": "2022 OCS",
    "2022 European Championship": "2022 European Championship",
    "2022 Regional Championships": "2022 Regionals",
    "2022 Jawa Cup": "2022 Jawa Cup",
    "2022 Decipher Cards Only Retro Event": "2022 Retro DCO",
}

PC_URL = {
    "2024 Online Championship Series Playoffs": "https://www.starwarsccg.org/2024-10-online-championship-series-ocs-playoffs-oct-nov-2024/",
    "2024 Retro Online Championship Series Playoffs": "https://www.starwarsccg.org/2024-11-retro-online-championship-series-rocs-playoffs-dec-2024/",
    "2024 Champions League": "https://www.starwarsccg.org/2024-12-champions-league-dec-2024-feb-2025/",
    "2024 European Championship": "https://www.starwarsccg.org/2024-06-european-championships-copenhagen-denmark-may-17th-2024/",
    "2024 Jawa Cup": "https://www.starwarsccg.org/2024-03-jawa-cup-top-8-feb-13-25-on-gemp/",
    "2024 Eighth Annual GEMPC": "https://www.starwarsccg.org/8th-annual-gempc-feb-may-2024/",
    "2024 Regional Championships": "https://www.starwarsccg.org/2024-02-regional-championships/",
    "2023 European Championship": "https://www.starwarsccg.org/2023-08-european-championships-bochum-germany-sept-8-10/",
    "2023 Champions League": "https://www.starwarsccg.org/2023-1-champions-league-knockout-round/",
    "2023 San Diego Super Open": "https://www.starwarsccg.org/2023-02-san-diego-super-open/",
    "2023 Regional Championships": "https://www.starwarsccg.org/2023-03-2023-regional-championship-events/",
    "2022 Online Championship Series Playoffs": "https://www.starwarsccg.org/2022-ocs-playoffs/",
    "2022 European Championship": "https://www.starwarsccg.org/2022-09-european-championship/",
    "2022 Regional Championships": "https://www.starwarsccg.org/2022-06-2022-regional-championship-events/",
    "2022 Jawa Cup": "https://www.starwarsccg.org/2021-jawa-cup-top-8/",
}

STAGE_ORDER = {
    "2024 Online Championship Series Playoffs": ("Finals", "Semifinals", "Quarterfinals", "Top 16"),
    "2024 Retro Online Championship Series Playoffs": ("Finals", "Semifinals", "Quarterfinals", "constructed"),
    "2024 Champions League": ("Finals", "Semifinals", "Quarterfinals", "constructed"),
    "2024 Jawa Cup": ("Finals", "Top 8", "Swiss"),
    "2024 Eighth Annual GEMPC": ("Finals", "Semifinals", "Quarterfinals", "Top 8", "constructed"),
    "2023 Champions League": ("Finals", "Semifinals", "Quarterfinals", "constructed"),
    "2022 Online Championship Series Playoffs": ("Finals", "Semifinals", "Quarterfinals", "Top 16", "constructed"),
    "2022 Jawa Cup": ("Finals", "Top 4", "Top 8", "constructed"),
}


def parse_url(url: str):
    slug = url.rstrip("/").split("/")[-1].lower()
    if slug.startswith("2025-") or slug.startswith("2026-"):
        return None
    m = re.search(r"-(ds|ls)-(.+)$", slug)
    if not m:
        return None
    side = m.group(1).upper()
    obj = hm.pretty_obj(m.group(2))
    left = slug[: m.start()]
    rm = re.match(r"(\d{4})-([a-z0-9-]+)-regionals?-(.+)$", left)
    if not rm:
        rm = re.match(r"(2023)-(ryloth)-(.+)$", left)
    if rm:
        year, planet, player_slug = rm.groups()
        if year not in ("2022", "2023", "2024"):
            return None
        planet_title = hm.PLANET_NAME.get(planet, hm.pretty_name(planet))
        event = f"{year} Regional Championships"
        return event, planet_title, False, year, hm.pretty_name(player_slug), side, obj, url
    for pref, event, stage, t8, year in PREFIXES:
        if left.startswith(pref):
            rest = left[len(pref) :]
            player = hm.pretty_name(rest.strip("-"))
            return event, stage, t8, year, player, side, obj, url
    return None


def _safe_title(s: str) -> str:
    return re.sub(r"[#<>\[\]\|\{\}]", "", s).replace("  ", " ").strip()


def deck_title(event, stage, player, side, obj):
    if event.endswith("Regional Championships"):
        year = event.split()[0]
        return _safe_title(f"{year} {stage} Regionals {player} {side} {obj}")
    short = SHORT[event]
    st = "" if stage in ("Day 1", "Swiss", "constructed") else stage + " "
    return _safe_title(f"{short} {st}{player} {side} {obj}")


def wiki_fname(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_") + ".wiki"


def format_for(event: str) -> str:
    if "Jawa" in event:
        return "[[Jawa Format]]"
    if "Retro Online" in event:
        return "[[Premiere - Death Star II]]"
    return "[[Open]]"


def main():
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    urls = [ln.strip() for ln in URL_FILE.read_text(encoding="utf-8").splitlines() if ln.strip()]
    parsed = []
    skip = nofile = thin = 0
    for url in urls:
        info = parse_url(url)
        if not info:
            skip += 1
            continue
        event, stage, t8, year, player, side, obj, url = info
        html = DECKS / (url.rstrip("/").split("/")[-1] + ".html")
        if not html.exists():
            nofile += 1
            continue
        counts, cards = ge.parse_pc_html(html)
        if sum(counts.values()) < 10:
            thin += 1
            print("THIN", html.name, sum(counts.values()))
            continue
        parsed.append((event, stage, t8, year, player, side, obj, url, counts, cards))
    print("parsed", len(parsed), "skip", skip, "nofile", nofile, "thin", thin)

    pages_for = defaultdict(list)
    hub_labels = {}
    titles = []
    for event, stage, t8, year, player, side, obj, url, counts, cards in parsed:
        title = deck_title(event, stage, player, side, obj)
        pages_for[(event, stage, player, side)].append(title)

    for event, stage, t8, year, player, side, obj, url, counts, cards in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = (pages_for.get((event, stage, player, other)) or [None])[0]
        ge.EVENT_TITLE = event
        ge.deck_page_title = lambda p, t, s, o, event=event, stage=stage: deck_title(
            event, stage, p, s, o
        )
        title, body, hub = ge.render_deck(
            player, t8, side, obj, counts, cards, url, companion, dests, title_map, bp
        )
        hub = hm.polish_hub(hub, obj)
        body = body.replace("[[Category:2026]]", f"[[Category:{year}]]")
        body = body.replace("* [[European Championships]]", "* [[List of SWCCG tournaments]]")
        body = re.sub(r"\* '''Stage:''' [^\n]+", f"* '''Stage:''' {stage}", body, count=1)
        body = body.replace("* '''Format:''' [[Open]]", f"* '''Format:''' {format_for(event)}")
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub
        titles.append((title, f"pages/{wiki_fname(title)}"))

    def cell(event, stage, player, side):
        bits = []
        for page in pages_for.get((event, stage, player, side)) or []:
            bits.append(f"[[{page}|{hub_labels.get(page, page)}]]")
        return " · ".join(bits) if bits else "—"

    def players_in(event, stage):
        out = []
        for e, st, t8, year, player, side, obj, url, counts, cards in parsed:
            if e == event and st == stage and player not in out:
                out.append(player)
        return out

    def fill_round_hub(event, stages):
        hubp = PAGES / wiki_fname(event)
        if not hubp.exists():
            return
        rows = []
        for st in stages:
            for p in players_in(event, st):
                rows.append([st, f"[[{p}]]", cell(event, st, p, "DS"), cell(event, st, p, "LS")])
        if not rows:
            return
        table = hm.wikitable(["Round", "Player", "Dark", "Light"], rows)
        text = hm.replace_section(
            hubp.read_text(encoding="utf-8"), ("Decklists", "Bracket"), "Decklists", table
        )
        hubp.write_text(text, encoding="utf-8", newline="\n")
        titles.append((event, f"pages/{wiki_fname(event)}"))

    def fill_day_hub(event, t8_stage, d1_stage):
        hubp = PAGES / wiki_fname(event)
        if not hubp.exists():
            return
        text = hubp.read_text(encoding="utf-8")

        def ptab(heading, stage):
            rows = []
            for i, p in enumerate(players_in(event, stage), 1):
                rows.append([str(i), f"[[{p}]]", cell(event, stage, p, "DS"), cell(event, stage, p, "LS")])
            return hm.wikitable([heading, "Player", "Dark", "Light"], rows, sortable=True)

        if players_in(event, t8_stage):
            text = hm.replace_section(text, ("Top 8", "Top 4", "Decklists"), t8_stage, ptab("Finish", t8_stage))
        if players_in(event, d1_stage):
            text = hm.replace_section(text, ("Day 1", "Decklists"), "Day 1", ptab("Day 1", d1_stage))
        hubp.write_text(text, encoding="utf-8", newline="\n")
        titles.append((event, f"pages/{wiki_fname(event)}"))

    for event, stages in STAGE_ORDER.items():
        fill_round_hub(event, stages)
    fill_day_hub("2024 European Championship", "Top 8", "Day 1")
    fill_day_hub("2023 European Championship", "Top 8", "Day 1")
    fill_day_hub("2022 European Championship", "Top 8", "Day 1")
    fill_day_hub("2023 San Diego Super Open", "Day 2", "Day 1")

    for year in ("2024", "2023", "2022"):
        ev = f"{year} Regional Championships"
        hubp = PAGES / wiki_fname(ev)
        if not hubp.exists():
            continue
        found = []
        for e, st, t8, y, player, side, obj, url, counts, cards in parsed:
            if e == ev and st not in found:
                found.append(st)
        if not found:
            continue
        chunks = ["Published constructed lists as posted on the PC results page."]
        for planet in found:
            rows = []
            for p in players_in(ev, planet):
                rows.append([f"[[{p}]]", cell(ev, planet, p, "DS"), cell(ev, planet, p, "LS")])
            chunks.append(
                f"=== {planet} Regionals ===\n\n"
                + hm.wikitable(["Player", "Dark", "Light"], rows, sortable=True)
            )
        text = hm.replace_section(
            hubp.read_text(encoding="utf-8"), ("Decklists",), "Decklists", "\n\n".join(chunks)
        )
        hubp.write_text(text, encoding="utf-8", newline="\n")
        titles.append((ev, f"pages/{wiki_fname(ev)}"))

    by_p = defaultdict(list)
    for event, stage, t8, year, player, side, obj, url, counts, cards in parsed:
        by_p[(player, event, year)].append((stage, t8, side, obj, url))
    for (player, event, year), rows_src in by_p.items():
        rows = []
        stages = []
        for stage, t8, side, obj, url in rows_src:
            if stage not in stages:
                stages.append(stage)
        for stage in stages:
            ds = cell(event, stage, player, "DS")
            ls = cell(event, stage, player, "LS")
            rows.append(
                f"|- \n| {year} || [[{event}]] ({stage}) || {format_for(event)} || — || {ds} || {ls}"
            )
        if rows:
            upsert_stub(player, rows, event, PC_URL.get(event, ""))
            sp = STUBS / (player.replace(" ", "_") + ".wiki")
            if sp.exists():
                st = sp.read_text(encoding="utf-8")
                cat = f"[[Category:{year}]]"
                if cat not in st:
                    st = st.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
                    sp.write_text(st, encoding="utf-8", newline="\n")
                titles.append((player, f"pages/player-stubs/{sp.name}"))

    seen = {}
    for t, r in titles:
        seen[t] = r
    TSV.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8", newline="\n")
    print("html titles", len(seen), "->", TSV)


if __name__ == "__main__":
    main()
