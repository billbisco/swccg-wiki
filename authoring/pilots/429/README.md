# Vader image-viewer review pilot â€” Story429

The page is `SWCCG Wiki:Samples/Original Virtual Darth Vader image viewer`. Its three `Card` portraits become historical/remaster selectable panels plus an always-visible slip. The marker is required and initialization is idempotent. Without JavaScript all three images and the ordered source note remain available.

`wiki/SwccgChrome.php` is the existing live hook, newly recorded here from the checked baseline; its only behavior addition loads the two viewer resources on that exact sample title. Ordinary cards get no viewer resources. No extension, configuration or permission change is required. Existing global Card template and canonical card content remain unchanged.

Deploy viewer resources into the already-mounted host `chrome/` directory (container path `/swccg-chrome/`) and update the existing PHP hook in place (a single-file bind mount retains its inode). Validate PHP first; preserve and check the pre-change hash. Rollback restores that exact hook from the saved baseline, leaving the page useful as a static comparison; remove the new resources only after they are no longer referenced.

Validation covers default historical view, both selectors, invariant source slip/text, native comparison dialog/close/Escape/focus, keyboard controls, mobile width, fallback markup and ordinary-page boundary. The exact source assets are recorded in Story429 evidence. Native previews, source image hashes, independent backups, central preservation registration and live reviewed/public checks accompany delivery. Full rollout and GEMP are outside scope.
