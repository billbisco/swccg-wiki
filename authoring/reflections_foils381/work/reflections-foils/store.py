"""Scoped partial-repository backup; never checks out or rewrites unrelated files."""
import json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;mode=sys.argv[1]
repo={'wiki':'work/wiki-source','evidence':'work/japanese-preservation/evidence-repo','images':'work/japanese-files-backup.git'}[mode]
branch='codex/reflections-foil-articles-381' if mode=='wiki' else 'main'
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
if mode=='images':
    import hashlib
    for r in json.loads((root/'uploaded-images.json').read_bytes()):
        binary=(root/r['local_file']).read_bytes();assert hashlib.sha256(binary).hexdigest()==r['sha256']
        files['files/'+r['name']]=binary
else:
    prefix='authoring/reflections_foils381/work/reflections-foils/' if mode=='wiki' else 'evidence/381/'
    for p in root.iterdir():
        if p.is_file() and p.suffix in ['.py','.md','.json','.jsonl','.csv','.wiki','.txt','.webp','.png','.gz']:
            b=p.read_bytes()
            if p.suffix not in ['.webp','.png','.gz']:b=b.replace(b'\r\n',b'\n')
            if p.suffix in ['.py','.md','.txt']:b=b.rstrip()+b'\n'
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
git('read-tree',base);updates=[]
for path,b in files.items():
    oid=git('hash-object','-w','--stdin',data=b).decode().strip();updates.append('100644 '+oid+'\t'+path+'\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip();commit=git('commit-tree',tree,*[a for p in parents for a in ['-p',p]],'-m','Inventory and complete regular Reflections foil publications (Refs swccg-guild/work#381)').decode().strip()
changed=set(p for p in git('diff','--name-only','-z',base,commit).decode().split('\0') if p);assert changed<=set(files)
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8');print(mode,commit,len(changed),'paths')
