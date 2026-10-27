# FlashCards Unit 3｜2026-10-27 小恐龍手繪插畫正式接入規格

- Project: `/Users/chiangpofu/Projects/active/flashcards`
- Notion source of truth: https://app.notion.com/p/3d3dffffcd808123aeb1cc29acf90180
- Visual anchor reference: `assets/unit2/Codex 圖像 2026年9月20日 上午10_24_38.png` (see `design/FLASHCARDS_VISUAL_INDEX.md`)
- Unit 3: **34 English vocabulary items**, 34 individual raster PNGs + 34 WebP optimized derivatives.
- Source: 2026-10-27 user's four approved small-dinosaur illustration sheets, cropped *without the printed word captions*.
- No SVG/vector redraw for the Unit 3 illustration system. Keep existing legacy renderer only if other units still rely on it.

## Data integration

Set `image` on each **Unit 3 item only**. Do not use a global word-only override, which could accidentally change other units. Reuse the existing `illustrationFor(item)` image precedence and `<picture>` output. Its WebP rewrite `assets/...png` → `assets/optimized/...webp` matches this package.

## UX and visual QA

- 34 / 34 entries in Unit 3, 0 duplicates, 0 missing `image`.
- `assets/unit3/*.png` exists for every item; WebP derivative exists in `assets/optimized/unit3/*.webp`.
- No handwritten English word labels within any image; answer appears only in the website's existing learning UI.
- Run Learn and Spell, confirm wrong-answer review and audio, check at mobile widths 375 / 390 / 430 px.
- Avoid crop edges or image scaling distorting the original soft-paper texture.
- Verify only the approved images are used, not the old Unit 3 inline SVG renderer.
- **Can**: user explicitly selected the noun meaning「罐子」on 2026-10-27 in this integration chat. Use the existing cookie-canister illustration; category is Object, theme is theme-accessor. This release does not teach the modal auxiliary meaning.
- **Hand**: raised hand highlighted by motion rays; **Sign**: pedestrian direction sign; **Safe**: protected zone and shield/check symbol. Visual inspection found these compatible with the intended Body / Object / Trait categories.
- All 34 PNGs visually inspected: no English answer captions. Original scene framing is preserved, including intentional edge crops; CSS uses object-fit:contain. Quiet includes sleep marks (zzz), and Time/Now include clock numerals, neither spelling the answer.
- Original nested input package is retained unmodified and is not included in the release commit. Selected originals are copied byte-for-byte to assets/unit3/*.png, with their supplied WebP derivatives under assets/optimized/unit3/.
- No change to Unit 1 and Unit 2 images, sessions, grammar, local review state, or stored quiz results.

## Release control

User requested commit, GitHub push, and GitHub Pages live publication. Execute these **from the canonical local repo** only after `git status`, `git diff`, branch reconciliation and browser QA. Do not overwrite uncommitted Codex work, force push, or claim success before checking GitHub Pages.

## Local QA completed 2026-10-27

- Base local main: `c285fb7dd3cb8d42f0c335b50643aef4ae368948` (existing Unit 3 vocabulary commit). Fetched remote main: `21706f11141772575413ac47d630044d5f8d6317`; local ahead 1 / behind 0 before integration.
- 34 unique words and mappings; all supplied PNG checksums matched and PNG/WebP copies are byte-identical to the input package.
- Browser HTTP and decode: **34/34 PNG + 34/34 WebP**, all 200. WebP total: 807,588 bytes; PNG total: 6,652,686 bytes.
- Real UI traversal of Unit 3-1 (20) and Unit 3-2 (14): **Learn 34/34, Spell 34/34**; answers hidden before checking; score/completion verified.
- Each subunit tested with one deliberate wrong answer, followed by wrong-word review and a correct result of **1/1**.
- Mobile touch emulation at **375, 390, 430px**: all 34 images in both modes (68 checks per width), no clipped card/control bounding boxes, no horizontal overflow or overlapping input/check controls. Desktop 1280px also inspected.
- Unit 1-1/1-2/2-1/2-2 Learn and Spell smoke checks passed; elementary Learn and Spell passed. Existing word arrays are byte-for-byte unchanged.
- **0 JavaScript exceptions; 0 card image request failures**. Local server has the existing unrelated `/favicon.ico` 404.
- Listen button dispatches the current word with `en-US`. Automated QA intercepts speech to avoid repeated playback; actual audio was not human-auditioned.
- No source images regenerated or recropped. Source boards are not in this package, so original pre-crop boundaries cannot be reconstructed. Supplied crop framing was visually inspected; display uses `contain`.
- Mapping, provenance, hashes and validation summary: `UNIT3_RASTER_MANIFEST_2026-10-27.json`.
- Release is gated on this QA; remote deployment and fresh live content must be verified against the eventual release commit SHA separately.
