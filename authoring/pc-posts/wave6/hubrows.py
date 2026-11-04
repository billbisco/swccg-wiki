#!/usr/bin/env python3
"""Wave 6 step 5: link new deck pages from their event hub and player Tournament Results.

python3 hubrows.py outdir   (reads outdir/plan.json; writes outdir/hubs/*.wiki + outdir/hubs.tsv, report-hubs.txt)
Hub: under the stage section, a new row is added right after the sibling deck's row (same player), with the
new deck in the Dark or Light column and "—" in the other (the 2020 TMW Finals rows already use this shape).
If the sibling row is not found, the row is appended to the first Dark/Light table of the matching stage section.
Player page: the new deck is added to that event's Tournament Results row (<br> between decks on one side).
"""
import json, re, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compare as CP   # noqa: E402


def label(title, side):
    return title.split(f" {side} ", 1)[-1]


def split_cells(row):
    body = row.split("\n", 1)[1] if row.startswith("|-") else row
    body = body.strip()
    if body.startswith("|"): body = body[1:]
    return [c.strip() for c in re.split(r"\s*\|\|\s*|\n\|\s*", body)]


def main():
    out = pathlib.Path(sys.argv[1])
    plan = [p for p in json.load(open(out / "plan.json")) if p["status"] == "built"]
    hubs = collections.defaultdict(list)
    for p in plan: hubs[p["event"]].append(p)
    (out / "hubs").mkdir(exist_ok=True)
    rep, tsv = [], []
    texts = CP.wikitext(sorted(hubs))
    hub_dates, hub_fmt = {}, {}
    for h, tx in texts.items():
        md = re.search(r"'''Dates?:'''\s*([^\n<]+)", tx or ""); hub_dates[h] = md.group(1).strip() if md else ""
        mf = re.search(r"'''(?:Environment|Format):'''\s*(\[\[[^\]]+\]\])", tx or ""); hub_fmt[h] = mf.group(1) if mf else "[[Open]]"
    for hub, ps in hubs.items():
        t = texts.get(hub, "")
        if not t:
            rep.append(f"NO-HUB {hub}: " + ", ".join(p["title"] for p in ps)); continue
        for p in ps:
            if f"[[{p['title']}|" in t or f"[[{p['title']}]]" in t: continue
            sd = p["side"]; link = f"[[{p['title']}|{label(p['title'], sd)}]]"
            # rows of all tables
            m = re.search(r"\[\[" + re.escape(p["sibling"]) + r"[|\]]", t)
            if m:
                rs = t.rfind("\n|-", 0, m.start()); re_ = t.find("\n|", m.end())
                while re_ != -1 and not (t.startswith("\n|-", re_) or t.startswith("\n|}", re_)):
                    re_ = t.find("\n|", re_ + 1)
                row = t[rs + 1:re_]
                cells = split_cells(row)
                # header of this table
                ts = t.rfind("{|", 0, rs); head = t[ts:rs]
                hm = re.search(r"\n!\s*(.*)", head)
                hcells = [h.strip() for h in re.split(r"\s*!!\s*", hm.group(1))] if hm else []
                if "Dark" in hcells and "Light" in hcells and len(cells) == len(hcells):
                    new = list(cells)
                    di, li = hcells.index("Dark"), hcells.index("Light")
                    new[di] = link if sd == "DS" else "—"; new[li] = link if sd == "LS" else "—"
                    t = t[:re_] + "\n|-\n| " + " || ".join(new) + t[re_:]
                    rep.append(f"HUB-ROW {hub} <- {p['title']}"); continue
                rep.append(f"HUB-SHAPE {hub}: row of {p['sibling']} has {len(cells)} cells vs header {hcells}")
            else:
                # append a new player row to the stage's Dark/Light table
                start = 0
                if p.get("stage"):
                    for mm in re.finditer(r"^==+\s*(.*?)\s*==+\s*$", t, re.M):
                        if p["stage"].lower() in mm.group(1).lower(): start = mm.end(); break
                tm_ = None
                for mt in re.finditer(r"\{\|[^\n]*\n(?:\|-\s*\n)?!\s*([^\n]*)", t[start:]):
                    hc = [h.strip() for h in re.split(r"\s*!!\s*", mt.group(1))]
                    if "Dark" in hc and "Light" in hc: tm_ = (start + mt.start(), hc); break
                if not tm_:
                    rep.append(f"HUB-NO-TABLE {hub}: {p['title']} needs a manual row"); continue
                ts, hc = tm_; te = t.find("\n|}", ts)
                cells = []
                for h in hc:
                    if h == "Dark": cells.append(link if sd == "DS" else "—")
                    elif h == "Light": cells.append(link if sd == "LS" else "—")
                    elif h.lower() in ("player", "name"): cells.append(f"[[{p['player']}]]")
                    else: cells.append("")
                t = t[:te] + "\n|-\n| " + " || ".join(cells) + t[te:]
                rep.append(f"HUB-NEW-ROW {hub} <- {p['title']} (check placement)")
        (out / "hubs" / (re.sub(r"[^A-Za-z0-9 ._()-]", "_", hub) + ".wiki")).write_text(t, encoding="utf-8")
        tsv.append(f"{hub}\thubs/{re.sub(r'[^A-Za-z0-9 ._()-]', '_', hub)}.wiki")
    # player pages
    players = collections.defaultdict(list)
    for p in plan:
        if p["player"]: players[p["player"]].append(p)
    ptexts = CP.wikitext(sorted(players))
    (out / "players").mkdir(exist_ok=True)
    for pl, ps in players.items():
        t = ptexts.get(pl, "")
        if not t:
            p0 = ps[0]
            dates = hub_dates.get(p0["event"], ""); fmt = hub_fmt.get(p0["event"], "[[Open]]")
            dark = "<br>".join(f"[[{q['title']}|{label(q['title'], 'DS')}]]" for q in ps if q["side"] == "DS") or "—"
            light = "<br>".join(f"[[{q['title']}|{label(q['title'], 'LS')}]]" for q in ps if q["side"] == "LS") or "—"
            src = f"[{p0['link']} {p0['post_title']}], starwarsccg.org"
            t = ("'''" + pl + "''' played the [[" + p0["event"] + "]].<ref name=\"pc-deck\">" + src + "</ref>\n\n"
                 "== Tournament Results ==\n\n{| class=\"wikitable\"\n|-\n! Date !! Event !! Format !! Finish !! Dark !! Light\n|- \n"
                 f"| {dates} || [[{p0['event']}]] || {fmt} || || {dark} || {light}\n" + "|}\n\n== See also ==\n\n"
                 f"* [[{p0['event']}]]\n* [[List of SWCCG tournaments]]\n\n== Sources ==\n\n* {src}\n\n"
                 "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n[[Category:Players]]\n"
                 f"[[Category:{p0['event'][:4]}]]\n")
            fn = re.sub(r"[^A-Za-z0-9 ._()-]", "_", pl) + ".wiki"
            (out / "players" / fn).write_text(t, encoding="utf-8"); tsv.append(f"{pl}\tplayers/{fn}")
            rep.append(f"PLAYER-STUB {pl} <- {', '.join(q['title'] for q in ps)} (check the name is not an existing player)")
            continue
        changed = False
        for p in ps:
            if p["title"] in t: continue
            m = re.search(r"\[\[" + re.escape(p["sibling"]) + r"(\|[^\]]*)?\]\]", t)
            if not m:
                lk = f"[[{p['title']}|{label(p['title'], p['side'])}]]"
                mev = re.search(r"\|[^\n]*\[\[" + re.escape(p["event"]) + r"(\|[^\]]*)?\]\][^\n]*", t)
                if mev:   # event row exists but links other decks: add to its side cell
                    row = mev.group(0); cells = row.split("||")
                    i = -1 if p["side"] == "LS" else -2
                    c = cells[i].strip()
                    cells[i] = " " + (lk if c in ("—", "-", "") else c + "<br>" + lk) + (" " if i == -2 else "")
                    t = t.replace(row, "||".join(cells), 1); changed = True
                    rep.append(f"PLAYER-ROW {pl} <- {p['title']} (event row)"); continue
                mt = re.search(r"== Tournament Results ==\s*\n\{\|[^\n]*\n(?:\|-\s*\n)?![^\n]*\n", t)
                if not mt:
                    rep.append(f"PLAYER-NO-TABLE {pl}: {p['title']} not added"); continue
                dark = lk if p["side"] == "DS" else "—"; light = lk if p["side"] == "LS" else "—"
                newrow = f"|-\n| {hub_dates.get(p['event'], '')} || [[{p['event']}]] || {hub_fmt.get(p['event'], '[[Open]]')} || || {dark} || {light}\n"
                tbl_end = t.find("\n|}", mt.end())
                ins = tbl_end + 1
                for rr in re.finditer(r"\|-\s*\n\|\s*([^\n]*)", t[mt.end():tbl_end]):
                    y = re.search(r"(19|20)\d\d", rr.group(1))
                    if y and y.group(0) < p["event"][:4]:
                        ins = mt.end() + rr.start(); break
                t = t[:ins] + newrow + t[ins:]; changed = True
                rep.append(f"PLAYER-NEW-ROW {pl} <- {p['title']}"); continue
            sib_side = " DS " if " DS " in p["sibling"] else " LS "
            link = f"[[{p['title']}|{label(p['title'], p['side'])}]]"
            if sib_side.strip() == p["side"]:
                t = t[:m.end()] + "<br>" + link + t[m.end():]; changed = True
            else:
                # put it into the other side's cell of the same row
                rs = t.rfind("\n|-", 0, m.start()); re_ = t.find("\n|-", m.end()); re2 = t.find("\n|}", m.end())
                re_ = min(x for x in (re_, re2) if x != -1)
                row = t[rs:re_]
                cells = row.split("||")
                if p["side"] == "LS":
                    last = cells[-1]
                    cells[-1] = (" " + link) if last.strip() in ("—", "-", "") else (last.rstrip() + "<br>" + link)
                else:
                    cells[-2] = (" " + link + " ") if cells[-2].strip() in ("—", "-", "") else (cells[-2].rstrip() + "<br>" + link + " ")
                t = t[:rs] + "||".join(cells) + t[re_:]; changed = True
            rep.append(f"PLAYER-ROW {pl} <- {p['title']}")
        if changed:
            fn = re.sub(r"[^A-Za-z0-9 ._()-]", "_", pl) + ".wiki"
            (out / "players" / fn).write_text(t, encoding="utf-8"); tsv.append(f"{pl}\tplayers/{fn}")
    (out / "hubs.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    (out / "report-hubs.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print(collections.Counter(r.split()[0] for r in rep))


if __name__ == "__main__":
    main()
