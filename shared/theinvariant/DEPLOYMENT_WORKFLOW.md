# The Invariant — Deployment Workflow

*Last updated: 2024-12-14*

---

## 🎯 Overview

**Everything runs on EC2. Git is just for pushing updates.**

- Frontend: Served by Caddy from `/var/www/theinvariant/frontend/`
- Backend: Node.js API on port 3000, managed by PM2
- Admin Panel: Accessible globally at `https://theinvariant.org/admin`

---

## 🚀 Quick Deploy

### One Command Deployment

```bash
./deploy.sh
```

This script:
1. Builds the frontend (`npm run build`)
2. Deploys frontend to EC2 (`rsync` to `/var/www/theinvariant/frontend/`)
3. Deploys backend to EC2 (`rsync` to `/var/www/theinvariant/backend/`)
4. Installs backend dependencies
5. Restarts backend with PM2

---

## 📋 Manual Deployment

### 1. Build Frontend

```bash
npm run build
```

Output goes to `out/` directory.

### 2. Deploy Frontend

```bash
rsync -avz --delete \
  -e "ssh -i /tmp/theinvariant-key.pem -o StrictHostKeyChecking=no" \
  out/ \
  ubuntu@3.95.34.98:/var/www/theinvariant/frontend/
```

### 3. Deploy Backend

```bash
rsync -avz --delete \
  -e "ssh -i /tmp/theinvariant-key.pem -o StrictHostKeyChecking=no" \
  --exclude 'node_modules' \
  --exclude '.env' \
  backend/ \
  ubuntu@3.95.34.98:/var/www/theinvariant/backend/
```

### 4. Restart Backend

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 << 'ENDSSH'
cd /var/www/theinvariant/backend
npm install --production
pm2 restart theinvariant-backend || pm2 start server.js --name theinvariant-backend
pm2 save
ENDSSH
```

---

## 🌐 Access URLs

Once deployed:

- **Public Site**: `https://theinvariant.org/`
- **Admin Panel**: `https://theinvariant.org/admin`
- **Overview Dashboard**: `https://theinvariant.org/admin/overview`
- **API**: `https://theinvariant.org/api/*` or `https://api.theinvariant.org/*`

---

## 🔧 Initial EC2 Setup (One-Time)

If EC2 isn't set up yet:

```bash
# SSH into EC2
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98

# Run setup script
bash <(curl -s https://raw.githubusercontent.com/your-repo/theinvariant-site/main/shared/theinvariant/infrastructure/ec2-setup.sh)

# Or copy and run locally
scp -i /tmp/theinvariant-key.pem shared/theinvariant/infrastructure/ec2-setup.sh ubuntu@3.95.34.98:~/
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'bash ~/ec2-setup.sh'
```

---

## 📦 Backend Setup on EC2

### First-Time Backend Setup

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 << 'ENDSSH'
cd /var/www/theinvariant/backend

# Install dependencies
npm install --production

# Set up database
psql -U theinvariant -d theinvariant -f db/schema.sql

# Create .env file (or use Parameter Store)
cat > .env <<EOF
DB_HOST=localhost
DB_PORT=5432
DB_NAME=theinvariant
DB_USER=theinvariant
DB_PASSWORD=$(cat ~/.db_password)
OPENAI_API_KEY=$(aws ssm get-parameter --name /theinvariant/openai-api-key --with-decryption --query Parameter.Value --output text)
PORT=3000
EOF

# Start with PM2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
ENDSSH
```

---

## 🔄 Git Workflow

### Simple Workflow

1. **Make changes locally**
2. **Test locally** (optional)
3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Update admin panel"
   git push origin main
   ```
4. **Deploy:**
   ```bash
   ./deploy.sh
   ```

That's it! No CI/CD needed. Just push and deploy.

---

## 🛠️ Troubleshooting

### Frontend not updating?

```bash
# Check Caddy is serving correct directory
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'ls -la /var/www/theinvariant/frontend/'

# Reload Caddy
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'sudo systemctl reload caddy'
```

### Backend not running?

```bash
# Check PM2 status
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'pm2 list'

# Check logs
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'pm2 logs theinvariant-backend'

# Restart
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'pm2 restart theinvariant-backend'
```

### Admin panel not loading?

1. Check backend is running: `pm2 list`
2. Check API is accessible: `curl https://theinvariant.org/api/health`
3. Check browser console for errors
4. Verify Caddy config has `/api/*` proxy

---

## 🔐 Security Notes

- Admin routes are **not protected** yet - add authentication!
- Use HTTPS (Caddy handles this automatically)
- Keep EC2 security group restricted
- Use Parameter Store for secrets (not .env in git)

---

## 📊 Monitoring

### Check Backend Status

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'pm2 monit'
```

### Check Caddy Logs

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'sudo journalctl -u caddy -f'
```

### Check System Resources

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'htop'
```

---

**Simple workflow: Push to git → Run deploy.sh → Done! 🚀**
