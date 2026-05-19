# Security and compliance — Consolidation Report

**Document:** `security` book (`_topic_maps/_topic_map.yml`, distro: `openshift-enterprise`)  
**JTBD Records:** 15 main jobs, 120 user stories (from 122 assemblies) → **15 final jobs** (no merges required)

---

## Executive Summary

### What's Changing

The **Security and compliance** book is organized today by **product and technical domain**: each security Operator (Compliance, File Integrity, Security Profiles, cert-manager, and others) has its own top-level section, alongside chapters for container security, certificates, and standalone hardening topics. That structure matches how features are built and owned, but it does not match how administrators and security engineers work through a problem. A reader preparing for an audit must discover that compliance *concepts* live under Container security while compliance *scans* live under Compliance Operator, and that TLS guidance is split across three separate sections.

The proposed restructure organizes the same 122 assemblies under **15 outcome-based jobs** grouped by workflow stage (plan → secure → configure → observe → confirm). Users enter through goals—“run compliance scans,” “replace ingress certificates,” “sync secrets from a vault”—and follow nested paths to the Operator or assembly they need. No assemblies are removed; only the navigation taxonomy changes.

### Key Improvements

- **Goal-first entry:** Quick Navigation maps common intents to Jobs 1–15 instead of requiring familiarity with seven Operator names.
- **Certificate path unified:** Three top-level sections (configure, types, cert-manager) become Jobs 7 → 8 → 9 with an explicit workflow link.
- **Compliance concept before tool:** “Understanding compliance” moves from Container security into Job 2, paired with Compliance Operator execution in Job 4.
- **NBDE consolidated:** NBDE Tang Server Operator and Network-Bound Disk Encryption sections merge under Job 10 (one encryption goal).
- **Audit topics grouped:** Flat audit assemblies at book end become Job 13 (accountability and investigation).
- **Hardening cluster grouped:** TLS profiles, seccomp defaults, and API access constraints unite under Job 14 (production hardening).
- **21% fewer top-level choices:** 19 section groups → 15 main jobs.
- **Operator lifecycle preserved:** Install → configure → troubleshoot sequences remain as nested approaches within each job, not deleted.

---

## Current Structure (Feature-Based)

Extracted from `_topic_maps/_topic_map.yml` (Security and compliance book, `openshift-enterprise` filter).

- **Security and compliance overview** — Book orientation; links to major domains
- **Container security** — Supply chain and runtime (13 assemblies)
  - Understanding, host/VM security, RHCOS hardening, image signatures, compliance concepts, content, registries, build, deploy, platform, network, storage, monitoring
- **Configuring certificates** — Procedural TLS for ingress, API, service serving (4 assemblies)
- **Certificate types and descriptions** — Reference for each certificate class (13 assemblies)
- **Compliance Operator** — Full operator lifecycle (17 assemblies)
  - Concepts, management, scan management subdirs
- **File Integrity Operator** — Node file integrity (10 assemblies)
- **Security Profiles Operator** — seccomp, SELinux, audit logging (11 assemblies)
- **NBDE Tang Server Operator** — Tang server deployment (6 assemblies)
- **Understanding secrets management** — Secrets Operators overview (1 assembly)
- **cert-manager Operator for Red Hat OpenShift** — Automated TLS (15 assemblies)
- **Zero Trust Workload Identity Manager** — SPIFFE/SPIRE identity (11 assemblies)
- **External Secrets Operator for Red Hat OpenShift** — External vault sync (10 assemblies)
- **Viewing audit logs** — Audit log review (1 assembly)
- **Configuring the audit log policy** — Audit policy (1 assembly)
- **Configuring TLS security profiles** — Cluster TLS profiles (1 assembly)
- **Configuring seccomp profiles** — Cluster seccomp defaults (1 assembly)
- **Allowing JavaScript-based access to the API server** — API access hardening (1 assembly)
- **Scanning pods for vulnerabilities** — Image/pod scanning (1 assembly)
- **Network-Bound Disk Encryption (NBDE)** — Encryption planning without operator (4 assemblies)

**Total:** 19 top-level section groups, 122 leaf assemblies, organized by **feature, Operator, and component name**.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand & Plan**
  - Job 1: Understand the Security and Compliance Landscape
  - Job 2: Understand Compliance Requirements
