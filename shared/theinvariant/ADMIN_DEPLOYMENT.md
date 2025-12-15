# Admin Panel — Global Deployment

*Last updated: 2024-12-14*

---

## ✅ Admin Panel is Now Global

The admin panel is accessible from anywhere in the world at:

- **Agent Souls Dashboard**: `https://theinvariant.org/admin`
- **Overview Dashboard**: `https://theinvariant.org/admin/overview`

---

## 🚀 Deployment

### Quick Deploy

```bash
./deploy.sh
```

This deploys both frontend and backend to EC2.

### What Gets Deployed

1. **Frontend** → `/var/www/theinvariant/frontend/`
   - Built Next.js static export
   - Includes `/admin` routes
   - Served by Caddy

2. **Backend** → `/var/www/theinvariant/backend/`
   - Node.js API server
   - Runs on port 3000
   - Managed by PM2

---

## 🔧 How It Works

### Architecture

```
Internet
  ↓
theinvariant.org (Route53 → EC2 IP)
  ↓
Caddy (HTTPS, port 443)
  ├── / → Frontend (static files)
  ├── /admin → Frontend (static files, SPA routing)
  └── /api/* → Backend (reverse proxy to localhost:3000)
```

### API Routing

- Frontend uses **relative paths**: `/api/admin/*`
- Caddy proxies `/api/*` → `localhost:3000`
- Works globally, no CORS issues

### Admin Routes

- Next.js builds `/admin` as static HTML
- Caddy serves with SPA fallback
- All routes accessible globally

---

## 📋 First-Time Setup

### 1. Deploy Backend to EC2

```bash
# Copy backend code
rsync -avz --delete \
  -e "ssh -i /tmp/theinvariant-key.pem" \
  --exclude 'node_modules' \
  backend/ \
  ubuntu@3.95.34.98:/var/www/theinvariant/backend/

# SSH and set up
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 << 'ENDSSH'
cd /var/www/theinvariant/backend
npm install --production

# Create database
psql -U theinvariant -d theinvariant -f db/schema.sql

# Set environment (use Parameter Store or .env)
# Then start:
pm2 start ecosystem.config.js
pm2 save
ENDSSH
```

### 2. Deploy Frontend

```bash
npm run build
./deploy.sh
```

---

## 🌐 Access

Once deployed:

- **Public Site**: `https://theinvariant.org/`
- **Admin Panel**: `https://theinvariant.org/admin` ← **Global access!**
- **Overview**: `https://theinvariant.org/admin/overview`
- **API Health**: `https://theinvariant.org/api/health`

---

## 🔄 Update Workflow

1. **Make changes**
2. **Test locally** (optional)
3. **Commit:**
   ```bash
   git add .
   git commit -m "Update admin panel"
   git push
   ```
4. **Deploy:**
   ```bash
   ./deploy.sh
   ```

**That's it!** Admin panel updates are live globally.

---

## 🛠️ Troubleshooting

### Admin panel shows 404?

1. Check frontend is deployed: `ls /var/www/theinvariant/frontend/admin/`
2. Check Caddy config has `/admin/*` handler
3. Reload Caddy: `sudo systemctl reload caddy`

### API calls failing?

1. Check backend is running: `pm2 list`
2. Check backend logs: `pm2 logs theinvariant-backend`
3. Test API directly: `curl https://theinvariant.org/api/health`

### CORS errors?

- Shouldn't happen (using relative paths)
- If they do, check Caddy is proxying `/api/*` correctly

---

## 🔐 Security (TODO)

**Currently admin panel is NOT protected!**

Add authentication:
1. JWT tokens
2. Session-based auth
3. OAuth (Google/GitHub)
4. IP whitelist (for now)

---

**Admin panel is now global! Access from anywhere at `https://theinvariant.org/admin` 🌍**
