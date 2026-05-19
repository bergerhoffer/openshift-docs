# Security and compliance - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-05-19  
**Source:** `_topic_maps/_topic_map.yml` (book: `security`, distro: `openshift-enterprise`)  
**JTBD Records:** 135 (15 `main_job`, 120 `user_story`)  
**Main Jobs:** 15 (rolled up from 122 assemblies)

---

## Current Structure (Feature-Based)

Organized by product area, Operator name, and technical component. Users navigate by *what the documentation is about* (a feature or Operator), not *what they are trying to accomplish*.

```
Security and compliance
├── Security and compliance overview
├── Container security
│   ├── Understanding container security
│   ├── Understanding host and VM security
│   ├── Hardening Red Hat Enterprise Linux CoreOS
│   ├── Container image signatures
│   ├── Understanding compliance
│   ├── Securing container content
│   ├── Using container registries securely
│   ├── Securing the build process
│   ├── Deploying containers
│   ├── Securing the container platform
│   ├── Securing networks
│   ├── Securing attached storage
│   └── Monitoring cluster events and logs
├── Configuring certificates
│   ├── Replacing the default ingress certificate
│   ├── Adding API server certificates
│   ├── Securing service traffic using service serving certificates
│   └── Updating the CA bundle
├── Certificate types and descriptions
│   └── (13 reference topics: API server, proxy, node, etcd, ingress, …)
├── Compliance Operator
│   ├── Overview, release notes, support
│   ├── Concepts (understanding, CRDs)
│   ├── Management (install, update, manage, uninstall)
│   └── Scan management (profiles, scans, tailor, results, remediation, advanced, troubleshooting, oc-compliance)
├── File Integrity Operator
│   └── (10 topics: overview through uninstall)
├── Security Profiles Operator
│   └── (11 topics: overview, seccomp, SELinux, audit logging, …)
├── NBDE Tang Server Operator
│   └── (6 topics: overview through Tang URL)
├── Understanding secrets management
├── cert-manager Operator for Red Hat OpenShift
│   └── (15 topics: install, ACME, Istio-CSR, trust-manager, …)
├── Zero Trust Workload Identity Manager
│   └── (11 topics: SPIRE, OIDC federation, …)
├── External Secrets Operator for Red Hat OpenShift
│   └── (10 topics: install, APIs, migration, …)
├── Viewing audit logs
├── Configuring the audit log policy
├── Configuring TLS security profiles
├── Configuring seccomp profiles
├── Allowing JavaScript-based access to the API server from additional hosts
├── Scanning pods for vulnerabilities
└── Network-Bound Disk Encryption (NBDE)
    ├── About disk encryption technology
    ├── Tang server installation considerations
    ├── Tang server encryption key management
    └── Disaster recovery considerations
```

**Top-level navigation items:** 19 (including nested section groups)  
**Leaf assemblies (openshift-enterprise):** 122  
**Organization pattern:** One section per Operator or technical domain; lifecycle tasks (install → configure → troubleshoot) repeated per product

---

## Proposed JTBD-Based Structure

Organized by user goals and workflow stages. Users navigate by *what they need to accomplish*, then drill into Operator-specific paths.

### Getting Started

**Job 1: Understand the Security and Compliance Landscape**  
  When: Responsible for cluster security and need a map of controls  
  Personas: Cluster administrator  
  → Lines 1-496: Security and compliance overview

### Choose Your Approach

**Job 2: Understand Compliance Requirements**  
  When: Regulatory or governance obligations apply  
  Personas: Compliance officer, Cluster administrator  
  → Lines 3078-3549: Understanding compliance

**Job 3: Secure the Container Supply Chain and Runtime**  
  When: Running containerized workloads end-to-end  
  Personas: Platform engineer, Cluster administrator  
  - Container model and host security (12 assemblies consolidated under one job)
  - Image trust, registries, build, deploy, platform, network, storage, monitoring

### Secure Your Environment

**Job 4: Assess and Remediate Cluster Compliance**  
  When: Automated compliance assessment is required  
  Personas: Cluster administrator, Compliance officer  
  - Compliance Operator lifecycle (17 assemblies: install → scan → remediate → troubleshoot)

**Job 5: Detect Unauthorized Node File Changes**  
  When: Node integrity evidence is needed for audits or IR  
  Personas: Security engineer, Cluster administrator  
  - File Integrity Operator (10 assemblies)

**Job 6: Enforce Workload Security Profiles**  
  When: seccomp/SELinux enforcement is required  
  Personas: Platform engineer, Cluster administrator  
  - Security Profiles Operator (11 assemblies)

### Set Up & Configure

**Job 7: Manage Platform TLS Certificates**  
  When: Organizational PKI must replace default cluster TLS  
  Personas: Cluster administrator  
  - Ingress, API server, service serving certs, CA bundle (4 assemblies)

