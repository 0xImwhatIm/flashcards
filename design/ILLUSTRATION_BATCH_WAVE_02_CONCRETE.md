# FlashCards Illustration Batch｜Wave 02 Concrete Places & Objects

> Status: `review-ready / 5 generated + 1 approved House anchor / anchor-audited`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected all six current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Scope

This is the next vocabulary wave after the spatial batch. It stays with concrete Unit 2 place/object words so that character consistency can be checked across simple one-character scenes before adding more abstract traits and connectors.

| Unit | Word | Semantic scene |
|---:|---|---|
| 2 | House | approved user-provided House anchor: green mascot pointing beside a simple house |
| 2 | Living Room | green anchor in a minimal living room with a sofa and one lamp |
| 2 | Wall | green anchor beside a single freestanding wall panel |
| 2 | Kitchen | green anchor at a simple counter with one kitchen cue |
| 2 | Dining Room | green anchor at a table with two chairs and one plate |
| 2 | Sofa | green anchor sitting on a standalone sofa |

## Absolute character lock

Every image uses the same lock as `FLASHCARDS_VISUAL_INDEX.md` and Wave 01:

- compact integrated bean/gumdrop green anchor; no long neck or tall slender body;
- three small rounded back plates;
- short rounded arms, short flat feet, no fingers or toe lines;
- two dot eyes, one short mouth arc, no cheeks/blush/eyebrows/teeth/extra facial marks;
- anchor green `#18B985`／`#13A97C`, matte fill, charcoal `#202223` outline;
- opaque warm off-white `#F8F6F0` background, one ground line, subtle paper grain only;
- no text, logos, watermark, glossy 3D, neon color or crowded scenery.

## Prompt deltas

The shared absolute lock is the base prompt. Each scene adds only one semantic delta:

