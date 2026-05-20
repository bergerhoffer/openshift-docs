# Security and Compliance + Authentication and Authorization
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

*Source books: Security and compliance (`security/`), Authentication and authorization (`authentication/`) — unified job map*

---

## Guide Overview

**Purpose:** Help platform, cluster, and security teams secure OpenShift clusters end to end: from trusted workloads and hardened infrastructure through identity, access control, compliance evidence, and ongoing monitoring.

**Personas:** Platform administrator, Cluster administrator, Security/compliance officer, Security administrator

**Main Jobs:** 14 core jobs across 6 workflow stages

**Source:** `security-auth-combined.adoc` (155 topic-map assemblies, ~108k lines reduced)

---

## Quick Navigation

**I want to:**

- Lock down what runs on the cluster → Job 1: Secure the container supply chain (Secure)
- Harden nodes and the OS → Job 2: Harden cluster infrastructure (Secure)
- Control who can access the API → Job 5: Authenticate users and API clients (Secure)
- Connect corporate login (LDAP, OIDC) → Job 6: Integrate enterprise identity (Configure)
- Set project permissions and multitenancy → Job 7: Define and enforce access permissions (Secure)
- Limit pod privileges (PSA, SCC) → Job 8: Constrain workload security context (Secure)
- Manage TLS for routes and the API → Job 11: Manage platform TLS certificates (Configure)
- Automate certs and external secrets → Job 12: Operate certificate and secrets operators (Operate)
- Run CIS/compliance scans → Job 13: Demonstrate regulatory compliance (Confirm)
- Investigate who did what → Job 14: Monitor and investigate security activity (Monitor)

---

# Table of Contents

## Getting Started

### Job 1: Secure the container supply chain
*When bringing containerized workloads into production*

**Personas:** Platform administrator

**Requires:** Organizational policies for trusted image sources (recommended before compliance scans)

#### 1.1 Understand the security layers

**Goal:** Map host, platform, build, and runtime controls before implementing them.

→ Lines 523-900: Understanding container security  
  Source: Security book — Container security overview  
  - Trusted base images through CI/CD  
  - Vulnerability scanning and image replacement  
  - Links to authentication, networking, and compliance topics

→ Lines 3605-4100: Understanding compliance  
  Source: Security book — Compliance concepts  
  - Risk management and control frameworks

#### 1.2 Harden content, build, and deployment

**Goal:** Control what is built, where images come from, and what can be deployed.

→ Lines 4077-4894: Securing container content  
  Source: Security book — Container content

→ Lines 4895-5465: Using container registries securely  
  Source: Security book — Registries

→ Lines 5466-6722: Securing the build process / Deploying containers  
  Source: Security book — Build and deploy

#### 1.3 Verify image trust (Confirmation step)

**Goal:** Block unsigned or untrusted images at deploy time.

- **User story: Enable image signature verification** (Red Hat registries and signature policy)
  *Persona: Platform administrator*
  → Lines 2112-3100: Container image signatures  
    Source: Security book — `security-container-signature.adoc`

---

### Job 2: Harden cluster infrastructure
*When operating OpenShift on bare metal or virtualized infrastructure*

**Personas:** Platform administrator

#### 2.1 Secure hosts and the platform OS

**Goal:** Reduce attack surface on nodes running workloads.

→ Lines 1053-1610: Understanding host and VM security  
  Source: Security book — Host and VM security

→ Lines 1611-2100: Hardening Red Hat Enterprise Linux CoreOS / Fedora CoreOS  
  Source: Security book — `security-hardening.adoc`

---

## Secure Your Environment

### Job 3: Segment and protect networking and storage
*When workloads communicate inside and outside the cluster*

**Personas:** Platform administrator

**Related:** Job 7 (RBAC/multitenancy), Job 11 (TLS for ingress)

#### 3.1 Network isolation and traffic control

**Goal:** Limit lateral movement and control ingress/egress.

→ Lines 7335-7881: Securing networks  
  Source: Security book — Container security / networks  
  - Network namespaces, network policies, ingress/egress

#### 3.2 Storage security

**Goal:** Protect persistent data paths used by workloads.

→ Lines 7882-8379: Securing attached storage  
  Source: Security book — Container security / storage

---

### Job 4: Protect data at rest
*When persistent data must remain confidential if media is lost or stolen*

**Personas:** Platform administrator

#### 4.1 Plan disk encryption

**Goal:** Choose NBDE/Tang architecture and key management.

