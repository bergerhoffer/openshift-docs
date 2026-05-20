# Security and Compliance + Authentication and Authorization — TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis date:** 2026-05-19  
**Source:** `_topic_maps/_topic_map.yml` (OpenShift Container Platform)  
**JTBD records:** 24 (`security-auth-jtbd.jsonl`)  
**Main jobs:** 14 (unified across both books)  
**Assemblies analyzed:** 155 (123 security + 32 authentication)

---

## Current Structure (Feature-Based)

Two separate books in the topic map. Navigation is **product- and operator-centric**: users pick a book, then a section or Operator, then leaf topics.

### Security and compliance (`security/`) — 19 top-level sections, 123 topics

- Security and compliance overview
- **Container security** (14 topics: understanding, hosts/VMs, hardening, signatures, compliance concepts, content, registries, build, deploy, platform, networks, storage, monitoring)
- **Configuring certificates** (4 topics)
- **Certificate types and descriptions** (13 reference topics: API server, proxy, service CA, nodes, bootstrap, etcd, OLM, ingress, control plane, …)
- **Compliance Operator** (nested: concepts, management, scan management — ~20 topics)
- **File Integrity Operator** (10 topics: overview, release notes, support, install, update, understand, configure, advanced, troubleshoot, uninstall)
- **Security Profiles Operator** (11 topics)
- **NBDE Tang Server Operator** (6 topics)
- Understanding secrets management
- **cert-manager Operator for Red Hat OpenShift** (14 topics)
- **Zero Trust Workload Identity Manager** (11 topics)
- **External Secrets Operator for Red Hat OpenShift** (10 topics)
- Viewing audit logs
- Configuring the audit log policy
- Configuring TLS security profiles
- Configuring seccomp profiles
- Allowing JavaScript-based access to the API server from additional hosts
- Scanning pods for vulnerabilities
- **Network-Bound Disk Encryption (NBDE)** (4 topics)

### Authentication and authorization (`authentication/`) — 20 top-level sections, 32 topics

- Authentication and authorization overview
- Understanding authentication
- Configuring the internal OAuth server
- Configuring OAuth clients
- Managing user-owned OAuth access tokens
- Understanding identity provider configuration
- **Configuring identity providers** (9 IdP-specific topics: htpasswd, Keystone, LDAP, basic auth, request-header, GitHub, GitLab, Google, OIDC)
- Enabling direct authentication with an OIDC identity provider
- Using RBAC to define and apply permissions
- Removing the kubeadmin user
- Understanding and creating service accounts
- Using service accounts in applications
- Using a service account as an OAuth client
- Scoping tokens
- Using bound service account tokens
- Managing security context constraints
- Understanding and managing pod security admission
- Impersonating the system:admin user
- Syncing LDAP groups
- **Managing cloud provider credentials** (5 topics: CCO overview, mint, passthrough, manual, short-term creds)

### Current-structure pain points

| Issue | Example |
|-------|---------|
| **Book boundary** | RBAC/multitenancy appears in *both* books (`authentication/using-rbac` and `security/security-platform`) |
| **Operator silos** | Compliance, FIO, SPO, cert-manager, ESO each repeat install → configure → uninstall |
| **IdP fragmentation** | Nine sibling topics under “Configuring identity providers” with no decision guide |
| **Certificate sprawl** | 4 procedural + 13 reference certificate topics without a single “manage PKI” entry point |
| **Goal vs. component** | User seeking “CIS scan results” must find Compliance Operator → scan management → scans |

---

## Proposed JTBD-Based Structure

Unified job map (both books). **14 main jobs** in workflow order; **10 user stories** for common implementation paths.

### Getting Started

**Job 1: Secure the container supply chain**  
When: Bringing containerized workloads into production  
Personas: Platform administrator  
→ Container security lifecycle (understand, content, registries, build, deploy, signatures)

**Job 2: Harden cluster infrastructure**  
When: Operating on bare metal or VMs  
→ Host/VM security, RHCOS/FCOS hardening

### Secure Your Environment

**Job 3: Segment and protect networking and storage**  
**Job 4: Protect data at rest** (NBDE/Tang)  
**Job 5: Enforce runtime security profiles** (SPO, TLS/seccomp, vulnerability scan)

