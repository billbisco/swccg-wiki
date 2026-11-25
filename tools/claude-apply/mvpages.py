#!/usr/bin/env python3
"""mvpages.py <tsv old\tnew\texpected_src_revid> : move pages as Holocron Claude, no redirect left, talk pages too.
Prints JSON lines: old,new,result,newlatest."""
import sys,json,os
sys.path.insert(0,os.path.expanduser("~/w/tools"))
from wiki_api_apply import Wiki
w=Wiki()
def latest(t):
    p=w.get(action="query",titles=t,prop="revisions",rvprop="ids")["query"]["pages"][0]
    return None if p.get("missing") else p["revisions"][0]["revid"]
for l in open(sys.argv[1]):
    if not l.strip(): continue
    old,new,exp=l.rstrip("\n").split("\t")
    cur=latest(old)
    if cur is None and latest(new):
        print(json.dumps(dict(old=old,new=new,result="already",newlatest=latest(new)),ensure_ascii=False)); continue
    if str(cur)!=exp:
        print(json.dumps(dict(old=old,new=new,result=f"DRIFT {cur}!={exp}"),ensure_ascii=False)); continue
    d=w.post(action="move",**{"from":old},to=new,reason=sys.argv[2],movetalk="1",noredirect="1",token=w.csrf)
    r="ERROR "+d["error"]["code"]+": "+d["error"].get("info","")[:150] if "error" in d else "moved"
    print(json.dumps(dict(old=old,new=new,result=r,newlatest=latest(new)),ensure_ascii=False),flush=True)
