# Embino Pitch Deck

Professional 12-slide company pitch deck for Embino, designed for printing with WeasyPrint.

## Contents

- **pitch.html** — Main pitch deck (12 slides, landscape format)

## Slides

1. **Title/Hero** — Embino introduction and tagline
2. **The Problem** — Current state of MCU programming
3. **The Abstraction Gap** — Why LLMs broke the pattern
4. **The Solution** — Express intent, not implementation
5. **How It Works** — Three components (DSL, Translator, Runtime)
6. **Technical Specs** — Datasheet with performance targets
7. **Market Opportunity** — Market size and target segments
8. **Business Model** — Three-stage hardware roadmap
9. **SBIR Phase I Plan** — 12-month technical feasibility study
10. **Innovation & IP** — Technical and commercial innovation
11. **Team** — Leadership and planned technical team
12. **Call to Action** — Funding ask and contact information

## Design

- **Style:** Terminal aesthetic matching embino-site
- **Colors:** Dark mode with electric green (#33FF33) accents
- **Fonts:** Monospace (Monaco, Courier New)
- **Format:** 11" × 8.5" landscape, optimized for printing

## Usage

### Generate PDF with WeasyPrint

```bash
# Install WeasyPrint
pip install weasyprint

# Generate PDF
weasyprint pitch.html pitch.pdf

# Or with custom options
weasyprint pitch.html pitch.pdf --presentational-hints --optimize-images
```

### View in Browser

Open `pitch.html` directly in any modern browser to preview.

### Print Settings

When printing from browser:
- Layout: Landscape
- Paper: Letter (11" × 8.5")
- Margins: None
- Background graphics: On

## Customization

All content and styling is self-contained in `pitch.html`. Edit directly to:
- Update content
- Adjust colors (CSS variables at top)
- Modify layout
- Add/remove slides

## Source Material

Content derived from:
- `/shared/SBIR/about_embino.md`
- `/shared/SBIR/basic_project.md`
- `/shared/SBIR/CRITICAL_GAPS.md`
- `/embino-site/` style guide

---

**Company:** Kernel Keys LLC  
**Project:** Embino — Tiny intelligence for tiny devices  
**Website:** embino.com

