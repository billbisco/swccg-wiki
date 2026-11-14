"""PC-local resumable ledger; no image payloads in SQLite."""
import contextlib
import datetime
import json
import shutil
import sqlite3
from pathlib import Path

@contextlib.contextmanager
def batch_lock(directory):
    """An OS lock is released on exit/crash; no stale PID lock can resubmit work."""
    f=Path(directory,'capture.lock').open('a+b')
    if f.tell()==0:f.write(b'0');f.flush()
    f.seek(0)
    try:
        import os
        if os.name=='nt':
            import msvcrt
            msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
        else:
            import fcntl
            fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        yield
    finally:
        f.close()

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def connect(directory):
    root=Path(directory);root.mkdir(parents=True,exist_ok=True)
    ensure_space(root)
    db=sqlite3.connect(root/'inventory.sqlite',timeout=30)
    db.row_factory=sqlite3.Row
    db.executescript('''
      CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS files(title TEXT PRIMARY KEY,current_url TEXT,mime TEXT,bytes INTEGER,
        sha1 TEXT,timestamp TEXT,metadata TEXT,history_done INTEGER DEFAULT 0);
      CREATE TABLE IF NOT EXISTS versions(id TEXT PRIMARY KEY,title TEXT,url TEXT,timestamp TEXT,
        sha1 TEXT,bytes INTEGER,mime TEXT,current INTEGER,metadata TEXT,status TEXT DEFAULT 'pending',
        source_sha256 TEXT,capture TEXT,archive_sha256 TEXT,verified_at TEXT,error TEXT,attempts INTEGER DEFAULT 0);
      CREATE TABLE IF NOT EXISTS usage(title TEXT,pageid INTEGER,page TEXT,ns INTEGER,PRIMARY KEY(title,pageid));
      CREATE TABLE IF NOT EXISTS descriptions(title TEXT PRIMARY KEY,revid INTEGER,text TEXT);
      CREATE TABLE IF NOT EXISTS events(time TEXT,event TEXT,data TEXT);
    ''')
    return db

def ensure_space(directory):
    if shutil.disk_usage(directory).free < 20*1024**3:
        raise RuntimeError('PC disk reserve reached: less than 20 GiB free')

def getmeta(db,key,default=None):
    r=db.execute('SELECT value FROM meta WHERE key=?',(key,)).fetchone()
    return json.loads(r[0]) if r else default

def setmeta(db,key,value):
    db.execute('INSERT OR REPLACE INTO meta VALUES (?,?)',(key,json.dumps(value)))

def version_id(title,info):
    import hashlib
    return hashlib.sha256(json.dumps([title,info['timestamp'],info['sha1'],info['url']],ensure_ascii=False).encode()).hexdigest()

def add_version(db,title,info,current):
    if not info.get('url') or not info.get('sha1') or not info.get('timestamp'):
        raise ValueError('Public version missing identity')
    db.execute('''INSERT INTO versions(id,title,url,timestamp,sha1,bytes,mime,current,metadata)
      VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET current=excluded.current,metadata=excluded.metadata''',
      (version_id(title,info),title,info['url'],info['timestamp'],info['sha1'],info['size'],info.get('mime',''),int(current),json.dumps(info)))

def event(db,name,data):
    db.execute('INSERT INTO events VALUES(?,?,?)',(now(),name,json.dumps(data)));db.commit()

def report(db,directory):
    q=lambda sql:db.execute(sql).fetchone()[0]
    data={'observed_at':now(),'cutoff':getmeta(db,'cutoff'),'current_files':q('SELECT COUNT(*) FROM files'),
      'current_image_files':q("SELECT COUNT(*) FROM files WHERE mime LIKE 'image/%'"),
      'current_total_bytes':q('SELECT COALESCE(SUM(bytes),0) FROM files'),
      'public_image_versions':q("SELECT COUNT(*) FROM versions WHERE mime LIKE 'image/%'"),
      'public_image_version_bytes':q("SELECT COALESCE(SUM(bytes),0) FROM versions WHERE mime LIKE 'image/%'"),
      'files_with_history_scanned':q('SELECT COUNT(*) FROM files WHERE history_done=1'),
      'scanned_unused_files':q('SELECT COUNT(*) FROM files f WHERE history_done=1 AND NOT EXISTS(SELECT 1 FROM usage u WHERE u.title=f.title)'),
      'current_image_bytes':q("SELECT COALESCE(SUM(bytes),0) FROM files WHERE mime LIKE 'image/%'"),
      'unique_inventoried_image_hashes':q("SELECT COUNT(DISTINCT sha1) FROM versions WHERE mime LIKE 'image/%'"),
      'inventory_complete':getmeta(db,'inventory_complete',False),
      'states':dict(db.execute("SELECT status,COUNT(*) FROM versions WHERE mime LIKE 'image/%' GROUP BY status")),
      'site_statistics_start':getmeta(db,'site_statistics'),
      'storage':'PC-local metadata; streamed verification; no server-side payload staging'}
    Path(directory,'coverage.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    return data
