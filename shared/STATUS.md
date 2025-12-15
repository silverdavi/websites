# Website Projects — Status & Ideation

*Last updated: 2025-12-14*

---

## Quick Reference

| Site | Status | Design | Primary Color |
|------|--------|--------|---------------|
| unpop.info | ✅ Live | Light/paper | #C84B31 brick red |
| dhsilver.me | ✅ Live | Dark | #F4A261 amber |
| kernel-keys.com | ✅ Live | Light | #00D4AA teal |
| embino.com | ✅ Live | Dark/terminal | #33FF33 green |
| vax.ninja | ✅ Live | Dark/retro | #FF6B9D pink |
| freshsilver.net | ✅ Live | Light/fresh | #0EA5E9 sky blue |
| theinvariant.org | 🚧 New | Light/vintage | #8B4513 saddle brown |

---

## Shared Standards

### Tech Stack (all sites)
- **Framework:** React 19 + TypeScript
- **Build:** Vite (static output to `dist/`)
- **Styling:** CSS Modules (no Tailwind)
- **Hosting:** GitHub Pages with custom domains
- **CI/CD:** GitHub Actions

### Project Structure
```
site-name/
├── .github/workflows/deploy.yml
├── public/
│   ├── CNAME          # custom domain
│   └── favicon.svg
├── src/
│   ├── App.tsx
│   ├── App.module.css
│   ├── main.tsx
│   └── styles/global.css
├── index.html         # Vite entry (dev only)
├── package.json
├── tsconfig.json
├── vite.config.ts
└── .gitignore         # MUST include dist/
```

### GitHub Pages Deployment

⚠️ **Critical:** Two things must be configured correctly:

**1. Workflow file** (`.github/workflows/deploy.yml`):
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

**2. GitHub Pages source = "GitHub Actions"** (not "Deploy from a branch"):
- Repo → Settings → Pages → Build and deployment → Source: **GitHub Actions**
- CLI: `gh api repos/OWNER/REPO/pages -X PUT -f build_type=workflow`

**3. `.gitignore` must include `dist/`**

❌ **Common mistake:** If source is "Deploy from a branch", GitHub serves root `index.html` (Vite dev entry with `/src/main.tsx`) instead of built artifact → MIME type errors.

### DNS (Route 53)
- All 6 domains: A records → GitHub Pages IPs (`185.199.108-111.153`)
- CNAME for www → `silverdavi.github.io`
- Setup script: `shared/setup-dns.sh`

### Shared Data Files
| File | Purpose |
|------|---------|
| `shared/data/profile.json` | Professional profile (experience, publications, patents) |
| `shared/data/unpopular_science.json` | Book metadata |
| `shared/some_info/publications.txt` | ORCID export |
| `shared/some_info/patents.txt` | Patent list |
| `shared/some_info/resume-flat-reichman.tex` | CV LaTeX source |
| `shared/ABOUT.md` | Design tokens per site |

### Design Tokens by Site

| Site | Background | Text | Accent | Heading Font | Body Font |
|------|------------|------|--------|--------------|-----------|
| unpop.info | #FFFEF5 | #1A1A1A | #C84B31 | Literata | Source Serif 4 |
| dhsilver.me | #0D0D0D | #E8E8E8 | #F4A261 | Bricolage Grotesque | Geist |
| kernel-keys.com | #FAFAFA | #0A0A0A | #00D4AA | Syne | DM Sans |
| embino.com | #0C0C0C | #33FF33 | #FF6B35 | IBM Plex Sans | IBM Plex Mono |
| vax.ninja | #1a0a2e | #E8E8E8 | #FF6B9D | Press Start 2P | VT323 |
| freshsilver.net | #F8FAFC | #1E293B | #0EA5E9 | Space Grotesk | Inter |
| theinvariant.org | #FDFBF7 | #2C2416 | #8B4513 | Playfair Display | Source Sans 3 |

---

## unpop.info — Unpopular Science Book

