# GPT Models Setup ✅

*Completed: 2024-12-14*

---

## 🤖 Models Configured

**Using the best models: gpt-5-nano and gpt-5-mini for efficiency, gpt-5.2 for the best quality**

### 1. **GPT-5-nano** ⚡ (Best for speed & cost)
- **Model**: `gpt-5-nano` - Ultra-lightweight, best for speed and cost
- **Use Case**: Trivial checks (typos, formatting, profanity, policy violations)
- **Temperature**: 0.2 (very precise)
- **Max Tokens**: 500
- **Cost**: Lowest tier

### 2. **GPT-5-mini** ⚖️ (Best for iteration)
- **Model**: `gpt-5-mini` - Faster, cost-efficient, best for iteration
- **Use Case**: Iteration, collaboration, critique, story hunting
- **Temperature**: 0.4 (balanced)
- **Max Tokens**: 2000
- **Cost**: Mid tier
- **Used For**:
  - Intake reviews
  - Draft writing
  - Critique
  - Story hunting
  - Editorial meetings

### 3. **GPT-5.2** ✨ (Best for quality)
- **Model**: `gpt-5.2` - The best model, enhanced capabilities for final quality
- **Use Case**: Final synthesis only (publishable content)
- **Temperature**: 0.7 (creative but controlled)
- **Max Tokens**: 4000
- **Cost**: Highest tier
- **Used For**:
  - Story finalization

---

## 📋 Implementation

### Service: `gptService.js`

**Functions:**
- `callGPT(model, prompt, options, context)` - Generic GPT caller
- `callNano(prompt, context)` - Quick wrapper for nano
- `callMini(prompt, options, context)` - Quick wrapper for mini
- `callGPT52(prompt, options, context)` - Quick wrapper for 5.2
- `getModelForTask(taskType)` - Auto-select model based on task
- `testModels()` - Test all three models

**Features:**
- ✅ Automatic usage tracking
- ✅ Error handling
- ✅ Reasoning logging (for mini and 5.2)
- ✅ Cost calculation
- ✅ Duration tracking

---

## 🔧 Task Integration

### Updated Tasks:

1. **`reviewIntake`** → Uses `gpt-5-mini`
   - Reviews intake items
   - Makes accept/reject decisions
   - Provides reasoning

2. **`writeDraft`** → Uses `gpt-5-mini`
   - Writes article drafts
   - Creates story records
   - 500-800 words (small) or 2000-4000 (major)

3. **`critique`** → Uses `gpt-5-mini`
   - Provides editorial feedback
   - Quality scoring
   - Recommendations

4. **`finalize`** → Uses `gpt-5.2`
   - Final polish and synthesis
   - Publication-ready content
   - Metadata generation

5. **`huntSmallStory`** → Uses `gpt-5-mini`
   - Identifies story opportunities
   - Creates intake submissions

6. **`researchMajorPiece`** → Uses `gpt-5-mini`
   - Deep research identification
   - Comprehensive story pitches

7. **`editorialMeeting`** → Uses `gpt-5-mini`
   - Strategic decisions
   - Story selection

---

## 🧪 Testing

Run test script:
```bash
cd /var/www/theinvariant/backend
node scripts/test-gpt-models.js
```

This will:
- Test all three models
- Verify API connectivity
- Show response examples
- Report any failures

---

## 📊 Usage Tracking

All GPT calls are automatically tracked:
- Token usage (input/output/total)
- Cost calculation
- Duration
- Model used
- Agent context

Stored in `api_usage` table for analysis.

---

## 🔑 Requirements

**Environment Variable:**
```bash
OPENAI_API_KEY=your_key_here
```

**Package:**
```json
"openai": "^4.20.0"
```

---

## ✅ Status

- ✅ All three models configured
- ✅ Service created with proper error handling
- ✅ Tasks updated to use GPT calls
- ✅ Usage tracking integrated
- ✅ Reasoning logging for transparency
- ✅ Test script available

---

**Backend is ready to use GPT-5-nano, mini, and 5.2!** 🤖✨
