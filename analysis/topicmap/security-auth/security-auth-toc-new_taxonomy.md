# OpenShift Container Platform — Security & authentication
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help cluster administrators, platform engineers, and compliance officers secure OpenShift clusters through authentication, authorization, workload controls, secrets, certificates, compliance scanning, and audit.

**Personas:** Cluster administrator, Developer

**Main Jobs:** 12 core jobs across 3 workflow stages (Plan, Secure, Operate)

## Quick Navigation

**I want to:**
- Understand how OCP security is layered → Job 1 (Plan)
- Connect users through my corporate IdP → Job 2 (Secure)
- Grant least-privilege access with RBAC → Job 3 (Secure)
- Automate API access with service accounts → Job 4 (Secure)
- Lock down pod privileges (SCC, PSA, seccomp) → Job 5 (Secure)
- Sign images and harden CI/CD → Job 6 (Secure)
- Store secrets and cloud credentials safely → Job 7 (Secure)
- Replace ingress or API certificates → Job 8 (Secure)
- Encrypt etcd or node disks → Job 9 (Secure)
- Pass a compliance scan (CIS, PCI, etc.) → Job 10 (Secure)
- Find CVEs or tampered files on nodes → Job 11 (Operate)
- Configure audit logs for investigations → Job 12 (Operate)

---

# Table of Contents

## Understand your security model

### Job 1: Understand OCP security layers and shared responsibility
*When securing an OpenShift cluster, I want to understand ocp security layers and shared responsibility, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 23 (23 user stories, 0 procedures)

- API access control and management
- About authentication in {product-title}
- About authorization in {product-title}
- Compliance overview
- Configuring custom certificates
- *...and 18 more*

## Secure the cluster

### Job 2: Assign and audit permissions with RBAC
*When securing an OpenShift cluster, I want to assign and audit permissions with rbac, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 2 (2 user stories, 0 procedures)

- Evaluating authorization
- Impersonating the system:admin user

### Job 3: Configure workload and automation identities
*When securing an OpenShift cluster, I want to configure workload and automation identities, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 7 (7 user stories, 0 procedures)

- Default cluster service accounts
- Default project service accounts and roles
- Redirect URIs for service accounts as OAuth clients
- Role scope
- Understanding and creating service accounts
- *...and 2 more*

### Job 4: Control who can sign in to the cluster
*When securing an OpenShift cluster, I want to control who can sign in to the cluster, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 24 (24 user stories, 0 procedures)

- Configuring a GitHub or GitHub Enterprise identity provider
- Configuring a GitLab identity provider
- Configuring a Google identity provider
- Configuring a Keystone identity provider
- Configuring an LDAP identity provider
- *...and 19 more*

### Job 5: Demonstrate compliance with security profiles
*When securing an OpenShift cluster, I want to demonstrate compliance with security profiles, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 60 (60 user stories, 0 procedures)

- About extended compliance profiles
- BSI Profile Support
- CIS compliance profiles
- Compliance Operator concepts
- Compliance Operator lifecycle
- *...and 55 more*

### Job 6: Encrypt sensitive data at rest
*When securing an OpenShift cluster, I want to encrypt sensitive data at rest, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 8 (7 user stories, 1 procedures)

- About disk encryption technology
- Configuring and managing Tang servers using the NBDE Tang Server Operator
- Disaster recovery considerations
- Installing the NBDE Tang Server Operator
- NBDE Tang Server Operator overview
- *...and 2 more*

### Job 7: Enforce what pods are allowed to run
*When securing an OpenShift cluster, I want to enforce what pods are allowed to run, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 37 (36 user stories, 1 procedures)

- Admission control
- Advanced Security Profiles Operator tasks
- Benefits of Advanced Audit Logging Framework
- Configuring a custom seccomp profile
- Controlling volumes
- *...and 31 more*

### Job 8: Manage certificates and TLS for cluster services
*When securing an OpenShift cluster, I want to manage certificates and tls for cluster services, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 74 (72 user stories, 2 procedures)

- Adding API server certificates
- Authenticating the cert-manager Operator for Red Hat OpenShift
- Common configurable fields in the CertManager CR for the cert-manager components
- Configuring TLS security profiles
- Customization
- *...and 67 more*

### Job 9: Manage secrets and cloud provider credentials
*When securing an OpenShift cluster, I want to manage secrets and cloud provider credentials, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 40 (40 user stories, 0 procedures)

- Authentication flow for AWS STS
- Configuring Network Policy for the Operand
- Configuring Zero Trust Workload Identity Manager OIDC Federation
- Configuring Zero Trust Workload Identity Manager SPIRE Federation
- Customizing the External Secrets Operator for Red Hat OpenShift
- *...and 35 more*

### Job 10: Secure the container software supply chain
*When securing an OpenShift cluster, I want to secure the container software supply chain, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 8 (8 user stories, 0 procedures)

- Annotating image objects
- Automated verification during updates
- Controlling pod execution
- Deploying containers
- Image metadata
- *...and 3 more*

## Operate and monitor security

### Job 11: Configure auditing and investigate security events
*When securing an OpenShift cluster, I want to configure auditing and investigate security events, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 2 (2 user stories, 0 procedures)

- Allowing JavaScript-based access to the API server from additional hosts
- Configuring the audit log policy

### Job 12: Detect vulnerabilities and unauthorized file changes
*When securing an OpenShift cluster, I want to detect vulnerabilities and unauthorized file changes, so I can reduce risk and meet organizational security requirements.*

**Personas:** Cluster administrator
**Child topics:** 28 (28 user stories, 0 procedures)

- Checking the AIDE configuration
- Configuring the File Integrity Operator
- Determining that the daemon set's pods are running on the expected nodes
- Determining the FileIntegrity object's phase
- File Integrity Operator Overview
- *...and 23 more*
