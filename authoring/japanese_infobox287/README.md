# #287 — Japanese/shared card infobox migration in progress

Bill authorized migration first, then remaining Japanese-set content repairs. Shared guidance: ai-team-skills commit 426db52.

Current scope: 794 live manual infoboxes (793 Japanese plus the oversized English promo), captured after #361. No card article or production Template:Card has yet been changed for this migration.

Inputs: heads-before.json, before-renders.json.gz, targets.json, english-sample.json, baseline-summary.json, lint-backlog.csv. Converter: convert.py. Optional template extension: template.py / template-draft.wiki. Publication must use exact current revision/hash and timestamps; never replay old packets over a newer revision.

The draft preserves native sections and existing metadata/navigation. Old undefined photo references are restored from their existing printing-specific File pages and separately recorded. Further translation, statistics or identity repairs belong to the later content pass. The follow-up Task completes the original style backlog immediately after rebuilding.

Next: publish only Template:Card/sandbox, render the 10 initial samples and 50 English controls, fix conservation failures, then validate all 794 drafts before touching the production template or cards.
