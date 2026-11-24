#!/usr/bin/env python3
"""Back up live wiki revisions into billbisco/swccg-wiki pages/ through the GitHub API (no local clone).
Always merges into the CURRENT remote pages/INDEX.tsv (lesson 2026-11-24: a stale local INDEX dropped 6,730 rows).
    GH_TOKEN=... python3 backup_api.py titles.tsv "commit message"
New titles get pages/<wiki_fname>.wiki and an appended INDEX row; existing titles keep their INDEX path.
"""
import json,os,sys,urllib.request,urllib.error,urllib.parse,base64
T=os.environ["GH_TOKEN"]; R="https://api.github.com/repos/billbisco/swccg-wiki"
def gh(m,p,d=None,raw=False):
    h={"Authorization":"token "+T,"Content-Type":"application/json"}
    if raw: h["Accept"]="application/vnd.github.raw"
    r=urllib.request.Request(R+p,json.dumps(d).encode() if d is not None else None,h,method=m)
    try: b=urllib.request.urlopen(r,timeout=180).read()
    except urllib.error.HTTPError as e: sys.exit(f"GitHub {m} {p.split('?')[0]} -> {e.code}: {e.read()[:400]!r}")
    return b if raw else json.loads(b)
def fname(t):
    n=t.replace(" ","_").replace(":","_").replace("/","_")
    for ch in '?*"<>|': n=n.replace(ch,"")
    return n+".wiki"
titles=[l.rstrip("\r\n").split("\t")[0] for l in open(sys.argv[1],encoding="utf-8") if l.strip() and not l.startswith("Talk:")]
head=gh("GET","/git/ref/heads/main")["object"]["sha"]; base=gh("GET",f"/git/commits/{head}")["tree"]["sha"]
lines=gh("GET",f"/contents/pages/INDEX.tsv?ref={head}",raw=True).decode("utf-8").splitlines()
idx={l.split("\t")[0]:l.split("\t")[1] for l in lines if "\t" in l}
tree=[];added=[]
for i in range(0,len(titles),40):
    u="https://swccg.com/wiki/api.php?"+urllib.parse.urlencode(dict(action="query",prop="revisions",rvprop="content",rvslots="main",format="json",formatversion=2,titles="|".join(titles[i:i+40])))
    for p in json.load(urllib.request.urlopen(u,timeout=120))["query"]["pages"]:
        if "revisions" not in p: continue
        t=p["title"]; path=idx.get(t)
        if not path: path="pages/"+fname(t); added.append(f"{t}\t{path}")
        tree.append({"path":path,"mode":"100644","type":"blob","content":p["revisions"][0]["slots"]["main"]["content"]})
if added:
    b=gh("POST","/git/blobs",{"content":base64.b64encode(("\n".join(lines+added)+"\n").encode()).decode(),"encoding":"base64"})["sha"]
    tree.append({"path":"pages/INDEX.tsv","mode":"100644","type":"blob","sha":b})
nt=gh("POST","/git/trees",{"base_tree":base,"tree":tree})["sha"]
me={"name":"billbisco","email":"billbisco@users.noreply.github.com"}
c=gh("POST","/git/commits",{"message":sys.argv[2],"tree":nt,"parents":[head],"author":me,"committer":me})["sha"]
gh("PATCH","/git/refs/heads/main",{"sha":c}); print("committed",c[:9],len(tree)-(1 if added else 0),"pages,",len(added),"new INDEX rows")
