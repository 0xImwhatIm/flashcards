# FlashCards Illustration Batch｜Wave 10 Traits & Expressions Plan

> Status: `Wave 10A + Wave 10B user-selected / 7 Unit 1 assets wired / Really? + Very semantic revision selected`
>
> Date: 2026-09-21 (Asia/Taipei)

## Scope

After Wave 09, the remaining Unit 1 words without an image/prototype were:

`Really`, `Handsome`, `Very`, `Beautiful`; all four are now generated as Wave 10B candidates.

`Right` is tracked separately in `ILLUSTRATION_BATCH_WAVE_11_RIGHT_SPATIAL.md`; its current approved sense is turn-right direction, not static location or correctness.

These words should not be generated as one undifferentiated batch. The three Wave 10A candidates have concrete identity/state anchors; the four Wave 10B words need an explicit semantic review because a standalone card can easily become subjective, generic or context-dependent.

## Recommended two-step production order

### Wave 10A｜Concrete identity/state proof

Generate first:

| Word | Proposed visual grammar | Main risk to review | Output |
|---|---|---|---|
| `Woman` | One adult anchor mascot in a neutral portrait-like stance, with one restrained scene-specific coral scarf or flower cue and no relationship, job or home prop. | Avoid collapsing into `Wife`, `Aunt` or `Housewife`; avoid relying on stereotypes. | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/woman-v1.png` |
| `Young` | A highlighted young mascot beside one older grandpa-like mascot using the same grammar; one short static pointer arrow identifies the younger subject. | Avoid collapsing into `Baby`, `Daughter`, `Years Old` or `Old`; age cue must remain a comparison, not a family story. | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/young-v4.png` |
| `New` | One mascot presents a freshly sprouted small plant with one mustard freshness sparkle; no gift bow, price tag or text. | Avoid collapsing into `Gift`, `Special` or `Colorful`; the untouched/new state must be the focus. | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/new-v1.png` |

Shared Wave 10A prompt constraints:

- use the canonical compact green mascot, visible tail and three rounded plates;
- warm off-white opaque paper field, thick charcoal contour and restrained pigment grain;
- no text, letters, digits, logos, watermark or speech bubble;
- one semantic focus, no unrelated characters, no permanent gender costume; if an approved gendered word needs a cue, use at most one small lipstick, blush or simplified-eyelash mark under the Visual Index exception;
- mark `Woman`, `Young` and `New` as requiring blind learner review before production acceptance.

### Wave 10B｜Abstract modifier and appearance proof

Wave 10B is now generated as a review batch; acceptance remains gated:

| Word | Proposed visual grammar | Main risk to review | Output |
|---|---|---|---|
| `Really` | `Really? = 真的嗎？`：主角歪頭、停住一隻手，直視另一個角色提出的簡單物件／主張；以互動姿勢表達確認與質疑，不烘焙文字。 | 若沒有眼神與「先停一下」的姿勢，容易讀成 `Special`、`Yes` 或單純驚訝。 | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/really-v2.png`（`really-v1.png` 保留為歷史候選） |
| `Very` | 借用使用者提供的梗圖「張嘴、反應極強烈」的姿勢能量，轉成單一綠色恐龍的誇張高強度反應，表示程度非常高；不複製貓或原背景。 | 可能被讀成單純 `Surprised`；需以 blind-label 確認是否能與 `Big`／`Tall` 或情緒詞區分。 | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/very-v2.png`（`very-v1.png` 保留為歷史候選） |
| `Handsome` | One adult masculine-coded anchor portrait with a small mirror, muted bow tie and restrained grooming cue, no partner or romantic scene. | Subjectivity and stereotype risk; must not become `Police Officer`, `Husband` or `Beautiful`. | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/handsome-v1.png` |
| `Beautiful` | One adult/friendly anchor portrait admiring one harmonious flower arrangement, with one small sparkle and one approved muted-coral lip cue. | Subjectivity and overlap with `Colorful`, `Special` or `Handsome`; avoid beauty-score or glamour language. | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/beautiful-v1.png` |

Wave 10B acceptance rule: if a hidden-label review cannot distinguish the intended word from a nearby adjective or emotional state, keep the prototype as `semantic hold` and do not wire it into the app.

## Current execution｜Woman

`Woman` is the first scheduled Wave 10A candidate and is stored as a review-ready prototype, not a production replacement. The image uses one adult-coded anchor mascot, one restrained muted-coral scarf cue, no relationship/job/home prop, and no text. The coral cue is scene-specific and does not change the canonical mascot anatomy.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W10A-WOMAN | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/woman-v1.png` | `942ac18299b60ae1b01ccb00ecaf995ad4e4e8e07399d449a21afa6087c5aa88` | `generated / review-ready` | Semantic pass: adult identity is presented without a relationship, job or home scene. Character pass: compact bean silhouette, visible low tail, three rounded plates, dot eyes, short mouth, charcoal contour and warm-paper field read at 160 px. Blind learner review remains required; not wired into `index.html`. |

