## The Invariant — Master Specification (Canonical)

This is the **single source of truth** for *The Invariant*:

- **Product thesis** (time, decay, map, archaeology)
- **Editorial machine** (simulated newsroom, roles, cadence)
- **Technical architecture** (frontend, backend, DB, orchestrator)
- **Model discipline** (GPT-5-nano / GPT-5-mini / GPT-5.2; no mocks)
- **Gemini image pipeline** (`gemini-3-pro-image-preview`)
- **AWS + Route53 + deployment** (EC2/Caddy/PM2/SSM)

It is deliberately both:
- a **magazine manifesto**, and
- an **ops/engineering runbook**.

---

## Table of contents

- 1) Product thesis
- 2) Editorial identity, tone, and old-magazine aesthetic
- 3) The simulated newsroom (crew, roles, beats)
- 4) Cadence (timers) and the 24/7 rhythm
- 5) Data model (Postgres tables and fields)
- 6) Task graph (end-to-end workflow) + payload contracts
- 7) Model strategy (exact models, parameters, guarantees)
- 8) Image generation (Gemini) end-to-end
- 9) Public API contract (what frontend relies on)
- 10) Frontend architecture (static shell + live data)
- 11) Backoffice/admin system (RBAC + dashboards)
- 12) Infrastructure (AWS + Route53) and deployment
- 13) Monitoring, debugging, and cost control
- 14) Security posture (practical)
- 15) Roadmap + “definition of done”

---

## 1) Product thesis: a living surface with enforced impermanence

### 1.1 The core premise
**The Invariant** is not “a site that publishes articles.” It is an **editorial machine** that produces a continuously-changing surface.

- There is **no issue cycle**.
- The homepage is **the present**.
- Every piece has a **lifespan**.
- The environment **decays** around pieces as they age.

### 1.2 Time is part of the UI
Pieces pass through perceptual states:

- **Vivid**: loud presence; foreground
- **Fading**: receding; less saturation/contrast/motion
- **Dying**: minimal salience; residue
- **Dead**: not deleted—**archived** and reachable via excavation

### 1.3 Reading mode stabilizes time
A key design invariant:

- The **map** shows decay.
- **Reading mode** always yields a stable, legible article regardless of age.

### 1.4 Archaeology mode
The archive exists, but not as a default tab.

- Old content is “below the surface.”
- Retrieval is intentional: “dig” or “excavate.”

---

## 2) Editorial identity: old magazine + modern energy (with strict tone rules)

### 2.1 Editorial stance
Publication-wide stance is **progressive** with:

- structural analysis over individual blame
- explicit power analysis (who benefits / who is harmed)
- global South perspectives when covering global issues
- evidence-first sourcing

The canonical publication rules live in `shared/theinvariant/TONE_RULES.md`.

### 2.2 The aesthetic
The vibe is:

- **old magazine typography** (serif-forward, editorial hierarchy)
- **vibrant modern accents** (bright palette, micro-interactions)
- **decay as design** (time is visible)

### 2.3 Design principles (non-negotiable)
- Bold, not timid
- Vibrant, not muted
- Dynamic, not static
- Varied, not uniform
- Engaging, not passive

---

## 3) The simulated newsroom: the crew and roles

### 3.1 The “living building” metaphor
The newsroom is modeled as rooms that run forever:

- **Editorial meeting room** (hourly)
- **Journalist desks** (small story hunts, 6-hour cycles)
- **Deep research pods** (major pieces, 2-day cycles)
- **Image studio** (on-demand)
- **Story queue conveyor** (FIFO)
- **Archive layer** (permanent)

### 3.2 Canonical crew (21 personas)
Canonical editorial structure (from `shared/theinvariant/CREW.md`):

- **7 editors** (one per beat)
- **14 writers** (two per beat)

Beats:

- News
- Politics
- Science
- Global
- Health
- Tech
- Social Justice

### 3.3 Editors (beat leads)
Editors have veto power and act as quality gates:

- **Miriam Cross** — News Editor
- **Theo Okonkwo** — Politics Editor
- **Dr. Elena Voss** — Science Editor
- **Amara Diallo** — Global Editor
- **Dr. James Okafor** — Health Editor
- **Sasha Kim** — Tech Editor
- **Carmen Reyes** — Social Justice Editor

Each editor has:

- a persona
- beat-specific constraints
- sourcing standards
- stylistic expectations

### 3.4 Writers (two per beat)
Writers are constrained authors:

- they must follow publication-wide tone rules
- they must follow beat and editor constraints
- they must cite real sources

