# Security & authentication — Content Gaps

**Analysis date:** 2026-05-20

Gaps identified during JTBD extraction and consolidation of 155 assemblies (security + authentication).

## Gap summary

| Gap | Impact | Main job | Recommendation |
|-----|--------|----------|----------------|
| No dedicated parent topic for merged Security & authentication guide | High | All | Author new assembly index with JTBD quick navigation and links to Plan/Secure/Operate jobs |
| etcd encryption documented in etcd book, not security | Medium | Encrypt sensitive data at rest | Add user story with xref to etcd/etcd-encrypt.adoc from Job 9 parent topic |
| Certificate types are reference-heavy without decision path | Medium | Manage certificates and TLS | Add 'Choose a certificate strategy' concept module at start of Job 8 |
| Network security (policies, egress, IPsec) in Networking guide | Medium | Understand security layers; Enforce pod security | Related jobs links only (out of scope for merge); do not duplicate content |
| Dedicated/ROSA/HCP authentication variants | Medium | Control sign-in; RBAC | Keep distro conditionals; add user stories per platform in Job 2–3 |
| security/index.adoc intro blurb marked TODO | Low | Understand security layers | Complete overview aligned to Job 1 parent topic |
| RBAC book has only 2 extracted child records (large assembly) | Low | Assign permissions with RBAC | Split using-rbac into additional user_story records during content rewrite |
| Procedure-level granularity underrepresented (4 of 325) | Low | All | Re-tag step-heavy modules as procedure during editorial pass |

## Jobs with fewer than 5 mapped child records

- **Configure auditing and investigate security events:** 2 records — review for missing user_story splits
- **Assign and audit permissions with RBAC:** 2 records — review for missing user_story splits

## Cross-book links required

| External book | Topic | Link from job |
|---------------|-------|---------------|
| etcd | etcd encryption | Job 9 — Encrypt data at rest |
| Networking | Network policy, egress firewall, IPsec | Related jobs from Jobs 1, 5, 6 (not in merge scope) |

## Reference vs. procedure balance

| Job | Child records | Notes |
|-----|---------------|-------|
| Configure auditing and investigate security events | 2 | ~0 concept/reference-heavy sections |
| Detect vulnerabilities and unauthorized file changes | 28 | ~1 concept/reference-heavy sections |
| Demonstrate compliance with security profiles | 60 | ~1 concept/reference-heavy sections |
| Encrypt sensitive data at rest | 8 | ~0 concept/reference-heavy sections |
| Manage certificates and TLS for cluster services | 74 | ~56 concept/reference-heavy sections |
| Manage secrets and cloud provider credentials | 40 | ~0 concept/reference-heavy sections |
| Secure the container software supply chain | 8 | ~0 concept/reference-heavy sections |
| Enforce what pods are allowed to run | 37 | ~1 concept/reference-heavy sections |
| Configure workload and automation identities | 7 | ~1 concept/reference-heavy sections |
| Assign and audit permissions with RBAC | 2 | ~0 concept/reference-heavy sections |
| Control who can sign in to the cluster | 24 | ~0 concept/reference-heavy sections |
| Understand OCP security layers and shared responsibility | 23 | ~3 concept/reference-heavy sections |