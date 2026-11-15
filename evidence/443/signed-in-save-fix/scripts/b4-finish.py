from b4common import *
sys.path.insert(0,str(ROOT.parent/'wiki-gap-audit-20261108'));from board_api import call
browser=read('browser-checks.json');assert browser['result']=='PASS'and browser['originalBotPreferenceRestored'];deploy=read('deploy.json');assert deploy['source_revision']=='0148df06b9d87c608651b401f58f3317afdd5222'
review='''# Own review: signed-in Save default failure

Bill supplied a screenshot of the authenticated settings page reporting Could not save the default. Reproduced with our own bot in a real isolated Chrome session: preference initialization swallowed TypeError: win.mw.loader.using is not a function. Direct browser API calls after startup succeeded. Earlier direct-HTTP account verification did not cover browser initialization timing.

The installed MediaWiki startup.js exposes mw.config and runs plain RLQ functions before mediawiki.base defines loader.using. The base module later drains dependency-array entries using mw.loader.using(entry[0],entry[1]). Removing the direct-start shortcut alone (PR63) remained insufficient and failed the actual signed-in browser test. That failed receipt/deployment is retained, not claimed passing. PR64 uses the dependency-aware [['mediawiki.base'], callback] entry and models both real startup stages in the regression fixture.

Final19 behavior tests pass, including partial startup with plain callbacks executing early and dependency entries deferred. Own source/diff review found no unresolved issue. PR64 merged/deployed at0148df06b9d87c608651b401f58f3317afdd5222. Only the viewer JavaScript asset changed at runtime, SHA2560e16135b2e6697aefe1e64487df4e02c8716ef5caa450ba07d79cd16c9c90f12. Exact17 page caches refreshed at MediaWiki and Nginx layers; no global purge or server configuration change.

Authoritative live checks used the actual authenticated browser form, not a direct API substitute: Save default, reload, card default, per-card isolation, and no account value copied to guest storage all pass. A second fresh own-bot login in a phone context reads the stored value, saves the opposite value and passes reload/fit. An independent guest context passes save/reload/card navigation and has no default controls in article content. The original own-bot preference is restored and independently checked in finally. No human account/browser was accessed; authenticated cookies existed only in process memory and were not logged or stored. Browsers are closed.

No wiki text, card images, publication/version identity, settings placement, template, permission or database configuration changed. No Archive.org upload or saver action occurred. Source rollback bytes/hashes are recorded, but the known-broken full source was not reintroduced on production for a rollback demonstration. The bug and failed first attempt are reproducible in isolated startup fixtures/retained real-browser evidence. Final source merge and independent evidence readbacks are distinct from local/VPS preservation. Wider Story443 rollout remains open; this reported saving failure is fixed. No active own jobs remain after evidence publication.
'''
(B/'own-review.md').write_bytes(review.encode());save('results.json',{'ticket':443,'reported_bug':'Signed-in Save default fails before MediaWiki base loads','result':'PASS','behavior_tests':19,'final_pr':64,'superseded_incomplete_pr':63,'source_merge':deploy['source_revision'],'sha256':deploy['sha256'],'real_signed_in_ui':'PASS','fresh_authenticated_session':'PASS','phone':'PASS','guest_regression':'PASS','original_bot_preference_restored':True,'human_account_touched':False,'wiki_content_edits':0,'archive_uploads':0,'server_configuration_changes':0,'whole443_complete':False,'active_jobs':[]})
names=['own-review.md','results.json','behavior-tests.txt','browser-checks.json','probe-before.json','probe.json','first-fix-browser-failure.json','first-fix-deploy.json','deploy.json','cache-purge.json','first-fix-tests.txt','failure-before.jpg','signed-in-saved-desktop.jpg','signed-in-saved-phone.jpg']
for n in names:
 if n.endswith('.jpg'):assert(B/n).stat().st_size<=512000
