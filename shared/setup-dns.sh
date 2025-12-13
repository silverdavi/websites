#!/bin/bash
# Route 53 DNS setup for GitHub Pages
# GitHub username: silverdavi

set -e

GITHUB_USER="silverdavi"
DOMAINS=("unpop.info" "dhsilver.me" "kernel-keys.com" "embino.com")

# GitHub Pages IP addresses
GITHUB_IPS=(
  "185.199.108.153"
  "185.199.109.153"
  "185.199.110.153"
  "185.199.111.153"
)

echo "=== Route 53 DNS Setup for GitHub Pages ==="
echo ""

# Check AWS credentials
echo "Checking AWS credentials..."
aws sts get-caller-identity || {
  echo "ERROR: AWS CLI not configured. Run 'aws configure' first."
  exit 1
}
echo ""

# List existing hosted zones
echo "Existing hosted zones:"
aws route53 list-hosted-zones --query 'HostedZones[*].[Name,Id]' --output table
echo ""

for DOMAIN in "${DOMAINS[@]}"; do
  echo "----------------------------------------"
  echo "Processing: $DOMAIN"
  echo "----------------------------------------"
  
  # Get hosted zone ID
  ZONE_ID=$(aws route53 list-hosted-zones \
    --query "HostedZones[?Name=='${DOMAIN}.'].Id" \
    --output text | sed 's|/hostedzone/||')
  
  if [ -z "$ZONE_ID" ]; then
    echo "WARNING: No hosted zone found for $DOMAIN"
    echo "Creating hosted zone..."
    ZONE_ID=$(aws route53 create-hosted-zone \
      --name "$DOMAIN" \
      --caller-reference "$(date +%s)-$DOMAIN" \
      --query 'HostedZone.Id' \
      --output text | sed 's|/hostedzone/||')
    echo "Created hosted zone: $ZONE_ID"
  else
    echo "Found hosted zone: $ZONE_ID"
  fi
  
  # Create change batch JSON
  CHANGE_BATCH=$(cat <<EOF
{
  "Changes": [
    {
      "Action": "UPSERT",
      "ResourceRecordSet": {
        "Name": "${DOMAIN}",
        "Type": "A",
        "TTL": 300,
        "ResourceRecords": [
          {"Value": "${GITHUB_IPS[0]}"},
          {"Value": "${GITHUB_IPS[1]}"},
          {"Value": "${GITHUB_IPS[2]}"},
          {"Value": "${GITHUB_IPS[3]}"}
        ]
      }
    },
    {
      "Action": "UPSERT",
      "ResourceRecordSet": {
        "Name": "www.${DOMAIN}",
        "Type": "CNAME",
        "TTL": 300,
        "ResourceRecords": [
          {"Value": "${GITHUB_USER}.github.io"}
        ]
      }
    }
  ]
}
EOF
)

  echo "Creating/updating DNS records..."
  aws route53 change-resource-record-sets \
    --hosted-zone-id "$ZONE_ID" \
    --change-batch "$CHANGE_BATCH"
  
  echo "✓ $DOMAIN configured"
  echo ""
done

echo "=== DNS Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Wait 5-10 minutes for DNS propagation"
echo "2. In each GitHub repo, go to Settings → Pages"
echo "3. Set custom domain to the corresponding domain"
echo "4. Enable 'Enforce HTTPS' once verified"
echo ""
echo "Verify with: dig +short <domain>"

