import json,urllib.request,urllib.parse,sys,time
API="https://swccg.com/wiki/api.php"
def q(**p):
    p.update(format="json",formatversion=2); 
    for i in range(4):
        try: return json.load(urllib.request.urlopen(API+"?"+urllib.parse.urlencode(p),timeout=60))
        except Exception as e: time.sleep(3)
titles=[]
for g in sys.argv[1:]:
    titles+=[l.split("\t")[0] for l in open(f"{g}/apply.tsv").read().splitlines()]
titles=[t for t in titles if not t.startswith("Talk:")]
# purge
for i in range(0,len(titles),40):
    d=urllib.parse.urlencode(dict(action="purge",titles="|".join(titles[i:i+40]),forcelinkupdate=1,format="json")).encode()
    urllib.request.urlopen(API,d,timeout=120)
bad=[];red=set()
for t in titles:
    r=q(action="parse",page=t,prop="text|links",disablelimitreport=1)
    h=r["parse"]["text"]
    if "cite_error" in h or "mw-ext-cite-error" in h: bad.append(t)
    for l in r["parse"]["links"]:
        if not l.get("exists") and l["ns"]==0: red.add(l["title"])
print(len(titles),"pages; cite errors:",bad); print("red links:",len(red),sorted(red)[:60])
