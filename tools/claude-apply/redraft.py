import sys, json, os, urllib.request, urllib.parse
sys.argv=[sys.argv[0]]+sys.argv[1:2]  # keep default
os.chdir("/home/claude/rredirx/work"); sys.path.insert(0,".")
import s7_draft as S
API="https://swccg.com/wiki/api.php"
def q(**p):
    p.update(format="json",formatversion=2); return json.load(urllib.request.urlopen(urllib.request.Request(API,urllib.parse.urlencode(p).encode()),timeout=120))
titles=[l.split("\t")[0] for l in open("/home/claude/capply/rb1/unmerged.tsv") if l.strip()]
out="/home/claude/capply/rb2"; os.makedirs(out,exist_ok=True)
# which redirects are still redirects live
need=sorted({r for p in titles for r in S.per_page.get(p,())})
isred={}
for i in range(0,len(need),50):
    d=q(action="query",titles="|".join(need[i:i+50]),prop="info")
    norm={n["to"]:n["from"] for n in d["query"].get("normalized",[])}
    for pg in d["query"]["pages"]: isred[norm.get(pg["title"],pg["title"])]=bool(pg.get("redirect"))
rows=[];base={}
for p in titles:
    lp=q(action="query",titles=p,prop="revisions",rvprop="content|ids",rvslots="main")["query"]["pages"][0]["revisions"][0]
    t0=lp["slots"]["main"]["content"]; t=t0; skipped=[]
    for r in sorted(S.per_page.get(p,()),key=len,reverse=True):
        if not isred.get(r): skipped.append(r); continue
        t,n,fl=S.edit(t,r,p,t0)
    if t!=t0:
        fn=p.replace("/","%2F")+".wiki"; open(f"{out}/{fn}","w").write(t); rows.append((p,fn)); base[p]=lp["revid"]
    print(p, "changed" if t!=t0 else "nochange", "skipped:",skipped[:3])
open(f"{out}/apply.tsv","w").write("".join(f"{a}\t{b}\n" for a,b in rows)); json.dump(base,open(f"{out}/base_revids.json","w"))
