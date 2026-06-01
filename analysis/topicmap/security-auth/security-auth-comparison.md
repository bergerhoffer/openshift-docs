# Security & authentication — TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-05-20
**JTBD Records:** 325
**Main Jobs:** 12

---

## Current Structure (Feature-Based)

### Security and compliance (`security/`)

- Security and compliance overview
- Container security
  - Understanding container security
  - Understanding host and VM security
  - Hardening Red Hat Enterprise Linux CoreOS
  - Container image signatures
  - Hardening Fedora CoreOS
  - Understanding compliance
  - Securing container content
  - Using container registries securely
  - Securing the build process
  - Deploying containers
  - Securing the container platform
  - Securing networks
  - Securing attached storage
  - Monitoring cluster events and logs
- Configuring certificates
  - Replacing the default ingress certificate
  - Adding API server certificates
  - Securing service traffic using service serving certificates
  - Updating the CA bundle
- Certificate types and descriptions
  - User-provided certificates for the API server
  - Proxy certificates
  - Service CA certificates
  - Node certificates
  - Bootstrap certificates
  - etcd certificates
  - OLM certificates
  - Aggregated API client certificates
  - Machine Config Operator certificates
  - User-provided certificates for default ingress
  - Ingress certificates
  - Monitoring and cluster logging Operator component certificates
  - Control plane certificates
- Compliance Operator
  - Compliance Operator overview
  - Compliance Operator release notes
  - Compliance Operator support
  - Compliance Operator concepts
    - Understanding the Compliance Operator
    - Understanding the Custom Resource Definitions
  - Compliance Operator management
    - Installing the Compliance Operator
    - Updating the Compliance Operator
    - Managing the Compliance Operator
    - Uninstalling the Compliance Operator
  - Compliance Operator scan management
    - Supported compliance profiles
    - Compliance Operator scans
    - Tailoring the Compliance Operator
    - Retrieving Compliance Operator raw results
    - Managing Compliance Operator remediation
    - Performing advanced Compliance Operator tasks
    - Troubleshooting Compliance Operator scans
    - Using the oc-compliance plugin
- File Integrity Operator
  - File Integrity Operator Overview
  - File Integrity Operator release notes
  - File Integrity Operator support
  - Installing the File Integrity Operator
  - Updating the File Integrity Operator
  - Understanding the File Integrity Operator
  - Configuring the File Integrity Operator
  - Performing advanced File Integrity Operator tasks
  - Troubleshooting the File Integrity Operator
  - Uninstalling the File Integrity Operator
- Security Profiles Operator
  - Security Profiles Operator overview
  - Security Profiles Operator release notes
  - Security Profiles Operator support
  - Understanding the Security Profiles Operator
  - Enabling the Security Profiles Operator
  - Managing seccomp profiles
  - Managing SELinux profiles
  - Advanced Security Profiles Operator tasks
  - Advanced Audit Logging Framework
  - Troubleshooting the Security Profiles Operator
  - Uninstalling the Security Profiles Operator
- NBDE Tang Server Operator
  - *...57 more entries*

### Authentication and authorization (`authentication/`)

- Authentication and authorization overview
- Understanding authentication
- Configuring the internal OAuth server
- Configuring OAuth clients
- Managing user-owned OAuth access tokens
- Understanding identity provider configuration
- Configuring identity providers
  - Configuring an htpasswd identity provider
  - Configuring a Keystone identity provider
  - Configuring an LDAP identity provider
  - Configuring a basic authentication identity provider
  - Configuring a request header identity provider
  - Configuring a GitHub or GitHub Enterprise identity provider
  - Configuring a GitLab identity provider
  - Configuring a Google identity provider
  - Configuring an OpenID Connect identity provider
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
- Managing cloud provider credentials
  - About the Cloud Credential Operator
  - Mint mode
  - Passthrough mode
  - Manual mode with long-term credentials for components
  - Manual mode with short-term credentials for components

---

## Proposed JTBD-Based Structure

### Job 1: Configure auditing and investigate security events (Operate)
- **When:** When securing an OpenShift cluster, I want to configure auditing and investigate security events, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 2: Detect vulnerabilities and unauthorized file changes (Operate)
- **When:** When securing an OpenShift cluster, I want to detect vulnerabilities and unauthorized file changes, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 3: Demonstrate compliance with security profiles (Secure)
- **When:** When securing an OpenShift cluster, I want to demonstrate compliance with security profiles, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 4: Encrypt sensitive data at rest (Secure)
- **When:** When securing an OpenShift cluster, I want to encrypt sensitive data at rest, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 5: Manage certificates and TLS for cluster services (Secure)
- **When:** When securing an OpenShift cluster, I want to manage certificates and tls for cluster services, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 6: Manage secrets and cloud provider credentials (Secure)
- **When:** When securing an OpenShift cluster, I want to manage secrets and cloud provider credentials, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 7: Secure the container software supply chain (Secure)
- **When:** When securing an OpenShift cluster, I want to secure the container software supply chain, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 8: Enforce what pods are allowed to run (Secure)
- **When:** When securing an OpenShift cluster, I want to enforce what pods are allowed to run, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 9: Configure workload and automation identities (Secure)
- **When:** When securing an OpenShift cluster, I want to configure workload and automation identities, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 10: Assign and audit permissions with RBAC (Secure)
- **When:** When securing an OpenShift cluster, I want to assign and audit permissions with rbac, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 11: Control who can sign in to the cluster (Secure)
- **When:** When securing an OpenShift cluster, I want to control who can sign in to the cluster, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

### Job 12: Understand OCP security layers and shared responsibility (Plan)
- **When:** When securing an OpenShift cluster, I want to understand ocp security layers and shared responsibility, so I can reduce risk and meet organizational security requirements.
- **Persona:** Cluster administrator

---

## Key Differences

### Current Structure (Feature-Based)
- **Organized by:** Product operators, certificate types, and platform layers
- **Navigation:** 2 books, ~155 leaf topics, ~16 section groupings
- **User journey:** Find the operator or component first, then locate the task

### Proposed Structure (JTBD-Based)
- **Organized by:** 12 outcome-oriented main jobs across Plan → Secure → Operate
- **Navigation:** Start from goal (e.g., pass compliance audit), drill to operator procedures
- **User journey:** Goal → approach → procedure

### Metrics

| Metric | Current | Proposed |
|--------|---------|----------|
| Top-level book entries | 2 books | 1 merged guide |
| Root TOC branches (approx.) | 15+ operator/feature branches | 12 main jobs |
| Leaf topics | 155 | 155 (mapped under jobs) |
| Max navigation depth to task | 4–5 (book → operator → subdir → topic) | 3 (category → job → user story) |

### Consolidation wins

1. **Authentication + Security merged** — single guide for access and platform security
2. **SCC/PSA + Security Profiles Operator** — one pod-security job (was split across books)
3. **Certificate procedures + cert types + cert-manager** — one certificates job
4. **Operator silos flattened** — install/configure/uninstall nest under jobs, not book root
