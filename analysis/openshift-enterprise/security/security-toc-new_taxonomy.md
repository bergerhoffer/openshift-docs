# Security and compliance
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help cluster administrators, platform engineers, and security teams secure OpenShift clusters, meet compliance obligations, and operate security-focused Operators across the container lifecycle.

**Personas:** Cluster administrator, Platform engineer, Security engineer, Security architect, Compliance officer

**Main Jobs:** 15 core jobs across 7 workflow stages (Plan, Secure, Configure, Reference, Monitor, Observe, Confirm)

---

## Quick Navigation

**I want to:**

- Understand how OpenShift handles security and compliance → **Job 1** (Plan)
- Learn compliance concepts before choosing tools → **Job 2** (Plan)
- Secure images, builds, registries, and running workloads → **Job 3** (Secure)
- Run compliance scans and remediations → **Job 4** (Secure)
- Detect tampering on cluster nodes → **Job 5** (Monitor)
- Enforce seccomp and SELinux for pods → **Job 6** (Secure)
- Replace ingress/API/service certificates → **Job 7** (Configure)
- Understand what each cluster certificate does → **Job 8** (Reference)
- Automate TLS with cert-manager → **Job 9** (Configure)
- Set up NBDE/Tang disk encryption → **Job 10** (Secure)
- Deploy zero-trust workload identity (SPIFFE/SPIRE) → **Job 11** (Configure)
- Pull secrets from external vaults → **Job 12** (Configure)
- Review audit logs and policy → **Job 13** (Observe)
- Harden TLS profiles, seccomp, and API access → **Job 14** (Secure)
- Scan pods for image vulnerabilities → **Job 15** (Confirm)

---

# Table of Contents
## Getting Started

### Job 1: Understand the Security and Compliance Landscape
*When I am responsible for cluster security, I want to understand how OpenShift addresses security and compliance across layers, so I can plan controls and assign ownership.*

**Personas:** Cluster administrator

#### 1.1 Orient to the security book

**Goal:** Map major security domains (containers, certificates, compliance, operators, audit) before diving into tasks.

→ Lines 1-496: Security and compliance overview  
  Source: `index.adoc` — Security overview, Compliance overview, cross-links to major sections

- Container security, auditing, certificates, encryption, vulnerability scanning
- Compliance Operator and File Integrity Operator introductions

---

## Choose Your Approach

### Job 2: Understand Compliance Requirements
*When my organization must meet regulatory or governance requirements, I want to understand compliance concepts and checking options in OpenShift, so I can choose appropriate controls.*

**Personas:** Compliance officer, Cluster administrator

#### 2.1 Learn compliance fundamentals

**Goal:** Decide whether automated compliance scanning (Compliance Operator) fits your regulatory framework.

→ Lines 3078-3549: Understanding compliance  
  Source: `container_security/security-compliance.adoc`

**Timing:** BEFORE Job 4 (Run compliance scans) — without framework context, profile selection is guesswork.

---

### Job 3: Secure the Container Supply Chain and Runtime
*When I run containerized workloads, I want to secure images, builds, registries, deployment, networking, and storage, so I can reduce supply-chain and runtime risk.*

**Personas:** Platform engineer, Cluster administrator

#### 3.1 Understand the container security model

**Goal:** Learn how host, orchestration, build, and application layers interact.

→ Lines 497-1026: Understanding container security  
  Source: `container_security/security-understanding.adoc`

→ Lines 1027-1584: Understanding host and VM security  
  Source: `container_security/security-hosts-vms.adoc`

#### 3.2 Harden the node operating system

**Goal:** Apply RHCOS hardening appropriate for OpenShift Container Platform.

→ Lines 1585-2085: Hardening Red Hat Enterprise Linux CoreOS  
  Source: `container_security/security-hardening.adoc`

#### 3.3 Trust and verify container images

**Goal:** Ensure only signed or trusted images enter the cluster.

→ Lines 2086-3077: Container image signatures  
  Source: `container_security/security-container-signature.adoc`

→ Lines 3550-4367: Securing container content  
  Source: `container_security/security-container-content.adoc`