### 3.5 Supervisory agent
A system-wide agent responsible for:

- cross-beat consistency
- final sanity checks
- editorial meeting assistance
- preventing drift

### 3.6 Crew reality: full cast vs. seeded/minimal cast
Two truths:

- **Canonical end-state**: 7 editors + 14 writers + supervisory agent.
- **Bootstrapping mode**: you may seed fewer personas first to validate the task graph.

The system must support both without changing the underlying philosophy.

---

## 4) Cadence (timers): the 24/7 rhythm

Timers create tasks. Tasks produce artifacts (intake items, drafts, images, queue entries). The entire newsroom is a **scheduler + queue + state machine**.

### 4.1 The four core cadences

#### (A) Hourly editorial meeting
- **Cron**: `0 * * * *`
- **Agent**: supervisory
- **Task type**: `editorial_meeting`
- **Goal**: decide whether to add ONE new story; assign it.

#### (B) Small story hunts (every 6 hours per writer)
- **Cron**: `0 */6 * * *` (staggered per writer by hour)
- **Agents**: writers
- **Task type**: `hunt_small_story`
- **Goal**: find one real, timely story pitch with real sources.

#### (C) Major piece research (every 2 days per writer)
- **Cron**: `0 9 */2 * *` (or staggered per writer)
- **Agents**: writers
- **Task type**: `research_major_piece`
- **Goal**: produce a deep pitch (multiple sources, angles, uncertainties).

#### (D) Auto-publish queue
- **Cron**: `*/10 * * * *`
- **Agent**: supervisory or system
- **Task type**: `publish_next`
- **Goal**: publish next queued story (FIFO).

### 4.2 Staggering strategy (why it matters)
Staggering prevents thundering herds:

- not all writers hunt at the same minute
- not all drafts finalize simultaneously
- image generation load is spread

Canonical approach:

- each writer is assigned a stable offset hour
- their `*/6` cycle fires at that offset

---

## 5) Data model: Postgres tables and fields (practical)

This is the schema conceptually required by the machine. Exact SQL may vary, but the **fields and meanings are the contract**.

### 5.1 `editor_profiles`
Stores editors.

- `id` (uuid)
- `name` (text)
- `beat` (text)
- `personality_config` (jsonb)
- `tone_rules` (jsonb)
- `is_active` (bool)
- `created_at`, `updated_at`

### 5.2 `writer_profiles`
Stores writers.

- `id` (uuid)
- `name` (text)
- `beat` (text)
- `assigned_editor_id` (uuid → editor_profiles)
- `personality_config` (jsonb)
- `tone_rules` (jsonb)
- `is_active` (bool)
- `created_at`, `updated_at`

### 5.3 `intake_items`
The intake queue is the raw material store.

- `id` (uuid)
- `status` (`pending`, `accepted`, `rejected`, …)
- `priority` (1–5)
- `beat` (text)
- `summary` (text)
- `relevance` (text)
- `sources` (jsonb array of {title,url,type}) — must be real URLs
- `angle` (text)
- `submitted_by` (text/uuid)
- `assigned_editor_id` (uuid)
- `created_at`, `updated_at`

### 5.4 `stories`
Canonical published artifacts.

- `id` (uuid)
- `status` (`draft`, `review`, `approved`, `queued`, `published`, `decaying`, `archived`)
- `title` (text)
- `section`/`beat` (text)
- `summary` (text)
- `blocks` (jsonb) — structured content blocks
- `authors` (jsonb)
- `intake_item_id` (uuid → intake_items)
- `assigned_writer_id` (uuid → writer_profiles)
- `assigned_editor_id` (uuid → editor_profiles)

Time/decay:

- `published_at` (timestamp)
- `lifespan_days` (int)
- `freshness` (numeric 0–100)
- `decay_rate` (numeric percent/day)
- `freshness_updated_at` (timestamp)

Queue:

- `queue_position` (int)

Media:

- `image_url` (text)
- `image_style` (jsonb)

Archive:

- `archived_at` (timestamp)

### 5.5 `agent_timers`
Defines the rhythm.

- `id` (uuid)
- `agent_type` (text)
- `agent_id` (uuid/text)
- `timer_name` (text)
- `cron_expression` (text)
- `task_type` (text)
- `task_payload` (jsonb)
- `is_active` (bool)
- `next_run_at` (timestamp)

### 5.6 `agent_tasks`
The work queue.

