"""People, event hubs and the tournament list for tournament-report batches (Claude 2026-10-24).

Bill 2026-10-24: every tournament a report mentions gets a page and a row on [[List of SWCCG tournaments]];
every named player gets an article with what they played (small-world rule); reports' new facts update
existing event tables. Used by tr_build.py.
"""
import datetime as dt
import re

import decktech_batch as b
import tr_build as T

MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                      "September", "October", "November", "December"], 1)}


def date_key(s: str) -> str:
    """Sort key YYYY-MM-DD from '31 July 1999', 'July 1999', '21–22 November 1998', '1999', '2000-04-29'."""
    s = re.sub(r"<ref.*", "", s or "")
    if re.match(r"\d{4}-\d\d", s):
        return s[:10]
    y = re.findall(r"\b(19\d\d|20\d\d)\b", s)
    if not y:
        return ""
    mo = [MONTHS[m] for m in re.findall("|".join(MONTHS), s)]
    d = re.findall(r"\b(\d{1,2})(?:[–-]\d{1,2})?\s+(?:" + "|".join(MONTHS) + ")", s)
    return f"{y[-1]}-{(mo[-1] if mo else 0):02d}-{int(d[-1]) if d else 0:02d}"


def full_name(n: str | None) -> bool:
    """A full name gets a person page. Initials or abbreviated surnames ("Kevin W.", "Jeroen v. Beers",
    "v/d Meer") are not full names (Claude 2026-10-25)."""
    if not n or " " not in n.strip() or re.search(r"[?()/]|surname|unknown|not given|unnamed", n, re.I):
        return False
    parts = n.split()
    return not any(re.fullmatch(r"[A-Za-z]\.?", p) or p.endswith(".") and len(p) <= 3 for p in parts[1:])


def events(d: dict) -> list[dict]:
    keys = ("event", "event_status", "event_desc", "event_date", "event_site", "event_type", "event_format",
            "event_winner", "players", "author_finish", "author_record", "author_points", "games", "other_results",
            "summary", "author_played")
    main = {k: d.get(k) for k in keys}
    main["decks"] = d.get("decks") or []
    main["parent"] = d.get("event_parent")
    return [main] + [dict(se, decks=se.get("decks") or [], parent=se["parent"] if "parent" in se else d.get("event"))
                     for se in d.get("side_events") or []]


def named(e: dict) -> bool:
    return bool(e.get("event")) and e.get("event_status") != "unnamed"


def ev_link(e: dict) -> str:
    return f"[[{e['event']}]]" if named(e) else (e.get("event_desc") or "a tournament")


def hub_format(text: str | None) -> str | None:
    m = re.search(r"'''Format:'''\s*\[\[([^\]|]+)", text or "")
    return m.group(1) if m else None


def other_side(s: str | None) -> str | None:
    return {"Dark": "Light", "Light": "Dark"}.get(s or "")


def participants(d: dict) -> dict[str, list[dict]]:
    """name -> entries {e, finish, dark:set, light:set, author:bool}."""
    out: dict[str, dict[int, dict]] = {}

    def entry(name, i, e):
        return out.setdefault(name, {}).setdefault(i, {"e": e, "finish": "", "dark": [], "light": [], "author": False})

    who = T.person(d)
    for i, e in enumerate(events(d)):
        if who and e.get("author_played") is not False:  # e.g. a judge's report (Claude 2026-10-25)
            x = entry(who, i, e)
            x["author"] = True
            x["finish"] = e.get("author_finish") or (f"{e['author_record']} record" if e.get("author_record") else "")
            for k in e.get("decks") or []:
                desc = f"[[{k['deck_page']}|{k['description']}]]" if k.get("deck_page") else T.dlink(k.get("description"), k.get("objective"))
                if k.get("side") in ("Dark", "Light") and desc and desc not in x[k["side"].lower()]:
                    x[k["side"].lower()].append(desc)
            for g in e.get("games") or []:
                if g.get("author_side") in ("Dark", "Light") and g.get("author_deck") and not e.get("decks"):
                    dd = T.dlink(g["author_deck"], g.get("author_objective"))
                    if dd not in x[g["author_side"].lower()]:
                        x[g["author_side"].lower()].append(dd)
        for g in e.get("games") or []:
            n = g.get("opponent")
            if not full_name(n) or n == who:
                continue
            x = entry(n, i, e)
            side = g.get("opponent_side") or other_side(g.get("author_side"))
            dd = T.dlink(g.get("opponent_deck"), g.get("opponent_objective"))
            if side and dd and dd not in x[side.lower()]:
                x[side.lower()].append(dd)
        for r in e.get("other_results") or []:
            if full_name(r.get("player")) and r["player"] != who:
                entry(r["player"], i, e)["finish"] = r.get("finish") or ""
    return {n: list(v.values()) for n, v in out.items()}


