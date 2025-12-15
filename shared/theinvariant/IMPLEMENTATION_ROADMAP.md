# Implementation Roadmap: Newsroom Workflow

*Created: 2024-12-14*

---

## 🎯 Goal

Transform the editorial system into a **24/7 human-like newsroom** with:
- Hourly editorial meetings
- 6-hour small story hunts
- 2-day major piece research
- FIFO story queue
- Gemini image generation
- Permanent archive

---

## 📅 Phase 1: Timer Infrastructure (Week 1)

### Tasks
1. ✅ **Timer system exists** - Already implemented
2. ⏳ **Add cron parsing library** - Use `node-cron` properly
3. ⏳ **Create timer seeding script** - All writers get timers
4. ⏳ **Test timer execution** - Verify triggers work

### Files to Create/Modify
- `backend/services/agentScheduler.js` - Improve cron parsing
- `backend/scripts/seed-timers.js` - Create all timers
- `backend/db/add-timers.sql` - Database updates if needed

---

## 📅 Phase 2: Editorial Meeting System (Week 1-2)

### Tasks
1. ⏳ **Create `editorial_meeting` task type**
2. ⏳ **Implement meeting logic** - Review queue, decide on story
3. ⏳ **Create meeting records** - Log all meetings
4. ⏳ **Add supervisory agent** - Runs meetings

### Files to Create/Modify
- `backend/services/taskRunner.js` - Add `editorialMeeting()` method
- `backend/db/add-meetings-table.sql` - New table
- `backend/services/meetingCoordinator.js` - Meeting orchestration

---

## 📅 Phase 3: Story Hunting Tasks (Week 2)

### Tasks
1. ⏳ **Implement `hunt_small_story` task**
2. ⏳ **Implement `research_major_piece` task**
3. ⏳ **Connect to news APIs** - Real-time feeds
4. ⏳ **Create intake submissions** - Auto-submit findings

### Files to Create/Modify
- `backend/services/taskRunner.js` - Add hunting methods
- `backend/services/newsFeeds.js` - News aggregation
- `backend/services/intakeManager.js` - Intake submission

---

## 📅 Phase 4: Story Queue System (Week 2-3)

### Tasks
1. ⏳ **Implement FIFO queue logic**
2. ⏳ **Add queue position tracking**
3. ⏳ **Create publish scheduler** - Auto-publish from queue
4. ⏳ **Build archive system** - Move old stories

### Files to Create/Modify
- `backend/services/storyQueue.js` - Queue management
- `backend/services/publishScheduler.js` - Auto-publishing
- `backend/db/add-queue-fields.sql` - Database updates

---

## 📅 Phase 5: Image Generation (Week 3)

### Tasks
1. ⏳ **Install Google GenAI SDK** - `npm install @google/genai`
2. ⏳ **Create `imageGenerator.js`** - Service for images
3. ⏳ **Add style selection** - Editor chooses style
4. ⏳ **Integrate with approval** - Generate on approval
5. ⏳ **Set up image storage** - Local or S3

### Files to Create/Modify
- `backend/services/imageGenerator.js` - ✅ Created
- `backend/services/taskRunner.js` - Add `generateStoryImage()` call
- `backend/routes/admin.js` - Style selection endpoint
- `app/admin/story-approval.tsx` - UI for style selection

---

## 📅 Phase 6: Newsroom Dashboard (Week 3-4)

### Tasks
1. ⏳ **Create "Newsroom Floor" view**
2. ⏳ **Show active meetings** - Real-time status
3. ⏳ **Display writer activity** - Who's working on what
4. ⏳ **Visualize story queue** - Queue position, status
5. ⏳ **Image generation status** - Show progress

### Files to Create/Modify
- `app/admin/newsroom/page.tsx` - Main newsroom view
- `components/NewsroomFloor.tsx` - Visual layout
- `components/MeetingRoom.tsx` - Meeting display
- `components/WriterDesks.tsx` - Writer activity
- `components/StoryQueue.tsx` - Queue visualization

---

## 🔧 Technical Details

### Dependencies to Add

```json
{
  "dependencies": {
    "@google/genai": "^1.0.0",
    "node-cron": "^3.0.3"  // Already have, but use properly
  }
}
```

### Environment Variables

```bash
GOOGLE_API_KEY=your_key_here  # For Gemini image generation
NEWS_API_KEY=optional          # For news feeds
```

### Database Migrations

1. Add queue fields to stories
2. Create editorial_meetings table
3. Add image storage fields
4. Create indexes for performance

---

## 📊 Success Criteria

- [ ] Hourly meetings run automatically
- [ ] Writers hunt stories on schedule
- [ ] Stories flow through FIFO queue
- [ ] Images generate for all published stories
- [ ] Archive preserves all content
- [ ] Dashboard shows real-time activity

---

## 🚀 Quick Start (After Implementation)

1. **Seed all timers:**
   ```bash
   node backend/scripts/seed-timers.js
   ```

2. **Start backend:**
   ```bash
   pm2 start backend/server.js
   ```

3. **View newsroom:**
   ```
   https://theinvariant.org/admin/newsroom
   ```

---

**Let's build a newsroom that never sleeps!** 🏢✨
