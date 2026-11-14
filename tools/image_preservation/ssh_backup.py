"""Bounded direct source batches into the existing checked local cache. No server staging."""
import argparse,json,os,sqlite3,sys,time
from pathlib import Path
from .store import batch_lock,connect,ensure_space,now
from .offline_backup import CAP,hashes,source_identity,schema,progress
from .ssh_source import start,receive

def record(db,info,result,path):
    checked=now()
    db.execute('INSERT OR REPLACE INTO backup_objects VALUES(?,?,?,?)',(result['sha256'],path,result['bytes'],checked))
    db.execute("INSERT OR REPLACE INTO local_backups VALUES(?,'backed_up',?,?,?,?,NULL)",(info['id'],result['sha256'],path,result['bytes'],checked))
    db.execute('INSERT OR REPLACE INTO local_copy_sources VALUES(?,?,?,?)',(info['id'],'wiki_ssh',info['url'],checked));db.commit()

def run(data,limit=0):
    root=data/'offline-originals';root.mkdir(exist_ok=True);(root/'parts').mkdir(exist_ok=True)
    db=connect(data);schema(db)
    try:
        with batch_lock(data):
            used=sum(p.stat().st_size for p in root.rglob('*') if p.is_file());done=0
            while True:
                ensure_space(root)
                rows=db.execute("SELECT v.* FROM versions v LEFT JOIN local_backups b ON v.id=b.version_id WHERE v.mime LIKE 'image/%' AND b.version_id IS NULL ORDER BY v.current,v.title,v.timestamp LIMIT 500").fetchall()
                if not rows:break
                selected=[];batch_bytes=0
                for row in rows:
                    if limit and done+len(selected)>=limit:break
                    info=dict(row)
                    if selected and batch_bytes+info['bytes']>128*1024**2:break
                    if used+batch_bytes+info['bytes']>CAP:raise RuntimeError('Local cache reached25GiB cap')
                    selected.append(info);batch_bytes+=info['bytes']
                if not selected:break
                print('SOURCE_BATCH',len(selected),batch_bytes,flush=True)
                with (data/'ssh-source-backup-stderr.log').open('ab') as err:
                    proc=start(selected,err)
                    try:
                        for info in selected:
                            ensure_space(root);part=root/'parts'/(info['id']+'.part')
                            try:
                                error=receive(proc,info,part)
                                if error:raise ValueError(error)
                                result=hashes(part);source_identity(info,result)
                                rel='objects/'+result['sha256'][:2]+'/'+result['sha256'];target=root/rel
                                target.parent.mkdir(parents=True,exist_ok=True)
                                if target.exists():
                                    if hashes(target)!=result:raise ValueError('Existing cache object failed readback')
                                    part.unlink()
                                else:os.replace(part,target);used+=result['bytes']
                                if hashes(target)!=result:raise ValueError('New cache object failed independent readback')
                                record(db,info,result,rel)
                                print('LOCAL_BACKED_UP',info['id'],info['title'],result['bytes'],flush=True)
                            except ValueError as error:
                                db.execute("INSERT OR REPLACE INTO local_backups(version_id,status,error) VALUES(?,'needs_reconciliation',?)",(info['id'],str(error)[:500]));db.commit()
                                print('LOCAL_NEEDS_RECONCILIATION',info['id'],str(error)[:180],flush=True)
                            finally:part.unlink(missing_ok=True)
                            done+=1
                            if done%10==0:progress(db,data,root,'running')
                        if proc.stdout.read(1):raise RuntimeError('Trailing source stream bytes')
                        if proc.wait(timeout=30):raise RuntimeError('SSH source batch failed')
                    except BaseException:
                        proc.kill();proc.wait();raise
                    finally:proc.stdout.close()
                progress(db,data,root,'running')
                if limit and done>=limit:break
            result=progress(db,data,root,'batch_complete' if limit else 'initial_pass_complete')
            print('DONE',json.dumps(result),flush=True)
    finally:db.close()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path('work/image382/data'));p.add_argument('--limit',type=int,default=0)
    args=p.parse_args();run(args.data,args.limit)
