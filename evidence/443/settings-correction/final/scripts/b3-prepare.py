from b3common import *
import requests
sys.path.insert(0,str(ROOT.parent/'wiki-gap-audit-20261108'));from board_api import call
titles=['SWCCG Wiki:Display settings','SWCCG Wiki:Samples/Original Virtual card images','SWCCG Wiki talk:Samples/Original Virtual card images'];r=requests.get('https://wiki.swccg.com/api.php',params={'action':'query','format':'json','formatversion':2,'titles':'|'.join(titles),'prop':'revisions|flagged','rvprop':'ids|timestamp|content','rvslots':'main'},timeout=45);r.raise_for_status();baseline=r.json();save('baseline.json',baseline);D=B/'drafts';D.mkdir(exist_ok=True)
def old(t):return next(x for x in baseline['query']['pages']if x['title']==t)
assert old(titles[0]).get('missing'),'Existing settings page requires merge'
settings='''Choose which image appears by default when a card has both an Original and a matching Remastered image of the selected publication and language.

== Card images ==
<div class="swccg-card-image-preferences-target"></div>

Signed-in readers save this choice with their account. Guests save it in this browser. The Original and Remastered buttons beneath a card change that view without changing the saved default.

Signed-in readers can also change this setting under [[Special:Preferences#mw-prefsection-rendering|Preferences → Appearance]].
'''
hub=old(titles[1])['revisions'][0]['slots']['main']['content'];before="Use '''Card images''' above to save a default for future views.";assert before in hub;hub=hub.replace(before,"Use the '''[[SWCCG Wiki:Display settings|Display settings]]''' tab after Discussion to save a default for future views.")
talk=old(titles[2])['revisions'][0]['slots']['main']['content']+'''\n\n== Saved image defaults moved out of article content ==

Bill rejected the above-article saved-default box because it consumes reading space. The default form now belongs only on [[SWCCG Wiki:Display settings]], reached by a native Display settings tab immediately after Discussion. The per-card Original and Remastered buttons stay beneath the complete image group. Existing account/browser saved values are retained; signed-in readers can also use Preferences → Appearance. No card text, image bytes, publication identities or Versions templates are changed. ~~~~
'''
plan=[]
for title,name,text in zip(titles,['settings.wiki','hub.wiki','talk-hub.wiki'],[settings,hub,talk]):
 (D/name).write_bytes((text.rstrip()+'\n').encode());plan.append({'title':title,'file':name,'kind':'talk'if'talk:'in title else'hub','base':old(title).get('revisions',[{}])[0].get('revid')})
save('plan.json',plan);save('source-accuracy.json',{'ticket':443,'user_correction':'Saved default belongs on settings page; no large controls in article reading space; a tab after Discussion is acceptable','implementation':'Dedicated Display settings project page; native localized after-Discussion tab; explicit config flag plus placeholder required for default form; account and guest storage keys preserved; per-card controls unchanged','checks':'18 behavior tests pass including article form absence, dedicated target placement, guest navigation persistence and failures; PHP/core hook and live browser checks follow deployment','archive_policy':'Reading/downloads allowed; uploads/Save Page Now paused','card_text_image_versions_changed':False})
issue=call('GET','/repos/swccg-guild/work/issues/443');save('issue.json',issue)
comment=call('POST','/repos/swccg-guild/work/issues/443/comments',{'body':'PLAN: (MemoryCoreChatGPT) Bill rejected the saved-default option box above card content: space is at a premium, and this belongs on a settings page, with a tab after Discussion acceptable. Move the explicit default form to SWCCG Wiki:Display settings, add a compact native localized tab after Discussion, and render no default form/spacer on card articles or review pages. Preserve per-card below-slip buttons and existing account/browser saved defaults; retain native account Appearance preference. No card, source-image or Versions changes. Verify desktop/phone layout, guest settings→card/reload flow, account persistence, localization, native navigation and rollback; update hub instructions and ticket evidence. Routine app change only, no server configuration or archive upload.'});save('plan-comment.json',{'url':comment['html_url'],'author':comment['user']['login']});assert comment['user']['login']=='MemoryCoreChatGPT2';print(json.dumps({'drafts':3,'comment':comment['html_url']}))
