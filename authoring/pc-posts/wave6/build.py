#!/usr/bin/env python3
"""Wave 6 step 4: build wiki pages for MISSING PC deck posts.

python3 build.py verdicts.json pcrest.json decklists.json outdir
Writes outdir/pages/*.wiki, outdir/gemp/*.txt, outdir/apply.tsv (title<TAB>pages/file), outdir/plan.json
(per page: event hub, player, sibling page used for naming), outdir/report.txt.
Pages follow the wave-5 deck page shape (lead, Deck info, Decklist with CardLink, See also, Sources, References).
"""
import json, re, sys, pathlib, collections, html as H, urllib.parse, urllib.request, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent.parent))
import render as RD            # noqa: E402
import classify as CL          # noqa: E402
import compare as CP           # noqa: E402
import gemp_importable as gi   # noqa: E402
gi.CARD_DB = HERE.parent.parent / "gemp-data" / "card_blueprint_database.json"
gi.FORMATS_JSON = HERE.parent.parent / "gemp-data" / "swccgFormats.json"

STAGE_RX = [(r"\bday\s*(\d)\b", lambda m: f"Day {m.group(1)}"), (r"\bpods?\b", lambda m: "Pods"),
            (r"sweet 16|round of 16", lambda m: "Round of 16"), (r"elite 8|\btop 8\b", lambda m: "Top 8"),
            (r"final (?:4|four)|\btop 4\b", lambda m: "Final Four"), (r"final confrontation|\bfinals?\b", lambda m: "Finals"),
            (r"\bround (\d)\b", lambda m: f"Round {m.group(1)}"), (r"\btop (\d+)\b", lambda m: f"Top {m.group(1)}")]


def stage_of(s):
    s = CP.norm(s)
    for rx, f in STAGE_RX:
        m = re.search(rx, s)
        if m: return f(m)
    return None


def gemp_rows(cardlist):
    """(qty, GEMP title, side hint) from render()'s cardlist (resolved wiki titles; shields included)."""
    global _NK
    if _NK is None:
        import unicodedata
        _NK = {}
        for c in json.load(open(gi.CARD_DB)):
            _NK.setdefault((c.get("side"), nk(c["title"])), c["title"])
            base = re.sub(r" \([^()]*\)$", "", c["title"])     # GEMP subtitle: "BB-8 (Beebee-Ate)"
            if base != c["title"]: _NK.setdefault((c.get("side"), "BASE:" + nk(base)), c["title"])
    rows = []
    for q, ttl, raw, v, shield in cardlist:
        if not ttl: continue
        hint = "DARK" if " (Dark)" in ttl else None
        t = ttl.replace("•", "").replace("&#8226;", "")
        t = re.sub(r" \((?!V\)|AI\))[^()]*\)", "", t)   # strip wiki disambiguators, keep (V)/(AI)
        rows.append((q, t, hint))
    return rows


_NK = None


def nk(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "", t)


def gemp_xml(rows, side):
    """xml_for with a normalized-title fallback per card; raises KeyError when a card has no GEMP blueprint."""
    out = []
    for q, t, hint in rows:
        s2 = hint or side
        try:
            gi.lookup(t, s2, None); out.append((q, t, hint)); continue
        except KeyError:
            pass
        hit = _NK.get((s2, nk(t))) or _NK.get((s2, nk(t.split(" / ")[0]))) or _NK.get((s2, "BASE:" + nk(t)))
        if not hit:
            raise KeyError(f"no blueprint for {s2} {t!r}")
        out.append((q, hit, hint))
    return gi.xml_for(out, side, "all")


def info_lines(txt):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\* '''([^':]+):'''\s*(.*)$", txt, re.M)}


