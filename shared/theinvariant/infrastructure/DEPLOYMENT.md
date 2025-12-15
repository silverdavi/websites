# The Invariant — Deployment Guide

*Last updated: 2024-12-14*

---

## Infrastructure Status

✅ **AWS Resources Created:**

| Resource | ID/Name | Details |
|----------|---------|---------|
| **EC2 Instance** | `i-0e583442c9eaf880b` | t3.medium, Ubuntu 24.04 LTS |
| **Public IP** | `3.95.34.98` | Static (will change on restart) |
| **VPC** | `vpc-06490f5558ca66f6f` | 10.0.0.0/16 |
| **Security Group** | `sg-04208b2d83649704d` | HTTP, HTTPS, SSH open |
| **S3 Bucket** | `theinvariant-assets-1765728529` | For static assets |
| **Route53 Zone** | `Z02787152ZSPM0AK00U9X` | theinvariant.org |
| **Route53 Records** | | `theinvariant.org` → GitHub Pages<br>`api.theinvariant.org` → EC2 IP |
| **IAM Role** | `theinvariant-ec2-role` | Parameter Store access |
| **Secrets** | Parameter Store | `/theinvariant/openai-api-key`<br>`/theinvariant/google-api-key` |

---

## SSH Access

```bash
ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
```

**Note:** The key is at `/tmp/theinvariant-key.pem`. Copy it somewhere safe if needed.

---

## EC2 Setup Script

Run this on the EC2 instance to install all dependencies:

```bash
#!/bin/bash
# The Invariant - EC2 Initial Setup

set -e

echo "🚀 Setting up The Invariant backend server..."

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install Node.js 20.x
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Postgres
sudo apt-get install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql <<EOF
CREATE DATABASE theinvariant;
CREATE USER theinvariant WITH PASSWORD 'CHANGE_THIS_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE theinvariant TO theinvariant;
\q
EOF

# Install Meilisearch
curl -L https://install.meilisearch.com | sh
sudo mv meilisearch /usr/local/bin/
sudo systemctl enable meilisearch
sudo systemctl start meilisearch

# Install Caddy
sudo apt-get install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt-get update
sudo apt-get install -y caddy

# Install PM2 for process management
sudo npm install -g pm2

# Install AWS CLI (for Parameter Store access)
sudo apt-get install -y awscli

# Create app directory
sudo mkdir -p /var/www/theinvariant
sudo chown ubuntu:ubuntu /var/www/theinvariant

# Create Caddy config
sudo tee /etc/caddy/Caddyfile <<'CADDYFILE'
theinvariant.org {
    root * /var/www/theinvariant
    file_server
    
    handle /api/* {
        reverse_proxy localhost:3000
    }
    
    # SPA fallback
    try_files {path} /index.html
}

api.theinvariant.org {
    reverse_proxy localhost:3000
}
CADDYFILE

# Enable and start Caddy
sudo systemctl enable caddy
sudo systemctl start caddy

echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Change Postgres password in /etc/postgresql/*/main/pg_hba.conf"
echo "   2. Deploy backend code to /var/www/theinvariant/backend"
echo "   3. Configure environment variables"
echo "   4. Start backend with PM2"
```

---

## Environment Variables on EC2

The EC2 instance can access secrets from Parameter Store using the IAM role.

**In your backend code, use AWS SDK to fetch:**

```javascript
// Node.js example
const { SSMClient, GetParameterCommand } = require("@aws-sdk/client-ssm");

const ssm = new SSMClient({ region: "us-east-1" });

async function getSecret(name) {
  const response = await ssm.send(
    new GetParameterCommand({
      Name: name,
      WithDecryption: true,
    })
  );
  return response.Parameter.Value;
}

// Usage
const openaiKey = await getSecret("/theinvariant/openai-api-key");
const googleKey = await getSecret("/theinvariant/google-api-key");
```

**Or use environment variables (set on instance):**

```bash
# On EC2, create /home/ubuntu/.env
OPENAI_API_KEY=$(aws ssm get-parameter --name /theinvariant/openai-api-key --with-decryption --query Parameter.Value --output text)
GOOGLE_API_KEY=$(aws ssm get-parameter --name /theinvariant/google-api-key --with-decryption --query Parameter.Value --output text)
```

