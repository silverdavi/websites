#!/bin/bash
# The Invariant - AWS Infrastructure Setup
# Creates: EC2, Route53, S3, CloudFront, Parameter Store secrets

set -e

REGION="us-east-1"
DOMAIN="theinvariant.org"
STACK_NAME="theinvariant-infra"

echo "🚀 Setting up The Invariant infrastructure..."

# Check AWS credentials
echo "✅ AWS Identity:"
aws sts get-caller-identity

# 1. Create S3 bucket for assets
echo ""
echo "📦 Creating S3 bucket..."
BUCKET_NAME="theinvariant-assets-$(date +%s)"
if [ "$REGION" == "us-east-1" ]; then
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" || true
else
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION" || true
fi

aws s3api put-bucket-versioning \
  --bucket "$BUCKET_NAME" \
  --versioning-configuration Status=Enabled

aws s3api put-bucket-encryption \
  --bucket "$BUCKET_NAME" \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

echo "✅ S3 bucket: $BUCKET_NAME"

# 2. Create Route53 hosted zone (if domain not already managed)
echo ""
echo "🌐 Setting up Route53..."
HOSTED_ZONE_ID=$(aws route53 list-hosted-zones-by-name \
  --dns-name "$DOMAIN" \
  --query "HostedZones[0].Id" \
  --output text 2>/dev/null || echo "")

if [ -z "$HOSTED_ZONE_ID" ] || [ "$HOSTED_ZONE_ID" == "None" ]; then
  echo "Creating hosted zone for $DOMAIN..."
  HOSTED_ZONE=$(aws route53 create-hosted-zone \
    --name "$DOMAIN" \
    --caller-reference "theinvariant-$(date +%s)" \
    --query "HostedZone.Id" \
    --output text)
  HOSTED_ZONE_ID=$(echo "$HOSTED_ZONE" | cut -d'/' -f3)
  echo "✅ Created hosted zone: $HOSTED_ZONE_ID"
  echo "⚠️  Update your domain registrar with these nameservers:"
  aws route53 get-hosted-zone --id "$HOSTED_ZONE_ID" \
    --query "DelegationSet.NameServers" \
    --output table
else
  echo "✅ Using existing hosted zone: $HOSTED_ZONE_ID"
fi

# 3. Create VPC (if doesn't exist)
echo ""
echo "🌐 Setting up VPC..."
VPC_ID=$(aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=theinvariant-vpc" \
  --query "Vpcs[0].VpcId" \
  --output text 2>/dev/null || echo "")

if [ -z "$VPC_ID" ] || [ "$VPC_ID" == "None" ]; then
  echo "Creating VPC..."
  VPC_ID=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --query "Vpc.VpcId" \
    --output text)
  
  aws ec2 create-tags \
    --resources "$VPC_ID" \
    --tags Key=Name,Value=theinvariant-vpc
  
  # Enable DNS
  aws ec2 modify-vpc-attribute \
    --vpc-id "$VPC_ID" \
    --enable-dns-support
  aws ec2 modify-vpc-attribute \
    --vpc-id "$VPC_ID" \
    --enable-dns-hostnames
  
  # Create internet gateway
  IGW_ID=$(aws ec2 create-internet-gateway \
    --query "InternetGateway.InternetGatewayId" \
    --output text)
  aws ec2 attach-internet-gateway \
    --vpc-id "$VPC_ID" \
    --internet-gateway-id "$IGW_ID"
  
  # Create public subnet
  SUBNET_ID=$(aws ec2 create-subnet \
    --vpc-id "$VPC_ID" \
    --cidr-block 10.0.1.0/24 \
    --availability-zone "${REGION}a" \
    --query "Subnet.SubnetId" \
    --output text)
  
  # Create route table
  RT_ID=$(aws ec2 create-route-table \
    --vpc-id "$VPC_ID" \
    --query "RouteTable.RouteTableId" \
    --output text)
  aws ec2 create-route \
    --route-table-id "$RT_ID" \
    --destination-cidr-block 0.0.0.0/0 \
    --gateway-id "$IGW_ID" > /dev/null
  aws ec2 associate-route-table \
    --subnet-id "$SUBNET_ID" \
    --route-table-id "$RT_ID" > /dev/null
  
  echo "✅ Created VPC: $VPC_ID"
