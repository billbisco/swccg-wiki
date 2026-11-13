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
    manifest=json.loads((root/'recovered-face-manifest.json').read_bytes())
    for item in json.loads((root/'recovered-files-payload.json').read_bytes()):
        source=next(m for m in manifest if m['sha256']==item['sha256'])
        binary=(root/Path(source['file'].replace('\\','/'))).read_bytes()
        import hashlib
        assert hashlib.sha256(binary).hexdigest()==item['sha256']
        files['files/'+item['name']]=binary
else:
    dest='authoring/japanese_other369/' if mode=='wiki' else 'evidence/369/'
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.py','.md','.json','.jsonl','.csv','.txt','.wiki','.webp','.png','.gz']:
            binary=path.read_bytes()
            if path.suffix not in ['.png','.webp','.gz']:binary=binary.replace(b'\r\n',b'\n')
            if path.suffix in ['.py','.md','.txt']:binary=binary.rstrip()+b'\n'
            files[dest+('work/japanese-other369/' if mode=='wiki' else '')+path.name]=binary
    if mode=='wiki':
        files[dest+'work/wiki-tools/style_lint.py']=Path('work/wiki-tools/style_lint.py').read_bytes().replace(b'\r\n',b'\n')
        files[dest+'work/wiki_title_publish.py']=(Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0].rstrip()+'\n').encode()
        files[dest+'work/japanese-complete/upload.py']=Path('work/japanese-complete/upload.py').read_bytes().replace(b'\r\n',b'\n').rstrip()+b'\n'
        files[dest+'requirements.txt']=b'requests\nbeautifulsoup4\nPillow\nmwparserfromhell==0.7.2\n'
        if (root/'checked-heads.json').exists():
            sys.path.insert(0,'work/wiki-tools');from dump_live import wiki_fname
            index=dict(line.split('\t',1) for line in git('show',base+':pages/INDEX.tsv').decode().splitlines() if '\t' in line)
            for title,page in json.loads((root/'checked-heads.json').read_bytes()).items():
                path=index.get(title,'pages/'+wiki_fname(title));assert not any(t!=title and p.casefold()==path.casefold() for t,p in index.items()),title
                index[title]=path;files[path]=(page['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
            files['pages/INDEX.tsv']=''.join(t+'\t'+p+'\n' for t,p in sorted(index.items(),key=lambda x:(x[0].casefold(),x[0]))).encode()
            from datetime import datetime,timezone
            now=datetime.now(timezone.utc).isoformat()
            done=json.loads(git('show',base+':ops/wayback/done.json'))
            captures={r['url']:r for r in map(json.loads,(root/'image-captures.jsonl').read_text().splitlines())}
            captures.update({r['url']:r for r in [json.loads((root/'preservation.json').read_bytes()),json.loads((root/'recovered-preservation.json').read_bytes())]})
            assert len(captures)==12 and all(r['verified'] for r in captures.values())
            for url,r in captures.items():
                done[url]=dict(status='verified',capture=r['capture'],last=now,verify=dict(method='sha256',sha256=r['sha256'],bytes=r['bytes'],at=now),note='Japanese original photo preservation, byte-verified by MemoryCoreChatGPT (#369)')
            files['ops/wayback/done.json']=(json.dumps(done,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
    else:
        files['docs/design-log/369-japanese-card-audit.md']=(root/'design-log.md').read_bytes().replace(b'\r\n',b'\n')
git('read-tree',base);updates=[]
for path,binary in files.items():
    oid=git('hash-object','-w','--stdin',data=binary).decode().strip();updates.append(f'100644 {oid}\t{path}\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip();pa=[a for p in parents for a in ['-p',p]]
commit=git('commit-tree',tree,*pa,'-m','Audit Japanese card completeness and preserve verified repairs (Refs swccg-guild/work#369)').decode().strip()
changed=set(x for x in git('diff','--name-only','-z',base,commit).decode().split('\0') if x);assert changed<=set(files),changed-set(files)

if mode=='wiki':
    checkenv=dict(env);checkenv.pop('GIT_NO_LAZY_FETCH',None)
    check=subprocess.run(['git','-C',repo,'-c','core.protectNTFS=false','diff','--check',base,commit],env=checkenv,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (root/'diff-check.txt').write_bytes(check.stdout)
    assert check.returncode==0,'Whitespace check failed; see diff-check.txt'
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8')
print(mode,commit,len(changed),'paths')