→ Lines ~82000-83400: About disk encryption technology / NBDE Tang Server Operator  
  Source: Security book — Network-Bound Disk Encryption, NBDE Tang Server Operator

---

### Job 5: Enforce runtime security profiles
*When defense-in-depth is required beyond RBAC and network policy*

**Personas:** Platform administrator

**Requires:** Job 8 — Constrain workload security context (PSA/SCC foundation)

#### 5.1 Operator-driven seccomp and SELinux

**Goal:** Apply organization-approved syscall and MAC profiles to workloads.

→ Lines ~38000-42000 (approx.): Security Profiles Operator overview and management  
  Source: Security book — `security_profiles_operator/`  
  - Seccomp and SELinux profiles  
  - Advanced audit logging (SPO)

#### 5.2 Cluster-wide hardening controls

**Goal:** Align API and workload TLS/seccomp baselines.

→ Related topics: Configuring TLS security profiles; Configuring seccomp profiles; Scanning pods for vulnerabilities  
  Source: Security book — cluster hardening assemblies

---

## Set Up & Configure

### Job 6: Authenticate users and API clients
*When users and automation interact with the cluster API*

**Personas:** Cluster administrator

**Timing:** BEFORE Job 7 (authorization) and Job 14 (meaningful audit attribution)

#### 6.1 Understand authentication model

**Goal:** Separate authentication (who) from authorization (what they may do).

→ Lines 83986-84650: Understanding authentication  
  Source: Authentication book — Users, groups, API authentication, OAuth server

→ Lines 6723-7300: Authentication and authorization (platform context)  
  Source: Security book — `security-platform.adoc` (cross-book)

#### 6.2 Configure OAuth server and clients

**Goal:** Enable secure interactive and programmatic login.

- **User story: Configure the internal OAuth server**
  *Persona: Cluster administrator*
  → Lines 84613-86727: Configuring the internal OAuth server / OAuth clients / access tokens  
    Source: Authentication book — OAuth configuration

#### 6.3 Retire bootstrap credentials (Conclude step)

**Goal:** Remove shared emergency admin after durable access exists.

- **User story: Remove the kubeadmin user**
  *Persona: Cluster administrator*  
  **Requires:** At least one other cluster-admin access path (Job 7)
  → Lines 95348-95823: Removing the kubeadmin user  
    Source: Authentication book

---

### Job 7: Integrate enterprise identity
*When the organization relies on corporate directories or external IdPs*

**Personas:** Cluster administrator

**Requires:** Job 6 — Authenticate users and API clients

#### 7.1 Choose an identity provider approach

**Goal:** Map enterprise IdP to OpenShift OAuth.

→ Lines 86728-87403: Understanding identity provider configuration  
  Source: Authentication book — IdP overview

**Options (by integration type):**

- **Option A: LDAP** (existing corporate directory)
  *Persona: Cluster administrator*
  → Lines 88928-103868: Configuring an LDAP identity provider / Syncing LDAP groups  
    Source: Authentication book — `identity_providers/`, `ldap-syncing.adoc`

- **Option B: OpenID Connect** (corporate SSO)
  *Persona: Cluster administrator*
  → Lines 92888-94328: Configuring an OpenID Connect identity provider / Enabling direct authentication with OIDC  
    Source: Authentication book — OIDC and external-auth

- **Option C: Other IdPs** (htpasswd, GitHub, Google, GitLab, Keystone, request-header, basic auth)
  → Lines 87404-93350: Configuring identity providers (per-provider assemblies)  
    Source: Authentication book — `identity_providers/`

---

### Job 8: Define and enforce access permissions
*When multiple teams share a cluster*

**Personas:** Cluster administrator

**Requires:** Job 6 — Authenticate users and API clients

#### 8.1 RBAC rules, roles, and bindings

**Goal:** Enforce least privilege per project and cluster.

→ Lines 94329-95300: Using RBAC to define and apply permissions  
  Source: Authentication book — `using-rbac.adoc`

#### 8.2 Multitenancy and project isolation

**Goal:** Combine RBAC with namespace/project boundaries.

→ Lines 6723-7300: Isolating containers with multitenancy  
  Source: Security book — `security-platform.adoc` (cross-book)

---

### Job 9: Constrain workload security context
*When diverse workloads share infrastructure*

**Personas:** Platform administrator

**Requires:** Job 8 — Define and enforce access permissions

#### 9.1 Pod Security Admission

**Goal:** Enforce Kubernetes pod security standards per namespace.

→ Lines 100315-101090: Understanding and managing pod security admission  
  Source: Authentication book — PSA modes, profiles, SCC reconciliation

