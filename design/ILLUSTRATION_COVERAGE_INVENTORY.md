# FlashCards Illustration Coverage Inventory

> Status: `63 user-selected final + 5 Wave 13 review candidates / 69 vocabulary cards / 68 unique image assets / 69 wired / 0 without an image`
>
> Date: 2026-09-22 (Asia/Taipei)

## Counting rule

This inventory parses the live `JUNIOR_UNIT1_WORDS` and `JUNIOR_UNIT2_WORDS` arrays in `index.html`. A word is counted as **covered** when a current image asset is wired for that word. Duplicate variants and superseded files remain in the repository as history. The 2026-09-21 selection is recorded in `design/FINAL_IMAGE_SELECTION_2026-09-21.md`.

## Summary

| Unit | Vocabulary words | Covered by an image/prototype | Still without an image/prototype |
|---:|---:|---:|---:|
| Unit 1 | 29 | 29 | 0 |
| Unit 2 | 40 | 40 | 0 |
| **Total** | **69** | **69** | **0** |

## Unit 1

Covered: `Family`, `Son`, `Office Worker`, `Cousin`, `I See`, `Classmate`, `Too`, `Baby`, `Singer`, `Writer`, `Police Officer`, `Uncle`, `Aunt`, `Wife`, `Daughter`, `Husband`, `Junior High School`, `Elementary School`, `Housewife`, `Nice to Meet You`, `Dear`, `Years Old`, `Woman`, `Young`, `New`, `Really`, `Handsome`, `Very`, `Beautiful`.

Still without an image/prototype (0):

None. All Unit 1 words now have a user-selected current image wired into `index.html`.

## Unit 2

Covered: `House`, `Parents`, `Living Room`, `Wall`, `Purple`, `Color`, `Colorful`, `Favorite`, `Kitchen`, `Dining Room`, `But`, `Gray`, `Brown`, `Cookie`, `Mice`, `Maybe`, `Sofa`, `Hungry`, `Notebook`, `Marker`, `Brush`, `Gift`, `Pencil Case`, `Bathroom`, `Table`, `Bedroom`, `Near`, `Between`, `Behind`, `In Front Of`, `Special`, `Inside`, `Outside`, `Each Other`, `Right`, `Above`, `Enough`, `Person`, `Persons`, `People`.

Still without an image/prototype (0):

None. `Right` now uses the selected Wave 11 turn-right asset; the earlier static viewer-right candidate is retained as historical, and a future correctness sense would require a separate asset. `Above`, `Enough`, `Person`, `People` and `Outside` are newly wired Wave 13 review candidates; `Persons` is a plural extension card that deliberately reuses the `People` image so the three-word family stays together.

`Colorful` was added to the live Unit 2 vocabulary on 2026-09-20 and is now wired to the selected Wave 05 extension asset. The selected Wave 06, Wave 07, Wave 08, Wave 09, Wave 10 and Wave 11 assets are also wired into `index.html`. Unselected wave variants remain stored locally as history. This local final-selection state is separate from Git commit or publication.

The color group (`Purple`, `Color`, `Gray`, `Brown`) shares one controlled color-meaning grammar. The user selected the current `Favorite`／`Special` and `But`／contrast candidates for this final set, with `But` explicitly using v1 and v2 retained as history. Wave 10 uses `Woman`, `Young`, `New`, `Really v2`, `Very v2`, `Handsome` and `Beautiful`; the earlier `Really v1`／`Very v1` candidates remain historical. Wave 11 uses `Right` as a turn-right asset. Wave 12 replaces the four human-style Unit 1 sources (`Too`, `Son`, `Office Worker`, `Cousin`) with anchor-locked small-dinosaur versions while preserving the old files.

## Anchor re-audit before review/integration

The review/integration pass must re-apply `design/FLASHCARDS_VISUAL_INDEX.md` and the House semantic anchor:

- compact bean/gumdrop body with low visual center; no long neck or tall slender anatomy;
- three small rounded back plates, short rounded limbs and flat feet;
- low soft tail is a required visible identity cue whenever the scene does not intentionally occlude it;
- two small black dot eyes and one short mouth arc; no extra facial marks;
- emerald/teal green, charcoal contour, opaque warm-paper field and restrained paper grain;
- one clear semantic focus; 1–3 characters only when the meaning requires them; no text, logo or watermark.

The Wave 01 `In Front Of` and `Near` bases failed the tail-visibility check. Their v2 replacements now show the tail and the preview points to v2; v1 files remain preserved as superseded audit history. Wave 05’s four color prototypes, Wave 06’s four abstract-grammar prototypes, Wave 07’s four people/roles prototypes, Wave 08’s five family-role prototypes and Wave 09’s six school/greeting prototypes pass the current visible-tail and 160 px checks. Wave 09 uses intentional school scale, greeting interaction and age-progression composition; these are semantic cues, not new anchor variants.

Wave 13 adds `Above`, `Enough`, `Person`, `People` and `Outside` from the next Unit 2 vocabulary expansion. Their prompts, semantic decisions, hashes and review status are recorded in `design/ILLUSTRATION_BATCH_WAVE_13_UNIT2_EXPANSION.md`.

## Recommended next order

1. Run the final app-level smoke test across Unit 1 and Unit 2 with the selected image map.
2. If any selected card reveals a character or semantic issue, make a new versioned replacement; do not overwrite the selected file or delete history.
3. Commit and publish only after the user explicitly authorizes that Git step.
