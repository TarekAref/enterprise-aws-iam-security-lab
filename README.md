# Enterprise AWS IAM Security Lab

> A portfolio repository demonstrating enterprise-oriented identity and access management design in Amazon Web Services (AWS), with emphasis on least privilege, temporary credentials, cross-account authorization, policy evaluation, governance, auditability, and operational security.

## Executive Summary

This repository turns foundational AWS Identity and Access Management (IAM) concepts into an **enterprise security design and hands-on lab portfolio**. It is intentionally structured to show not only *how* IAM objects are created, but also *why* access decisions are made, how privileges are constrained, how identities are governed across multiple AWS accounts, and how access is monitored and reviewed over time.

The project demonstrates practical knowledge of:

- IAM users, groups, roles, and policies
- Authentication versus authorization
- Least-privilege design
- Role assumption and temporary credentials through AWS Security Token Service (STS)
- Cross-account access and trust policies
- Identity-based and resource-based policies
- Permissions boundaries
- AWS Organizations guardrails with Service Control Policies (SCPs)
- Workforce access through AWS IAM Identity Center and federation
- Multi-factor authentication (MFA)
- Access-key risk reduction
- IAM Access Analyzer
- AWS CloudTrail-based auditability
- Identity lifecycle governance
- Break-glass and privileged-access concepts
- Policy validation and continuous access review

This repository is an **educational portfolio lab**, not a claim that the examples have been deployed in a production enterprise environment. The goal is to demonstrate enterprise-ready thinking, secure design choices, and the ability to translate IAM theory into reviewable technical controls.

---

## Why This Repository Is Enterprise-Oriented

A basic IAM lab often stops at creating a user, attaching a policy, and enabling MFA. Enterprise IAM requires a broader control model:

```text
Corporate Identity Provider / Workforce Directory
                    |
                    v
            IAM Identity Center
                    |
        +-----------+-----------+
        |                       |
        v                       v
   Development AWS          Production AWS
      Account                  Account
        |                       |
 Permission Sets / Roles   Permission Sets / Roles
        |                       |
        +-----------+-----------+
                    |
                    v
          Temporary Credentials
                    |
                    v
           AWS Resources / APIs
                    |
        +-----------+-----------+
        |                       |
        v                       v
  CloudTrail / Logs       IAM Access Analyzer
        |                       |
        +-----------+-----------+
                    |
                    v
        Review, Detection, Governance
```

The design assumes that human workforce identities should normally use federation and temporary credentials rather than permanent IAM-user access keys. Workloads should use IAM roles whenever possible. Multi-account environments are governed with organizational guardrails, and access is continuously reviewed rather than treated as a one-time configuration task.

---

## Repository Architecture

```text
enterprise-aws-iam-security-lab/
├── README.md
├── SECURITY.md
├── CHANGELOG.md
├── docs/
│   ├── 01-iam-foundations.md
│   ├── 02-enterprise-architecture.md
│   ├── 03-policy-evaluation.md
│   ├── 04-identity-lifecycle.md
│   ├── 05-cross-account-access.md
│   ├── 06-credential-and-mfa-strategy.md
│   ├── 07-monitoring-and-audit.md
│   ├── 08-governance-and-controls.md
│   └── 09-threat-model.md
├── labs/
│   ├── README.md
│   ├── lab-01-s3-least-privilege.md
│   ├── lab-02-lambda-execution-role.md
│   ├── lab-03-cross-account-assume-role.md
│   └── lab-04-access-analyzer-review.md
├── policies/
│   ├── identity/
│   │   └── s3-readonly-project.json
│   ├── trust/
│   │   ├── lambda-assume-role.json
│   │   └── cross-account-role.json
│   ├── boundary/
│   │   └── developer-permissions-boundary.json
│   └── scp/
│       └── deny-security-service-tampering.json
├── scripts/
│   └── validate-json.py
├── evidence/
│   └── README.md
└── .github/
    └── workflows/
        └── validate-policies.yml
```

---

## Core IAM Mental Model

### Authentication

Authentication answers:

> **Who is making the request?**

Examples include a federated workforce user, IAM role session, IAM user, application, or AWS service principal.

### Authorization

Authorization answers:

> **What is this authenticated principal allowed to do, to which resource, and under what conditions?**

AWS evaluates applicable policies before allowing a request. The important enterprise rule is:

> **An explicit Deny overrides an Allow.**

Permissions can be shaped by identity-based policies, resource-based policies, permissions boundaries, session policies, and organization-level controls such as SCPs and Resource Control Policies (RCPs).

---

## Identity Strategy

### Human Workforce Access

**Preferred enterprise pattern:**

```text
User
  -> Corporate Identity Provider / IAM Identity Center
  -> Permission Set / Role
  -> Temporary AWS credentials
  -> Authorized AWS resources
```

Long-lived IAM users should not be the default workforce-access model in a mature multi-account environment.

### Workload Access

**Preferred enterprise pattern:**

```text
Lambda / EC2 / ECS / Application
  -> IAM Role
  -> AWS STS temporary credentials
  -> Specific AWS API actions
```

