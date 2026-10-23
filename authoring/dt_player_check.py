"""Before a build: fix player_page / redirects for every deck in IDS against the live wiki (2026-10-23).

  python3 dt_player_check.py ID...
A redirected name becomes its target person page; 'new' on a page that exists becomes 'existing' and the reverse."""
import json, re, sys
import decktech_batch as db

cache = {}
for i in [a for a in sys.argv[1:] if a.isdigit()]:
    p = db.DECKS / f"{i}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("player_page") == "none":
        continue
    name = d.get("player_link") or d["player"]
    if name not in cache:
        cache[name] = db.live_text(name)
    t, ch = cache[name], False
    if t and t.lstrip().upper().startswith("#REDIRECT"):
        tgt = re.search(r"\[\[([^\]|#]+)", t).group(1).strip()
        print(i, "redirect", name, "->", tgt)
        d["player"], d["player_page"], ch = tgt, "existing", True
    elif t is not None and d["player_page"] == "new":
        d["player_page"], ch = "existing", True
        print(i, name, "new -> existing")
    elif t is None and d["player_page"] == "existing":
        d["player_page"], ch = "new", True
        print(i, name, "existing -> new")
    if ch:
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