→ Lines 4368-4938: Using container registries securely  
  Source: `container_security/security-registries.adoc`

#### 3.4 Secure build, deploy, and platform layers

**Goal:** Control how images are built, deployed, and isolated at runtime.

→ Lines 4939-5549: Securing the build process  
  Source: `container_security/security-build.adoc`

→ Lines 5550-6195: Deploying containers  
  Source: `container_security/security-deploy.adoc`

→ Lines 6196-6807: Securing the container platform  
  Source: `container_security/security-platform.adoc`

→ Lines 6808-7354: Securing networks  
  Source: `container_security/security-network.adoc`

→ Lines 7355-7852: Securing attached storage  
  Source: `container_security/security-storage.adoc`

#### 3.5 Monitor security-relevant events

**Goal:** Watch cluster events and logs for security incidents.

→ Lines 7853-8390: Monitoring cluster events and logs  
  Source: `container_security/security-monitoring.adoc`

---

## Secure Your Environment

### Job 4: Assess and Remediate Cluster Compliance
*When I need automated compliance assessment, I want to install and run the Compliance Operator with profiles and remediations, so I can demonstrate and improve regulatory posture.*

**Personas:** Cluster administrator, Compliance officer

**Requires:** Job 2 (compliance concepts); cluster admin access; supported compliance profile for your platform

#### 4.1 Evaluate and install the Compliance Operator

**Goal:** Confirm support scope and deploy the operator.

→ Lines 16875-17332: Compliance Operator overview  
  Source: `compliance_operator/co-overview.adoc`

→ Lines 17333-18592: Compliance Operator release notes  
  Source: `compliance_operator/compliance-operator-release-notes.adoc`

→ Lines 18593-19084: Compliance Operator support  
  Source: `compliance_operator/co-support.adoc`

→ Lines 19085-19750: Understanding the Compliance Operator  
  Source: `compliance_operator/co-concepts/compliance-operator-understanding.adoc`

→ Lines 19751-20788: Understanding the Custom Resource Definitions  
  Source: `compliance_operator/co-concepts/compliance-operator-crd.adoc`

→ Lines 20789-21627: Installing the Compliance Operator  
  Source: `compliance_operator/co-management/compliance-operator-installation.adoc`

#### 4.2 Operate and maintain the operator

**Goal:** Keep the Compliance Operator current and healthy.

→ Lines 21628-22148: Updating the Compliance Operator  
  Source: `compliance_operator/co-management/compliance-operator-updating.adoc`

→ Lines 22149-22658: Managing the Compliance Operator  
  Source: `compliance_operator/co-management/compliance-operator-manage.adoc`

→ Lines 22659-23207: Uninstalling the Compliance Operator  
  Source: `compliance_operator/co-management/compliance-operator-uninstallation.adoc`

#### 4.3 Run scans, tailor profiles, and remediate

**Goal:** Execute compliance checks and act on findings.

→ Lines 23208-24207: Supported compliance profiles  
  Source: `compliance_operator/co-scans/compliance-operator-supported-profiles.adoc`

→ Lines 24208-25178: Compliance Operator scans  
  Source: `compliance_operator/co-scans/compliance-scans.adoc`

→ Lines 25179-25791: Tailoring the Compliance Operator  
  Source: `compliance_operator/co-scans/compliance-operator-tailor.adoc`

→ Lines 25792-26309: Retrieving Compliance Operator raw results  
  Source: `compliance_operator/co-scans/compliance-operator-raw-results.adoc`

→ Lines 26310-27429: Managing Compliance Operator remediation  
  Source: `compliance_operator/co-scans/compliance-operator-remediation.adoc`

#### 4.4 Advanced workflows and troubleshooting

**Goal:** Handle edge cases and diagnose failed scans.

→ Lines 27430-28237: Performing advanced Compliance Operator tasks  
  Source: `compliance_operator/co-scans/compliance-operator-advanced.adoc`

→ Lines 28238-29284: Troubleshooting Compliance Operator scans  
  Source: `compliance_operator/co-scans/compliance-operator-troubleshooting.adoc`

