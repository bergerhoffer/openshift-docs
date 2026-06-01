# Security & authentication — Consolidation Report

**Document:** security-auth-combined.adoc (security + authentication books)
**JTBD Records:** 325 extracted → **12 final main jobs** (within 10–15 target)

---

## Executive Summary

### What's Changing

OpenShift security documentation is split across **Security and compliance** (123 topics) and **Authentication and authorization** (32 topics), organized primarily by **operator name**, **certificate type**, and **platform layer**. Users pursuing outcomes such as "pass a compliance audit" or "replace the ingress certificate" must know which component owns the task before they can navigate the TOC.

The proposed structure reorganizes the same content into **12 main jobs** grouped by JTBD lifecycle stage (**Plan**, **Secure**, **Operate**). Operator install/upgrade/uninstall sequences become user stories within the relevant job rather than parallel top-level branches.

### Key Improvements

- **Merged access and platform security:** Authentication and Security books become one JTBD guide.
- **Unified pod runtime enforcement:** SCC, PSA, and Security Profiles Operator under one job.
- **Certificate navigation simplified:** Procedures, reference types, and cert-manager under one job (74 child records today).
- **Compliance Operator demoted from book root:** 60 topics roll up under "Demonstrate compliance."
- **Supply chain vs. monitoring split clarified:** Build/sign/deploy vs. vulnerability and file-integrity detection.
- **Stable top-level navigation:** 12 goals vs. 15+ operator/feature roots.

---

## Current Structure (Feature-Based)

- **Security and compliance** (`security/`)
- **Authentication and authorization** (`authentication/`)

Major root branches include: Container security, Configuring certificates, Certificate types, Compliance Operator, File Integrity Operator, Security Profiles Operator, cert-manager, External Secrets, NBDE, identity providers, RBAC, CCO, and more.

---

## Proposed JTBD-Based Structure

### Quick Overview

**Plan**
- Understand OCP security layers and shared responsibility (23 topics)

**Secure**
- Demonstrate compliance with security profiles (60 topics)
- Encrypt sensitive data at rest (8 topics)
- Manage certificates and TLS for cluster services (74 topics)
- Manage secrets and cloud provider credentials (40 topics)
- Secure the container software supply chain (8 topics)
- Enforce what pods are allowed to run (37 topics)
- Configure workload and automation identities (7 topics)
- Assign and audit permissions with RBAC (2 topics)
- Control who can sign in to the cluster (24 topics)

**Operate**
- Configure auditing and investigate security events (2 topics)
- Detect vulnerabilities and unauthorized file changes (28 topics)

### Detailed Job Descriptions

#### Configure auditing and investigate security events
- **Statement:** When securing an OpenShift cluster, I want to configure auditing and investigate security events, so I can reduce risk and meet organizational security requirements.
- **Stage:** Operate
- **Persona:** Cluster administrator
- **Mapped child records:** 2

#### Detect vulnerabilities and unauthorized file changes
- **Statement:** When securing an OpenShift cluster, I want to detect vulnerabilities and unauthorized file changes, so I can reduce risk and meet organizational security requirements.
- **Stage:** Operate
- **Persona:** Cluster administrator
- **Mapped child records:** 28

#### Demonstrate compliance with security profiles
- **Statement:** When securing an OpenShift cluster, I want to demonstrate compliance with security profiles, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 60

#### Encrypt sensitive data at rest
- **Statement:** When securing an OpenShift cluster, I want to encrypt sensitive data at rest, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 8

#### Manage certificates and TLS for cluster services
- **Statement:** When securing an OpenShift cluster, I want to manage certificates and tls for cluster services, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 74

#### Manage secrets and cloud provider credentials
- **Statement:** When securing an OpenShift cluster, I want to manage secrets and cloud provider credentials, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 40

#### Secure the container software supply chain
- **Statement:** When securing an OpenShift cluster, I want to secure the container software supply chain, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 8

#### Enforce what pods are allowed to run
- **Statement:** When securing an OpenShift cluster, I want to enforce what pods are allowed to run, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 37

#### Configure workload and automation identities
- **Statement:** When securing an OpenShift cluster, I want to configure workload and automation identities, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 7

#### Assign and audit permissions with RBAC
- **Statement:** When securing an OpenShift cluster, I want to assign and audit permissions with rbac, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 2

#### Control who can sign in to the cluster
- **Statement:** When securing an OpenShift cluster, I want to control who can sign in to the cluster, so I can reduce risk and meet organizational security requirements.
- **Stage:** Secure
- **Persona:** Cluster administrator
- **Mapped child records:** 24

#### Understand OCP security layers and shared responsibility
- **Statement:** When securing an OpenShift cluster, I want to understand ocp security layers and shared responsibility, so I can reduce risk and meet organizational security requirements.
- **Stage:** Plan
- **Persona:** Cluster administrator
- **Mapped child records:** 23

---

## Key Differences

| Aspect | Current | Proposed |
|--------|---------|----------|
| Organizing principle | Feature / operator | User outcome |
| Books | 2 | 1 (merged) |
| Top-level branches | 15+ | 12 jobs |
| SCC vs. SPO location | Auth vs. Security | Single pod-security job |

---

## Consolidation Examples

### Example 1: Pod security (before → after)

**Before:**
- Authentication → Managing security context constraints
- Authentication → Understanding and managing pod security admission
- Security → Security Profiles Operator → (8 subtopics)

**After:** Job 5 — Enforce what pods are allowed to run
- User stories for SCC, PSA, seccomp, SELinux profiles, SPO lifecycle

### Example 2: Certificates (before → after)

**Before:**
- Security → Configuring certificates (4 topics)
- Security → Certificate types and descriptions (12 topics)
- Security → cert-manager Operator (14 topics)

**After:** Job 8 — Manage certificates and TLS for cluster services
- Decision path → replace ingress/API → cert-manager automation → reference types

### Example 3: Compliance Operator (before → after)

**Before:** Root-level Compliance Operator with concepts, management, scans subtrees

**After:** Job 10 — Demonstrate compliance with security profiles
- Install → scan → tailor → remediate → troubleshoot as sequential user stories

---

## Navigation Improvement Summary

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Books to search | 2 | 1 | −50% |
| Root TOC intents | 15+ feature branches | 12 jobs | −20%+ |
| Clicks to SCC+SPO guidance | 2 books | 1 job | Unified |

---

## Document Statistics

- **Assemblies reduced:** 155
- **Combined source size:** ~4.3 MB
- **JTBD records:** 325 (12 main_job, 309 user_story, 4 procedure)
- **Distro filter:** openshift-enterprise
