"""Local-only consistent SQLite backup and independent inventory/cache audit."""
from pathlib import Path
import sqlite3,json,hashlib,datetime,shutil,gzip,urllib.parse,collections
P=Path(__file__).resolve().parent;BASE=P.parent
DATA=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data')
reserve=20*1024**3
def save(n,v):(P/n).write_bytes((json.dumps(v,indent=2)+'\n').encode())
def digest(path):
 a=hashlib.sha1();b=hashlib.sha256();n=0
 with path.open('rb')as f:
  while c:=f.read(128*1024):a.update(c);b.update(c);n+=len(c)
 return {'sha1':a.hexdigest(),'sha256':b.hexdigest(),'bytes':n}
snapshot=P/'inventory-consistent.sqlite'
if not snapshot.exists():
 assert shutil.disk_usage(P).free>reserve+2*(DATA/'inventory.sqlite').stat().st_size
 src=sqlite3.connect((DATA/'inventory.sqlite').as_uri()+'?mode=ro',uri=True)
 dst=sqlite3.connect(snapshot);src.backup(dst,pages=1000,sleep=.05);dst.close();src.close()
db=sqlite3.connect(snapshot.as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
observed=datetime.datetime.now(datetime.timezone.utc).isoformat()
files={r['title']:dict(r)for r in db.execute('SELECT title,current_url,timestamp,sha1,bytes,mime,history_done FROM files')}
versions=[dict(r)for r in db.execute('SELECT * FROM versions')];images=[r for r in versions if r['mime'].startswith('image/')]
by_title=collections.defaultdict(list)
for r in versions:by_title[r['title']].append(r)
usage=collections.Counter(r['title']for r in db.execute('SELECT title FROM usage'))
descriptions={r['title']:r['revid']for r in db.execute('SELECT title,revid FROM descriptions')}
backups={r['version_id']:dict(r)for r in db.execute('SELECT * FROM local_backups')}
problems=collections.defaultdict(list);alias_groups=collections.defaultdict(list);export=[]
for r in versions:
 if not r['mime'].startswith('image/'):continue
 m=json.loads(r['metadata']);f=files.get(r['title']);u=urllib.parse.urlsplit(r['url'])
 identity=hashlib.sha256(json.dumps([r['title'],r['timestamp'],r['sha1'],r['url']],ensure_ascii=False).encode()).hexdigest()
 if identity!=r['id']:problems['version_id_mismatch'].append(r['id'])
 if u.scheme!='https'or u.netloc!='wiki.swccg.com'or not u.path.startswith('/images/'):problems['non_wiki_image_url'].append({'id':r['id'],'title':r['title']})
 if not f:problems['orphan_version'].append(r['id'])
 elif r['current']and(r['sha1']!=f['sha1']or r['timestamp']!=f['timestamp']or r['bytes']!=f['bytes']):problems['stale_current_flag'].append(r['id'])
 if m.get('width')is None or m.get('height')is None:problems['missing_dimensions'].append(r['id'])
 if r['status']=='verified'and(not r['source_sha256']or r['source_sha256']!=r['archive_sha256']or not r['capture']or not r['verified_at']):problems['incomplete_verified_receipt'].append(r['id'])
 alias_groups[(r['title'],r['timestamp'],r['sha1'])].append(r)
 b=backups.get(r['id'],{})
 export.append({'version_id':r['id'],'title':r['title'],'url':r['url'],'timestamp':r['timestamp'],'sha1':r['sha1'],'bytes':r['bytes'],'mime':r['mime'],'current':bool(r['current']),'width':m.get('width'),'height':m.get('height'),'usage_count':usage[r['title']],'description_revision':descriptions.get(r['title']),'local_status':b.get('status'),'local_sha256':b.get('sha256'),'local_path':b.get('path'),'archive_status':r['status']})
for t,f in files.items():
 if not f['mime'].startswith('image/'):continue
 matches=[r for r in by_title[t]if r['timestamp']==f['timestamp']and r['sha1']==f['sha1']and r['url']==f['current_url']]
 if len(matches)!=1:problems['current_file_mapping'].append({'title':t,'matches':len(matches)})
 if not f['history_done']:problems['unscanned_history'].append(t)
 if t not in descriptions:problems['missing_file_description'].append(t)
aliases=[{'title':k[0],'timestamp':k[1],'sha1':k[2],'rows':[{'id':r['id'],'url':r['url'],'current':r['current']}for r in v]}for k,v in alias_groups.items()if len(v)>1]
prior=json.loads((BASE/'cache-readback.json').read_bytes());known={r['version_id']:r for r in prior['rows']}
new_checks=[];inherited=[]
for r in images:
 b=backups.get(r['id'])
 if not b or b['status']!='backed_up':continue
 k=known.get(r['id'])
 if k and k['sha256']==b['sha256']and k['bytes']==r['bytes']:
  inherited.append(r['id']);continue
 src=(DATA/'offline-originals'/b['path']).resolve();assert src.is_relative_to((DATA/'offline-originals').resolve())
 h=digest(src);sha1=int(r['sha1'],16)if len(r['sha1'])==40 else int(r['sha1'],36)
 assert h['sha256']==b['sha256']and h['bytes']==r['bytes']and int(h['sha1'],16)==sha1
 new_checks.append({'version_id':r['id'],'title':r['title'],'sha256':h['sha256'],'bytes':h['bytes'],'source_sha1_and_size_match':True})
raw=b''.join((json.dumps(r,ensure_ascii=False)+'\n').encode()for r in export)
(P/'inventory.jsonl.gz').write_bytes(gzip.compress(raw,mtime=0));assert gzip.decompress((P/'inventory.jsonl.gz').read_bytes())==raw
save('new-cache-readback.json',{'observed_at':observed,'archive_org_requests':0,'newly_read_back':len(new_checks),'newly_read_back_bytes':sum(r['bytes']for r in new_checks),'inherited_checked_mappings':len(inherited),'prior_immutable_evidence':'https://github.com/billbisco/swccg-wiki/commit/2c80779e4560c96202a5e22605689ffff9a63263','rows':new_checks})
report={'observed_at':observed,'archive_org_requests':0,'source_ledger_writes':0,'snapshot':digest(snapshot),'snapshot_integrity_check':'ok','image_version_rows':len(images),'current_image_filenames':sum(f['mime'].startswith('image/')for f in files.values()),'current_flagged_image_rows':sum(r['current']for r in images),'historical_flagged_image_rows':sum(not r['current']for r in images),'non_image_version_rows':len(versions)-len(images),'image_type_counts':dict(collections.Counter(r['mime']for r in images)),'raw_archive_status_counts':dict(collections.Counter(r['status']for r in images)),'local_backup_status_counts':dict(collections.Counter(r['status']for r in backups.values())),'problem_counts':{k:len(v)for k,v in problems.items()},'problems':dict(problems),'same_upload_url_alias_candidates':aliases,'newly_rehashed_versions':len(new_checks),'previously_checked_exact_mappings':len(inherited),'inventory_compressed':digest(P/'inventory.jsonl.gz'),'pc_free_bytes':shutil.disk_usage(P).free,'pc_reserve_bytes':reserve,'coverage_complete':False,'limitations':['Read-only frozen checkpoint; ongoing owner may subsequently correct mappings or add backups','No final Wiki delta; no fresh Archive.org request or verification','Snapshot includes File descriptions for local recovery; raw DB is retained on PC, not published as shared evidence']}
save('quality-report.json',report);db.close()
print(json.dumps({k:report[k]for k in ['observed_at','image_version_rows','problem_counts','local_backup_status_counts','newly_rehashed_versions','previously_checked_exact_mappings','pc_free_bytes']}),flush=True)
