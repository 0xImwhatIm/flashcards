# FlashCards Illustration Batch｜Wave 12 Unit 1 repair

Date: 2026-09-21
Status: `generated / copied / visually checked / ready for final app smoke QA`

## Scope

The user requested four Unit 1 illustrations to be regenerated under the approved small-dinosaur character rules. The earlier human-style files remain in `assets/unit1/` as historical references and are not deleted.

## Anchor lock

Primary reference: `assets/unit2/Codex 圖像 2026年9月20日 上午10_24_38.png`

Every prompt reasserted the following invariants:

- warm off-white paper background and soft paper texture;
- compact rounded emerald-green dinosaur mascot grammar;
- thick, slightly wobbly charcoal contour;
- tiny dot eyes, short gentle mouth, short rounded arms and feet;
- three small rounded back plates and a clearly visible curved tail;
- no human characters, realistic rendering, readable text, labels, numbers, watermarks, or speech bubbles.

Multiple characters are allowed when the vocabulary meaning requires them. Secondary dinosaurs use the same body grammar with restrained color variation.

## Generated assets

| Word | Current selected asset | Semantic direction |
|---|---|---|
| `Too` | `assets/visual-prototypes/batch-v0.2/wave-12-unit1-repair/too-v2.png` | Two same-grammar dinosaurs perform the same action with matching blank flashcards: “also / as well”. |
| `Son` | `assets/visual-prototypes/batch-v0.2/wave-12-unit1-repair/son-v2.png` | One larger adult and one smaller child dinosaur share an album; size and gentle guidance communicate son. |
| `Office Worker` | `assets/visual-prototypes/batch-v0.2/wave-12-unit1-repair/office-worker-v2.png` | One dinosaur works at a simple desk with blank monitor, papers, and mug. |
| `Cousin` | `assets/visual-prototypes/batch-v0.2/wave-12-unit1-repair/cousin-v2.png` | Two same-generation dinosaurs share fruit at a family gathering; no parents or couple cues. |

## Prompt record

The four prompts used the anchor plus the corresponding old Unit 1 image as a semantic reference only. Each prompt explicitly instructed the generator to transform the old human scene into the dinosaur system and to preserve the word meaning without copying the old rendering style.

The first transparent-background `Too` candidate is retained as `too-v2-alpha-candidate.png`; the selected `too-v2.png` is the opaque warm-paper revision.

Special constraints:

- `Too`: parallel matching action, not reciprocal pointing and not contrast.
- `Son`: exactly one adult and one smaller child; a restrained tie is permitted only as an adult cue.
- `Office Worker`: minimal office desk props; blank monitor and visible tail.
- `Cousin`: same-generation pair with one shared neutral prop; no crowd, parents, sibling, or romance cues.

## But selection revision

The user selected `assets/visual-prototypes/batch-v0.2/wave-06-abstract-grammar/but-v1-character-hold.png` as the current `But` asset. `but-v2.png` remains in the repository as historical evidence and is not deleted.

## QA checklist

- [x] Four new files copied to staging and canonical repository.
- [x] Old four Unit 1 files preserved.
- [x] `But` mapping switched to explicit user-selected v1.
- [x] 1254 px source files and 160 px QA thumbnails validated.
- [x] Four repaired images visually checked against the anchor.
- [ ] Final browser smoke check of all four Wave 12 cards.
- [ ] User visual approval of the four repaired cards.