→ Lines 29285-30118: Using the oc-compliance plugin  
  Source: `compliance_operator/co-scans/oc-compliance-plug-in-using.adoc`

---

### Job 5: Detect Unauthorized Node File Changes
*When I must detect unauthorized changes on cluster nodes, I want continuous file integrity monitoring, so I can investigate tampering and support audits.*

**Personas:** Security engineer, Cluster administrator

#### 5.1 Deploy and configure the File Integrity Operator

**Goal:** Install FIO and define integrity check policies.

→ Lines 30119-30545: File Integrity Operator Overview  
  Source: `file_integrity_operator/fio-overview.adoc`

→ Lines 30546-31248: File Integrity Operator release notes  
  Source: `file_integrity_operator/file-integrity-operator-release-notes.adoc`

→ Lines 31249-31714: File Integrity Operator support  
  Source: `file_integrity_operator/fio-support.adoc`

→ Lines 31715-32264: Installing the File Integrity Operator  
  Source: `file_integrity_operator/file-integrity-operator-installation.adoc`

→ Lines 32265-32778: Updating the File Integrity Operator  
  Source: `file_integrity_operator/file-integrity-operator-updating.adoc`

→ Lines 32779-33646: Understanding the File Integrity Operator  
  Source: `file_integrity_operator/file-integrity-operator-understanding.adoc`

→ Lines 33647-34351: Configuring the File Integrity Operator  
  Source: `file_integrity_operator/file-integrity-operator-configuring.adoc`

#### 5.2 Advanced use, troubleshooting, and removal

→ Lines 34352-34873: Performing advanced File Integrity Operator tasks  
  Source: `file_integrity_operator/file-integrity-operator-advanced-usage.adoc`

→ Lines 34874-35339: Troubleshooting the File Integrity Operator  
  Source: `file_integrity_operator/file-integrity-operator-troubleshooting.adoc`

→ Lines 35340-35789: Uninstalling the File Integrity Operator  
  Source: `file_integrity_operator/fio-uninstalling.adoc`

---

### Job 6: Enforce Workload Security Profiles
*When I need consistent workload isolation, I want to manage seccomp and SELinux profiles for pods, so I can enforce least-privilege execution.*

**Personas:** Platform engineer, Cluster administrator

#### 6.1 Deploy and enable the Security Profiles Operator

→ Lines 35790-36209: Security Profiles Operator overview  
  Source: `security_profiles_operator/spo-overview.adoc`

→ Lines 36210-36804: Security Profiles Operator release notes  
  Source: `security_profiles_operator/spo-release-notes.adoc`

→ Lines 36805-37270: Security Profiles Operator support  
  Source: `security_profiles_operator/spo-support.adoc`

→ Lines 37271-37701: Understanding the Security Profiles Operator  
  Source: `security_profiles_operator/spo-understanding.adoc`

→ Lines 37702-38293: Enabling the Security Profiles Operator  
  Source: `security_profiles_operator/spo-enabling.adoc`

#### 6.2 Manage seccomp and SELinux profiles

→ Lines 38294-39258: Managing seccomp profiles  
  Source: `security_profiles_operator/spo-seccomp.adoc`

→ Lines 39259-40423: Managing SELinux profiles  
  Source: `security_profiles_operator/spo-selinux.adoc`

#### 6.3 Advanced audit logging and lifecycle

→ Lines 40424-41315: Advanced Security Profiles Operator tasks  
  Source: `security_profiles_operator/spo-advanced.adoc`

→ Lines 41316-42796: Advanced Audit Logging Framework  
  Source: (SPO advanced audit content)

→ Lines 42797-43259: Troubleshooting the Security Profiles Operator  
  Source: `security_profiles_operator/spo-troubleshooting.adoc`

→ Lines 43260-43713: Uninstalling the Security Profiles Operator  
  Source: `security_profiles_operator/spo-uninstalling.adoc`

---

## Set Up & Configure

### Job 7: Manage Platform TLS Certificates
*When cluster components require trusted TLS, I want to replace and manage ingress, API, and service certificates, so I can meet organizational PKI requirements.*

**Personas:** Cluster administrator

