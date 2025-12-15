# Website Activation Guide
## Getting Stories and Graphics Live

*Created: 2024-12-14*

---

## 🎯 Current Status

- ✅ Frontend code updated (HeaderStats, StoryCard, vibrant colors)
- ✅ Backend API working
- ⏳ No stories in database yet
- ⏳ Frontend needs proper deployment
- ⏳ API key needs to be set

---

## 🚀 Activation Steps

### **Step 1: Set API Key**

The `.env` file on EC2 needs `OPENAI_API_KEY` set:

```bash
ssh ubuntu@3.95.34.98
cd /var/www/theinvariant/backend
# Edit .env or use AWS Parameter Store
# Ensure OPENAI_API_KEY is set (not "placeholder")
```

### **Step 2: Deploy Frontend**

```bash
cd /Users/davidsilver/dev/websites/theinvariant-site
npm run build
rsync -avz -e "ssh -i /tmp/theinvariant-key.pem" out/ ubuntu@3.95.34.98:/var/www/theinvariant/frontend/
```

### **Step 3: Seed Initial News**

Once API key is set:

```bash
ssh ubuntu@3.95.34.98
cd /var/www/theinvariant/backend
node scripts/seed-initial-news-standalone.js
```

This will:
- Research news for all writers
- Create intake items
- Populate the queue

### **Step 4: Let Workflow Run**

The automatic workflow will:
1. Editorial meetings review intake
2. Assign stories to writers
3. Writers create drafts
4. Editors critique and approve
5. Stories finalized
6. Images generated
7. Stories published

---

## 🎨 Graphics & Colors

The vibrant colors are in:
- `app/page.module.css` - Updated with gradients
- `app/globals.css` - Bright color variables
- Header, hero, cards all have colorful gradients

**Deploy CSS:**
```bash
npm run build  # Rebuilds with CSS
rsync out/ to /var/www/theinvariant/frontend/
```

---

## ✅ Checklist

- [ ] API key set on EC2
- [ ] Frontend deployed to `/var/www/theinvariant/frontend/`
- [ ] CSS files deployed
- [ ] Initial news seeded
- [ ] Editorial meetings running
- [ ] Stories flowing through workflow
- [ ] Stories publishing to website

---

**Once activated, the website will come alive!** 🚀✨
