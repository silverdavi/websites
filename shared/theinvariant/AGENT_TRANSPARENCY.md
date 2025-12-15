# Agent Transparency — Windows to Their Souls

*Last updated: 2024-12-14*

---

## Philosophy

**Every GPT-5 agent has a "soul" — their internal state, reasoning, and memory.**

We keep windows open to see:
- What they're thinking right now
- What they did in their last round
- Their reasoning process
- Patterns they've noticed
- Concerns they have
- Goals they're working toward

---

## Database Schema

### Agent Memory
Stores persistent memories:
- `memory_key` - e.g., 'last_intake_review', 'preferred_topics'
- `memory_value` - JSON data
- `importance` - 1-10, how critical to retain
- `context` - What this memory is about

### Agent Reasoning
Logs their thought process:
- `reasoning_type` - 'decision', 'analysis', 'reflection', 'planning'
- `thought_process` - Their actual thinking
- `conclusion` - What they decided
- `confidence` - 0.00 to 1.00
- `alternatives_considered` - Other options they thought about

### Agent Work History
What they did in previous rounds:
- `round_number` - Which iteration
- `work_type` - 'intake_review', 'draft_written', etc.
- `input_data` - What they received
- `output_data` - What they produced
- `quality_score` - Self or system assessment
- `lessons_learned` - What they learned

### Agent State
Current "soul" state:
- `current_focus` - What they're thinking about now
- `active_context` - Current working context
- `recent_decisions` - Last N decisions
- `patterns_noticed` - Patterns they've identified
- `concerns` - Things they're worried about
- `goals` - Current goals
- `mood` - 'confident', 'uncertain', 'focused', 'frustrated'
- `energy_level` - 1-10

---

## API Endpoints

### Get Agent's Soul (Full Transparency)
```
GET /admin/agent-soul/:agent_type/:agent_id
```

Returns:
- Current state
- All memories
- Recent reasoning (last 10)
- Recent work (last 10)

### Get Agent State
```
GET /admin/agent-state/:agent_type/:agent_id
```

Returns current "soul" state.

### Get Agent Memories
```
GET /admin/agent-memories/:agent_type/:agent_id
```

Returns all stored memories, ordered by importance.

### Get Agent Reasoning History
```
GET /admin/agent-reasoning/:agent_type/:agent_id?limit=50
```

Returns their thought process history.

### Get Agent Work History
```
GET /admin/agent-work-history/:agent_type/:agent_id?limit=20
```

Returns what they did in previous rounds.

### Get All Agents' Souls
```
GET /admin/agents-souls?agent_type=editor
```

Returns souls for all agents (optionally filtered by type).

---

## Usage in Task Runner

When agents work, they:

1. **Log their reasoning** before making decisions
2. **Record their work** with input/output
3. **Store memories** about patterns and decisions
4. **Update their state** with current focus, mood, energy

Example:
```javascript
// Agent reviews intake
const reasoning = await agentMemory.logReasoning(
  'editor',
  editor_id,
  task_id,
  'decision',
  'Reviewing intake item. Previous similar reviews: 5. Considering relevance...',
  {
    alternatives_considered: ['accept', 'reject', 'request_more_info'],
    confidence: 0.75
  }
);

// Record their work
await agentMemory.recordWork(
  'editor',
  editor_id,
  'intake_review',
  input_data,
  decision,
  { reasoning_id: reasoning.id, quality_score: 0.8 }
);

// Update state
await agentMemory.updateState('editor', editor_id, {
  current_focus: 'Reviewing intake queue',
  recent_decisions: [{ type: 'intake_review', decision }],
  mood: 'focused',
  energy_level: 7
});
```

---

## Frontend Dashboard

Build a dashboard that shows:

1. **Agent Soul View**
   - Current state (focus, mood, energy)
   - Recent decisions
   - Patterns noticed
   - Concerns

2. **Reasoning Timeline**
   - Chronological view of their thinking
   - See what they considered
   - Confidence levels
   - Alternatives they rejected

3. **Work History**
   - What they did in each round
   - Input → Output flow
   - Quality scores over time
   - Lessons learned

4. **Memory Bank**
   - All stored memories
   - Importance-weighted
   - Searchable

---

## Benefits

✅ **Transparency** - See what agents are thinking
✅ **Debugging** - Understand why they made decisions
✅ **Learning** - See patterns in their work
✅ **Trust** - Full visibility into AI reasoning
✅ **Improvement** - Identify areas to refine

---

**Windows to their souls are open! 👁️**
