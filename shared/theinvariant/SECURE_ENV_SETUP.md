# Secure .env Setup for EC2 Backend

*Last updated: 2024-12-14*

---

## 🔐 Two Secure Methods

### Method 1: AWS Parameter Store (Recommended)

**Most secure** - Secrets stored encrypted in AWS, accessed via IAM role.

#### Step 1: Upload secrets to Parameter Store

From your local machine:

```bash
cd /Users/davidsilver/dev/websites/theinvariant-site/backend
./scripts/upload-secrets.sh
```

This reads `/Users/davidsilver/dev/websites/shared/.env` and uploads:
- `OPENAI_API_KEY` → `/theinvariant/openai-api-key`
- `GOOGLE_API_KEY` → `/theinvariant/google-api-key`

#### Step 2: Generate .env on EC2

SSH into EC2 and run:

```bash
cd /var/www/theinvariant/backend
./scripts/setup-env.sh
```

This script:
- Fetches secrets from Parameter Store (using IAM role)
- Gets database password from `~/.db_password`
- Creates `.env` with secure permissions (600)

---

### Method 2: Direct Secure Transfer

**Simpler** - Directly transfer .env file with secure permissions.

From your local machine:

```bash
cd /Users/davidsilver/dev/websites/theinvariant-site/backend
./scripts/sync-env.sh
```

This:
- Transfers `.env` via `scp` (encrypted)
- Sets permissions to 600 (owner read/write only)
- Never exposes secrets in transit

---

## 🔒 Security Best Practices

### ✅ DO:
- Use AWS Parameter Store for production (Method 1)
- Set file permissions to 600: `chmod 600 .env`
- Use IAM roles (EC2 already has access)
- Never commit `.env` to git (already in `.gitignore`)

### ❌ DON'T:
- Don't store .env in git
- Don't use world-readable permissions
- Don't hardcode secrets in code
- Don't share .env files via email/chat

---

## 📋 What Gets Set

The `.env` file contains:

```bash
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=theinvariant
DB_USER=theinvariant
DB_PASSWORD=<from ~/.db_password>

# API Keys
OPENAI_API_KEY=<from Parameter Store or .env>
GOOGLE_API_KEY=<from Parameter Store or .env>

# Server
PORT=3000
NODE_ENV=production
```

---

## 🚀 Quick Setup

### Option A: Parameter Store (Recommended)

```bash
# 1. Upload secrets
./backend/scripts/upload-secrets.sh

# 2. On EC2, generate .env
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
cd /var/www/theinvariant/backend
./scripts/setup-env.sh
```

### Option B: Direct Transfer

```bash
# One command from local
./backend/scripts/sync-env.sh
```

---

## ✅ Verification

After setup, verify on EC2:

```bash
# Check file exists and permissions
ls -la /var/www/theinvariant/backend/.env
# Should show: -rw------- (600)

# Test backend can read it
cd /var/www/theinvariant/backend
node -e "require('dotenv').config(); console.log('DB:', process.env.DB_NAME)"
```

---

## 🔄 Updating Secrets

### Update Parameter Store:

```bash
./backend/scripts/upload-secrets.sh
```

Then on EC2:
```bash
cd /var/www/theinvariant/backend
./scripts/setup-env.sh
pm2 restart theinvariant-backend
```

### Update Direct .env:

```bash
./backend/scripts/sync-env.sh
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98 'pm2 restart theinvariant-backend'
```

---

**Your secrets are secure! 🔐**
