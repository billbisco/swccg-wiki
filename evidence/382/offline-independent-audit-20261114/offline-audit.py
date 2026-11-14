"""Read-only consistent inventory export and bounded local restore. No HTTP code."""
from pathlib import Path
import sqlite3,json,hashlib,gzip,shutil,datetime,collections
P=Path(__file__).resolve().parent
DATA=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data')
CACHE=DATA/'offline-originals'
RESERVE=20*1024**3;CAP=64*1024**2
def save(n,v):(P/n).write_bytes((json.dumps(v,indent=2)+'\n').encode())
def hashes(path):
 a=hashlib.sha1();b=hashlib.sha256();n=0
 with path.open('rb')as f:
  while chunk:=f.read(128*1024):a.update(chunk);b.update(chunk);n+=len(chunk)
 return {'sha1':a.hexdigest(),'sha256':b.hexdigest(),'bytes':n}
def image_valid(path,mime):
 if mime=='image/svg+xml':
  import xml.etree.ElementTree as ET
  assert ET.parse(path).getroot().tag.endswith('svg');return {'type':'SVG','parse':'PASS'}
 from PIL import Image
 with Image.open(path)as im:
  result={'type':im.format,'width':im.width,'height':im.height,'frames':getattr(im,'n_frames',1)}
  im.verify()
 with Image.open(path)as im:im.load()
 return result
