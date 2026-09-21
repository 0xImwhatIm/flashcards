# FlashCards Illustration Batch｜Wave 09 School & Greetings

> Status: `generated / 6 Unit 1 words / review-ready / anchor-locked`
>
> Date: 2026-09-21 (Asia/Taipei)

> Final selection update: the user selected all six current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Batch decision

This wave covers six remaining concrete Unit 1 words: `Junior High School`, `Elementary School`, `Housewife`, `Nice to Meet You`, `Dear` and `Years Old`. The two school scenes use different building scale and student cues; the two greeting scenes use distinct interaction grammars; `Housewife` uses a household-care action rather than the married-couple grammar from Wave 08; and `Years Old` uses intentional growth stages rather than a generic child portrait.

These are review-ready semantic prototypes, not production replacements. They are stored in the project but are not wired into `index.html`.

## Shared anchor lock

- compact emerald/teal bean or gumdrop mascot with a low visual center; no long neck or tall slender anatomy;
- rounded back plates and a low soft tail, both visible unless a scene intentionally occludes them; standard single-mascot scenes use three plates, while `Years Old` intentionally grows from 3 to 4 to 5 plates;
- short rounded limbs, flat feet, two small black dot eyes and one short charcoal mouth arc;
- thick, slightly wobbly charcoal contour; opaque warm off-white paper field; restrained matte pigment grain;
- one clear semantic focus; 1–3 characters normally, with three repeated silhouettes only when age progression is the meaning;
- supporting species or buildings use the same ink, paper and low-saturation grammar;
- no text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows or eye highlights.

## Semantic grammar and prompt deltas

| ID | Word | Semantic construction | Planned output |
|---|---|---|---|
| W09-JHS | Junior High School | Older student-sized anchor mascot with a medium backpack and blank notebooks approaches a taller two-row-window school building. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/junior-high-school-v1.png` |
| W09-ELEMENTARY | Elementary School | Smaller walking child mascot with a small backpack and blank picture book approaches a low one-story schoolhouse; no numbers on the ground squares. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/elementary-school-v1.png` |
| W09-HOUSEWIFE | Housewife | One adult mascot folds laundry into a basket at a small home table; one scene-specific muted-mustard apron and a plant establish household care, with no partner. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/housewife-v1.png` |
| W09-NICE-MEET | Nice to Meet You | Two equal-status characters face each other, bow slightly and touch rounded hands palm-to-palm; one small mustard sparkle marks a welcoming first meeting. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/nice-to-meet-you-v1.png` |
| W09-DEAR | Dear | One mascot holds a blank cream envelope with one small mustard heart seal close to its chest; the image tests affectionate salutation without text or a second character. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/dear-v1.png` |
| W09-YEARS-OLD | Years Old | Three intentional growth stages of the same mascot progress from small to taller beside a small cake with three unnumbered candles; no digits or ruler. Back plates scale in size and increase in count from 3 to 4 to 5. | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/years-old-v3.png` |

### Prompt set

All six prompts used the same anchor-locked opening:

```text
Use case: illustration-story. FlashCards vocabulary prototype, square 1254x1254 illustration. Use the same compact emerald/teal green bean/gumdrop mascot as the provided FlashCards anchor: low visual center, three small rounded back plates, low soft tail, short rounded limbs, flat feet, two small black dot eyes and one short mouth arc. Flat hand-drawn children's illustration, the entire canvas filled with an opaque warm off-white paper field (#F8F6F0), generous upper negative space, one thin ground line, thick rounded charcoal ink with slight wobble, restrained matte pigment/paper grain, natural muted colors. No text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows, teeth or eye highlights. One semantic focus, readable at 160 px.
```

Prompt deltas:

- `Junior High School`: older student-sized mascot with medium blue-gray backpack and blank notebooks, taller two-row-window school building, no signs or extra students;
- `Elementary School`: smaller standing child with small mustard backpack and blank picture book, low one-story schoolhouse, no numbers or classroom crowd;
- `Housewife`: adult mascot in a scene-specific mustard apron folding blank laundry at a low table beside a basket and small plant, no partner or kitchen clutter;
- `Nice to Meet You`: two equal-status characters with simultaneous small bow and palm-to-palm rounded-hand touch, one mustard sparkle, no gift exchange;
- `Dear`: one mascot holding a blank envelope with a small mustard heart seal, affectionate salutation cue, no writing or romance scene;
- `Years Old`: three same-mascot growth stages with visible tails plus a small cake with three plain candles; back plates grow in size and count (3 → 4 → 5), with no digits, ruler or arrows.

