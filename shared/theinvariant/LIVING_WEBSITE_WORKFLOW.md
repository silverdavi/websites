# The Invariant — Living Website Workflow
## "A Website That Never Sleeps"

*Created: 2024-12-14*

---

## 🎯 Goal

**Make the website ALIVE** — constantly updated with:
- ✅ Fresh news stories
- ✅ Tech stories  
- ✅ Images for every story
- ✅ Continuous content flow
- ✅ Visual decay of old content
- ✅ Permanent archive

---

## 🔄 The Complete Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    STORY DISCOVERY                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│  │ Hourly       │    │ Every 6 hrs  │    │ Every 2 days │     │
│  │ Editorial    │    │ Small Story  │    │ Major Piece  │     │
│  │ Meeting      │    │ Hunt         │    │ Research      │     │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘     │
│         │                    │                   │              │
│         └────────────────────┴───────────────────┘              │
│                            ↓                                     │
│                    INTAKE QUEUE                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    EDITORIAL REVIEW                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Editor reviews intake (GPT-5-mini)                          │
│  2. Decision: Accept / Reject / Request More Info               │
│  3. If accepted → Assign to Writer                              │
│  4. Create write_draft task                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    DRAFT WRITING                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Writer receives assignment                                   │
│  2. Writer researches & writes draft (GPT-5-mini)               │
│  3. Story created with status='draft'                           │
│  4. Story saved to database                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    EDITORIAL CRITIQUE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Editor reviews draft (GPT-5-mini)                           │
│  2. Provides feedback & quality score                         │
│  3. Decision: Approve / Request Revisions                        │
│  4. If approved → Create finalize task                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    FINALIZATION                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Final polish with GPT-5.2 (best quality)                    │
│  2. Story status → 'approved'                                  │
│  3. Editor selects visual style                                 │
│  4. Create generate_story_image task                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    IMAGE GENERATION                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Image generator reads story content                         │
│  2. Applies editor's style parameters                          │
│  3. Calls Gemini 3 Pro Image API                                │
│  4. Saves image to /var/www/theinvariant/images/stories/       │
│  5. Updates story with image_url                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PUBLISHING QUEUE (FIFO)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Story added to queue (status='queued')                     │
│  2. Queue position assigned (FIFO - oldest first)              │
│  3. Auto-publish every 10 minutes                              │
│  4. Story status → 'published'                                  │
│  5. Story appears on website                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    LIVE ON WEBSITE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Story visible in feed (sorted by published_at DESC)        │
│  2. Image displayed with story                                 │
│  3. Story ages over time (visual decay)                        │
│  4. After lifespan → status='decaying'                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    ARCHIVE                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. After decay period → status='archived'                     │
│  2. Story remains searchable forever                           │
│  3. Never deleted, always accessible                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⏰ The Rhythm: 24/7 Continuous Flow

### **Hourly: Editorial Meetings**
- **Time**: Every hour at :00 (e.g., 1:00, 2:00, 3:00...)
- **What**: All agents meet, review queue, decide on ONE new story
- **Result**: ~24 stories considered per day
- **Status**: ✅ Implemented

### **Every 6 Hours: Small Story Hunt**
- **Time**: 00:00, 06:00, 12:00, 18:00 (staggered per writer)
- **What**: Each writer hunts for quick stories (500-800 words)
- **Result**: ~56 small stories per day (14 writers × 4)
- **Status**: ✅ Implemented

### **Every 2 Days: Major Piece Research**
- **Time**: Every 2 days at 9:00 AM (alternating writers)
- **What**: Deep research for comprehensive pieces (2000-4000 words)
- **Result**: ~49 major pieces per week (14 writers × 3.5)
- **Status**: ✅ Implemented

### **Every 10 Minutes: Auto-Publish**
- **Time**: Every 10 minutes
- **What**: Publish next story from queue (FIFO)
- **Result**: ~6 stories published per hour, ~144 per day
- **Status**: ✅ Implemented

---

## 📊 Content Flow Projections

### **Daily Output**
- **Editorial meetings**: ~24 stories considered
- **Small story hunts**: ~56 stories discovered
- **Major pieces**: ~7 stories researched
- **Total intake**: ~87 stories/day
- **Published**: ~144 stories/day (from queue)
- **Images generated**: ~144 images/day

### **Weekly Output**
- **Stories published**: ~1,008 stories/week
- **Images generated**: ~1,008 images/week
- **Archive growth**: Permanent, searchable

---

## 🔧 Implementation Status

### ✅ **Completed**
- [x] GPT models configured (nano, mini, 5.2)
- [x] Task runner with all task types
- [x] Story queue system (FIFO)
- [x] Image generator service
- [x] Agent scheduler with timers
- [x] Auto-publish cron (every 10 min)
- [x] Database schema (all tables)
- [x] Agent memory & transparency

### ⏳ **Needs Completion**

#### **1. Connect Editorial Meeting → Story Assignment**
- [ ] When meeting decides to add story, automatically:
  - Select highest-priority intake item
  - Assign to appropriate writer
  - Create `write_draft` task
- **File**: `backend/services/taskRunner.js` → `editorialMeeting()`

#### **2. Connect Draft → Critique → Finalize**
- [ ] When draft completed, automatically:
  - Create `critique` task for assigned editor
- [ ] When critique approves, automatically:
  - Create `finalize` task
- **File**: `backend/services/taskRunner.js` → `writeDraft()`, `critique()`

