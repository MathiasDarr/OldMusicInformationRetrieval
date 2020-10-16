#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="dakobed-serverless-pipeline"

# Uploads files to S3 bucket and creates CloudFormation template
sam package \
    --template-file template.yaml \
    --s3-bucket $BUCKET \
    --output-template-file package.yaml

## Deploys your stack
sam deploy \
    --template-file package.yaml \
    --stack-name DakobedUploadStack \
    --capabilities CAPABILITY_IAM
