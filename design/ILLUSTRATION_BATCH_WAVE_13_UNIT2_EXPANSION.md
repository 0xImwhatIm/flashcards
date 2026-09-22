# FlashCards Illustration Batch｜Wave 13 Unit 2 expansion

> Status: `generated / 4 Unit 2 words / review-ready / anchor-locked`
>
> Date: 2026-09-22 (Asia/Taipei)

## Scope

Unit 2新增四個單字：`Above`、`Enough`、`Person`、`People`。本批使用正式綠色小恐龍定錨圖作為 character/style reference，先接入本機 app 供語意與角色一致性檢視；目前是 review-ready 候選，不宣稱已通過最終選圖。

來源語意依使用者提供的課本照片記錄：

- `Above`：在……上方／位置高於另一物，兩者不必接觸；與 `on` 區分。
- `Enough`：足夠的；以「每個角色各有一份」表達 sufficiency，而非單純很多。
- `Person`：一個人／單一個體；本批用單一友善小恐龍肖像表示，不加入職業或身份線索。
- `People`：人們／複數個體；本批用三隻並列的小恐龍表示複數，不加入家庭、職業或群眾場景線索。

## Shared visual lock

- Reference: `assets/unit2/Codex 圖像 2026年9月20日 上午10_24_38.png`
- 1:1 square, 1254 × 1254 RGB PNG
- Warm off-white paper field, generous negative space, one ground line
- Thick, slightly wobbly charcoal contour with restrained pigment grain
- Compact green bean/gumdrop mascot, dot eyes, short curved mouth
- Low rounded tail visible when not semantically occluded; three rounded dorsal plates visible
- No baked vocabulary, labels, numbers, logos, speech bubbles or watermark

## Selected working candidates

| Word | Semantic composition | Asset | SHA-256 | Status |
|---|---|---|---|---|
| `Above` | Green mascot stands below one floating mustard ball, with a clear vertical gap and upward pointing gesture; no contact and no arrow overlay. | `assets/visual-prototypes/batch-v0.2/wave-13-unit2-expansion/above-v1.png` | `e5a1160b53aaeffd9198f1af8c7d3c5eb2e28a5503492f9aaba42028e92c3854` | review-ready |
| `Enough` | Three characters each receive exactly one matching bowl; the green anchor remains primary and the two companions make “enough for everyone” countable. | `assets/visual-prototypes/batch-v0.2/wave-13-unit2-expansion/enough-v1.png` | `5540b32ac63b654ebbd8c65cb098fb4a97c8a6e546d921fd5583438278684d09` | review-ready |
| `Person` | One green mascot stands alone and waves; no occupation, clothing or extra role cue. | `assets/visual-prototypes/batch-v0.2/wave-13-unit2-expansion/person-v1.png` | `5cc488e668d6928b58e3d7cfc876e7358cf1484155c0808bebe49e26275015d461` | review-ready |
| `People` | Exactly three separate dinosaur individuals stand side by side; the green anchor remains central and the companions are only plural-count cues. | `assets/visual-prototypes/batch-v0.2/wave-13-unit2-expansion/people-v1.png` | `c7b45c72d5966785ccd6807bef7a0627615aa9f2bd9fcdc9d6c8b2b680cae117` | review-ready |

## Prompt set

All four assets were generated with built-in ImageGen using the anchor above as the only style/character reference.

### `Above`

```text
Create a clear wordless illustration for the English word "above". Show the same green small dinosaur standing on the ground below a single simple warm-mustard ball floating clearly above its head, with a visible vertical gap and the dinosaur looking upward and pointing toward the higher object. The object must be above, not touching or resting on the dinosaur. Keep the approved mascot anatomy, visible low rounded tail, three rounded dorsal plates, warm off-white paper, thick wobbly charcoal contour, no arrows, text or watermark.
```

### `Enough`

```text
Create a clear wordless illustration for the English word "enough". Show three friendly small dinosaur characters standing in a simple row with exactly three matching bowls of food, one bowl held by or placed directly in front of each character, so every character has one share and none is missing. Keep the green anchor dinosaur primary, with one dusty blue-gray bird-like companion and one muted terracotta triceratops companion. Keep all bodies and tails visible, no table, no numbers, no checkmarks, no text or watermark.
```

### `Person`

```text
Create a clear wordless illustration for the English word "person". Show one friendly green small dinosaur standing upright like a single individual, facing the viewer and giving a small wave. Treat the dinosaur as the one person in the scene; do not add a role, occupation, costume or other character. Preserve the visible low rounded tail and three rounded dorsal plates, with warm off-white paper, thick wobbly charcoal contour, no props, text or watermark.
```

### `People`

```text
Create a clear wordless illustration for the English word "people". Show exactly three friendly small dinosaur individuals standing side by side on the same ground line, with the green anchor in the middle and one dusty blue-gray and one muted terracotta companion. They are three separate people, not a family role, occupation, crowd or action scene. Keep all bodies, tails and the main three dorsal plates visible; use the same warm paper, charcoal contour and restrained pigment grain, with no props, text or watermark.
```

## Integration

`index.html` now includes the four words at the end of `JUNIOR_UNIT2_WORDS` and maps them through `IMAGE_OVERRIDES`. `Person` remains one dinosaur; `People` is exactly three. The vocabulary data remains separate from the image paths so future candidate replacement does not alter phonetics, categories or lesson order.

## QA follow-up

- [x] 1254 × 1254 RGB PNGs
- [x] No readable text, logo or watermark observed
- [x] `Above` reads as static higher position, not movement
- [x] `Enough` reads as one share per character, not abundance
- [x] `Person` reads as one individual, not a role
- [x] `People` reads as exactly three individuals, not a family or crowd
- [ ] Owner blind review and final selection
- [ ] Update final image selection and coverage documents after approval
