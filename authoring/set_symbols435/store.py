import json,os,hashlib,subprocess,sys,tarfile,io
from pathlib import Path
p=Path(__file__).parent;mode=sys.argv[1]
repo={'cardmaker':'work/cardmaker-source','wiki':'work/wiki-source','evidence':'work/japanese-preservation/evidence-repo'}[mode]
branch={'cardmaker':'codex/shared-set-symbols-435','wiki':'codex/set-symbols-pilot-435','evidence':'main'}[mode]
env=dict(os.environ,GIT_INDEX_FILE=str((p/(mode+'.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=env)
exists=git('ls-remote','--heads','origin',branch).strip();git('fetch','origin',branch if exists else 'main');parent=git('rev-parse','FETCH_HEAD').decode().strip();git('fetch','origin','main');base=git('rev-parse','FETCH_HEAD').decode().strip();parents=list(dict.fromkeys([parent,base]))
if mode=='cardmaker':
    files={'tools/export_set_symbols.py':(p/'export-symbols.py').read_bytes(),'assets/symbols/README.md':(p/'SYMBOLS-README.md').read_bytes()}
    files.update({'assets/symbols/'+f.name:f.read_bytes() for f in (p/'symbols').iterdir()})
    tree={line.split('\t')[1]:line.split()[2] for line in git('ls-tree','-r',base,'assets/icons').decode().splitlines()}
    for row in json.loads((p/'symbols/manifest.json').read_bytes())['symbols']:
        raw=(p/'cardmaker'/row['source']).read_bytes();oid=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();assert tree[row['source']]==oid,(row['source'],'Source master changed')
else:
    if mode=='wiki':
        with tarfile.open(p/'shared-symbols.tar.xz','w:xz') as t:
            for folder in ['cardmaker','symbols','old-wiki-assets']:
                for f in sorted((p/folder).rglob('*')):
                    if f.is_file():t.add(f,arcname=f.relative_to(p).as_posix())
    prefix='authoring/set_symbols435/' if mode=='wiki' else 'evidence/435/'
    files={prefix+f.name:f.read_bytes() for f in p.iterdir() if f.is_file() and (f.suffix in ['.json','.md','.py','.webp','.html'] or f.name.endswith('.tar.xz'))}
    if mode=='evidence':files['docs/design-log/435-shared-set-symbols.md']=(p/'design-log.md').read_bytes()
git('read-tree',base);updates=[]
for path,data in files.items():
    if path.endswith(('.py','.md','.html','.json')):data=data.replace(b'\r\n',b'\n').rstrip()+b'\n'
    oid=git('hash-object','-w','--stdin',data=data).decode().strip();updates.append('100644 '+oid+'\t'+path+'\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode());tree=git('write-tree','--missing-ok').decode().strip();commit=git('commit-tree',tree,*[a for parent in parents for a in ['-p',parent]],'-m','Share CardMaker set-symbol WebP exports and visual pilot (Refs swccg-guild/work#435)').decode().strip()
assert set(filter(None,git('diff','--name-only','-z',base,commit).decode().split('\0')))<=set(files)
git('diff','--check',base,commit)
git('push','origin',commit+':refs/heads/'+branch);(p/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8');print(mode,commit,len(files),'scoped paths stored')
