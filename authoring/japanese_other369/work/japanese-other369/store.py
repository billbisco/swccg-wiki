import json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;mode=sys.argv[1]
repo={'wiki':'work/wiki-source','evidence':'work/japanese-preservation/evidence-repo','images':'work/japanese-files-backup.git'}[mode]
branch='codex/japanese-card-audit-369' if mode=='wiki' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((root/(mode+'.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):
    e=dict(env)
    if args[0]=='show':e.pop('GIT_NO_LAZY_FETCH',None)
    return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=e)
exists=git('ls-remote','--heads','origin','refs/heads/'+branch).strip()
git('fetch','origin',branch if exists else 'main');parent=git('rev-parse','FETCH_HEAD').decode().strip();base=parent;parents=[parent]
if mode=='wiki' and (root/'checked-heads.json').exists():
    git('fetch','origin','main');base=git('rev-parse','FETCH_HEAD').decode().strip()
    if base!=parent:parents.append(base)
files={}
if mode=='images':
    files['files/Japanese-Hoth-2-1B-PSA-175224368.jpg']=(root/'2-1b-PSA-175224368.jpg').read_bytes()
else:
    dest='authoring/japanese_other369/' if mode=='wiki' else 'evidence/369/'
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.py','.md','.json','.jsonl','.csv','.txt','.wiki','.webp','.png']:
            binary=path.read_bytes()
            if path.suffix not in ['.png','.webp']:binary=binary.replace(b'\r\n',b'\n')
            if path.suffix in ['.py','.md','.txt']:binary=binary.rstrip()+b'\n'
            files[dest+('work/japanese-other369/' if mode=='wiki' else '')+path.name]=binary
    if mode=='wiki':
        files[dest+'work/wiki-tools/style_lint.py']=Path('work/wiki-tools/style_lint.py').read_bytes().replace(b'\r\n',b'\n')
        files[dest+'work/wiki_title_publish.py']=(Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0].rstrip()+'\n').encode()
        files[dest+'work/japanese-complete/upload.py']=Path('work/japanese-complete/upload.py').read_bytes().replace(b'\r\n',b'\n')
        files[dest+'requirements.txt']=b'requests\nbeautifulsoup4\nPillow\nmwparserfromhell==0.7.2\n'
        if (root/'checked-heads.json').exists():
            sys.path.insert(0,'work/wiki-tools');from dump_live import wiki_fname
            index=dict(line.split('\t',1) for line in git('show',base+':pages/INDEX.tsv').decode().splitlines() if '\t' in line)
            for title,page in json.loads((root/'checked-heads.json').read_bytes()).items():
                path=index.get(title,'pages/'+wiki_fname(title));assert not any(t!=title and p.casefold()==path.casefold() for t,p in index.items()),title
                index[title]=path;files[path]=(page['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
            files['pages/INDEX.tsv']=''.join(t+'\t'+p+'\n' for t,p in sorted(index.items(),key=lambda x:(x[0].casefold(),x[0]))).encode()
git('read-tree',base);updates=[]
for path,binary in files.items():
    oid=git('hash-object','-w','--stdin',data=binary).decode().strip();updates.append(f'100644 {oid}\t{path}\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip();pa=[a for p in parents for a in ['-p',p]]
commit=git('commit-tree',tree,*pa,'-m','Audit Japanese card completeness and preserve verified repairs (Refs swccg-guild/work#369)').decode().strip()
changed=set(x for x in git('diff','--name-only','-z',base,commit).decode().split('\0') if x);assert changed<=set(files),changed-set(files)
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8')
print(mode,commit,len(changed),'paths')
