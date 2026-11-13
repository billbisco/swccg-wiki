import os
import json
from pathlib import Path
import subprocess
import sys

root=Path(__file__).parent
mode=sys.argv[1]
repo='work/wiki-source' if mode=='wiki' else 'work/japanese-preservation/evidence-repo'
branch='codex/japanese-card-infobox-287' if mode=='wiki' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((root/(mode+'-store.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):
    child_env=dict(env)
    if args and args[0]=='show':child_env.pop('GIT_NO_LAZY_FETCH',None)
    return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=child_env)
exists=git('ls-remote','--heads','origin','refs/heads/'+branch).strip()
git('fetch','origin',branch if exists else 'main')
parent=git('rev-parse','FETCH_HEAD').decode().strip()
parents=[parent]
if mode=='wiki' and (root/'checked-heads.json').exists():
    git('fetch','origin','main')
    tree_base=git('rev-parse','FETCH_HEAD').decode().strip()
    if tree_base!=parent:parents.append(tree_base)
else:tree_base=parent
files={}
if mode=='wiki':
    base='authoring/japanese_infobox287/'
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.py','.json','.jsonl','.wiki','.md','.csv','.gz','.txt'] and path.name!='board.py':
            files[base+'work/japanese-infobox287/'+path.name]=path.read_bytes()
    files[base+'work/audit_wiki_card_titles.py']=Path('work/audit_wiki_card_titles.py').read_bytes()
    files[base+'work/wiki-tools/style_lint.py']=Path('work/wiki-tools/style_lint.py').read_bytes()
    files[base+'work/wiki_title_publish.py']=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0].encode()
    files[base+'README.md']=(root/'README.md').read_bytes()
    files[base+'requirements.txt']=b'beautifulsoup4\nrequests\nPillow\nmwparserfromhell==0.7.2\n'
    if (root/'checked-heads.json').exists():
        sys.path.insert(0,'work/wiki-tools')
        from dump_live import wiki_fname
        index=dict(line.split('\t',1) for line in git('show',tree_base+':pages/INDEX.tsv').decode().splitlines() if '\t' in line)
        for title,page in json.loads((root/'checked-heads.json').read_bytes()).items():
            path=index.get(title,'pages/'+wiki_fname(title))
            assert not any(t!=title and p.casefold()==path.casefold() for t,p in index.items()),title
            index[title]=path
            files[path]=(page['revisions'][0]['slots']['main']['content'].rstrip('\n')+'\n').encode()
        files['pages/INDEX.tsv']=''.join(t+'\t'+p+'\n' for t,p in sorted(index.items(),key=lambda x:(x[0].casefold(),x[0]))).encode()
        archive=json.loads((root/'bgg-preservation.json').read_bytes())
        done=json.loads(git('show',tree_base+':ops/wayback/done.json'))
        from datetime import datetime,timezone
        now=datetime.now(timezone.utc).isoformat()
        done[archive['url']]=dict(status='verified',capture=archive['capture'],last=now,verify=dict(method='sha256',sha256=archive['sha256'],bytes=archive['bytes'],at=now),note='Complete BGG page snapshot, byte-verified by MemoryCoreChatGPT (#287/#366); staging removed')
        files['ops/wayback/done.json']=(json.dumps(done,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
else:
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.json','.jsonl','.md','.csv','.gz','.wiki','.diff','.webp','.png','.txt']:
            if path.name in ['AGENTS.md','docs-SPEC-PROCESS.md','followup-story.json']:continue
            files['evidence/287/2026-11-13/'+path.name]=path.read_bytes()
            if path.name in ['followup-story.md','cleanup-packet.json','cleanup-receipts.jsonl','bgg-preservation.json','366-pass-report.md','source-verification.json','public-verification.json','lint-backlog.csv','reference-repairs.json']:
                files['evidence/366/'+path.name]=path.read_bytes()
    files['evidence/287/lint-backlog.csv']=(root/'lint-backlog.csv').read_bytes()
    old_readme=git('show',parent+':evidence/287/README.md').decode()
    pointer='## 13 November 2026 execution\n\nChatGPT now implements #287 under Bill\'s direction. Refreshed baselines, drafts and verification: [2026-11-13/](2026-11-13/README.md). The current lint backlog is one oversized promo; the earlier 35-page count predates #361.\n'
    if '## 13 November 2026 execution' not in old_readme:files['evidence/287/README.md']=(old_readme.rstrip()+'\n\n'+pointer).encode()
    files['docs/design-log/287-japanese-infobox.md']=(root/'design-log.md').read_bytes()
git('read-tree',tree_base)
updates=[]
for path,binary in files.items():
    oid=git('hash-object','-w','--stdin',data=binary).decode().strip()
    updates.append(f'100644 {oid}\t{path}\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip()
parent_args=[arg for p in parents for arg in ['-p',p]]
commit=git('commit-tree',tree,*parent_args,'-m','Preserve Japanese card infobox migration work and refreshed evidence (Refs #287)').decode().strip()
changed=[p for p in git('diff','--name-only','-z',tree_base,commit).decode().split('\0') if p]
assert set(changed)<=set(files),sorted(set(changed)-set(files))[:30]
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-store-commit.txt')).write_text(commit+'\n',encoding='utf8')
print(mode,commit,len(changed),'paths saved',branch)