### Set Up & Configure

**Job 6: Authenticate users and API clients** (+ OAuth config, remove kubeadmin user story)  
**Job 7: Integrate enterprise identity** (LDAP, OIDC, other IdPs as options)  
**Job 8: Define and enforce access permissions** (RBAC + multitenancy from both books)  
**Job 9: Constrain workload security context** (PSA, SCC, admission plugins)  
**Job 10: Manage machine identities** (service accounts, tokens, CCO user story)  
**Job 11: Manage platform TLS certificates** (+ certificate types reference)  
**Job 12: Operate certificate and secrets operators** (cert-manager, ESO)

### Confirm & Comply

**Job 13: Demonstrate regulatory compliance** (Compliance Operator + scans user story)

### Track & Investigate

**Job 14: Monitor and investigate security activity** (audit logs, monitoring, FIO user story)

*Full detail with line references: `security-auth-toc-new_taxonomy.md`*

---

## Key Differences

### Current structure (feature-based)

| Aspect | Characteristic |
|--------|----------------|
| **Organized by** | Product book, Operator name, technical component |
| **Top-level navigation** | 39 sections across 2 books (19 + 20) |
| **Leaf topics** | 155 assemblies |
| **User journey** | “Which Operator?” → “Install or configure?” → leaf topic |
| **Cross-cutting goals** | Split across books (e.g., access control, audit, identity) |

### Proposed structure (JTBD-based)

| Aspect | Characteristic |
|--------|----------------|
| **Organized by** | User goals and workflow stage |
| **Top-level navigation** | 14 main jobs (unified) |
| **Implementation paths** | 10 user stories nested under jobs |
| **User journey** | “What do I need to accomplish?” → job → option/path → source sections |
| **Cross-cutting goals** | Explicitly merged (e.g., Job 8 pulls RBAC from both books) |

---

## Navigation Improvement

| Metric | Current | Proposed | Change |
|--------|---------|----------|--------|
| Books to search | 2 | 1 (unified map) | Single goal index |
| Top-level sections | 39 | 14 main jobs | **64% fewer** top-level choices |
| “I want LDAP login” | Auth book → IdP section → LDAP topic | Quick nav → Job 7 → Option A | 3 hops vs. 2 |
| “I want CIS compliance” | Security → Compliance Operator → co-scans → scans | Quick nav → Job 13 | Operator depth reduced |
| “I want RBAC + project isolation” | Auth (RBAC) + Security (platform) | Job 8 (single job) | **Consolidated** |

**Benefit:** Goal-directed users reach relevant content in **2–3 decisions** (pick job → pick path → open section) instead of guessing book and Operator name first.

---

## Workflow Coverage Comparison

| Stage | Current (combined) | Proposed | Gap status |
|-------|-------------------|----------|------------|
| Get Started / Understand | ⚠️ Scattered (overviews + container security intro) | ✅ Jobs 1–2 | Improved |
| Secure (supply chain, hosts, network) | ✅ Container security + NBDE + profiles | ✅ Jobs 1–5 | Reorganized |
| Configure (identity, RBAC, certs) | ✅ Split across 2 books, many Operators | ✅ Jobs 6–12 | Consolidated |
| Administer (service accounts) | ✅ Auth book | ✅ Job 10 | Clearer |
| Operate (cert/secrets operators) | ✅ Per-Operator sections | ✅ Job 12 | Grouped |
| Confirm (compliance) | ✅ Compliance Operator subtree | ✅ Job 13 | Elevated to goal |
| Monitor / audit | ⚠️ Audit + monitoring + FIO in separate top-level sections | ✅ Job 14 | Consolidated |
| Troubleshoot | ⚠️ Per-Operator “Troubleshooting” topics | ⚠️ Not a main job | Gap remains |
| Upgrade | ⚠️ Per-Operator “Updating” topics | ⚠️ Not a main job | Gap remains |
| Migrate | ⚠️ ESO migration topic only | ❌ No main job | Gap remains |
| Reference (cert types) | ✅ 13 sibling reference topics | ✅ Job 11.2 (nested reference) | Reorganized |

### Gaps identified (both structures)

