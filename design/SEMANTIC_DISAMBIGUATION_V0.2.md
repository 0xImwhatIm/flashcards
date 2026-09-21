# FlashCards Semantic Disambiguation & Character Diversity｜v0.2

> Status: `concept revision / 8 comparison prototypes generated; v3 correction review-ready`
>
> Date: 2026-09-20 (Asia/Taipei)

> Related production wave: `design/ILLUSTRATION_BATCH_WAVE_01_SPATIAL.md`

## 1. This revision

The v0.1 pilot proved that the anchor mascot can survive 1-, 2- and 3-character scenes. The next problem is not color; it is **semantic separation**. Similar relationship words need different visual grammars, and the character world needs enough variety that a second character does not look like a cloned family member every time.

The user's six reference images are treated as concept references for diversity, species variety and relationship staging only. The original green dinosaur anchor remains the primary visual source of truth. Text, watermark, background color and unrelated rendering styles from those references are not copied into production assets.

## 2. Character system v0.2

### 2.1 Three role tiers

| Tier | Role | Examples | Constraint |
|---|---|---|---|
| A | Anchor hero | green long-bodied dinosaur from the official anchor | Stable silhouette, face, line weight and emerald/teal identity |
| B | Recurring companion species | triceratops, ankylosaurus, small bird, small mammal | Same naive hand-drawn grammar; one iconic silhouette trait; muted supporting color |
| C | Context role | human child, teacher, parent, animal friend | Only when the word needs that identity; do not become a second brand system |

The mascot is therefore a **world grammar**, not a single-species restriction. The anchor hero should remain present when it helps continuity, but a meaningful scene may use a triceratops, another dinosaur, a bird, a small mammal or a human-like role.

### 2.2 Companion species rules

- Use one iconic shape cue per species: triceratops horns, ankylosaurus club tail, small bird beak, mammal ears, or a human-sized silhouette.
- Keep the same thick near-black hand-drawn contour, dot eyes, small mouth, flat color fields and warm-paper staging.
- Supporting species may use muted sage, blue-gray, pink, ochre or coral; the anchor green remains the strongest brand color when present.
- Do not make every supporting role a recolored copy of the anchor. Different species should explain a relationship, age, role or action.
- Keep the semantic cast intentional: normally 1–3 characters; `Family` may use 4–5 because group membership is the word itself.
- Avoid a random zoo. Every extra character must answer “why is this character necessary to understand this word?”

## 3. Semantic separation rules

### 3.1 Family vs Parents

| Word | Canonical scene | Distinguishing cue | Avoid |
|---|---|---|---|
| `Parents` | exactly two adult-sized roles + one child-sized role | two adults visibly protect, guide or present something to the child; triangle composition | four-person crowd, siblings only, generic group portrait |
| `Family` | 4–5 members, at least two generations or visibly varied roles/species | broad group belonging: shared table, home portrait, picnic, group activity; no single couple-child triangle | only two adults + one child, which reads as parents |

`Parents` is a **relationship role**. `Family` is a **larger belonging group**. Species diversity is especially useful for `Family`, while scale and protective gesture are more important for `Parents`.

### 3.2 Between

The visual minimum is: **two stable anchors + one central subject occupying the middle gap**.

Two variants should be tested:

- `Between / clean`: two clearly different objects or characters on the left and right, central mascot exactly between them, no annotation.
- `Between / instructional`: the same composition plus two small numerals (`1`, `2`) above the side anchors and a thin double-ended bracket or inward guide lines. Numerals and arrows are a controlled teaching exception for spatial words, not general illustration decoration.

The annotation must clarify the relation, not create a sequence puzzle. No `3`, no sentence, no label, no arrow that suggests movement rather than position.

### 3.3 Each other

The previous “one character sends a letter to another” is not sufficient. It reads as `send`, `give`, or `mail` because the action is one-way.

Accepted semantic grammar:

