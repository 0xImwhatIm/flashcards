# FlashCards UI Visual Refresh v0.2

Date: 2026-09-21

## Goal

Align the interactive learning interface with the approved FlashCards illustration anchor and the newly selected dinosaur assets, without changing the learning flow or answer logic.

## Visual decisions

- Use a warm paper canvas with a restrained grain-like CSS texture instead of the cool gray application background.
- Use charcoal ink for primary text and borders, with slightly irregular corner radii and offset shadows to echo the hand-drawn contour.
- Use the illustration palette as UI tokens: emerald/teal for progress and listening, muted slate blue for secondary navigation, mustard for shuffle/review, and coral for forward/completion actions.
- Keep cards paper-colored and quiet so the illustration remains the focal point; replace large theme gradients with a small accent strip and a warm category badge.
- Enlarge the illustration frame so the generous negative space in the approved square assets does not make the mascot feel undersized.
- Preserve the existing Learn, Spell, Listen, Auto Read, speed, wrong-answer review, and course/session controls.

## Accessibility and behavior

- Existing semantic buttons, labels, keyboard focus styling, reduced-motion handling, and responsive breakpoints remain in place.
- Color is used as a secondary cue; button labels and phase labels remain explicit.
- No new external runtime dependency was added; the refresh is CSS-only plus the existing Google font imports.

## Release status

The owner approved this UI after visual review on 2026-09-21. It is now being released through the repository's `main` branch and GitHub Pages.

## 2026-09-22 Elementary parity

The Elementary course now uses the same approved editorial skin as Junior: warm
paper canvas, charcoal ink borders, mascot-led accent colors, paper cards, and
the same responsive control layout. Course labels, vocabulary, illustrations,
and learning behavior remain course-specific; this change only removes the old
generic Elementary presentation.

The owner approved the parity update after visual review on 2026-09-22. The
title underline was removed as a final polish, and this update is being
published through the repository's `main` branch and GitHub Pages.
