# FlashCards Spatial Instructional Overlays｜v0.1

> Status: `implemented prototype / separate overlay layer / base assets unchanged`
>
> Date: 2026-09-20 (Asia/Taipei)

## Decision

The four Wave 01 spatial images should keep their clean base illustrations. Directional arrows are useful for teaching, but they should be a **separate instructional overlay** that can be switched on in Figma or the UI. The arrow is a relation cue, not part of the permanent character artwork.

This keeps the semantic image reusable, avoids clutter at small card sizes, and prevents the arrow from becoming a second visual style.

The four prototype SVG overlays are stored with Wave 01 under `assets/visual-prototypes/batch-v0.2/wave-01-spatial/overlays/`; the HTML composed preview is in the same folder.

## Shared overlay grammar

- Use the same charcoal contour and restrained mustard accent as the Visual Index: charcoal `#202223`, mustard `#F2C44E`, rounded caps and rounded arrowheads.
- Use one overlay idea per card. Never combine a depth arrow, a distance bracket and motion trails on the same asset.
- Keep arrows outside faces, eyes, mouths, back plates and the primary semantic object.
- No text, labels, numbers, dotted measurement rulers, glossy 3D arrows or emoji.
- The overlay must explain a static relation. If it can be read as an action that is happening instead of a position that is true, reduce the shaft length or use a bracket/occlusion cue.
- Store the base image and overlay as separate layers/variants: `base`, `instructional-overlay`, and `composed-preview`.

## Per-word recommendations

| Word | Recommended cue | Why | Avoid |
|---|---|---|---|
| `Behind` | A short receding depth arrow that starts on the foreground/right plane and points toward the rear/upper plane behind the box/object; the arrowhead sits on the rear side, not above the character. Preserve the existing occlusion. | The occlusion proves the relation; the arrowhead direction now explicitly travels away from the viewer into depth. | A floating left/right arrow, a large arrow over the character, or a full perspective tunnel. |
| `In Front Of` | A short perspective arrow from the background sign/object toward the foreground anchor/viewer, with a slightly larger near arrowhead. Keep the anchor visibly overlapping the signboard. | “Front” is toward the viewer, so a small depth wedge is clearer than a flat horizontal arrow. | A normal side-to-side arrow, an arrow that hides the anchor face, or glossy 3D rendering. |
| `Inside` | One vertical downward arrow whose endpoint is clearly inside the container interior, below the rim. Keep the mascot and rim visible. | The arrow endpoint confirms containment without changing the base scene. | An arrow ending on the rim, an arrow passing through the face, or a second outward arrow. |
| `Near` | Two short inward-facing chevrons／arrowheads around the narrow gap, optionally paired with a small rounded distance bracket under the gap. The heads stop before touching. | The small gap and the bracket communicate closeness without implying a long movement path. | Long arrows, motion trails, arrowheads touching, or a symbol that reads as `Between`／exchange. |

## UI / Figma model

```text
Illustration asset
├─ base: clean semantic image
├─ instructionalOverlay: none | behindDepth | frontDepth | insideDown | nearGap
└─ composedPreview: base + optional instructionalOverlay
```

The default card uses `base`. The overlay is enabled only when the learner needs extra spatial scaffolding or when a prototype is being reviewed. It must not be baked into the canonical raster asset.

## 2026-09-20 direction correction

User review found that the original `Behind` overlay arrowhead pointed toward the foreground/box edge and sat too far above the box. The corrected SVG now starts closer to the foreground plane (`M753 720`), travels up/right into the rear plane, and ends at `932 598` with the arrowhead at the rear endpoint. This makes the static relation read as **front → behind**, not as movement toward the viewer. A second review found that the `In Front Of` arrowhead was pointing sideways relative to its shaft; its triangle now follows the final down-left tangent toward the foreground anchor. The base illustrations and the `Inside`／`Near` overlays are unchanged.

## Acceptance checks

- [ ] Base image still reads correctly with the overlay hidden.
- [ ] Overlay improves positional recognition at 160 px without obscuring the anchor.
- [x] `Behind` and `In Front Of` are distinguished by occlusion direction plus opposite depth-arrow orientation: `Behind` points rear/up; `In Front Of` points foreground/down.
- [ ] `Inside` arrow ends inside the container.
- [ ] `Near` remains “close” rather than “moving toward” or `Between`.
- [ ] Overlay uses the same line, color and paper-world grammar as the illustration.

## Future movement-directional family

Movement arrows are a separate future system. They may use longer shafts, repeated arrowheads, motion trails or controlled speed marks, but they must not reuse the static-position overlay files or their short relation-only geometry. The distinction is intentional: **position arrow = where a relation exists; movement arrow = where something is going**.
