import subprocess,json,hashlib,re
from pathlib import Path
import requests
p=Path(__file__).parent;manifest=json.loads((p/'build-manifest.json').read_bytes())
raw=subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','cat','/opt/swccg-wiki/SwccgChrome.php']);(p/'SwccgChrome.live-before.php').write_bytes(raw)
# Match the current checked-in application file before adding a bounded hook.
repo=subprocess.check_output(['git','-C','work/wiki-source','show','origin/main:wiki/SwccgChrome.php'])
def without_own_hook(text):return re.sub(r'\n        // Bounded public shared-search pilot449;[^\n]*\n        if \([^\n]*\) \{\n            \$out->addInlineStyle\([^\n]*\n            \$out->addInlineScript\([^\n]*\n        \}\n','',text,count=1)
assert without_own_hook(raw.decode()).replace('\r\n','\n')==without_own_hook(repo.decode()).replace('\r\n','\n'),'Live hook differs from source; reconcile first'
source=without_own_hook(raw.decode());anchor='\t\t$title = $out->getTitle();'
method=source.split('public static function onBeforePageDisplay',1)[1].split('public static function',1)[0]
assert method.count(anchor)==1
addition='''
        // Bounded public shared-search pilot449; ordinary Wiki pages load no resources.
        if ( $title && $title->getPrefixedText() === 'SWCCG Wiki:Samples/Shared search pilot' ) {
            $out->addInlineStyle( file_get_contents( '/swccg-chrome/CSS_FILE' ) );
            $out->addInlineScript( file_get_contents( '/swccg-chrome/JS_FILE' ) );
        }
'''.replace('CSS_FILE',manifest['css']).replace('JS_FILE',manifest['js'])
source=source.replace(anchor,anchor+addition,1)
(p/'product/SwccgChrome.php').write_text(source,encoding='utf8',newline='\n')
title=manifest['wikiTitle'];r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=title,prop='revisions|info',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();h=r.json()['query']['pages'][0];(p/'wiki-before.json').write_text(json.dumps(h,ensure_ascii=False,indent=2),encoding='utf8')
row=dict(title=title,text=(p/'product/wiki-sample.wiki').read_text(encoding='utf8'),section=None,summary='Add a bounded shared search pilot for symbols, uniqueness and public decklists (#449)')
if h.get('missing'):row['new']=True
else:
    old=h['revisions'][0]['slots']['main']['content'];row.update(before_revid=h['revisions'][0]['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest())
(p/'wiki-packet.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf8');print('Scoped Wiki hook and guarded native sample packet prepared')