def result_row(d: dict, x: dict, fmt: str | None) -> str:
    e = x["e"]
    ref = T.ref(d)
    return (f"| {T.event_long(e) or ''} || {ev_link(e)} || {f'[[{fmt}]]' if fmt else ''} || {x['finish']}{ref} || "
            f"{', '.join(x['dark'])} || {', '.join(x['light'])}")


RESULTS_HEAD = '{| class="wikitable"\n|-\n! Date !! Event !! Format !! Finish !! Dark !! Light'


LOG: list[str] = []


def add_result_rows(text: str, rows: list[tuple[str, str]], who: str = "") -> str:
    """rows = [(event_marker, row)]; skip events already in the table; newest first.
    Every skipped or impossible row is logged: a silent miss left player pages empty (Bill 2026-10-24)."""
    m = re.search(r"^== Tournament [Rr]esults ==\s*$", text, re.M)
    if not m:
        first = re.search(r"^==[^=]", text, re.M)
        k = first.start() if first else len(text)
        text = text[:k] + "== Tournament Results ==\n\n" + RESULTS_HEAD + "\n|}\n\n" + text[k:]
        m = re.search(r"^== Tournament [Rr]esults ==\s*$", text, re.M)
    t0 = text.find("{|", m.end())
    t1 = text.find("\n|}", t0)
    table = text[t0:t1]
    pieces = table.split("\n|-\n")
    h = next((i for i, p in enumerate(pieces) if p.lstrip().startswith("!") or "\n!" in p), None)
    if h is None:
        LOG.append(f"{who}: Tournament Results table has no header row; rows NOT added: {[r for _, r in rows]}")
        return text
    head, rws = pieces[:h + 1], pieces[h + 1:]
    hl = next(l for l in head[-1].split("\n") if l.lstrip().startswith("!"))
    cols = [re.sub(r".*\|", "", c).strip().lower() for c in hl.lstrip().lstrip("!").split("!!")]
    std = ["date", "event", "format", "finish", "dark", "light"]
    if "event" not in cols:
        LOG.append(f"{who}: Tournament Results header has no Event column; rows NOT added: {[r for _, r in rows]}")
        return text
    if cols != std:  # map our Date/Event/Format/Finish/Dark/Light row onto this page's own columns
        def remap(row):
            v = dict(zip(std, [c.strip() for c in row.lstrip()[1:].split("||")]))
            return "| " + " || ".join(v.get(c, "") for c in cols)
        rows = [(m, remap(r)) for m, r in rows]
    for marker, row in rows:
        if marker and marker in table:
            i = next((i for i, r in enumerate(rws) if marker in r), None)
            filled = []
            if i is not None:
                old = [c for c in rws[i].lstrip()[1:].split("||")]
                nw = [c.strip() for c in row.lstrip()[1:].split("||")]
                rn = re.search(r'<ref name="([^"]+)"', row)
                short = f'<ref name="{rn.group(1)}" />' if rn else ""
                if len(old) == 6 and len(nw) == 6 and cols == std:
                    for j, lab in ((4, "Dark"), (5, "Light")):
                        if old[j].strip() in ("", "—") and nw[j]:
                            old[j] = f" {nw[j]}{short} "
                            filled.append(lab)
                    if old[3].strip() in ("",) and re.sub(r"<ref.*", "", nw[3]).strip():
                        old[3] = f" {nw[3]} "
                        filled.append("Finish")
                    rws[i] = "|" + "||".join(old)
            LOG.append(f"{who}: already has a row for {marker}]]" + (f"; filled {', '.join(filled)} from the report" if filled else "; nothing new"))
            continue
        k = date_key(row.split("||")[0].lstrip("| "))
        pos = len(rws)
        for i, r in enumerate(rws):
            if date_key(r.split("||")[0].lstrip("| ")) < k:
                pos = i
                break
        rws.insert(pos, row)
    new = "\n|-\n".join(head + rws)
    return dedupe_refs(text[:t0] + new + text[t1:])