1. Two characters face one another.
2. The action occurs in both directions at the same time.
3. The clearest child-tested cue is **both characters pointing at each other simultaneously**; use mirrored rounded-arm gestures with no prop required.
4. Matching-object exchange or two curved arrows forming a loop remain valid secondary grammars when a sentence needs those actions, but they are not the default.
5. Avoid a teacher/student hierarchy and avoid one character merely receiving.

Good candidates: mirrored pointing, exchanging matching cards, passing a ball simultaneously, mirrored high-five with two curved reciprocal motion marks, or two characters helping lift the same object. The strongest current candidate is **two different species pointing at each other at the same time**.

## 4. Reference-image interpretation

| Reference | Useful lesson | Not imported |
|---|---|---|
| Green dinosaur holding a small brown animal | scale and inter-species tenderness can explain relationship | pink background, exact character design |
| Quote card with pink/green characters | color contrast and a companion can create emotional pairing | all text, watermark, quote-card format |
| Kitchen scene with triceratops and other animals | species variety and prop-based semantic staging | busy perspective, saturated background, exact characters |
| Multi-species room scene | group interaction and role variety | crowded composition and unrelated props |
| Family photo / framed group | family can be a broad group rather than a nuclear triangle | speech bubble, text, photo frame, exact characters |
| Blue creature with drink | a supporting species can carry a distinct silhouette | exact creature, gray background, copied pose |

## 5. v0.2 comparison set

| ID | Word | Variant | Cast | Planned file | Decision question |
|---|---|---|---:|---|---|
| S02-FAM | Family | diverse group portrait | 5 | `assets/visual-prototypes/semantic-v0.2/family-parents/family-v2.png` | Does this read broader than parents? |
| S02-PAR | Parents | two adults protecting one child | 3 | `assets/visual-prototypes/semantic-v0.2/family-parents/parents-v2.png` | Does the narrow definition read immediately? |
| S02-BTC | Between | clean spatial staging | 1 + 2 anchors | `assets/visual-prototypes/semantic-v0.2/between/between-clean-v2.png` | Is the relation clear without annotation? |
| S02-BTA | Between | numerals + restrained guide lines | 1 + 2 anchors | `assets/visual-prototypes/semantic-v0.2/between/between-annotated-v2.png` | Does annotation improve clarity without clutter? |
| S02-EOL | Each Other | reciprocal loop exchange | 2 | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-loop-v2.png` | Does two-way action read as mutual? |
| S02-EHF | Each Other | mirrored helping action | 2 | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-help-v2.png` | Is mutual help clearer than exchange? |
| S02-EPT | Each Other | mirrored mutual pointing | 2 | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-pointing-v2.png` | Does the child-facing cue read immediately? |
| S02-EPT3 | Each Other | corrected mutual pointing with anchor lock | 2 | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-pointing-v3.png` | Does the semantic pass survive the character lock? |

## 6. Shared v0.2 generation invariant

```text
Use case: illustration-story
Asset type: square FlashCards semantic illustration prototype
Input images: Image 1 is the official green dinosaur anchor and has highest priority. Any other supplied image is concept reference for species diversity only; do not copy its text, watermark, background, composition or exact characters.
Scene/backdrop: warm off-white paper background, one thin hand-drawn ground line, simple semantic props only, generous upper negative space.
Subject: use the exact cast count requested by the scene. Keep the anchor mascot grammar for the primary role; supporting species may be triceratops, ankylosaurus, bird, small mammal or human-like context role with one iconic silhouette cue.
Style/medium: naive children's editorial illustration; thick charcoal-black hand-drawn outline with slight natural wobble; flat matte low-saturation color fields; subtle paper/pigment variation; no glossy 3D rendering.
Composition/framing: 1:1 square, full cast visible, one primary focal point, lower-half grouping, readable at 160 px.
Lighting/mood: soft diffuse daylight; warm, friendly, calm and semantically clear.
Constraints: every character and prop must serve the target word; no watermark; no copied text; no decorative crowd.
Avoid: cloned recolored mascots, unrelated species, competing focal points, crowded scenery, perfect vector geometry, anime features, realistic anatomy, neon colors, glossy effects.
```

