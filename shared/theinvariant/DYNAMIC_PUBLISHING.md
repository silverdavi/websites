# Dynamic Story Publishing System
## No Redeployment Required!

*Created: 2024-12-14*

---

## 🎯 How It Works

The website is set up for **dynamic content updates** - stories appear automatically without redeploying the frontend!

### **Architecture**

1. **Frontend (Next.js Static)**
   - Built once and deployed as static files
   - Uses client-side fetching with `useEffect`
   - Auto-refreshes every 30 seconds to get new stories

2. **Backend API (Express)**
   - Serves stories from PostgreSQL database
   - API endpoints return fresh data with no-cache headers
   - Stories are published by updating database status

3. **Caddy Reverse Proxy**
   - Proxies `/api/*` from `theinvariant.org` → `localhost:3000`
   - Also serves `api.theinvariant.org` → `localhost:3000`
   - No caching - passes through to backend

---

## 📡 API Endpoints

### **GET `/api/map`**
Returns all published stories with freshness data.

**Response:**
```json
[
  {
    "id": "...",
    "title": "...",
    "status": "published",
    "freshness": 95.5,
    "is_fresh": true,
    "published_at": "2024-12-14T...",
    ...
  }
]
```

**Headers:**
- `Cache-Control: no-cache, no-store, must-revalidate`
- Always returns fresh data from database

### **GET `/api/stats`**
Returns platform statistics (updated every 10 seconds).

### **GET `/api/piece/:id`**
Returns a single story by ID.

---

## 🚀 Publishing Flow

1. **Story Workflow Completes**
   - Story goes through: intake → draft → critique → finalize → image generation
   - Story status set to `approved` or `queued`

2. **Automatic Publishing (Cron)**
   - Every 10 minutes: `storyQueue.publishNext()` runs
   - Moves story from `queued` → `published`
   - Sets `published_at = NOW()`
   - Initializes `freshness = 100.00`

3. **Frontend Auto-Refresh**
   - Frontend fetches `/api/map` every 30 seconds
   - New stories appear automatically!
   - No page reload needed
   - No redeployment needed

---

## ✅ Features

- ✅ **No Redeployment**: Stories appear automatically
- ✅ **Auto-Refresh**: Frontend polls API every 30 seconds
- ✅ **Fresh Data**: No caching - always current
- ✅ **Real-Time Stats**: Header stats update every 10 seconds
- ✅ **Dynamic Freshness**: Calculated on-the-fly from database

---

## 🔧 Manual Publishing

If you need to publish a story immediately:

```bash
# Via admin API
curl -X POST https://api.theinvariant.org/api/admin/publish-next \
  -H "Authorization: Bearer YOUR_TOKEN"

# Or directly in database
psql -U theinvariant -d theinvariant -c "
  UPDATE stories 
  SET status = 'published', published_at = NOW(), freshness = 100.00
  WHERE id = 'STORY_ID';
"
```

---

## 📊 Monitoring

Check if stories are being published:

```bash
# Check published stories
curl https://api.theinvariant.org/api/map | jq 'length'

# Check stats
curl https://api.theinvariant.org/api/stats | jq

# Check queue
curl https://api.theinvariant.org/api/stats | jq '.queue_depth'
```

---

**The website is now a living, breathing newspaper that updates itself!** 🗞️✨
