#!/bin/bash

#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="mir-cloudformation-artifacts"

# Uploads files to S3 bucket and creates CloudFormation template
aws cloudformation package \
    --template-file template.yaml \
    --s3-bucket $BUCKET \
    --output-template-file package.yaml

## Deploys your stack
aws cloudformation deploy \
    --template-file package.yaml \
    --stack-name DStack \
    --capabilities CAPABILITY_IAM