**Job 9: Automate Certificate Lifecycle**  
  When: High-volume issuance and renewal is needed  
  Personas: Platform engineer  
  - cert-manager Operator (15 assemblies)

**Job 10: Protect Data at Rest with NBDE**  
  When: Network-bound disk encryption is mandated  
  Personas: Cluster administrator  
  - NBDE Tang Server Operator + NBDE planning topics (10 assemblies)

**Job 11: Establish Zero-Trust Workload Identity**  
  When: SPIFFE/SPIRE-based workload authentication is adopted  
  Personas: Security architect, Platform engineer  
  - Zero Trust Workload Identity Manager (11 assemblies)

**Job 12: Sync Secrets from External Vaults**  
  When: Secrets live in external vaults, not in-cluster  
  Personas: Platform engineer  
  - Secrets management overview + External Secrets Operator (10 assemblies)

### Reference

**Job 8: Understand Cluster Certificate Architecture**  
  When: Troubleshooting TLS or planning rotation  
  Personas: Platform engineer  
  - Certificate types and descriptions (13 reference assemblies)

### Observe System State

**Job 13: Audit and Investigate Cluster Activity**  
  When: Accountability and investigation are required  
  Personas: Security engineer, Cluster administrator  
  - Audit log view + audit policy (2 assemblies)

### Confirm Readiness

**Job 14: Harden Cluster Security Defaults**  
  When: Production hardening before go-live  
  Personas: Cluster administrator  
  - TLS security profiles, seccomp profiles, JavaScript API access (3 assemblies)

**Job 15: Scan Workloads for Vulnerabilities**  
  When: Image risk must be assessed before production  
  Personas: Cluster administrator  
  - Pod vulnerability scanning (1 assembly)

---

## Key Differences

### Current Structure (Feature-Based)

| Aspect | Detail |
|--------|--------|
| **Organized by** | Operators, components, and technical domains |
| **Top-level navigation** | 19 section groups |
| **Leaf topics** | 122 assemblies |
| **User journey** | Pick an Operator or domain → read linear lifecycle docs |
| **Cross-cutting goals** | Split across multiple sections (e.g., TLS in 3 places) |

### Proposed Structure (JTBD-Based)

| Aspect | Detail |
|--------|--------|
| **Organized by** | User goals and workflow stages (Plan → Secure → Configure → Observe → Confirm) |
| **Top-level navigation** | 15 main jobs |
| **Implementation paths** | 120 user stories nested under main jobs |
| **User journey** | State your goal → follow job → choose Operator path |
| **Cross-cutting goals** | Consolidated (e.g., all certificate work under Jobs 7–9) |

### Hierarchy Levels

| Level | Current | Proposed |
|-------|---------|----------|
| **Level 1** | Operator / feature name | Main job (outcome) |
| **Level 2** | Assembly title (task-oriented) | Themed user story group |
| **Level 3** | Procedures inside modules | Line-referenced procedures |

---

## Example: Content Consolidation

### TLS and certificates (fragmented today)

**Current (3 separate top-level sections):**

- Configuring certificates (4 procedural topics)
- Certificate types and descriptions (13 reference topics)
- cert-manager Operator for Red Hat OpenShift (15 topics)

**Proposed (one workflow, three jobs):**

- **Job 7:** Manage platform TLS (replace ingress, API, service certs)
- **Job 8:** Understand certificate architecture (reference when needed)
- **Job 9:** Automate lifecycle with cert-manager

**Benefit:** Users with a TLS goal start at Job 7; reference and automation are linked prerequisites, not unrelated book sections.

---

### Compliance (concept vs. tool split)

**Current:**

- Understanding compliance (under Container security)
- Compliance Operator (separate 17-topic section)

**Proposed:**

- **Job 2:** Understand compliance requirements (concept)
- **Job 4:** Assess and remediate with Compliance Operator (execution)

**Benefit:** Concept before tooling; audit prep path is Jobs 2 → 4 → 13.

---

### seccomp (duplicated concepts)

**Current:**

- Managing seccomp profiles (Security Profiles Operator)
- Configuring seccomp profiles (book-root topic)

**Proposed:**

- **Job 6:** Operator-managed seccomp/SELinux profiles
- **Job 14:** Cluster-wide seccomp defaults and hardening

**Benefit:** Distinguishes workload profiles (SPO) from cluster defaults (hardening job).

---

## Navigation Improvement

| Metric | Current | Proposed | Change |
|--------|---------|----------|--------|
| Top-level items | 19 section groups | 15 main jobs | **21% fewer** top-level choices |
| Goal-first entry | No — feature-first | Yes — Quick Navigation by intent | Added |
| Certificate content entry points | 3 separate sections | 3 linked jobs (7→8→9) | Consolidated path |
| Operator install docs | 7 isolated Operator sections | Grouped under 6 security jobs | Thematic grouping |
| Typical click depth to task | 3–4 (book → Operator → subdir → assembly) | 2–3 (job → user story → assembly) | **~1 fewer level** |

