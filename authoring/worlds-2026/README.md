# 2026 World Championship (Bloomington, MN, 23–25 Oct 2026) — LIVE 2026-10-29

- Source of each list: the PC's official GEMP files (forum t=87042, `2026 Worlds Lists.zip` + corrected
  `26Worlds Kramer DS IE.txt`), in `gemp-files/`. Downloaded through FlareSolverr on the gemp server: a
  `request.get` on the attachment URL inside a session makes its Chrome save the file to `/app/Downloads`
  in the `flaresolverr` container (`docker cp` it out).
- Standings: PC event page (Day 1 1–58, Top 8 order). Per-deck PC posts used as each page's first source and to
  cross-check card counts (`report.txt`).
- `gen_w26.py` → hub + 132 deck pages in the 2026 BWC/Nationals layout (plain links, Starting Card / Starting
  Interrupt, GEMP download line); wiki printing chosen by matching the blueprint set to the card image's
  `V<n>-` prefix; Set 27 cards via Category:Virtual Set 27. `persons.py` → Tournament Results rows (53 players),
  5 new player pages. Emmett Armstrong DS: 2x The Ebb Of Battle added from the post (not in GEMP).
- Applied as Holocron Claude: 132 files, 324 pages; 0 conflicts, no red links. Page list: `changed-pages-2026-10-29.md`.