| Gap | Recommendation |
|-----|----------------|
| **Troubleshooting** | Add cross-operator “Troubleshoot security issues” job linking CO/FIO/SPO/auth troubleshooting topics |
| **Upgrade** | Add “Upgrade security Operators” consumption job or surface under Operate |
| **Zero Trust Workload Identity Manager** | Not in JTBD records — add user story under Job 10 or Job 12 if in scope |
| **Emotional / audit-confidence jobs** | Optional Job 13 outcome: “feel confident in audits” (emotional job type) |

---

## Example: Content Consolidation

### Identity providers (fragmented → goal-based)

**Current (9 sibling topics under one section):**

- Configuring an htpasswd identity provider  
- Configuring a Keystone identity provider  
- Configuring an LDAP identity provider  
- … (GitHub, GitLab, Google, OIDC, etc.)

**Proposed:**

**Job 7: Integrate enterprise identity**  
- Option A: LDAP (+ group sync)  
- Option B: OIDC / SSO  
- Option C: Other IdPs (reference table in TOC appendix)

**Benefit:** Decision-first navigation; procedural topics remain as sources, not as the primary TOC shape.

---

### Certificate management (reference sprawl → layered job)

**Current:**

- Configuring certificates (4 procedural topics)  
- Certificate types and descriptions (13 parallel reference topics)

**Proposed:**

**Job 11: Manage platform TLS certificates**  
- 11.1 Replace and configure cluster certificates (procedural)  
- 11.2 Understand certificate types (reference, nested)

**Benefit:** One entry point for PKI goals; reference material is clearly subordinate.

---

### Access control (cross-book → single job)

**Current:**

- `authentication/using-rbac.adoc`  
- `security/container_security/security-platform.adoc` (multitenancy, admission, SCC overview, OAuth overview)

**Proposed:**

**Job 8: Define and enforce access permissions** (RBAC + multitenancy)  
**Job 9: Constrain workload security context** (PSA, SCC, admission — auth + security)

**Benefit:** Matches how admins actually work; removes “which book?” for platform access control.

---

## Mapping: Current Top-Level Sections → Proposed Jobs

| Current section (book) | Primary proposed job(s) |
|------------------------|-------------------------|
| Container security | Jobs 1, 3, 8 (partial) |
| Configuring certificates + Certificate types | Job 11 |
| Compliance Operator | Job 13 |
| File Integrity Operator | Job 14 (user story) |
| Security Profiles Operator | Job 5 |
| NBDE / NBDE Tang Server Operator | Job 4 |
| cert-manager / External Secrets / secrets management | Job 12 |
| Audit logs / audit policy / monitoring | Job 14 |
| TLS seccomp / pod vulnerability scan | Job 5 |
| Zero Trust Workload Identity Manager | *Not mapped in JTBD set* |
| Understanding authentication / OAuth / IdPs | Jobs 6, 7 |
| RBAC / SCC / PSA / service accounts | Jobs 8, 9, 10 |
| Cloud Credential Operator | Job 10 (user story) |

---

## Recommendations for Stakeholders

1. **Keep both books physically** but add a **unified “Security and access” landing page** using the 14-job quick navigation from the JTBD TOC.  
2. **Cross-link at consolidation points** — especially Job 8 (RBAC + multitenancy) and Job 9 (PSA/SCC) — so users are not sent to the “wrong” book.  
3. **Add an IdP decision table** (already drafted in JTBD TOC appendix B) to the authentication overview or Job 7 hub.  
4. **Collapse Operator boilerplate** in navigation (install/update/uninstall) under job-based hubs while keeping full Operator TOCs for maintenance.  
5. **Extend JTBD analysis** with user stories for Zero Trust Workload Identity Manager and a cross-cutting troubleshooting job if those goals matter for the next revision.

---

## Source Artifacts

| Artifact | Path |
|----------|------|
| JTBD records | `analysis/topicmap/security-auth/security-auth-jtbd.jsonl` |
| JTBD TOC | `analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md` |
| Combined reduced source | `analysis/topicmap/security-auth/security-auth-combined.adoc` |
| Topic map extract | `analysis/topicmap/security-auth/security-auth-topicmap.json` |
| This comparison | `analysis/topicmap/security-auth/security-auth-comparison.md` |