- `id` (uuid)
- `agent_type` (text)
- `agent_id` (text)
- `task_type` (text)
- `status` (`pending`, `running`, `completed`, `failed`)
- `priority` (int)
- `payload` (jsonb)
- `result` (jsonb)
- `error` (text)
- `created_at`, `started_at`, `completed_at`

### 5.7 Transparency tables (souls)
From `shared/theinvariant/AGENT_TRANSPARENCY.md`:

- `agent_memory`
- `agent_reasoning`
- `agent_work_history`
- `agent_state`

These tables are the “windows to their souls.”

### 5.8 `api_usage`
Tracks cost and token usage:

- model
- tokens in/out
- duration
- task context

### 5.9 `editorial_meetings`
Stores meeting logs.

- `id` (uuid)
- `meeting_time` (timestamp)
- `participants` (jsonb)
- `agenda` (jsonb)
- `decisions` (jsonb)
- `stories_considered` (jsonb)
- `story_selected` (uuid → stories.id; nullable)

Important invariant:
- `story_selected` must only reference a **story id**, never an intake id.

---

## 6) Task graph: the newsroom as a state machine

This is the “orchestrated newsroom” in concrete terms.

### 6.1 Task types (canonical)

- `editorial_meeting`
- `hunt_small_story`
- `research_major_piece`
- `review_intake`
- `write_draft`
- `critique`
- `finalize`
- `generate_story_image`
- `publish_next`
- `decay_update` (optional cron)
- `archive_story` (optional)

### 6.2 Payload contracts (examples)

#### `hunt_small_story` payload
```json
{
  "beat": "News",
  "story_type": "small",
  "target_length": "500-800 words"
}
```

#### `write_draft` payload
```json
{
  "intake_item_id": "uuid",
  "constraints": {
    "beat": "Tech",
    "tone_rules_version": "...",
    "must_include": ["power analysis", "sources"],
    "must_avoid": ["mock urls", "placeholders"]
  }
}
```

#### `finalize` payload
```json
{
  "story_id": "uuid",
  "editor_notes": "...",
  "target": "publication-ready",
  "lifespan_days": 14,
  "decay_rate": 10
}
```

#### `generate_story_image` payload
```json
{
  "story_id": "uuid",
  "style": {
    "style_category": "photorealistic",
    "mood": "urgent",
    "color_palette": "muted",
    "composition": "centered",
    "lighting": "natural",
    "editor_notes": "Focus on human element"
  },
  "aspect_ratio": "1:1",
  "size": "2K"
}
```

### 6.3 Orchestration rule (critical)
When a task completes, it should enqueue the next task **without manual intervention**.

Example chain:

- `editorial_meeting` decides “add story” → enqueue `write_draft`
- `write_draft` complete → enqueue `critique`
- `critique` approves → enqueue `finalize`
- `finalize` complete → enqueue `generate_story_image`
- `generate_story_image` complete → enqueue `publish_next` or enqueue queue-placement

This is the difference between “agents exist” and “a newsroom runs.”

---

## 7) Model strategy: exact models, parameters, and guarantees

### 7.1 Non-negotiables
- **No fallback/mock endpoints.** Real keys, real calls.
- **No pretending success.** If a call fails, log the failure and stop the transition.
- **No silent model swapping.** If a model call fails, fix the integration.

### 7.2 Model roles

#### `gpt-5-nano`
- Purpose: high-volume gatekeeping
- Examples: URL validation, profanity/policy checks, basic schema validation, decay category classification

Recommended defaults:
- temperature: 0.2
- max_tokens: ~500

#### `gpt-5-mini`
- Purpose: editorial iteration
- Examples: hunting, drafting, critique, editorial meetings

Recommended defaults:
- temperature: 0.4–0.6 (persona-dependent)
- max_tokens: task-dependent (2k–8k)

#### `gpt-5.2`
- Purpose: final synthesis
- Examples: finalization only

Recommended defaults:
- temperature: ~0.7 (controlled creativity)
- max_tokens: ~4000+ (depending on length)

### 7.3 Task → model map (canonical)
- `editorial_meeting` → `gpt-5-mini`
- `hunt_small_story` → `gpt-5-mini`
- `research_major_piece` → `gpt-5-mini`
- `review_intake` → `gpt-5-mini` (+ `gpt-5-nano` quick validations)
- `write_draft` → `gpt-5-mini`
- `critique` → `gpt-5-mini`
- `finalize` → `gpt-5.2`

---

## 8) Gemini image generation: end-to-end

### 8.1 The only image model
- Model: `gemini-3-pro-image-preview`

