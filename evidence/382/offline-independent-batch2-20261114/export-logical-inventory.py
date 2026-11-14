from pathlib import Path
import sqlite3,json,gzip,hashlib,datetime,collections
P=Path(__file__).resolve().parent
source=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data/inventory.sqlite')
db=sqlite3.connect(source.as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
rows=[dict(r)for r in db.execute("SELECT v.*,a.upload_id,b.status local_status,b.sha256 local_sha256 FROM versions v JOIN version_aliases a ON a.version_id=v.id LEFT JOIN local_backups b ON b.version_id=v.id WHERE v.mime LIKE 'image/%'ORDER BY v.title,v.timestamp,v.id")]
uploads={r['upload_id']:dict(r)for r in db.execute('SELECT * FROM upload_versions')}
usage=collections.Counter(r[0]for r in db.execute('SELECT title FROM usage'));desc={r[0]:r[1]for r in db.execute('SELECT title,revid FROM descriptions')}
groups=collections.defaultdict(list)
for r in rows:groups[r['upload_id']].append(r)
out=[]
for uid,aliases in groups.items():
 u=uploads[uid];first=aliases[0];m=json.loads(first['metadata'])
 assert all(r['title']==first['title']and r['timestamp']==first['timestamp']and r['sha1']==first['sha1']and r['bytes']==first['bytes']for r in aliases)
 current=[r for r in aliases if r['current']];assert len(current)<=1
 assert not current or u['current_version_id']==current[0]['id']
 out.append({'upload_id':uid,'title':first['title'],'timestamp':first['timestamp'],'sha1':first['sha1'],'bytes':first['bytes'],'mime':first['mime'],'width':m.get('width'),'height':m.get('height'),'current':bool(current),'canonical_current_version_id':current[0]['id']if current else None,'usage_count':usage[first['title']],'description_revision':desc.get(first['title']),'aliases':[{'version_id':r['id'],'url':r['url'],'current':bool(r['current']),'archive_status':r['status'],'local_status':r['local_status'],'local_sha256':r['local_sha256']}for r in aliases]})
assert len(out)==36616 and len(rows)==36617 and sum(r['current']for r in out)==31379
raw=b''.join((json.dumps(r,ensure_ascii=False)+'\n').encode()for r in out);compressed=gzip.compress(raw,mtime=0)
(P/'logical-inventory.jsonl.gz').write_bytes(compressed);assert gzip.decompress((P/'logical-inventory.jsonl.gz').read_bytes())==raw
report={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_org_requests':0,'source_ledger_writes':0,'upload_events':len(out),'exact_url_alias_rows':len(rows),'current_uploads':sum(r['current']for r in out),'historical_uploads':sum(not r['current']for r in out),'all_alias_rows_retained':sum(len(r['aliases'])for r in out)==len(rows),'compressed_sha256':hashlib.sha256(compressed).hexdigest(),'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'compressed_bytes':len(compressed),'local_backup_alias_rows_at_export':sum(r['local_status']=='backed_up'for r in rows),'final_delta_complete':False,'note':'Logical grouping fixes the known same-upload URL alias without deleting source mappings or conflating equal bytes uploaded at different dates. This is still the initial inventory, not final Wiki delta reconciliation.'}
(P/'logical-inventory-report.json').write_bytes((json.dumps(report,indent=2)+'\n').encode());db.rollback();db.close();print(json.dumps(report))
