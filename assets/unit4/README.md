# Unit 4 — What Time Is The Concert?

35 words, in the supplied order; Unit 4-1 contains 20 and Unit 4-2 contains 15.

Artwork status: **pending**. No approved Unit 4 sheet or individual illustrations
were found in the inspected project, Downloads, Desktop, or Pictures locations.
The app shows an explicit pending illustration message without requesting missing
files or falling back to SVG. The manifest paths are reserved, not existing assets.

## Add the approved dinosaur raster cards

1. If supplied as a sheet, inspect the grid and crop each complete card without
   borders from adjacent cells; confirm word-to-image meaning before integration.
2. Save each approved PNG using `manifest.json`; add the corresponding WebP under
   `assets/optimized/unit4/`. Preserve the hand-drawn dinosaur style.
3. In `index.html`, replace the matching `UNIT4_IMAGE_PATHS` null with the PNG path.
   The item constructor clears its pending state automatically. Update manifest status.
4. Test actual PNG and WebP HTTP/decode, Learn, Spell, Review, and mobile layouts.

Special filenames: `pm.png`, `am.png`, `oclock.png`. Keep p.m., a.m., and o'clock
unchanged in vocabulary/spelling. Unit 4 sign means autograph; do not reuse Unit 3's
notice-sign image. Fan means a music fan. Free is provisionally available/not busy
in this concert/weekend context; confirm against the supplied artwork/textbook.

No new illustration was generated, and no old unit image was substituted.