**Status:** ✅ LIVE  
**URL:** https://unpop.info  
**Repo:** [silverdavi/unpop-site](https://github.com/silverdavi/unpop-site)

### Current State
- 50 chapters with sidenote visuals (PDF → PNG converted)
- Carousel showcasing title, summary, topics, quote, full sidenote caption
- Grid view of all chapters
- Kickstarter link: "Back on Kickstarter →" button
- Illustrator credit (J DG Hayes) in footer with avatar

### Data Sources
- `src/data/chapters.json` — parsed from LaTeX source using **pandoc**
- Original source: `/Users/davidsilver/dev/private/unpopular-science-source/`
- Script: `scripts/build_chapters_manifest.py`

### TODO / Ideas
- [ ] Add newsletter signup
- [ ] Prologue page
- [ ] About the author section
- [ ] Sample chapter full-text preview?
- [ ] Mobile carousel improvements
- [ ] Add search/filter by topic

---

## dhsilver.me — Personal Site

**Status:** ✅ LIVE  
**URL:** https://dhsilver.me  
**Repo:** [silverdavi/dhsilver-site](https://github.com/silverdavi/dhsilver-site)

### Current State
- Dark mode with subtle grain texture overlay
- Single-page scroll layout

### Sections
- **Hero:** Name, title, location, social links, stats (12 publications, 14 patents)
- **Experience:** Timeline with 6 roles (Rhea Labs, Canotera, AKA Foods, Embryonics, Apple, Intel)
- **Publications:** 10 selected papers with DOI links and role tags (Nature, PNAS, IEEE TPAMI, etc.)
- **Patents:** 14 patents grid (Apple, Intel, Embryonics, AKA Foods)
- **Projects:** Cards linking to unpop.info, kernel-keys.com, embino.com

### Data Sources
- `shared/data/profile.json` — full professional profile
- `shared/some_info/` — publications, patents, resume

### TODO / Ideas
- [ ] Add newsletter signup
- [ ] Research interests section
- [ ] Education section
- [ ] Mobile nav improvements

---

## kernel-keys.com — Consulting Site

**Status:** ✅ LIVE  
**URL:** https://kernel-keys.com  
**Repo:** [silverdavi/kernel-keys-site](https://github.com/silverdavi/kernel-keys-site)

### Current State
- Full React site with professional consulting aesthetic (light mode, Syne + DM Sans)
- Tab-based navigation: Services, Research, Ventures
- Generated images (Gemini 3 Pro): neural network hero, research area visualizations
- Rich content with clickable DOI links and patent numbers
- Contact section with ORCID/Scopus IDs

### Tabs / Sections
- **Hero:** Neural network visualization background, stats (12+ pubs, 14+ patents, 6 ventures)
- **Services:** 4 cards with detailed bullet lists (ML Engineering, Data Systems, Research Collab, Product R&D)
- **Research:** 4 areas with images + clickable publication links
  - Geometric ML & Computer Vision (IEEE TPAMI, MIDL, AIiH)
  - Behavioral & Social Research (PLOS ONE, WILTY)
  - Computational Biology (Nature, PNAS, Bioinformatics)
  - Food Technology (4 patents with Google Patents links)
- **Ventures:** 6 venture cards + full patent portfolio organized by company
  - Rhea Labs, Canotera, AKA Foods, Embryonics, Unpopular Science, Autonomous Food Systems
  - 14 patents with clickable links (Intel, Apple, Embryonics, AKA Foods)
- **Contact:** Email CTA, ORCID/Scopus IDs, social links
- **Footer:** Logo, copyright

### Generated Assets
- `hero_neural.png` — Neural network/knowledge graph visualization (hero background)
- `research_geometric.png` — Geometric ML/manifold wireframe
- `research_social.png` — Social network analysis graph
- `research_bio.png` — DNA/computational biology visualization
- `research_food.png` — Molecular gastronomy/chemistry visualization
- `venture_isometric.png` — Isometric interconnected systems (ventures banner)

### Image Generation
- Script: `shared/KERNELKEYS/generate_kernel_images.py`
- Run from: `shared/SBIR/code/` (uses venv and .env with GOOGLE_API_KEY)
- Model: `gemini-3-pro-image-preview`

### Strategic Purpose
Site establishes breadth of business activities for legitimacy:
- Media/behavioral research → justifies streaming/TV expenses
- Food technology → justifies ingredient/equipment expenses
- Science communication → justifies educational material expenses
- All with real DOI links and patent numbers as evidence

### TODO / Ideas
- [ ] Add case study cards with metrics
- [ ] Newsletter signup
- [ ] Client testimonials (if available)

---

## embino.com — Tiny SLM Hardware Project

**Status:** ✅ LIVE  
**URL:** https://embino.com  
**Repo:** [silverdavi/embino-site](https://github.com/silverdavi/embino-site)

### Current State
- Full React site with terminal aesthetic (dark mode, IBM Plex Mono, green on black)
- Single-page scroll-snap layout with 7 sections
- Generated images (Gemini 3 Pro): hero circuit, ESP32 product shot, breadboard prototype
- Custom generated icons (green line art, transparent backgrounds)
- Scroll-snap pagination with proximity snapping
- Animated scroll arrows on every section (↓ down, ↑ back to top on last)

### Sections
- **Hero:** Logo with blinking cursor, circuit trace background, CTA
- **Problem:** 4 pain points (C/C++, Memory, Timing, Intent)
- **Solution:** Pipeline visual with custom icons (Human → DSL → Bytecode → MCU)
- **How It Works:** 3 cards (Language, Translator, Runtime) with code example
- **Specs:** Datasheet-style table + ESP32 photo
- **Use Cases:** Smart lighting, Sensor alerts, Robot behavior (custom icons)
- **Signup:** Email waitlist form
- **Footer:** Links to dhsilver.me, kernel-keys.com

### Generated Assets
- `hero_circuit.png` — Abstract circuit traces (hero background)
- `esp32_hero.png` — Photorealistic ESP32 board
- `breadboard_prototype.png` — Maker workbench photo
- `icon_*.png` — 7 custom icons (write, gear, package, plug, lightbulb, thermometer, robot)

### TODO / Ideas
- [ ] Connect waitlist form to Formspree/actual backend
- [ ] Add dev log / blog section
- [ ] Demo videos / GIFs
- [ ] More generated images (robot closeup, PCB macro)

---

## vax.ninja — Anti-Vaxxer Satire Game

**Status:** ✅ LIVE (landing page)  
**URL:** https://vax.ninja  
**Repo:** [silverdavi/vax-ninja-site](https://github.com/silverdavi/vax-ninja-site)

### Current State
- Landing page with game concept teaser
- Disease level previews (COVID-19, Measles, Polio, Smallpox, Tetanus, Whooping Cough)
- Satirical messaging with pro-vaccine disclaimer
- Retro arcade aesthetic with scanlines and flicker effects

### Concept
A satirical Pacman-style game where you play as an anti-vaxxer running from a doctor trying to vaccinate you. Goal: catch diseases before getting vaccinated. Each disease adds debuffs:

- **COVID-19:** Need O₂ packs every round
- **Measles:** Vision blur effect
- **Polio:** Speed -50%
- **Smallpox:** One-hit KO
- **Tetanus:** Random freeze
- **Whooping Cough:** Can't stop moving

### Design
- Dark retro aesthetic with scanlines
- Fonts: Press Start 2P (headings), VT323 (body)
- Colors: Purple/pink/neon (#1a0a2e bg, #FF6B9D accent, #39FF14 virus green)

### TODO / Ideas
- [ ] Build actual game engine (Canvas/WebGL)
- [ ] Level progression system
- [ ] Sound effects and music
- [ ] High score leaderboard
- [ ] Mobile controls

---

## freshsilver.net — Travel Plans & Blog

**Status:** ✅ LIVE  
**URL:** https://freshsilver.net  
**Repo:** [silverdavi/freshsilver-site](https://github.com/silverdavi/freshsilver-site)

### Current State
- Featured trip: Israel New Year's 2025-2026 (Dec 29 – Jan 2)
- Day-by-day itinerary with events, times, and locations
- Countdown to departure (auto-updates to "Currently traveling" / "Trip complete")
- Trip highlights section (NYE Karaoke, Snooker, Family)
- Clickable map links for locations

### Current Trip: Israel NYE 2025
| Day | Route | Highlights |
|-----|-------|------------|
| Dec 29 | JFK → TLV | ✈️ Flight LY10 |
| Dec 30 | Safed → Haifa | 👨‍👩‍👧 Family, 🍻 Irrelevant Group |
| Dec 31 | Haifa → Tel Aviv | 🎱 Dan Snooker Club, 🎤 BitBox Karaoke (13 friends) |
| Jan 1 | Central → Airport | 👤 Visits (Amos, Rafi, Perl), ✈️ Flight home |
| Jan 2 | JFK → Home | 🛬 Land, rest |

### Data Sources
- `rawplan/rawplan.tsv` — Trip itinerary spreadsheet
- `rawplan/karaoke.txt` — BitBox booking confirmation (Hebrew)

### Design
- Light, fresh, modern aesthetic
- Fonts: Space Grotesk (headings), Inter (body)
- Colors: Sky blue accent (#0EA5E9), clean whites and grays

### TODO / Ideas
- [ ] Photo gallery component
- [ ] Blog/story pages per trip
- [ ] Map visualization
- [ ] Share links for friends
- [ ] Past trips archive

---

## theinvariant.org — Ideas Magazine

**Status:** 🚧 NEW (planning)  
**URL:** https://theinvariant.org  
**Repo:** [silverdavi/theinvariant-site](https://github.com/silverdavi/theinvariant-site)

> ⚠️ **Different tech stack** — see `shared/theinvariant/TECH_STACK.md`

### Tech Stack (unique to this site)

| Layer | Choice |
|-------|--------|
| Framework | Next.js (App Router) + TypeScript |
| CMS | Sanity |
| Interactive | PixiJS v8 (map, scratch/reveal) |
| Animation | GSAP |
| State | Zustand + IndexedDB |
| Styling | Tailwind + shadcn/ui |
| Search | Meilisearch (on EC2) |
| Backend | EC2 (Node.js + Postgres) |
| Frontend | Static (EC2 or S3+CloudFront) |

### Concept
A magazine exploring "constants amidst chaos" — science, philosophy, culture. Two modes:
1. **Exploration mode** — interactive map, scratch/reveal, playful discovery
2. **Reading mode** — clean, fast, typographically stable articles

### Design
- Light, warm, vintage aesthetic with cream background (#FDFBF7)
- Fonts: Playfair Display (display), Cormorant Garamond (headings), Source Sans 3 (body)
- Colors: Saddle brown accent (#8B4513), deep charcoal text (#2C2416)
- Mobile-first, 60fps target, offline-tolerant

### Content Model (Graph)
- `Issue` → `Node` → `Story` | `Media` | `Puzzle` | `CriticReview` | `LinkCard`
- Nonlinear traversal via relationships

### TODO
- [ ] Define content graph schema (Sanity)
- [ ] Define map scene contract (node rendering, linking, revealing)
- [ ] Scaffold Next.js project
- [ ] Setup Sanity studio
- [ ] Setup Vercel + DNS
