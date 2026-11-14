from pathlib import Path
import sys,json,sqlite3,base64,hashlib,importlib.util
P=Path(__file__).resolve().parent;ROOT=P.parent
sys.path.insert(0,str(ROOT/'wiki-tcgmix-expanded'))
from backup import gh
spec=importlib.util.spec_from_file_location('offline_audit_support',P/'offline-audit.py')
# Do not import the audit module: it intentionally produces a new checkpoint on execution.
from PIL import Image
def save(n,v):(P/n).write_bytes((json.dumps(v,indent=2)+'\n').encode())
receipts=json.loads((ROOT/'modern-timeline-followup-20261114/image-preservation/github-backup.json').read_bytes())['receipts']
receipts.append(json.loads((ROOT/'modern-timeline-completion-20261114/images/lead-backup-receipt.json').read_bytes())['receipt'])
dbpath=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data/inventory.sqlite')
db=sqlite3.connect(dbpath.as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');out=[]
restored=P/'github-restore-sample';restored.mkdir(exist_ok=True)
for receipt in receipts:
 s=receipt['subject'];storage=receipt['storage'];repo=storage['repository'].replace('https://github.com/','repos/')
 info=gh(repo+'/contents/'+storage['path']+'?ref='+storage['commit']);blob=gh(repo+'/git/blobs/'+info['sha']);payload=base64.b64decode(blob['content'])
 assert len(payload)==s['bytes']and hashlib.sha256(payload).hexdigest()==s['content_sha256']
 rows=db.execute('SELECT id,title,url,timestamp,sha1,bytes,mime,current,status FROM versions WHERE url=?AND timestamp=?',(s['original_version_url'],s['upload_timestamp'])).fetchall();row,=rows
 sh=hashlib.sha1(payload).hexdigest();assert row['bytes']==len(payload)and int(row['sha1'],16)==int(sh,16)
 path=restored/Path(storage['path']).name;path.write_bytes(payload);assert path.read_bytes()==payload
 with Image.open(path)as im:im.verify()
 with Image.open(path)as im:im.load();shape=[im.width,im.height]
 out.append({'version_id':row['id'],'title':row['title'],'original_url':row['url'],'upload_timestamp':row['timestamp'],'mime':row['mime'],'bytes':len(payload),'sha256':s['content_sha256'],'mediawiki_sha1_matches':True,'image_decodes':True,'dimensions':shape,'backup_repository':storage['repository'],'backup_commit':storage['commit'],'backup_path':storage['path'],'independent_github_restore':'PASS','archive_status':row['status'],'local_ledger_modified':False})
aliases=[]
for group in db.execute("SELECT title,timestamp,sha1,count(*)n FROM versions WHERE mime LIKE 'image/%'GROUP BY title,timestamp,sha1 HAVING count(*)>1"):
 rows=[dict(r)for r in db.execute('SELECT id,title,url,timestamp,sha1,bytes,current,status FROM versions WHERE title=?AND timestamp=?AND sha1=?',(group['title'],group['timestamp'],group['sha1']))]
 current=dict(db.execute('SELECT title,current_url,timestamp,sha1,bytes FROM files WHERE title=?',(group['title'],)).fetchone())
 aliases.append({'file':current,'rows':rows,'classification':'Same-title/timestamp/SHA1 source-URL alias candidate; retain both exact URL mappings, do not count as two distinct upload events without reconciliation','canonical_current_candidate':current['current_url'],'needs_owner_reconciliation':True,'live_history_refetch_performed':False,'ledger_modified':False})
db.rollback();db.close()
report={'issue':382,'archive_org_requests':0,'github_restore_samples':out,'source_url_alias_candidates':aliases,'ledger_writes':0,'duplicate_downloaders_started':0,'active_bulk_backup_owner_unchanged':True,'important_count_note':'Raw image-version table rows include the alias candidate. Neither deduplicated upload-event total nor final historical count is claimed until owner reconciles final metadata delta.'}
save('github-restore-and-alias-reconciliation.json',report)
print(json.dumps({'independent_github_restores':len(out),'alias_candidates':len(aliases),'archive_org_requests':0,'ledger_writes':0}))
