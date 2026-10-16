#!/usr/bin/env python3
"""Automated checks for a built batch before applying (replaces hand review).

    python3 batch_qa.py y-<batch>.tsv

Flags: links/images that don't exist, links to decision pages (Category:Disambiguation), card links on the wrong
side for the deck, and any line of an existing live page that the new text drops (except source/link-only lines).
Exit 1 when something needs a look.
"""
import json, re, sys, urllib.parse, urllib.request

API = "https://wiki.swccg.com/api.php"


def api(**p):
    q = urllib.parse.urlencode({**p, "format": "json", "formatversion": "2"})
    with urllib.request.urlopen(API + "?" + q, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def info(titles):
    out = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        r = api(action="query", titles="|".join(titles[i:i + 50]), redirects=1, prop="categories", cllimit="max")
        red = {x["from"]: x["to"] for x in r["query"].get("redirects", [])}
        norm = {x["from"]: x["to"] for x in r["query"].get("normalized", [])}
        pages = {p["title"]: p for p in r["query"]["pages"]}
        for t in titles[i:i + 50]:
            n = norm.get(t, t)
            p = pages.get(red.get(n, n), {})
            out[t] = {"missing": p.get("missing", False) or not p,
                      "cats": {c["title"][9:] for c in p.get("categories", [])}}
    return out


def main(tsv):
    rows = [l.split("\t") for l in open(tsv, encoding="utf-8").read().splitlines() if l.strip()]
    own = {t.lower() for t, _ in rows}
    flags = []
    for t, path in rows:
        text = open(path, encoding="utf-8").read()
        side = (re.search(r"\* '''Side:''' \[\[(Light|Dark)\]\]", text) or [None, None])[1]
        body = text.split("== Original post")[0]
        cl = re.findall(r"\{\{CardLink\|([^|}]+)\|([^|}]+)", text)
        links = {m.strip() for m in re.findall(r"\[\[([^\]|#]+)", text) if not m.startswith((":", "Category:", "Media:"))}
        links |= {d for d, _ in cl}
        inf = info(list(links) + ["File:" + i for _, i in cl if not i.startswith("File:")])
        for l in sorted(links):
            if l.startswith("File:"):
                continue
            if inf[l]["missing"] and l.lower() not in own:
                flags.append(f"{t}: RED [[{l}]]")
            elif "Disambiguation" in inf[l]["cats"] and t not in ("DeckTech decks",):
                flags.append(f"{t}: DECISION PAGE [[{l}]]")
        for _, im in cl:
            if inf.get("File:" + im, {}).get("missing"):
                flags.append(f"{t}: MISSING IMAGE {im}")
        if side:
            other = "Dark" if side == "Light" else "Light"
            for d, _ in re.findall(r"\{\{CardLink\|([^|}]+)\|([^|}]+)", body):
                c = inf.get(d, {}).get("cats", set())
                if other in c and side not in c:
                    flags.append(f"{t}: {other.upper()} CARD in {side} deck: {d}")
    # existing pages: nothing live may be dropped
    for t, path in rows:
        r = api(action="query", titles=t, prop="revisions", rvprop="content", rvslots="main")["query"]["pages"][0]
        if "revisions" not in r:
            continue
        live = r["revisions"][0]["slots"]["main"]["content"]
        new = open(path, encoding="utf-8").read()
        ls, ns = set(re.split(r"\n|(?<=\.) ", live)), set(re.split(r"\n|(?<=\.) ", new))
        gone = [x for x in ls - ns if x.strip() and "Preservation copies" not in x and "CardLink" not in x
                and "web.archive.org" not in x]
        for g in gone[:5]:
            flags.append(f"{t}: DROPS live text: {g[:140]}")
    print("\n".join(flags) if flags else "QA clean")
    print(f"pages {len(rows)}, flags {len(flags)}")
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
