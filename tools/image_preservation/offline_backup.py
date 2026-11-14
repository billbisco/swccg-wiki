"""PC-local original-byte backups. Transport permits Wiki images only, never Archive.org."""
import argparse,hashlib,json,os,re,shutil,sqlite3,time,urllib.error,urllib.parse,urllib.request
from pathlib import Path
from .store import connect,batch_lock,ensure_space,now

CAP=25*1024**3

def wiki_image_url(url):
    p=urllib.parse.urlsplit(url)
    if p.scheme!='https' or p.netloc!='wiki.swccg.com' or not p.path.startswith('/images/'):
        raise ValueError('Offline backup transport permits only https://wiki.swccg.com/images/ URLs')
    return url

class WikiOnlyRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        wiki_image_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def hashes(path):
    a=hashlib.sha1();b=hashlib.sha256();n=0
    with path.open('rb') as f:
        while chunk:=f.read(128*1024):a.update(chunk);b.update(chunk);n+=len(chunk)
    return {'sha1':a.hexdigest(),'sha256':b.hexdigest(),'bytes':n}

def source_identity(info,result):
    sha=info['sha1']
    value=int(sha,16) if re.fullmatch('[0-9a-fA-F]{40}',sha) else int(sha,36)
    if value!=int(result['sha1'],16) or result['bytes']!=info['bytes']:
        raise ValueError('Source differs from inventoried version; needs metadata reconciliation')

def schema(db):
    db.executescript('''
      CREATE TABLE IF NOT EXISTS backup_objects(sha256 TEXT PRIMARY KEY,path TEXT NOT NULL,bytes INTEGER NOT NULL,verified_at TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS local_backups(version_id TEXT PRIMARY KEY,status TEXT NOT NULL,sha256 TEXT,path TEXT,bytes INTEGER,verified_at TEXT,error TEXT);
    ''')

def download(info,part,opener):
    url=wiki_image_url(info['url'])
    req=urllib.request.Request(url,headers={'User-Agent':'SWCCG-OfflineBackup/1.0 (Story382)','Accept-Encoding':'identity'})
    with opener.open(req,timeout=60) as response,part.open('wb') as out:
        wiki_image_url(response.geturl())
        n=0
        while chunk:=response.read(128*1024):
            n+=len(chunk)
            if n>info['bytes']:raise ValueError('Response larger than inventoried original')
            if n%(8*1024**2)<len(chunk):ensure_space(part.parent)
            out.write(chunk)
        out.flush();os.fsync(out.fileno())

def backup_one(db,info,root,opener,budget):
    ensure_space(root)
    # Reuse only an object independently re-read and tied to the same original SHA-1/size.
    duplicate=db.execute('''SELECT o.* FROM backup_objects o JOIN local_backups b ON b.sha256=o.sha256
      JOIN versions v ON v.id=b.version_id WHERE v.sha1=? AND v.bytes=? AND b.status='backed_up' LIMIT 1''',(info['sha1'],info['bytes'])).fetchone()
    if duplicate:
        target=root/duplicate['path'];result=hashes(target);source_identity(info,result)
        if result['sha256']!=duplicate['sha256']:raise ValueError('Existing local object failed readback')
        return result,duplicate['path']
    part=root/'parts'/(info['id']+'.part');part.parent.mkdir(exist_ok=True)
    if budget['used']+info['bytes']>CAP:raise RuntimeError('Local backup cache reached its 25 GiB cap')
    try:
        download(info,part,opener)
        result=hashes(part);source_identity(info,result)
        rel='objects/'+result['sha256'][:2]+'/'+result['sha256']
        target=root/rel;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            existing=hashes(target)
            if existing!=result:raise ValueError('Content-addressed object failed readback')
            part.unlink()
        else:
            os.replace(part,target);budget['used']+=result['bytes']
        # Independent disk read, not just the network hashing pass.
        if hashes(target)!=result:raise ValueError('New local object failed independent readback')
        return result,rel
    finally:
        if part.exists():part.unlink()

def progress(db,data,root,status):
    result={'observed_at':now(),'pid':os.getpid(),'status':status,'archive_org_requests':0,
      'backup_states':dict(db.execute('SELECT status,count(*) FROM local_backups GROUP BY status')),
      'unique_objects':db.execute('SELECT count(*) FROM backup_objects').fetchone()[0],
      'object_bytes':db.execute('SELECT coalesce(sum(bytes),0) FROM backup_objects').fetchone()[0],
      'cache_cap_bytes':CAP,'pc_free_bytes':shutil.disk_usage(root).free,
      'archive_verified_versions':db.execute("SELECT count(*) FROM versions WHERE status='verified'").fetchone()[0]}
    temp=data/'offline-backup-progress.part';temp.write_text(json.dumps(result,indent=2));os.replace(temp,data/'offline-backup-progress.json')
    return result

def run(data,limit):
    root=data/'offline-originals';root.mkdir(exist_ok=True)
    db=connect(data);schema(db);opener=urllib.request.build_opener(WikiOnlyRedirect())
    with batch_lock(data):
        budget={'used':sum(p.stat().st_size for p in root.rglob('*') if p.is_file())}
        rows=db.execute("SELECT v.* FROM versions v LEFT JOIN local_backups b ON b.version_id=v.id WHERE v.mime LIKE 'image/%' AND b.version_id IS NULL ORDER BY v.current,v.title,v.timestamp").fetchall()
        count=0
        for r in rows:
            if limit and count>=limit:break
            info=dict(r);ensure_space(root)
            try:
                result,path=backup_one(db,info,root,opener,budget)
                verified=now()
                db.execute('INSERT OR REPLACE INTO backup_objects VALUES(?,?,?,?)',(result['sha256'],path,result['bytes'],verified))
                db.execute("INSERT OR REPLACE INTO local_backups VALUES(?,'backed_up',?,?,?,?,NULL)",(info['id'],result['sha256'],path,result['bytes'],verified))
                print('LOCAL_BACKED_UP',info['title'],result['bytes'],flush=True)
            except (ValueError,urllib.error.URLError,TimeoutError) as e:
                db.execute("INSERT OR REPLACE INTO local_backups(version_id,status,error) VALUES(?,'needs_reconciliation',?)",(info['id'],str(e)[:500]))
                print('LOCAL_NEEDS_RECONCILIATION',info['title'],str(e)[:150],flush=True)
            db.commit();count+=1
            progress(db,data,root,'running')
            time.sleep(.5)
        result=progress(db,data,root,'batch_complete' if limit else 'initial_pass_complete')
        print(json.dumps(result),flush=True)
    db.close()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path('work/image382/data'));p.add_argument('--limit',type=int,default=50)
    a=p.parse_args();run(a.data,a.limit)