#### 9.2 Security context constraints and admission

**Goal:** Reject overly privileged pods at admission time.

- **User story: Manage security context constraints**
  *Persona: Platform administrator*
  → Lines 98923-100314: Managing security context constraints  
    Source: Authentication book

- **User story: Tune admission plugins and SCC defaults**
  *Persona: Platform administrator*
  → Lines 6723-7230: Protecting control plane with admission plugins  
    Source: Security book — `security-platform.adoc`

---

### Job 10: Manage machine identities for applications
*When applications and operators need programmatic API access*

**Personas:** Platform administrator

**Requires:** Job 6 — Authenticate users and API clients; Job 8 — RBAC for binding permissions

#### 10.1 Service accounts and tokens

**Goal:** Provision automation identities without sharing human credentials.

→ Lines 95824-98920: Service accounts, bound tokens, token scoping, OAuth clients  
  Source: Authentication book — service account assemblies

#### 10.2 Cloud credential modes (public cloud)

**Goal:** Limit cloud IAM exposure for platform components.

- **User story: Configure Cloud Credential Operator modes**
  *Persona: Platform administrator* (cloud deployments)
  → Lines 103868-107997: About the Cloud Credential Operator / mint / passthrough / manual modes  
    Source: Authentication book — `managing_cloud_provider_credentials/`

---

### Job 11: Manage platform TLS certificates
*When cluster components and routes must trust custom or corporate CAs*

**Personas:** Cluster administrator

#### 11.1 Replace and configure cluster certificates

**Goal:** Present trusted TLS for API, ingress, and service traffic.

→ Lines 8918-11453: Replacing ingress certificate / API server / service serving certs / CA bundle  
  Source: Security book — `certificates/`

#### 11.2 Understand certificate types (Reference)

**Goal:** Navigate PKI roles across control plane components.

→ Lines 11454-17401: Certificate types and descriptions (API, etcd, ingress, OLM, nodes, etc.)  
  Source: Security book — `certificate_types_descriptions/`

---

### Job 12: Operate certificate and secrets operators
*When workloads need automated TLS or external secret sources*

**Personas:** Platform administrator

**Requires:** Job 11 — Manage platform TLS certificates (conceptual foundation)

#### 12.1 cert-manager Operator

**Goal:** Issue, renew, and attach certificates to routes and workloads.

→ Lines ~43000-48000 (approx.): cert-manager Operator install, ACME issuers, securing routes  
  Source: Security book — `cert_manager_operator/`

#### 12.2 External Secrets Operator

**Goal:** Sync secrets from external vaults into the cluster.

→ Lines ~48000-52000 (approx.): External Secrets Operator  
  Source: Security book — `external_secrets_operator/`

→ Related: Understanding secrets management  
  Source: Security book — `understanding-secrets-management.adoc`

---

## Confirm & Comply

### Job 13: Demonstrate regulatory compliance
*When the organization must meet regulatory or internal control frameworks*

**Personas:** Security/compliance officer

**Requires:** Job 1 — Secure the container supply chain (baseline posture)

#### 13.1 Compliance Operator lifecycle

**Goal:** Install, configure, and run benchmark scans.

→ Lines 17402-24734: Compliance Operator overview, concepts, installation, management  
  Source: Security book — `compliance_operator/`

#### 13.2 Run scans and remediate (Confirmation step)

**Goal:** Produce CIS/profile results and track fixes.

- **User story: Run Compliance Operator scans**
  *Persona: Security/compliance officer*
  → Lines 24735-27900: Compliance Operator scans, tailoring, remediation, troubleshooting  
    Source: Security book — `co-scans/`

---

## Track & Investigate

### Job 14: Monitor and investigate security activity
*When investigating incidents or preparing audit evidence*

**Personas:** Cluster administrator, Security administrator

**Related:** Job 13 (compliance evidence), Job 6 (authenticated actors in audit logs)

#### 14.1 Cluster events and monitoring

**Goal:** Observe security-relevant platform activity.

→ Lines 8380-8917: Monitoring cluster events and logs  
  Source: Security book — Container security / monitoring

#### 14.2 API audit logs

**Goal:** Reconstruct API actions with user and resource context.

→ Lines 76354-77115: Viewing audit logs  
  Source: Security book — `audit-log-view.adoc`

→ Lines 77116-78000: Configuring the audit log policy  
  Source: Security book — `audit-log-policy-config.adoc`

#### 14.3 File integrity monitoring

**Goal:** Detect unexpected node file changes.

