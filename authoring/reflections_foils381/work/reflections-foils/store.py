"""Scoped partial-repository backup; never checks out or rewrites unrelated files."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;mode=sys.argv[1]
repo={'wiki':'work/wiki-source','evidence':'work/japanese-preservation/evidence-repo','images':'work/japanese-files-backup.git','sources':'work/japanese-files-backup.git'}[mode]
branch='codex/reflections-foil-publication-381' if mode=='wiki' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((root/(mode+'.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):
    e=dict(env)
    if args[0]=='show':e.pop('GIT_NO_LAZY_FETCH',None)
    return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=e)
exists=git('ls-remote','--heads','origin','refs/heads/'+branch).strip()
git('fetch','origin',branch if exists else 'main');parent=git('rev-parse','FETCH_HEAD').decode().strip();base=parent;parents=[parent]
if mode=='wiki':
    git('fetch','origin','main');base=git('rev-parse','FETCH_HEAD').decode().strip()
    if base!=parent:parents.append(base)
files={}
if mode in ['images','sources']:
    import hashlib
    records=json.loads((root/'uploaded-images.json').read_bytes()) if mode=='images' else json.loads((root/'psa-originals.json').read_bytes())+list(map(json.loads,(root/'swca-originals-results.jsonl').read_text(encoding='utf8').splitlines()))
    for r in records:
        if 'local_file' not in r:continue
        binary=(root/r['local_file']).read_bytes();assert hashlib.sha256(binary).hexdigest()==r['sha256']
        path='files/'+r['name'] if mode=='images' else 'sources/381/'+r['local_file'].replace('\\','/')
        files[path]=binary
else:
    prefix='authoring/reflections_foils381/work/reflections-foils/' if mode=='wiki' else 'evidence/381/'
    for p in root.iterdir():
        if p.is_file() and p.suffix in ['.py','.md','.json','.jsonl','.csv','.wiki','.txt','.webp','.png','.gz']:
            b=p.read_bytes()
            if p.suffix not in ['.webp','.png','.gz']:b=b.replace(b'\r\n',b'\n')
            if p.suffix in ['.py','.md','.txt']:b=b.rstrip()+b'\n'
            if p.suffix=='.txt':b=b'\n'.join(line.rstrip(b' \t') for line in b.split(b'\n'))
            # Original bytes live in the image repository; do not duplicate base64
            # payloads in every evidence/source commit. upload-batch.py regenerates them.
            if p.name.endswith('-files-payload.json'):
                payload=json.loads(b)
                for row in payload:row.pop('data',None)
                b=(json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode()
            files[prefix+p.name]=b
    if mode=='evidence' and (root/'design-log.md').exists():files['docs/design-log/381-reflections-foils.md']=(root/'design-log.md').read_bytes().replace(b'\r\n',b'\n')
    if mode=='wiki':
        files['authoring/reflections_foils381/requirements.txt']=b'requests\nbeautifulsoup4\nPillow\nmwparserfromhell==0.7.2\n'
        if (root/'published-heads.json').exists():
            sys.path.insert(0,'work/wiki-tools');from dump_live import wiki_fname
            index=dict(s.split('\t',1) for s in git('show',base+':pages/INDEX.tsv').decode().splitlines() if '\t' in s)
            for title,p in json.loads((root/'published-heads.json').read_bytes()).items():
                path=index.get(title,'pages/'+wiki_fname(title));assert not any(t!=title and q.casefold()==path.casefold() for t,q in index.items())
                index[title]=path;files[path]=(p['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
            files['pages/INDEX.tsv']=''.join(t+'\t'+p+'\n' for t,p in sorted(index.items(),key=lambda x:(x[0].casefold(),x[0]))).encode()
            from datetime import datetime,timezone
            now=datetime.now(timezone.utc).isoformat();done=json.loads(git('show',base+':ops/wayback/done.json'));queue=git('show',base+':ops/wayback/queue.txt').decode().splitlines()
            captures=[]
            for preserve_file in [root/'first-preservation.json',root/'old-primary-preservation.json',*root.glob('batch*-preservation.json')]:
                if preserve_file.exists():
                    r=json.loads(preserve_file.read_bytes())
                    if r.get('verified'):captures.append(r)
                    elif r.get('url'):
                        if r['url'] not in queue:queue.append(r['url'])
                        if done.get(r['url'],{}).get('status')!='verified':done[r['url']]=dict(status='retry',last=now,note='Story381 source snapshot capture pending: '+r.get('error','not captured'),staging_path=r.get('staging_path'))
            for gallery_file in root.glob('batch*-image-gallery-results.json'):
                results=json.loads(gallery_file.read_bytes())
                if isinstance(results,dict):results=[results]
                for r in results:
                    if r.get('kind')=='gallery' and r.get('url') and not r.get('verified'):
                        if r['url'] not in queue:queue.append(r['url'])
            for capture_file in [root/'first-image-captures.jsonl',*root.glob('batch*-image-captures.jsonl')]:
                if not capture_file.exists():continue
                latest={r['url']:r for r in map(json.loads,capture_file.read_text(encoding='utf8').splitlines())}
                captures.extend(r for r in latest.values() if r.get('verified'))
                for url,r in latest.items():
                    if url not in queue:queue.append(url)
                    if not r.get('verified') and done.get(url,{}).get('status')!='verified':
                        done[url]=dict(status='retry',last=now,note='Story381 exact original-image version awaiting a byte-verified replay: '+r.get('error','capture pending'),wiki_image_version=dict(title=r['title'],timestamp=r['version'],sha1=r['sha1'],mime=r['mime']),expected_sha256=r['image_sha256'])
            for r in captures:
                verify=dict(method='sha256',sha256=r['sha256'],bytes=r.get('bytes',r.get('size')),at=now)
                entry=dict(status='verified',capture=r['capture'],last=now,verify=verify,note='Exact original/source snapshot payload verified by MemoryCoreChatGPT (#381)')
                if r.get('version'):entry['wiki_image_version']=dict(title=r['title'],timestamp=r['version'],sha1=r['sha1'],mime=r['mime'])
                done[r['url']]=entry
                if r['url'] not in queue:queue.append(r['url'])
            for citation_file in [root/'old-citation-final.json',*root.glob('batch*-citation-final.json')]:
                if not citation_file.exists():continue
                for r in json.loads(citation_file.read_bytes()).values():
                    if r.get('verify') and r.get('status')=='verified':
                        url=r.get('preserved_url',r['url']);done[url]=dict(status='verified',capture=r['capture'],last=now,verify=r['verify'],note='Inherited foil-family citation preserved and verified (#381)')
                        if url not in queue:queue.append(url)
            pending=root/'preservation-queue.json'
            if pending.exists():
                for item in json.loads(pending.read_bytes()).values():
                    if item.get('worker_url') and item['worker_url'] not in queue:queue.append(item['worker_url'])
            files['ops/wayback/done.json']=(json.dumps(done,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
            files['ops/wayback/queue.txt']=('\n'.join(queue).rstrip()+'\n').encode()
git('read-tree',base);updates=[]
# Most large evidence blobs already exist after the previous checkpoint. Check
# all object identities together; write only new blobs, keeping updates scoped.
assert git('rev-parse','--show-object-format').strip()==b'sha1'
objects={path:hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest() for path,b in files.items()}
unique=list(dict.fromkeys(objects.values()))
checked=git('cat-file','--batch-check=%(objectname) %(objecttype)',data=('\n'.join(unique)+'\n').encode()).decode().splitlines()
present={line.split()[0] for line in checked if line.endswith(' blob')}
for path,b in files.items():
    oid=objects[path]
    if oid not in present:
        assert git('hash-object','-w','--stdin',data=b).decode().strip()==oid
        present.add(oid)
    updates.append('100644 '+oid+'\t'+path+'\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip();commit=git('commit-tree',tree,*[a for p in parents for a in ['-p',p]],'-m','Inventory and complete regular Reflections foil publications (Refs swccg-guild/work#381)').decode().strip()
changed=set(p for p in git('diff','--name-only','-z',base,commit).decode().split('\0') if p);assert changed<=set(files)
if mode=='wiki':
    check=subprocess.run(['git','-C',repo,'-c','core.protectNTFS=false','diff','--check',base,commit],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (root/'source-diff-check.txt').write_bytes(check.stdout)
    assert check.returncode==0,check.stdout.decode(errors='replace')[:2500]
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8');print(mode,commit,len(changed),'paths')