- **Secure**
  - Job 3: Secure the Container Supply Chain and Runtime
  - Job 4: Assess and Remediate Cluster Compliance
  - Job 5: Detect Unauthorized Node File Changes
  - Job 6: Enforce Workload Security Profiles
  - Job 10: Protect Data at Rest with NBDE
  - Job 14: Harden Cluster Security Defaults
- **Set Up & Configure**
  - Job 7: Manage Platform TLS Certificates
  - Job 9: Automate Certificate Lifecycle
  - Job 11: Establish Zero-Trust Workload Identity
  - Job 12: Sync Secrets from External Vaults
- **Reference**
  - Job 8: Understand Cluster Certificate Architecture
- **Observe**
  - Job 13: Audit and Investigate Cluster Activity
- **Confirm**
  - Job 15: Scan Workloads for Vulnerabilities

### Detailed Job Descriptions

#### Understand & Plan

**Job 1: Understand the Security and Compliance Landscape**

*When I am responsible for cluster security, I want to understand how OpenShift addresses security and compliance across layers, so I can plan controls and assign ownership.*

Prerequisites: None

- **1.1. Orient to security domains** `[concept]`
  - Security and compliance overview (`index.adoc`): Container security, audit, certificates, compliance, vulnerability scanning
  - Context: Start here before choosing Operators or hardening tasks

**Job 2: Understand Compliance Requirements**

*When my organization must meet regulatory or governance requirements, I want to understand compliance concepts and checking options in OpenShift, so I can choose appropriate controls.*

Prerequisites: Job 1 (recommended)

- **2.1. Learn compliance fundamentals** `[concept]`
  - Understanding compliance (`container_security/security-compliance.adoc`): Framework context before tool selection
  - Context: Complete before Job 4 (Compliance Operator installation)

#### Secure

**Job 3: Secure the Container Supply Chain and Runtime**

*When I run containerized workloads, I want to secure images, builds, registries, deployment, networking, and storage, so I can reduce supply-chain and runtime risk.*

Prerequisites: Cluster administrator or platform engineer access

- **3.1. Understand the container security model** `[concept]`
  - Understanding container security; Understanding host and VM security
  - Context: Foundation for all subsequent container hardening tasks
- **3.2. Harden nodes and trust images** `[procedure]`
  - Hardening RHCOS; Container image signatures; Securing container content; Using container registries securely
  - Context: Apply before production workloads
- **3.3. Secure build, deploy, and runtime** `[procedure]`
  - Securing the build process; Deploying containers; Securing the container platform; Securing networks; Securing attached storage
  - Context: End-to-end workload lifecycle
- **3.4. Monitor security events** `[procedure]`
  - Monitoring cluster events and logs
  - Context: Ongoing observation after deployment

**Job 4: Assess and Remediate Cluster Compliance**

*When I need automated compliance assessment, I want to install and run the Compliance Operator with profiles and remediations, so I can demonstrate and improve regulatory posture.*

Prerequisites: Job 2; cluster admin; supported compliance profile

- **4.1. Evaluate and install** `[concept]` / `[procedure]`
  - Compliance Operator overview, release notes, support, understanding, CRDs, installation
  - Context: Confirm support and version before install
- **4.2. Operate the operator** `[procedure]`
  - Updating, managing, uninstalling the Compliance Operator
  - Context: Day-2 lifecycle
- **4.3. Run scans and remediate** `[procedure]`
  - Supported profiles, scans, tailoring, raw results, remediation, advanced tasks, troubleshooting, oc-compliance plugin
  - Context: Core audit workflow

**Job 5: Detect Unauthorized Node File Changes**

*When I must detect unauthorized changes on cluster nodes, I want continuous file integrity monitoring, so I can investigate tampering and support audits.*

Prerequisites: Cluster admin

- **5.1. Deploy File Integrity Operator** `[procedure]`
  - Overview through installation, update, understanding, configuring
  - Context: Required before integrity policies take effect
- **5.2. Advanced use and troubleshooting** `[procedure]`
  - Advanced tasks, troubleshooting, uninstall
  - Context: After baseline configuration

**Job 6: Enforce Workload Security Profiles**

*When I need consistent workload isolation, I want to manage seccomp and SELinux profiles for pods, so I can enforce least-privilege execution.*

Prerequisites: Cluster admin; Security Profiles Operator supported on platform

- **6.1. Enable and understand SPO** `[concept]` / `[procedure]`
  - Overview, release notes, support, understanding, enabling
  - Context: Operator must be enabled before profile binding
- **6.2. Manage seccomp and SELinux** `[procedure]`
  - Managing seccomp profiles; Managing SELinux profiles
  - Context: Workload-specific enforcement
