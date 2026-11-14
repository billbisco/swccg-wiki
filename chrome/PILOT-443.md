# Original Virtual image pilot

Three exact review pages and their hub are allowlisted in card-image-pilot.json. Canonical card pages, set thumbnails and hover consumers remain unchanged in this first cohort. Card publication/text state and image language are explicit metadata; only matching renditions may form a pair.

The existing Luke Skywalker review sample already had a deployed legacy hook when this work began. Preserve that hook and its assets unchanged; it is not activated by the new pilot manifest. New markers and legacy Vader markers are distinct, so the old viewer cannot initialize the three updated panels. This is compatibility preservation, not another rollout example or ownership transfer.

Use `npm ci --ignore-scripts` then `npm run test:card-images` for the13 behavioral checks. PHP is syntax-checked against the deployed MediaWiki PHP runtime. Native API persistence and live browser geometry/cache checks follow controlled deployment.

Account preference: swccg-card-images through core GetPreferences/UserGetDefaultOptions and API options. Guest preference: the same key in browser localStorage. Page config contains only public image mappings and localized labels; account options are fetched through authenticated private API requests. Explicit Save default affects future panel initialization; per-card buttons do not write preferences.

Rollback: restore the exact old /opt/swccg-wiki/SwccgChrome.php in place from the scoped before-deploy volume backup. The legacy viewer remains intact. New chrome assets can remain dormant. Restore the old Vader sample revision if desired; preserve new original files and their provenance. Do not roll back unrelated common CSS, templates or other sample pages.

All Archive.org traffic remains paused. Backups and registered pending objects are not checked external captures. Wider consumer/language coverage remains tracked on #443 after Bill reviews these examples.
