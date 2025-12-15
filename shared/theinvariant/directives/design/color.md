# Directive: Color Palette

**Created by:** Design Team  
**Date:** 2024-12-14  
**Why:** Establish warm, vintage magazine color system with decay states. Supports both vivid and faded content.  
**Status:** Active

---

## Base Palette

### Backgrounds

| Color | Hex | Usage | Contrast Ratio |
|-------|-----|-------|----------------|
| **Background** | `#FDFBF7` | Main page background | - |
| **Background Alt** | `#F7F4ED` | Sections, cards | - |
| **Background Accent** | `#EDE8DC` | Hover states, highlights | - |

### Text

| Color | Hex | Usage | Contrast Ratio |
|-------|-----|-------|----------------|
| **Text Primary** | `#2C2416` | Body text, headings | 12.5:1 (AAA) |
| **Text Muted** | `#6B5D4D` | Secondary text, captions | 5.2:1 (AA) |
| **Text Light** | `#8B7D6B` | Tertiary text, metadata | 4.1:1 (AA) |

### Accent

| Color | Hex | Usage |
|-------|-----|-------|
| **Accent** | `#8B4513` | Primary accent, links, highlights |
| **Accent Dark** | `#5C3317` | Hover states, emphasis |
| **Accent Light** | `#A0522D` | Subtle highlights |

### Rules & Dividers

| Color | Hex | Usage |
|-------|-----|-------|
| **Rule** | `#D4C4A8` | Borders, dividers |
| **Rule Dark** | `#B8A88C` | Stronger borders |

---

## Decay States

Content ages through these visual states:

### Vivid (0-7 days)
- **Opacity:** 100%
- **Saturation:** 100%
- **Color:** Full palette
- **Animation:** Full speed
- **Z-index:** Foreground (high)

### Fading (7-14 days)
- **Opacity:** 75-85%
- **Saturation:** 60-70%
- **Color:** Desaturated
- **Animation:** 50% speed
- **Z-index:** Mid

### Dying (14-30 days)
- **Opacity:** 50-60%
- **Saturation:** 30-40%
- **Color:** Muted, grayish
- **Animation:** 25% speed
- **Z-index:** Background (low)

### Dead (30+ days)
- **Opacity:** 20-30%
- **Saturation:** 0-10%
- **Color:** Grayscale
- **Animation:** None
- **Z-index:** Deep background

---

## Implementation

### CSS Variables

```css
:root {
  --color-bg: #FDFBF7;
  --color-bg-alt: #F7F4ED;
  --color-text: #2C2416;
  --color-text-muted: #6B5D4D;
  --color-accent: #8B4513;
  
  /* Decay states */
  --decay-vivid-opacity: 1;
  --decay-fading-opacity: 0.8;
  --decay-dying-opacity: 0.55;
  --decay-dead-opacity: 0.25;
}
```

### PixiJS Color Filters

```typescript
// Apply decay filter to PixiJS sprites
const decayFilter = new ColorMatrixFilter();
const age = computeAge(publishedAt);
if (age > 30) {
  decayFilter.desaturate(0.9); // Dead: grayscale
  sprite.alpha = 0.25;
} else if (age > 14) {
  decayFilter.desaturate(0.6); // Dying
  sprite.alpha = 0.55;
} else if (age > 7) {
  decayFilter.desaturate(0.3); // Fading
  sprite.alpha = 0.8;
}
```

---

## Accessibility

- **Contrast:** All text meets WCAG AA (4.5:1) minimum
- **Color blind:** Don't rely solely on color (use icons, patterns)
- **Dark mode:** Future consideration (not in v1)

---

## Reading Mode

When reading an article, decay is **frozen**. Article appears in full color regardless of age:

- **Background:** `#FDFBF7`
- **Text:** `#2C2416` (full contrast)
- **Accent:** `#8B4513` (vivid)
- **No opacity/saturation changes**

---

## Examples

```css
/* Vivid piece */
.piece-vivid {
  opacity: var(--decay-vivid-opacity);
  filter: none;
}

/* Fading piece */
.piece-fading {
  opacity: var(--decay-fading-opacity);
  filter: saturate(0.7);
}

/* Dead piece (background layer) */
.piece-dead {
  opacity: var(--decay-dead-opacity);
  filter: grayscale(0.9);
  pointer-events: none; /* Not clickable */
}
```
