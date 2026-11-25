import json,sys,time
from pathlib import Path
import os;sys.path.insert(0,os.path.expanduser("~/w/tools"))
from wiki_api_apply import Wiki
d=Path(sys.argv[1]); summ=sys.argv[2]
u=json.load(open(d/"uploads.json"))["uploads"]; w=Wiki()
for x in u:
    p=w.get(action="query",titles="File:"+x["file"],prop="imageinfo",iiprop="sha1")["query"]["pages"][0]
    if not p.get("missing"):
        print(x["file"],"exists", "same" if p["imageinfo"][0]["sha1"]==x["sha1"] else "DIFFERENT"); continue
    print(x["file"],"->",w.upload_new(d/Path(x["local_path"]).name,x["file"],x["page_wikitext"],summ),flush=True); time.sleep(1)
