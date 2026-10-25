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
        t = d['title'] if d['title'].lower().startswith(d['author'].lower() + " ") else f"{d['author']} {d['title']}"  # no doubled name (Claude 2026-10-25)
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
    """A table cell: escape | except inside [[links]] (Claude 2026-10-25: piped links were escaped and broke)."""
    if s in (None, ""):
        return "—"
    parts = re.split(r"(\[\[[^\]]*\]\])", str(s))
    return "".join(p if p.startswith("[[") else p.replace("|", "&#124;") for p in parts)


def dlink(desc, obj):
    """A deck description, linked to its Objective's Decipher page when the data names one (Bill 2026-10-24)."""
    if obj and desc:
        return f"[[{obj}|{desc}]]"
    if obj:
        return f"[[{obj}|{obj.split(' / ')[0]}]]"
    return desc


def games_block(g: list, head: str | None) -> list[str]:
    if not g:
        return []
    out = ([head, ""] if head else []) + [
        "Games as the author describes them; margins are as stated in the report.", "",
        '{| class="wikitable"', "|-",
        "! Round !! Opponent !! Author's deck !! Opponent's deck !! Result !! Margin"]
    for x in g:
        opp = f"[[{x['opponent']}]]" if x.get("opponent_page") else cell(x.get("opponent"))
        ad = " ".join(v for v in (f"[[{x['author_side']}]]" if x.get("author_side") else "", dlink(x.get("author_deck"), x.get("author_objective")) or "") if v)
        res = cell(x.get("result")) + (f" ({x['note']})" if x.get("note") else "")
        out += ["|-", f"| {cell(x.get('round'))} || {opp} || {cell(ad)} || {cell(dlink(x.get('opponent_deck'), x.get('opponent_objective')))} || {res} || {cell(x.get('margin'))}"]
    return out + ["|}", ""]


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
        deck = f"[[{x['deck_page']}|{x['description']}]]" if x.get("deck_page") else dlink(x.get("description"), x.get("objective")) or "—"
        info.append(f"* '''{x['side']} deck:''' {deck}" if x.get("side") else f"* '''Deck:''' {deck}")
    out = [lead, "", "== Report info ==", *info, ""]
    out += games_block(d.get("games") or [], "== Games ==")
    o = d.get("other_results") or []
    if o:
        out += ["== Other results named in the report ==", ""]
        out += [f"* {x['finish']}: " + (f"[[{x['player']}]]" if x.get("player_page") else x["player"]) for x in o]
        out += [""]
    for se in d.get("side_events") or []:
        name = f"[[{se['event']}]]" if se.get("event") and se.get("event_status") != "unnamed" else (se.get("event_desc") or "Side event")
        out += [f"== Side event: {se.get('event') or se.get('event_desc') or 'other event'} ==", ""]
        line = f"The report also covers {name}"
        if se.get("event_date"):
            line += f" ({event_long(se)})"
        line += "."
        if se.get("summary"):
            line += " " + se["summary"]
        out += [line, ""]
        out += games_block(se.get("games") or [], None)
    ds_ = d.get("discrepancies") or []
    if ds_:
        out += ["== Discrepancies ==", "",
                "Where this report disagrees with other sources, the wiki keeps the other record and notes the difference here.", ""]
        out += [f"* {x['text']}" + (f" (see [[{x['event']}]])" if x.get("event") else "") for x in ds_]
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


def dedupe_bullets(text: str, head: str) -> str:
    """Drop repeated identical bullet lines in == head == (an author's report was once listed per event; Claude 2026-10-25)."""
    m = re.search(rf"^== {re.escape(head)} ==\s*$", text, re.M)
    if not m:
        return text
    n = re.search(r"^==[^=]", text[m.end():], re.M)
    k = m.end() + n.start() if n else len(text)
    seen, out = set(), []
    for line in text[m.end():k].split("\n"):
        if line.startswith("* "):
            if line in seen:
                continue
            seen.add(line)
        out.append(line)
    return text[:m.end()] + "\n".join(out) + text[k:]


def add_section(text: str, head: str, bullets: list[str], intro: str = "") -> str:
    """Add bullets to == head == (create it before See also / Sources / References / categories)."""
    bullets = [x for x in dict.fromkeys(bullets) if x.split(" — ")[0] not in text]  # each bullet once (Claude 2026-10-25)
    text = dedupe_bullets(text, head)
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


BUILT = R / "built.txt"  # keys already published; catalogs list only these plus the current batch (Claude 2026-10-25)


