from b3common import *
titles=list(read('source-manifest.json')['pages'])+[r['title']for r in read('plan.json')if r['title']not in read('source-manifest.json')['pages']]
code="""from pathlib import Path
import subprocess,json,hashlib,urllib.parse
titles=TITLES
r=subprocess.run(['docker','exec','-i','-u','www-data','swccg_wiki','php','maintenance/run.php','purgePage'],input=('\\n'.join(titles)+'\\n').encode(),capture_output=True);assert r.returncode==0,r.stderr.decode()
cache=Path('/var/cache/nginx/wiki-live');deleted=[]
for title in titles:
 path='/wiki/'+title.replace(' ','_');variants={path,urllib.parse.quote(path,safe=\"/():\"),urllib.parse.quote(path,safe=\"/():'\")}
 for path in variants:
  key='httpswiki.swccg.com'+path;digest=hashlib.md5(key.encode()).hexdigest();target=cache/digest[-1]/digest[-3:-1]/digest;assert target.resolve().is_relative_to(cache.resolve())
  if target.is_file():
   with target.open('rb')as f:head=f.read(2048)
   assert('KEY: '+key+'\\n').encode()in head;target.unlink();deleted.append(path)
print(json.dumps({'native_titles_purged':len(titles),'exact_nginx_keys_deleted':deleted,'global_purge':False}))
""".replace('TITLES',repr(titles))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1000:];save('cache-purge.json',json.loads(r.stdout));print(json.dumps({'scoped_purge':'PASS','titles':len(titles)}))
