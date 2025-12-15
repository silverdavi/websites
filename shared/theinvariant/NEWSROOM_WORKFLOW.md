# The Invariant — Newsroom Workflow Plan
## "A Living Building, 24/7"

*Last updated: 2024-12-14*

---

## 🏢 The Building Metaphor

Think of this as a **physical newsroom floor** that never sleeps:

- **Editorial Meeting Room** (Hourly) - All editors and writers gather
- **Journalist Desks** (6-hour cycles) - Each writer hunts for small stories
- **Deep Research Pods** (2-day cycles) - Major investigative pieces
- **Image Studio** (On-demand) - Visual creation when stories are approved
- **Story Queue** (FIFO) - Stories flow through like a conveyor belt
- **Archive** (Permanent) - Nothing is deleted, everything is accessible

---

## ⏰ The Rhythm: Human-Like but Continuous

### 1. **Editorial Meetings** (Every 1 Hour)
**Location:** Virtual meeting room  
**Participants:** All editors + all writers  
**Duration:** ~15 minutes (simulated)

**What Happens:**
1. Review current story queue status
2. Discuss what's trending/breaking
3. **Decide: Should we add ONE new story?**
4. If yes: Select highest-priority intake item
5. Assign to appropriate writer
6. Set deadline and priority

**Implementation:**
- Timer: `0 * * * *` (every hour at :00)
- Task Type: `editorial_meeting`
- Creates: `consider_new_story` task for supervisory agent

---

### 2. **Small Story Hunt** (Every 6 Hours)
**Location:** Each journalist's desk  
**Participants:** Individual writers  
**Duration:** ~30 minutes per writer

**What Happens:**
1. Writer scans their beat for quick stories
2. Checks news feeds, social signals, trending topics
3. Identifies ONE small story (500-800 words)
4. Submits to intake queue
5. Editor reviews in next meeting

**Implementation:**
- Timer: `0 */6 * * *` (every 6 hours)
- Task Type: `hunt_small_story`
- Creates: `intake_submission` task for each writer

**Writers:**
- Dana Reyes (News) - 00:00, 06:00, 12:00, 18:00
- Jalen Brooks (News) - 01:00, 07:00, 13:00, 19:00
- Priya Sharma (Politics) - 02:00, 08:00, 14:00, 20:00
- Marcus Webb (Politics) - 03:00, 09:00, 15:00, 21:00
- ... (staggered across all 14 writers)

---

### 3. **Major Piece Research** (Every 2 Days)
**Location:** Deep research pods  
**Participants:** Individual writers  
**Duration:** ~4-6 hours per writer

**What Happens:**
1. Writer identifies a major story opportunity
2. Deep research and investigation
3. Multiple source verification
4. Draft comprehensive piece (2000-4000 words)
5. Submit for editorial review

**Implementation:**
- Timer: `0 9 */2 * *` (every 2 days at 9 AM)
- Task Type: `research_major_piece`
- Creates: `deep_research` task for each writer

**Schedule:**
- Day 1: News, Politics, Science writers
- Day 2: Global, Health, Tech, Social Justice writers
- Alternates every 2 days

---

## 📋 Story Queue System (FIFO + Archive)

### Queue Structure

```
┌─────────────────────────────────────┐
│  PUBLISHING QUEUE (FIFO)            │
│  ────────────────────────────────    │
│  [Story 1] → [Story 2] → [Story 3]  │
│  (Newest at end, oldest at front)   │
└─────────────────────────────────────┘
           ↓ (when published)
┌─────────────────────────────────────┐
│  ACTIVE FEED                        │
│  ────────────────────────────────    │
│  All published stories               │
│  (Sorted by: published_at DESC)      │
│  (Decay applied visually)            │
└─────────────────────────────────────┘
           ↓ (after lifespan)
┌─────────────────────────────────────┐
│  ARCHIVE                            │
│  ────────────────────────────────    │
│  All stories (never deleted)        │
│  (Searchable, accessible)            │
│  (Status: 'archived')                │
└─────────────────────────────────────┘
```

### Story States

1. **`draft`** - Writer working on it
2. **`review`** - Editor reviewing
3. **`approved`** - Ready to publish
4. **`queued`** - In publishing queue (FIFO)
5. **`published`** - Live on site
6. **`decaying`** - Past prime, fading visually
7. **`archived`** - Moved to archive (still accessible)

### Queue Management

- **New stories** added to END of queue
- **Oldest approved story** publishes next
- **Published stories** stay in feed (with decay)
- **Archived stories** remain searchable forever

---

## 🎨 Image Generation System

### Using Gemini 3 Pro Preview

**Model:** `gemini-3-pro-image-preview` (ONLY model for images)

**When Images Are Generated:**
1. Story approved by editor
2. Editor specifies visual style
3. Image generated before publishing
4. Stored with story metadata

### Visual Style Decision

**Editor's Role:**
- Reviews story content
- Determines visual mood/tone
- Selects style category:
  - `photorealistic` - News/documentary style
  - `illustrative` - Conceptual/abstract
  - `minimalist` - Clean, simple
  - `vintage` - Retro aesthetic
  - `bold` - High contrast, dramatic
  - `subtle` - Soft, understated

**Style Parameters:**
```json
{
  "style_category": "photorealistic",
  "mood": "urgent",
  "color_palette": "muted",
  "composition": "centered",
  "lighting": "natural",
  "editor_notes": "Focus on human element"
}
```

### Image Generation Flow

1. **Editor approves story** → Sets visual style
2. **Task created:** `generate_story_image`
3. **Image generator service:**
   - Reads story title, summary, key themes
   - Applies editor's style parameters
   - Calls Gemini 3 Pro Preview API
   - Generates image (2K resolution, 1:1 aspect)
   - Stores in S3/CloudFront
   - Updates story metadata with image URL

