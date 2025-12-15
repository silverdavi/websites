# Directive: Map Visual Design

**Created by:** Design Team  
**Date:** 2024-12-14  
**Why:** Define how the interactive map renders nodes, connections, and decay states in PixiJS. Ensures consistent visual language.  
**Status:** Active

---

## Node Appearance

### Base Node

- **Shape:** Circular (future: custom shapes per content type)
- **Size:** 60px diameter (vivid), scales down with decay
- **Border:** 2px, color matches decay state
- **Background:** Gradient or solid, matches beat color
- **Label:** Title text, truncated if >20 chars

### Decay Visual States

| State | Size | Opacity | Saturation | Animation |
|-------|------|---------|------------|-----------|
| **Vivid** | 100% (60px) | 100% | 100% | Pulsing, breathing |
| **Fading** | 90% (54px) | 80% | 70% | Slow pulse |
| **Dying** | 75% (45px) | 55% | 40% | Minimal |
| **Dead** | 60% (36px) | 25% | 10% | None |

### Beat Colors

Each beat has a distinct color for visual organization:

| Beat | Color | Hex |
|------|-------|-----|
| News | Red | `#C84B31` |
| Politics | Blue | `#2E86AB` |
| Science | Green | `#06A77D` |
| Global | Orange | `#F77F00` |
| Health | Purple | `#7209B7` |
| Tech | Teal | `#00D4AA` |
| Social Justice | Pink | `#FF6B9D` |

---

## Connections (Relationships)

### Visual Style

- **Line:** 1px stroke, color matches source node
- **Opacity:** 60% (subtle, doesn't dominate)
- **Style:** Curved (bezier) for organic feel
- **Animation:** Subtle flow animation (particles along line)

### Connection Types

| Type | Color | Style |
|------|-------|-------|
| Related | Source node color | Solid |
| Continues | Source node color | Dashed |
| Responds To | Source node color | Dotted |

---

## Layout Rules

### Positioning

- **Algorithm:** Force-directed graph (D3.js force simulation)
- **Spacing:** Minimum 120px between node centers
- **Clustering:** Nodes of same beat cluster loosely
- **Dead layer:** Separate z-index, lower opacity, behind live nodes

### Camera/Viewport

- **Initial view:** Centered on most recent piece
- **Zoom:** 0.5x to 2x (mouse wheel, pinch)
- **Pan:** Click and drag
- **Bounds:** Prevent panning too far from content

---

## Interaction

### Hover

- **Scale:** 110% (subtle grow)
- **Glow:** Subtle shadow/outline
- **Label:** Show full title (if truncated)
- **Cursor:** Pointer

### Click

- **Action:** Navigate to reading mode
- **Feedback:** Brief scale animation (110% → 100%)
- **Transition:** Smooth fade to reading view

### Dead Nodes

- **Not clickable** (pointer-events: none)
- **Visible** but very faded (archaeology layer)
- **Scratch/reveal** interaction (future)

---

## Performance

### Rendering Budget

- **Max nodes visible:** 100 (paginate if more)
- **Max connections:** 200
- **Target FPS:** 60 (on mid-range phone: 30+)
- **Texture memory:** <50MB

### Optimization

- **Culling:** Only render nodes in viewport
- **LOD:** Lower detail for distant nodes
- **Batching:** Group sprites for efficient rendering
- **Particles:** Limit to 50 active particles

---

## Implementation Notes

### PixiJS Structure

```typescript
// Scene hierarchy
Container (map)
  ├── DeadLayer (z: 0, alpha: 0.3)
  │   └── DeadNodes[]
  ├── ConnectionLayer (z: 1)
  │   └── Connections[]
  └── LiveLayer (z: 2)
      └── LiveNodes[]
```

### Decay Computation

```typescript
function computeDecayState(publishedAt: string): DecayState {
  const age = daysSince(publishedAt);
  if (age > 30) return 'dead';
  if (age > 14) return 'dying';
  if (age > 7) return 'fading';
  return 'vivid';
}
```

---

## Examples

```typescript
// Create node sprite
const node = new Graphics();
node.beginFill(beatColor);
node.drawCircle(0, 0, 30);
node.alpha = decayOpacity;
node.scale.set(decayScale);

// Apply decay filter
const filter = new ColorMatrixFilter();
if (decayState === 'dead') {
  filter.desaturate(0.9);
}
node.filters = [filter];
```

---

## Future Enhancements

- Custom node shapes per content type
- Scratch/reveal for dead layer
- Particle effects on connections
- 3D depth (optional, if performance allows)
