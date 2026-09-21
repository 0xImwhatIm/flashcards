# FlashCards Illustration Batch｜Wave 07 People & Roles

> Status: `generated / 4 Unit 1 words / review-ready / anchor-locked`
>
> Date: 2026-09-21 (Asia/Taipei)

> Final selection update: the user selected all four current assets in this wave; they are wired in `index.html`. See `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Batch decision

This wave covers four concrete Unit 1 identity and role words: `Singer`, `Writer`, `Police Officer` and `Baby`. They were selected because each can be taught with one unambiguous prop or pose while keeping the same mascot grammar. Family relations, school words and abstract adjectives remain separate waves so their semantic distinctions can be reviewed without mixing them into this batch. `Right` remains gated by the Unit 2 sense decision.

These are review-ready semantic prototypes, not production replacements. They are stored in the project but are not wired into `index.html`.

## Shared anchor lock

- compact emerald/teal bean or gumdrop mascot with a low visual center; no long neck or tall slender anatomy;
- three small rounded back plates and a low soft tail, both visible unless the scene intentionally occludes them;
- short rounded limbs, flat feet, two small black dot eyes and one short charcoal mouth arc;
- thick, slightly wobbly charcoal contour; opaque warm off-white paper field; restrained matte pigment grain;
- one clear semantic focus; 1–3 characters only when the meaning requires them;
- no text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows or eye highlights.

## Semantic grammar and prompt deltas

| ID | Word | Semantic construction | Planned output |
|---|---|---|---|
| W07-SINGER | Singer | One mascot sings into a small mustard microphone; two restrained charcoal sound curves support the action. An open mouth is allowed only as the semantic singing cue. | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/singer-v2.png` |
| W07-WRITER | Writer | One mascot sits at a small warm-wood desk, pencil touching a completely blank open notebook; a small dusty blue-gray lamp establishes a writing workspace. | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/writer-v1.png` |
| W07-POLICE-OFFICER | Police Officer | One mascot wears an oversized dusty blue-gray police cap with a blank mustard badge and gives a calm on-duty gesture; no weapon, vehicle, city or readable insignia. | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/police-officer-v1.png` |
| W07-BABY | Baby | A small mascot is wrapped in a warm cream swaddle in a low dusty blue-gray cradle, with a simple mustard rattle. The swaddle intentionally occludes most of the body while the tail tip and three plates remain visible. | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/baby-v1.png` |

### Prompt set

All four prompts used the same anchor-locked opening:

```text
Use case: illustration-story. FlashCards vocabulary prototype, square 1254x1254 illustration. Use the same compact emerald/teal green bean/gumdrop mascot as the provided FlashCards anchor: low visual center, three small rounded back plates, low soft tail, short rounded limbs, flat feet, two small black dot eyes and one short mouth arc. Flat hand-drawn children's illustration, warm off-white paper field, generous upper negative space, one thin ground line, thick rounded charcoal ink with slight wobble, restrained matte pigment/paper grain, natural muted colors. No text, letters, numbers, logos, watermark, speech bubble, glossy 3D, anime eyes, fingers, toes, blush, eyebrows, teeth or eye highlights. One semantic focus, readable at 160 px.
```

Prompt deltas:

- `Singer`: one microphone held near the face, open singing mouth with no teeth, two simple charcoal sound curves, no stage or audience;
- `Writer`: pencil touching a blank notebook on a small desk, lamp only as a quiet workspace cue, no letters or marks on the paper;
- `Police Officer`: blue-gray cap and blank mustard badge, friendly raised hand, no weapon, vehicle, city or readable text;
- `Baby`: small mascot in cream swaddle and low cradle, mustard rattle, keep the tail tip and three plates visible, no second adult.

## Result registry

Generation mode: built-in ImageGen. All four selected final assets are 1254×1254 RGB PNGs and have a 160 px thumbnail export. `review-ready` remains below `pilot_accepted`.

| ID | Asset | SHA-256 | Status | QA |
|---|---|---|---|---|
| W07-SINGER | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/singer-v2.png` | `08b1372267d1257cb2cefe427ecdbb75f1bfc78ec1667a85e0ca2cda0c9258a8` | `generated / review-ready` | Singer reads at 160 px; tail and three plates visible. Open mouth/pink interior is a deliberate semantic exception for singing and has no teeth or text. |
| W07-WRITER | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/writer-v1.png` | `ba4acabeb4355d0af461650032b5511fecd112e392fc76a539e81d83d936d1f7` | `generated / review-ready` | Pencil, blank notebook and desk read at 160 px; tail and three plates visible; no page text. |
| W07-POLICE-OFFICER | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/police-officer-v1.png` | `973bd86d1a488f19dee31937daae8cc0ac1f3c708ec9b0cde8fb8dbd16e47fb3` | `generated / review-ready` | Cap, blank badge and calm gesture read at 160 px; tail and three plates visible; no weapon or insignia text. |
| W07-BABY | `assets/visual-prototypes/batch-v0.2/wave-07-people-roles/baby-v1.png` | `4d01d30eb679a2af0012b6ad21b4b2150cb7c387c1a738dd7fa0f9e400444701` | `generated / review-ready` | Swaddled baby, cradle and rattle read at 160 px; intentional swaddle occlusion still leaves the tail tip and three plates visible. |

### Superseded audit output

`singer-v1-character-hold.png` is retained as audit history only. It had an overly dark vignette/edge treatment that broke the uniform warm-paper background. `singer-v2.png` is the replacement review candidate.

## QA gates

- [x] 1254×1254 RGB output for all four selected final assets.
- [x] 160 px thumbnail remains semantically readable for all four.
- [x] Tail and three rounded plates remain visible, except where Baby's swaddle intentionally occludes the body (tail tip and plates remain visible).
- [x] No text, logo, watermark or readable label appears.
- [x] Singer v1 was held and v2 regenerated after the background drift was identified.
- [ ] Blind learner review.
- [ ] `pilot_accepted` and local app wiring.

## Next order

1. Review Wave 07 with labels hidden and compare it with the House anchor at both full size and 160 px.
2. Generate the family-role wave (`Uncle`, `Aunt`, `Wife`, `Daughter`, `Husband`) with explicit relationship grammar so it does not collapse into generic people.
3. Handle school/identity words (`Junior High School`, `Elementary School`, `Dear`, `Nice to Meet You`) as a separate contextual wave; keep abstract adjectives for later.
4. Keep `Right` gated until its intended meaning is selected.
