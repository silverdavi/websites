# The Invariant — Infrastructure Summary

*Created: 2024-12-14*

---

## ✅ COMPLETE: AWS Infrastructure Provisioned

### Resources Created

| Resource | ID/Value | Status |
|----------|----------|--------|
| **EC2 Instance** | `i-0e583442c9eaf880b` | ✅ Running |
| **Public IP** | `3.95.34.98` | ✅ Active |
| **VPC** | `vpc-06490f5558ca66f6f` | ✅ Created |
| **Security Group** | `sg-04208b2d83649704d` | ✅ Configured (HTTP/HTTPS/SSH) |
| **S3 Bucket** | `theinvariant-assets-1765728529` | ✅ Created |
| **Route53 Zone** | `Z02787152ZSPM0AK00U9X` | ✅ Active |
| **Route53 Records** | | ✅ Configured |
| **IAM Role** | `theinvariant-ec2-role` | ✅ Attached |
| **Parameter Store Secrets** | | ✅ Stored |

### DNS Configuration

- ✅ `theinvariant.org` → GitHub Pages (A records: 185.199.108-111.153)
- ✅ `www.theinvariant.org` → `silverdavi.github.io` (CNAME)
- ✅ `api.theinvariant.org` → `3.95.34.98` (A record)

### Secrets Management

- ✅ OpenAI API key stored in Parameter Store: `/theinvariant/openai-api-key`
- ✅ Google API key stored in Parameter Store: `/theinvariant/google-api-key`
- ✅ IAM role attached to EC2 for secure access
- ⏳ GitHub secrets (repo doesn't exist yet - will set when created)

---

## 📋 Next Steps

### Immediate (Do Now)

1. **SSH into EC2:**
   ```bash
   ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
   ```

2. **Run EC2 setup script:**
   ```bash
   # Copy script to instance
   scp -i /tmp/theinvariant-key.pem \
     shared/theinvariant/infrastructure/ec2-setup.sh \
     ubuntu@3.95.34.98:~/
   
   # SSH in and run
   ssh -i /tmp/theinvariant-key.pem ubuntu@3.95.34.98
   chmod +x ec2-setup.sh
   ./ec2-setup.sh
   ```

3. **Create GitHub repo** (if not exists):
   ```bash
   cd /Users/davidsilver/dev/websites/theinvariant-site
   gh repo create silverdavi/theinvariant-site --public --source=. --push
   ```

4. **Set GitHub secrets:**
   ```bash
   gh secret set OPENAI_API_KEY --repo silverdavi/theinvariant-site -b "$(grep OPENAI_API_KEY shared/.env | cut -d'=' -f2)"
   gh secret set GOOGLE_API_KEY --repo silverdavi/theinvariant-site -b "$(grep GOOGLE_API_KEY shared/.env | cut -d'=' -f2)"
   ```

### Short Term

- Deploy backend code to EC2
- Configure Caddy for HTTPS
- Deploy frontend (GitHub Pages or EC2)
- Test end-to-end workflow

---

## 💰 Cost Estimate

| Service | Monthly |
|---------|---------|
| EC2 t3.medium | ~$30 |
| EBS 30GB | ~$2.50 |
| S3 (50GB) | ~$1.50 |
| CloudFront (100GB) | ~$8.50 |
| Route53 | ~$1 |
| **Total** | **~$45/month** |

---

## 🔐 Security Status

- ✅ Secrets in Parameter Store (encrypted)
- ✅ IAM role with least privilege
- ✅ Security group configured
- ⚠️ SSH open to 0.0.0.0/0 (consider restricting)
- ⚠️ Postgres password needs to be changed (will be set in ec2-setup.sh)

---

## 📁 Files Created

- `infrastructure/setup.sh` - AWS infrastructure provisioning script
- `infrastructure/ec2-setup.sh` - EC2 server setup script
- `infrastructure/DEPLOYMENT.md` - Full deployment guide
- `infrastructure/SUMMARY.md` - This file

---

## 🚀 THE INVARIANT IS COMING!

All infrastructure is ready. The machine is waiting for code.