### Wave 10A-02 execution｜Young + New

`Young` and `New` are now generated as review-ready candidates. `Young` uses `young-v4.png`, a comparison scene with a highlighted young mascot, one older grandpa-like mascot, and a single static pointer arrow. Earlier solo backpack versions (`young-v1.png` through `young-v3.png`) remain preserved audit history. `New` uses a single fresh sprout scene rather than a gift-like box, keeping it distinct from `Gift`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W10A-YOUNG | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/young-v4.png` | `85e2982fcc054b7eeb233a172e6ccb99c0db954f4a5fe9f8f0ac0d834ec09f39` | `generated / review-ready` | Semantic pass: one mustard pointer arrow identifies the younger of two same-grammar dinosaurs; the older companion uses a small rounded beard and cane. Character pass: both retain visible tails and three plates; 160 px comparison reads. `young-v1.png` through `young-v3.png` remain unselected audit history. |
| W10A-NEW | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/new-v1.png` | `b4a68b9ea67b0eaec041ab8f6f6dfce76be004e13e3fcc007804778047d0048b` | `generated / review-ready` | Semantic pass: one fresh sprout plus one mustard sparkle communicates new without a bow, price tag or text. Character pass: tail and three rounded plates visible; 160 px thumbnail created. |

Both candidates remain below `pilot_accepted` until hidden-label learner recognition and side-by-side anchor review pass.

### Wave 10B execution｜Really + Very + Handsome + Beautiful

