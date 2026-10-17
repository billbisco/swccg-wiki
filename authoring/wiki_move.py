"""Move wiki pages as the bot (2026-10-17). python3 wiki_move.py FROM TO REASON [--keep-redirect]
Credentials from WIKI_BOT_USER / WIKI_BOT_PASS (never printed). Default suppresses the redirect (crude-title renames)."""
import sys
from wiki_api_apply import Wiki

def main(a):
    w = Wiki()
    p = dict(action="move", **{"from": a[0]}, to=a[1], reason=a[2], movetalk="1", token=w.csrf)
    if "--keep-redirect" not in a:
        p["noredirect"] = "1"
    r = w.post(**p)
    print("MOVE", a[0], "->", a[1], "ok" if "move" in r else r.get("error"))

if __name__ == "__main__":
    main(sys.argv[1:])
