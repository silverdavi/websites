# The Invariant — Design Directives Library

*Last updated: 2024-12-14*

---

## Purpose

This library contains all design, editorial, and technical directives for The Invariant. Each directive includes metadata: **who** created it, **when**, and **why**.

Directives are versioned and can be superseded. Check the status in each file.

---

## Structure

### Design Directives

| File | Purpose | Status |
|------|---------|--------|
| [typography.md](./design/typography.md) | Font choices, scales, hierarchy | Active |
| [color.md](./design/color.md) | Palette, decay states, accessibility | Active |
| [layout.md](./design/layout.md) | Grid, spacing, responsive breakpoints | Active |
| [animation.md](./design/animation.md) | GSAP patterns, timing, easing | Active |
| [map-visual.md](./design/map-visual.md) | PixiJS rendering rules, node appearance | Active |

### Editorial Directives

| File | Purpose | Status |
|------|---------|--------|
| [tone.md](./editorial/tone.md) | Voice, constraints (references TONE_RULES.md) | Active |
| [structure.md](./editorial/structure.md) | Article format, block types | Active |
| [decay.md](./editorial/decay.md) | Lifespan rules, visual decay curves | Active |

### Technical Directives

| File | Purpose | Status |
|------|---------|--------|
| [performance.md](./technical/performance.md) | Budgets, optimization targets | Active |
| [accessibility.md](./technical/accessibility.md) | WCAG compliance, keyboard nav | Active |
| [api-contracts.md](./technical/api-contracts.md) | Backend API specifications | Active |

---

## How to Use

1. **Before making design changes:** Check relevant directive files
2. **When creating new patterns:** Document in appropriate directive file
3. **When superseding:** Mark old directive as "Superseded by [link]" and create new one
4. **Always include:** Who, when, why in directive files

---

## Version Control

Directives are tracked in git. Major changes should:
- Update the directive file
- Update this README if structure changes
- Note the change in commit message