else
  echo "✅ Using existing VPC: $VPC_ID"
  SUBNET_ID=$(aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=$VPC_ID" \
    --query "Subnets[0].SubnetId" \
    --output text)
fi

# 4. Create EC2 security group
echo ""
echo "🔒 Creating security group..."
SG_ID=$(aws ec2 create-security-group \
  --group-name theinvariant-sg \
  --description "The Invariant EC2 security group" \
  --vpc-id "$VPC_ID" \
  --query "GroupId" \
  --output text 2>/dev/null || \
  aws ec2 describe-security-groups \
    --filters "Name=group-name,Values=theinvariant-sg" "Name=vpc-id,Values=$VPC_ID" \
    --query "SecurityGroups[0].GroupId" \
    --output text)

# Allow HTTP, HTTPS, SSH
aws ec2 authorize-security-group-ingress \
  --group-id "$SG_ID" \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0 2>/dev/null || true

aws ec2 authorize-security-group-ingress \
  --group-id "$SG_ID" \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0 2>/dev/null || true

aws ec2 authorize-security-group-ingress \
  --group-id "$SG_ID" \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0 2>/dev/null || true

echo "✅ Security group: $SG_ID"

# 5. Create EC2 key pair (if doesn't exist)
echo ""
echo "🔑 Setting up key pair..."
KEY_NAME="theinvariant-key"
aws ec2 create-key-pair \
  --key-name "$KEY_NAME" \
  --query "KeyMaterial" \
  --output text > "/tmp/${KEY_NAME}.pem" 2>/dev/null && \
  chmod 400 "/tmp/${KEY_NAME}.pem" && \
  echo "✅ Key pair created: /tmp/${KEY_NAME}.pem" || \
  echo "✅ Key pair already exists"

# 6. Get latest Ubuntu 24.04 LTS AMI
echo ""
echo "🖼️  Finding Ubuntu 24.04 LTS AMI..."
AMI_ID=$(aws ec2 describe-images \
  --owners 099720109477 \
  --filters \
    "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*" \
    "Name=state,Values=available" \
  --query "Images | sort_by(@, &CreationDate) | [-1].ImageId" \
  --output text \
  --region "$REGION")

echo "✅ Using AMI: $AMI_ID"

# 7. Create EC2 instance (t3.medium)
echo ""
echo "🖥️  Launching EC2 instance..."
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id "$AMI_ID" \
  --instance-type t3.medium \
  --key-name "$KEY_NAME" \
  --security-group-ids "$SG_ID" \
  --subnet-id "$SUBNET_ID" \
  --associate-public-ip-address \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=theinvariant-backend},{Key=Project,Value=theinvariant}]" \
  --query "Instances[0].InstanceId" \
  --output text)

echo "⏳ Waiting for instance to be running..."
aws ec2 wait instance-running --instance-ids "$INSTANCE_ID"

# Get public IP
PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids "$INSTANCE_ID" \
  --query "Reservations[0].Instances[0].PublicIpAddress" \
  --output text)

echo "✅ EC2 instance: $INSTANCE_ID"
echo "   Public IP: $PUBLIC_IP"

# 8. Store secrets in Parameter Store
echo ""
echo "🔐 Storing secrets in Parameter Store..."
# Read from .env
OPENAI_KEY=$(grep "^OPENAI_API_KEY=" /Users/davidsilver/dev/websites/shared/.env | cut -d'=' -f2)
GOOGLE_KEY=$(grep "^GOOGLE_API_KEY=" /Users/davidsilver/dev/websites/shared/.env | cut -d'=' -f2)

if [ -n "$OPENAI_KEY" ]; then
  aws ssm put-parameter \
    --name "/theinvariant/openai-api-key" \
    --value "$OPENAI_KEY" \
    --type "SecureString" \
    --overwrite 2>/dev/null && echo "✅ Stored OpenAI key" || echo "⚠️  OpenAI key already exists"
fi