def all_finished() -> list[dict]:
    built = set(BUILT.read_text().split()) if BUILT.exists() else set()
    out = []
    for src in SOURCES:
        for f in sorted((R / src).glob("*.json")):
            d = load(f"{src}/{f.stem}")
            if finished(d) and not d.get("skip") and f"{src}/{f.stem}" in built:
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

    emitted: dict[str, str] = {}

    def emit(title: str, text: str) -> None:
        fn = "pages/" + title.replace(" ", "_").replace("/", "%2F") + ".wiki"
        (pk / fn).write_text(text, encoding="utf-8")
        emitted[title] = text
        if f"{title}\t{fn}" not in rows:
            rows.append(f"{title}\t{fn}")

    titles = [page_title(d) for d in ds]
    if len(set(t.lower() for t in titles)) != len(titles):
        raise SystemExit(f"duplicate report titles: {titles}")
    for d in ds:
        emit(page_title(d), article(d))
    import tr_world as W
    log: list[str] = []
    cache: dict[str, str | None] = {}

    def live(t: str):
        if t not in cache:
            cache[t] = b.live_text(t)
        return cache[t]

    # events: new hubs, existing hub updates
    hubs: dict[str, str] = {}
    new_events = []
    for d in ds:
        for e in W.events(d):
            if not W.named(e):
                continue
            ev = e["event"]
            cur = hubs.get(ev) or live(ev)
            if cur is None:
                cur = W.new_hub(e, d)
                new_events.append(e)
            else:
                cur = W.hub_add_participants(cur, d, e, log)
                if ev in {x["event"] for x in new_events} and e.get("event_winner") and not re.search(r"^\* '''Winner:'''", cur, re.M):
                    # a hub created earlier in this batch takes the winner a later report names (Claude 2026-10-25)
                    cur = W.hub_updates(cur, d, [{"event": ev, "field": "winner", "value": e["event_winner"]}], log)
                    for x in new_events:
                        if x["event"] == ev and not x.get("event_winner"):
                            x["event_winner"] = e["event_winner"]  # so its List row gets the winner too
                cur = add_section(cur, "Tournament reports", [W.event_bullet(d, e)],
                                  "Players' own reports from this event.")
            if e.get("parent"):
                par = hubs.get(e["parent"]) or live(e["parent"])
                if par is not None:
                    hubs[e["parent"]] = add_section(par, "Side events", [f"* [[{ev}]] — " + (e.get("event_type") or "side event") + (f", {W.T.event_long(e)}" if e.get("event_date") else "")])
            hubs[ev] = W.ensure_ref(cur, d)
        for u in d.get("hub_updates") or []:
            if u.get("event") in hubs or live(u.get("event") or ""):
                hubs[u["event"]] = W.ensure_ref(W.hub_updates(hubs.get(u["event"]) or live(u["event"]), d, [u], log), d)
        for x in d.get("discrepancies") or []:
            if x.get("event") and (x["event"] in hubs or live(x["event"])):
                hubs[x["event"]] = W.ensure_ref(W.hub_discrepancies(hubs.get(x["event"]) or live(x["event"]), d, [x]), d)
    for ev, txt in hubs.items():
        hubs[ev] = txt = W.prune_named(txt)
        emit(ev, txt)
    # a hub date made precise from a report is copied to its List row (Claude 2026-10-25)
    ups = [m.groups() for m in (re.match(r"(.+): Date '(.+)' -> '(.+)' from the report$", x) for x in log) if m]
    wins = [(u["event"], u["value"]) for d in ds for u in d.get("hub_updates") or [] if u.get("field") == "winner"]
    if wins:  # an unknown winner on the List is filled from a report's hub update (Claude 2026-10-25)
        L = emitted.get("List of SWCCG tournaments") or live("List of SWCCG tournaments")
        for ev, who in wins:
            link = f"[[{who}]]" if W.full_name(who) else who
            L = re.sub(rf"^(\| [^\n]*\|\| \[\[{re.escape(ev)}\]\] \|\|[^\n]*\|\| )(—|Unknown|)\s*$", rf"\g<1>{link}", L, flags=re.M)
        emit("List of SWCCG tournaments", L)
    if ups:
        L = emitted.get("List of SWCCG tournaments") or live("List of SWCCG tournaments")
        for ev, old, new in ups:
            L2 = re.sub(rf"(\|\| \[\[{re.escape(ev)}\]\] \|\| ){re.escape(old)}( \|\|)", rf"\g<1>{new}\2", L)
            if L2 == L:  # the List row has its own wording: replace its date cell (Claude 2026-10-25)
                L2 = re.sub(rf"(\|\| \[\[{re.escape(ev)}\]\] \|\| )[^|\n]*?( \|\|)", rf"\g<1>{new}\2", L, count=1)
                log.append(f"{ev}: List row date set to '{new}'" if L2 != L else f"{ev}: List row date '{old}' not found")
            L = L2
        emit("List of SWCCG tournaments", L)
    sites = [(u["event"], u["value"]) for d in ds for u in d.get("hub_updates") or [] if u.get("field") == "site"]
    if sites:  # an empty Site cell on the List is filled from a report's hub update (Claude 2026-10-25)
        L = emitted.get("List of SWCCG tournaments") or live("List of SWCCG tournaments")
        L2 = L
        for ev, site in sites:
            L2 = re.sub(rf"^(\| [^\n]*?\|\| \[\[{re.escape(ev)}\]\] \|\|[^|\n]*\|\| )(?:—)?( \|\|)", lambda m: m.group(1) + site + m.group(2), L2, count=1, flags=re.M)
        if L2 != L:
            emit("List of SWCCG tournaments", L2)
    if new_events:
        L = emitted.get("List of SWCCG tournaments") or live("List of SWCCG tournaments")
        for e in new_events:
            if not e.get("event_date"):
                log.append(f"{e['event']}: no date, not added to the List")
                continue
            L = W.list_insert(L, e)
        emit("List of SWCCG tournaments", L)
    if "List of SWCCG tournaments" in emitted:
        emit("List of SWCCG tournaments", W.list_sort(emitted["List of SWCCG tournaments"]))

    def fmt_of(e):
        if e.get("event_format"):
            return e["event_format"]
        return W.hub_format(hubs.get(e.get("event") or "") or (live(e["event"]) if W.named(e) else None))

    # people
    people: dict[str, list] = {}
    for d in ds:
        for n, xs in W.participants(d).items():
            people.setdefault(n, []).extend((d, x) for x in xs)
    for n, entries in people.items():
        cur = live(n)
        if cur and cur.lstrip().upper().startswith("#REDIRECT"):
            m = re.match(r"#REDIRECT\s*\[\[([^\]|#]+)", cur.strip(), re.I)
            log.append(f"{n} redirects to {m.group(1) if m else '?'}; used the target")
            n = m.group(1).strip()
            cur = live(n)
        if cur and re.search(r"\[\[Category:Disambiguation\]\]|\{\{[Dd]isambig", cur):
            log.append(f"{n} is a disambiguation page: rows NOT added (map the report's name to the right person)")
            continue
        txt = W.person_text(n, entries, cur, fmt_of)
        for d, _x in entries:
            txt = W.ensure_ref(txt, d)
        emit(n, txt)
    # both ways (Bill 2026-10-24): every person linked in a touched event's results lists that event on their page
    for ev in list(hubs):
        for n, row in W.hub_people(emitted.get(ev) or hubs[ev]):
            cur = emitted.get(n) or live(n)
            if cur is None:
                log.append(f"{ev}: [[{n}]] has no page")
                continue
            if cur.lstrip().upper().startswith("#REDIRECT"):
                tgt = re.match(r"#REDIRECT\s*\[\[([^\]|#]+)", cur.strip(), re.I).group(1).strip()
                hub = (emitted.get(ev) or hubs[ev]).replace(f"[[{n}]]", f"[[{tgt}]]").replace(f"[[{n}|", f"[[{tgt}|")
                hubs[ev] = hub
                emit(ev, hub)
                log.append(f"{ev}: [[{n}]] was a redirect; now links [[{tgt}]]")
                n, cur = tgt, emitted.get(tgt) or live(tgt)
                if cur is None:
                    continue
            tbl = W.person_results_table(cur)
            if f"[[{ev}]]" in tbl or f"[[{ev}|" in tbl:
                continue
            r = W.row_from_hub(emitted.get(ev) or hubs[ev], ev, row)
            if not r:
                log.append(f"{n}: {ev} row has no citable source on the event page; not added")
                continue
            emit(n, W.add_result_rows(cur, [(f"[[{ev}", r)], n))
    log += W.LOG
    (pk / "log.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("\n".join("LOG " + x for x in log))
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
    built = set(BUILT.read_text().split()) if BUILT.exists() else set()
    BUILT.write_text("\n".join(sorted(built | set(keys))) + "\n")
    subprocess.run(["tar", "cf", f"/mnt/user-data/outputs/{batch}-apply.tar", "-C", str(pk), "."], check=True)
    print(f"{len(rows)} pages -> /mnt/user-data/outputs/{batch}-apply.tar")


if __name__ == "__main__":
    main()
