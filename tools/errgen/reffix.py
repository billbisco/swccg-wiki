import json,urllib.request,urllib.parse,os,sys
API="https://swccg.com/wiki/api.php"
def q(**p):
    p.update(format="json",formatversion=2); return json.load(urllib.request.urlopen(urllib.request.Request(API,urllib.parse.urlencode(p).encode()),timeout=90))
d=sys.argv[1]; os.chdir(d)
rows=[l.rstrip("\n").split("\t") for l in open("apply.tsv") if l.strip()]
mem=[r for r in rows if not r[0].startswith("Template:")]
live={}
for i in range(0,len(mem),50):
    for p in q(action="query",titles="|".join(r[0] for r in mem[i:i+50]),prop="revisions",rvprop="content",rvslots="main")["query"]["pages"]:
        live[p["title"]]=p["revisions"][0]["slots"]["main"]["content"]
for t,f in mem:
    fn=os.path.basename(f); s=open(fn).read(); L=live[t]
    if L.count("<references")>s.count("<references") and "has_refs" not in s and "<ref" in s:
        v=s.index("\n|versions="); e=s.index("\n",v+1); s=s[:e+1]+"|has_refs=1\n"+s[e+1:]; open(fn,"w").write(s); print("fixed",t)
    if len(L)-len(s)>3000: print("BIG SHRINK",t,len(L),len(s))
print("checked",len(mem))
