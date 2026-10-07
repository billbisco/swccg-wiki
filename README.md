# SWCCG Wiki

Preservation copy of encyclopedia wikitext for [wiki.swccg.com](https://wiki.swccg.com).

This repository holds generated MediaWiki pages, generators, and championship transcribes so the encyclopedia can be rebuilt if the live site is unavailable.

Live site: https://wiki.swccg.com

## License

Fan encyclopedia. Respective rights belong to their owners.

Star Wars, Star Wars Customizable Card Game, card names, card text, and related marks remain with Lucasfilm Ltd., Disney, Decipher, and/or the Players Committee. This project claims none of those rights. Original arrangement, generators, and documentation in this repository may be copied to preserve and rebuild the encyclopedia.

See `NOTICE`.

## Layout

- `pages/` — MediaWiki wikitext (cards, tournaments, players, rules)
- `generate_*.py` — page generators
- `encyclopedia/**/transcribe_*.py` — championship 60 transcribes (sheet emails redacted)
- `chrome/` — shared site header/footer
- `apply-*.sh` — apply helpers used on the live wiki
- `SWCCG-Wiki-PRD.md` — product document

Scans, PDFs, extract rasters, and card-art binaries stay off this repo because of size. Those files live on the live wiki and can be dumped separately (MediaWiki `dumpBackup.php` plus an image dump, or Internet Archive).

## What this is not

This is a fan encyclopedia. It is not Lucasfilm, Disney, Decipher, or the Players Committee.