- **6.3. Advanced audit logging and lifecycle** `[procedure]`
  - Advanced tasks, Advanced Audit Logging Framework, troubleshooting, uninstall
  - Context: Extended observability and problem resolution

**Job 10: Protect Data at Rest with NBDE**

*When I must protect data at rest on nodes, I want network-bound disk encryption with Tang servers, so I can meet encryption requirements without storing keys on nodes.*

Prerequisites: Cluster admin; planning for Tang connectivity

- **10.1. Deploy NBDE Tang Server Operator** `[procedure]`
  - Operator overview through Tang URL identification (6 assemblies)
  - Context: Managed Tang lifecycle on cluster
- **10.2. Plan NBDE without the operator** `[concept]`
  - About disk encryption technology; Tang installation considerations; key management; disaster recovery
  - Context: Planning and manual/key-management scenarios

**Job 14: Harden Cluster Security Defaults**

*When I harden a production cluster, I want to configure TLS profiles, seccomp defaults, and API access constraints, so I can reduce attack surface.*

Prerequisites: Cluster admin

- **14.1. Configure TLS and seccomp defaults** `[procedure]`
  - Configuring TLS security profiles; Configuring seccomp profiles
  - Context: Cluster-wide defaults (distinct from SPO workload profiles in Job 6)
- **14.2. Restrict API access patterns** `[procedure]`
  - Allowing JavaScript-based access to the API server from additional hosts
  - Context: When console or tooling requires broader API access

#### Set Up & Configure

**Job 7: Manage Platform TLS Certificates**

*When cluster components require trusted TLS, I want to replace and manage ingress, API, and service certificates, so I can meet organizational PKI requirements.*

Prerequisites: Cluster admin; access to organizational CA material

- **7.1. Replace ingress and API certificates** `[procedure]`
  - Replacing default ingress certificate; Adding API server certificates
  - Context: Most common PKI customization path
- **7.2. Service serving and CA bundle** `[procedure]`
  - Securing service traffic using service serving certificates; Updating the CA bundle
  - Context: In-cluster service trust chain

**Job 9: Automate Certificate Lifecycle**

*When I need automated X.509 certificate issuance and renewal, I want to deploy and configure the cert-manager Operator, so I can reduce manual certificate operations.*

Prerequisites: Job 7 (recommended for context); cluster admin

- **9.1. Install and configure cert-manager** `[procedure]`
  - Overview, release notes, install, egress proxy, API customization, authentication
  - Context: Foundation for automated issuance
- **9.2. Issue and integrate certificates** `[procedure]`
  - ACME issuer, certificates with issuer, securing routes, Istio-CSR integration
  - Context: Production certificate workflows
- **9.3. Operate and secure the operator** `[procedure]`
  - Network policy, trust-manager, monitoring, log levels, uninstall
  - Context: Day-2 operations and hardening

**Job 11: Establish Zero-Trust Workload Identity**

*When I adopt zero-trust workload identity, I want to deploy SPIFFE/SPIRE and related federation, so I can authenticate workloads without long-lived secrets.*

Prerequisites: Security architect review; cluster admin

- **11.1. Deploy Zero Trust Workload Identity Manager** `[procedure]`
  - Overview, components, release notes, install, deploy operands
  - Context: Multi-operand deployment
- **11.2. Configure federation and operations** `[procedure]`
  - Egress proxy, OIDC federation, SPIRE federation, create-only mode, monitoring, uninstall
  - Context: Production identity federation

**Job 12: Sync Secrets from External Vaults**

*When sensitive values live in external vaults, I want the External Secrets Operator to sync secrets into the cluster, so I can avoid duplicating secret storage.*

Prerequisites: External vault access; cluster admin

- **12.1. Understand secrets management landscape** `[concept]`
  - Understanding secrets management
  - Context: Choose between secrets Operators before install
- **12.2. Deploy and operate External Secrets Operator** `[procedure]`
  - ESO overview through uninstall, APIs, migration from community operator
  - Context: Vault-to-cluster sync workflow

#### Reference

**Job 8: Understand Cluster Certificate Architecture**

*When I troubleshoot TLS or plan certificate rotation, I want to understand each certificate type used by the platform, so I can manage lifecycle and trust correctly.*

Prerequisites: Jobs 7 or 9 in progress (recommended)