#### 7.1 Replace and extend platform certificates

→ Lines 8391-8919: Replacing the default ingress certificate  
  Source: `certificates/replacing-default-ingress-certificate.adoc`

→ Lines 8920-9462: Adding API server certificates  
  Source: `certificates/api-server.adoc`

→ Lines 9463-10446: Securing service traffic using service serving certificates  
  Source: `certificates/service-serving-certificate.adoc`

→ Lines 10447-10926: Updating the CA bundle  
  Source: `certificates/updating-ca-bundle.adoc`

---

## Reference

### Job 8: Understand Cluster Certificate Architecture
*When I troubleshoot TLS or plan certificate rotation, I want to understand each certificate type used by the platform, so I can manage lifecycle and trust correctly.*

**Personas:** Platform engineer

**Goal:** Use as reference while performing Job 7 or diagnosing TLS failures.

→ Lines 10927-11360: User-provided certificates for the API server  
→ Lines 11361-11888: Proxy certificates  
→ Lines 11889-12357: Service CA certificates  
→ Lines 12358-12796: Node certificates  
→ Lines 12797-13226: Bootstrap certificates  
→ Lines 13227-13764: etcd certificates  
→ Lines 13765-14191: OLM certificates  
→ Lines 14192-14616: Aggregated API client certificates  
→ Lines 14617-15103: Machine Config Operator certificates  
→ Lines 15104-15544: User-provided certificates for default ingress  
→ Lines 15545-16035: Ingress certificates  
→ Lines 16036-16451: Monitoring and cluster logging Operator component certificates  
→ Lines 16452-16874: Control plane certificates  

  Source: `certificate_types_descriptions/*.adoc`

---

### Job 9: Automate Certificate Lifecycle
*When I need automated X.509 certificate issuance and renewal, I want to deploy and configure the cert-manager Operator, so I can reduce manual certificate operations.*

**Personas:** Platform engineer

#### 9.1 Install and configure cert-manager

→ Lines 47148-47682: cert-manager Operator overview  
  Source: `cert_manager_operator/index.adoc`

→ Lines 47683-48125: cert-manager Operator release notes  
  Source: `cert_manager_operator/cert-manager-operator-release-notes.adoc`

→ Lines 48126-48837: Installing the cert-manager Operator  
  Source: `cert_manager_operator/cert-manager-operator-install.adoc`

→ Lines 48838-49343: Configuring the egress proxy  
  Source: `cert_manager_operator/cert-manager-operator-proxy.adoc`

→ Lines 49344-50645: Customizing cert-manager via Operator API fields  
  Source: `cert_manager_operator/cert-manager-customizing-api-fields.adoc`

→ Lines 50646-51583: Authenticating the cert-manager Operator  
  Source: `cert_manager_operator/cert-manager-authenticate.adoc`

#### 9.2 Issue certificates and integrate with the mesh

→ Lines 51584-52861: Configuring an ACME issuer  
  Source: `cert_manager_operator/cert-manager-operator-issuer-acme.adoc`

→ Lines 52862-53535: Configuring certificates with an issuer  
  Source: `cert_manager_operator/cert-manager-creating-certificate.adoc`

→ Lines 53536-54120: Securing routes with cert-manager  
  Source: `cert_manager_operator/` (routes integration)

→ Lines 54121-54998: Integrating cert-manager with Istio-CSR  
  Source: `cert_manager_operator/cert-manager-operator-integrating-istio.adoc`

#### 9.3 Network policy, trust distribution, and operations

→ Lines 54999-55634: Network policy configuration for cert-manager Operator  
  Source: cert-manager network policy content

→ Lines 55635-56589: Distributing certificates using trust-manager operand  
  Source: trust-manager content

→ Lines 56590-57330: Monitoring the cert-manager Operator  
  Source: `cert_manager_operator/cert-manager-monitoring.adoc`

→ Lines 57331-57857: Configuring log levels  
  Source: `cert_manager_operator/cert-manager-log-levels.adoc`

→ Lines 57858-58369: Uninstalling the cert-manager Operator  
  Source: `cert_manager_operator/cert-manager-operator-uninstall.adoc`