def person_text(name: str, ds_entries: list[tuple[dict, dict]], cur: str | None, fmt_of) -> str:
    rows = [(f"[[{x['e']['event']}" if named(x["e"]) else f"{T.event_long(x['e'])} || {ev_link(x['e'])}",
             result_row(d, x, fmt_of(x["e"]))) for d, x in ds_entries]
    authored = [d for d, x in ds_entries if x["author"]]
    if cur:  # an event that has since been named replaces its old description row / bullet
        for d, x in ds_entries:
            desc = x["e"].get("event_desc")
            if named(x["e"]) and desc:
                cur = re.sub(r"\n\|-\n\|[^\n]*\|\| " + re.escape(desc) + r" \|\|[^\n]*", "", cur)
                cur = re.sub(r"^(\* \[\[" + re.escape(T.page_title(d)) + r"\]\] — )" + re.escape(desc), r"\g<1>[[" + x["e"]["event"].replace("\\", "") + "]]", cur, flags=re.M)
    if cur is None:
        d, x = ds_entries[0]
        if x["author"]:
            handle = re.search(r'"([^"]+)"', d["byline"])
            h = f" (DeckTech handle '''{handle.group(1)}''')" if handle and handle.group(1) != name else ""
            lead = f"'''{name}'''{h} is a Star Wars CCG player who wrote a tournament report for {T.SOURCES[d['source']][1]}."
        else:
            played = " and ".join(x["dark"] + x["light"])
            when = T.event_long(x["e"])
            verb = (f"finished {x['finish']} at" if re.match(r"\d+(st|nd|rd|th)|top|finalist", x["finish"] or "", re.I)
                    else "played at")
            lead = (f"'''{name}''' is a Star Wars CCG player who {verb} {ev_link(x['e'])}"
                    + (((" on " if re.match(r"\d", when) else " in ") + when) if when else "")
                    + (f" with {played}" if played else "")
                    + f", according to {T.person(d) or d['byline']}'s tournament report.{T.ref(d)}")
        years = sorted({(x["e"].get("event_date") or T.iso(d["date"]))[:4] for d, x in ds_entries})
        cur = (lead + "\n\n" + RESULTS_HEAD + "\n|}\n\n== See also ==\n\n* [[List of SWCCG tournaments]]\n* [[Tournament reports]]\n\n"
               "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n[[Category:People]]\n[[Category:Players]]\n"
               + "\n".join(f"[[Category:{y}]]" for y in years) + "\n")
        cur = cur.replace(RESULTS_HEAD, "== Tournament Results ==\n\n" + RESULTS_HEAD, 1)
    cur = add_result_rows(cur, rows, name)
    if authored:
        cur = T.add_section(cur, "Tournament reports", [T.report_bullet(d) for d in authored])
    return cur


def results_table_span(text: str):
    for h in ("== Results ==", "== Final standings ==", "== Standings ==", "== Published lists =="):
        k = text.find(h)
        if k >= 0:
            t0 = text.find("{|", k)
            nxt = text.find("\n== ", k + 5)
            if t0 >= 0 and (nxt < 0 or t0 < nxt):
                return t0, text.find("\n|}", t0)
    return None