## 7. Generation prompts and result registry

The eight assets below were generated as one controlled comparison batch plus two child-directed revisions. The shared invariant above is the base prompt; each scene adds only the following semantic delta. This keeps the comparison about meaning, cast and staging rather than accidental style drift.

| ID | Scene delta / prompt addition | Output | Size | SHA-256 | Review result |
|---|---|---|---:|---|---|
| S02-FAM | `Show five family members: green anchor, large orange triceratops adult, blue-gray bird, brown small mammal and olive ankylosaurus. Gather them around a shared fruit picnic with mixed sizes and at least two generations; no couple-child triangle.` | `assets/visual-prototypes/semantic-v0.2/family-parents/family-v2.png` | 1254×1254 | `cd295196feb70f22738eba288b1c7168c13a91fb6f3b5c65cbee5b93002f4738` | `review-ready / strong separation` |
| S02-PAR | `Show exactly three roles: two adult-sized parents (green anchor and orange triceratops) standing protectively with one small pale-blue child between them at a doorway; use a clear adult-child scale relationship.` | `assets/visual-prototypes/semantic-v0.2/family-parents/parents-v2.png` | 1254×1254 | `8c96c31733c6b2e0c53d19c363f6f06325c8a1cf51f27a95f9ac7b97b1b0c485` | `review-ready / strong narrow definition` |
| S02-BTC | `Place the green anchor exactly between two stable, distinct side anchors: a blue-gray flag on the left and a tan flag on the right. Use a single ground line and no annotation.` | `assets/visual-prototypes/semantic-v0.2/between/between-clean-v2.png` | 1254×1254 | `fb06540f8f48bd67785380ba2581bc008f38eed7e11aba797f027cf8fc1a1c36` | `review-ready / clear without annotation` |
| S02-BTA | `Repeat the Between composition, adding only a small yellow numeral 1 above the left anchor, numeral 2 above the right anchor, and a thin double-ended bracket/inward guide line showing the middle gap. No prose or 3.` | `assets/visual-prototypes/semantic-v0.2/between/between-annotated-v2.png` | 1254×1254 | `4119ce6a420777bd372764b88be92b9c88f40543dd2e89982d3d983019dba3c1` | `review-ready / controlled instructional exception` |
| S02-EOL | `Show two different species facing one another, green anchor and terracotta triceratops, each holding one matching blank card. Add two opposite curved mustard arrows forming a visible loop; both characters act at the same time.` | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-loop-v2.png` | 1254×1254 | `2445b20540a42ef34937e763317bdcdbba992541aa7605800899e597118f3a63` | `review-ready / strongest Each other candidate` |
| S02-EHF | `Show the green anchor and a blue-gray bird lifting the same small table together, mirrored effort marks on both sides and equal participation; no leader or receiver.` | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-help-v2.png` | 1254×1254 | `72892e5a9eb9216e66bc5f263e25d0aba4834a088d16e28adac1d90a0562a1ef` | `review-ready / mutual action, but may read as help` |
| S02-EPT | `Show exactly two different species facing one another: the green anchor on the left and a warm coral-orange triceratops on the right. Each extends one rounded arm directly toward the other at the same time; both gaze at one another. No objects, arrows or labels; the mirrored gestures must read as “point at each other.”` | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-pointing-v2.png` | 1254×1254 | `9e509ddf99982adb1b1da0520ce0bb375205c4c1e5ba012213fe72c84ba0f60e` | `semantic pass / character-consistency hold` |
| S02-EPT3 | `Keep the same mutual-pointing scene, but enforce the absolute anchor lock: compact integrated green bean silhouette, three small rounded back plates, short rounded arms with broad tips, flat feet with no toe lines, no cheek marks or blush, #18B985/#13A97C green, opaque #F8F6F0 paper background, and the same restrained charcoal outline.` | `assets/visual-prototypes/semantic-v0.2/each-other/each-other-pointing-v3.png` | 1254×1254 | `cb0dbca37f975f3535e8aca6a70a72a10208d55445ece94301b3597a597b8245` | `review-ready / semantic pass / character lock pass at 160 px` |

