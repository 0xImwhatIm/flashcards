# FlashCards Illustration Batch｜Wave 11 Right (turn direction)

> Status: `generated / 1 Unit 2 word / 2 semantic candidates / review-ready / anchor-locked`
>
> Date: 2026-09-21 (Asia/Taipei)

> Final selection update: the user selected `right-v2-turn.png`; it is wired in `index.html`. The earlier static-location version remains historical. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Scope and decision

`Right` is currently approved in the Unit 2 sense **「右轉／turn right」**. It is not the correctness sense (`correct`), and it is no longer represented primarily as a static right-side location. The current candidate uses a familiar traffic-sign grammar: a blue-gray sign with a clear curved arrow turning to the viewer's right. The earlier static-location candidate remains preserved as historical evidence.

## Semantic grammar

- Place one quiet blue-gray traffic sign on a short pole and one large clean curved arrow turning right inside it.
- Place the canonical green mascot beside the sign, slightly oriented toward the right, on the same ground line.
- Keep the mascot and sign as the only semantic objects; do not add a road, cars or text.
- The sign arrow is a semantic prop, not a reusable UI overlay or motion trail.

## Generation record

Prompt intent: “Right” means turn right. Use the same compact green bean/gumdrop mascot, visible tail and three small rounded dorsal plates, beside a blue-gray roadside sign with one large clean mustard/white curved arrow pointing right. Warm off-white paper, thick wobbly charcoal contour, subtle pigment grain, one ground line, generous upper whitespace, no letters, words, road scene, cars or speed trails.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W11-RIGHT-V1 | `assets/visual-prototypes/batch-v0.2/wave-11-right-spatial/right-v1.png` | `0f775e6524f501b7920f72f7c18946249980cb1519ab52ec6f759c1071f8a761` | `historical / superseded` | Earlier static viewer-right location candidate; retained for audit history after the learner-facing sense was clarified as turn-right. |
| W11-RIGHT-V2 | `assets/visual-prototypes/batch-v0.2/wave-11-right-spatial/right-v2-turn.png` | `c54fc16aa68a5f9f72e4996a30d49dc38fe2fbd56b895a4d628bffc42441671d` | `generated / review-ready` | Semantic pass: familiar traffic sign and right-bending arrow communicate turn right without text or correctness symbols. Character pass: compact bean silhouette, visible low tail, three rounded plates, dot eyes, short mouth, warm-paper field and charcoal contour; 160 px thumbnail created. |

## QA gates

- [x] 1254 × 1254 RGB PNG with opaque warm-paper background.
- [x] 160 × 160 QA thumbnail created.
- [x] Tail and three rounded plates remain readable.
- [x] Sign contains one static semantic right-turn arrow; no speed trails, text, logo, watermark or right/wrong symbol.
- [x] Semantic and character checks recorded separately.
- [ ] Hidden-label learner recognition and mobile integration review.
- [ ] Not wired into `index.html`; remains `review-ready` until acceptance.

## Next order

Review `right-v2-turn.png` beside the House anchor and the Wave 10 candidates. If the turn-right reading remains clear at hidden-label and 160 px review, it can enter a separately authorized integration pass. A future correctness sense for `Right` must be planned as a separate semantic asset, not silently merged with this one.
