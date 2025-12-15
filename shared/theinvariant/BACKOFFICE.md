# The Invariant — Backoffice Specification

*Last updated: 2024-12-14*

---

## Overview

The backoffice is a protected web interface for editorial staff to manage the entire publication workflow. It runs on the same EC2 backend as the public API, with authentication and protected routes.

**URL:** `https://theinvariant.org/admin` (or subdomain: `admin.theinvariant.org`)

---

## Authentication

### Initial Implementation

- Simple session-based auth (JWT tokens)
- Hardcoded user list in environment variables
- Role-based access:
  - **Admin**: Full access
  - **Editor**: Beat-specific access + intake queue
  - **Writer**: View assigned pieces, submit drafts
  - **Researcher**: Submit intake items only

### Future

- OAuth integration (Google Workspace)
- Multi-factor authentication
- Audit logging of all admin actions

---

## Routes & Features

### 1. Dashboard (`/admin`)

**Overview metrics:**
- Live pieces count (by age: vivid/fading/dying/dead)
- Intake queue size
- Pending approvals
- Recent activity feed
- System health (API, database, Meilisearch)

**Quick actions:**
- Jump to intake queue
- View urgent approvals
- System settings

---

### 2. Intake Queue (`/admin/intake`)

**View:**
- Table/list of all researcher submissions
- Filters: status (pending/reviewed/accepted/rejected), beat, date
- Sort: newest first, priority

**Actions per item:**
- **Accept** → Opens assignment modal
- **Reject** → Add reason, archive
- **View details** → Full submission, sources, suggested lifespan

**Assignment modal:**
- Select beat
- Select writer
- Set priority (1-5)
- Set lifespan (days)
- Set visual weight (low/medium/high)
- Add editor notes

**Bulk actions:**
- Accept multiple
- Assign to beat
- Archive rejected

---

### 3. Story Manager (`/admin/stories`)

**Views:**
- **All stories** (default)
- **By status**: Draft / In Review / Approved / Live / Dead
- **By beat**: News / Politics / Science / Global / Health / Tech / Social Justice
- **By writer**: Filter by assigned writer
- **By editor**: Filter by approving editor

**Story card/list item shows:**
- Title, beat, status badge
- Writer, editor
- Age (if live): "3 days old" → "vivid"
- Priority, visual weight
- Last updated timestamp
- Quick actions: Edit, View, Approve, Reject

**Actions:**
- **View** → Full story view with version history
- **Edit** → Inline editing (if draft)
- **Approve** → Move to finalization queue
- **Reject** → Return to writer with notes
- **Change assignment** → Reassign writer/editor
- **Set lifespan** → Adjust decay timeline
- **Archive** → Mark as dead manually

**Search:**
- Full-text search across titles, content, metadata
- Powered by Meilisearch

---

### 4. Assignment Board (`/admin/assignments`)

**Kanban-style board:**
- Columns: Unassigned / Assigned / In Progress / Review / Approved / Live

**Drag-and-drop:**
- Move stories between columns
- Reassign writers by dragging to different beat lanes

**Filters:**
- By beat (horizontal lanes)
- By priority
- By deadline

**Bulk operations:**
- Assign multiple to writer
- Set priority/lifespan for multiple
- Batch approve

---

### 5. Approval Flow (`/admin/approvals`)

**Queue view:**
- Stories awaiting editor approval
- Grouped by editor (beat)
- Shows draft, writer notes, editor notes

**Review interface:**
- Side-by-side: draft on left, editor panel on right
- Editor can:
  - Request changes (add notes, return to writer)
  - Approve (moves to finalization)
  - Reject (with reason)
- Version history visible
- AI suggestions (GPT-5-mini) for tone/consistency

**Approval criteria checklist:**
- Tone matches beat
- Sources cited
- Structural expectations met
- No forbidden patterns
- Sourcing standards met

---

### 6. Prompt Editor (`/admin/prompts`)

**Persona management:**
- List all editors and writers
- Edit personality configs
- Edit tone rules
- Version history of changes

**Editor interface:**
- **Personality tab:**
  - Voice (dropdown: analytical, passionate, sardonic, etc.)
  - Perspective (systemic, personal, institutional)
  - Temperature (slider: 0.3-0.9)
  - Constraints (textarea: forbidden patterns, required framings)
- **Tone rules tab:**
  - Must include (list)
  - Must avoid (list)
  - Sourcing standards (textarea)
  - Structural expectations (textarea)
- **Preview tab:**
  - Test prompt with sample content
  - See AI response

**Bulk operations:**
- Apply tone rules to all writers in beat
- Copy personality from one to another
- Reset to defaults

**Version control:**
- View history of changes
- Rollback to previous version
- Compare versions side-by-side

---

### 7. Analytics (`/admin/analytics`)

**Metrics dashboard:**
- **Engagement:**
  - Views per piece (live pieces)
  - Time on page
  - Excavation attempts (dead pieces accessed)
  - Search queries