- **8.1. Certificate type reference** `[reference]`
  - 13 assemblies under `certificate_types_descriptions/`: API server, proxy, service CA, node, bootstrap, etcd, OLM, aggregated API, MCO, ingress, monitoring/logging, control plane
  - Context: Use while performing Jobs 7 or 9, not as a linear read

#### Observe

**Job 13: Audit and Investigate Cluster Activity**

*When I need accountability for cluster changes, I want to configure audit policy and review audit logs, so I can support investigations and compliance evidence.*

Prerequisites: Cluster admin; audit log backend available

- **13.1. View audit logs** `[procedure]`
  - Viewing audit logs (`audit-log-view.adoc`)
  - Context: Investigation and evidence collection
- **13.2. Configure audit policy** `[procedure]`
  - Configuring the audit log policy (`audit-log-policy-config.adoc`)
  - Context: Define what gets recorded before review

#### Confirm

**Job 15: Scan Workloads for Vulnerabilities**

*When I deploy container images, I want to scan pods for known vulnerabilities, so I can identify images or pods that need remediation before production.*

Prerequisites: Quay Container Security Operator or equivalent; cluster admin

- **15.1. Run vulnerability scans** `[procedure]`
  - Scanning pods for vulnerabilities (`pod-vulnerability-scan.adoc`)
  - Context: Pre-production gate or continuous monitoring

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Operator, component, and domain names | User goals and workflow stages |
| **Top-level navigation** | 19 section groups | 15 main jobs |
| **Leaf content** | 122 assemblies | 122 assemblies (unchanged) |
| **Compliance path** | Concept under Container security; tool under Compliance Operator | Jobs 2 → 4 (concept then execution) |
| **TLS / certificates** | 3 separate top-level sections | Jobs 7 → 8 → 9 (manage → reference → automate) |
| **NBDE** | Operator section + NBDE section | Job 10 (single encryption goal) |
| **Audit** | Two flat topics at book end | Job 13 (grouped) |
| **seccomp** | SPO + book-root topic | Jobs 6 (workload) + 14 (cluster defaults) |
| **User journey** | “Which Operator do I need?” | “What am I trying to accomplish?” |
| **Findability** | Product name required | Quick Navigation by intent |

### Job List Adjustments from Suggested Input

The analysis produced **15 main jobs** in `security-jtbd.jsonl`, and the proposed TOC retains **15 jobs** with no merges or dissolutions:

1. **No merges required** — Each main job maps to a distinct user outcome (compliance, file integrity, certificates, etc.). Overlap is handled by nesting 120 user stories under jobs, not by collapsing jobs.
2. **User story roll-up** — 122 assemblies roll up to 120 user stories (one duplicate topic title: “Configuring the egress proxy” appears under cert-manager and Zero Trust).
3. **Job titles refined for TOC** — JSONL `section` fields use assembly names (e.g., “Replacing the default ingress certificate”); TOC uses outcome titles (e.g., “Manage Platform TLS Certificates”). Semantics unchanged.
4. **Job 14 promoted from scattered topics** — TLS profiles, seccomp profiles, and JavaScript API access were book-root siblings; grouped as one hardening job for production readiness.

---

## Consolidation Examples

### Example 1: TLS and certificates (3 sections → 3 linked jobs)

**Current (Fragmented):**

- Configuring certificates (ingress, API, service serving, CA bundle)
- Certificate types and descriptions (13 reference topics)
- cert-manager Operator for Red Hat OpenShift (15 topics)

Readers fixing a TLS issue must guess whether they need procedural config, reference material, or the cert-manager Operator.

**Proposed (Consolidated):**

- **Job 7:** Manage Platform TLS Certificates (procedural platform certs)
- **Job 8:** Understand Cluster Certificate Architecture (reference, linked from 7 and 9)
- **Job 9:** Automate Certificate Lifecycle (cert-manager Operator)

**Benefit:** One certificate workflow with explicit roles for manage, lookup, and automate—~67% fewer top-level entry points for TLS goals (3 sections → 1 logical path with 3 steps).

---

### Example 2: Compliance (2 locations → 2 sequential jobs)

**Current (Fragmented):**

- Understanding compliance (nested under Container security)
- Compliance Operator (17 topics in separate section)

Audit preparation requires discovering both locations; the concept appears unrelated to the Operator section.

**Proposed (Consolidated):**

- **Job 2:** Understand Compliance Requirements (concept)
- **Job 4:** Assess and Remediate Cluster Compliance (Compliance Operator, 17 assemblies)

