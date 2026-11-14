"""Public Wiki metadata CLI. Provider capture/replay commands are retired."""
import argparse,json
from .store import connect,report
from .inventory import current,histories
from .runner import RETIRED

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['inventory','histories','report','batch','run','restore'])
    p.add_argument('--data',default='work/image382/data')
    p.add_argument('--limit',type=int,default=10,help='Legacy compatibility only; provider commands are retired')
    p.add_argument('--history-batches',type=int,default=0)
    p.add_argument('--title',action='append',help='Legacy compatibility only')
    a=p.parse_args()
    if a.command in ('batch','run','restore'):p.error(RETIRED)
    db=connect(a.data)
    try:
        if a.command=='inventory':current(db,a.data)
        elif a.command=='histories':histories(db,a.data,a.history_batches)
        print(json.dumps(report(db,a.data),indent=2),flush=True)
    finally:db.close()
if __name__=='__main__':main()
