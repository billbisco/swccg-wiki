import json,hashlib,subprocess,re
from pathlib import Path
p=Path(__file__).parent;product=p/'product';product.mkdir(exist_ok=True)
def gitshow(repo,path):return subprocess.check_output(['git','-C',repo,'show','HEAD:'+path])
native=gitshow('work/search-gemp-source','src/gemp-swccg-async/src/main/web/js/gemp-016/cards/CardFilter.js').decode()
html=gitshow('work/search-gemp-source','src/gemp-swccg-async/src/main/web/deckBuild.html').decode()
(p/'CardFilter.before.js').write_text(native,encoding='utf8');(p/'deckBuild.before.html').write_text(html,encoding='utf8')
anchor='        var filterTable = $("<table id=\'filterTable\' />");';assert native.count(anchor)==1
addition='''
        // Shared-search pilot449: public read-only lookup, preserving builder context.
        if (typeof window !== 'undefined' && /\\/deckBuild\\.html$/.test(window.location.pathname)) {
            var sharedPilotWindow = null;
            var sharedPilotLink = $("<a href='searchPilot.html' id='sharedSearchPilot449' style='color:#8fc8ff'>Symbols, uniqueness &amp; decklists (pilot)</a>");
            sharedPilotLink.click(function (event) {
                event.preventDefault();
                var sharedPilotUrl = new URL('searchPilot.html', window.location.href);
                var existingTitle = $('#nameInput').val();
                if (existingTitle) sharedPilotUrl.searchParams.set('sp_text', existingTitle);
                sharedPilotWindow = window.open(sharedPilotUrl.href, 'swccgSharedSearchPilot449');
            });
            window.addEventListener('message', function (event) {
                if (event.origin !== window.location.origin || event.source !== sharedPilotWindow || !sharedPilotWindow) return;
                if (!event.data || event.data.type !== 'swccg-search-pilot-title' || typeof event.data.title !== 'string') return;
                if (!event.data.title.trim() || event.data.title.length > 120) return;
                $('#nameInput').val(event.data.title).change();
            });
        }
'''
native=native.replace(anchor,anchor+addition)
# Reuse the existing heading line: an extra row would overlap the fixed card pane.
native=native.replace('        this.fullFilterDiv.append(filterTable);', "        if (typeof sharedPilotLink !== 'undefined') filterTable.find('.cardFilterText').append(' · ', sharedPilotLink);\n        this.fullFilterDiv.append(filterTable);")
(product/'CardFilter.js').write_text(native,encoding='utf8',newline='\n')
digest=hashlib.sha256(native.encode()).hexdigest()[:12]
html,n=re.subn(r'(js/gemp-016/cards/CardFilter\.js)(?:\?v=[^"\']*)?',r'\1?v=search449-'+digest,html);assert n==1
(product/'deckBuild.html').write_text(html,encoding='utf8',newline='\n')
data=json.loads((product/'data.json').read_bytes());bundle=(product/'query.js').read_text(encoding='utf8')+'\nwindow.SharedSearchPilotData='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n'+(product/'ui.js').read_text(encoding='utf8')
bundlebytes=bundle.encode();cssbytes=(product/'pilot.css').read_bytes().replace(b'\r\n',b'\n');jsname='shared-search-449.'+hashlib.sha256(bundlebytes).hexdigest()[:12]+'.js';cssname='shared-search-449.'+hashlib.sha256(cssbytes).hexdigest()[:12]+'.css'
(product/jsname).write_bytes(bundlebytes);(product/cssname).write_bytes(cssbytes)
base='https://wiki.swccg.com/chrome/'
for context,name in [('gemp','searchPilot.html'),('scomp','scomp.html')]:
    title='GEMP shared search pilot' if context=='gemp' else 'SCOMPLINK pilot · swccg.com'
    document='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><link rel="stylesheet" href="'+base+cssname+'"><main data-swccg-search-pilot="'+context+'"><p>Loading the shared search pilot… <a href="https://wiki.swccg.com/wiki/Decklists">Browse published decklists</a> if the controls are unavailable.</p></main><script src="'+base+jsname+'" defer></script></html>\n'
    (product/name).write_text(document,encoding='utf8',newline='\n')
wiki_title='SWCCG Wiki:Samples/Shared search pilot'
wiki='''__NOTOC__
This sample searches a small set of verified card printings and four published decklists. It compares printed set symbols with symbol references, uniqueness, and decklists containing a card.

<div data-swccg-search-pilot="wiki"><p>Loading the shared search pilot…</p></div>

== Source records ==
The pilot retains the original article and card-image links, publication and text-state identifiers, and the original GEMP deck downloads. Main-deck and outside-deck quantities remain separate.

* [[Seeking An Audience]] and [[Seeking An Audience (Reflections III Foil)]]
* [[Officer Evax]], [[Admiral Ozzel]], [[Rebel Barrier]] and [[Houjix]]
* [[2026 Retro GEMPC Timo Dusel DS Ralltiir Operations]]
* [[2026 Retro GEMPC Timo Dusel LS Hidden Base]]
* [[2026 Worlds Top 8 Brian Fred DS ISB]]
* [[2026 Worlds Top 8 Brian Fred LS Diplo]]
'''
(product/'wiki-sample.wiki').write_text(wiki,encoding='utf8',newline='\n')
manifest=dict(story=449,snapshotId=data['snapshotId'],wikiTitle=wiki_title,js=jsname,css=cssname,js_sha256=hashlib.sha256(bundlebytes).hexdigest(),css_sha256=hashlib.sha256(cssbytes).hexdigest(),gempSourceCommit=subprocess.check_output(['git','-C','work/search-gemp-source','rev-parse','HEAD']).decode().strip(),gempFiles=['src/gemp-swccg-async/src/main/web/js/gemp-016/cards/CardFilter.js','src/gemp-swccg-async/src/main/web/deckBuild.html','src/gemp-swccg-async/src/main/web/searchPilot.html'])
(p/'build-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
print(jsname,cssname,'and native adapters prepared')
