const {test}=require('node:test');
const assert=require('node:assert/strict');
const {JSDOM}=require('jsdom');
const fs=require('node:fs');
const viewer=require('../chrome/card-image-viewer.js');
const card={label:'Example',state:'1101_1:PC-E2',language:'en',slip:'slip.png',renditions:[
 {kind:'original',state:'1101_1:PC-E2',language:'en',file:'original.gif'},
 {kind:'remastered',state:'1101_1:PC-E2',language:'en',file:'remaster.webp'}]};
const messages={original:'Original',remastered:'Remastered',group:'Card image',setting:'Card images',save:'Save default',saved:'Saved',failed:'Save failed'};
function portrait(file){return `<div class="card-portrait"><a href="/wiki/File:${file}"><img src="/images/${file}"></a></div>`;}
function markup(key='example'){return `<div class="card-rail">${portrait('original.gif')}${portrait('remaster.webp')}${portrait('slip.png')}<div class="card-image-note"><span class="swccg-card-image-marker" data-card-image-key="${key}"></span></div><table class="card-infobox"><caption>Info</caption></table></div><p class="game-text">Exact selected publication text</p>`;}
async function fixture({guest='original',account,invalidAccount,failRead,failWrite,failLoad,legacyThenables,blockStorage,screenWidth,settingsPage=false,cardPanel=true,words=messages,definition=card}={}){
 const dom=new JSDOM(`<meta name="viewport" content="width=1120"><div class="mw-parser-output">${cardPanel?markup():''}${settingsPage?'<div class="swccg-card-image-preferences-target"></div>':''}</div>`,{url:'https://wiki.swccg.com/wiki/Example'});const w=dom.window;
 if(screenWidth)Object.defineProperty(w.screen,'width',{value:screenWidth});
 const cfg={wgUserName:account?'TestBot':null,swccgCardImagePilot:{cards:{example:structuredClone(definition)},messages:words,settingsPage}};
 const calls=[];let value=invalidAccount||account;let guestValue=guest;
 Object.defineProperty(w,'localStorage',{value:{getItem(){if(blockStorage)throw Error('blocked');return guestValue;},setItem(k,v){if(blockStorage)throw Error('blocked');guestValue=v;}}});
 for(const img of w.document.querySelectorAll('img')){Object.defineProperty(img,'complete',{value:true});Object.defineProperty(img,'naturalWidth',{value:350});}
 w.mw={config:{get:k=>cfg[k]},loader:{using:()=>failLoad?Promise.reject(Error('unavailable')):Promise.resolve()},Api:function(){this.get=async p=>{calls.push(p);if(failRead)throw Error('read failed');return {query:{userinfo:{options:{'swccg-card-images':value}}}};};this.postWithToken=async(t,p)=>{calls.push(p);if(failWrite)throw Error('write failed');value=p.change.split('=')[1];return {options:'success'};};},hook:()=>({add(){}})};
 if(legacyThenables){const NativeApi=w.mw.Api;const wrap=p=>({then:(resolve,reject)=>p.then(resolve,reject)});w.mw.loader.using=()=>wrap(Promise.resolve());w.mw.Api=function(){const a=new NativeApi();this.get=p=>wrap(a.get(p));this.postWithToken=(t,p)=>wrap(a.postWithToken(t,p));};}
 viewer.start(w);await w.swccgCardImages.initialize();
 return {w,doc:w.document,cfg,calls,guestValue:()=>guestValue,accountValue:()=>value,close:()=>dom.window.close()};
}
function selected(f){return f.doc.querySelector('.swccg-card-image-stage .card-portrait:not([hidden]) img')?.getAttribute('src');}
function button(f,label){return [...f.doc.querySelectorAll('.swccg-card-image-choices button')].find(x=>x.textContent===label);}
async function save(f,value){f.doc.querySelector('select').value=value;f.doc.querySelector('form').dispatchEvent(new f.w.Event('submit',{cancelable:true}));await new Promise(setImmediate);}
test('availability matrix excludes other state/card/language and duplicate assets',()=>{
 for(const [rends,expected,pair]of [[card.renditions,'original',true],[[card.renditions[0]],'original',false],[[card.renditions[1]],'remastered',false],[[],undefined,false],[[{...card.renditions[1],state:'different'}],undefined,false],[[{...card.renditions[0],language:'ja'}],undefined,false],[[card.renditions[0],{...card.renditions[1],file:'original.gif'}],'original',false]]){
  const result=viewer.choose({...card,renditions:rends},'original',()=>true);assert.equal(result.selected?.kind,expected);assert.equal(result.pair,pair);
 }
 assert.equal(viewer.choose(card,'remastered',r=>r.kind==='original').selected.kind,'original');
 assert.equal(viewer.preference('bad'),'original');
});
test('browser entry waits for asynchronous MediaWiki startup before reading config',async()=>{
 const dom=new JSDOM(`<div class="mw-parser-output">${markup()}</div>`,{url:'https://wiki.swccg.com/wiki/Example',runScripts:'outside-only'});const w=dom.window;
 for(const image of w.document.querySelectorAll('img')){Object.defineProperty(image,'complete',{value:true});Object.defineProperty(image,'naturalWidth',{value:350});}
 w.eval(fs.readFileSync(require.resolve('../chrome/card-image-viewer.js'),'utf8'));
 assert.equal(w.RLQ.length,1);assert.equal(w.swccgCardImages,undefined);
 const cfg={wgUserName:null,swccgCardImagePilot:{cards:{example:card},messages}};w.mw={config:{get:k=>cfg[k]},hook:()=>({add(){}})};
 for(const ready of w.RLQ)ready();await w.swccgCardImages.initialize();assert.equal(w.document.querySelectorAll('.swccg-card-image-choices button').length,2);dom.window.close();
});
test('buttons follow stage and publisher slip and precede Info; no duplicate initialization',async()=>{
 const f=await fixture();const rail=f.doc.querySelector('.card-rail');const stage=rail.querySelector('.swccg-card-image-stage');const slip=[...rail.children].find(p=>p.querySelector('img[src="/images/slip.png"]'));const controls=rail.querySelector('.swccg-card-image-choices');
 assert.equal(stage.nextElementSibling,slip);assert.equal(slip.nextElementSibling,controls);assert.ok(controls.compareDocumentPosition(rail.querySelector('table'))&4);
 await f.w.swccgCardImages.initialize();viewer.start(f.w);await f.w.swccgCardImages.initialize();assert.equal(f.doc.querySelectorAll('.swccg-card-image-choices').length,1);assert.equal(f.doc.querySelectorAll('form').length,0);assert.equal(f.doc.querySelectorAll('.swccg-card-image-choices img').length,0);f.close();
});

