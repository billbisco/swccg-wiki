"""Scope-only backup on fresh remote heads, preserving concurrent work."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;mode=sys.argv[1];assert mode in ['wiki','evidence']
repo='work/wiki-source' if mode=='wiki' else 'work/japanese-preservation/evidence-repo'
branch='codex/reflections-foil-tables-430' if mode=='wiki' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((root/(mode+'.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):
    e=dict(env)
    if args[0]=='show':e.pop('GIT_NO_LAZY_FETCH',None)
    return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=e)
exists=git('ls-remote','--heads','origin',branch).strip()
git('fetch','origin',branch if exists else 'main');parent=git('rev-parse','FETCH_HEAD').decode().strip();base=parent;parents=[parent]
if mode=='wiki':
    git('fetch','origin','main');base=git('rev-parse','FETCH_HEAD').decode().strip()
    if base!=parent:parents.append(base)
prefix='authoring/reflections_foil_tables430/work/reflections-foil-tables/' if mode=='wiki' else 'evidence/430/'
files={prefix+p.name:p.read_bytes().replace(b'\r\n',b'\n') if p.suffix not in ['.webp','.gz'] else p.read_bytes() for p in root.iterdir() if p.is_file() and p.suffix in ['.py','.md','.json','.jsonl','.wiki','.txt','.webp','.gz']}
if mode=='evidence' and (root/'design-log.md').exists():files['docs/design-log/430-reflections-foil-tables.md']=(root/'design-log.md').read_bytes().replace(b'\r\n',b'\n')
if mode=='wiki' and (root/'published-heads.json').exists():
    sys.path.insert(0,'work/wiki-tools');from dump_live import wiki_fname
    index=dict(s.split('\t',1) for s in git('show',base+':pages/INDEX.tsv').decode().splitlines() if '\t' in s)
    for title,h in json.loads((root/'published-heads.json').read_bytes()).items():
        path=index.get(title,'pages/'+wiki_fname(title));assert not any(t!=title and p.casefold()==path.casefold() for t,p in index.items());index[title]=path
        files[path]=(h['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
    files['pages/INDEX.tsv']=''.join(t+'\t'+p+'\n' for t,p in sorted(index.items(),key=lambda v:(v[0].casefold(),v[0]))).encode()
for path,data in list(files.items()):
    if path.endswith(('.py','.md','.txt','.wiki')):files[path]=data.rstrip()+b'\n'
git('read-tree',base);updates=[]
for path,data in files.items():
    oid=git('hash-object','-w','--stdin',data=data).decode().strip();updates.append('100644 '+oid+'\t'+path+'\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode());tree=git('write-tree','--missing-ok').decode().strip()
commit=git('commit-tree',tree,*[a for p in parents for a in ['-p',p]],'-m','Display Reflections foil tables and scan contribution requests (Refs swccg-guild/work#430)').decode().strip()
assert set(git('diff','--name-only',base,commit).decode().splitlines())<=set(files)
check=subprocess.run(['git','-C',repo,'-c','core.protectNTFS=false','diff','--check',base,commit],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);assert check.returncode==0,check.stdout.decode()
git('push','origin',commit+':refs/heads/'+branch);(root/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8')
print(mode,commit,len(files),'scoped paths backed up')