def hub_add_participants(text: str, d: dict, e: dict, log: list) -> str:
    span = results_table_span(text)
    if not span:  # no single results table: list people the hub doesn't link yet (Claude 2026-10-25)
        rp = f"[[{T.page_title(d)}]]"
        who = T.person(d)
        ppl = ([(who, e.get("author_finish") or "")] if who and e.get("author_played") is not False else [])
        ppl += [(r["player"], r.get("finish") or "") for r in e.get("other_results") or [] if full_name(r.get("player"))]
        ppl += [(g["opponent"], "") for g in e.get("games") or [] if full_name(g.get("opponent"))]
        add, seen = [], set()
        for n, f in ppl:
            if n in seen or f"[[{n}]]" in text or f"[[{n}|" in text:
                continue
            seen.add(n)
            add.append(f"* [[{n}]] — {f + ', ' if f else ''}named in {rp}<ref name=\"tr-{d['id']}\" />")
        if add:
            if f'<ref name="tr-{d["id"]}">' not in text:
                add[0] = add[0].replace(f'<ref name="tr-{d["id"]}" />', T.ref(d), 1)
            text = T.add_section(text, "Players named in tournament reports", add,
                                 "Players these reports name who are not in the event's results above.")
        return text
    t0, t1 = span
    table = text[t0:t1]
    hdr = next((l for l in table.split("\n") if l.startswith("!")), "")
    ncol = hdr.count("!!") + 1
    who = T.person(d)
    ppl = []
    if who:
        ppl.append((who, e.get("author_finish") or (f"{e['author_record']} record" if e.get("author_record") else "")))
    for r in e.get("other_results") or []:
        if full_name(r.get("player")):
            ppl.append((r["player"], r.get("finish") or ""))
    for g in e.get("games") or []:
        if full_name(g.get("opponent")):
            ppl.append((g["opponent"], ""))
    seen, add, named_only = set(), [], []
    for n, f in ppl:
        if n in seen or f"[[{n}]]" in table or f"[[{n}|" in table:
            continue
        seen.add(n)
        m = re.search(rf"\|\| {re.escape(n)}(?=[ <\n(]|$)", table)
        if m:  # listed as plain text: link it now that the person has a page
            new_table = table[:m.start()] + f"|| [[{n}]]" + table[m.end():]
            text = text[:t0] + new_table + text[t1:]
            t1 += len(new_table) - len(table)
            table = new_table
            continue
        if not f and "Results below come from" not in text:
            if f"[[{n}]]" in text or f"[[{n}|" in text:
                continue
            # a sourced standings table: an opponent with no finish goes in a list below it (Claude 2026-10-25)
            named_only.append(f"* [[{n}]] — named in [[{T.page_title(d)}]]<ref name=\"tr-{d['id']}\" />")
            continue
        # map onto the table's own columns by header name (Claude 2026-10-25: a Player-first table got Finish first)
        heads = [h.strip().lower() for h in re.split(r"!!|\|\|", hdr.lstrip("!").strip())]
        cells = ["—"] * max(ncol, 2)
        pi = next((i for i, h in enumerate(heads) if re.search(r"player|name|team", h)), 1)
        fi = next((i for i, h in enumerate(heads) if re.search(r"finish|place|rank|result|#|pos", h)), 0 if pi != 0 else 1)
        cells[pi] = f"[[{n}]]<ref name=\"tr-{d['id']}\" />"
        cells[fi] = f or ""
        add.append("| " + " || ".join(cells))
    if named_only:
        if f'<ref name="tr-{d["id"]}">' not in text and not add:
            named_only[0] = named_only[0].replace(f'<ref name="tr-{d["id"]}" />', T.ref(d), 1)
        text = T.add_section(text, "Players named in tournament reports", named_only,
                             "Players these reports name who are not in the event's results above.")
        t0 = text.find(table)
        t1 = t0 + len(table)
    if not add:
        return text
    if f'<ref name="tr-{d["id"]}">' not in text:
        add[0] = add[0].replace(f'<ref name="tr-{d["id"]}" />', T.ref(d), 1)
    return text[:t1] + "".join("\n|-\n" + a for a in add) + text[t1:]


