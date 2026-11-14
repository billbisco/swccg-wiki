"""Recover a bounded representative sample from Archive.org alone."""
import json
from pathlib import Path
from .network import stream_hash,raw_capture
from .store import ensure_space,now

def sample(db,directory):
    root=Path(directory,'restore-sample');root.mkdir(exist_ok=True)
    selected={}
    for mime in ('image/gif','image/jpeg','image/png','image/webp','image/svg+xml'):
        row=db.execute("SELECT * FROM versions WHERE status='verified' AND mime=? ORDER BY bytes DESC LIMIT 1",(mime,)).fetchone()
        if row:selected[row['id']]=dict(row)
    for query in ("SELECT * FROM versions WHERE status='verified' AND current=0 LIMIT 1",
      "SELECT v.* FROM versions v JOIN files f ON f.title=v.title WHERE v.status='verified' AND f.history_done=1 AND NOT EXISTS(SELECT 1 FROM usage u WHERE u.title=f.title) LIMIT 1",
      "SELECT * FROM versions WHERE status='verified' AND title='File:Promo-Foil-L-itcouldbeworse.jpg' LIMIT 1"):
        row=db.execute(query).fetchone()
        if row:selected[row['id']]=dict(row)
    total=sum(p.stat().st_size for p in root.iterdir() if p.is_file())
    results=[]
    for info in selected.values():
        ensure_space(directory)
        target=root/(info['id']+'.bin')
        if total+info['bytes']>1024**3:raise RuntimeError('Recovery sample 1 GiB cap reached')
        result=stream_hash(raw_capture(info['capture'],info['url']),info['mime'],info['bytes'],target)
        if result['sha256']!=info['source_sha256']:raise ValueError('Recovered sample hash differs from recorded original')
        total+=info['bytes']
        results.append({'id':info['id'],'title':info['title'],'upload_timestamp':info['timestamp'],'mime':info['mime'],
          'historical':not bool(info['current']),'original_url':info['url'],'capture':info['capture'],
          'restored_file':target.name,'bytes':info['bytes'],'sha256':result['sha256'],'matches_recorded_original':True})
    report={'at':now(),'source':'Archive.org raw payloads only; no live image fetches','sample':results,'bytes_retained':total,'limit_bytes':1024**3}
    Path(directory,'restore-report.json').write_text(json.dumps(report,indent=2))
    return report
