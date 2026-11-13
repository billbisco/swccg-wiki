import os
from pathlib import Path
import subprocess
import sys

root=Path(__file__).parent
mode=sys.argv[1]
repo='work/wiki-source' if mode=='wiki' else 'work/japanese-preservation/evidence-repo'
branch='codex/japanese-card-infobox-287' if mode=='wiki' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((root/(mode+'-store.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=env)
exists=git('ls-remote','--heads','origin','refs/heads/'+branch).strip()
git('fetch','origin',branch if exists else 'main')
parent=git('rev-parse','FETCH_HEAD').decode().strip()
files={}
if mode=='wiki':
    base='authoring/japanese_infobox287/'
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.py','.json','.wiki','.md','.csv','.gz','.txt'] and path.name!='board.py':
            files[base+'work/japanese-infobox287/'+path.name]=path.read_bytes()
    files[base+'work/audit_wiki_card_titles.py']=Path('work/audit_wiki_card_titles.py').read_bytes()
    files[base+'work/wiki-tools/style_lint.py']=Path('work/wiki-tools/style_lint.py').read_bytes()
    files[base+'work/wiki_title_publish.py']=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0].encode()
    files[base+'README.md']=(root/'README.md').read_bytes()
    files[base+'requirements.txt']=b'beautifulsoup4\nrequests\nPillow\nmwparserfromhell==0.7.2\n'
else:
    for path in root.iterdir():
        if path.is_file() and path.suffix in ['.json','.md','.csv','.gz','.wiki','.diff','.webp']:
            if path.name in ['AGENTS.md','docs-SPEC-PROCESS.md','followup-story.json']:continue
            files['evidence/287/2026-11-13/'+path.name]=path.read_bytes()
    files['evidence/287/lint-backlog.csv']=(root/'lint-backlog.csv').read_bytes()
    old_readme=git('show',parent+':evidence/287/README.md').decode()
    pointer='## 13 November 2026 execution\n\nChatGPT now implements #287 under Bill\'s direction. Refreshed baselines, drafts and verification: [2026-11-13/](2026-11-13/README.md). The current lint backlog is one oversized promo; the earlier 35-page count predates #361.\n'
    if '## 13 November 2026 execution' not in old_readme:files['evidence/287/README.md']=(old_readme.rstrip()+'\n\n'+pointer).encode()
    files['docs/design-log/287-japanese-infobox.md']=(root/'design-log.md').read_bytes()
git('read-tree',parent)
updates=[]
for path,binary in files.items():
    oid=git('hash-object','-w','--stdin',data=binary).decode().strip()
    updates.append(f'100644 {oid}\t{path}\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
tree=git('write-tree','--missing-ok').decode().strip()
commit=git('commit-tree',tree,'-p',parent,'-m','Preserve Japanese card infobox migration work and refreshed evidence (Refs #287)').decode().strip()
changed=git('diff-tree','--no-commit-id','--name-only','-r',commit).decode().splitlines()
assert set(changed)<=set(files)
git('push','origin',commit+':refs/heads/'+branch)
(root/(mode+'-store-commit.txt')).write_text(commit+'\n',encoding='utf8')
print(mode,commit,len(changed),'paths saved',branch)
