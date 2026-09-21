# FlashCards Illustration Batch｜Wave 04 Home & Social Context

> Status: `generated / 5 Unit 2 words / review-ready / anchor-locked`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected all five current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Scope

This is the next preparation wave after the spatial overlays, Wave 02 places and Wave 03 everyday objects. It combines the three remaining concrete home words with two already-approved social/animal semantic directions so the next generation pass tests both quiet single-subject scenes and controlled multi-character scenes.

`Hungry`, `Maybe`, `Purple`, `Gray`, `Brown`, `Color`, `Favorite`, `Special`, `But` and the ambiguous `Right` remain deferred to later state/trait/connector decisions. `Right` stays explicitly deferred until its intended direction-versus-correctness sense is decided.

| Unit | Word | Cast | Semantic scene |
|---:|---|---:|---|
| 2 | Bathroom | 1 | green anchor in a minimal bathroom cue: sink, mirror and towel |
| 2 | Table | 1 | green anchor beside one standalone table, no dining-room setting |
| 2 | Bedroom | 1 | green anchor beside one bed, pillow and small lamp |
| 2 | Parents | 3 | exactly two adult-sized roles protecting one child-sized role |
| 2 | Mice | 3 | green anchor observing two small gray mice; no extra animal crowd |

## Absolute character lock

Every image uses the shared lock from `FLASHCARDS_VISUAL_INDEX.md` and the approved House semantic anchor:

- compact integrated bean/gumdrop green body; no long neck or tall slender anatomy;
- three small rounded back plates and a low, soft tail when the pose permits;
- short rounded arms and short flat rounded feet; no fingers or toe lines;
- two small black dot eyes and one short mouth arc; no cheeks, blush, eyebrows, teeth, pupils or extra facial marks;
- anchor green `#18B985`／`#13A97C`, matte fill, charcoal `#202223` contour;
- opaque warm off-white `#F8F6F0` background, one ground line, subtle paper grain;
- no text, letters, numbers, logos, watermark, glossy 3D, neon colors or crowded scenery.

### Multi-character constraints

- `Parents`: exactly two larger adult-sized characters plus one smaller child-sized primary character; use a protective triangle gesture, not a generic group portrait. Supporting roles may use one restrained muted accessory each.
- `Mice`: exactly two small gray mice plus the green anchor; each mouse gets one simple species cue (rounded ears and thin tail), with the same charcoal line and paper texture. No cat, cheese pile or crowd.

## Prompt deltas

The shared absolute lock is the base prompt. Each scene adds one semantic delta only:

| ID | Prompt delta | Planned output |
|---|---|---|
| W04-BATHROOM | `Show a minimal bathroom cue: one small sink, one rounded mirror and one hanging towel; no toilet detail, shower clutter or bedroom furniture.` | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/bathroom-v1.png` |
| W04-TABLE | `Show one standalone simple table with four rounded legs and the anchor beside it; no chairs, plate, sofa or room context.` | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/table-v1.png` |
| W04-BEDROOM | `Show one simple bed with a pillow and one small bedside lamp; no sofa, dining table or full bedroom clutter.` | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/bedroom-v1.png` |
| W04-PARENTS | `Show exactly two larger adult-sized mascots gently protecting or guiding one smaller child-sized mascot; no extra people and no readable family labels.` | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/parents-v1.png` |
| W04-MICE | `Show the green anchor observing exactly two small gray mice standing nearby; no other animals, no mouse labels and no crowded props.` | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/mice-v1.png` |

## QA gates after generation

- [x] Prompt set preserves the House anchor's darker green, tail cue and loose charcoal contour.
- [x] Bathroom / Table / Bedroom remain distinct at 160 px without room clutter.
- [x] `Parents` is exactly two adults plus one child, not `Family`.
- [x] `Mice` reads as plural through exactly two supporting mice, not a generic animal crowd.
- [ ] No image is wired into `index.html` until hidden-label and cross-wave review.

## Result registry

Generation mode: built-in ImageGen, one prompt per asset. All five outputs are 1254×1254 RGB PNGs and have been checked at 160 px. `review-ready` is not `pilot_accepted`.

| ID | Asset | SHA-256 | Status | Semantic / character QA |
|---|---|---|---|---|
| W04-BATHROOM | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/bathroom-v1.png` | `fbdf41d3e1d74182e264d42b200d3b00731f1582c123d0a3acddb35436752350` | `generated / review-ready` | Pass: sink, mirror and towel make Bathroom clear; anchor proportions, three plates, dot eyes and single-color body hold. |
| W04-TABLE | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/table-v1.png` | `2910eb5a83b6ff8c61e5ec2614def9b9dcf17071552c43f4532afa42ee7b4d03` | `generated / review-ready` | Pass: one standalone table is unmistakable; no room clutter; anchor lock holds. |
| W04-BEDROOM | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/bedroom-v1.png` | `17d419d1b447ad90aba2b01d08727a165a0b5e481a0fd4d9a07667b529114577` | `generated / review-ready` | Pass: bed, pillow and lamp read as Bedroom; dot-eye correction applied before acceptance. |
| W04-PARENTS | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/parents-v1.png` | `38c19b15497b0dd58a680634f7b3eb91ed4ac5872dc0be35ecd29ef8055b9999` | `generated / review-ready` | Pass: exactly two larger adults plus one smaller child; green anchor and coral triceratops remain in the same visual grammar. |
| W04-MICE | `assets/visual-prototypes/batch-v0.2/wave-04-home-social/mice-v1.png` | `8a40a1518c41b0733a86df011689bece1edd9545cc887efb9c108d231bd8ab96` | `generated / review-ready` | Pass: exactly two gray mice beside the green anchor; opaque warm-paper background and no extra animal crowd. |

These are review-ready prototypes only. No `index.html` wiring or production replacement has been performed.