---

### Job 10: Protect Data at Rest with NBDE
*When I must protect data at rest on nodes, I want network-bound disk encryption with Tang servers, so I can meet encryption requirements without storing keys on nodes.*

**Personas:** Cluster administrator

#### 10.1 Deploy the NBDE Tang Server Operator

→ Lines 43714-44123: NBDE Tang Server Operator overview  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-overview.adoc`

→ Lines 44124-44540: NBDE Tang Server Operator release notes  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-release-notes.adoc`

→ Lines 44541-44964: Understanding the NBDE Tang Server Operator  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-understanding.adoc`

→ Lines 44965-45492: Installing the NBDE Tang Server Operator  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-installing.adoc`

→ Lines 45493-46145: Configuring and managing Tang servers  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc`

→ Lines 46146-46678: Identifying URL of a Tang server  
  Source: `nbde_tang_server_operator/nbde-tang-server-operator-identifying-url.adoc`

#### 10.2 Plan and operate NBDE without the operator

**Goal:** Understand encryption technology, Tang planning, key management, and DR.

→ Lines 80135-80779: About disk encryption technology  
  Source: `network_bound_disk_encryption/nbde-about-disk-encryption-technology.adoc`

→ Lines 80780-81286: Tang server installation considerations  
  Source: `network_bound_disk_encryption/nbde-tang-server-installation-considerations.adoc`

→ Lines 81287-82307: Tang server encryption key management  
  Source: `network_bound_disk_encryption/nbde-managing-encryption-keys.adoc`

→ Lines 82308-82899: Disaster recovery considerations  
  Source: `network_bound_disk_encryption/nbde-disaster-recovery-considerations.adoc`

---

### Job 11: Establish Zero-Trust Workload Identity
*When I adopt zero-trust workload identity, I want to deploy SPIFFE/SPIRE and related federation, so I can authenticate workloads without long-lived secrets.*

**Personas:** Security architect, Platform engineer

→ Lines 58370-58871: Zero Trust Workload Identity Manager overview  
→ Lines 58872-59410: Zero Trust Workload Identity Manager components  
→ Lines 59411-60142: Zero Trust Workload Identity Manager release notes  
→ Lines 60143-60768: Installing Zero Trust Workload Identity Manager  
→ Lines 60769-62313: Deploying Zero Trust Workload Identity Manager operands  
→ Lines 62314-63940: Configuring OIDC Federation  
→ Lines 63941-65889: Configuring SPIRE Federation  
→ Lines 65890-66433: Enabling create-only mode  
→ Lines 66434-67408: Monitoring Zero Trust Workload Identity Manager  
→ Lines 67409-68026: Uninstalling the Zero Trust Workload Identity Manager  

  Source: Zero Trust Workload Identity Manager assemblies under `security/`

---

### Job 12: Sync Secrets from External Vaults
*When sensitive values live in external vaults, I want the External Secrets Operator to sync secrets into the cluster, so I can avoid duplicating secret storage.*

**Personas:** Platform engineer

→ Lines 46679-47078: Understanding secrets management  
  Source: `understanding-secrets-management.adoc`

→ Lines 68027-68547: External Secrets Operator overview  
→ Lines 68548-69077: External Secrets Operator release notes  
→ Lines 69078-69885: Installing the External Secrets Operator  
→ Lines 69886-70954: Configuring Network Policy for the Operand  
→ Lines 70955-71870: Monitoring the External Secrets Operator  
→ Lines 71871-72830: Customizing the External Secrets Operator  
→ Lines 72831-73391: Uninstalling the External Secrets Operator  
→ Lines 73392-74998: External Secrets Operator APIs  
→ Lines 74999-75840: Migrating from community External Secrets Operator  

  Source: External Secrets Operator assemblies under `security/`

---

## Observe System State

### Job 13: Audit and Investigate Cluster Activity
*When I need accountability for cluster changes, I want to configure audit policy and review audit logs, so I can support investigations and compliance evidence.*

**Personas:** Security engineer, Cluster administrator

→ Lines 75841-76602: Viewing audit logs  
  Source: `audit-log-view.adoc`

→ Lines 76603-77301: Configuring the audit log policy  
  Source: `audit-log-policy-config.adoc`

---

### Job 14: Harden Cluster Security Defaults
*When I harden a production cluster, I want to configure TLS profiles, seccomp defaults, and API access constraints, so I can reduce attack surface.*

**Personas:** Cluster administrator

→ Lines 77302-78337: Configuring TLS security profiles  
  Source: `tls-security-profiles.adoc`

→ Lines 78338-79000: Configuring seccomp profiles  
  Source: `seccomp-profiles.adoc`

→ Lines 79001-79472: Allowing JavaScript-based access to the API server from additional hosts  
  Source: `allowing-javascript-access-api-server.adoc`

---

## Confirm Readiness

### Job 15: Scan Workloads for Vulnerabilities
*When I deploy container images, I want to scan pods for known vulnerabilities, so I can identify images or pods that need remediation before production.*

**Personas:** Cluster administrator

→ Lines 79473-82899: Scanning pods for vulnerabilities  
  Source: `pod-vulnerability-scan.adoc`

---
## Appendices

### A. Security Operator Comparison Matrix

| Operator | Primary job | When to use |
|----------|-------------|-------------|
| Compliance Operator | Regulatory scan + remediation | CIS/STIG-style compliance evidence |
| File Integrity Operator | Node file tampering detection | Host integrity monitoring |
| Security Profiles Operator | seccomp/SELinux profiles | Workload sandbox enforcement |
| cert-manager Operator | Automated TLS certificates | High-volume cert issuance/renewal |
| External Secrets Operator | External vault → cluster secrets | Centralized secret stores |
| Zero Trust Workload Identity Manager | SPIFFE/SPIRE identity | Zero-trust workload auth |
| NBDE Tang Server Operator | Tang server lifecycle | NBDE key escrow |

### B. Operator Selection Guide

| If you need… | Start with… |
|--------------|-------------|
| Compliance report for auditors | Job 4 (Compliance Operator) |
| Detect changed binaries on nodes | Job 5 (File Integrity Operator) |
| Restrict syscall/filesystem access | Job 6 (Security Profiles Operator) |
| Custom ingress/API TLS | Job 7, then Job 8 for reference |
| Let's Encrypt / ACME automation | Job 9 (cert-manager) |
| Disk encryption with network keys | Job 10 (NBDE) |
| Vault/AWS/GCP secret sync | Job 12 (External Secrets) |

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs |
|-------|----------|------|
| Plan | ✅ | 1, 2 |
| Secure | ✅ | 3, 4, 5, 6, 10, 14 |
| Configure | ✅ | 7, 9, 11, 12 |
| Reference | ✅ | 8 |
| Monitor | ✅ | 5 (file integrity) |
| Observe | ✅ | 13 |
| Confirm | ✅ | 15 |
| Troubleshoot | ⚠️ Partial | Embedded in operator jobs (4, 5, 6, 9) |
| Upgrade | ⚠️ Partial | Release notes per operator |
| Migrate | ⚠️ Partial | Job 12 (ESO migration) |

### D. Document Statistics

| Metric | Value |
|--------|-------|
| Source | `security-combined.adoc` |
| Distro filter | `openshift-enterprise` |
| Assemblies analyzed | 122 |
| JTBD records | 135 (15 main_job, 120 user_story) |
| Validation | 135 pass, 0 flagged |
| Combined document lines | ~82,900 |

---

## Navigation Guide

**New to OpenShift security?** Start with Job 1, then Job 3 for container fundamentals, then branch to Jobs 4–6 based on your compliance and workload needs.

**Preparing for an audit?** Jobs 2 → 4 → 13 form the core path; add Job 5 for integrity evidence.

**TLS pain points?** Jobs 7 and 8 together; add Job 9 if you need automation.

**Line references** point to `security-combined.adoc` in `analysis/openshift-enterprise/security/`. Writers can map back to original assemblies via `security-topicmap.json` and `security-include-graph.json`.

---

*Generated from `security-jtbd.jsonl` — JTBD topic map analysis, openshift-enterprise distro.*