test('signed-in browser entry waits past early mw.config until the base loader is ready',async()=>{
 const dom=new JSDOM('<div class="mw-parser-output"><div class="swccg-card-image-preferences-target"></div></div>',{url:'https://wiki.swccg.com/wiki/Settings',runScripts:'outside-only'});const w=dom.window;let stored='remastered';
 const cfg={wgUserName:'TestBot',swccgCardImagePilot:{cards:{},messages,settingsPage:true}};
 w.mw={config:{get:k=>cfg[k]},loader:{}};
 w.eval(fs.readFileSync(require.resolve('../chrome/card-image-viewer.js'),'utf8'));
 assert.equal(w.swccgCardImages,undefined);assert.equal(w.RLQ.length,1);assert.equal(w.document.querySelectorAll('form').length,0);
 w.mw.loader.using=async()=>{};w.mw.Api=function(){this.get=async()=>({query:{userinfo:{options:{'swccg-card-images':stored}}}});this.postWithToken=async(t,p)=>{stored=p.change.split('=')[1];return{options:'success'};};};w.mw.hook=()=>({add(){}});
 for(const run of w.RLQ)run();await w.swccgCardImages.initialize();assert.equal(w.document.querySelector('select').value,'remastered');w.document.querySelector('select').value='original';w.document.querySelector('form').dispatchEvent(new w.Event('submit',{cancelable:true}));await new Promise(setImmediate);assert.equal(stored,'original');assert.equal(w.document.querySelector('[role="status"]').textContent,'Saved');dom.window.close();
});
test('per-card choice changes only presentation, not text, slip or saved default',async()=>{
 const f=await fixture();const text=f.doc.querySelector('.game-text').textContent;const slip=f.doc.querySelector('img[src="/images/slip.png"]');button(f,'Remastered').click();assert.equal(selected(f),'/images/remaster.webp');assert.equal(button(f,'Remastered').getAttribute('aria-pressed'),'true');assert.equal(f.guestValue(),'original');assert.equal(f.doc.querySelector('.game-text').textContent,text);assert.equal(f.doc.querySelector('img[src="/images/slip.png"]'),slip);f.close();
});
test('keyboard keys move focus and selection',async()=>{
 const f=await fixture();button(f,'Original').dispatchEvent(new f.w.KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}));assert.equal(f.doc.activeElement,button(f,'Remastered'));assert.equal(selected(f),'/images/remaster.webp');button(f,'Remastered').dispatchEvent(new f.w.KeyboardEvent('keydown',{key:'Home'}));assert.equal(selected(f),'/images/original.gif');f.close();
});
test('explicit guest default affects future views, preserving current per-card choice',async()=>{
 const f=await fixture({settingsPage:true,cardPanel:false});await save(f,'remastered');assert.equal(f.guestValue(),'remastered');const next=await fixture({guest:f.guestValue()});assert.equal(selected(next),'/images/remaster.webp');assert.equal(next.doc.querySelectorAll('form').length,0);f.close();next.close();
});
test('blocked guest storage and invalid values remain usable',async()=>{
 for(const options of [{blockStorage:true},{guest:'corrupt'}]){const f=await fixture({...options,settingsPage:true});assert.equal(selected(f),'/images/original.gif');if(options.blockStorage){await save(f,'remastered');assert.equal(f.doc.querySelector('[role="status"]').textContent,'Save failed');}f.close();}
});
test('account overrides guest; account save never modifies guest storage',async()=>{
 const f=await fixture({account:'remastered',guest:'original',settingsPage:true});assert.equal(selected(f),'/images/remaster.webp');assert.equal(f.guestValue(),'original');await save(f,'original');assert.equal(f.accountValue(),'original');assert.equal(f.guestValue(),'original');assert.ok(f.calls.every(p=>p.assert==='user'));const guest=await fixture({guest:f.guestValue()});assert.equal(selected(guest),'/images/original.gif');f.close();guest.close();
});
test('account read/write failures and invalid account values fail usefully',async()=>{
 for(const options of [{account:'remastered',failRead:true},{account:'remastered',failLoad:true},{account:'remastered',invalidAccount:'bad'},{account:'original',failWrite:true}]){const f=await fixture({...options,settingsPage:true});assert.equal(selected(f),'/images/original.gif');await save(f,'remastered');assert.equal(f.doc.querySelector('[role="status"]').textContent,options.failLoad||options.failWrite?'Save failed':'Saved');assert.equal(f.guestValue(),'original');f.close();}
});
test('MediaWiki-style thenables without catch/finally save and re-enable the form',async()=>{
 const f=await fixture({account:'original',legacyThenables:true,settingsPage:true});await save(f,'remastered');assert.equal(f.accountValue(),'remastered');assert.equal(f.doc.querySelector('[role="status"]').textContent,'Saved');assert.equal(f.doc.querySelector('form button').disabled,false);f.close();
});
test('image failure hides the pair and falls back, retaining preference',async()=>{
 const f=await fixture({guest:'remastered'});const im=f.doc.querySelector('img[src="/images/remaster.webp"]');im.dispatchEvent(new f.w.Event('error'));assert.equal(selected(f),'/images/original.gif');assert.equal(f.doc.querySelector('.swccg-card-image-choices').hidden,true);assert.equal(f.guestValue(),'remastered');im.dispatchEvent(new f.w.Event('load'));assert.equal(selected(f),'/images/remaster.webp');assert.equal(f.doc.querySelector('.swccg-card-image-choices').hidden,false);f.close();
});
test('single rendition has no visible pair and unknown markers retain native fallback',async()=>{
 const f=await fixture({definition:{...card,renditions:[card.renditions[1]]}});assert.equal(selected(f),'/images/remaster.webp');assert.equal(f.doc.querySelector('.swccg-card-image-choices').hidden,true);f.close();const n=await fixture({definition:{...card,renditions:[]}});assert.equal(n.doc.querySelectorAll('.swccg-card-image-choices').length,0);assert.equal(n.doc.querySelectorAll('.card-portrait').length,3);n.close();
});
test('interface localization is independent of English image language',async()=>{
 const f=await fixture({words:{...messages,original:'オリジナル',remastered:'リマスター'}});assert.ok(button(f,'オリジナル'));button(f,'リマスター').click();assert.equal(selected(f),'/images/remaster.webp');f.close();
});
test('phone viewport adjustment is limited to allowlisted pilot script activation',async()=>{
 const phone=await fixture({screenWidth:390});assert.equal(phone.doc.querySelector('meta[name="viewport"]').content,'width=device-width, initial-scale=1');phone.close();
 const desktop=await fixture({screenWidth:1920});assert.equal(desktop.doc.querySelector('meta[name="viewport"]').content,'width=1120');desktop.close();
 const dom=new JSDOM('<meta name="viewport" content="width=1120">');Object.defineProperty(dom.window.screen,'width',{value:390});dom.window.mw={config:{get:()=>undefined}};viewer.start(dom.window);assert.equal(dom.window.document.querySelector('meta').content,'width=1120');dom.window.close();
});
test('replacing selected card/language recomputes availability without duplicate controls',async()=>{
 const f=await fixture();f.cfg.swccgCardImagePilot.cards.example={...card,language:'ja',renditions:[{...card.renditions[1],language:'ja'}]};await f.w.swccgCardImages.initialize();assert.equal(selected(f),'/images/remaster.webp');assert.equal(f.doc.querySelector('.swccg-card-image-choices').hidden,true);assert.equal(f.doc.querySelectorAll('.swccg-card-image-stage').length,1);f.close();
});

