"""Errata-table census for swccg-guild/work#638: which card families have later text states and
whether their member pages show a shared Template:Card errata/* comparison. Read-only."""
import csv,json,re,time,urllib.request,urllib.parse,collections,sys
API="https://swccg.com/wiki/api.php"
def q(**p):
    p.update(format="json",formatversion=2)
    for i in range(5):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(API,urllib.parse.urlencode(p).encode()),timeout=90))
        except Exception as e: time.sleep(3+i*3)
    raise SystemExit("api fail")
fams=list(csv.DictReader(open("/home/claude/census1325/families.tsv"),delimiter="\t"))
pages=sorted({m.strip() for f in fams for m in f["members"].split(" | ") if m.strip()})
print(len(fams),"families",len(pages),"member pages",file=sys.stderr)
tpl={}
for i in range(0,len(pages),50):
    cont={}
    while True:
        d=q(action="query",titles="|".join(pages[i:i+50]),prop="templates",tlnamespace=10,tllimit="max",redirects=1,**cont)
        mp={x["from"]:x["to"] for k in ("normalized","redirects") for x in d["query"].get(k,[])}
        for p in d["query"]["pages"]:
            tpl.setdefault(p["title"],set()).update(x["title"] for x in p.get("templates",[]) if x["title"].startswith("Template:Card errata/"))
        for a,b in mp.items(): tpl.setdefault("__map__"+a,b)
        if "continue" in d: cont={k:v for k,v in d["continue"].items()}
        else: break
    time.sleep(0.4)
def T(m):
    t=m
    for _ in range(3): t=tpl.get("__map__"+t,t)
    return tpl.get(t,set())
ERR=re.compile(r"\((?:Errata|PC Errata|PC \d{4} D-E1|Decipher Errata|.*?(?:slip|disc card|E card|D-E1 card))",re.I)
out=[]
for f in fams:
    mem=[m.strip() for m in f["members"].split(" | ") if m.strip()]
    errm=[m for m in mem if ERR.search(m)]
    have=[m for m in mem if T(m)]
    tset=sorted(set().union(*[T(m) for m in mem])) if mem else []
    if not errm: st="no later text states"
    elif not have: st="NO TABLE"
    elif len(have)<len(mem): st="table on some members"
    else: st="table on every member"
    if len(tset)>1 and st!="no later text states": st+=" (several tables)"
    out.append(dict(family=f["family"],era=f["era"],origin_set=f["origin_set"],side=f["side"],type=f["type"],n_members=len(mem),n_errata=len(errm),n_with_table=len(have),status=st,tables=" | ".join(tset),missing=" | ".join(m for m in mem if not T(m))))
with open("/home/claude/census638/families638.tsv","w") as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0]),delimiter="\t"); w.writeheader(); w.writerows(out)
c=collections.Counter((o["era"],o["status"]) for o in out)
for k,v in sorted(c.items()): print(k,v)
