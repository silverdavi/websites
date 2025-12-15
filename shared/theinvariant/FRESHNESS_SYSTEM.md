# Freshness Thermometer System

*Created: 2024-12-14*

---

## 🎯 Overview

Every story on the website has a **freshness thermometer** that shows how fresh the content is. Freshness starts at 100% and decays over time based on a configurable decay rate.

---

## 📊 How It Works

### **Freshness Calculation**
- **Starts at**: 100% when published
- **Decays by**: `decay_rate`% per day
- **Formula**: `freshness = 100 - (days_since_published × decay_rate)`
- **Minimum**: 0% (never goes negative)

### **Decay Rates**
- **5%/day** - Sensational/breaking news (stays fresh longer)
- **10%/day** - Normal stories (default)
- **20%/day** - Minor/filler content (fades quickly)

### **Visual Effects**
- **Freshness ≥ 20%**: Full opacity, normal display
- **Freshness < 20%**: Gradual fade (opacity = freshness / 20)
- **Minimum opacity**: 30% (even at 0% freshness)

---

## 🎨 Thermometer Display

The thermometer shows:
- **Green** (80-100%): Very fresh
- **Yellow** (50-79%): Moderately fresh
- **Orange** (20-49%): Getting stale
- **Red** (<20%): Stale (with fade effect)

---

## 🔧 Implementation

### **Database Fields**
```sql
ALTER TABLE stories ADD COLUMN freshness DECIMAL(5,2) DEFAULT 100.00;
ALTER TABLE stories ADD COLUMN decay_rate DECIMAL(5,2) DEFAULT 10.00;
ALTER TABLE stories ADD COLUMN freshness_updated_at TIMESTAMP;
```

### **Automatic Updates**
- **Daily at midnight**: Updates all published stories
- **Every hour**: Updates freshness for responsive decay
- **On publish**: Initializes freshness to 100%

### **Editor Control**
- Editor sets decay rate during finalization
- GPT-5-nano analyzes story importance:
  - "sensational" → 5%/day
  - "normal" → 10%/day
  - "minor" → 20%/day
- Editors can manually adjust freshness/decay via API

---

## 📡 API Endpoints

### **Get Freshness**
```
GET /api/piece/:id/freshness
```

### **Update Freshness** (Editor/Admin)
```
PATCH /api/piece/:id/freshness
Body: { freshness: 85, decay_rate: 5 }
```

### **Stories Include Freshness**
```
GET /api/map
GET /api/piece/:id
```
Both endpoints include `freshness` and `is_fresh` fields.

---

## 🎯 Frontend Integration

### **StoryCard Component**
- Displays thermometer next to category
- Applies fade when freshness < 20%
- Shows decay rate in tooltip

### **Visual Fade**
```css
opacity: freshness < 20 ? Math.max(0.3, freshness / 20) : 1.0
```

---

## ✅ Status

- ✅ Database fields added
- ✅ Freshness service created
- ✅ Automatic decay calculation
- ✅ Cron jobs for updates
- ✅ API endpoints
- ✅ Frontend components
- ✅ Visual fade effect

---

**The freshness system is ready!** 🌡️✨