- **Editorial:**
  - Pieces published per day/week/month
  - Average lifespan
  - Decay distribution (how many in each state)
  - Beat distribution
- **Performance:**
  - API response times
  - Frontend load times
  - Error rates

**Visualizations:**
- Line chart: pieces published over time
- Pie chart: pieces by beat
- Bar chart: pieces by age state
- Heatmap: engagement by time of day

**Export:**
- CSV export of all metrics
- PDF reports (weekly/monthly)

---

### 8. Version History (`/admin/history`)

**Audit log:**
- All actions on all pieces
- Filterable by:
  - Piece ID
  - Actor (editor/writer/admin)
  - Action type
  - Date range

**Action types:**
- `created` - Piece created from intake
- `edited` - Content changed
- `assigned` - Writer/editor assigned
- `approved` - Editor approved
- `rejected` - Editor rejected
- `published` - Went live
- `lifespan_changed` - Decay timeline adjusted
- `archived` - Manually marked dead

**View:**
- Timeline view (chronological)
- Diff view (what changed)
- Actor attribution
- Timestamp (ISO)

**Search:**
- Full-text search across all log entries

---

## Data Model

### Backend API Routes

```
GET    /admin/dashboard          → Overview metrics
GET    /admin/intake             → Intake queue
POST   /admin/intake/:id/accept  → Accept and assign
POST   /admin/intake/:id/reject  → Reject with reason
GET    /admin/stories             → All stories (filtered)
GET    /admin/stories/:id        → Single story with history
PUT    /admin/stories/:id        → Update story
POST   /admin/stories/:id/approve → Approve for finalization
POST   /admin/stories/:id/reject  → Reject with notes
GET    /admin/assignments         → Assignment board data
PUT    /admin/assignments/:id     → Update assignment
GET    /admin/approvals           → Approval queue
GET    /admin/prompts             → All personas
GET    /admin/prompts/:id        → Single persona
PUT    /admin/prompts/:id         → Update persona
GET    /admin/analytics           → Analytics data
GET    /admin/history             → Audit log
POST   /admin/auth/login          → Login
POST   /admin/auth/logout         → Logout
GET    /admin/auth/me             → Current user
```

### Database Schema Additions

```sql
-- Editor profiles
CREATE TABLE editor_profiles (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  beat VARCHAR(50) NOT NULL,
  personality_config JSONB,
  tone_rules JSONB,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Writer profiles
CREATE TABLE writer_profiles (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  beat VARCHAR(50) NOT NULL,
  assigned_editor_id UUID REFERENCES editor_profiles(id),
  personality_config JSONB,
  tone_rules JSONB,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Audit log
CREATE TABLE audit_log (
  id UUID PRIMARY KEY,
  piece_id UUID REFERENCES pieces(id),
  action VARCHAR(50) NOT NULL,
  actor_id UUID NOT NULL,
  actor_type VARCHAR(20) NOT NULL, -- 'editor', 'writer', 'admin'
  timestamp TIMESTAMP DEFAULT NOW(),
  diff JSONB,
  notes TEXT
);

CREATE INDEX idx_audit_log_piece ON audit_log(piece_id);
CREATE INDEX idx_audit_log_actor ON audit_log(actor_id);
CREATE INDEX idx_audit_log_timestamp ON audit_log(timestamp DESC);
```

---

## UI/UX Guidelines

### Design System

- **Framework**: React + Tailwind CSS
- **Components**: shadcn/ui for dialogs, tables, forms
- **Theme**: Dark mode (editorial staff work long hours)
- **Typography**: Same as public site (Playfair Display, Cormorant Garamond, Source Sans 3)

### Layout

- **Sidebar navigation** (always visible)
- **Top bar** (user info, notifications, search)
- **Main content area** (responsive grid)

### Responsive

- Desktop-first (editors work on laptops/desktops)
- Tablet support for mobile editing
- Touch-friendly drag-and-drop

### Performance

- Lazy load story content
- Virtual scrolling for long lists
- Optimistic UI updates
- Real-time updates via WebSocket (future)

---

## Security

### Access Control

- All `/admin/*` routes require authentication
- Role-based permissions (RBAC)
- Beat-specific access (editors only see their beat)

### Data Protection

- HTTPS only
- Input sanitization
- SQL injection prevention (parameterized queries)
- XSS prevention (React's built-in escaping)

### Audit Trail

- All actions logged
- Immutable audit log (append-only)
- Regular backups

---

## Future Enhancements

- [ ] Real-time collaboration (multiple editors on same piece)
- [ ] Comment threads on pieces
- [ ] AI-powered suggestions (tone, structure, sources)
- [ ] Mobile app (React Native)
- [ ] Email notifications for assignments/approvals
- [ ] Slack/Discord integration
- [ ] Advanced analytics (cohort analysis, retention)
- [ ] A/B testing for headlines/lifespans
