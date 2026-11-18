$services = \MediaWiki\MediaWikiServices::getInstance();
$plan = json_decode($input597, true, 512, JSON_THROW_ON_ERROR);
if (($plan['ticket'] ?? null) !== 597 || !in_array($plan['mode'] ?? '', ['inspect','preview','apply'], true)) { throw new \RuntimeException('Unsupported scope'); }
$user = $services->getUserFactory()->newFromName('Memory Core ChatGPT');
if (!$user || !$user->getId() || $user->getName() !== 'Memory Core ChatGPT') { throw new \RuntimeException('Existing assigned account unavailable'); }
$permissions = $services->getPermissionManager();
$rights = ['edit'=>$permissions->userHasRight($user,'edit'),'review'=>$permissions->userHasRight($user,'review'),'bot'=>$permissions->userHasRight($user,'bot')];
echo "ACTOR597 ".json_encode(['name'=>$user->getName(),'id'=>$user->getId(),'rights'=>$rights])."\n";
if ($plan['mode'] === 'inspect') { return; }
if (!$rights['edit'] || !$rights['review'] || !$rights['bot']) { throw new \RuntimeException('Existing assigned permissions insufficient'); }
if (count($plan['pages'] ?? []) > 50) { throw new \RuntimeException('Batch exceeds fifty guarded pages'); }
\MediaWiki\StubObject\StubGlobalUser::setUser($user);
\RequestContext::getMain()->setUser($user);
$seen = []; $count = 0;
foreach ($plan['pages'] as $item) {
    $title = \MediaWiki\Title\Title::newFromText($item['title']);
    if (!$title || !in_array($title->getNamespace(), [0,1,4,5,6,10,11], true) || isset($seen[$title->getPrefixedDBkey()])) { throw new \RuntimeException('Invalid or duplicate scoped title'); }
    $seen[$title->getPrefixedDBkey()] = true;
    $draft = $item['text'];
    if (!hash_equals($item['after_sha256'], hash('sha256',$draft))) { throw new \RuntimeException('Draft identity mismatch'); }
    $page = $services->getWikiPageFactory()->newFromTitle($title);
    $updater = $page->newPageUpdater($user);
    if ($updater->hasEditConflict(intval($item['baserevid']))) { echo "PAGE597 ".json_encode(['title'=>$item['title'],'status'=>'conflict','expected'=>$item['baserevid'],'current'=>$page->getLatest()])."\n"; continue; }
    $parent = $updater->grabParentRevision();
    $content = $parent ? $parent->getContent(\MediaWiki\Revision\SlotRecord::MAIN,\MediaWiki\Revision\RevisionRecord::FOR_PUBLIC) : null;
    $before = $content ? $content->serialize() : '';
    if (!hash_equals($item['before_sha256'],hash('sha256',$before))) { echo "PAGE597 ".json_encode(['title'=>$item['title'],'status'=>'content-conflict'])."\n"; continue; }
    if ($plan['mode'] === 'preview') {
        $parsed = $services->getParser()->parse($draft,$title,\MediaWiki\Parser\ParserOptions::newFromUser($user));
        $html = $parsed->getRawText();
        $dateRows = [];
        foreach (['Released','Effective','Remastered','Blanked','Retired','Versions'] as $label) {
            if (preg_match('~<tr[^>]*>\s*<th[^>]*>\s*'.preg_quote($label,'~').'\s*</th>\s*<td[^>]*>(.*?)</td>\s*</tr>~s',$html,$match)) { $dateRows[$label]=trim(html_entity_decode(strip_tags($match[1]))); }
        }
        echo "PAGE597 ".json_encode(['title'=>$item['title'],'status'=>'preview','base'=>$item['baserevid'],'after_sha256'=>$item['after_sha256'],'date_rows'=>$dateRows,'cite_error'=>strpos($html,'mw-ext-cite-error')!==false,'html_bytes'=>strlen($html)])."\n";
        continue;
    }
    if ($before === $draft) { echo "PAGE597 ".json_encode(['title'=>$item['title'],'status'=>'nochange','revid'=>$parent->getId()])."\n"; continue; }
    $updater->setOriginalRevisionId(intval($item['baserevid']));
    $updater->setContent(\MediaWiki\Revision\SlotRecord::MAIN,\MediaWiki\Content\ContentHandler::makeContent($draft,$title));
    $updater->saveRevision(\MediaWiki\CommentStore\CommentStoreComment::newUnsavedComment($plan['summary']),EDIT_FORCE_BOT);
    if (!$updater->getStatus()->isOK()) { echo "PAGE597 ".json_encode(['title'=>$item['title'],'status'=>'save-failed','errors'=>$updater->getStatus()->getErrorsArray()])."\n"; continue; }
    $revision = $updater->getNewRevision();
    if (!$revision || $revision->getUser()->getName() !== 'Memory Core ChatGPT') { throw new \RuntimeException('New revision actor mismatch'); }
    $actual = $revision->getContent(\MediaWiki\Revision\SlotRecord::MAIN)->serialize();
    if (!hash_equals($item['after_sha256'],hash('sha256',$actual))) { throw new \RuntimeException('Saved content mismatch'); }
    $reviewed = null;
    if (\FlaggedRevs::inReviewNamespace($title)) {
        $reviewed = \FlaggedRevs::autoReviewEdit($page,$user,$revision,['accuracy'=>1],false,true);
        if (!$reviewed) { throw new \RuntimeException('Actual revision review failed'); }
    }
    echo "PAGE597 ".json_encode(['title'=>$item['title'],'pageid'=>$page->getId(),'status'=>'saved','revid'=>$revision->getId(),'parentid'=>$revision->getParentId(),'sha256'=>hash('sha256',$actual),'bytes'=>strlen($actual),'actor'=>$revision->getUser()->getName(),'review_inserted'=>$reviewed,'timestamp'=>$revision->getTimestamp()])."\n";
    $count++;
}
echo "DONE597 ".json_encode(['mode'=>$plan['mode'],'saved'=>$count,'pages'=>count($plan['pages']),'configuration_changes'=>false])."\n";
