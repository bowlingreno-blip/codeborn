# CODEBORN — SPRITE SHEET GENERATION PROMPT (extraction-optimized, v1)

Fill in the two variables, then paste the whole block into your image generator.

- `{TIER}` = COMMON / UNCOMMON / RARE
- `{N}` = sheet number for that tier

---

## PROMPT — ROSTER SHEET (commons, uncommons, rares)

Create a video game pixel-art sprite sheet. This is a clean production asset, NOT an infographic — no stat panels, no anatomy callouts, no decorative framing.

CANVAS AND GRID
- Landscape orientation, highest available resolution.
- A uniform grid of exactly 8 columns and 5 rows, separated by thin solid black gridlines.
- The background of every cell is solid flat magenta (#FF00FF). No gradients, no texture, no vignette, no lighting effects on the background.
- Generous gutters: every sprite is centered in its cell with clear magenta margin on all four sides. No sprite may touch or cross a gridline.

SPRITES
- Exactly one creature per cell — 40 creatures total, full body visible, nothing cropped.
- Retro pixel-art style: sharp square pixels, hard edges, flat colors. NO anti-aliasing, no blur, no soft shading, no outer glow, no drop shadows.
- Every creature has a continuous 1–2 pixel dark outline enclosing its entire silhouette. This is mandatory — the outline must be unbroken.
- Maximum of about 14 colors per creature. Never use magenta or near-magenta anywhere inside a creature.
- Front or three-quarter view, standing idle pose, consistent scale across the sheet.

COLUMNS = ELEMENT, in this fixed left-to-right order:
1 Fire · 2 Water · 3 Earth · 4 Electric · 5 Ice · 6 Poison · 7 Shadow · 8 Psychic
The element must be expressed through anatomy, not just color: Fire = volcanic horns, ember vents, smoke manes. Water = fins, wave tails, shell armor. Earth = stone plating, crystal growths. Electric = zigzag spines, lightning horns, antennae. Ice = frozen antlers, icicle features. Poison = venom sacs, thorns, dripping stingers. Shadow = elongated forms, obsidian horns, glowing eyes. Psychic = floating detached ornaments, crystal crests, third eyes.

EVERY CREATURE ON THIS SHEET IS {TIER} TIER. Apply the tier's design language:
- COMMON: small, simple, cute, one defining feature, instantly readable silhouette.
- UNCOMMON: more elaborate anatomy, two defining traits, light elemental armor.
- RARE: complex silhouette, distinct species identity, larger appendages, majestic or aggressive presence.

BODY VARIETY
Every creature must use a distinct body plan — quadruped, biped, serpent, avian, insectoid, crustacean, cephalopod, bat, fish, turtle, spider, feline, canine, cervid, amphibian, pangolin, and so on. Believable anatomy: defined torso, functional limbs, clear head and neck, real weight distribution. No blobs, no floating spheres, no shapeless masses. No two creatures on the sheet may share nearly the same silhouette.

TEXT
No text anywhere on the image except one large plain header at the top: "{TIER} — SHEET {N}".

---

## PROMPT — HIGH-TIER SINGLE RENDER (pseudo, legendary, mythical)

For the 10 high-tier species, generate ONE creature per image so the entire canvas budget goes to fidelity. Same rules, adjusted:

Create a single video game pixel-art creature sprite, centered on a solid flat magenta (#FF00FF) background filling the whole canvas. Retro pixel-art style: sharp square pixels, flat colors, no anti-aliasing, no shadows or glow. Continuous 1–2 pixel dark outline enclosing the full silhouette. Maximum ~16 colors, never magenta inside the creature. Full body, three-quarter view, idle pose.

The creature is {ELEMENT} element, {TIER} tier:
- PSEUDO: apex predator, complex anatomy, large horns/wings/fins/armor, hero-creature quality.
- LEGENDARY: awe-inspiring, regal posture, intricate elemental integration, unforgettable silhouette.
- MYTHICAL: divine and ancient, elegant, unique anatomy unlike any other creature — face-of-the-franchise quality.

{Describe the specific creature concept here — body plan, key features, personality.}

---

## NAMES

Ask the generator (as text output, NOT rendered in the image) for a plain list of the 40 creature names in grid order, row by row, left to right. Paste that list into Claude along with the sheet.

---

## QA CHECKLIST — before sending a sheet to Claude
- [ ] Background is flat magenta everywhere behind and between sprites
- [ ] No sprite touches or crosses a gridline
- [ ] Every outline looks closed (no gaps where creature color meets magenta directly... a quick squint test is fine)
- [ ] No soft shadows or glows under any creature
- [ ] Only text on the image is the big header
- [ ] Sheet is one tier only

## WHY THESE RULES (each maps to a real failure from the first extraction)
- **Magenta background** → the cream sheet made white/ice creatures unextractable; magenta is distinct from every creature palette, so extraction becomes exact color-keying instead of guesswork.
- **Mandatory closed outline** → stops background removal from eating into light-colored creatures.
- **Gutters + no line contact** → the first sheet had sprites bleeding across cells into their neighbors' crops.
- **No anti-aliasing / flat colors** → soft edges are what turn crisp sprites into mush at 64×64.
- **One tier per sheet + fixed column order** → the position of a sprite IS its metadata; no unreliable tiny text to read.
- **High tiers rendered solo** → your franchise faces deserve the full canvas, not 1/40th of one.
