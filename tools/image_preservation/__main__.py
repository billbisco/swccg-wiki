import argparse,json,os,time
from pathlib import Path
from .store import connect,report,batch_lock,ensure_space,getmeta,now
from .inventory import current,histories
from .runner import batch,recover_interrupted
from .restore import sample

def main():
    p=argparse.ArgumentParser(description='PC-local verified preservation of public wiki image originals')
    p.add_argument('command',choices=['inventory','histories','batch','run','restore','report'])
    p.add_argument('--data',default='work/image382/data')
    p.add_argument('--limit',type=int,default=10)
    p.add_argument('--history-batches',type=int,default=0)
    p.add_argument('--title',action='append',help='Restrict a pilot to an exact inventory File title; repeat as needed')
    a=p.parse_args();db=connect(a.data)
    if a.command=='inventory':current(db,a.data)
    elif a.command=='histories':histories(db,a.data,a.history_batches)
    elif a.command=='restore':print(json.dumps(sample(db,a.data),indent=2),flush=True)
    elif a.command=='batch':
        with batch_lock(a.data):
            recover_interrupted(db)
            print(json.dumps(batch(db,a.data,a.limit,titles=a.title),indent=2),flush=True)
    elif a.command=='run':
        with batch_lock(a.data):
            recover_interrupted(db)
            throttles=0
            while True:
                ensure_space(a.data)
                state={'pid':os.getpid(),'observed_at':now(),'status':'running','batch_limit':a.limit}
                Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2))
                result=batch(db,a.data,a.limit,titles=a.title)
                state.update(observed_at=now(),last_batch=result)
                if result.get('stopped')=='external_throttle':
                    throttles+=1;state['status']='backoff';state['retry_after']=result['retry_after']
                    if throttles>=3:
                        state['status']='stopped_external_throttle'
                        Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2));break
                    Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2))
                    time.sleep(result['retry_after']);continue
                throttles=0
                # Three unsuccessful validations require reconciliation, not a hot retry loop.
                db.execute("UPDATE versions SET status='needs_reconciliation' WHERE status='retry' AND attempts>=3");db.commit()
                if result['selected']==0:
                    if getmeta(db,'inventory_complete'):
                        state['status']='finished_available_requests'
                        Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2));break
                    state['status']='waiting_for_inventory'
                    Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2));time.sleep(60)
                else:
                    Path(a.data,'runtime.json').write_text(json.dumps(state,indent=2));time.sleep(30)
    print(json.dumps(report(db,a.data),indent=2),flush=True)
    db.close()

if __name__=='__main__':main()
