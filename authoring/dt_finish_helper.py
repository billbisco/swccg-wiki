"""Write a finished deck JSON from a compact spec and validate every card."""
import json,sys
sys.path.insert(0,"/home/claude/swccg-wiki/authoring")
import decktech_batch as b
def finish(pid, spec_cards, **fields):
    d=json.load(open(f"decktech-decks/{pid}.json",encoding="utf-8"))
    d.update(fields)
    side=d["side"]; rows=[]; bad=[]
    for q,name,posted in spec_cards:
        if fields.get("types",{}).get(name)=="UNKNOWN":  # keep the posted name; never the suggestion
            rows.append([q,name,"UNKNOWN",f"posted: {posted}"]); continue
        st,card=b.suggest(name,side)
        if st!="exact": bad.append((name,st,card))
        t=b.card_type(card) if card else ""
        if fields.get("types",{}).get(name): t=fields["types"][name]
        rows.append([q,card or name,t or "?",f"posted: {posted}"])
    d.pop("types",None)
    d["cards"]=rows
    json.dump(d,open(f"decktech-decks/{pid}.json","w",encoding="utf-8"),indent=1,ensure_ascii=False)
    print(pid,"qty",sum(r[0] for r in rows),"not-exact",bad)
    return d
