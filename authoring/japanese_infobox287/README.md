# #287 — Shared Japanese card infobox migration

Live migration complete: 794 cards, 797 changed pages including template controls, zero lint/Cite errors, 50 unchanged English controls. [Migration report](migration-report.md) · [all live page links](published-pages.md) · [PASS report](287-pass-report.md).

Reproduction from the authoring bundle root: install requirements, then run `python work/japanese-infobox287/check.py drafts` and `python work/japanese-infobox287/fidelity.py` for captured conservation checks. `verify.py` performs live read-only checks; publication scripts are guarded and should never be replayed over newer revisions. `convert.py` must be followed by `set-icons.py` when rebuilding drafts.

No separate wiki Test exists; sandbox examples preceded live publication. Code and source backup: [PR #15](https://github.com/billbisco/swccg-wiki/pull/15). Task #366 resolves the original citation/style backlog. Follow-up #369 audits the remaining Japanese sets.