| ID | Prompt delta | Planned output |
|---|---|---|
| W02-HOUSE | `Approved user-provided semantic anchor: green mascot points beside one small warm cream house; retain the sparse paper background and no neighborhood.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/house-anchor.jpg` |
| W02-LIVING | `Show a minimal living room cue: one simple sofa, one small floor lamp and a small rug; the anchor stands in the room.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/living-room-v1.png` |
| W02-WALL | `Show one freestanding warm cream wall panel with the anchor standing beside it; one tiny framed blank shape is allowed only if needed for wall recognition.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/wall-v1.png` |
| W02-KITCHEN | `Show the anchor at one simple warm-wood counter with a small bowl and a single hanging utensil cue; no full kitchen clutter.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/kitchen-v1.png` |
| W02-DINING | `Show one small dining table, two simple chairs and one blank plate; the anchor stands or sits at the table.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/dining-room-v1.png` |
| W02-SOFA | `Show one standalone sofa as the dominant object with the anchor sitting on it; no complete room.` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/sofa-v1.png` |

## QA gates

- [x] Word meaning is inferable with the English label hidden in the visual review.
- [x] Anchor passes silhouette, face, plate, limb, color and background lock in the six-image pass.
- [x] Scene is readable at 160 px and has one focal object.
- [x] No image is wired into `index.html`; this batch remains an isolated review set.
- [x] `Living Room` and `Sofa` remain distinguishable: one is a room cue, one is the standalone object.

## Result registry

Generated with built-in ImageGen for the five scene prototypes. The House card now uses the user-provided semantic anchor JPEG; the previous generated `house-v1.png` remains preserved as a superseded candidate. All selected files are 1254 × 1254 px RGB images. `review-ready` is not `pilot_accepted`.

| ID | Status | Output | SHA-256 | 160 px / character review |
|---|---|---|---|---|
| W02-HOUSE | `approved semantic anchor` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/house-anchor.jpg` | `2e116e52ad6b468ca52ac25bdb019e5912ea13de3280c2c714228d974629a4d3` | Pass: user-selected House anchor; compact mascot, three rounded plates, simple face, pointing pose |
| W02-LIVING | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/living-room-v1.png` | `3d433a31f709a50fa6433ff93631b19c9b921950727ee7b09433ebfa09a9de8a` | Pass: sofa + lamp + rug read as room; anchor remains primary |
| W02-WALL | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/wall-v1.png` | `7d2b95b9c0e9323cc961c67c0064bbc60369c0fabbd545f198d82a719faa66f2` | Pass: freestanding wall panel is unmistakable; blank frame has no text |
| W02-KITCHEN | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/kitchen-v1.png` | `1a55a90511a4b95def77160f13d4ebf4cf3d4e8424e7901fcf57e76d6741b495` | Pass: counter + bowl + utensil read at thumbnail size; no dining cue |
| W02-DINING | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/dining-room-v1.png` | `5388ded309ac6619432b3919292e1edfc0e58a76deae9725e98161b2d4fc5fd0` | Pass: two chairs + table + plate; sparse v2 keeps mascot visible |
| W02-SOFA | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-02-concrete/sofa-v1.png` | `c23617672b34a57f213361c5aee7ecab557094e7bef85bc39ad7487f628442fe` | Pass: standalone sofa reads separately from Living Room |

### 160 px QA record

Thumbnail copies were rendered under `/tmp/flashcards-wave02-qa.WoCBa0/` plus `/tmp/flashcards-wave02-anchor-qa.1ujsqJ/` for the new House anchor and manually inspected. All six selected assets are opaque RGB images (five PNG prototypes plus the House JPEG); no readable text, logo or watermark was observed. The first room-heavy Dining Room attempt was discarded and replaced by the sparse two-chair/table version recorded above.

## 2026-09-20 anchor consistency audit

The attached House image is adopted as a **semantic House anchor**, not as a replacement for the global character anchor. It keeps the same mascot grammar—compact green bean body, three rounded back plates, dot eyes, short curved mouth, rounded limbs, charcoal hand-inked outline, warm paper field and one ground line—while adding a pointing pose and a slate-blue roof cue for `House`.

| Audit area | Finding across the current batch | Decision |
|---|---|---|
| Canvas, paper and line language | All six images use opaque warm off-white fields, charcoal contours and matte paper/pigment texture. Line weight varies slightly because of ImageGen, but no hard style break is present. | `PASS` |
| Mascot identity | All six retain the compact bean/gumdrop body, simple face and rounded back-plate grammar. Pose changes (standing, pointing, seated) are semantic variants, not new character designs. | `PASS` |
| Back plates and tail visibility | Three plates are readable in each selected image at full size; the tail is visible in the House anchor and partially occluded or suppressed by front-facing poses in several prototypes. This is a watch item, not a contradictory anatomy change. | `PASS / WATCH` |
| Green and supporting palette | The House anchor is slightly darker/less saturated than the generated prototypes; the others remain within the approved emerald/teal family with muted scene colors. | `PASS / MINOR SATURATION VARIANCE` |
| Semantic composition | House, Wall, Kitchen, Dining Room, Living Room and Sofa remain distinguishable at 160 px; Living Room uses the room cue, Sofa remains the standalone object. | `PASS` |

### Per-asset review disposition

- `House`: **approved semantic anchor**; use `house-anchor.jpg` for the House card. The former `house-v1.png` is superseded but retained for history.
- `Living Room`: **review-ready / style-consistent**, with the highest furniture/detail density and a larger mascot scale; keep as a scene prototype, not a new character reference.
- `Wall`: **review-ready / closest visual match** to the clean anchor grammar.
- `Kitchen`: **review-ready / style-consistent**, with a slightly brighter green and larger counter cue; no character anatomy break.
- `Dining Room`: **review-ready / sparse v2**, preserving mascot visibility and the same line/paper system.
- `Sofa`: **review-ready / seated pose variant**, with the sofa as the semantic focal object.

Conclusion: the batch has **no major character-style break**, but it is not pixel-identical to the new House anchor. Future generations should use the House anchor's darker green, more visibly tapered tail and slightly looser contour as the additional reference, while retaining the existing absolute lock.
