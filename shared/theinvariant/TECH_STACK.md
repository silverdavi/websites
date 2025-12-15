# The Invariant — Tech Stack Directive

*Last updated: 2024-12-14*

---

## 0) Non-negotiable Product Requirements

| Requirement | Target |
|-------------|--------|
| **Mobile-first** | No hover-only UX |
| **Performance** | 60 fps on mid-range phones for interactive layer |
| **Offline-tolerant** | Cached last issue + assets |
| **Accessibility** | Keyboard nav (non-canvas), reduced motion mode, readable type scales, color contrast |

### Two Render Modes

1. **Exploration mode** — non-linear map, scratch/reveal, playful UI
2. **Reading mode** — clean, fast, typographically stable articles

---

## 1) Framework & Runtime

| Choice | Reason |
|--------|--------|
| **Next.js (App Router)** | Routing/SEO, static output, mature deployment, image optimization |
| **TypeScript** | Type safety, better DX |

---

## 2) Rendering Strategy

| Layer | Technology | Use Case |
|-------|------------|----------|
| **DOM** | React/Next.js | Articles, nav, search, issue index, author pages, accessibility, share cards |
| **Canvas/WebGL** | PixiJS v8 | Interactive map scene (not DOM layout) |

### Interactive Engine Decision

✅ **PixiJS v8** (2D-first, collage, scratch cards, masks, particles, responsive scaling)

⏳ Optional upgrade: Three.js / React Three Fiber only if committing to 3D camera/world depth. **Do not start there.**

---

## 3) Animation

| Layer | Technology |
|-------|------------|
| **Sequences** | GSAP (scene transitions, reveals, guided tours) |
| **Micro-interactions** | CSS animations only |

---

## 4) State Management

| Concern | Solution |
|---------|----------|
| **Global state** | Zustand |
| **Persistence** | IndexedDB (Dexie) + localStorage for tiny prefs |

### State includes:
- Current issue
- Discovered nodes
- Scratch progress
- Bookmarks
- Reading progress
- Preferences (reduced motion, audio off)
- Feature flags

---

## 5) Content System

**Treat content as a graph, not pages.**

### Headless CMS

✅ **Sanity** — best mix of editor experience + structured content + portability

Alternatives: Contentful (enterprise), Strapi (self-host)

### Content Model

```
Issue
├── Node (map piece / entry point)
│   ├── → Story (article)
│   ├── → Media (photo essay, film, art)
│   ├── → Puzzle
│   ├── → CriticReview
│   ├── → LinkCard (curated web links)
│   └── → Node (relationships)
└── Relationships: Node→Story, Node→Node, Story→Story (nonlinear traversal)
```

### Build Pipeline

```
CMS → JSON → Next build-time fetch (ISR) + client fetch for live updates
```

---

## 6) Search

✅ **Meilisearch** — fast, great DX

Alternative: Algolia (paid, polished)

### Index fields:
- Titles, tags, authors, issue, excerpts, entities

---

## 7) Styling + Design System

| Layer | Technology | Status |
|-------|------------|--------|
| **Utility CSS** | Tailwind CSS | ✅ Configured |
| **Components** | shadcn/ui (dialogs, toggles, inputs only) | ✅ Installed |
| **Typography** | @tailwindcss/typography (for articles) | ✅ Installed |
| **Fonts** | Google Fonts (Playfair Display, Cormorant Garamond, Source Sans 3) | ✅ Configured |

⚠️ **Never let shadcn/ui style the "vibe" layer** — only boring UI elements.

### Installed Packages
- ✅ `shadcn/ui` — Button, Card components
- ✅ `@tailwindcss/typography` — Beautiful article typography
- ✅ `class-variance-authority` — Component variants
- ✅ `clsx` + `tailwind-merge` — Class utilities
- ✅ `lucide-react` — Icons
- ✅ `@radix-ui/react-slot` — Radix primitives

See `PACKAGES_SETUP.md` for usage examples.

---

## 8) Media Pipeline

| Media | Strategy |
|-------|----------|
| **Images** | next/image + AVIF/WebP, responsive sizes, blur placeholders |
| **Video** | Embed + progressive poster images; avoid heavy autoplay |
| **Audio** | Web Audio API + small ambient loops (optional) |
| **Preload** | Issue manifest + staged asset loading |

---

## 9) Performance & Quality Gates

### Budgets
- JS bundle per route
- Texture memory for Pixi scene
- Max concurrent animations

### Tooling

| Purpose | Tool |
|---------|------|
| Performance audits | Lighthouse CI |
| Error tracking | Sentry |
| Analytics | PostHog or Plausible (privacy-respecting) |

### Feature toggles
- Low-power mode: disable heavy shaders, reduce particles

---

## 10) Deployment

| Aspect | Choice |
|--------|--------|
| **Backend** | EC2 (Node.js + Postgres + Meilisearch) |
| **Frontend** | Static, served from EC2 or S3+CloudFront |
| **Assets** | S3 + CloudFront CDN |
| **Deploy** | CLI scripts (`aws s3 sync`, `rsync`, or GitHub Actions) |

**No Vercel. All AWS. Full CLI control.**

---

## 11) Testing

| Type | Tool |
|------|------|
| Unit | Vitest |
| E2E | Playwright |
| Visual regression | Playwright screenshots |

---

## Decision Summary (Locked)

| Category | Choice |
|----------|--------|
| Framework | Next.js (static export) or Vite + React |
| CMS | Sanity (or flat JSON files) |
| Interactive | PixiJS v8 |
| Animation | GSAP |
| State | Zustand + IndexedDB |
| Styling | Tailwind + shadcn/ui |
| Search | Meilisearch (on EC2) |
| Backend | EC2 (Node.js + Postgres) |
| Frontend hosting | EC2 or S3+CloudFront |
| Ops | Sentry + PostHog/Plausible |

**All AWS. CLI-managed. No Vercel.**

---

## Next Steps

1. [ ] Define **content graph schema** (Sanity schema definitions)
2. [ ] Define **map scene contract**:
   - What is a "node"?
   - How does it render?
   - How does it link?
   - How does it reveal?
3. [ ] Scaffold Next.js project with locked stack
4. [ ] Setup Sanity studio

> *"That's the piece that keeps the whole thing from becoming a one-off art project you can't ship monthly."*