The four remaining Unit 1 words are now generated as review-ready prototypes. The first `Really` attempt was rejected because it reproduced the house scene and had a dark/transparent background; `really-v1.png` was the clean replacement before the semantic clarification. On 2026-09-21, the teaching meaning was narrowed to `Really? = 真的嗎？`, so `really-v2.png` now uses a two-character verification posture. `Very` was also revised from a flower comparison to a meme-inspired (pose only) high-intensity reaction, producing `very-v2.png`; the supplied cat image is not copied. The earlier v1 files remain preserved for comparison. All four remain below `pilot_accepted` until hidden-label recognition and anchor review pass.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W10B-REALLY-V2 | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/really-v2.png` | `13155573ed4c4438442574e91a4ec17353e3222dd40fdf678d9654d0ceeec720` | `generated / review-ready` | Semantic pass: `Really?` is shown by green mascot's head tilt, raised stop/verification hand, eye contact, and a blue companion presenting a neutral object; no text or question mark. Character pass: green mascot has visible tail and three readable plates at full size and 160 px; the blue companion is a semantically necessary supporting character. |
| W10B-VERY-V2 | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/very-v2.png` | `fb6bdac5ed8e216d2c95c9b6d4dde996cacddbb4e43e9c10826a5f661c245323` | `generated / review-ready` | Semantic pass: one mascot's open-mouth, arms-up reaction and restrained mustard strokes signal an extremely high degree; pose energy is adapted from the user's meme reference without copying the cat or scene. Character pass: tail and three rounded plates remain visible at full size and 160 px. |
| W10B-REALLY-V1-HISTORY | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/really-v1.png` | `c878c6fb38e49e4401a04348237a8aba6dff752e342454a6026f0d7aae1652bc` | `historical / superseded` | Previous emphatic-confirmation candidate; retained for audit and comparison only. |
| W10B-VERY-V1-HISTORY | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/very-v1.png` | `1fc76a80250b57a9a0eab7d8edc4e732a84369a503e83ccd6eaadb28a602de3a` | `historical / superseded` | Previous tall-flower degree candidate; retained for audit and comparison only. |
| W10B-HANDSOME | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/handsome-v1.png` | `0b3c55b73d6d39f7e78d5b551100840a0dfb0fd6ca3f6306bf61219ac2a8810c` | `generated / review-ready` | Semantic pass: mirror, grooming comb and one muted bow tie suggest groomed masculine-coded appearance without romance/job. Character pass: reflection is a mirror duplicate, tail and three plates visible; 160 px thumbnail created. |
| W10B-BEAUTIFUL | `assets/visual-prototypes/batch-v0.2/wave-10-traits-expressions/beautiful-v1.png` | `f290a06071b83fd3886f8e2918f01422b8a61d3f1f71cdf418a2765abea9f8e1` | `generated / review-ready` | Semantic pass: harmonious flower arrangement, one sparkle and one tiny muted-coral lip cue; no glamour scene. Character pass: tail and three plates visible; 160 px thumbnail created. |

Shared gate: preserve the visible tail and three rounded plates, use the warm-paper field and one clear semantic focus, export 1254×1254 RGB PNG plus 160 px QA thumbnails, and keep all four `review-ready` until hidden-label recognition.

### Next phase after Wave 10B

The user selected all seven Wave 10 assets. The next step is app-level smoke QA with the selected image map; do not replace or delete the preserved v1 history for `Really`／`Very`.

## Anchor and QA gates for Wave 10

- [x] Re-read `design/FLASHCARDS_VISUAL_INDEX.md` before generation.
- [x] Every generated candidate is a 1254×1254 RGB PNG with an opaque warm-paper background.
- [x] 160 px thumbnails remain readable for the current review pass.
- [x] Tail and three rounded back plates are visible unless an intentional semantic occlusion is documented.
- [x] Semantic QA and character-consistency QA are recorded separately; final acceptance remains open.
- [ ] No generated asset is wired into `index.html` until hidden-label review passes.
- [x] `Right` is generated separately as a turn-right traffic-sign candidate; it is not part of Wave 10.

## Generation-ready prompt skeleton

```text
Use case: illustration-story.
Asset type: FlashCards vocabulary prototype, square 1254x1254 illustration.
Use the same compact emerald/teal bean/gumdrop mascot as the FlashCards anchor: low visual center, three small rounded back plates, low soft tail, short rounded limbs, flat feet, two black dot eyes and one short mouth arc.
Entire canvas filled with opaque warm off-white paper (#F8F6F0), generous upper negative space, one thin ground line, thick slightly wobbly charcoal contour, restrained matte pigment grain and low-saturation natural colors.
One semantic focus, readable at 160 px. No text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, eyebrows, teeth, eye highlights or transparent background; only an explicitly approved single gender cue may override the default no-blush/no-cosmetics rule.
Primary word grammar: <insert one approved word-specific construction here>.
```

## Decision checkpoint before ImageGen

`Woman`, `Young`, `New`, `Really v2`, `Very v2`, `Handsome` and `Beautiful` were selected by the user and wired into `index.html`. `Really v1` and `Very v1` remain preserved history. `Right` is recorded in the separate Wave 11 spatial plan as the selected turn-right asset; its earlier static-location candidate remains historical.
