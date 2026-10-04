# IAM Foundations

## Purpose

AWS Identity and Access Management (IAM) controls **who or what can access AWS** and **what actions that principal may perform**.

## Core Entities

### IAM User

An IAM user is an identity in one AWS account that can have long-term credentials. In modern enterprise designs, IAM users should not be the default for workforce access when federation and IAM Identity Center are available.

### IAM User Group

A user group is a collection of IAM users used to simplify permission assignment. Groups are useful in legacy or account-local IAM-user models, but they do not replace enterprise federation.

### IAM Role

An IAM role is an assumable identity with permissions. Roles normally provide temporary credentials through AWS Security Token Service (STS) and are central to workload access and cross-account delegation.

### IAM Policy

A policy is a JSON permissions document. Common elements include:

- `Version`
- `Statement`
- `Effect`
- `Action`
- `Resource`
- `Condition`

## Authentication vs. Authorization

```text
Authentication = Who are you?
Authorization  = What are you allowed to do?
```

Authentication establishes the principal. Authorization evaluates whether that principal may perform a requested action on a resource under the current request context.

## IAM Policy Types Used in Enterprise Environments

- Identity-based policies
- Resource-based policies
- Permissions boundaries
- Session policies
- AWS Organizations Service Control Policies (SCPs)
- AWS Organizations Resource Control Policies (RCPs)

## Least Privilege

Least privilege means granting only the permissions needed for a defined task. A strong policy usually narrows:

1. **Action** — exact API operations.
2. **Resource** — exact Amazon Resource Names (ARNs) when supported.
3. **Condition** — contextual restrictions such as source network, tags, MFA state, or organization membership.

## Enterprise Takeaway

Knowing how to create an IAM user is foundational. Enterprise IAM maturity is demonstrated by reducing dependence on long-lived users and credentials, designing roles and federation, applying guardrails, validating policy behavior, and continuously reviewing access.
