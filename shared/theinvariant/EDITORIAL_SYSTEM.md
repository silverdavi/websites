# The Invariant — Editorial System

*Last updated: 2024-12-14*

---

## Overview

An editorial machine, not a website.

- Continuous publishing
- Automatic aging and replacement
- Central editorial control
- Plural voices
- Stable engineering

---

## Roles

### Human

| Role | Count | Function |
|------|-------|----------|
| Editors | 7 | Accept/reject, assign, approve, freeze (one per beat) |
| Designers | ~2 | Section visual languages, interaction patterns |
| Researchers | ~3-5 | Submit raw material to intake |
| Writers | 14 | Expand accepted items into pieces (2 per beat) |

**Full crew details:** See [`CREW.md`](./CREW.md) for complete profiles of all 7 editors and 14 writers.

**Persona files:** Individual JSON personality configs in [`personas/editors/`](./personas/editors/) and [`personas/writers/`](./personas/writers/).

### AI Agents

| Agent | Scope | Model |
|-------|-------|-------|
| Per-editor agent | Each editor has one | GPT-5-mini |
| Per-writer agent | Each writer has one | GPT-5-mini |
| Supervisory agent | Shared, system-wide | GPT-5-mini |

---

## Model Usage

| Model | Purpose | Cost Tier |
|-------|---------|-----------|
| **GPT-5-nano** | Trivial checks only: typos, formatting errors, profanity, obvious policy violations | Cheapest |
| **GPT-5-mini** | Internal discussion, mentoring, outline critique, tone enforcement, consistency checks | Mid |
| **GPT-5.2** | Final synthesis only. Produces publishable text from approved inputs | Expensive |

### Usage Discipline

- Nano for gatekeeping (high volume, low stakes)
- Mini for iteration (medium volume, collaborative)
- 5.2 for finalization only (low volume, high quality)

---

## Tone & Constraint Files

Each editor and writer has a **versioned rules file** containing:

- Voice and tone limits
- Topic scope
- Forbidden patterns
- Structural expectations
- Sourcing standards
- Visual assumptions

**These are hard constraints, not suggestions.**

**Publication-wide tone rules:** See [`TONE_RULES.md`](./TONE_RULES.md) for master constraints that apply to all content.

**Individual personas:** Stored as JSON files in `personas/editors/` and `personas/writers/`, version-controlled, referenced by AI agents.

---

## Workflow

### 1. Intake & Selection

Researchers submit raw material to intake store:

```yaml
intake_item:
  sources: [urls, documents]
  summary: "Short factual summary"
  relevance: "Why this matters now"
  suggested_lifespan: 14  # days
  open_questions: ["...", "..."]
  submitted_by: "researcher_id"
  submitted_at: "2024-12-14T10:00:00Z"
```

Editors decide:

| Decision | Type |
|----------|------|
| Accept or reject | boolean |
| Section | enum |
| Lifespan | days |
| Priority | 1-5 |
| Visual weight | low/medium/high |
| Assigned writer | writer_id |

All decisions stored as structured data.

### 2. Writing & Iteration

- Writers expand accepted items
- GPT-5-mini handles iteration, critique, mentoring
- Writers submit drafts
- Editors approve and freeze content

### 3. Finalization

Approved material passed to GPT-5.2 with:

- Research (sources, facts)
- Draft (writer's work)
- Editor notes
- Tone rules (from constraint file)
- Section constraints

Outputs:

- Final text (blocks)
- Metadata
- Structural annotations

### 4. Design & Placement

Design is system-level, not per-piece:

- Section visual languages
- Interaction patterns
- Placement rules
- Decay and aging behavior

Design outputs are **declarative** — frontend interprets them.

---

## Data Model

Everything is JSON. Each piece includes:

```typescript
interface Piece {
  id: string
  
  // Content
  blocks: ContentBlock[]
  
  // Metadata
  title: string
  section: Section
  authors: string[]
  publishedAt: string  // ISO timestamp
  
  // Time behavior
  lifespan: number     // days until "dead"
  decayProfile: 'linear' | 'stepped' | 'custom'
  
  // Visual
  visualIntensity: 'low' | 'medium' | 'high'
  interactionHints: string[]
  
  // Map placement
  placementAnchors: Anchor[]
  
  // Graph
  relationships: Edge[]
}
```

---

## Backend

### Principles

- Always-on
- Simple
- Predictable
- No heavy CMS
- **Single box, full control**

### Recommended Stack: EC2 + Postgres

**One EC2 instance running 24/7.**

| Component | Choice |
|-----------|--------|
| **Compute** | EC2 t3.small or t3.medium |
| **OS** | Ubuntu 24.04 LTS |
| **Runtime** | Node.js (or Python/Go) |
| **Database** | Postgres (on same box or RDS) |
| **Search** | Meilisearch (on same box) |
| **Assets** | S3 + CloudFront |
| **Scheduler** | Cron or systemd timers |
| **Process manager** | PM2 or systemd |
| **Reverse proxy** | Caddy (auto-HTTPS) or nginx |

### Why EC2 over Lambda

| Factor | EC2 | Lambda |
|--------|-----|--------|
| Always-on workload | ✅ Flat cost | ❌ Pays per-invocation |
| Scheduled jobs (decay) | ✅ Simple cron | ⚠️ EventBridge + cold starts |
| Meilisearch | ✅ Same box | ❌ Separate service needed |
| Debugging | ✅ SSH in, tail logs | ⚠️ CloudWatch friction |
| Complexity | ✅ One thing | ❌ Many services to wire |
| Predictable cost | ✅ Fixed monthly | ⚠️ Variable |

### Responsibilities

| Function | Description |
|----------|-------------|
| Intake | Receive researcher submissions |
| Versioning | Track all edits, decisions, state changes |
| State transitions | Draft → Approved → Published → Decaying → Dead |
| Time-based decay | Cron job runs hourly/daily, updates age state |
| JSON delivery | API serves current state to frontend |
| Search index | Meilisearch updates on publish |

### API Surface

```
GET  /api/map           → Current map state (all live pieces, positions, ages)
GET  /api/piece/:id     → Single piece (full content, readable regardless of age)
GET  /api/excavate      → Dead layer (archaeology mode)
GET  /api/search?q=     → Meilisearch proxy
POST /api/intake        → Researcher submission (authenticated)
POST /api/decision/:id  → Editor decision (authenticated)
POST /api/finalize/:id  → Trigger GPT-5.2 synthesis (authenticated)
```

### Backoffice

**Full specification:** See [`BACKOFFICE.md`](./BACKOFFICE.md) for complete details.

The backoffice is a protected web interface (`/admin/*` routes) for editorial staff to manage the entire publication workflow.

**Key Features:**
- Intake Queue — View researcher submissions, accept/reject, assign to beat
- Story Manager — View all stories by status (draft/review/approved/live/dead)
- Assignment Board — Kanban-style board for assigning writers, setting lifespan, priority
- Approval Flow — Review drafts, request changes, approve for finalization
- Prompt Editor — Edit AI personalities, tone rules, constraints per editor/writer
- Analytics — Views, engagement, decay status, excavation attempts
- Version History — Full audit trail of all edits and decisions

**Tech Stack:**
- Same EC2 backend (add `/admin/*` routes)
- Auth: Simple JWT or session-based (start with hardcoded users)
- Frontend: React + Tailwind (can be same codebase, protected routes)

### Suggested Instance Sizing

| Traffic | Instance | RAM | Cost |
|---------|----------|-----|------|
| Low (dev/launch) | t3.small | 2 GB | ~$15/month |
| Moderate | t3.medium | 4 GB | ~$30/month |
| Higher | t3.large | 8 GB | ~$60/month |

Add 20-50 GB gp3 EBS storage: ~$2-4/month.

---

## Frontend Contract

| Principle | Implementation |
|-----------|----------------|
| Stable JSON schema | Frontend knows the shape, always |
| Renderer interprets age | Visual decay computed client-side from `publishedAt` + `lifespan` |
| No per-piece code changes | New content = new data, not new code |
| No redeploys for new content | Static frontend, dynamic data |

---

## Cost Estimation

### AWS Backend — EC2 Stack (Monthly)

| Service | Spec | Cost |
|---------|------|------|
| EC2 | t3.medium (4GB RAM) | ~$30 |
| EBS | 30GB gp3 | ~$2.50 |
| S3 | 50GB assets | ~$1.50 |
| CloudFront | 100GB transfer | ~$8.50 |
| Route 53 | Hosted zone + queries | ~$1 |
| **Subtotal** | | **~$45/month** |

*Meilisearch runs on the EC2 instance — no extra cost.*

### Frontend Hosting (Monthly)

| Option | Cost | Notes |
|--------|------|-------|
| **Same EC2 box** | $0 | Caddy serves static + API |
| **S3 + CloudFront** | ~$1-5 | CDN edge caching |
| **GitHub Pages** | $0 | Simple, no CLI needed |

**Recommended:** Serve from EC2. One box, one deploy.

### AI Model Usage (Monthly, Estimated)

Assuming ~50 pieces/month, 15 writers, moderate iteration:

| Model | Usage | Est. Price | Monthly Cost |
|-------|-------|------------|--------------|
| GPT-5-nano | ~500K tokens | ~$0.10/1M tokens | ~$0.05 |
| GPT-5-mini | ~2M tokens | ~$3/1M tokens | ~$6 |
| GPT-5.2 | ~200K tokens | ~$30/1M tokens | ~$6 |
| **Subtotal** | | | **~$12-25/month** |

### Sanity CMS (Monthly)

| Tier | Cost |
|------|------|
| Free | $0 (limited) |
| Team | $99/month (if needed) |

### Meilisearch (Monthly)

| Option | Cost |
|--------|------|
| On EC2 (same box) | $0 (included) |
| Meilisearch Cloud | ~$30/month |

### Total Estimated Monthly Cost

| Scenario | Backend | Frontend | AI | CMS | Total |
|----------|---------|----------|-----|-----|-------|
| **Minimal** | $45 | $0 | $15 | $0 | **~$60** |
| **Comfortable** | $60 | $5 | $30 | $0 | **~$95** |
| **Scaled** (t3.large, RDS) | $120 | $10 | $100 | $99 | **~$330** |

*Frontend $0 if served from EC2. $5-10 if using S3+CloudFront for CDN.*

---

## Result

Continuous publishing.  
Automatic aging and replacement.  
Central editorial control.  
Plural voices.  
Stable engineering.

**An editorial machine, not a website.**
