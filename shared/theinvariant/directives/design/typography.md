# Directive: Typography

**Created by:** Design Team  
**Date:** 2024-12-14  
**Why:** Establish consistent, readable typography that supports both exploration and reading modes. Vintage magazine aesthetic with modern readability.  
**Status:** Active

---

## Font Stack

### Display (Headlines, Masthead)
- **Primary:** Playfair Display
- **Fallback:** Georgia, serif
- **Usage:** Hero titles, section headers, masthead logo
- **Weights:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **Style:** Elegant, editorial, vintage

### Headings
- **Primary:** Cormorant Garamond
- **Fallback:** Georgia, serif
- **Usage:** Article titles, subsection headers
- **Weights:** 400 (regular), 500 (medium), 600 (semibold)
- **Style:** Refined, readable, classic

### Body
- **Primary:** Source Sans 3
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif
- **Usage:** Body text, captions, UI elements
- **Weights:** 300 (light), 400 (regular), 500 (medium), 600 (semibold)
- **Style:** Clean, modern, accessible

---

## Type Scale

### Desktop

| Element | Size | Line Height | Font Family | Weight |
|---------|------|-------------|-------------|--------|
| Hero Title | 4rem (64px) | 1.1 | Playfair Display | 400 |
| H1 | 3.5rem (56px) | 1.2 | Cormorant Garamond | 500 |
| H2 | 2.5rem (40px) | 1.2 | Cormorant Garamond | 500 |
| H3 | 1.75rem (28px) | 1.3 | Cormorant Garamond | 500 |
| H4 | 1.25rem (20px) | 1.4 | Cormorant Garamond | 600 |
| Body | 1.125rem (18px) | 1.7 | Source Sans 3 | 400 |
| Small | 0.875rem (14px) | 1.6 | Source Sans 3 | 400 |
| Caption | 0.75rem (12px) | 1.5 | Source Sans 3 | 400 |

### Mobile

| Element | Size | Line Height |
|---------|------|-------------|
| Hero Title | 2.5rem (40px) | 1.1 |
| H1 | 2rem (32px) | 1.2 |
| H2 | 1.75rem (28px) | 1.2 |
| H3 | 1.5rem (24px) | 1.3 |
| Body | 1rem (16px) | 1.7 |

---

## Hierarchy Rules

1. **Maximum 3 font sizes per page** (excluding UI elements)
2. **Headings:** Use semantic HTML (h1-h6), never style divs as headings
3. **Contrast:** Minimum 4.5:1 for body text, 3:1 for large text (WCAG AA)
4. **Line length:** 45-75 characters for body text
5. **Spacing:** Use consistent vertical rhythm (multiples of 0.5rem)

---

## Reading Mode Specifics

- **Article titles:** H1, Playfair Display, 2.5rem
- **Body paragraphs:** 1.125rem, Source Sans 3, max-width 720px
- **Pull quotes:** 1.5rem, Cormorant Garamond, italic
- **Captions:** 0.875rem, Source Sans 3, color: muted

---

## Map Mode Specifics

- **Node labels:** 0.875rem, Source Sans 3, bold
- **UI text:** 0.875rem, Source Sans 3, regular
- **Legends:** 0.75rem, Source Sans 3, regular

---

## Examples

```css
/* Hero title */
.hero-title {
  font-family: var(--font-display);
  font-size: 4rem;
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

/* Article body */
.article-body {
  font-family: var(--font-body);
  font-size: 1.125rem;
  line-height: 1.7;
  max-width: 720px;
}
```

---

## Font Loading

- **Strategy:** Self-hosted, preload critical fonts
- **Format:** WOFF2 (modern), WOFF (fallback)
- **Subset:** Latin-1 extended (covers most content)

---

## Accessibility

- **Minimum size:** 16px (1rem) for body text
- **Scalable:** All sizes use rem units (respects user zoom)
- **Reduced motion:** Respects `prefers-reduced-motion` for animations
