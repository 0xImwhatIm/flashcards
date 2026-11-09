# Unit 4 supplied raster release — 2026-11-09

This completes the artwork previously marked pending in UNIT4_INTEGRATION_2026-11-09.md.
Base commit: 371d62ad4016fc75b63972a5ab43c1a71b68d69e.

## Integration

- User supplied four 1280×960 JPEG sheets: 9 + 9 + 9 + 8 = 35 cards.
- Original sheets preserved byte-for-byte in assets/unit4/source/.
- Extracted 35 PNGs; generated 35 WebPs (quality 88, method 6; total 887922 bytes).
- Crop boxes exclude titles and external labels, including tiny label fragments.
- Source pixels are preserved exactly in PNG crops; no redraw, retouch or upscale.
- manifest.json records crop coordinates, source/derivative SHA-256, dimensions and mappings.
- extract_cards.py reproduces the derivatives after validating source hashes.
- UNIT4_IMAGE_PATHS now assigns real paths to item.image. Existing raster renderer retained.
- Existing Unit 4 words, 20/15 sessions, course keys and Sign meanings unchanged.
- Free is available/not busy; fan is music fan; sign is autograph.
- Text embedded in supplied art is retained (weekdays, English, today, p.m.); these can
  provide spelling hints. No separately invented clean-art variants are introduced.

## Verification

- Inspected all 35 cropped illustrations in a contact sheet and mobile screenshots.
- 35/35 Learn and 35/35 Spell UI flows; 2/2 intentional wrong-answer reviews completed.
- All Unit 4 cards select their WebP and use object-fit: contain; no pending-art state.
- 375/390/430px Learn/Spell: no horizontal overflow or overlapping controls.
- 274 unique assets (70 Unit 4 plus 204 prior-unit PNG/WebP) HTTP/decode checks passed.
- Zero JavaScript exceptions and zero card asset HTTP failures.
- The existing missing favicon.ico still returns 404 in local preview; unrelated to card art.
- 14 legacy course/session mode smoke checks passed.
- All 35 PNGs exactly match source crop pixels; all manifest hashes match.
- Rebuilt all derivatives with extract_cards.py and verified reproducibility.
- Preserved 73 pre-existing untracked Unit 3 files byte-for-byte and excluded them from commit.
- git diff --check passed. Audio API calls checked, no human listening test.

Evidence: /Users/chiangpofu/.codex/visualizations/2026/11/09/01a1c034-b4a9-7551-955a-95d3da1a22d6/unit4-art/
