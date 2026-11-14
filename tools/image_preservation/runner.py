"""Serialized capture/check loop with explicit per-version state and bounded batches."""
import json
import re
import time
import urllib.error
import urllib.parse
from .network import open_url,stream_hash,raw_capture,check_hashes,Throttled
from .store import now,event,report

def existing_capture(url):
    with open_url('https://archive.org/wayback/available?url='+urllib.parse.quote(url,safe='')) as r:
        data=json.load(r)
    closest=data.get('archived_snapshots',{}).get('closest',{})
    if closest.get('available') and str(closest.get('status'))=='200':
        return closest['url'].replace('http://web.archive.org/','https://web.archive.org/')
    return None

def save_original(url):
    with open_url('https://web.archive.org/save/'+url) as r:
        final=r.geturl();location=r.headers.get('Content-Location','')
        mime=r.headers.get_content_type()
        # Binary response need not be retained; the verifier fetches raw bytes separately.
        payload=r.read(2*1024*1024) if mime.startswith('text/') else b''
    for value in (final,location,payload.decode('utf-8','replace')):
        m=re.search(r'/web/(\d{14})(?:\*|id_)?/',value)
        if m:return 'https://web.archive.org/web/'+m[1]+'/'+url
    return existing_capture(url)

def verify_one(info,capture):
    source=stream_hash(info['url'],info['mime'],info['bytes'])
    archived=stream_hash(raw_capture(capture,info['url']),info['mime'],info['bytes'])
    check_hashes(info,source,archived)
    return source,archived

def batch(db,directory,limit=10,gap=30,titles=None):
    where="mime LIKE 'image/%' AND status IN ('pending','retry')"
    args=[]
    if titles:
        where+=' AND title IN ('+','.join('?' for _ in titles)+')';args+=titles
    rows=db.execute('SELECT * FROM versions WHERE '+where+' ORDER BY attempts,current DESC,bytes LIMIT ?',(*args,limit)).fetchall()
    summary={'started_at':now(),'selected':len(rows),'verified':0,'retry':0,'stopped':None}
    last_save=0
    for row in rows:
        info=dict(row)
        try:
            needs_new=info['error'] and ('Archived original hash mismatch' in info['error'] or 'Payload size mismatch' in info['error'])
            capture=None if needs_new else (info['capture'] or existing_capture(info['url']))
            if not capture:
                wait=gap-(time.monotonic()-last_save)
                if wait>0:time.sleep(wait)
                db.execute("UPDATE versions SET status='saving',attempts=attempts+1,error=NULL WHERE id=?",(info['id'],));db.commit()
                capture=save_original(info['url']);last_save=time.monotonic()
                if not capture:raise ValueError('Save returned no checked capture; will recheck index')
            db.execute("UPDATE versions SET status='checking',capture=? WHERE id=?",(capture,info['id']));db.commit()
            source,archived=verify_one(info,capture)
            db.execute("UPDATE versions SET status='verified',source_sha256=?,archive_sha256=?,verified_at=?,error=NULL WHERE id=?",
              (source['sha256'],archived['sha256'],now(),info['id']));db.commit()
            summary['verified']+=1
            print('VERIFIED',info['title'],capture,flush=True)
        except Throttled as e:
            db.execute("UPDATE versions SET status='retry',error=? WHERE id=?",(str(e),info['id']));db.commit()
            summary.update(stopped='external_throttle',retry_after=e.retry_after)
            event(db,'throttled',summary);break
        except (ValueError,urllib.error.URLError,TimeoutError) as e:
            db.execute("UPDATE versions SET status='retry',error=?,attempts=attempts+1 WHERE id=?",(str(e)[:500],info['id']));db.commit()
            summary['retry']+=1
            print('RETRY',info['title'],str(e)[:180],flush=True)
        report(db,directory)
    summary['finished_at']=now();event(db,'batch',summary);report(db,directory)
    return summary

def recover_interrupted(db):
    # Saved capture URLs survive; only unfinished requests are retried, never verified rows.
    db.execute("UPDATE versions SET status='retry',error='Interrupted before verification; inspect saved capture' WHERE status IN ('saving','checking')")
    db.commit()