files={'evidence/443/signed-in-save-fix/'+n:(B/n).read_bytes()for n in names}
for x in ROOT.glob('b4*.py'):files['evidence/443/signed-in-save-fix/scripts/'+x.name]=x.read_bytes()
for x in ROOT.glob('b4*.cjs'):files['evidence/443/signed-in-save-fix/scripts/'+x.name]=x.read_bytes()
ep=pin('billbisco/swccg-wiki','final-evidence',files)
shared={k:v for k,v in files.items()if k.split('/')[-1]in['own-review.md','results.json','browser-checks.json','signed-in-saved-desktop.jpg','signed-in-saved-phone.jpg','behavior-tests.txt']}
path='docs/design-log/443-wiki-image-rendition-rollout.md';old=base64.b64decode(gh('repos/swccg-guild/work/contents/'+path+'?ref=main')['content']);entry='''

### 2026-11-14 — fix actual signed-in preference startup
- **Trigger:** Bill reported Save default failing while signed in. Real own-bot browser reproduces swallowed TypeError: loader.using is not a function, despite direct API success. Earlier direct API verification missed browser timing.
- **Decision:** Use dependency-aware RLQ [['mediawiki.base'], callback], not mw.config presence or plain RLQ callbacks. Installed startup.js executes plain functions early; mediawiki.base processes dependency entries later. PR63 was insufficient and rejected by the real browser test; retained failed evidence is not a pass. PR64 is the final correction.
- **Verification:**19 behavior tests model both real loader stages. Actual signed-in UI save/reload/card defaults and local-card isolation pass. A fresh authenticated phone session reads and reverses the saved value. Guest regression and absence of article default controls pass. Original own-bot option restored in finally; no human account, credential storage or desktop control. PR64 merged/deployed at0148df06b9d87c608651b401f58f3317afdd5222; JS SHA2560e16135b2e6697aefe1e64487df4e02c8716ef5caa450ba07d79cd16c9c90f12. No Wiki content/image/configuration or archive write.
- **Who:** MemoryCoreChatGPT, following Bill’s reported failure. **Status:** bug delivered; wider Story443 remains open.
- **Evidence:** '''+ep['repository']+'/tree/'+ep['commit']+'/evidence/443/signed-in-save-fix\n';shared[path]=old+entry.encode();wp=pin('swccg-guild/work','shared-final',shared)
body='''PROGRESS: (MemoryCoreChatGPT) signed-in Save default bug fixed and verified through actual browser UI

Confirmed root cause: mw.config exists before mediawiki.base installs mw.loader.using. The early-start shortcut swallowed that TypeError and left no API client for saving. A direct API test did not cover this race. Plain RLQ callbacks also execute early in the installed startup.js; PR63 therefore remained insufficient and failed the actual browser test. Final [PR64](https://github.com/billbisco/swccg-wiki/pull/64) uses dependency-aware [['mediawiki.base'], callback], exactly as the installed startup/base queue supports. Its19-test fixture models both stages.

Actual signed-in browser Save default→reload→card passes. Per-card choices do not change the saved default; account values never copy into guest storage. A fresh independent own-bot login on phone reads the saved value, saves the opposite choice and passes reload/fit. Guest save/reload/card regression and no article default forms pass. Original bot preference restored and checked in finally. No human/Admin account accessed, cookies persisted/logged or desktop capture/input used. The screenshot is our own bot account.

Merged/deployed0148df06b9d87c608651b401f58f3317afdd5222, live JS SHA2560e16135b2e6697aefe1e64487df4e02c8716ef5caa450ba07d79cd16c9c90f12;17 scoped MediaWiki/Nginx page caches refreshed. No Wiki text, card images, settings placement or server configuration changed; no archive upload.19 tests and own diff review pass; hosted checks are unconfigured, no hosted-CI pass claimed. Broken full-source rollback was not reintroduced into production; exact before-assets/hashes and failed browser receipts are retained.

[Shared evidence]('''+wp['repository']+'/tree/'+wp['commit']+'''/evidence/443/signed-in-save-fix) · [full failure/diagnostic/deploy evidence]('''+ep['repository']+'/tree/'+ep['commit']+'''/evidence/443/signed-in-save-fix). Independent Git blob readback passed. This saving failure is fixed; wider Story443 remains open. No active own jobs. Existing open tabs must refresh to load the corrected inline script.

![Signed-in save succeeded](https://raw.githubusercontent.com/swccg-guild/work/'''+wp['commit']+'''/evidence/443/signed-in-save-fix/signed-in-saved-desktop.jpg)
'''
if not(B/'result-comment.json').exists():
 r=call('POST','/repos/swccg-guild/work/issues/443/comments',{'body':body});assert r['user']['login']=='MemoryCoreChatGPT2';checked=call('GET','/repos/swccg-guild/work/issues/comments/'+str(r['id']));assert checked['body']==body;save('result-comment.json',{'url':r['html_url'],'author':r['user']['login'],'readback':True})
issue=call('GET','/repos/swccg-guild/work/issues/443');assert issue['state']=='open'and'MemoryCoreChatGPT2'in[x['login']for x in issue['assignees']];save('final-ticket-check.json',{'result':read('result-comment.json'),'state':'open','assignee':'MemoryCoreChatGPT2','active_jobs':[]});print(json.dumps({'comment':read('result-comment.json')['url'],'evidence':ep['commit'],'shared':wp['commit']}))
