# Security Policy

## Scope

This repository contains educational IAM examples. It must not contain live credentials, real secret material, or confidential enterprise identifiers.

## Credential Handling Rules

Never commit:

- AWS access key IDs paired with real secret keys
- Secret access keys
- Session tokens
- Passwords
- MFA seeds / QR codes
- Private keys
- `.aws/credentials`
- `.env` files containing secrets

Use IAM roles and temporary credentials for labs whenever possible.

## Evidence Sanitization

Before adding screenshots to `evidence/`:

1. Remove or mask account IDs if they are not required.
2. Remove email addresses and personal data not needed for evidence.
3. Never capture secret access keys or session tokens.
4. Keep the AWS Region and resource name only when they help prove the control being demonstrated.
5. Add a short Markdown note explaining what the screenshot proves.

## Incident Rule

If a credential is accidentally committed, assume compromise. Revoke or rotate the credential immediately, then remove it from Git history as a separate cleanup step.