def hub_updates(text: str, d: dict, ups: list, log: list) -> str:
    lab = {"players": "Players", "date": "Date", "site": "Site"}
    for u in ups:
        if u.get("field") == "winner":  # fill an Unknown winner (Claude 2026-10-25)
            m0 = re.search(r"^\* '''Winner:'''\s*(Unknown|—|)\s*$", text, re.M)
            val = str(u["value"])
            link = f"[[{val}]]" if full_name(val) else val
            if m0:
                text = text[:m0.start()] + f"* '''Winner:''' {link}<ref name=\"tr-{d['id']}\" />" + text[m0.end():]
                text = text.replace(" The winner is unknown.", f" {link} won it.", 1)
                log.append(f"{u['event']}: Winner set to {val} from the report")
            else:
                log.append(f"{u['event']}: has a Winner already; report says {val}")
            continue
        f = lab.get(u.get("field"))
        if not f:
            continue
        m0 = re.search(rf"^\* '''{f}s?:'''(.*)$", text, re.M)
        if m0:
            cur = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", m0.group(1)).strip()
            val = str(u["value"])
            ref = f"<ref name=\"tr-{d['id']}\" />"
            # a vaguer existing value is made precise; a site is added when the hub doesn't name it (Claude 2026-10-25)
            if (f == "Date" and re.fullmatch(r"(\w+ )?\d{4}", cur) and cur.split()[-1] in val and val != cur
                    and (len(cur.split()) == 1 or cur.split()[0] in val)):
                text = text[:m0.start(1)] + f" {val}{ref}" + text[m0.end(1):]
                log.append(f"{u['event']}: Date {cur!r} -> {val!r} from the report")
            elif f == "Site" and val.split(",")[0].split()[0].lower() not in cur.lower():
                text = text[:m0.end(1)] + f"; {val}{ref}" + text[m0.end(1):]
                log.append(f"{u['event']}: Site {cur!r} + {val!r} from the report")
            else:
                log.append(f"{u['event']}: has {f} already ({cur}); report says {val}")
            continue
        m = list(re.finditer(r"^\* '''[^']+:'''.*$", text, re.M))
        line = f"* '''{f}:''' {u['value']}<ref name=\"tr-{d['id']}\" />"
        if m:
            text = text[:m[-1].end()] + "\n" + line + text[m[-1].end():]
        else:
            log.append(f"{u['event']}: no infobox bullets; {f} {u['value']} not added")
    return text


def hub_discrepancies(text: str, d: dict, items: list) -> str:
    bl = [f"* {x['text']}<ref name=\"tr-{d['id']}\" />" for x in items]
    return T.add_section(text, "Discrepancies", bl,
                         "Where a source disagrees with the record on this page, the page keeps the record and notes the difference here.")


def ensure_ref(text: str, d: dict) -> str:
    """The first use of tr-<id> on a page must carry the full ref."""
    short = f'<ref name="tr-{d["id"]}" />'
    if short in text and f'<ref name="tr-{d["id"]}">' not in text:
        text = text.replace(short, T.ref(d), 1)
    return text


def event_bullet(d: dict, e: dict) -> str:
    who = T.person(d)
    bits = [f"by [[{who}]]" if who else f"by {d['byline']}"]
    bits += [v for v in (e.get("author_finish"), e.get("author_record")) if v]
    return f"* [[{T.page_title(d)}]] — " + ", ".join(bits)


def new_hub(e: dict, d: dict) -> str:
    rows = []
    who = T.person(d)
    if who:
        rows.append((e.get("author_finish") or (f"{e['author_record']} record" if e.get("author_record") else ""), f"[[{who}]]"))
    for r in e.get("other_results") or []:
        rows.append((r.get("finish") or "", f"[[{r['player']}]]" if full_name(r.get("player")) else r.get("player")))
    for g in e.get("games") or []:
        if full_name(g.get("opponent")) and all(g["opponent"] not in p for _, p in rows):
            rows.append(("", f"[[{g['opponent']}]]"))
    order = lambda f: (0, int(re.match(r"\d+", f).group())) if re.match(r"\d+(st|nd|rd|th)", f or "") else (1, 0)
    rows.sort(key=lambda r: order(r[0]))
    tab = "\n".join(f"|-\n| {f} || {p}<ref name=\"tr-{d['id']}\" />" for f, p in rows)
    when = T.event_long(e)
    site = e.get("event_site")
    typ = (e.get("event_type") or "tournament").lower() if e.get("event_type") not in ("DPC", "Grand Slam") else e["event_type"]
    if typ in ("local", "local tournament", "store"):
        typ = "local tournament"
    lead = f"'''{e['event']}''' was a Star Wars CCG {typ}" + (f" held in {site}" if site else "") + (f" on {when}" if re.match(r"\d", when or "") else (f" in {when}" if when else "")) + "."
    if e.get("event_winner"):
        lead += f" [[{e['event_winner']}]] won it." if full_name(e["event_winner"]) else f" {e['event_winner']} won it."
    lead += f" It is known from {who or d['byline']}'s tournament report.{T.ref(d)}"
    if e.get("parent"):
        lead += f" It was played alongside the [[{e['parent']}]]."
    info = [f"* '''Date:''' {when}" if when else None, f"* '''Site:''' {site}" if site else None,
            f"* '''Format:''' [[{e['event_format']}]]" if e.get("event_format") else None,
            f"* '''Players:''' {e['players']}" if e.get("players") else None,
            (f"* '''Winner:''' " + (f"[[{e['event_winner']}]]" if full_name(e.get("event_winner")) else e["event_winner"]))
            if e.get("event_winner") else None]  # no empty Winner line (Claude 2026-10-25)
    year = (e.get("event_date") or "")[:4]
    see = ([f"* [[{e['parent']}]]"] if e.get("parent") else []) + ["* [[List of SWCCG tournaments]]", "* [[Tournament reports]]"]
    return (lead + "\n\n" + "\n".join(x for x in info if x) + "\n\n== Results ==\n\n"
            "Results below come from players' tournament reports (each row cites its report).\n\n"
            '{| class="wikitable"\n! Finish !! Player\n' + tab + "\n|}\n\n== Tournament reports ==\n\nPlayers' own reports from this event.\n\n"
            + event_bullet(d, e) + "\n\n== See also ==\n\n" + "\n".join(see) + "\n\n== References ==\n<references />\n\n"
            "[[Category:Tournaments]]\n" + (f"[[Category:{year}]]\n" if year else ""))


