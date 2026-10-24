#!/usr/bin/env python3
"""Build wiki pages for finished tournament-report data files (Claude 2026-10-24, Bill's option 3:
an article per report + the report's results on player and event pages).

  python3 tr_build.py <batch> <source>/<id> ...     e.g.  tr_build.py tr-batch-01 decktech/d3 decktech/d110

Writes /tmp/claude-0/<batch>pkg/{y-<batch>.tsv,pages/,since.txt,wiki_api_apply.py} and a tar in
/mnt/user-data/outputs/<batch>-apply.tar, applied on the PC with dtchunk_long.sh like the deck batches.
Pages: each report article; each author's person page (new stub, or a "Tournament reports" section
added/extended); each existing event hub ("Tournament reports" section); the source catalog page
(e.g. [[DeckTech tournament reports]]) and the [[Tournament reports]] hub, both rebuilt from every
finished data file. Hub results rows and new hubs are written by hand per batch (they need judgment).
"""
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import decktech_batch as b

A = Path(__file__).parent
R = A / "tournament-reports"
FORBID = set("#<>[]{}|")

SOURCES = {  # source key -> (catalog page, how the report was published, category)
    "decktech": ("DeckTech tournament reports", "DeckTech", "DeckTech tournament reports"),
}


def load(key: str) -> dict:
    src, rid = key.split("/")
    d = json.loads((R / src / f"{rid}.json").read_text(encoding="utf-8"))
    d["_key"] = key
    return d


def finished(d: dict) -> bool:
    return bool(d.get("title") and d.get("author") is not None and "games" in d)


def long_date(s: str) -> str:
    for f in ("%b %d, %Y", "%Y-%m-%d"):
        try:
            x = dt.datetime.strptime(s.strip(), f)
            return f"{x.day} {x.strftime('%B %Y')}"
        except ValueError:
            pass
    return s


