# Admin Panel — Agent Souls Dashboard

*Last updated: 2024-12-14*

---

## 🎯 Access the Admin Panel

### URLs

- **Agent Souls Dashboard**: `/admin` or `/admin/page`
- **Overview Dashboard**: `/admin/overview`

### Development

1. Start the backend:
   ```bash
   cd backend
   npm install
   npm run dev
   ```

2. Start the frontend:
   ```bash
   npm run dev
   ```

3. Visit: `http://localhost:3000/admin`

---

## 📊 What You Can See

### Agent Souls Dashboard (`/admin`)

**Agent Cards View:**
- All agents with their current state
- Mood indicators (confident, focused, uncertain, etc.)
- Energy levels (visual progress bar)
- Quick stats (reasoning logs, work history, memories)

**Agent Detail View:**
Click any agent card to see:

1. **Current State (Soul)**
   - Current focus
   - Mood
   - Energy level
   - Recent decisions
   - Patterns noticed
   - Concerns
   - Goals

2. **Recent Reasoning**
   - Thought process logs
   - Alternatives considered
   - Confidence levels
   - Conclusions reached
   - Timestamps

3. **Work History**
   - Previous rounds of work
   - Input → Output flow
   - Quality scores
   - Lessons learned
   - Round numbers

4. **Memories**
   - All stored memories
   - Importance levels
   - Context
   - Last updated

### Overview Dashboard (`/admin/overview`)

**System-wide metrics:**
- Active tasks count
- Active timers
- Today's API usage & costs
- Active agents count
- Recent activity feed
- Agent performance stats

---

## 🔄 Real-time Updates

The dashboard automatically refreshes every 5 seconds to show:
- Latest agent states
- New reasoning logs
- Recent work
- Updated memories
- System activity

---

## 🎨 Design

- Uses bright accent colors for visual indicators
- Card-based layout
- Responsive grid
- Clean typography with vintage-modern fonts
- Energy level progress bars
- Mood badges with color coding

---

## 🚀 Next Steps

1. **Add authentication** - Protect `/admin/*` routes
2. **Add filtering** - Filter by agent type, status, etc.
3. **Add search** - Search reasoning logs, memories
4. **Add exports** - Export agent data
5. **Add WebSocket** - Real-time updates instead of polling
6. **Add charts** - Visualize agent performance over time

---

**Your admin panel is ready! Visit `/admin` to see your robots' souls! 👁️**
