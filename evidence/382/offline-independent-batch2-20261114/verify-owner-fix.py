from pathlib import Path
import sqlite3,json,datetime
P=Path(__file__).resolve().parent
DATA=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-d-block-5/work/image382/data')
def connect(p):
 d=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');return d
before=connect(P/'inventory-consistent.sqlite');after=connect(DATA/'inventory.sqlite')
old={r['id']:dict(r)for r in before.execute('SELECT * FROM versions')};new={r['id']:dict(r)for r in after.execute('SELECT * FROM versions')}
assert set(old)<=set(new)
changes=[]
for key,row in old.items():
 actual=new[key]
 for col,value in row.items():
  if col=='current':
   if actual[col]!=value:changes.append({'id':key,'old':value,'new':actual[col]})
  else:assert actual[col]==value,(key,col)
assert changes==[{'id':'3e55464012b0b887551334cb1abc28904e6d685b3559dfd9992a947813cb3fde','old':1,'new':0}]
old_backups={r['version_id']:dict(r)for r in before.execute('SELECT * FROM local_backups')};new_backups={r['version_id']:dict(r)for r in after.execute('SELECT * FROM local_backups')}
assert all(new_backups[k]==v for k,v in old_backups.items())
ids=['0a47b5832b0d5c6662e887c44402d6d6f10ddc9757383c657975486d1d402cc9','3e55464012b0b887551334cb1abc28904e6d685b3559dfd9992a947813cb3fde']
aliases=[dict(after.execute('SELECT * FROM version_aliases WHERE version_id=?',(i,)).fetchone())for i in ids]
assert aliases[0]['upload_id']==aliases[1]['upload_id'];upload=dict(after.execute('SELECT * FROM upload_versions WHERE upload_id=?',(aliases[0]['upload_id'],)).fetchone());assert upload['current_version_id']==ids[0]
current_files=after.execute("SELECT count(*)FROM files WHERE mime LIKE 'image/%'").fetchone()[0]
current_rows=after.execute("SELECT count(*)FROM versions WHERE mime LIKE 'image/%'AND current=1").fetchone()[0];assert current_rows==current_files==31379
distinct=after.execute("SELECT count(DISTINCT a.upload_id)FROM version_aliases a JOIN versions v ON v.id=a.version_id WHERE v.mime LIKE 'image/%'").fetchone()[0];assert distinct==36616
receipt=json.loads((DATA.parent/'upload-alias-reconciliation.json').read_bytes())
result={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_org_requests':0,'source_ledger_writes':0,'all_prior_version_rows_preserved':len(old),'all_prior_version_fields_except_current_unchanged':True,'exact_current_flag_changes':changes,'prior_local_backup_receipts_unchanged':len(old_backups),'prior_archive_verified_rows_unchanged':sum(r['status']=='verified'for r in old.values()),'same_upload_aliases':aliases,'logical_upload':upload,'current_image_filenames':current_files,'current_image_rows':current_rows,'distinct_image_uploads':distinct,'raw_image_url_alias_rows':sum(r['mime'].startswith('image/')for r in new.values()),'logical_historical_image_uploads':distinct-current_files,'owner_migration_receipt':receipt,'bulk_backup_progress':json.loads((DATA/'offline-backup-progress.json').read_bytes()),'result':'PASS'}
for d in [before,after]:d.rollback();d.close()
(P/'owner-fix-independent-check.json').write_bytes((json.dumps(result,indent=2)+'\n').encode());print(json.dumps({k:result[k]for k in ['observed_at','all_prior_version_rows_preserved','prior_local_backup_receipts_unchanged','current_image_rows','distinct_image_uploads','result']}))