def iso(s: str) -> str:
    try:
        return dt.datetime.strptime(s.strip(), "%b %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return s


def event_long(d: dict) -> str:
    e = d.get("event_date") or ""
    if re.fullmatch(r"\d{4}-\d\d-\d\d", e):
        return long_date(e)
    if re.fullmatch(r"\d{4}-\d\d", e):
        x = dt.datetime.strptime(e, "%Y-%m")
        return x.strftime("%B %Y")
    return e


def person(d: dict) -> str | None:
    if d.get("author_page") == "none":
        return None
    return d.get("author_link") or d["author"]


def page_title(d: dict) -> str:
    if d.get("page_title"):
        t = d["page_title"]
    elif d.get("withhold_title"):
        t = f"{d['author']} {d['event'] or (d.get('event_date') or '')[:4] + ' tournament'} report"
    else:
        t = f"{d['author']} {d['title']}"
    t = re.sub(r"\s+", " ", t).strip() + " (tournament report)"
    bad = FORBID & set(t)
    if bad:
        raise SystemExit(f"{d['_key']}: title has {bad}: {t}")
    return t


def ref(d: dict) -> str:
    src = SOURCES[d["source"]][1]
    return (f'<ref name="tr-{d["id"]}">[{d["url"]} {d["posted_title"]}], {src} ({d["byline"]}, '
            f'{long_date(d["date"])}). Preservation copy: [{d["mirror"]} GitHub Pages].</ref>')


def event_text(d: dict) -> str:
    if d.get("event") and d.get("event_status") != "unnamed":
        return f"[[{d['event']}]]"
    return d.get("event_desc") or "a tournament"


def nowiki(s: str) -> str:
    return s.replace("</nowiki>", "&lt;/nowiki&gt;")


def cell(s) -> str:
    return "—" if s in (None, "") else str(s).replace("|", "&#124;")


def article(d: dict) -> str:
    who = person(d)
    whol = f"[[{who}]]" if who else d["byline"]
    src = SOURCES[d["source"]][1]
    lead = (f"'''{page_title(d)}''' is the tournament report {whol} posted on {src} on {long_date(d['date'])} "
            f"about {event_text(d)}.{ref(d)}")
    if d.get("withhold_title"):
        lead += " The report's own title is not used as the page title; it appears in the original report below."
    if d.get("summary"):
        lead += " " + d["summary"]
    info = [f"* '''Author:''' {whol}" + (f" (byline: {d['byline']})" if who and d['byline'] != who else "")]
    info.append(f"* '''Published:''' {long_date(d['date'])} ({src})")
    if not d.get("withhold_title"):
        info.append(f"* '''Report title:''' ''{d['title']}''")
    info.append(f"* '''Event:''' {event_text(d)}")
    if d.get("event_date"):
        info.append(f"* '''Event date:''' {event_long(d)}")
    if d.get("event_site"):
        info.append(f"* '''Site:''' {d['event_site']}")
    if d.get("players"):
        info.append(f"* '''Players:''' {d['players']}")
    for k, lab in (("author_finish", "Finish"), ("author_record", "Record"), ("author_points", "Points")):
        if d.get(k):
            info.append(f"* '''{lab}:''' {d[k]}")
    for x in d.get("decks") or []:
        deck = f"[[{x['deck_page']}|{x['description']}]]" if x.get("deck_page") else x.get("description") or "—"
        info.append(f"* '''{x['side']} deck:''' {deck}" if x.get("side") else f"* '''Deck:''' {deck}")
    out = [lead, "", "== Report info ==", *info, ""]
    g = d.get("games") or []
    if g:
        out += ["== Games ==", "",
                "Games as the author describes them; margins are as stated in the report.", "",
                '{| class="wikitable"', "|-",
                "! Round !! Opponent !! Author's deck !! Opponent's deck !! Result !! Margin"]
        for x in g:
            opp = f"[[{x['opponent']}]]" if x.get("opponent_page") else cell(x.get("opponent"))
            ad = " ".join(v for v in (f"[[{x['author_side']}]]" if x.get("author_side") else "", x.get("author_deck") or "") if v)
            res = cell(x.get("result")) + (f" ({x['note']})" if x.get("note") else "")
            out += ["|-", f"| {cell(x.get('round'))} || {opp} || {cell(ad)} || {cell(x.get('opponent_deck'))} || {res} || {cell(x.get('margin'))}"]
        out += ["|}", ""]
    o = d.get("other_results") or []
    if o:
        out += ["== Other results named in the report ==", ""]
        out += [f"* {x['finish']}: " + (f"[[{x['player']}]]" if x.get("player_page") else x["player"]) for x in o]
        out += [""]
    out += ["== Original report ==", "",
            f"'''{d['posted_title']}'''",
            f"* '''Author:''' {d['byline']}",
            f"* '''Published:''' {d['date']}",
            "",
            '<div style="white-space:pre-wrap; font-family:inherit"><nowiki>',
            nowiki(d["body"]),
            "</nowiki></div>", ""]
    see = ["[[Tournament reports]]", f"[[{SOURCES[d['source']][0]}]]"]
    if who:
        see.insert(0, f"[[{who}]]")
    if d.get("event") and d.get("event_status") != "unnamed":
        see.insert(0, f"[[{d['event']}]]")
    for x in d.get("decks") or []:
        if x.get("deck_page"):
            see.append(f"[[{x['deck_page']}]]")
    year = (d.get("event_date") or iso(d["date"]))[:4]
    out += ["== See also ==", "", *[f"* {s}" for s in see], "",
            "== Sources ==", "",
            f"* [{d['url']} {d['posted_title']}], stephenskilton.com",
            f"* [{d['mirror']} {d['posted_title']}] (GitHub Pages)", "",
            "== References ==", "<references />", "",
            "[[Category:Tournament reports]]",
            f"[[Category:{SOURCES[d['source']][2]}]]",
            f"[[Category:{year}]]"]
    return "\n".join(out) + "\n"


def report_bullet(d: dict, for_hub: bool = False) -> str:
    who = person(d)
    bits = []
    if for_hub:
        bits.append(f"by [[{who}]]" if who else f"by {d['byline']}")
    else:
        bits.append(event_text(d))
        if d.get("event_date"):
            bits.append(event_long(d))
    if d.get("author_finish"):
        bits.append(d["author_finish"])
    if d.get("author_record"):
        bits.append(d["author_record"])
    return f"* [[{page_title(d)}]] — " + ", ".join(bits)


def add_section(text: str, head: str, bullets: list[str], intro: str = "") -> str:
    """Add bullets to == head == (create it before See also / Sources / References / categories)."""
    bullets = [x for x in bullets if x.split(" — ")[0] not in text]
    if not bullets:
        return text
    add = "\n".join(bullets)
    m = re.search(rf"^== {re.escape(head)} ==\s*$", text, re.M)
    if m:
        n = re.search(r"^==[^=]", text[m.end():], re.M)
        k = m.end() + n.start() if n else len(text)
        body = text[:k].rstrip("\n")
        return body + "\n" + add + "\n\n" + text[k:]
    for h in ("== See also ==", "== Sources ==", "== References ==", "{{#if:1|", "[[Category:"):
        k = text.find(h)
        if k >= 0:
            return text[:k] + f"== {head} ==\n\n" + (intro + "\n\n" if intro else "") + add + "\n\n" + text[k:]
    return text.rstrip("\n") + f"\n\n== {head} ==\n\n" + add + "\n"


def new_person(name: str, ds: list[dict]) -> str:
    d = ds[0]
    handle = re.search(r'"([^"]+)"', d["byline"])
    h = f" (DeckTech handle '''{handle.group(1)}''')" if handle and handle.group(1) != name else ""
    years = sorted({(x.get("event_date") or iso(x["date"]))[:4] for x in ds})
    return (f"'''{name}'''{h}{ref(d)} is a Star Wars CCG player who wrote "
            f"{'a tournament report' if len(ds) == 1 else 'tournament reports'} for {SOURCES[d['source']][1]}.\n\n"
            "== Tournament reports ==\n\n" + "\n".join(report_bullet(x) for x in ds) + "\n\n"
            "== See also ==\n\n* [[Tournament reports]]\n* [[" + SOURCES[d["source"]][0] + "]]\n\n"
            "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n"
            "[[Category:People]]\n" + "\n".join(f"[[Category:{y}]]" for y in years) + "\n")


def all_finished() -> list[dict]:
    out = []
    for src in SOURCES:
        for f in sorted((R / src).glob("*.json")):
            d = load(f"{src}/{f.stem}")
            if finished(d) and not d.get("skip"):
                out.append(d)
    return out


def catalog_decktech(ds: list[dict], current: str) -> str:
    rows = []
    for d in sorted(ds, key=lambda x: (iso(x["date"]), x["id"])):
        who = person(d)
        rows.append(f"|-\n| data-sort-value=\"{iso(d['date'])}\" | {long_date(d['date'])} || {event_text(d)} || "
                    f"[[{page_title(d)}|{'(title withheld)' if d.get('withhold_title') else d['title']}]] || "
                    f"{'[[' + who + ']]' if who else d['byline']} || {cell(d.get('author_finish'))}")
    table = ('{| class="wikitable sortable"\n|-\n! Posted !! Event !! Report !! Author !! Finish\n'
             + "\n".join(rows) + "\n|}")
    head = ("'''DeckTech tournament reports''' are the tournament reports players posted on DeckTech alongside its "
            "decklists, from August 1999 to 2002. DeckTech itself is gone; Stephen Skilton's archive keeps 1,406 of them "
            "under [https://www.stephenskilton.com/decktech_archives/tournament_reports/ Tournament Reports] "
            "(mirror: [https://stevetotheizz0.github.io/decktech_archives/tournament_reports/ GitHub Pages]). "
            "The archive keeps each report's text, author and date, but its titles are URL slugs, so the titles here "
            "are rebuilt from them. Each report on this wiki has its own article, part of [[Tournament reports]].")
    tail = current[current.find("\n== See also =="):] if "\n== See also ==" in current else ""
    tail = tail.replace("* [[Decklists]] · [[DeckTech]] · [[DeckTech decks]]",
                        "* [[Tournament reports]] · [[DeckTech]] · [[DeckTech decks]] · [[Decklists]]")
    if "[[Category:Tournament reports]]" not in tail:
        tail = tail.rstrip("\n") + "\n[[Category:Tournament reports]]\n"
    pending = ""
    m = re.search(r"\n== Worlds reports (?:already on the archive|not yet transcribed) ==.*?(?=\n== )", current, re.S)
    if m:  # keep the not-yet-transcribed Worlds rows, drop the ones that now have articles
        done = {d["slug"] for d in ds}
        keep = [r.strip() for r in re.findall(r"\n(\| [^\n]*\|\| \[https://www\.stephenskilton[^\n]*)", m.group(0))
                if not any(s in r for s in done)]
        if keep:
            pending = ("\n== Worlds reports not yet transcribed ==\n\nThese DecipherCon / Worlds reports are in the "
                       "archive and will get articles as transcription continues.\n\n"
                       '{| class="wikitable sortable"\n|-\n! Date !! Event !! Title !! Author !! Archive\n'
                       + "".join(f"|-\n{r}\n" for r in keep) + "|}\n")
    body = (f"{head}\n\n== Reports on this wiki ==\n\n{len(ds)} of the archive's 1,406 reports have their own "
            "article so far (report text verbatim, plus the author's games and results). "
            "Sort by any column.\n\n" + table + "\n" + pending + tail)
    return body


TR_HUB = """'''Tournament reports''' are players' own accounts of Star Wars CCG tournaments: who they played, what decks they met, and how they finished. They were posted on deck sites, fan sites and forums, and later recorded as videos. On this wiki each report has its own article, with the original text reproduced verbatim and uncensored, and its results are added to the event's page and the author's page.

== How report articles are organized ==

* '''One article per report''', titled ''<Author> <Report title> (tournament report)''. A report whose own title is crude is titled by author and event instead; the original title stays inside the article.
* '''Report info''' gives the author, publication, event, date, finish and record; '''Games''' lists each game the author describes; '''Original report''' is the report as published.
* The author's person page gets a '''Tournament reports''' section, and the event's page lists the reports written about it.
* Results taken only from a report are marked as such. When a report disagrees with Decipher's records (for example on the city of an event), the wiki follows Decipher's record and notes the discrepancy.
* Every report article is in [[:Category:Tournament reports]] and in a category for its source.

== Sources ==

{| class="wikitable"
|-
! Source !! Years !! Reports on the wiki !! Catalog
%ROWS%
|}

More sources will get their own catalog page and category, named ''<Source> tournament reports'', as they are added: other fan websites, the Players Committee forum, and video reports such as YouTube tournament coverage.

== See also ==

* [[Tournaments]]
* [[List of SWCCG tournaments]]
* [[Championships]]
* [[Decklists]]

[[Category:Tournament reports]]
[[Category:Tournaments]]
"""


def tr_hub(ds: list[dict]) -> str:
    rows = []
    for src, (cat, name, _c) in SOURCES.items():
        s = [d for d in ds if d["source"] == src]
        ys = sorted({iso(d["date"])[:4] for d in s})
        rows.append(f"|-\n| {name} || {ys[0] + '–' + ys[-1] if ys else '—'} || {len(s)} || [[{cat}]]")
    return TR_HUB.replace("%ROWS%", "\n".join(rows))


def main() -> None:
    batch, keys = sys.argv[1], sys.argv[2:]
    ds = [load(k) for k in keys]
    for d in ds:
        if not finished(d):
            raise SystemExit(f"{d['_key']} is not finished")
    pk = Path(f"/tmp/claude-0/{batch}pkg")
    shutil.rmtree(pk, ignore_errors=True)
    (pk / "pages").mkdir(parents=True)
    rows = []

    def emit(title: str, text: str) -> None:
        fn = "pages/" + title.replace(" ", "_").replace("/", "%2F") + ".wiki"
        (pk / fn).write_text(text, encoding="utf-8")
        rows.append(f"{title}\t{fn}")

    titles = [page_title(d) for d in ds]
    if len(set(t.lower() for t in titles)) != len(titles):
        raise SystemExit(f"duplicate report titles: {titles}")
    for d in ds:
        emit(page_title(d), article(d))
    by_person: dict[str, list[dict]] = {}
    for d in ds:
        if person(d):
            by_person.setdefault(person(d), []).append(d)
    for name, xs in by_person.items():
        cur = b.live_text(name)
        if cur and cur.lstrip().upper().startswith("#REDIRECT"):
            raise SystemExit(f"{name} is a redirect; set author_link")
        emit(name, new_person(name, xs) if cur is None else
             add_section(cur, "Tournament reports", [report_bullet(x) for x in xs]))
    by_event: dict[str, list[dict]] = {}
    for d in ds:
        if d.get("event") and d.get("event_status") == "existing":
            by_event.setdefault(d["event"], []).append(d)
    for ev, xs in by_event.items():
        cur = b.live_text(ev)
        if cur is None:
            raise SystemExit(f"event {ev} marked existing but missing")
        emit(ev, add_section(cur, "Tournament reports", [report_bullet(x, True) for x in xs],
                             "Players' own reports from this event."))
    every = all_finished()
    keys_now = {d["_key"] for d in every}
    every += [d for d in ds if d["_key"] not in keys_now]
    cur = b.live_text("DeckTech tournament reports") or ""
    emit("DeckTech tournament reports", catalog_decktech([d for d in every if d["source"] == "decktech"], cur))
    emit("Tournament reports", tr_hub(every))
    emit("Category:Tournament reports",
         "Articles for individual Star Wars CCG tournament reports. See [[Tournament reports]].\n\n[[Category:Tournaments]]\n")
    emit("Category:DeckTech tournament reports",
         "Tournament reports first published on DeckTech. See [[DeckTech tournament reports]].\n\n[[Category:Tournament reports]]\n")
    (pk / f"y-{batch}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    shutil.copy(pk / f"y-{batch}.tsv", A / f"y-{batch}.tsv")
    shutil.copy(A / "wiki_api_apply.py", pk)
    (pk / "since.txt").write_text(dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")
    print("\n".join(r.split("\t")[0] for r in rows))
    subprocess.run(["tar", "cf", f"/mnt/user-data/outputs/{batch}-apply.tar", "-C", str(pk), "."], check=True)
    print(f"{len(rows)} pages -> /mnt/user-data/outputs/{batch}-apply.tar")


if __name__ == "__main__":
    main()
