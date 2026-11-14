from pathlib import Path
import sqlite3,json,hashlib,shutil,datetime
from PIL import Image
P=Path(__file__).resolve().parent
DATA=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data')
CACHE=(DATA/'offline-originals').resolve();OUT=P/'isolated-restore';OUT.mkdir(exist_ok=True)
CAP=64*1024**2;RESERVE=20*1024**3
def digest(path):
 h=hashlib.sha256()
 with path.open('rb')as f:
  while b:=f.read(128*1024):h.update(b)
 return h.hexdigest()
db=sqlite3.connect((P/'inventory-consistent.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
rows=[dict(r)for r in db.execute("SELECT v.id,v.title,v.timestamp,v.url,v.sha1,v.bytes,v.mime,v.current,b.sha256,b.path FROM versions v JOIN local_backups b ON b.version_id=v.id WHERE b.status='backed_up'ORDER BY v.title,v.timestamp")]
used_titles={r[0]for r in db.execute('SELECT DISTINCT title FROM usage')};db.close()
selected={};labels={}
def choose(r,label):
 if not r:return
 selected[r['id']]=r;labels.setdefault(r['id'],[]).append(label)
for mime in sorted({r['mime']for r in rows}):
 eligible=[r for r in rows if r['mime']==mime and r['bytes']<=8*1024**2]
 choose(eligible[0]if eligible else None,'image type '+mime)
 choose(next((r for r in eligible if r['title']not in used_titles),None),'unused current filename with retained historical version')
 choose(max(eligible,key=lambda r:r['bytes'])if eligible else None,'largest bounded '+mime+' sample')
animated_candidates=[]
for r in rows:
 if r['mime']not in('image/gif','image/webp','image/png'):continue
 src=(CACHE/r['path']).resolve();assert src.is_relative_to(CACHE)
 with Image.open(src)as im:
  if getattr(im,'n_frames',1)>1:
   animated_candidates.append(r['id']);choose(r,'animation');break
results=[];total=0
for r in selected.values():
 if total+r['bytes']>CAP:continue
 assert shutil.disk_usage(P).free>RESERVE+r['bytes']
 src=(CACHE/r['path']).resolve();assert src.is_relative_to(CACHE)and digest(src)==r['sha256']
 suffix={'image/gif':'.gif','image/png':'.png','image/jpeg':'.jpg','image/webp':'.webp'}[r['mime']]
 target=OUT/(r['id']+suffix);shutil.copyfile(src,target);assert target.stat().st_size==r['bytes']and digest(target)==r['sha256']
 with Image.open(target)as im:im.verify()
 with Image.open(target)as im:
  frames=getattr(im,'n_frames',1);dimensions=[im.width,im.height]
  for frame in range(frames):im.seek(frame);im.load()
 results.append({**r,'current':bool(r['current']),'unused_current_filename':r['title']not in used_titles,'selection':labels[r['id']],'isolated_path':str(target.relative_to(P)).replace('\\','/'),'dimensions':dimensions,'decoded_frames':frames,'sha256_and_bytes_match':True,'all_frames_decode':True});total+=r['bytes']
report={'issue':382,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_org_requests':0,'scope':'Recovery from PC original cache only; no Archive.org recovery claimed','sample_versions':len(results),'sample_bytes':total,'mimes':sorted({r['mime']for r in results}),'all_historical':all(not r['current']for r in results),'unused_filename_samples':sum(r['unused_current_filename']for r in results),'animation_found_in_cached_candidates':bool(animated_candidates),'animation_inventory_scope':'Only cached checkpoint objects inspected; not entire wiki','svg_inventory_versions':0,'sample_cap_bytes':CAP,'pc_reserve_bytes':RESERVE,'pc_free_after':shutil.disk_usage(P).free,'rows':results}
(P/'restore-report.json').write_bytes((json.dumps(report,indent=2)+'\n').encode());print(json.dumps({k:v for k,v in report.items()if k!='rows'}))