### Batch decision

- `Family` now has a clearly wider cast than `Parents`; the five-character version is the better semantic direction, subject to a later busy-composition check at card size.
- `Parents` is appropriately narrow: two adults plus one child. This definition should remain stable in the production manifest.
- `Between / clean` is selected as the default illustration. `Between / instructional` remains a useful optional learning overlay; keep it separate rather than baking numbers into every image.
- The child's feedback selects **mutual pointing** as the preferred `Each other` grammar. The v2 pointing image remains a semantic pass but is held for character inconsistency; v3 is the corrected candidate and passes the current character-lock check at 160 px. The loop-exchange version remains a fallback for a sentence that explicitly involves exchanging or passing; the mutual-help version remains a candidate for `help one another`.

These eight files are prototypes, not yet wired into Unit 1／Unit 2 production cards. Keep them under `assets/visual-prototypes/` until blind semantic review passes.

## 8. Character consistency QA｜2026-09-20

The first mutual-pointing image (`v2`) passes the **meaning** review, but it does not pass the absolute anchor-character review. The corrected `v3` image is the current candidate and passes this static character check at 160 px; it still remains a prototype until blind learner review and card integration are complete.

| Check against the official anchor | Result | Evidence in `each-other-pointing-v2.png` |
|---|---|---|
| Green hero silhouette and head/body proportion | `v2 HOLD → v3 PASS` | v2 was taller and more long-necked; v3 returns to a compact integrated bean silhouette and a lower visual center. |
| Canonical anatomy | `v2 HOLD → v3 PASS` | v2 had an overlong tapered arm and toe marks; v3 uses short rounded arms, flat feet and three small rounded plates. |
| Face and expression parts | `v2 HOLD → v3 PASS` | v2 added cheek/blush texture; v3 returns to dot eyes and a short mouth with no extra marks. |
| Green color and surface treatment | `v2 HOLD → v3 PASS` | v3 returns to the anchor green family and restrained paper texture. |
| Ink, paper and semantic staging | `PASS` | Warm paper, thick dark contour, simple ground line, clean negative space and mutual pointing fit the world grammar. |
| Companion species role | `PASS WITH LIMITS` | The triceratops silhouette is useful; retain only its horns/frill as the identity cue and remove unnecessary blush/belly detailing in the production version. |

### Absolute lock for the next regeneration

Keep the semantic action unchanged, but enforce: exact anchor head/body silhouette and scale; three small rounded back plates; short rounded arm with no finger or tapered tip; two simple dot eyes when the view allows; one short mouth arc; no cheek marks, blush, toe lines or extra facial features; anchor green token family (`#18B985` / `#13A97C`); restrained paper grain only. The next asset should be judged `character pass` separately from `semantic pass`.

## 9. Acceptance gates

- [ ] `Family` is visibly broader than `Parents` in cast size or generational variety.
- [ ] `Parents` reads as two adults plus one child without needing the word label.
- [ ] `Between` clean and annotated versions can be compared side by side.
- [ ] `Between` annotation is limited to `1`, `2` and spatial guide marks; no prose.
- [ ] `Each other` is visibly reciprocal; a one-way exchange is rejected. The current preferred cue is simultaneous mutual pointing.
- [ ] At least one pilot uses a non-anchor species while preserving the anchor line/color grammar.
- [ ] No attached-reference text, watermark, quote, or exact character is copied.
- [ ] All eight prototypes remain separate from production assets until blind semantic review.

## 10. Next decision

After the eight comparisons, choose one semantic grammar for each word family and update the Unit 1／Unit 2 full manifest. Do not generate all 62 production images until `Family` vs `Parents`, `Between`, and `Each other` each have a passing visual grammar.
