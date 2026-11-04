#!/usr/bin/env python3
"""Wave 6: publish a batch-B dir (deck pages, GEMP files, hub/player/talk edits) as Holocron Claude, merging hub
and player edits with anything changed on the wiki since the agent read the page.

python3 publish_merge.py batchdir SINCE_ISO [--dry]
For every page in hubs.tsv: base = the last revision older than SINCE (what the agent built on), ours = the batch's
text, theirs = the current live text. If live == base we write ours; otherwise `git merge-file` 3-way merge; on a
conflict the page is skipped and listed in conflicts.txt.
"""
import json, os, re, sys, subprocess, tempfile, pathlib, urllib.parse
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
for l in open("/mnt/user-data/uploads/.grok/claude-agent/wiki-bot-password.env"):
    if "=" in l:
        k, v = l.strip().split("=", 1); os.environ[k] = v.strip().strip('"')
from wiki_api_apply import Wiki   # noqa: E402

b = pathlib.Path(sys.argv[1]); since = sys.argv[2]; dry = "--dry" in sys.argv
w = Wiki()
SUM = "PC deck post missing from the wiki (wave 6, Holocron Claude)"
LSUM = "Link new deck pages from PC deck posts (wave 6, Holocron Claude)"
log, conflicts = [], []


def revs(title):
    r = w.get(action="query", prop="revisions", titles=title, rvprop="ids|timestamp|content", rvslots="main", rvlimit=50)
    p = r["query"]["pages"][0]
    return [] if p.get("missing") else p["revisions"]


def text_of(rv): return rv["slots"]["main"]["content"]


def exists(fn):
    return not w.get(action="query", titles="File:" + fn)["query"]["pages"][0].get("missing")


plan = json.load(open(b / "plan.json"))
plan = {p["title"]: p for p in (plan if isinstance(plan, list) else plan.values())}
# 1. deck pages (+ GEMP files)
for line in (b / "apply.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    title, rel = line.split("\t")[:2]
    text = (b / rel).read_text(encoding="utf-8"); p = plan.get(title, {})
    g = p.get("gemp")
    if g and (b / "gemp" / g).exists() and not dry:
        fn, k = g, 2
        while exists(fn):
            fn = re.sub(r"\.txt$", f" {k}.txt", g); k += 1
        if fn != g:
            (b / "gemp" / fn).write_bytes((b / "gemp" / g).read_bytes())
            text = text.replace(f"Media:{g}", f"Media:{fn}")
        desc = f"== Summary ==\nGEMP import file for [[{title}]].\n\n== Source ==\n* [{p.get('link', '')} {p.get('post_title', title)}], starwarsccg.org (deck post)."
        r = w.upload_new(b / "gemp" / fn, fn, desc, SUM)
        if str(r).startswith("ERROR") and "duplicate" in str(r):
            r = w.upload(b / "gemp" / fn, SUM) + " (duplicate content)"; w.edit("File:" + fn, desc, SUM)
        log.append(f"FILE\t{fn}\t{r}"); print("FILE", fn, r, flush=True)
    if dry: print("would edit", title); continue
    rv = revs(title)
    if rv and p.get("existing") is None and not p.get("overwrites_existing") and not p.get("existing"):
        # an existing page we did not plan to overwrite: merge like a hub
        pass
    r = w.edit(title, text, SUM); log.append(f"PAGE\t{title}\t{r}"); print("PAGE", title, r, flush=True)
# 2. hub / player / talk pages, 3-way merged
for line in (b / "hubs.tsv").read_text(encoding="utf-8").splitlines() if (b / "hubs.tsv").exists() else []:
    if not line.strip(): continue
    title, rel = line.split("\t")[:2]
    ours = (b / rel).read_text(encoding="utf-8")
    rv = revs(title)
    if not rv:
        out = ours; how = "new"
    else:
        live = text_of(rv[0])
        older = [x for x in rv if x["timestamp"] < since]
        base = text_of(older[0]) if older else live
        if live == base:
            out, how = ours, "direct"
        elif ours == base or ours == live:
            out, how = live, "keep-live"
        else:
            with tempfile.TemporaryDirectory() as d:
                pa, pb, pc = (pathlib.Path(d) / n for n in ("ours", "base", "theirs"))
                pa.write_text(ours.rstrip("\n") + "\n"); pb.write_text(base.rstrip("\n") + "\n"); pc.write_text(live.rstrip("\n") + "\n")
                rc = subprocess.run(["git", "merge-file", "-p", str(pa), str(pb), str(pc)], capture_output=True, text=True)
                if rc.returncode != 0:
                    conflicts.append(title); print("CONFLICT", title, flush=True); continue
                out, how = rc.stdout, "merged"
    if dry: print("would", how, title); continue
    r = w.edit(title, out, LSUM); log.append(f"LINK\t{title}\t{how}\t{r}"); print("LINK", title, how, r, flush=True)
(b / "published.tsv").write_text("\n".join(log) + "\n", encoding="utf-8")
(b / "conflicts.txt").write_text("\n".join(conflicts) + "\n", encoding="utf-8")
print("errors", sum("ERROR" in x for x in log), "conflicts", len(conflicts))