---

## GitHub Secrets

**When you create the GitHub repo `silverdavi/theinvariant-site`, set secrets:**

```bash
# From your local machine
gh secret set OPENAI_API_KEY --repo silverdavi/theinvariant-site -b "$(grep OPENAI_API_KEY shared/.env | cut -d'=' -f2)"
gh secret set GOOGLE_API_KEY --repo silverdavi/theinvariant-site -b "$(grep GOOGLE_API_KEY shared/.env | cut -d'=' -f2)"
```

**Or manually in GitHub:**
- Repo → Settings → Secrets and variables → Actions → New repository secret

---

## Deployment Workflow

### Backend Deployment

1. **SSH into EC2:**
   ```bash
   ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
   ```

2. **Clone/pull backend code:**
   ```bash
   cd /var/www/theinvariant/backend
   git pull origin main
   npm install
   ```

3. **Set environment variables** (from Parameter Store or .env)

4. **Start with PM2:**
   ```bash
   pm2 start ecosystem.config.js
   pm2 save
   pm2 startup  # Run once to enable auto-start
   ```

### Frontend Deployment

**Option 1: Serve from EC2 (current setup)**
```bash
# Build locally or in CI
npm run build

# Deploy to EC2
rsync -avz dist/ ubuntu@3.95.34.98:/var/www/theinvariant/
```

**Option 2: S3 + CloudFront**
```bash
# Build
npm run build

# Deploy to S3
aws s3 sync dist/ s3://theinvariant-assets-1765728529 --delete

# Invalidate CloudFront (if configured)
aws cloudfront create-invalidation --distribution-id XXXXX --paths "/*"
```

**Option 3: GitHub Pages**
- Push to `main` branch
- GitHub Actions builds and deploys
- Route53 points `theinvariant.org` to GitHub Pages

---

## DNS Configuration

**Route53 records are set:**
- `theinvariant.org` (A) → GitHub Pages IPs
- `www.theinvariant.org` (CNAME) → `silverdavi.github.io`
- `api.theinvariant.org` (A) → EC2 IP `3.95.34.98`

**Note:** EC2 IP will change on instance restart. Consider:
1. Elastic IP (static IP, ~$3/month)
2. Or update Route53 record on restart

**To get Elastic IP:**
```bash
aws ec2 allocate-address --domain vpc
aws ec2 associate-address --instance-id i-0e583442c9eaf880b --allocation-id eipalloc-XXXXX
```

---

## Monitoring & Logs

**PM2 logs:**
```bash
pm2 logs
pm2 monit
```

**Caddy logs:**
```bash
sudo journalctl -u caddy -f
```

**System logs:**
```bash
sudo journalctl -f
```

---

## Cost Estimate

| Service | Monthly Cost |
|---------|--------------|
| EC2 t3.medium | ~$30 |
| EBS 30GB | ~$2.50 |
| S3 (50GB) | ~$1.50 |
| CloudFront (100GB) | ~$8.50 |
| Route53 | ~$1 |
| **Total** | **~$45/month** |

---

## Security Notes

1. **Change default Postgres password** immediately
2. **Restrict SSH access** (consider IP whitelist or VPN)
3. **Enable Caddy HTTPS** (automatic with Let's Encrypt)
4. **Regular security updates:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```
5. **Firewall:** Consider restricting security group to specific IPs
6. **Backups:** Set up automated EBS snapshots

---

## Troubleshooting

**Can't SSH:**
- Check security group allows port 22
- Verify key permissions: `chmod 400 /tmp/theinvariant-key.pem`

**Can't access API:**
- Check Caddy is running: `sudo systemctl status caddy`
- Check backend is running: `pm2 list`
- Check security group allows ports 80/443

**Secrets not accessible:**
- Verify IAM role is attached: `aws sts get-caller-identity` (on EC2)
- Check Parameter Store permissions in IAM role

---

## Next Steps

1. ✅ Infrastructure created
2. ⏳ SSH into EC2 and run setup script
3. ⏳ Deploy backend code
4. ⏳ Configure GitHub repo and secrets
5. ⏳ Deploy frontend
6. ⏳ Test end-to-end

**THE INVARIANT IS COMING! 🚀**
