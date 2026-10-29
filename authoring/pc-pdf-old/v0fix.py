import json,re,sys,pathlib,urllib.request,urllib.parse
sys.path.insert(0,"/home/claude/sw2/authoring/pc-pdf-scans")
import resolve_wiki as R
H=pathlib.Path(__file__).parent; O=H/"v0fix"
L=json.load(open(H/"v0fix.json")); rows=[]; log=[]
def live(t):
    r=R._q(action="query",titles=t,prop="revisions",rvprop="content|timestamp",rvslots="main")
    p=r["query"]["pages"][0]; return p["revisions"][0]["slots"]["main"]["content"]
def rawprefix(q):
    return [p["title"] for p in R._q(action="query",list="prefixsearch",pssearch=q,pslimit=40)["query"]["prefixsearch"]]
def norm(s): return re.sub(r"[^a-z0-9]","",s.replace("•","").lower())
def base(t): return re.sub(r"( \([^()]*\))+$","",t)
for title in L:
    txt=live(title); era="original" if title.startswith("2008") else "legacy"
    side="Dark" if " DS " in title else "Light"
    def fix(m):
        full=m.group(0); parts=full[2:-2].split("|"); tgt,img=parts[1],parts[2]
        R.fetch([tgt]); i=R._c["pages"].get(tgt)
        new=None
        if i and not re.match(r"(V0|VS\d*)-",i["image"]):
            new=(tgt,i["image"])
        else:
            want_v="(V)" in tgt; b=base(tgt.replace(" (V)",""))
            cands=[t for t in rawprefix(b) if norm(base(t.replace(" (V)","")))==norm(b) and (("(V)" in t)==want_v)]
            R.fetch(cands)
            ok=[R._c["pages"][t] for t in cands if R._c["pages"].get(t) and R._c["pages"][t]["card"] and R._c["pages"][t]["side"]==side and "(AI)" not in t and "(ALT)" not in t]
            for pre in (("OVS","VSh") if era=="original" else ("VB","VSh","OVS")):
                h=sorted([x for x in ok if x["image"].startswith(pre)],key=lambda x:len(x["title"]))
                if h: new=(h[0]["title"],h[0]["image"]); break
        if not new: log.append(f"KEEP {title}: {full}"); return full
        parts[1],parts[2]=new
        lab=re.sub(r"( \((?!V\))[^()]*\))+$","",new[0].replace("•",""))
        parts=[p for p in parts if not p.startswith("label=")]
        if lab!=new[0]: parts.append("label="+lab)
        out="{{"+"|".join(parts)+"}}"; log.append(f"FIX {title}: {full} -> {out}"); return out
    nt=re.sub(r"\{\{CardLink\|[^}]*\|(?:V0|VS\d*)-[^}]*\}\}",fix,txt)
    if nt!=txt:
        fn=re.sub(r"[^\w.-]+","_",title)+".wiki"; (O/"pages"/fn).write_text(nt,encoding="utf-8"); rows.append(f"{title}\tpages/{fn}")
(O/"all.tsv").write_text("\n".join(rows)+"\n",encoding="utf-8"); print("\n".join(log)); print(len(rows),"pages")