test('card pages never receive saved-default controls, even with an unrelated target',async()=>{
 const f=await fixture();const trap=f.doc.createElement('div');trap.className='swccg-card-image-preferences-target';f.doc.querySelector('.mw-parser-output').prepend(trap);await f.w.swccgCardImages.initialize();
 assert.equal(f.doc.querySelectorAll('form,select,.swccg-card-image-status').length,0);assert.equal(trap.children.length,0);assert.equal(f.doc.querySelectorAll('.swccg-card-image-choices button').length,2);f.close();
});

test('dedicated settings page contains one default form and no card selector',async()=>{
 const f=await fixture({settingsPage:true,cardPanel:false});await f.w.swccgCardImages.initialize();assert.equal(f.doc.querySelectorAll('.swccg-card-image-settings').length,1);assert.equal(f.doc.querySelectorAll('.swccg-card-image-choices').length,0);assert.equal(f.doc.querySelector('form').parentElement.className,'swccg-card-image-preferences-target');await save(f,'remastered');assert.equal(f.guestValue(),'remastered');assert.equal(f.doc.querySelector('[role="status"]').textContent,'Saved');f.close();
});

test('a settings page without its native target does not prepend a form to article content',async()=>{
 const f=await fixture();f.cfg.swccgCardImagePilot.settingsPage=true;await f.w.swccgCardImages.initialize();assert.equal(f.doc.querySelectorAll('form').length,0);f.close();
});
