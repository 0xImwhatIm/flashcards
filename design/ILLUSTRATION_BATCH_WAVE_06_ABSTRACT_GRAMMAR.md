# FlashCards Illustration Batch｜Wave 06 Abstract Grammar

> Status: `generated / 4 Unit 2 words / review-ready / anchor-locked`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected `Favorite`, `Hungry`, and `Special` as listed, and explicitly selected `But` v1 (`but-v1-character-hold.png`) over v2. All four are wired in `index.html`; v2 remains historical. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Batch decision

The current Unit 2 gaps were `Favorite`, `But`, `Hungry`, `Special` and `Right`. This wave generates the first four because each has a concrete visual grammar that can be tested without adding text. `Right` remains deferred until the owner selects the intended sense: **right-hand direction/location** or **correctness**.

These are semantic prototypes, not production replacements. They are stored in the project for review but are not yet wired into `index.html`.

## Shared anchor lock

- compact bean/gumdrop green mascot with a low visual center; no long neck or tall slender anatomy;
- three small rounded back plates and a low soft tail, both visible whenever the scene does not intentionally occlude them;
- short rounded arms, flat feet, two small black dot eyes and one short mouth arc;
- charcoal near-black wobbly contour, opaque warm off-white paper field, restrained matte pigment grain;
- one semantic focus, 1–3 characters only when the meaning requires them;
- no text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows, teeth or eye highlights.

## Semantic grammar and prompt deltas

| ID | Word | Semantic construction | Planned output |
|---|---|---|---|
| W06-FAVORITE | Favorite | One mascot hugs one selected small book-like object; two quiet alternatives remain nearby; one restrained mustard star marks preference. | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/favorite-v1.png` |
| W06-BUT | But | One mascot stands between a sunny play possibility and a rain/puddle obstacle; the contrast is spatial, with no arrows or text. | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/but-v1-character-hold.png` (user-selected) |
| W06-HUNGRY | Hungry | One mascot holds its tummy and looks toward an empty bowl with two crumbs; two subtle curved rumble marks support the state. | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/hungry-v1.png` |
| W06-SPECIAL | Special | One mascot presents a single unique mustard star-shaped object on a simple cream pedestal; no alternatives or crowd. | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/special-v1.png` |

### Prompt set

All four prompts used this shared opening and constraint block:

```text
Use case: illustration-story
Asset type: FlashCards vocabulary prototype, square 1254x1254 illustration.
Create the same compact green bean/gumdrop mascot in a flat hand-drawn children's illustration. Use a warm off-white paper field, generous upper negative space, one thin ground line, thick rounded charcoal ink, slight line wobble, matte pigment/paper grain, and restrained natural colors. Preserve the canonical low soft tail, three small rounded back plates, short rounded arms with no fingers, flat feet, two small black dot eyes, and one short mouth arc. No text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows, teeth, or eye highlights. Make one semantic focus readable at 160 px.
```

Prompt deltas:

- `Favorite`: one chosen small mustard-covered book-like object is hugged by the mascot; two smaller plain muted alternatives sit nearby; one restrained mustard star above the chosen object; preference, not gift or special.
- `But`: one mascot holds a mustard ball at the boundary between a small warm sun and a muted blue-gray rain cloud with a puddle; spatial contrast, not movement, no arrows or labels.
- `Hungry`: one mascot holds its tummy and looks at an empty shallow bowl with exactly two crumbs; two subtle curved rumble marks near the tummy; hungry, not illness or sadness.
- `Special`: one mascot presents one unique muted-mustard star-shaped object above a simple cream pedestal with a restrained halo; distinctive and important, not favorite or gift.

## Result registry

Generation mode: built-in ImageGen. All final assets are 1254×1254 RGB PNGs and passed the 160 px thumbnail check. `review-ready` remains below `pilot_accepted`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W06-FAVORITE | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/favorite-v1.png` | `994c5bd34fcda3e0692ae3c8afa6fbf37dc062f08cb5bbfeb92e7617b5a4bda5` | `generated / review-ready` | Semantic pass: one chosen object is visibly preferred among quiet alternatives. Character pass: tail, three plates and canonical face readable. |
| W06-BUT | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/but-v1-character-hold.png` | `see file` | `user-selected / wired / historical v2 retained` | Semantic pass: sunny possibility is visibly interrupted by rain/puddle contrast. User explicitly chose v1; the earlier v2 face-correction candidate remains available for comparison. |
| W06-HUNGRY | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/hungry-v1.png` | `699441a2751f299dbfcd1cf8b45ccfddaa1c71e9d4edd590cb50fd65a5ecff01` | `generated / review-ready` | Semantic pass: tummy-holding pose, empty bowl and two crumbs read at thumbnail size. Character pass: tail, three plates and canonical face readable. |
| W06-SPECIAL | `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/special-v1.png` | `9a548c31fc7710494a01942d47146098868ef1b41d90019cad10f420bcc2c8cd` | `generated / review-ready` | Semantic pass: one unique highlighted object reads as distinctive. Character pass: tail, three plates and canonical face readable. |

### Superseded audit output

`but-v2.png` remains as audit history. The user explicitly selected `but-v1-character-hold.png` for the current final mapping; any future character cleanup should create a new version rather than overwrite it.

## QA gates

- [x] 1254×1254 RGB output for all four final assets.
- [x] 160 px thumbnail remains semantically readable for all four.
- [x] Tail and three rounded plates remain visible in each final scene.
- [x] No text, logo, watermark or readable label appears.
- [x] `But` v1 is wired by explicit user selection; v2 is retained as history.
- [ ] Blind learner review.
- [ ] `pilot_accepted` and local app wiring.

## Next order

1. Review these four semantic prototypes and resolve any Favorite／Special or But／contrast ambiguity.
2. Decide the intended sense of `Right` before generating it.
3. Then begin Unit 1's 22 remaining words by semantic family rather than one unreviewed bulk run.