## Result registry

Generation mode: built-in ImageGen. All six selected final assets are 1254×1254 RGB PNGs and have a 160 px thumbnail export. `review-ready` remains below `pilot_accepted`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W09-JHS | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/junior-high-school-v1.png` | `d48fe230da04ff0b223a33f97f0269e8efc4c7bcfc7af90875c001e82c890c2f` | `generated / review-ready` | Taller two-row-window school and older-student backpack read at 160 px; tail and three plates remain visible; no building text. |
| W09-ELEMENTARY | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/elementary-school-v1.png` | `aa4bd28f6850038418ef596461fa0d258c0c2edad7ba2caae6605a7010be836d` | `generated / review-ready` | Smaller child, low one-story schoolhouse and blank book read at 160 px; tail and three plates remain visible; no numbers. |
| W09-HOUSEWIFE | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/housewife-v1.png` | `e5ee44d0e93fac53c7ad3e67c2004635657bc7344104b8aed3bb549bedbd2a25` | `generated / review-ready` | Laundry-folding action, basket, plant and apron read at 160 px; tail and three plates remain visible; no partner. |
| W09-NICE-MEET | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/nice-to-meet-you-v1.png` | `d4d11c412df2f330715f9fd7185b833a9096a2e8986bbff60c1c936ae650f566` | `generated / review-ready` | Equal-status two-character greeting, rounded-hand touch and welcome sparkle read at 160 px; green tail and three plates remain visible. |
| W09-DEAR | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/dear-v1.png` | `4dacb26a1a4909888c89bac093831730be56311c8fa1f49f1ce63e8f8db7b752` | `generated / review-ready` | Blank envelope and single heart seal read at 160 px; tail and three plates remain visible; no writing. Semantic interpretation remains open to affectionate salutation review. |
| W09-YEARS-OLD | `assets/visual-prototypes/batch-v0.2/wave-09-school-greetings/years-old-v3.png` | `311d153ef382039f3de7b0a3d5efa3106f15ac7c832cc8cd59d18e8ce4350236` | `generated / edited / review-ready` | Three growth stages and three plain candles read at 160 px; back plates now scale in both size and count (3 → 4 → 5); repeated silhouettes are intentional age progression, not a crowd. |

### Superseded audit output

`years-old-v1.png` remains preserved as the original review candidate. Its three back plates stayed nearly the same size across the three growth stages. `years-old-v2.png` remains preserved as the intermediate correction with proportional plate scaling. `years-old-v3.png` is the current candidate: plate size and count both increase with age (3 → 4 → 5); no other scene element was intentionally changed.

## QA gates

- [x] 1254×1254 RGB output for all six selected final assets.
- [x] 160 px thumbnail remains semantically readable for all six.
- [x] Green anchor tail and rounded plates remain visible in each final scene; standard scenes retain three plates and `Years Old` uses the explicit 3 → 4 → 5 growth rule.
- [x] No text, logo, watermark, digit or readable label appears.
- [x] Junior High School and Elementary School have visibly different building scale and student cues.
- [x] Housewife is separated from Wife by household-care action and the absence of a partner.
- [x] Years Old v3 applies the targeted proportional back-plate count-and-size correction and keeps the 160 px semantic read.
- [ ] Blind learner review of `Dear` versus a generic letter/gift image.
- [ ] Blind learner review of `Nice to Meet You` versus other reciprocal interaction words.
- [ ] Blind learner review of `Years Old` versus birthday-only interpretation.
- [ ] `pilot_accepted` and local app wiring.

## Next order

1. Review Wave 08 and Wave 09 with labels hidden; focus on `Dear`, `Nice to Meet You`, `Years Old` and the two school-level distinctions.
2. Generate the remaining trait/expression words (`Really`, `Handsome`, `Woman`, `New`, `Very`, `Beautiful`, `Young`) as a separate semantic wave.
3. Handle `Right` only after its intended direction/correctness sense is selected.
