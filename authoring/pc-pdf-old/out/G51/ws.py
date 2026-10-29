import sys,json,urllib.request,urllib.parse
for q in sys.argv[1:]:
    u="https://wiki.swccg.com/api.php?"+urllib.parse.urlencode({"action":"query","list":"search","srsearch":q,"srwhat":"title","srlimit":6,"format":"json"})
    r=json.load(urllib.request.urlopen(u)); print(q,"->",[x["title"] for x in r["query"]["search"]])