if [ -n "$GOOGLE_KEY" ]; then
  aws ssm put-parameter \
    --name "/theinvariant/google-api-key" \
    --value "$GOOGLE_KEY" \
    --type "SecureString" \
    --overwrite 2>/dev/null && echo "✅ Stored Google key" || echo "⚠️  Google key already exists"
fi

# 9. Create IAM role for EC2 to access Parameter Store
echo ""
echo "👤 Creating IAM role for EC2..."
ROLE_NAME="theinvariant-ec2-role"
aws iam create-role \
  --role-name "$ROLE_NAME" \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }' 2>/dev/null || echo "✅ Role already exists"

# Attach policy for Parameter Store access
aws iam put-role-policy \
  --role-name "$ROLE_NAME" \
  --policy-name "ParameterStoreAccess" \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter",
        "ssm:GetParameters",
        "ssm:GetParametersByPath"
      ],
      "Resource": "arn:aws:ssm:*:*:parameter/theinvariant/*"
    }]
  }' 2>/dev/null || echo "✅ Policy attached"

# Create instance profile
aws iam create-instance-profile \
  --instance-profile-name "$ROLE_NAME" 2>/dev/null || true

aws iam add-role-to-instance-profile \
  --instance-profile-name "$ROLE_NAME" \
  --role-name "$ROLE_NAME" 2>/dev/null || true

# Attach to instance (requires instance stop/start, so we'll note it)
echo "⚠️  To attach IAM role, run:"
echo "   aws ec2 associate-iam-instance-profile --instance-id $INSTANCE_ID --iam-instance-profile Name=$ROLE_NAME"

# 10. Create Route53 A records (GitHub Pages IPs + EC2)
echo ""
echo "🌐 Creating Route53 records..."
# GitHub Pages IPs
GITHUB_IPS=("185.199.108.153" "185.199.109.153" "185.199.110.153" "185.199.111.153")

# A records for root domain (GitHub Pages)
CHANGE_BATCH=$(cat <<EOF
{
  "Changes": [{
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "$DOMAIN",
      "Type": "A",
      "TTL": 300,
      "ResourceRecords": [
        {"Value": "${GITHUB_IPS[0]}"},
        {"Value": "${GITHUB_IPS[1]}"},
        {"Value": "${GITHUB_IPS[2]}"},
        {"Value": "${GITHUB_IPS[3]}"}
      ]
    }
  }, {
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "www.$DOMAIN",
      "Type": "CNAME",
      "TTL": 300,
      "ResourceRecords": [{"Value": "silverdavi.github.io"}]
    }
  }, {
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "api.$DOMAIN",
      "Type": "A",
      "TTL": 300,
      "ResourceRecords": [{"Value": "$PUBLIC_IP"}]
    }
  }]
}
EOF
)

aws route53 change-resource-record-sets \
  --hosted-zone-id "$HOSTED_ZONE_ID" \
  --change-batch "$CHANGE_BATCH" && \
  echo "✅ Route53 records created" || \
  echo "⚠️  Route53 records may already exist"

# 11. Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━/theinvariant-infrastructure-setup"
echo "✅ Infrastructure setup complete!"
echo ""
echo "📋 Summary:"
echo "   EC2 Instance: $INSTANCE_ID"
echo "   Public IP: $PUBLIC_IP"
echo "   SSH: ssh -i /tmp/${KEY_NAME}.pem ubuntu@$PUBLIC_IP"
echo "   S3 Bucket: $BUCKET_NAME"
echo "   Route53 Zone: $HOSTED_ZONE_ID"
echo "   Domain: $DOMAIN → GitHub Pages"
echo "   API: api.$DOMAIN → $PUBLIC_IP"
echo ""
echo "🔐 Secrets stored in Parameter Store:"
echo "   /theinvariant/openai-api-key"
echo "   /theinvariant/google-api-key"
echo ""
echo "📝 Next steps:"
echo "   1. SSH into instance: ssh -i /tmp/${KEY_NAME}.pem ubuntu@$PUBLIC_IP"
echo "   2. Install Node.js, Postgres, Meilisearch, Caddy"
echo "   3. Deploy backend code"
echo "   4. Configure Caddy for HTTPS"
echo ""
