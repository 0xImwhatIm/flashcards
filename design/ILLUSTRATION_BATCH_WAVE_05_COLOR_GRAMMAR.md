# FlashCards Illustration Batch｜Wave 05 Color Grammar

> Status: `generated / 4 Unit 2 words / review-ready / anchor-locked`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected the four color assets and the `Colorful` extension; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Scope

This bounded wave covers the four Unit 2 color words that still lack a current image/prototype: `Purple`, `Color`, `Gray` and `Brown`. They share one visual grammar so the learner reads color as the semantic focus rather than as four unrelated objects.

Deferred for later semantic review: `Favorite`, `But`, `Hungry`, `Special` and `Right`. `Right` remains gated until direction/location versus correctness is selected.

## Shared color-chip grammar

- Use one large, flat, rounded color swatch or paint chip as the semantic focus.
- Keep the green anchor beside the chip in a 3/4 pose with its low soft tail visibly readable, three rounded back plates, short rounded limbs, dot eyes and short mouth.
- `Purple`, `Gray` and `Brown` each show only one target-color chip; do not add competing color objects.
- `Color` shows a small orderly palette of four flat chips (purple, gray, brown and green) with no text, labels or rainbow clutter.
- The chip is not a named object, room, food or clothing item; its shape stays neutral and rounded.

## Absolute anchor lock

- compact bean/gumdrop body with low visual center; no long neck or tall slender anatomy;
- three small rounded back plates and a low soft tail that remains visible unless the scene intentionally occludes it;
- short rounded arms and flat rounded feet; no fingers or toe lines;
- two small black dot eyes and one short mouth arc; no cheeks, blush, eyebrows, teeth, highlights or extra facial marks;
- green `#18B985`／`#13A97C`, charcoal `#202223`, opaque warm off-white `#F8F6F0`, matte paper/pigment texture;
- no text, letters, numbers, logos, watermark, glossy 3D, neon colors or crowded scenery.

## Prompt deltas and planned outputs

| ID | Word | Prompt delta | Planned output |
|---|---|---|---|
| W05-PURPLE | Purple | Anchor beside one large neutral rounded swatch filled only with muted purple; no other colored object. | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/purple-v1.png` |
| W05-COLOR | Color | Anchor arranging four small flat swatches in purple, gray, brown and green; orderly palette, no labels. | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/color-v1.png` |
| W05-GRAY | Gray | Anchor beside one large neutral rounded swatch filled only with muted cool gray; no other colored object. | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/gray-v1.png` |
| W05-BROWN | Brown | Anchor beside one large neutral rounded swatch filled only with muted warm brown; no other colored object. | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/brown-v1.png` |

## QA gates

- [x] Target color is immediately visible at 160 px without text.
- [x] `Color` reads as a general palette, not as a single purple/gray/brown object.
- [x] All four retain a visibly readable low tail and three rounded back plates.
- [x] No unrelated object vocabulary is introduced by the swatch shape.
- [x] Local `index.html` image-override wiring completed after path and layout checks; hidden-label review and `pilot_accepted` remain pending.

## Result registry

Generation mode: built-in ImageGen, one prompt per asset. All four outputs are 1254×1254 RGB PNGs and passed 160 px thumbnail QA. `review-ready` is not `pilot_accepted`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W05-PURPLE | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/purple-v1.png` | `33f102c6583a83786075b6e3be4936c4745bd57a292c34bb48da49e767d92436` | `generated / review-ready` | Pass: single muted-purple chip; tail and three plates readable. |
| W05-COLOR | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/color-v1.png` | `1893e490c806c88de8eef32ed0547a342f9e37ab0b28f61a8a21cff6cb112a30` | `generated / review-ready` | Pass: exactly four ordered chips; general color concept reads at 160 px. |
| W05-GRAY | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/gray-v1.png` | `386faf2fc41f0cefc3277b63596a223c191e3a14ad779f2794b4677f50c6060c` | `generated / review-ready` | Pass: single muted-gray chip; no cloud/wall object cue. |
| W05-BROWN | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/brown-v1.png` | `a8daf0ac6c133049dd50a7a83797cbbed0832498fc2b8f0b82b0a8b23d94b7e1` | `generated / review-ready` | Pass: single muted-brown chip; no box/table/food object cue. |

The four base assets remain review-ready prototypes. They are now locally wired through the app's explicit image-override map; this is a reversible local integration and is not a production replacement or `pilot_accepted` decision.

## Semantic extension prototype｜Colorful

The approved `Color` palette is also the source for a separate exploratory `Colorful` prototype. It keeps the same mascot and replaces the orderly chips with controlled purple, gray, brown, green, coral, blue and yellow ink-like splashes across the warm paper field. The splashes communicate “多采多姿” while leaving the mascot’s face, three plates and low tail unobstructed.

| Word | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| Colorful | `assets/visual-prototypes/batch-v0.2/wave-05-color-grammar/colorful-v1.png` | `567129b51c48e7a671ee62b35685cc32acd7e9c97fc9054276d8b8f32d0a9ca1` | `generated / exploratory review-ready` | Pass: opaque 1254×1254 RGB, 160 px thumbnail remains legible; tail and three plates visible; no text or extra characters. |

`Colorful` was added to the live Unit 2 vocabulary array and is included in the current 63-word Unit 1／Unit 2 coverage count. Its image is locally wired through the same explicit override map; it remains `review-ready`, not `pilot_accepted`.