assert shutil.disk_usage(P).free>RESERVE+CAP
db=sqlite3.connect((DATA/'inventory.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
db.execute('BEGIN')
observed=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert db.execute('PRAGMA query_only=ON').fetchone()is None
counts={r['name']:r['n']for r in db.execute("SELECT 'current_files' name,count(*) n FROM files UNION ALL SELECT 'current_images',count(*)FROM files WHERE mime LIKE 'image/%' UNION ALL SELECT 'public_image_versions',count(*)FROM versions WHERE mime LIKE 'image/%' UNION ALL SELECT 'historical_image_versions',count(*)FROM versions WHERE mime LIKE 'image/%'AND current=0 UNION ALL SELECT 'nonimage_versions',count(*)FROM versions WHERE mime NOT LIKE 'image/%' UNION ALL SELECT 'archive_verified_image_versions',count(*)FROM versions WHERE mime LIKE 'image/%'AND status='verified' UNION ALL SELECT 'locally_backed_up_versions',count(*)FROM local_backups WHERE status='backed_up' UNION ALL SELECT 'locally_needs_reconciliation',count(*)FROM local_backups WHERE status='needs_reconciliation'")}
counts['unused_current_images']=db.execute("SELECT count(*)FROM files f WHERE mime LIKE 'image/%'AND NOT EXISTS(SELECT 1 FROM usage u WHERE u.title=f.title)").fetchone()[0]
types=[dict(r)for r in db.execute("SELECT mime,count(*) versions,sum(bytes) bytes FROM versions WHERE mime LIKE 'image/%'GROUP BY mime ORDER BY mime")]
rows=db.execute("""SELECT v.*,b.status local_status,b.sha256 local_sha256,b.path local_path,b.verified_at local_verified_at,
 coalesce(u.n,0)usage_count,d.revid description_revision FROM versions v
 LEFT JOIN local_backups b ON b.version_id=v.id
 LEFT JOIN(SELECT title,count(*)n FROM usage GROUP BY title)u ON u.title=v.title
 LEFT JOIN descriptions d ON d.title=v.title WHERE v.mime LIKE 'image/%' ORDER BY v.title,v.timestamp,v.id""").fetchall()
manifest=[]
for r in rows:
 m=json.loads(r['metadata']);manifest.append({'version_id':r['id'],'title':r['title'],'original_url':r['url'],'timestamp':r['timestamp'],'current':bool(r['current']),'mime':r['mime'],'bytes':r['bytes'],'width':m.get('width'),'height':m.get('height'),'mediawiki_sha1':r['sha1'],'local_sha256':r['local_sha256'],'local_status':r['local_status'],'local_object_path':r['local_path'],'local_verified_at':r['local_verified_at'],'archive_status':r['status'],'usage_count':r['usage_count'],'provenance_file_title':r['title'],'description_revision':r['description_revision']})
assert len(manifest)==counts['public_image_versions']
raw=b''.join((json.dumps(r,ensure_ascii=False)+'\n').encode()for r in manifest)
(P/'inventory-checkpoint.jsonl.gz').write_bytes(gzip.compress(raw,mtime=0))
assert gzip.decompress((P/'inventory-checkpoint.jsonl.gz').read_bytes())==raw
groups={}
for r in rows:
 key=(r['sha1'],r['bytes']);groups.setdefault(key,[]).append(r['id'])
unique_bytes=sum(k[1]for k in groups);total_bytes=sum(r['bytes']for r in rows)
samples=[];used=0;selected=set()
backed=[r for r in rows if r['local_status']=='backed_up']
cache_results=[]
for r in backed:
 src=(CACHE/r['local_path']).resolve();assert src.is_relative_to(CACHE.resolve())
 result=hashes(src);expected=int(r['sha1'],16)if len(r['sha1'])==40 else int(r['sha1'],36)
 assert result['sha256']==r['local_sha256']and result['bytes']==r['bytes']and int(result['sha1'],16)==expected
 cache_results.append({'version_id':r['id'],'sha256':result['sha256'],'bytes':result['bytes'],'matches_inventory_and_cache_receipt':True})
save('cache-readback.json',{'observed_at':observed,'archive_org_requests':0,'versions':len(cache_results),'bytes':sum(r['bytes']for r in cache_results),'rows':cache_results})
for mime in sorted({r['mime']for r in backed}):
 for current in [False,True]:
  match=next((r for r in backed if r['mime']==mime and bool(r['current'])==current and r['id']not in selected and r['bytes']<=8*1024**2),None)
  if match:selected.add(match['id']);samples.append(match)
restore=P/'offline-restore-sample';restore.mkdir(exist_ok=True)
results=[]
for r in samples[:12]:
 src=(CACHE/r['local_path']).resolve();assert src.is_relative_to(CACHE.resolve())
 if used+r['bytes']>CAP:break
 assert shutil.disk_usage(P).free>RESERVE+r['bytes']
 before=hashes(src);assert before['sha256']==r['local_sha256']and before['bytes']==r['bytes']
 expected=int(r['sha1'],16)if len(r['sha1'])==40 else int(r['sha1'],36)
 assert int(before['sha1'],16)==expected
 target=restore/(r['id']+src.suffix);shutil.copyfile(src,target);after=hashes(target);assert after==before
 results.append({'version_id':r['id'],'title':r['title'],'timestamp':r['timestamp'],'current':bool(r['current']),'mime':r['mime'],'bytes':r['bytes'],'sha256':before['sha256'],'sha1_matches_inventory':True,'isolated_copy_readback_matches':True,'decoded':image_valid(target,r['mime'])});used+=r['bytes']
meta={r['key']:json.loads(r['value'])for r in db.execute('SELECT key,value FROM meta')};db.rollback();db.close()
report={'issue':382,'observed_at':observed,'method':'Read-only SQLite transaction; no ledger/cache writes or downloader; local disk restore sample','archive_org_requests':0,'provider_hold':'ALL requests paused; reminder is reassessment only','counts':counts,'mime_types':types,'inventoried_payload_bytes':total_bytes,'unique_inventory_sha1_size_objects':len(groups),'unique_inventoried_payload_bytes':unique_bytes,'potential_dedup_savings_bytes':total_bytes-unique_bytes,'cutoff':meta.get('cutoff'),'initial_inventory_complete':meta.get('inventory_complete'),'final_delta_complete':False,'inventory_export':{'path':'inventory-checkpoint.jsonl.gz','sha256':hashes(P/'inventory-checkpoint.jsonl.gz')['sha256'],'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'versions':len(manifest)},'restore_sample':{'versions':len(results),'bytes':used,'scope':'PC cache only; does NOT establish Archive.org recovery','rows':results},'pc_free_bytes_after':shutil.disk_usage(P).free,'pc_reserve_bytes':RESERVE,'ongoing_backup_owner':'Existing #382 coordinating chat; this audit does not take ownership of its full job','unfinished':['Full initial local original-byte backup pass','Final uploads/replacements/version delta','Archive.org captures and recovery after explicit resumption','File Preservation links and incremental integration']}
save('offline-audit.json',report)
print(json.dumps({k:report[k]for k in ['observed_at','counts','archive_org_requests','pc_free_bytes_after']}|{'restore_sample_versions':len(results),'restore_sample_bytes':used,'compressed_inventory_bytes':(P/'inventory-checkpoint.jsonl.gz').stat().st_size}))
