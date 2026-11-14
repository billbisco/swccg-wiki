# Original Virtual image pilot

The initial three review pages and their hub remain allowlisted in card-image-pilot.json. Bill approved extending the cohort to all twelve later Original Virtual Set 1 publication articles after reviewing the examples. Each original, remaster and publisher slip was inspected for matching printed text, symbols and supported statistics before activation. Set thumbnails and hover consumers remain outside this cohort. Card publication/text state and image language are explicit metadata; only matching renditions may form a pair.

The existing Luke Skywalker review sample already had a deployed legacy hook when this work began. Preserve that hook and its assets unchanged; it is not activated by the new pilot manifest. New markers and legacy Vader markers are distinct, so the old viewer cannot initialize the three updated panels. This is compatibility preservation, not another rollout example or ownership transfer.

Use `npm ci --ignore-scripts` then `npm run test:card-images` for the15 behavioral checks. PHP is syntax-checked against the deployed MediaWiki PHP runtime. Native API persistence and live browser geometry/cache checks follow controlled deployment.

Account preference: swccg-card-images through core GetPreferences/UserGetDefaultOptions and API options. Guest preference: the same key in browser localStorage. Page config contains only public image mappings and localized labels; account options are fetched through authenticated private API requests. Explicit Save default affects future panel initialization; per-card buttons do not write preferences.

Rollback: restore the exact old /opt/swccg-wiki/SwccgChrome.php in place from the scoped before-deploy volume backup. The legacy viewer remains intact. New chrome assets can remain dormant. Restore the old Vader sample revision if desired; preserve new original files and their provenance. Do not roll back unrelated common CSS, templates or other sample pages.

Archive.org uploads and Save Page Now remain paused. Bill explicitly allows reading, historical searches and downloads. Backups and registered pending objects are not checked external captures; an indexed digest match alone is not replay verification. Image source credits point to the historical PC capture/PDF and reconstruction recipe, separately from wiki-upload preservation. Wider era, consumer and language coverage remains tracked on #443.

Batch 2 rollback: restore the exact pre-batch card-image-pilot.json from the scoped volume backup, retaining the original four-page/three-card cohort. Purge only affected MediaWiki page and exact Nginx cache keys. If content rollback is necessary, guard every revision against subsequent edits and retain independently useful primary-source/provenance corrections and historical uploads. Never revert shared Versions templates or another editor's card text.
