# Unit 4 integration — 2026-11-09

Canonical repo: `/Users/chiangpofu/Projects/active/flashcards`.
Remote: `https://github.com/0xImwhatIm/flashcards.git`; branch: `main`.
Base: `450c31e7cb729ff23b270b82b6db4e8c516be56e`.

## Delivered

- Added exactly the 35 supplied words, in supplied order and case, with phonetics.
- Unit 4-1: first 20; Unit 4-2: remaining 15. Both join juniorMixed (138 cards).
- Kept Unit 3 Sign (notice) and Unit 4 sign (autograph) distinct in the mixed deck.
- Reserved 35 PNG/WebP pairs in assets/unit4/manifest.json.
- Scoped UNIT4_IMAGE_PATHS maps into item.image; no global image override changes.
- Actual art is **not delivered**: no Unit 4 image or sheet found in inspected locations.
  Null mappings show an explicit pending-art message and make no image requests;
  they never use the SVG mascot fallback or unrelated existing word illustrations.
- Await approved dinosaur card images or a full sheet; see assets/unit4/README.md.

## Local verification

- Browser: Chromium through Playwright CLI; actual UI interactions.
- Learn: 35/35, including completion screens.
- Spell: 35/35, with an intentional wrong answer in each subunit.
- Wrong-answer Review: 2/2, corrected answers and 1/1 completion scores.
- Mobile: Learn/Spell at widths 375, 390, 430; no horizontal overflow or control overlaps.
- Inspected long-word 375px Learn and 390px Spell screenshots.
- Legacy: 14 mode/session smoke checks; 204 distinct PNG/WebP HTTP/decode successes.
- Zero JavaScript exceptions and zero card image HTTP failures.
- Initial local browser navigation requested the pre-existing missing favicon.ico (404).
  This is a site icon request, not a card asset or a JavaScript exception.
- TTS API invocation verified; no human listening test performed.
- Exact supplied words and manifest order checked; all old non-mixed sessions unchanged.
- All 73 pre-existing untracked Unit 3 files retained byte-for-byte and excluded from commit.
- git diff --check passed.

Evidence: `/Users/chiangpofu/.codex/visualizations/2026/11/09/01a1c034-b4a9-7551-955a-95d3da1a22d6/unit4-qa/`.

Full illustration QA remains pending until real Unit 4 assets are supplied.