### Implementation

**Service:** `backend/services/imageGenerator.js`
- Uses Google GenAI client (like RecipeDjerba)
- Reads `GOOGLE_API_KEY` from env
- Generates based on story content + editor style
- Stores images in `/var/www/theinvariant/images/stories/`

---

## 🤖 Agent Tasks & Timers

### Timer Definitions

```javascript
// Editorial Meeting (Every Hour)
{
  agent_type: 'supervisory',
  agent_id: 'supervisory-001',
  timer_name: 'Editorial Meeting - Hourly',
  cron_expression: '0 * * * *',  // Every hour at :00
  task_type: 'editorial_meeting',
  task_payload: {
    meeting_type: 'hourly',
    agenda: ['review_queue', 'consider_new_story', 'assign_priorities']
  }
}

// Small Story Hunt (Every 6 Hours, per writer)
{
  agent_type: 'writer',
  agent_id: writer.id,
  timer_name: `Small Story Hunt - ${writer.name}`,
  cron_expression: '0 */6 * * *',  // Every 6 hours
  task_type: 'hunt_small_story',
  task_payload: {
    story_type: 'small',
    target_length: '500-800 words',
    beat: writer.beat
  }
}

// Major Piece Research (Every 2 Days, per writer)
{
  agent_type: 'writer',
  agent_id: writer.id,
  cron_expression: '0 9 */2 * *',  // Every 2 days at 9 AM
  task_type: 'research_major_piece',
  task_payload: {
    story_type: 'major',
    target_length: '2000-4000 words',
    research_depth: 'deep',
    beat: writer.beat
  }
}
```

### Task Types

1. **`editorial_meeting`** - Supervisory agent runs meeting
2. **`consider_new_story`** - Decide if adding story this hour
3. **`hunt_small_story`** - Writer finds quick story
4. **`research_major_piece`** - Writer does deep research
5. **`write_draft`** - Writer creates content
6. **`review_draft`** - Editor reviews
7. **`generate_story_image`** - Create visual for story
8. **`publish_story`** - Move to queue and publish
9. **`archive_story`** - Move to archive after decay

---

## 🏗️ Implementation Plan

### Phase 1: Timer System
- [x] Create timer infrastructure
- [ ] Add hourly editorial meeting timer
- [ ] Add 6-hour small story hunt timers (all writers)
- [ ] Add 2-day major piece timers (all writers)
- [ ] Test timer execution

### Phase 2: Story Queue
- [ ] Implement FIFO queue logic
- [ ] Add queue position tracking
- [ ] Create archive system
- [ ] Build queue visualization in admin panel

### Phase 3: Image Generation
- [ ] Install Google GenAI SDK
- [ ] Create `imageGenerator.js` service
- [ ] Integrate with story approval flow
- [ ] Add style selection to editor interface
- [ ] Set up image storage (S3 or local)

### Phase 4: Task Implementation
- [ ] Implement `editorial_meeting` task
- [ ] Implement `hunt_small_story` task
- [ ] Implement `research_major_piece` task
- [ ] Implement `generate_story_image` task
- [ ] Connect all tasks to GPT API calls

### Phase 5: Newsroom Dashboard
- [ ] Create "Newsroom Floor" view
- [ ] Show active meetings
- [ ] Display writer activity
- [ ] Visualize story queue
- [ ] Show image generation status

---

## 📊 Database Updates Needed

### Add to `stories` table:
```sql
ALTER TABLE stories ADD COLUMN IF NOT EXISTS queue_position INTEGER;
ALTER TABLE stories ADD COLUMN IF NOT EXISTS image_url TEXT;
ALTER TABLE stories ADD COLUMN IF NOT EXISTS image_style JSONB;
ALTER TABLE stories ADD COLUMN IF NOT EXISTS archived_at TIMESTAMP;
CREATE INDEX idx_stories_queue_position ON stories(queue_position) WHERE status = 'queued';
CREATE INDEX idx_stories_archived_at ON stories(archived_at) WHERE status = 'archived';
```

### New table: `editorial_meetings`
```sql
CREATE TABLE editorial_meetings (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  meeting_time TIMESTAMP NOT NULL,
  participants JSONB DEFAULT '[]',  -- List of agent IDs
  agenda JSONB DEFAULT '[]',
  decisions JSONB DEFAULT '{}',  -- What was decided
  stories_considered JSONB DEFAULT '[]',
  story_selected UUID REFERENCES stories(id),
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🎯 Success Metrics

- **Stories per day:** ~24 (1 per hour from meetings)
- **Small stories per day:** ~56 (14 writers × 4 per day)
- **Major pieces per week:** ~49 (14 writers × 3.5 per week)
- **Total content:** ~80 stories/day, ~560/week
- **Image generation:** 100% of published stories have images
- **Archive growth:** Permanent, searchable history

---

## 🔄 The Human-Like Flow

**Hour 0:00** - Editorial meeting
- "What's happening? Should we cover X?"
- Decision: Yes, assign to Writer A

**Hour 0:15** - Writer A starts research
- Gathers sources, writes draft

**Hour 1:00** - Next editorial meeting
- Reviews Writer A's progress
- Considers new story Y

**Hour 6:00** - Small story hunts begin
- 14 writers simultaneously hunting
- Each finds one quick story

**Hour 12:00** - More small stories
- Another round of quick pieces

**Day 2** - Major pieces start
- Deep research begins
- Long-form content in development

**Continuous:**
- Stories flow through queue
- Images generated on approval
- Content published FIFO
- Old content decays visually
- Everything archived forever

---

**This is a living, breathing newsroom that never sleeps.** 🏢✨
