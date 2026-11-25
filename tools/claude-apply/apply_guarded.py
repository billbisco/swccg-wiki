#!/usr/bin/env python3
"""Apply reviewed drafts with edit-conflict guards (#601). Uses wiki_api_apply.Wiki (Holocron Claude sign-in).

    python3 apply_guarded.py BATCHDIR "summary"      # BATCHDIR has apply.tsv + base_revids.json + draft files

- Existing page: sends baserevid=<revid the draft was built on>; MediaWiki reports editconflict
  if someone saved in between (logged, skipped, never overwritten).
- New page (revid 0): createonly=1, so an existing page is never replaced.
Writes BATCHDIR/applied.jsonl (title, result, new revid).
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_api_apply import Wiki  # noqa: E402

d = Path(sys.argv[1]); summary = sys.argv[2]
base = json.loads((d / "base_revids.json").read_text(encoding="utf-8"))
rows = [l.split("\t") for l in (d / "apply.tsv").read_text(encoding="utf-8").splitlines() if l.strip()]
w = Wiki()
already_done = set()
if (d / "applied.jsonl").exists():
    for _l in (d / "applied.jsonl").read_text(encoding="utf-8").splitlines():
        _j = json.loads(_l)
        if _j["result"].startswith(("edited", "created", "nochange")): already_done.add(_j["title"])
def own_save(title, text):
    """After a timeout, the save may have landed before it was logged: if the latest revision is
    Holocron Claude's and equals the draft (signatures expanded), report it instead of an error."""
    u = "https://swccg.com/wiki/api.php?" + urllib.parse.urlencode(dict(action="query", prop="revisions", titles=title,
        rvprop="ids|user|content", rvslots="main", format="json", formatversion=2))
    try:
        r = json.load(urllib.request.urlopen(u, timeout=60))["query"]["pages"][0]["revisions"][0]
    except Exception:
        return None
    live = r["slots"]["main"]["content"]
    norm = lambda t: re.sub(r"\[\[User:Holocron Claude\|Holocron Claude\]\] \(\[\[User talk:Holocron Claude\|talk\]\]\) [0-9:]+, [0-9]+ \w+ [0-9]{4} \(UTC\)", "~~~~", t).strip()
    return r["revid"] if r["user"] == "Holocron Claude" and norm(live) == norm(text) else None
log = open(d / "applied.jsonl", "a", encoding="utf-8")
for title, rel in rows:
    if title in already_done: continue
    text = (d / Path(rel).name).read_text(encoding="utf-8")
    rev = int(base.get(title, 0) or 0)
    p = dict(action="edit", title=title, text=text, summary=summary, bot="1", token=w.csrf, maxlag="5")
    if rev:
        p["baserevid"] = str(rev)
    else:
        p["createonly"] = "1"
    for wait in (0, 20, 40, 60, 60, 60):
        time.sleep(wait)
        r = w.post(**p)
        if r.get("error", {}).get("code") != "ratelimited":
            break
    if "error" in r:
        res = "ERROR " + r["error"].get("code", "") + ": " + r["error"].get("info", "")[:120]; newrev = None
        if r["error"].get("code") in ("articleexists", "editconflict"):
            mine = own_save(title, text)
            if mine:
                res = f"nochange (own save rev {mine} landed before a timeout)"; newrev = mine
    else:
        e = r["edit"]
        if e.get("result") != "Success":
            res = "FAIL " + json.dumps(e)[:200]; newrev = None
        else:
            res = ("nochange" if e.get("nochange") else ("created" if e.get("new") else "edited")) + w.review(title)
            newrev = e.get("newrevid")
    print(title, "->", res, flush=True)
    log.write(json.dumps(dict(title=title, result=res, newrevid=newrev, base=rev), ensure_ascii=False) + "\n"); log.flush()
    time.sleep(1.5)