- **User story: Deploy the File Integrity Operator**
  *Persona: Security administrator*
  → Lines 30646-35000 (approx.): File Integrity Operator  
    Source: Security book — `file_integrity_operator/`

---

## Appendices

### A. Security operator map

| Operator / capability | Primary jobs | Book |
|----------------------|--------------|------|
| Compliance Operator | Job 13 | Security |
| File Integrity Operator | Job 14 | Security |
| Security Profiles Operator | Job 5 | Security |
| cert-manager Operator | Job 12 | Security |
| External Secrets Operator | Job 12 | Security |
| NBDE Tang Server Operator | Job 4 | Security |
| Cloud Credential Operator | Job 10 | Authentication |
| Built-in OAuth / RBAC / PSA / SCC | Jobs 6–9 | Authentication (+ Security platform) |

### B. Identity provider selection guide

| Approach | When to use | Documentation anchor |
|----------|-------------|----------------------|
| LDAP + group sync | Corporate directory is LDAP/AD | Job 7, Option A |
| OIDC / SSO | Organization standardizes on OIDC | Job 7, Option B |
| htpasswd | Small clusters, break-glass local users | Authentication — htpasswd IdP |
| Request header | Behind enterprise SSO proxy | Authentication — request-header IdP |
| GitHub / GitLab / Google | Developer-centric identity | Authentication — social IdP assemblies |

### C. Workflow coverage analysis

| Stage | Coverage | Jobs |
|-------|----------|------|
| Get Started | ✅ | Jobs 1–2 |
| Secure | ✅ | Jobs 3–5, 8–9 |
| Configure | ✅ | Jobs 6–7, 10–11 |
| Administer | ✅ | Job 10 |
| Operate | ✅ | Job 12 |
| Confirm | ✅ | Job 13 |
| Monitor | ✅ | Job 14 |
| Troubleshoot | ⚠️ Partial | Scattered in operator troubleshooting topics (not standalone main jobs) |
| Migrate | ❌ | External Secrets migration topic only; no cluster migration job |
| Upgrade | ⚠️ Partial | Operator update assemblies; no unified upgrade main job |

### D. Cross-book dependency map

```
Job 6 (Authenticate) ──► Job 7 (IdP) ──► Job 8 (RBAC)
                              │
Job 1 (Supply chain) ─────────┼──► Job 13 (Compliance)
                              │
Job 8 (RBAC) ──► Job 9 (PSA/SCC) ──► Job 5 (Runtime profiles)
                              │
Job 6 ──► Job 14 (Audit logs attribute actors)
Job 11 (TLS) ──► Job 12 (cert-manager / ESO)
```

---

## Navigation Guide

### By user journey

**Platform administrator — secure a new production cluster:**

1. Job 1: Secure the container supply chain  
2. Job 2: Harden cluster infrastructure  
3. Job 6: Authenticate users and API clients  
4. Job 7: Integrate enterprise identity  
5. Job 8: Define and enforce access permissions  
6. Job 9: Constrain workload security context  
7. Job 3: Segment and protect networking and storage  
8. Job 11: Manage platform TLS certificates  
9. Job 13: Demonstrate regulatory compliance  
10. Job 14: Monitor and investigate security activity  

**Cluster administrator — enable enterprise login and least privilege:**

1. Job 6: Authenticate users and API clients  
2. Job 7: Integrate enterprise identity (LDAP or OIDC user story)  
3. Job 8: Define and enforce access permissions  
4. User story: Remove kubeadmin (Job 6)  

**Security/compliance officer — audit readiness:**

1. Job 1: Secure the container supply chain  
2. Job 13: Demonstrate regulatory compliance (Compliance Operator scans user story)  
3. Job 14: Monitor and investigate security activity  

**Security administrator — detect tampering and investigate:**

1. Job 14: Monitor and investigate security activity (audit logs + File Integrity Operator user story)  

---

## Document Statistics

**Workflow coverage:**

- Secure: 7 jobs (1, 2, 3, 5, 8, 9, partial 6)  
- Configure: 4 jobs (6, 7, 10, 11)  
- Operate: 1 job (12)  
- Administer: 1 job (10)  
- Confirm: 1 job (13)  
- Monitor: 1 job (14)  

**Main jobs:** 14  
**User stories:** 10 (nested under parent jobs in TOC)  
**Topic-map assemblies:** 155 (123 security + 32 authentication)  
**Combined source lines:** ~107,997  

**Generated from:** `security-auth-jtbd.jsonl` (24 JTBD records, validation 24 pass / 0 flagged)

**Output path:** `analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md`