**Benefit:** Concept-before-tool sequence is explicit; audit prep path is Jobs 2 → 4 → 13 without cross-book hunting.

---

### Example 3: Security Operators (7 sections → 6 jobs)

**Current (Fragmented):**

- Separate top-level sections for Compliance, File Integrity, Security Profiles, NBDE Tang, cert-manager, Zero Trust, and External Secrets Operators—each with its own install/configure/troubleshoot pattern repeated seven times.

**Proposed (Consolidated):**

- Jobs 4, 5, 6, 9, 10, 11, 12 each own one Operator family under a **goal title** (compliance, integrity, profiles, certificates, encryption, identity, secrets).

**Benefit:** Users who know their goal (“file integrity monitoring”) find Job 5 directly instead of scanning seven Operator names; Operator lifecycle content stays nested inside the job.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|------------------|--------|
| Cross-Operator security monitoring | No dedicated job | Monitoring topics inside each Operator only | **Medium** — Users must know which Operator to open for metrics/logs |
| Cross-Operator upgrade planning | No dedicated job | Release notes per Operator section | **Medium** — Upgrade matrix for security stack not in one place |
| etcd encryption at rest | Job 1 links out | Documented in etcd book, mentioned in overview | **Low** — Acceptable cross-book link if intentional |
| Cluster-wide vulnerability governance | Job 15 only | Single scanning assembly | **Medium** — No policy/continuous scanning job beyond pod scan |
| Security incident response runbook | No job | Troubleshooting per Operator | **High** — No end-to-end IR narrative across audit + FIO + compliance |
| Zero Trust + ESO integration patterns | Jobs 11, 12 separate | Separate Operator sections | **Low** — Advanced integration; users can follow both jobs |
| Emotional / stakeholder jobs | Not extracted | Implied in compliance overview | **Low** — Optional JTBD layer for future research |
| HyperShift / hosted control plane compliance | Job 4 partial | Some Compliance Operator topics mention HCP | **Low** — Niche platform variant |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 19 section groups | 15 main jobs | **21% reduction** |
| Assemblies (content units) | 122 | 122 | No content loss |
| Entry points for TLS goals | 3 sections | 1 path (Jobs 7–9) | **Unified workflow** |
| Entry points for compliance audit | 2 sections | 1 path (Jobs 2, 4, 13) | **Sequential clarity** |
| Clicks to typical Operator install doc | Book → Operator → (subdir) → assembly (3–4) | Book → Job → assembly (2–3) | **~1 fewer level** |
| Goal-first navigation | None | 15-item Quick Navigation | **Added** |
| Operator names required upfront | Yes | No (optional after job selection) | **Lower cognitive load** |

**Final job count: 15** (unchanged from JTBD analysis). Consolidation is achieved by **grouping 122 assemblies under outcome-based jobs**, not by deleting or merging main jobs.

---

## Document Statistics

| Metric | Value |
|--------|-------|
| Book | Security and compliance (`security/`) |
| Distro filter | `openshift-enterprise` |
| Assemblies analyzed | 122 |
| JTBD records | 135 (15 main_job, 120 user_story) |
| Grounding validation | 135 pass, 0 flagged |
| Combined source lines | ~82,900 (`security-combined.adoc`) |
| Analysis artifacts | `security-jtbd.jsonl`, `security-toc-new_taxonomy.md`, `security-comparison.md` |

---

## Related Artifacts

| File | Role in workflow |
|------|------------------|
| `security-jtbd.jsonl` | Source records and evidence |
| `security-toc-new_taxonomy.md` | Proposed TOC with line references |
| `security-comparison.md` | Side-by-side structure comparison |
| `security-consolidation-report.md` | This stakeholder summary |
| `security-topicmap.json` | Parsed current topic map |
| `security-include-graph.json` | Module provenance for writers |

---

## Recommended Next Steps for Writers

1. **Pilot navigation** — Add Quick Navigation (from TOC) to the book overview assembly.
2. **Cross-links** — Link certificate assemblies to Jobs 7/8/9; compliance concept to Job 2 before Operator install.
3. **Topic map review** — Evaluate whether topic map order should reflect job order for portal navigation (optional, larger change).
4. **Close High gap** — Consider a lightweight “Respond to security events” job linking audit logs, FIO alerts, and compliance failures.
5. **Stakeholder review** — Use this report + `security-comparison.md` in a restructuring review with security docs owners.

---

*Generated by jtbd-consolidate from `analysis/openshift-enterprise/security/` analysis artifacts.*