This avoids embedding long-term access keys inside source code or application configuration.

---

## Policy Design Principles

This repository follows six design principles:

1. **Least privilege** — grant the minimum actions, resources, and conditions required.
2. **Temporary credentials first** — prefer roles and federation over static credentials.
3. **Explicit trust** — role trust policies define who or what may assume a role.
4. **Separation of duties** — avoid combining routine development and sensitive security administration privileges.
5. **Guardrails plus permissions** — organization controls define the maximum allowed operating space; identity/resource policies grant task-level permissions.
6. **Continuous verification** — review unused access, validate policies, inspect external access, and retain audit logs.

---

## Enterprise Policy Evaluation

A simplified authorization model:

```text
Request
  |
  v
Authenticate principal
  |
  v
Collect applicable policies
  |
  +--> Identity-based policy
  +--> Resource-based policy
  +--> Permissions boundary
  +--> Session policy
  +--> SCP / RCP
  |
  v
Any applicable explicit Deny?
  |                 |
 Yes                No
  |                 |
 DENY        Is required Allow present?
                    |          |
                   No         Yes
                    |          |
                   DENY       ALLOW
```

The real AWS evaluation logic is more nuanced than this diagram, especially for resource-based policies and session principals. See [`docs/03-policy-evaluation.md`](docs/03-policy-evaluation.md).

---

## Portfolio Labs

| Lab | Enterprise Skill Demonstrated | Primary AWS Concepts |
|---|---|---|
| Lab 01 | Least-privilege data access | S3, identity policy, ARN scoping |
| Lab 02 | Workload identity without static keys | Lambda, execution role, trust policy |
| Lab 03 | Secure cross-account delegation | STS, trust policy, external account |
| Lab 04 | Continuous access review | IAM Access Analyzer, unused/external access |

Every lab includes an objective, threat/risk statement, implementation steps, validation criteria, evidence checklist, and cleanup steps.

---

## Security Controls Demonstrated

| Control Objective | AWS Mechanism | Portfolio Evidence |
|---|---|---|
| Minimize privilege | Customer-managed IAM policies | Scoped JSON policy examples |
| Limit delegated admin | Permissions boundaries | Boundary policy example |
| Protect workforce access | IAM Identity Center + MFA | Architecture and governance docs |
| Avoid long-lived workload keys | IAM roles + STS | Lambda role lab |
| Protect multiple accounts | AWS Organizations + SCPs | Guardrail example |
| Detect unintended sharing | IAM Access Analyzer | Review lab |
| Create audit trail | AWS CloudTrail | Monitoring design |
| Govern cross-account access | Role trust policies | Cross-account lab |
| Support incident response | CloudTrail + credential revocation workflow | Threat model and response guidance |

---

## Important Security Rule: Never Commit Credentials

This repository must never contain:

- AWS secret access keys
- Session tokens
- Passwords
- MFA seed values or QR codes
- Private keys
- Real production account IDs when disclosure is unnecessary
- Sensitive screenshots containing credentials or confidential identifiers

Use placeholders such as:

```text
111122223333
444455556666
example-project-bucket
```

If a secret is ever committed, treat it as compromised and revoke/rotate it immediately; deleting it from the latest Git commit is not sufficient.

---

## Course Foundation vs. Enterprise Extension

The learning module provided the foundation: IAM users, groups, roles, policies, access keys, MFA, least privilege, cross-account roles, and policy structure.

This repository intentionally extends those fundamentals into current enterprise patterns:

- IAM Identity Center for centralized workforce access
- Federation and temporary credentials
- AWS Organizations and multi-account design
- SCP/RCP guardrails
- Permissions boundaries
- IAM Access Analyzer validation and access review
- CloudTrail-driven auditing
- Separation of duties and privileged access governance

This distinction is important: the repository is not a transcript of course material. It is an original security-engineering portfolio built from the concepts and expanded into enterprise architecture and controls.

---

## Professional Skills Demonstrated

This project is designed to demonstrate **enterprise experience-building** across:

- Cloud identity architecture
- Security requirements analysis
- Access-control design
- Technical documentation
- IAM policy authoring
- Cross-account trust design
- Risk-based security decisions
- Governance and control mapping
- Audit and detection planning
- Secure credential lifecycle management
- Change validation and evidence collection

---

## Current AWS Guidance Reflected in This Repository

The repository follows current AWS guidance to prefer federation and temporary credentials for human users, use roles for workloads, require MFA, apply least privilege, review unused access, validate policies, and use organizational guardrails in multi-account environments.

AWS-managed policies are useful for getting started, but they are not automatically least privilege for a specific workload. This repository therefore emphasizes customer-managed scoped policies for final designs.

---

## References

- AWS IAM Security Best Practices: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- AWS IAM Policy Evaluation Logic: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
- AWS IAM Access Analyzer: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
- AWS Organizations Best Practices: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html
- AWS IAM Identity Center: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

---

## Disclaimer

All policies, account IDs, resource names, and architecture examples in this repository are educational examples. They must be reviewed, tested, and adapted before use in any real AWS environment.