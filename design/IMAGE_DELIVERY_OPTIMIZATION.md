# FlashCards image delivery optimization

Updated 2026-09-22 for mobile delivery.

## Policy

- Original approved PNG/JPEG files remain the visual source-of-truth and are not replaced.
- The 68 images currently selected by `IMAGE_OVERRIDES` or item-level `image` fields have a matching derivative under `assets/optimized/`.
- Derivatives are WebP, constrained to 640px, quality 82, with metadata removed.
- `index.html` serves the WebP derivative first and keeps the original image as a browser/error fallback.
- The current card is loaded eagerly; the full deck is not preloaded.

## Why this exists

The selected originals are about 107 MB in total, while the optimized delivery set is about 1.1 MB. This keeps the visual anchors intact while making individual mobile requests much smaller.

When new approved artwork is added, generate its matching WebP under the same relative path in `assets/optimized/`, then verify the original and derivative both exist before publishing.
