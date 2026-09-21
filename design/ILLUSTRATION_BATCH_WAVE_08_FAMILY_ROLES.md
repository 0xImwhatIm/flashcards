# FlashCards Illustration Batch｜Wave 08 Family Roles

> Status: `generated / 5 Unit 1 words / review-ready / anchor-locked`
>
> Date: 2026-09-21 (Asia/Taipei)

> Final selection update: the user selected all five current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Batch decision

This wave tests the five remaining concrete family-role words that need a relationship cue rather than a generic portrait: `Uncle`, `Aunt`, `Wife`, `Daughter` and `Husband`. The scenes deliberately use two characters when the relation needs a partner or child, while keeping one primary semantic focus. `Family` and `Parents` remain governed by the existing broader-group and two-adults-plus-child rules; these five images must not collapse into either of those meanings.

These are review-ready semantic prototypes, not production replacements. They are stored in the project but are not wired into `index.html`.

## Shared anchor lock

- compact emerald/teal bean or gumdrop mascot with a low visual center; no long neck or tall slender anatomy;
- three small rounded back plates and a low soft tail, both visible unless the scene intentionally occludes them;
- short rounded limbs, flat feet, two small black dot eyes and one short charcoal mouth arc;
- thick, slightly wobbly charcoal contour; opaque warm off-white paper field; restrained matte pigment grain;
- one clear semantic focus; 1–3 characters only when the meaning requires them;
- supporting species may use one clear silhouette cue (the triceratops child uses three rounded horns), while preserving the same ink and paper grammar;
- no text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows or eye highlights.

## Semantic grammar and prompt deltas

| ID | Word | Semantic construction | Planned output |
|---|---|---|---|
| W08-UNCLE | Uncle | A larger adult green mascot gives a small child a piggyback ride; a single muted-mustard bow tie is the restrained adult-male cue. | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/uncle-v1.png` |
| W08-AUNT | Aunt | A larger adult green mascot helps a small terracotta triceratops child with a scarf; one muted-mustard flower clip is the restrained adult-feminine cue. | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/aunt-v2.png` |
| W08-WIFE | Wife | Two adult characters hold hands over one small wedding ring on a cream cushion; the green primary role uses one flower clip and the companion stays visually secondary. | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/wife-v1.png` |
| W08-HUSBAND | Husband | Two adult characters hold hands over one small wedding ring on a cream cushion; the green primary role uses one blue-gray tie and the companion stays visually secondary. | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/husband-v1.png` |
| W08-DAUGHTER | Daughter | A small walking green child with a tiny satchel holds one taller adult's hand; a small flower clip marks the daughter cue and the standing pose separates it from `Baby`. | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/daughter-v1.png` |

### Prompt set

All five prompts used the same anchor-locked opening:

```text
Use case: illustration-story. FlashCards vocabulary prototype, square 1254x1254 illustration. Use the same compact emerald/teal green bean/gumdrop mascot as the provided FlashCards anchor: low visual center, three small rounded back plates, low soft tail, short rounded limbs, flat feet, two small black dot eyes and one short mouth arc. Flat hand-drawn children's illustration, the entire canvas filled with an opaque warm off-white paper field (#F8F6F0), generous upper negative space, one thin ground line, thick rounded charcoal ink with slight wobble, restrained matte pigment/paper grain, natural muted colors. No text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows, teeth or eye highlights. One semantic focus, readable at 160 px.
```

Prompt deltas:

- `Uncle`: adult green mascot with one small mustard bow tie giving a smaller child a piggyback ride; no other adults or crowd;
- `Aunt`: adult green mascot with one small mustard flower clip helping a small terracotta triceratops child put on a simple scarf; no other adults;
- `Wife`: green adult primary plus one adult blue-gray companion, hands joined above one plain mustard wedding ring on a cream cushion; flower clip only, no ceremony;
- `Husband`: green adult primary plus one adult terracotta companion, hands joined above one plain mustard wedding ring on a cream cushion; small blue-gray tie only, no ceremony;
- `Daughter`: small standing green child with one flower clip and tiny mustard satchel holding one adult's hand; no swaddle, cradle or baby props.

## Result registry

Generation mode: built-in ImageGen. All five selected final assets are 1254×1254 RGB PNGs and have a 160 px thumbnail export. `review-ready` remains below `pilot_accepted`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W08-UNCLE | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/uncle-v1.png` | `e9b3a6631a374a9b5599c2fce0d5308d867a00153757e8283f9d85580ef4a67f` | `generated / review-ready` | Piggyback relation and adult/child scale read at 160 px; green tail and three plates remain visible. |
| W08-AUNT | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/aunt-v2.png` | `e8a309056ec7ccd726663dd667de0579a0e2449e2c870112470ed75cf2ec8a76` | `generated / review-ready` | Caring scarf action, flower clip and triceratops cue read at 160 px; green tail and three plates remain visible. |
| W08-WIFE | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/wife-v1.png` | `38b1c3c22149a7a6e487705ba207eb0d9652447e50b02ba56b38c6d527f00941` | `generated / review-ready` | Two-adult couple, joined hands, ring and flower clip read at 160 px; green tail and three plates remain visible. |
| W08-HUSBAND | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/husband-v1.png` | `c9f6ca0b350682c16eea1aae0733107d8967fd87c1b7c2ae63a1bf7c13b50286` | `generated / review-ready` | Two-adult couple, joined hands, ring and tie read at 160 px; green tail and three plates remain visible. |
| W08-DAUGHTER | `assets/visual-prototypes/batch-v0.2/wave-08-family-roles/daughter-v1.png` | `4e5d6afa60b44bd1d1c8cc539f07d7af19366a0ca84c174bbb220e9a7c6f3e6c` | `generated / review-ready` | Standing child/parent scale, hand-holding and satchel separate Daughter from Baby at 160 px; green tail and three plates remain visible. |

### Superseded audit output

`aunt-v1-transparent-hold.png` is retained as audit history only. It had an unintended transparent background, so `aunt-v2.png` was regenerated with an opaque warm-paper field.

## QA gates

- [x] 1254×1254 RGB output for all five selected final assets.
- [x] 160 px thumbnail remains semantically readable for all five.
- [x] Green anchor tail and three rounded plates remain visible in every final scene.
- [x] No text, logo, watermark or readable label appears.
- [x] Aunt v1 was held and v2 regenerated after the transparent-background drift was identified.
- [ ] Blind learner review of Uncle/Aunt versus generic adult-child relationship.
- [ ] Blind learner review of Wife/Husband cue clarity and cultural neutrality.
- [ ] `pilot_accepted` and local app wiring.

## Next order

1. Review Wave 07 and Wave 08 together with labels hidden; specifically test `Baby` versus `Daughter`, and `Uncle`/`Aunt` versus generic family scenes.
2. Review the Wife/Husband role cues before treating them as production grammar; the ring establishes marriage while the single accessory identifies the target role.
3. Generate the remaining school/identity and expression words (`Junior High School`, `Elementary School`, `Dear`, `Housewife`, `Nice to Meet You`, `Years Old`) as a separate contextual wave.
4. Keep `Right` gated until its intended meaning is selected.