def main():
    ver = json.load(open(sys.argv[1])); rest = json.load(open(sys.argv[2])); titles = json.load(open(sys.argv[3]))
    out = pathlib.Path(sys.argv[4]); (out / "pages").mkdir(parents=True, exist_ok=True); (out / "gemp").mkdir(exist_ok=True)
    tset = set(titles)
    pre = {}
    for t in titles:
        m = re.match(r"(\d{4}) (.*?) (DS|LS)\b", t)
        if m: pre[t] = (m.group(1), m.group(2), m.group(3))
    plan, rep, rows, used_titles, used_files = [], [], [], set(), set()
    miss = {s: v for s, v in ver.items() if v.get("final") == "MISSING"}
    for slug, v in sorted(miss.items()):
        p = rest[slug]; sd = v["side"]; yr = v["year"]
        ptitle = H.unescape(p["title"]["rendered"])
        st = CL.canon(slug.replace("-", " ") + " " + ptitle)
        stage = stage_of(slug.replace("-", " ") + " " + ptitle)
        # player sibling pages (same event, same player, either side), via the classify rule
        sib = []
        for t, (y, prefix, s2) in pre.items():
            if y != yr: continue
            core = [x for x in CL.canon(prefix) if not CL.STAGEW.match(x) and len(x) > 1]
            if len(core) >= 3 and CL.event_player_match(core, st):
                sib.append(t)
        sib.sort(key=lambda t: (stage is not None and stage_of(t) == stage, pre[t][2] == sd), reverse=True)
        player_override = None
        if not sib:
            # event siblings: other players' pages of this event (title minus the 2-3 name words matches the post)
            evs = collections.Counter(); evpage = {}
            for t, (y, prefix, s2) in pre.items():
                if y != yr: continue
                words = prefix.split()
                for k in (2, 3):
                    if len(words) <= k: continue
                    evp = " ".join(words[:-k])
                    core = [x for x in CL.canon(evp) if not CL.STAGEW.match(x) and len(x) > 1]
                    if core and all(CL.hit(a, st) for a in core):
                        stp = stage_of(evp)
                        if stage and stp and stp != stage: continue
                        evs[evp] += 1; evpage.setdefault(evp, t)
                        break
            if not evs:
                rep.append(f"NO-SIBLING {slug} ({ptitle})"); plan.append(dict(slug=slug, status="no-sibling", post_title=ptitle)); continue
            evp = max(evs, key=lambda e: (len(e), evs[e]))
            # player name from the post title: words before DS/LS that are not event/stage/place words
            m = re.match(r"(.*?)\b(DS|LS)\b", ptitle)
            words = (m.group(1) if m else ptitle).split()
            evc = set(CL.canon(evp)) | {"day", "place", "pods", "top", "round", "of", "final", "four", "sweet", "elite"}
            name = [w for w in words if not re.match(r"^\d", w) and CL.canon(w) and not set(CL.canon(w)) <= evc
                    and not re.match(r"(?i)^(\d+(st|nd|rd|th))$", w)]
            pname = " ".join(name[-3:]) if len(name) > 3 else " ".join(name)
            if not pname:
                rep.append(f"NO-PLAYER-NAME {slug} ({ptitle})"); plan.append(dict(slug=slug, status="no-player", post_title=ptitle)); continue
            player_override = pname
            fake = f"{yr} {evp} {pname} {sd} x"
            sib = [evpage[evp]]
            pre_override = f"{evp} {pname}"
            rep.append(f"EVENT-SIBLING {slug}: prefix '{yr} {evp}', player '{pname}' (check the name)")
        else:
            pre_override = None
        s0 = sib[0]
        sibtxt = CP.wikitext(sib[:8])
        inf = info_lines(sibtxt[s0])
        for t2 in sib[1:8]:
            i2 = info_lines(sibtxt[t2])
            for k in ("Player", "Event", "Format"):
                if not inf.get(k) and i2.get(k): inf[k] = i2[k]
        if not inf.get("Event") or (not inf.get("Player") and not player_override):
            rep.append(f"NO-EVENT-OR-PLAYER {slug}: siblings {sib[:3]} lack Deck info Event/Player")
            plan.append(dict(slug=slug, status="no-event", post_title=ptitle, sibling=s0)); continue
        prefix = pre_override or pre[s0][1]
        if not stage:
            stage = stage_of(prefix)
        if stage and stage_of(prefix) != stage:
            old = stage_of(prefix)
            if old:
                prefix = re.sub(re.escape(old), stage, prefix, count=1, flags=re.I)
            else:
                rep.append(f"STAGE-NOT-IN-TITLE {slug}: post stage {stage}, sibling {s0}")
        r = RD.render(pathlib.Path(HERE / "posts_html" / f"{slug}.html"), sd)
        obj = r["objective"]["title"].split(" / ")[0] if r["objective"] else None
        deck = obj or (r["start_loc"]["title"] if r.get("start_loc") else None) or (r["start_int"]["title"] if r["start_int"] else None)
        if not deck:
            m = re.search(r"\b(?:DS|LS)\b\s*(.*)$", ptitle); deck = (m.group(1).strip() if m else "") or "Deck"
        title = f"{yr} {prefix} {sd} {deck}"
        n = 2
        base = title
        while title in tset or title in used_titles:
            title = f"{base} ({n})"; n += 1
        used_titles.add(title)
        side_w = "Dark" if sd == "DS" else "Light"
        player = f"[[{player_override}]]" if player_override else inf.get("Player", "")
        event = inf.get("Event", "")
        fmt = inf.get("Format", "[[Open]]")
        def cl(i):
            return f"{{{{CardLink|{i['title']}|{i['image']}}}}}" if i.get("image") else f"[[{i['title']}]]"
        first = r["objective"] or r.get("start_loc")
        start_block = "* '''Starting Card:''' " + (cl(first) if first else "—") + "\n"
        if not r["objective"] and r["start_int"]:
            start_block += "* '''Starting Interrupt:''' " + cl(r["start_int"]) + "\n"
        pname = re.sub(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), player)
        ename = re.sub(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(1), event)
        link = (p.get("link") or f"https://www.starwarsccg.org/{slug}/").replace("starwarsccg.org/wp/", "starwarsccg.org/")
        page = (f"'''{title}''' was the {side_w} Side constructed list played by {player} at {event}"
                + (f" ({stage})" if stage else "") + ".\n\n== Deck info ==\n\n"
                f"* '''Player:''' {player}\n* '''Event:''' {event}\n" + (f"* '''Stage:''' {stage}\n" if stage else "")
                + f"* '''Format:''' {fmt}\n* '''Side:''' [[{side_w}]]\n" + start_block + "\n"
                "== Decklist ==\n\n" + r["body"] + "\n== See also ==\n"
                f"* {event}\n" + ("" if player_override else f"* [[{s0}]]\n") + "\n== Sources ==\n\n"
                f"* [{link} {CP.H.escape(ptitle) if False else ptitle.replace('[', '(').replace(']', ')')}], starwarsccg.org (deck post).\n\n"
                "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n"
                f"[[Category:Decklists]]\n[[Category:{yr}]]\n")
        fn = re.sub(r"[^A-Za-z0-9 ._()-]", "_", title) + ".wiki"
        (out / "pages" / fn).write_text(page, encoding="utf-8")
        # GEMP file when every main-deck card resolves
        gemp = None
        if not any(c[1] is None and not c[4] for c in r["cardlist"]):
            try:
                grows = gemp_rows(r["cardlist"])
                xml, _notes = gemp_xml(grows, "DARK" if sd == "DS" else "LIGHT")
                tok = re.sub(r"[^A-Za-z0-9]", "", ename.split()[1] if len(ename.split()) > 1 else "PC")[:8]
                base = gi.safe_deck_filename(gi.deck_name("Open", deck.split(" / ")[0][:28], pname or player_override or "Player", sd, yr, tok))
                g = {"xml": xml, "name": base}
                gname = base + ".txt"; k = 2
                while gname.lower() in used_files:
                    gname = base[:36] + f" {k}.txt"; k += 1
                used_files.add(gname.lower())
                (out / "gemp" / gname).write_text(g["xml"], encoding="utf-8", newline="\n")
                page = page.replace(start_block, start_block + gi.wiki_download_line(gname) + "\n", 1)
                (out / "pages" / fn).write_text(page, encoding="utf-8")
                gemp = gname
            except Exception as e:
                rep.append(f"NOGEMP {title}: {str(e)[:120]}")
        rows.append(f"{title}\tpages/{fn}")
        plan.append(dict(slug=slug, status="built", title=title, sibling=s0, player=pname, event=ename, stage=stage, side=sd,
                         deck=deck, gemp=gemp, total=r["total"], unresolved=r["unresolved"], post_title=ptitle, link=link))
        rep.append(f"OK {title} <- {ptitle} ({r['total']}+{r['shields']}) sib={s0}" + (f" UNRES {r['unresolved']}" if r["unresolved"] else ""))
    (out / "apply.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    json.dump(plan, open(out / "plan.json", "w"), indent=1, ensure_ascii=False)
    (out / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print(len(rows), "pages;", collections.Counter(x["status"] for x in plan))


if __name__ == "__main__":
    main()
