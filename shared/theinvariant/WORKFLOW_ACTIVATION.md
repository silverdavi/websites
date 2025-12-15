# Workflow Activation Guide
## Making The Website ALIVE

*Created: 2024-12-14*

---

## ✅ What's Complete

### **Automatic Task Flow**
- ✅ Editorial meeting → Auto-creates `write_draft` task
- ✅ Draft written → Auto-creates `critique` task
- ✅ Critique approved → Auto-creates `finalize` task
- ✅ Story finalized → Auto-creates `generate_story_image` task
- ✅ Image generated → Auto-adds to publishing queue
- ✅ Queue auto-publishes every 10 minutes

### **Timers & Scheduling**
- ✅ Hourly editorial meetings
- ✅ 6-hour small story hunts
- ✅ 2-day major piece research
- ✅ Auto-publish every 10 minutes
- ✅ Story decay check every hour

### **GPT Integration**
- ✅ GPT-5-nano, mini, 5.2 all configured
- ✅ All tasks use appropriate models
- ✅ Usage tracking active

---

## 🚀 Activation Steps

### **Step 1: Set Up Image Storage**

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
sudo mkdir -p /var/www/theinvariant/images/stories
sudo chmod 755 /var/www/theinvariant/images/stories
```

### **Step 2: Update Caddy Config**

Add to `/etc/caddy/Caddyfile`:

```caddy
handle /images/* {
    file_server
    root * /var/www/theinvariant
}
```

Then reload Caddy:
```bash
sudo caddy reload
```

### **Step 3: Deploy Updated Backend**

```bash
cd /Users/davidsilver/dev/websites/theinvariant-site
./deploy.sh
```

### **Step 4: Verify Timers Are Active**

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
cd /var/www/theinvariant/backend
psql -U theinvariant -d theinvariant -c "SELECT timer_name, cron_expression, next_run_at, is_active FROM agent_timers WHERE is_active = true;"
```

### **Step 5: Seed Initial Content**

Create some initial intake items to start the flow:

```bash
# On EC2
cd /var/www/theinvariant/backend
node scripts/seed-initial-content.js
```

Or manually via SQL:
```sql
INSERT INTO intake_items (sources, summary, relevance, suggested_lifespan, submitted_by, status, priority)
VALUES 
  ('[{"type": "news", "title": "Tech Breakthrough"}]', 'Major tech announcement', 'High relevance for tech beat', 14, 'system', 'pending', 5),
  ('[{"type": "news", "title": "Science Discovery"}]', 'New scientific finding', 'Important for science beat', 21, 'system', 'pending', 4);
```

### **Step 6: Monitor the Flow**

Watch the system come alive:

```bash
# Watch tasks being created
watch -n 5 'psql -U theinvariant -d theinvariant -c "SELECT task_type, status, COUNT(*) FROM agent_tasks GROUP BY task_type, status ORDER BY task_type;"'

# Watch queue status
watch -n 10 'psql -U theinvariant -d theinvariant -c "SELECT status, COUNT(*) FROM stories GROUP BY status;"'

# Watch published stories
psql -U theinvariant -d theinvariant -c "SELECT title, status, published_at FROM stories WHERE status IN ('published', 'decaying') ORDER BY published_at DESC LIMIT 10;"
```

---

## 📊 Expected Flow

### **Hour 0:00** - First Editorial Meeting
- Reviews queue (empty initially)
- Considers intake items
- Decides to add story
- Creates `write_draft` task

### **Hour 0:05** - Task Processing
- Writer picks up `write_draft` task
- Writes draft using GPT-5-mini
- Creates story record
- Auto-creates `critique` task

### **Hour 0:10** - Critique
- Editor picks up `critique` task
- Reviews draft using GPT-5-mini
- If approved (quality ≥ 0.7), auto-creates `finalize` task

### **Hour 0:15** - Finalization
- Editor finalizes using GPT-5.2
- Story status → 'approved'
- Auto-creates `generate_story_image` task

### **Hour 0:20** - Image Generation
- Image generated with Gemini
- Story auto-added to queue
- Story status → 'queued'

### **Hour 0:30** - First Publish
- Auto-publish cron runs
- Story at position 1 publishes
- Story status → 'published'
- Appears on website!

### **Every 10 Minutes** - Continuous Publishing
- Next story in queue publishes
- Website stays fresh

### **Every Hour** - Decay Check
- Stories past lifespan → 'decaying'
- Stories decaying 7+ days → 'archived'

---

## 🎯 Success Indicators

The website is **ALIVE** when you see:

1. **Tasks flowing automatically:**
   ```
   write_draft → critique → finalize → generate_story_image → queued → published
   ```

2. **Stories publishing regularly:**
   ```
   Every 10 minutes, a new story appears
   ```

3. **Queue building up:**
   ```
   Multiple stories in 'queued' status
   ```

4. **Images being generated:**
   ```
   Stories have image_url populated
   ```

5. **Content decaying:**
   ```
   Stories moving from 'published' → 'decaying' → 'archived'
   ```

---

## 🔧 Troubleshooting

### **No tasks being created?**
- Check timers are active: `SELECT * FROM agent_timers WHERE is_active = true;`
- Check cron is running: `pm2 logs theinvariant-backend`
- Check task runner: `SELECT * FROM agent_tasks ORDER BY created_at DESC LIMIT 10;`

### **Stories not publishing?**
- Check queue: `SELECT * FROM stories WHERE status = 'queued' ORDER BY queue_position;`
- Check publish cron: Look for "Story published" in logs
- Manually publish: `node -e "import('./services/storyQueue.js').then(m => m.storyQueue.publishNext())"`

### **Images not generating?**
- Check GOOGLE_API_KEY is set
- Check image directory exists: `ls -la /var/www/theinvariant/images/stories/`
- Check image generator logs in task results

### **No intake items?**
- Seed initial content (Step 5)
- Check story hunts are creating intake: `SELECT * FROM intake_items ORDER BY created_at DESC;`

---

## 📈 Monitoring Commands

```bash
# Overall health
psql -U theinvariant -d theinvariant -c "
  SELECT 
    (SELECT COUNT(*) FROM agent_tasks WHERE status = 'pending') as pending_tasks,
    (SELECT COUNT(*) FROM stories WHERE status = 'queued') as queued_stories,
    (SELECT COUNT(*) FROM stories WHERE status = 'published') as published_stories,
    (SELECT COUNT(*) FROM intake_items WHERE status = 'pending') as pending_intake;
"

# Recent activity
psql -U theinvariant -d theinvariant -c "
  SELECT task_type, status, COUNT(*), MAX(created_at) as latest
  FROM agent_tasks
  WHERE created_at > NOW() - INTERVAL '1 hour'
  GROUP BY task_type, status
  ORDER BY latest DESC;
"

# Story pipeline
psql -U theinvariant -d theinvariant -c "
  SELECT status, COUNT(*), 
    MIN(created_at) as oldest, 
    MAX(created_at) as newest
  FROM stories
  GROUP BY status
  ORDER BY status;
"
```

---

**The website is ready to come ALIVE!** 🚀✨
