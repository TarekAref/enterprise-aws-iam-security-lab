# Lab 01 — Least-Privilege S3 Read Access

## Objective

Create a role or test principal that can list one approved S3 bucket and read objects from that bucket, while remaining unable to delete objects or read from unrelated buckets.

## Risk Being Addressed

Broad permissions such as `s3:*` on `*` unnecessarily increase the impact of credential compromise or operator error.

## Policy

Use [`../policies/identity/s3-readonly-project.json`](../policies/identity/s3-readonly-project.json).

## Validation

Expected **allowed** operations:

```bash
aws s3api list-objects-v2 --bucket example-project-data
aws s3api get-object --bucket example-project-data --key public/sample.txt ./sample.txt
```

Expected **denied** operation:

```bash
aws s3api delete-object --bucket example-project-data --key public/sample.txt
```

## Evidence

Capture sanitized evidence showing:

- Attached policy
- Successful read
- Failed delete with `AccessDenied`

## Enterprise Interpretation

The value of the lab is not merely that read access works. The stronger evidence is that a destructive action is intentionally denied because it was never granted.

## Cleanup

Delete temporary roles/policies and test resources when the lab is complete.
