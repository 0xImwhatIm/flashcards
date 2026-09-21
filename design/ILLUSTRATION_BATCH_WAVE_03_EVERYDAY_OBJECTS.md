# FlashCards Illustration Batch｜Wave 03 Everyday Objects

> Status: `review-ready / 6 generated / anchor-locked`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected all six current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Scope

This is the next bounded wave after the spatial overlays and Wave 02 place/object scenes. It covers concrete, label-hidden objects that can be recognized from one clear action or one object silhouette. Abstract states (`Hungry`, `Maybe`, `Favorite`, `Special`) and relationship animals (`Mice`) remain for later semantic waves.

| Unit | Word | Semantic scene |
|---:|---|---|
| 2 | Notebook | green anchor writing in one open notebook |
| 2 | Marker | green anchor holding one thick marker over a blank card |
| 2 | Brush | green anchor painting with one brush and a tiny blank paper |
| 2 | Pencil Case | green anchor beside one zipped pencil case with two pencils peeking out |
| 2 | Cookie | green anchor holding one round cookie on a small plate |
| 2 | Gift | green anchor presenting one small wrapped gift |

## Absolute character lock

Every image uses the shared lock from `FLASHCARDS_VISUAL_INDEX.md`, including the House semantic anchor's preferred cues:

- compact integrated bean/gumdrop green body; no long neck or tall slender anatomy;
- three small rounded back plates and a low, soft tail when the pose permits;
- short rounded arms and short flat rounded feet; no fingers or toe lines;
- two small black dot eyes and one short mouth arc; no cheeks, blush, eyebrows, teeth, pupils or extra facial marks;
- anchor green in the darker emerald/teal family `#18B985`／`#13A97C`, matte fill, charcoal `#202223` contour;
- opaque warm off-white `#F8F6F0` background, one ground line, subtle paper grain;
- no text, letters, numbers, logos, watermark, glossy 3D, neon colors or crowded scenery.

## Prompt deltas

The shared absolute lock is the base prompt. Each scene adds one semantic delta only:

| ID | Prompt delta | Planned output |
|---|---|---|
| W03-NOTEBOOK | `Place one open blank notebook in front of the anchor; the anchor writes with one short pencil. No readable marks.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/notebook-v1.png` |
| W03-MARKER | `Show the anchor holding one chunky marker above a blank card; marker cap and body make the object unmistakable. No writing.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/marker-v1.png` |
| W03-BRUSH | `Show the anchor holding one paintbrush beside a tiny blank paper with one simple color dab. No letters or detailed classroom.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/brush-v1.png` |
| W03-PENCIL-CASE | `Show one standalone soft rectangular zipped pencil case beside the anchor, with two short pencils peeking out. No desk clutter.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/pencil-case-v1.png` |
| W03-COOKIE | `Show the anchor holding one round chocolate-chip cookie on a small blank plate. One cookie only; no kitchen scene.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/cookie-v1.png` |
| W03-GIFT | `Show the anchor presenting one small wrapped gift with a simple ribbon. No text, card or extra characters.` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/gift-v1.png` |

## QA gates

- [x] Word meaning is inferable with the English label hidden in the visual review.
- [x] Anchor passes silhouette, face, plate, limb, tail, color and background lock in the six-image pass.
- [x] Scene is readable at 160 px and has one focal object.
- [x] No readable marks leak into Notebook, Marker or Brush.
- [x] No image is wired into `index.html`; this batch remains an isolated review set.

## Result registry

Generated with built-in ImageGen, one asset per prompt, using the shared FlashCards anchor lock. All six selected outputs are 1254 × 1254 px RGB PNGs. `review-ready` is not `pilot_accepted`.

| ID | Status | Output | SHA-256 | 160 px / character review |
|---|---|---|---|---|
| W03-NOTEBOOK | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/notebook-v1.png` | `02de269cac8527780b3a59f412a15641ee43751250f4cf5f454b7c2162e4bd4f` | Pass: open blank notebook and writing pose remain legible; no readable marks |
| W03-MARKER | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/marker-v1.png` | `ed12a322099cd5ebb0c31bcd5111f0a9c8bc16a1539304039e688b6eb57d01f1` | Pass: capped chunky marker is distinct from pencil; blank card has no text |
| W03-BRUSH | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/brush-v1.png` | `3963d3edb0c99c78fea01da2c7b8609940b9e2627ea54038fb99a2649488c8f4` | Pass: bristle tip and one muted paint dab read at thumbnail size |
| W03-PENCIL-CASE | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/pencil-case-v1.png` | `0c909fe8e225292eeb5bdc6b796ce810ab981056274b17093af4dfcef116df5f` | Pass: zipper, soft case silhouette and two pencils are clear |
| W03-COOKIE | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/cookie-v1.png` | `d221438197d9691383442b6e3bb425d1df21e25a82ff6f8bf2822386182bcc56` | Pass: exactly one cookie on one plate; no extra food |
| W03-GIFT | `generated / review-ready` | `assets/visual-prototypes/batch-v0.2/wave-03-everyday-objects/gift-v1.png` | `bf076d764c62dc7c70d98448511f49e44cc744ba44f67a54ae412ecaf536f333` | Pass: one wrapped gift and ribbon read clearly; no extra characters |

### 160 px QA record

Thumbnail copies were rendered under `/tmp/flashcards-wave03-qa.3z0g9N/` and manually inspected. All six selected assets are opaque RGB PNGs; no readable text, logo or watermark was observed. The mascot keeps three rounded back plates and a low soft tail in every selected frame. `review-ready` remains a review state, not production acceptance.
