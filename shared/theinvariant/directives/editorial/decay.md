# Directive: Content Decay Rules

**Created by:** Editorial Team  
**Date:** 2024-12-14  
**Why:** Define how content ages and disappears. Core to The Invariant's "living surface" concept.  
**Status:** Active

---

## Lifespan Model

### Default Lifespan

- **Standard piece:** 14 days (vivid → fading → dying)
- **High priority:** 21 days (extended vivid phase)
- **Low priority:** 7 days (faster decay)
- **Editorial override:** Can set custom lifespan per piece

### Age Computation

```typescript
function computeAge(publishedAt: string): number {
  const now = new Date();
  const published = new Date(publishedAt);
  const diff = now.getTime() - published.getTime();
  return Math.floor(diff / (1000 * 60 * 60 * 24)); // days
}
```

---

## Decay Phases

### Phase 1: Vivid (0-7 days)

- **Editorial:** Fully present, high priority
- **Visual:** 100% opacity, full color, full animation
- **Interaction:** Fully clickable, prominent
- **Map position:** Foreground, center-attracted

### Phase 2: Fading (7-14 days)

- **Editorial:** Still relevant, but less urgent
- **Visual:** 80% opacity, 70% saturation, slower animation
- **Interaction:** Still clickable, but less prominent
- **Map position:** Mid-layer, receding

### Phase 3: Dying (14-30 days)

- **Editorial:** Withdrawing, making space for new
- **Visual:** 55% opacity, 40% saturation, minimal animation
- **Interaction:** Still readable if clicked, but hard to notice
- **Map position:** Background layer

### Phase 4: Dead (30+ days)

- **Editorial:** Context, not content. Archaeology only.
- **Visual:** 25% opacity, 10% saturation (grayscale), no animation
- **Interaction:** Not clickable by default (requires excavation mode)
- **Map position:** Deep background, residue

---

## Visual Decay Curve

Linear interpolation between phases:

```
Opacity:
  0-7 days:   1.0 → 0.8  (linear)
  7-14 days:  0.8 → 0.55 (linear)
  14-30 days: 0.55 → 0.25 (linear)
  30+ days:   0.25 (constant)

Saturation:
  0-7 days:   1.0 → 0.7  (linear)
  7-14 days:  0.7 → 0.4  (linear)
  14-30 days: 0.4 → 0.1  (linear)
  30+ days:   0.1 (constant)
```

---

## Reading Mode Exception

**When a piece is opened for reading, decay is frozen:**

- Article appears in full color (vivid state)
- No opacity/saturation changes
- Typography is stable and readable
- Decay only affects the map, not the reading experience

This ensures: "The piece may be dying on the map, but alive in your hands."

---

## Replacement Rules

### Space Reclamation

- **Dead pieces** (>30 days) are candidates for replacement
- **New pieces** can attach to positions where dead pieces were
- **Some connections** may be inherited
- **Others** break, creating new structure

### Inheritance

- **Position:** New piece can inherit dead piece's map position
- **Connections:** Editor decides (inherit, break, or create new)
- **Visual weight:** New piece starts fresh (vivid)

---

## Editorial Control

### Override Lifespan

Editors can set custom lifespan:
- **Breaking news:** 3 days (fast decay)
- **Feature:** 30 days (slow decay)
- **Evergreen:** Never dies (pinned, always vivid)

### Manual Archive

- Editors can manually mark piece as "dead"
- Useful for removing outdated content
- Still accessible via excavation

---

## Implementation

### Backend

```typescript
// Compute decay state
function getDecayState(piece: Piece): DecayState {
  const age = computeAge(piece.publishedAt);
  const lifespan = piece.lifespan || 14;
  
  if (age > lifespan) return 'dead';
  if (age > lifespan * 0.5) return 'dying';
  if (age > lifespan * 0.25) return 'fading';
  return 'vivid';
}
```

### Frontend

```typescript
// Apply decay visuals
function applyDecayVisuals(node: PixiNode, state: DecayState) {
  const config = DECAY_CONFIGS[state];
  node.alpha = config.opacity;
  node.scale.set(config.scale);
  // Apply color filter for saturation
}
```

---

## Examples

**Piece published 5 days ago:**
- Age: 5 days
- State: Vivid
- Opacity: ~0.93 (interpolated)
- Fully clickable, prominent

**Piece published 10 days ago:**
- Age: 10 days
- State: Fading
- Opacity: ~0.68 (interpolated)
- Still clickable, less prominent

**Piece published 20 days ago:**
- Age: 20 days
- State: Dying
- Opacity: ~0.4 (interpolated)
- Barely visible, background layer

**Piece published 40 days ago:**
- Age: 40 days
- State: Dead
- Opacity: 0.25 (constant)
- Not clickable, archaeology only

---

## Notes

- Decay is **computed client-side** from `publishedAt` timestamp
- No server-side decay state storage (computed on-demand)
- Reading mode **freezes** decay (always appears vivid)
- Dead pieces are **not deleted**, just hidden (archaeology accessible)
