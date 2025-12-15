# The Invariant — Concept

*Last updated: 2024-12-14*

---

## Core Premise

A publication that behaves like a **living surface with decay built in**.

---

## Time Model

There is **no issue cycle**. Content appears, ages, and disappears.

Every piece has a **lifespan**:

| Age | State | Behavior |
|-----|-------|----------|
| **0–7 days** | **Vivid** | Fully present, vibrant color, full motion, high priority |
| **7–14 days** | **Fading** | Color drains, motion slows, feels less urgent |
| **14–30 days** | **Dying** | Muted, withdrawn, giving way to newer material |
| **30+ days** | **Dead** | Pushed to background layer, residue only |

---

## The Surface

The site is always **the present**.

- There is **no archive as a primary experience**
- Older material exists only as **residue** — partially visible, obscured, accessible only through deliberate excavation
- The default state prioritizes what is **fresh and unfinished**

---

## The Map

The surface operates as a **continuously shifting map**.

- New pieces attach themselves where old ones were
- Some inherit connections
- Others break them
- The structure is **stable enough to be legible** but **never static long enough to feel complete**

---

## Reading Mode

Reading **stabilizes** the interface.

When a reader opens a piece, it is **readable regardless of age**. The decay affects the environment around it, not the act of reading itself.

> *The piece may be dying on the map, but alive in your hands.*

---

## Design Language of Time

| State | Visual Treatment |
|-------|------------------|
| **Fresh** | Asserts itself — vivid, animated, foreground |
| **Aging** | Withdraws — desaturated, slower, receding |
| **Dead** | Context, not content — texture, residue, archaeology |

---

## The Result

Not a magazine that publishes on a schedule, but a **system that enforces attention through impermanence**.

- If you are not present, **you miss things**
- If you return, **the place has changed**

---

## Implications for Implementation

### Content Model
- Every piece needs a `publishedAt` timestamp
- Age is computed client-side (or at build time for static layers)
- Visual state derived from age, not stored

### Map Rendering (PixiJS)
- Pieces at different life stages render with different:
  - Alpha/opacity
  - Saturation (color grading filter)
  - Animation speed/amplitude
  - Z-depth (fresher = foreground)
  - Interaction affordance (dead pieces harder to select)

### Archaeology Mode
- Optional toggle or gesture to "dig" — reveal dead layer
- Could be literal scratch/reveal mechanic
- Or parallax depth shift

### Reading Mode
- Entering a piece freezes its visual state
- Clean typography, stable layout
- Exit returns to decayed map state

### No Permalinks? Or Decaying Permalinks?
- Design decision: can you link to a dead piece?
- Options:
  1. Links work forever (piece is readable, but map shows it as dead)
  2. Links decay (404 after 90 days? redirect to excavation?)
  3. Links to dead pieces require "excavation" interaction

---

## Open Questions

- [ ] What is the minimum viable lifespan model? (linear decay vs. stepped states)
- [ ] How does the map reclaim space? (new pieces inherit position, or find new spots?)
- [ ] Is there any "pinned" content that never decays? (about page, etc.)
- [ ] How do relationships age? (if A links to B, and B dies, what happens to the link?)
- [ ] Is there seasonal variation? (summer = slower decay, winter = faster?)