**Benefit:** Users who know their goal (e.g., “run compliance scans”) land on Job 4 directly instead of scanning 19 top-level names for “Compliance Operator.”

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Plan / Get Started | ⚠️ Overview only; compliance concept buried in Container security | ✅ Jobs 1–2 | Improved |
| Secure (containers) | ✅ Container security section | ✅ Job 3 | Reorganized |
| Secure (compliance) | ⚠️ Split: concept + Operator | ✅ Jobs 2 + 4 | Improved |
| Secure (integrity/profiles) | ✅ Separate Operator sections | ✅ Jobs 5–6 | Reorganized |
| Configure (certificates) | ⚠️ Split across 3 sections | ✅ Jobs 7, 9 | Consolidated |
| Reference (certificates) | ✅ Dedicated section | ✅ Job 8 | Elevated as linked reference |
| Configure (secrets/identity) | ⚠️ Scattered Operators | ✅ Jobs 11–12 | Grouped by goal |
| Secure (encryption) | ⚠️ NBDE Operator + NBDE section separated | ✅ Job 10 | Consolidated |
| Observe (audit) | ⚠️ Two flat topics at book end | ✅ Job 13 | Grouped |
| Secure (hardening) | ⚠️ Flat topics (TLS, seccomp, API access) | ✅ Job 14 | Grouped |
| Confirm (vulnerabilities) | ✅ Single topic | ✅ Job 15 | Unchanged scope |
| Monitor | ⚠️ Per-Operator monitoring topics only | ⚠️ Embedded in Operator jobs | Partial |
| Troubleshoot | ⚠️ Per-Operator troubleshooting sections | ⚠️ Under Jobs 4–6, 9 | Partial |
| Upgrade | ⚠️ Release notes per Operator | ⚠️ Release notes per Operator | Gap remains |
| Migrate | ⚠️ ESO migration only | ⚠️ Job 12 (ESO only) | Partial |

### Coverage Summary

**Gaps in both structures:** Dedicated Monitor and Upgrade workflow stages at book level (content exists inside Operators but not as cross-cutting jobs).

**Gaps addressed by restructure:** Plan/compliance path, certificate consolidation, audit grouping, NBDE unification, goal-directed Quick Navigation.

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add Job: “Observe security posture” linking Operator monitoring + cluster logging | Medium |
| Upgrade | Add cross-Operator upgrade matrix or “Upgrade security Operators” job | Medium |
| etcd encryption | Overview links to etcd book; consider explicit job if in scope for this book | Low |

---

## Mapping: Current Sections → Proposed Jobs

| Current top-level section | Proposed job(s) |
|---------------------------|-----------------|
| Security and compliance overview | Job 1 |
| Container security | Jobs 2, 3, 14 (partial) |
| Configuring certificates | Job 7 |
| Certificate types and descriptions | Job 8 |
| Compliance Operator | Job 4 |
| File Integrity Operator | Job 5 |
| Security Profiles Operator | Job 6 |
| NBDE Tang Server Operator + Network-Bound Disk Encryption | Job 10 |
| Understanding secrets management + External Secrets Operator | Job 12 |
| cert-manager Operator | Job 9 |
| Zero Trust Workload Identity Manager | Job 11 |
| Viewing audit logs + Configuring audit log policy | Job 13 |
| TLS security profiles, seccomp profiles, JavaScript API access | Job 14 |
| Scanning pods for vulnerabilities | Job 15 |

---

## Structural Observations for Stakeholders

1. **Operator-centric layout matches product ownership** but forces users to know product names before goals. JTBD layout inverts this for readers while preserving Operator content as nested paths.

2. **The book grew by accretion** — seven security Operators plus platform topics — yielding 19 top-level entries. Fifteen outcome-based jobs reduce cognitive load without removing content.

3. **Reference material is separated today** (certificate types). The proposed structure keeps Job 8 as explicit reference, linked from Jobs 7 and 9, which mirrors how writers already cross-link but makes the reader path intentional.

4. **No content deletion implied** — this comparison is structural. All 122 assemblies remain; only navigation taxonomy changes.

---

## Related Artifacts

| File | Purpose |
|------|---------|
| `security-jtbd.jsonl` | Full JTBD records with evidence |
| `security-jtbd.csv` | Spreadsheet-friendly export |
| `security-toc-new_taxonomy.md` | Detailed proposed TOC with line references |
| `security-topicmap.json` | Parsed topic map (enterprise filter) |
| `security-combined.adoc` | Reduced source for line citations |
| `security-include-graph.json` | Module provenance |

---

*Generated by jtbd-compare from topic map + JTBD analysis output (`openshift-enterprise` / `security`).*
