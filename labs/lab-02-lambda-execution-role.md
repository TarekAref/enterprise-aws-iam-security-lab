# Lab 02 — Lambda Execution Role Without Static Keys

## Objective

Allow an AWS Lambda function to read from one S3 bucket using an IAM execution role rather than hard-coded access keys.

## Architecture

```text
Lambda function
      |
      | assumes execution role automatically
      v
IAM Role
      |
      | s3:GetObject
      v
Approved S3 bucket
```

## Trust Policy

Use [`../policies/trust/lambda-assume-role.json`](../policies/trust/lambda-assume-role.json).

## Permission Design

Attach only the application permissions required by the function. If CloudWatch Logs permissions are required, add the minimum log permissions separately or use the appropriate execution policy during the lab.

## Validation

1. Invoke the function against an approved object.
2. Confirm successful retrieval.
3. Attempt access to an unrelated bucket and verify denial.
4. Confirm CloudTrail records relevant API activity.

## Security Interpretation

The workload receives temporary credentials through its role session. No long-term access key needs to be embedded in function code.
