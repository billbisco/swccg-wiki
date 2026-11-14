import json
import time
from .network import api
from .store import add_version,getmeta,setmeta,now,report

def current(db,directory):
    if not getmeta(db,'cutoff'):
        setmeta(db,'cutoff',now())
        setmeta(db,'site_statistics',api(action='query',meta='siteinfo',siprop='statistics')['query']['statistics'])
        db.commit()
    if getmeta(db,'current_complete'):return
    cont=getmeta(db,'current_continue',{})
    while True:
        d=api(action='query',list='allimages',ailimit=500,aiprop='timestamp|url|size|sha1|mime|dimensions',**cont)
        for x in d['query']['allimages']:
            title='File:'+x['name']
            db.execute('''INSERT INTO files(title,current_url,mime,bytes,sha1,timestamp,metadata) VALUES(?,?,?,?,?,?,?)
              ON CONFLICT(title) DO UPDATE SET current_url=excluded.current_url,mime=excluded.mime,bytes=excluded.bytes,
              sha1=excluded.sha1,timestamp=excluded.timestamp,metadata=excluded.metadata''',
              (title,x['url'],x['mime'],x['size'],x['sha1'],x['timestamp'],json.dumps(x)))
            add_version(db,title,x,True)
        cont=d.get('continue',{})
        setmeta(db,'current_continue',cont)
        if not cont:setmeta(db,'current_complete',True)
        db.commit();r=report(db,directory)
        print('CURRENT_INVENTORY',r['current_files'],r['current_total_bytes'],flush=True)
        if not cont:return
        time.sleep(.2)

def histories(db,directory,max_batches=0):
    batches=0
    while True:
        titles=[r[0] for r in db.execute('SELECT title FROM files WHERE history_done=0 ORDER BY title LIMIT 25')]
        if not titles:
            if getmeta(db,'current_complete'):setmeta(db,'inventory_complete',True)
            db.commit();report(db,directory);return
        cont={}
        while True:
            d=api(action='query',titles='|'.join(titles),prop='imageinfo|fileusage|revisions',
              iiprop='timestamp|url|size|sha1|mime|archivename',iilimit='max',fulimit='max',
              rvprop='ids|content',rvslots='main',**cont)
            for p in d['query']['pages']:
                # allimages uses database filenames; title queries normalize underscores to spaces.
                title=p['title'].replace(' ','_')
                current_row=db.execute('SELECT sha1,timestamp FROM files WHERE title=?',(title,)).fetchone()
                if not current_row:continue
                for x in p.get('imageinfo',[]):
                    x['canonical_title']=p['title']
                    add_version(db,title,x,x['sha1']==current_row['sha1'] and x['timestamp']==current_row['timestamp'])
                for u in p.get('fileusage',[]):
                    db.execute('INSERT OR REPLACE INTO usage VALUES(?,?,?,?)',(title,u['pageid'],u['title'],u['ns']))
                for rev in p.get('revisions',[]):
                    text=rev.get('slots',{}).get('main',{}).get('content')
                    if text is not None:db.execute('INSERT OR REPLACE INTO descriptions VALUES(?,?,?)',(title,rev['revid'],text))
            cont=d.get('continue',{});db.commit()
            if not cont:break
            time.sleep(.2)
        db.executemany('UPDATE files SET history_done=1 WHERE title=?',[(t,) for t in titles]);db.commit()
        batches+=1;r=report(db,directory)
        if batches%10==0:print('HISTORY_INVENTORY',r['files_with_history_scanned'],r['public_image_versions'],flush=True)
        if max_batches and batches>=max_batches:return
