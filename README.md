# CODEBORN

A Skannerz-inspired barcode creature-collector. Scan any code — the code deterministically
births a creature: species, tier, grade, stats, and (1-in-4096) a shiny. Same code, same
creature, every time. Collect all 160, build a team of 3, battle.

**Play it:** open `index.html` in any browser — the whole game is one self-contained file
(no build step, no dependencies). Enable GitHub Pages on this repo and it's playable at
your github.io URL.

## Features
- **Deterministic engine** — xmur3/mulberry32 hashing maps any code to a species + grade
  (C/B/A/S/SS) + IVs + shiny roll. Codes are tradeable: a friend scanning your code gets
  the identical creature.
- **160-species tiered roster** — 70 common / 50 uncommon / 30 rare / 5 pseudo-legendary /
  3 legendary / 2 mythical, with weighted encounter odds (mythical ≈ 1 in 165 scans).
- **Two sprite systems** — Generator 3.0 (anatomical body-plan archetypes: quadrupeds,
  serpents, avians, insectoids, dragons... with elemental anatomy features) fills any
  species without hand art; imported 64×64 indexed sprites (own palettes, hue-rotated
  shinies) replace them one sheet at a time. 46/160 imported so far.
- **Battles** — team of 3, speed order, 8-type effectiveness chart, swap costs a turn,
  win to capture the wild lead's code.
- **Duplicate reinforcement** — rescanning an owned code feeds the original (+2%/dupe,
  cap +50%).
- **Persistence** — artifact storage / localStorage adapter; save is just codes + counters,
  creatures regenerate deterministically.

## Art pipeline
1. Generate a sheet with `docs/codeborn_sheet_prompt.md` (magenta-keyed, one tier per sheet).
2. `python3 tools/extract_sheet.py sheet.png > sprites.json`
3. Wire entries into the `HAND` table in `index.html`.

Proof sheets and style-bible artifacts live in `art/`.

## Roadmap
- Remaining sheets: 1× common (30), 2× uncommon, 1× rare, 9 solo high-tier renders
- Ability system (Magma Mantle, Volcanic Heart...)
- Animation frames (idle/walk/attack)
- Camera barcode scanning for the phone build
