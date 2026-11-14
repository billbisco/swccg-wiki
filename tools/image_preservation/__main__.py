import argparse,json
from .store import connect,report,batch_lock
from .inventory import current,histories
from .runner import batch,recover_interrupted

def main():
    p=argparse.ArgumentParser(description='PC-local verified preservation of public wiki image originals')
    p.add_argument('command',choices=['inventory','histories','batch','report'])
    p.add_argument('--data',default='work/image382/data')
    p.add_argument('--limit',type=int,default=10)
    p.add_argument('--history-batches',type=int,default=0)
    p.add_argument('--title',action='append',help='Restrict a pilot to an exact inventory File title; repeat as needed')
    a=p.parse_args();db=connect(a.data)
    if a.command=='inventory':current(db,a.data)
    elif a.command=='histories':histories(db,a.data,a.history_batches)
    elif a.command=='batch':
        with batch_lock(a.data):
            recover_interrupted(db)
            print(json.dumps(batch(db,a.data,a.limit,titles=a.title),indent=2),flush=True)
    print(json.dumps(report(db,a.data),indent=2),flush=True)
    db.close()

if __name__=='__main__':main()
