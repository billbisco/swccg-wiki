import json,os,subprocess,sys,tarfile,re
from pathlib import Path
p=Path(__file__).parent;mode=sys.argv[1];repos={'gemp':'work/search-gemp-source','wiki':'work/wiki-source','evidence':'work/japanese-preservation/evidence-repo'};repo=repos[mode];branch='main' if mode=='evidence' else 'codex/shared-search-pilot-449';default='master' if mode=='gemp' else 'main'
env=dict(os.environ,GIT_INDEX_FILE=str((p/(mode+'.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=env)
exists=git('ls-remote','--heads','origin',branch).strip();git('fetch','--filter=blob:none','origin',branch if exists else default);parent=git('rev-parse','FETCH_HEAD').decode().strip();git('fetch','--filter=blob:none','origin',default);base=git('rev-parse','FETCH_HEAD').decode().strip();parents=list(dict.fromkeys([parent,base]));manifest=json.loads((p/'build-manifest.json').read_bytes())
if mode=='gemp':
    files={path:(p/'product'/Path(path).name).read_bytes() for path in manifest['gempFiles']}
else:
    with tarfile.open(p/'source-data.tar.xz','w:xz') as t:
        for folder in ['faces','decks','product']:
            for f in sorted((p/folder).rglob('*')):
                if f.is_file():t.add(f,arcname=f.relative_to(p).as_posix())
        for f in p.glob('*-body.md'):t.add(f,arcname='story-updates/'+f.name)
    prefix='authoring/shared_search449/' if mode=='wiki' else 'evidence/449/'
    files={prefix+f.name:f.read_bytes() for f in p.iterdir() if f.is_file() and not f.name.endswith(('-body.md','-summary.txt')) and (f.suffix in ['.py','.js','.json','.md','.txt','.webp','.html','.wiki','.php'] or f.name.endswith('.tar.xz'))}
    if mode=='wiki':
        files['wiki/SwccgChrome.php']=(p/'product/SwccgChrome.php').read_bytes()
        for name in [manifest['js'],manifest['css']]:files['chrome/'+name]=(p/'product'/name).read_bytes()
        files['authoring/shared_search449/product/query.js']=(p/'product/query.js').read_bytes();files['authoring/shared_search449/product/data.json']=(p/'product/data.json').read_bytes()
        for published in ['wiki-published.json','talk-published.json']:
            if not (p/published).exists():continue
            j=json.loads((p/published).read_bytes());h=j['page'];title=h['title'];source=h['revisions'][0]['slots']['main']['content']
            # Preserve the existing ordering convention and only add our own page mapping.
            old=subprocess.check_output(['git','-C',repo,'show',base+':pages/INDEX.tsv']).decode();index=dict(s.split('\t',1) for s in old.splitlines() if '\t' in s)
            sys.path.insert(0,'work/wiki-tools');from dump_live import wiki_fname
            path=index.get(title,'pages/'+wiki_fname(title));index[title]=path;files[path]=(source.rstrip()+'\n').encode();files['pages/INDEX.tsv']=''.join(t+'\t'+v+'\n' for t,v in sorted(index.items())).encode()
    if mode=='evidence' and (p/'design-log.md').exists():files['docs/design-log/449-shared-search-pilot.md']=(p/'design-log.md').read_bytes()
git('read-tree',base);updates=[]
for path,data in files.items():
    if path.endswith(('.py','.js','.json','.md','.txt','.html','.wiki','.php','.css')):data=data.replace(b'\r\n',b'\n').rstrip()+b'\n'
    oid=git('hash-object','-w','--stdin',data=data).decode().strip();updates.append('100644 '+oid+'\t'+path+'\0')
git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode());tree=git('write-tree','--missing-ok').decode().strip();commit=git('commit-tree',tree,*[a for parent in parents for a in ['-p',parent]],'-m','Pilot shared symbol uniqueness and deck-membership search (Refs swccg-guild/work#449)').decode().strip();assert set(filter(None,git('diff','--name-only','-z',base,commit).decode().split('\0')))<=set(files)
check=subprocess.run(['git','-C',repo,'diff','--check',base,commit],env=env,stdout=subprocess.PIPE);assert check.returncode==0,check.stdout.decode()
git('push','origin',commit+':refs/heads/'+branch);(p/(mode+'-commit.txt')).write_text(commit+'\n',encoding='utf8');print(mode,commit,len(files),'scoped source/evidence paths pushed')