def list_insert(L: str, e: dict) -> str:
    if f"[[{e['event']}]]" in L or f"[[{e['event']}|" in L:
        return L
    y = (e.get("event_date") or "")[:4]
    tag = (e.get("event_date") or "")[:7]
    sec = re.search(rf"^== {y} ==\s*$", L, re.M)
    if not sec and y and int(y) <= 2001:
        sec = re.search(r"^== Decipher-era regionals and opens ==\s*$", L, re.M)
    if not sec:
        raise SystemExit(f"List has no == {y} == section for {e['event']}")
    t0 = L.find("{|", sec.end())
    t1 = L.find("\n|}", t0)
    tbl = L[t0:t1]
    parts = tbl.split("\n|-\n")
    win = (f"[[{e['event_winner']}]]" if full_name(e.get("event_winner")) else (e.get("event_winner") or ""))
    row = (f"| {tag} || [[{e['event']}]] || {T.event_long(e)} || {e.get('event_site') or ''} || "
           f"{'[[' + e['event_format'] + ']]' if e.get('event_format') else ''} || {win}")
    k = (e.get("event_date") or "") + "-99"
    pos = len(parts)
    for i, p in enumerate(parts[1:], 1):
        c = p.split("||")
        if len(c) < 3:
            continue
        pk = date_key(c[2])
        if not pk or pk.endswith("-00-00"):
            continue  # year-only rows don't fix a position
        if pk < k:
            pos = i
            break
    parts.insert(pos, row)
    return L[:t0] + "\n|-\n".join(parts) + L[t1:]


def hub_people(text: str) -> list:
    """(person, cells) for each results row whose player cell links a person; cells[-1] is a dict of
    {column name: cell} built from the table header."""
    span = results_table_span(text)
    if not span:
        return []
    tbl = text[span[0]:span[1]]
    hdr = next((l for l in tbl.split("\n") if l.startswith("!")), "")
    cols = [re.sub(r".*\|", "", c).strip().lower() for c in hdr.lstrip("!").split("!!")]
    out = []
    for r in tbl.split("\n|-\n"):
        r = r.strip()
        if not r.startswith("|") or r.startswith("|+") or r.startswith("{|"):
            continue
        cells = [c.strip() for c in r[1:].split("||")]
        pi = next((i for i, c in enumerate(cols) if c in ("player", "name")), 1)
        if len(cells) <= pi:
            continue
        m = re.match(r"(?:'+)?\[\[([^\]|#]+)", cells[pi])
        if m and not re.match(r"\d{4} ", m.group(1)):
            out.append((m.group(1).strip(), cells + [dict(zip(cols, cells))]))
    return out