### 8.2 When image generation happens
- after approval/finalization
- before publishing

### 8.3 Prompt construction (high level)
The generator should:

- read story title/summary/section + key themes
- apply editor style parameters
- generate a single strong cover-style image

### 8.4 Storage and serving
Canonical storage:

- `/var/www/theinvariant/images/stories/`

Canonical serving:

- Caddy serves `/images/*` from `/var/www/theinvariant`

---

## 9) Public API contract (frontend depends on this)

### 9.1 Core endpoints
- `GET /api/map` → list of published/decaying stories with `freshness`, `is_fresh`, `image_url`
- `GET /api/piece/:id` → full story
- `GET /api/stats` → live stats, queue depth, agent counts

### 9.2 Cache policy
`/api/*` should return:

- `Cache-Control: no-cache, no-store, must-revalidate`

---

## 10) Frontend architecture (static shell + live data)

### 10.1 Philosophy
Frontend is a static magazine surface that **reads live state** from the backend.

- static export for cheap hosting
- client-side fetch + polling for “living” updates

### 10.2 Rendering expectations
Story cards must show:

- title
- section/beat
- author(s)
- image (or placeholder)
- freshness indicator

---

## 11) Backoffice/admin system

### 11.1 Purpose
The backoffice is the human control panel.

- intake triage
- assignment
- approvals
- monitoring agent tasks/timers
- transparency (“souls”)

### 11.2 Roles and RBAC
- Admin
- Editor
- Writer
- Researcher

---

## 12) Infrastructure: AWS + Route53 + deployment (concrete)

### 12.1 Canonical AWS resources (recorded)
- EC2: `i-0e583442c9eaf880b` (t3.medium)
- VPC: `vpc-06490f5558ca66f6f`
- SG: `sg-04208b2d83649704d`
- Route53 zone: `Z02787152ZSPM0AK00U9X`
- API IP (when running): `3.95.34.98` (changes on restart without EIP)
- IAM role: `theinvariant-ec2-role`
- SSM params:
  - `/theinvariant/openai-api-key`
  - `/theinvariant/google-api-key`

### 12.2 DNS mapping
- `theinvariant.org` → GitHub Pages
- `www.theinvariant.org` → GitHub Pages CNAME
- `api.theinvariant.org` → EC2 IP

### 12.3 On-server layout
- frontend: `/var/www/theinvariant/frontend/`
- backend: `/var/www/theinvariant/backend/`
- images: `/var/www/theinvariant/images/stories/`

### 12.4 Caddy responsibilities
- terminate TLS
- serve static frontend
- reverse proxy `/api/*` → `localhost:3000`

### 12.5 PM2 responsibilities
- keep backend alive
- restart on crash
- provide logs

### 12.6 Deployment flow
- build frontend
- rsync frontend
- rsync backend (exclude `.env`)
- `npm install --production`
- restart pm2

---

## 13) Monitoring, debugging, and cost control

### 13.1 What to watch
- queue depth
- task failures by type
- image generation error rate
- API latency
- token spend per model

### 13.2 “pause posture” (cost control)
- stopping EC2 stops compute spend
- EBS storage remains (keeps data)

---

## 14) Security posture

Minimum viable:

- lock down admin routes
- protect secrets (SSM or `.env` with strict perms)
- parameterized SQL
- audit logs

---

## 15) Roadmap + definition of done

### 15.1 Definition of done (system)
- tasks chain automatically end-to-end
- no mocks/fallbacks
- every published story has an image
- newsroom runs unattended

### 15.2 Definition of done (experience)
- site feels alive
- decay is legible
- reading mode is timeless
- archive is archaeology

---

## Appendix A: Where the detailed source docs live

All details were originally specified across these repo docs:

- `shared/theinvariant/CONCEPT.md`
- `shared/theinvariant/CREW.md`
- `shared/theinvariant/NEWSROOM_WORKFLOW.md`
- `shared/theinvariant/LIVING_WEBSITE_WORKFLOW.md`
- `shared/theinvariant/TONE_RULES.md`
- `shared/theinvariant/GPT_MODELS_SETUP.md`
- `shared/theinvariant/BACKOFFICE.md`
- `shared/theinvariant/DYNAMIC_PUBLISHING.md`
- `shared/theinvariant/FRESHNESS_SYSTEM.md`
- `shared/theinvariant/DEPLOYMENT_WORKFLOW.md`
- `shared/theinvariant/infrastructure/DEPLOYMENT.md`