#### **3. Connect Finalize → Image Generation → Queue**
- [ ] When story finalized, automatically:
  - Editor selects style (or default)
  - Create `generate_story_image` task
- [ ] When image generated, automatically:
  - Add story to queue
- **File**: `backend/services/taskRunner.js` → `finalize()`, `generateStoryImage()`

#### **4. Story Decay System**
- [ ] Cron job to check story lifespans
- [ ] Mark stories as 'decaying' after lifespan
- [ ] Mark stories as 'archived' after decay period
- **File**: `backend/services/storyQueue.js` → add decay logic

#### **5. Frontend: Story Feed**
- [ ] Display published stories
- [ ] Show images
- [ ] Apply visual decay (opacity/fade based on age)
- [ ] Archive view
- **File**: `app/page.tsx` or `app/stories/page.tsx`

#### **6. Image Storage Setup**
- [ ] Create `/var/www/theinvariant/images/stories/` directory
- [ ] Update Caddy config to serve images
- [ ] Test image serving
- **File**: Caddyfile, server setup

#### **7. Seed Initial Content**
- [ ] Create initial intake items
- [ ] Seed with real story ideas
- [ ] Start the flow
- **File**: `backend/scripts/seed-initial-content.js`

---

## 🚀 Activation Steps

### **Step 1: Complete Task Connections**
```bash
# Update taskRunner.js to auto-create next tasks
# When editorial meeting → create write_draft
# When draft done → create critique
# When critique approves → create finalize
# When finalize done → create generate_image
# When image done → add to queue
```

### **Step 2: Set Up Image Storage**
```bash
ssh ubuntu@3.95.34.98
sudo mkdir -p /var/www/theinvariant/images/stories
sudo chmod 755 /var/www/theinvariant/images/stories
```

### **Step 3: Update Caddy Config**
```caddy
handle /images/* {
    file_server
    root * /var/www/theinvariant
}
```

### **Step 4: Add Decay Cron**
```javascript
// In server.js
cron.schedule('0 * * * *', async () => {
  // Check stories past lifespan → mark as decaying
  // Check decaying stories past decay period → archive
});
```

### **Step 5: Seed Initial Content**
```bash
node backend/scripts/seed-initial-content.js
```

### **Step 6: Verify Timers**
```bash
# Check all timers are active
SELECT * FROM agent_timers WHERE is_active = true;
```

### **Step 7: Monitor Flow**
```bash
# Watch the queue
SELECT status, COUNT(*) FROM stories GROUP BY status;

# Watch tasks
SELECT task_type, status, COUNT(*) FROM agent_tasks GROUP BY task_type, status;
```

---

## 📈 Monitoring the Living Website

### **Key Metrics**
- **Queue depth**: How many stories waiting to publish
- **Publish rate**: Stories published per hour
- **Image generation**: Success rate, time per image
- **Agent activity**: Tasks completed per hour
- **Content freshness**: Average age of published stories

### **Admin Dashboard Views**
- **Newsroom Floor**: Real-time activity
- **Story Queue**: Visual queue status
- **Agent Activity**: Who's working on what
- **Content Feed**: Published stories
- **Archive**: Searchable history

---

## 🎨 Visual Decay System

### **How It Works**
1. Story published → Full opacity, vibrant
2. After 50% of lifespan → Slight fade
3. After 75% of lifespan → More fade
4. After 100% of lifespan → Status='decaying', significant fade
5. After decay period → Status='archived', still visible but muted

### **Frontend Implementation**
```css
.story {
  opacity: 1;
  transition: opacity 0.3s;
}

.story.decaying {
  opacity: 0.6;
}

.story.archived {
  opacity: 0.4;
}
```

---

## 🔄 The Complete Flow (Example)

**Hour 0:00** - Editorial Meeting
- Reviews queue: 5 stories waiting
- Considers intake: 12 pending items
- Decision: Add story about "Tech Breakthrough"
- Assigns to Writer A (Tech beat)
- Creates `write_draft` task

**Hour 0:15** - Writer A
- Receives assignment
- Researches topic (GPT-5-mini)
- Writes draft (GPT-5-mini)
- Story created: status='draft'

**Hour 1:00** - Next Editorial Meeting
- Reviews Writer A's draft
- Creates `critique` task for Editor B

**Hour 1:15** - Editor B
- Reviews draft (GPT-5-mini)
- Provides feedback
- Approves draft
- Creates `finalize` task

**Hour 1:30** - Finalization
- GPT-5.2 polishes story
- Story status='approved'
- Editor selects style: "photorealistic, urgent"
- Creates `generate_story_image` task

**Hour 1:45** - Image Generation
- Gemini generates image
- Image saved
- Story added to queue (position 6)
- Story status='queued'

**Hour 2:00** - Auto-Publish
- Story at position 1 publishes
- Story status='published'
- Appears on website
- Image displayed

**Days Later** - Decay
- Story reaches end of lifespan
- Status='decaying'
- Visual fade applied
- Eventually archived

---

## ✅ Success Criteria

The website is **ALIVE** when:
- [ ] Stories publish automatically every 10 minutes
- [ ] Images generate for every published story
- [ ] Editorial meetings run hourly
- [ ] Writers hunt stories every 6 hours
- [ ] Major pieces researched every 2 days
- [ ] Content flows continuously (no manual intervention)
- [ ] Old content decays visually
- [ ] Archive preserves everything
- [ ] Frontend displays live feed

---

**LET'S MAKE IT ALIVE!** 🚀✨