def section_ref(hub: str, span_start: int) -> str:
    """First reference defined in the results section, for rows with no ref of their own."""
    h = hub.rfind("\n==", 0, span_start)
    e = hub.find("\n== ", span_start)
    sec = hub[h:e if e > 0 else len(hub)]
    m = re.search(r'<ref name="([^"]+)"', sec)
    if not m:
        return ""
    full = re.search(r'<ref name="' + re.escape(m.group(1)) + r'">.*?</ref>', hub, re.S)
    return full.group(0) if full else ""


def row_from_hub(hub: str, ev: str, cells: list) -> str:
    """A person-page Tournament Results row built from an event page's results row, reusing its refs.
    Columns are mapped by the hub's header names; returns '' when no source can be cited."""
    col = cells[-1] if cells and isinstance(cells[-1], dict) else {}
    plain = [c for c in cells if isinstance(c, str)]

    def defs(cell):
        out = ""
        for name in re.findall(r'<ref name="([^"]+)"', cell):
            full = re.search(r'<ref name="' + re.escape(name) + r'">.*?</ref>', hub, re.S)
            out += full.group(0) if full else f'<ref name="{name}" />'
        return out
    date = re.search(r"^\* '''Dates?:'''\s*(.+)$", hub, re.M)
    date = re.sub(r"<ref.*", "", date.group(1)).strip() if date else ""
    fmt = hub_format(hub)
    fin = next((v for k, v in col.items() if k in ("finish", "place", "rank", "#", "position")), plain[0] if not col else "")
    finish = re.sub(r"<ref.*?(?:/>|</ref>)", "", fin).strip()
    refs = defs(" ".join(plain))
    if not refs:
        span = results_table_span(hub)
        refs = section_ref(hub, span[0]) if span else ""
    if not refs:  # the event page's first source (its lead citation)
        m = re.search(r'<ref name="[^"]+">.*?</ref>', hub, re.S)
        refs = m.group(0) if m else ""
    if not refs:
        return ""
    dark = col.get("dark", "")
    light = col.get("light", "")
    dark, light = ("" if re.sub(r"<ref.*", "", x).strip() in ("—", "") else x for x in (dark, light))
    fl = f"[[{fmt}]]" if fmt else ""
    return f"| {date} || [[{ev}]] || {fl} || {finish}{refs} || {dark} || {light}"


def person_results_table(text: str) -> str:
    """The person's Tournament Results table text ('' if none). A link elsewhere on the page (See also, a
    Tournament reports bullet) does not count as listing the event (Bill 2026-10-24 miss: Andy McClure)."""
    m = re.search(r"^== Tournament [Rr]esults ==\s*$", text, re.M)
    if not m:
        return ""
    t0 = text.find("{|", m.end())
    nxt = re.search(r"^==[^=]", text[m.end():], re.M)
    if t0 < 0 or (nxt and t0 > m.end() + nxt.start()):
        return ""
    return text[t0:text.find("\n|}", t0)]


def dedupe_refs(text: str) -> str:
    """Keep the first full definition of each named ref; later identical definitions become <ref name="x" />."""
    seen = set()

    def rep(m):
        if m.group(1) in seen:
            return f'<ref name="{m.group(1)}" />'
        seen.add(m.group(1))
        return m.group(0)
    return re.sub(r'<ref name="([^"]+)">.*?</ref>', rep, text, flags=re.S)


def prune_named(text: str) -> str:
    """Drop 'Players named in tournament reports' bullets for people the page now lists elsewhere,
    and the section itself when it is left empty (Claude 2026-10-25)."""
    m = re.search(r"^== Players named in tournament reports ==\s*$", text, re.M)
    if not m:
        return text
    n = re.search(r"^==[^=]", text[m.end():], re.M)
    k = m.end() + n.start() if n else len(text)
    sec, rest = text[m.end():k], text[:m.start()] + text[k:]
    keep = []
    for line in sec.split("\n"):
        p = re.match(r"\* \[\[([^\]|]+)\]\]", line)
        if p and (f"[[{p.group(1)}]]" in rest or f"[[{p.group(1)}|" in rest):
            continue
        keep.append(line)
    if not any(l.startswith("* ") for l in keep):
        return text[:m.start()] + text[k:].lstrip("\n")
    return text[:m.end()] + "\n".join(keep) + text[k:]
