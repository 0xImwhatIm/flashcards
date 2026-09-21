# FlashCards Illustration Batch｜Wave 01 Spatial + Each Other

> Status: `wave-01 / 5 base images + 4 instructional overlays / tail-corrected review-ready / not wired`
>
> Date: 2026-09-20 (Asia/Taipei)

> Final selection update: the user selected the current `Each Other`, `Near`, `Behind`, `In Front Of` and `Inside` assets; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

> Instructional overlay rules: [`design/SPATIAL_INSTRUCTIONAL_OVERLAYS_V0.1.md`](SPATIAL_INSTRUCTIONAL_OVERLAYS_V0.1.md)

## Scope

This is the next bounded batch after the semantic pilot. It contains the corrected `Each other` candidate plus four remaining Unit 2 spatial words:

| Unit | Word | Asset |
|---:|---|---|
| 2 | Each other | corrected mutual-pointing candidate |
| 2 | Near | close side-by-side relationship |
| 2 | Behind | anchor behind a foreground box |
| 2 | In Front Of | anchor in front of a background signboard |
| 2 | Inside | anchor enclosed by an open container |

`Right` is intentionally deferred. Its intended sense (direction versus location) needs a separate semantic decision before it enters a production batch.

## Absolute character lock used for every image

- The green anchor is one continuous compact bean/gumdrop silhouette with a low visual center; no long neck or tall slender body.
- Exactly three small rounded back plates; no spikes or oversized plates.
- A low soft tail must remain visibly readable whenever the scene does not intentionally occlude it; a front-facing pose alone is not a reason to omit it.
- Short rounded arms with broad tips; no fingers, tapered tips or extra joints.
- Two short flat rounded feet; no toe lines.
- Two small black dot eyes and one short mouth arc; no cheeks, blush, eyebrows, teeth, highlights or extra facial marks.
- Anchor green remains in `#18B985`／`#13A97C`; fill is matte, with only subtle paper/pigment variation.
- Thick charcoal `#202223` contour with a gentle hand-drawn wobble.
- Opaque warm off-white `#F8F6F0` background, one ground line, no text or watermark.

## Scene prompts and result registry

The shared lock above is the invariant. Each asset adds only the following scene delta:

| ID | Scene delta | Output | Size / mode | SHA-256 | QA result |
|---|---|---|---|---|---|
| W01-EPT | Two characters face one another and point at each other simultaneously. Green anchor left; coral triceratops right. No props or arrows. | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-pointing-v3.png` | 1254×1254 RGB | `cb0dbca37f975f3535e8aca6a70a72a10208d55445ece94301b3597a597b8245` | `review-ready / semantic pass / character lock pass at 160 px` |
| W01-NEAR | Green anchor and small dusty-blue bird stand side by side with a narrow visible gap, close but not touching; the anchor tail is intentionally shown. | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/near-v2.png` | 1254×1254 RGB | `b793c7c09649f821daddd1834b6f6e28a35290d0022d8b722bc33602c81ddcab` | `review-ready / close relation and tail read at 160 px; v1 superseded for tail omission` |
| W01-BEH | Green anchor is behind one large foreground warm-tan box; head and upper body remain visible above/around it. | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/behind-v1.png` | 1254×1254 RGB | `c61bc79b85539448a98dbc17d467d5f01544622543efc2df91c729e0db4e092a` | `review-ready / depth relation reads at 160 px` |
| W01-FRONT | Green anchor stands fully in front of one muted blue-gray signboard, overlapping its lower middle; the low tail remains visible to the viewer’s right. | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/in-front-of-v2.png` | 1254×1254 RGB | `40d7ebb007a00c04b64a497a32a5c94bbff62963ae4fdc750a5ac304bd3b0a97` | `review-ready / foreground relation and tail read at 160 px; v1 superseded for tail omission` |
| W01-IN | Green anchor is visibly enclosed inside one open warm-tan container with a clear rim and interior. | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/inside-v1.png` | 1254×1254 RGB | `1ea2f6b3f257f1b6c1dfde18144a621acfb3b09eb3ca7816393a5f63922a8e7e` | `review-ready / enclosure reads at 160 px` |

## QA boundary

- All five files are separate prototypes; none replaces the official anchor or is wired into `index.html`. The superseded v1 files remain for audit history only.
- The images were checked at 1254 px and 160 px. The anchor silhouette, three back plates, rounded limbs, restrained face and opaque warm-paper background remain readable in this batch.
- `review-ready` is not the same as `pilot_accepted`: hidden-label learner recognition, final mobile card integration and cross-batch consistency remain open.
- If a future image violates the absolute lock, keep its semantic result but mark `character-consistency hold`; do not silently repair it by recoloring or cropping.

## Directional overlay decision

The four spatial base images remain clean. Do not permanently bake large arrows into them. When extra teaching scaffolding is needed, use the separate overlay layer defined in `design/SPATIAL_INSTRUCTIONAL_OVERLAYS_V0.1.md`:

- `Behind`: receding arrow partly hidden by the foreground object.
- `In Front Of`: short perspective arrow from the background object toward the foreground anchor.
- `Inside`: downward arrow ending inside the container.
- `Near`: two short inward-facing heads／a narrow distance bracket, not a long movement arrow.

### Produced overlay artifacts

All overlays are transparent, 1254×1254 SVG layers. They are deliberately not merged into the PNG base assets.

| Relation | Overlay file | SHA-256 |
|---|---|---|
| `Behind` | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlays/behind-depth.svg` | `1304b48750a46077bff870c1225e4017dc0beb9b64bbf70fb957ce702c1d70a9` |
| `In Front Of` | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlays/in-front-of-depth.svg` | `1839be8912fd6579df269148c9c91aef2a00132232632ed7517d676509cb9505` |
| `Inside` | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlays/inside-down.svg` | `8fc29eee3343a4624d7529baffbd81082056fafcff1ab0acc98fea8d1f8b8301` |
| `Near` | `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlays/near-gap.svg` | `c234ceafe6de376e8e81d6a34b3c2a9a9dc4f79eaa5e2e82b443a14ecc44ec9e` |

An HTML composed preview is available at `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlay-preview.html` (`b6a8449baae5109238d99596f06dbda2b68fdf80a974836fbaf80d6acf3abcc4`).

These are **position-directional** arrows: static, short, rounded and relation-focused. A future **movement-directional** arrow family must use a separate token/style set with motion trails, directional repetition or speed cues; it must not reuse these files.

## Next step

Blind-review these five files with the English labels hidden. If they pass, add accepted paths to the full Unit 1／Unit 2 manifest, then continue with the next semantic wave. Do not generate the remaining vocabulary in one unreviewed bulk run.
