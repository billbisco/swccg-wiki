"""Read the established queue's receipts and independently verify on the PC; never submit saves."""
import argparse,json,os,sqlite3,subprocess,sys,time
from pathlib import Path
from .store import connect,report,now,ensure_space,batch_lock
from .runner import verify_one
from .network import Throttled

DATA=Path('work/image382/data')
REMOTE="import json; from pathlib import Path; d=json.loads(Path('/opt/swccg-ops/repos/swccg-wiki/ops/wayback/done.json').read_text()); print(json.dumps({u:e for u,e in d.items() if u.startswith('https://wiki.swccg.com/images/')}))"
def once(db,limit=25):
    receipts=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=15','gemp','python3 -'],input=REMOTE,text=True,encoding='utf-8',timeout=45))
    (DATA/'queue-image-receipts.json').write_text(json.dumps(receipts,indent=2))
    checked=verified=0
    for url,entry in receipts.items():
        if not entry.get('capture') or entry.get('status') not in ('verified','ok','pending'):continue
        rows=db.execute("SELECT * FROM versions WHERE url=? AND mime LIKE 'image/%' AND status NOT IN ('verified','needs_reconciliation')",(url,)).fetchall()
        for r in rows:
            if checked>=limit:return {'checked':checked,'verified':verified,'receipt_urls':len(receipts)}
            ensure_space(DATA);info=dict(r);checked+=1
            try:
                source,archive=verify_one(info,entry['capture'])
                db.execute("UPDATE versions SET status='verified',capture=?,source_sha256=?,archive_sha256=?,verified_at=?,error=NULL WHERE id=?",(entry['capture'],source['sha256'],archive['sha256'],now(),info['id']))
                verified+=1;print('QUEUE_VERIFIED',info['title'],flush=True)
            except Throttled:
                db.commit();raise
            except (ValueError,OSError) as e:
                db.execute("UPDATE versions SET attempts=attempts+1,error=?,status=CASE WHEN attempts>=2 THEN 'needs_reconciliation' ELSE 'retry' END WHERE id=?",(str(e)[:500],info['id']))
                print('QUEUE_VERIFY_RETRY',info['title'],str(e)[:160],flush=True)
            db.commit();report(db,DATA);time.sleep(5)
    return {'checked':checked,'verified':verified,'receipt_urls':len(receipts)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--once',action='store_true');p.add_argument('--data',default='work/image382/data');a=p.parse_args();DATA=Path(a.data)
    db=connect(DATA)
    with batch_lock(DATA):
        while True:
            state={'pid':os.getpid(),'observed_at':now(),'role':'read queue receipts and verify only','status':'running'}
            wait=120
            try:state['result']=once(db)
            except Throttled as e:state.update(status='backoff',retry_after=e.retry_after);wait=max(120,e.retry_after)
            except (OSError,subprocess.SubprocessError,json.JSONDecodeError) as e:state.update(status='retry_metadata',error=type(e).__name__)
            state['observed_at']=now();(DATA/'queue-runtime.json').write_text(json.dumps(state,indent=2));print(json.dumps(state),flush=True)
            if a.once:break
            time.sleep(wait)
