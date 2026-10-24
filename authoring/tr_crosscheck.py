#!/usr/bin/env python3
"""Both-ways check (Bill 2026-10-24): every person linked in an event page's results table must list that event
in their own Tournament Results table. Audits every event linked from [[List of SWCCG tournaments]].
  python3 tr_crosscheck.py [--build BATCH]   (--build writes a package that adds the missing rows)"""
import json, re, sys, urllib.parse, urllib.request
import tr_world as W

API = "https://wiki.swccg.com/api.php"


def texts(titles):
    out = {}
    for i in range(0, len(titles), 50):
        q = dict(action="query", prop="revisions", rvprop="content", rvslots="main", titles="|".join(titles[i:i + 50]),
                 redirects="1", format="json", formatversion="2")
        r = json.load(urllib.request.urlopen(API, urllib.parse.urlencode(q).encode(), timeout=120))
        red = {x["from"]: x["to"] for x in r["query"].get("redirects", [])}
        got = {p["title"]: p["revisions"][0]["slots"]["main"]["content"] for p in r["query"]["pages"] if "revisions" in p}
        for t in titles[i:i + 50]:
            out[t] = got.get(red.get(t, t))
            if t in red:
                out[t + "\0redirect"] = red[t]
    return out


L = texts(["List of SWCCG tournaments"])["List of SWCCG tournaments"]
events = sorted({m.split("|")[0].strip() for m in re.findall(r"^\| [^\n]*?\|\| \[\[([^\]]+)\]\]", L, re.M)})
H = texts(events)
miss, people = [], set()
pairs = []
for ev in events:
    if not H.get(ev):
        continue
    for n, cells in W.hub_people(H[ev]):
        pairs.append((ev, n, cells))
        people.add(n)
P = texts(sorted(people))
for ev, n, cells in pairs:
    t = P.get(n)
    if t is None:
        miss.append((ev, n, "no page"))
        continue
    tbls = "".join(re.findall(r"\{\|.*?\n\|\}", t, re.S))  # any table (Tournament Results, Retro League, ...)
    if f"[[{ev}]]" not in tbls and f"[[{ev}|" not in tbls:
        miss.append((ev, n, "redirect->" + P.get(n + "\0redirect") if P.get(n + "\0redirect") else "missing row"))
print(f"{len(events)} events, {len(pairs)} linked results rows, {len(miss)} misses")
for m in miss:
    print("\t".join(m))
json.dump([list(m) for m in miss], open("/tmp/claude-0/crosscheck.json", "w"))
if "--build" in sys.argv:
    import datetime as dt, shutil, subprocess
    from pathlib import Path
    B = sys.argv[sys.argv.index("--build") + 1]
    pk = Path(f"/tmp/claude-0/{B}pkg"); shutil.rmtree(pk, ignore_errors=True); (pk / "pages").mkdir(parents=True)
    dates = {}
    for row in L.split("\n|-\n"):
        c = row.split("||")
        if len(c) >= 3:
            m = re.search(r"\[\[([^\]|]+)", c[1])
            if m:
                dates[m.group(1).strip()] = c[2].strip()
    out = {}
    for ev, n, why in miss:
        if why != "missing row":
            continue
        cells = next(c for e2, n2, c in pairs if e2 == ev and n2 == n)
        row = W.row_from_hub(H[ev], ev, cells)
        if not row:
            W.LOG.append(f"{n}: {ev} row has no citable source on the event page; not added")
            continue
        if row.startswith("|  ||") and dates.get(ev):
            row = "| " + dates[ev] + row[2:]
        out[n] = W.add_result_rows(out.get(n) or P[n], [(f"[[{ev}", row)], n)
    rows = []
    for n, t in out.items():
        fn = "pages/" + n.replace(" ", "_").replace("/", "%2F") + ".wiki"
        (pk / fn).write_text(t, encoding="utf-8"); rows.append(f"{n}\t{fn}")
    (pk / f"y-{B}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    shutil.copy("wiki_api_apply.py", pk)
    (pk / "since.txt").write_text(dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")
    subprocess.run(["tar", "cf", f"/mnt/user-data/outputs/{B}-apply.tar", "-C", str(pk), "."], check=True)
    print(f"{len(rows)} person pages -> {B}; LOG:", *W.LOG, sep="\n")
