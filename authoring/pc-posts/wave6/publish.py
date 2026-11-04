#!/usr/bin/env python3
"""Wave 6: publish a batch as Holocron Claude.

python3 publish.py batchdir [--dry]
1. GEMP files: uploaded under NEW names only (a clash with an existing wiki file gets a numeric suffix and the
   page's download line is patched), with a short file description citing the deck post.
2. Deck pages (apply.tsv), 3. hubs + player pages (hubs.tsv). Each edit is FlaggedRevs-reviewed by wiki_api_apply.
Writes batchdir/published.tsv (title, result).
"""
import json, os, re, sys, pathlib, urllib.parse
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
for l in open("/mnt/user-data/uploads/.grok/claude-agent/wiki-bot-password.env"):
    if "=" in l:
        k, v = l.strip().split("=", 1); os.environ[k] = v.strip().strip('"')
from wiki_api_apply import Wiki   # noqa: E402

b = pathlib.Path(sys.argv[1]); dry = "--dry" in sys.argv
plan = {p["title"]: p for p in json.load(open(b / "plan.json"))}
w = None if dry else Wiki()
log = []
SUM = "PC deck post missing from the wiki (wave 6, Holocron Claude)"


def exists(fn):
    r = w.get(action="query", titles="File:" + fn)["query"]["pages"][0]
    return not r.get("missing")


pages = [l.split("\t") for l in (b / "apply.tsv").read_text(encoding="utf-8").splitlines() if l]
for title, rel in pages:
    p = plan[title]; text = (b / rel).read_text(encoding="utf-8")
    if p.get("gemp") and not dry:
        g = p["gemp"]; fn = g; k = 2
        while exists(fn):
            fn = re.sub(r"\.txt$", f" {k}.txt", g); k += 1
        if fn != g:
            text = text.replace(f"[[Media:{g} |", f"[[Media:{fn} |")
        desc = (f"== Summary ==\nGEMP import file for [[{title}]].\n\n== Source ==\n* [{p['link']} {p['post_title']}], starwarsccg.org (deck post).")
        r = w.upload_new(b / "gemp" / g, fn, desc, SUM) if fn == g else None
        if fn != g:
            tmp = b / "gemp" / fn
            tmp.write_bytes((b / "gemp" / g).read_bytes()); r = w.upload_new(tmp, fn, desc, SUM)
        log.append(f"FILE\t{fn}\t{r}"); print("FILE", fn, r, flush=True)
    if dry:
        print("would edit", title); continue
    r = w.edit(title, text, SUM)
    log.append(f"PAGE\t{title}\t{r}"); print("PAGE", title, r, flush=True)
for l in (b / "hubs.tsv").read_text(encoding="utf-8").splitlines() if (b / "hubs.tsv").exists() else []:
    if not l: continue
    title, rel = l.split("\t")
    if dry:
        print("would edit", title); continue
    r = w.edit(title, (b / rel).read_text(encoding="utf-8"), "Link new deck pages from PC deck posts (wave 6, Holocron Claude)")
    log.append(f"LINK\t{title}\t{r}"); print("LINK", title, r, flush=True)
(b / "published.tsv").write_text("\n".join(log) + "\n", encoding="utf-8")
print("errors", sum("ERROR" in x for x in log))
