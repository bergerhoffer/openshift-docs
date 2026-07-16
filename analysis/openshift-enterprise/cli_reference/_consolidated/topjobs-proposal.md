# OpenShift Container Platform CLI Reference — Top-Level Jobs Proposal

**Product:** OpenShift Container Platform (CLI Reference)
**Date:** 2026-07-15
**Scope:** 1 doc, 55 JTBD records, 14 main jobs → 7 top-level jobs
**Data source:** `analysis/openshift-enterprise/cli_reference/`

---

## Summary

| # | Top-Level Job | CCS Category | Main Jobs Absorbed | Guides |
|---|---------------|-------------|-------------------|--------|
| 1 | Discover CLI tools | Discover | 1 | index, odo-important-update |
| 2 | Install and get started with the OpenShift CLI | Get Started | 2 | getting-started-cli |
| 3 | Configure the CLI environment | Configure | 2 | configuring-cli, usage-oc-kubectl, managing-cli-profiles |
| 4 | Extend the CLI with plugins | Extend | 2 | extending-cli-plugins, cli-manager (5 assemblies) |
| 5 | Look up oc developer commands | Reference | 1 | developer-cli-commands |
| 6 | Look up oc administrator commands | Reference | 1 | administrator-cli-commands |
| 7 | Install and use companion CLIs | Integrate | 5 | kn-cli-tools, tkn_cli (3), gitops-argocd, opm (2), hcp-cli-ref |

---

## Job Details

### Job 1: Discover CLI tools
**Category:** Discover | **Persona(s):** Cluster administrator, Developer

> When I am new to OpenShift or evaluating CLI options, I want to understand the available CLI tools, their purposes, and their current support status, so I can choose the right tool for my workflow.

**Source content:** CLI tools overview (index.adoc), odo deprecation notice (odo-important-update.adoc)

**Stages:**
1. CLI tools overview — review oc, kn, tkn, argocd, opm, hcp
2. Tool comparison and selection — decision matrix (content gap)
3. Deprecated/removed tools — odo deprecation notice

---

### Job 2: Install and get started with the OpenShift CLI
**Category:** Get Started | **Persona(s):** Cluster administrator, Developer

> When I need to start using the OpenShift CLI, I want to install it on my operating system, authenticate to a cluster, and perform basic operations, so I can begin managing my cluster and applications from the command line.

**Source content:** Getting started with the OpenShift CLI (getting-started-cli.adoc) — covers installation (4 methods), login, basic operations, help, logout

**Stages:**
1. Install the CLI — Customer Portal, web console, RPM, Homebrew
2. Authenticate and run first commands — login, create project, deploy app
3. Use help and manage sessions — oc help, oc explain, logout

---

### Job 3: Configure the CLI environment
**Category:** Configure | **Persona(s):** Developer, Cluster administrator

> When I have the OpenShift CLI installed, I want to configure my shell environment, manage authentication profiles, and understand multi-cluster access, so I can work efficiently across clusters and sessions.

**Source content:** Configuring the OpenShift CLI (configuring-cli.adoc), Usage of oc and kubectl commands (usage-oc-kubectl.adoc), Managing CLI profiles (managing-cli-profiles.adoc)

**Stages:**
1. Quick shell setup — tab completion, kubeconfig export
2. Understand oc vs kubectl — binary comparison, version compatibility
3. Multi-cluster profile management — context switching, manual config, load/merge rules

---

### Job 4: Extend the CLI with plugins
**Category:** Extend | **Persona(s):** Developer, Cluster administrator

> When I need CLI functionality beyond the default oc commands, I want to extend the CLI through custom plugins or the CLI Manager Operator, so I can add specialized tooling to my workflow.

**Source content:** Extending the OpenShift CLI with plugins (extending-cli-plugins.adoc), CLI Manager (5 assemblies: index, release-notes, install, using, uninstall)

**Stages:**
1. Write and install a custom plugin — manual plugin development
2. Use the CLI Manager for centralized plugin management — operator-managed Krew
3. Manage CLI Manager lifecycle — uninstall, cleanup

**Note:** CLI Manager is Technology Preview as of OCP 4.22.

---

### Job 5: Look up oc developer commands
**Category:** Reference | **Persona(s):** Developer

> When I am developing and deploying applications on OpenShift, I want to find the right oc commands organized by purpose, so I can efficiently manage the full application lifecycle from the command line.

**Source content:** OpenShift CLI developer command reference (developer-cli-commands.adoc) — ~100 commands, currently alphabetical

**Stages (purpose-grouped):**
1. Create and deploy applications
2. Manage deployments and scaling
3. Inspect and manage resources (CRUD)
4. Debug and troubleshoot applications
5. Configure application settings (oc set)
6. Manage container images
7. Authenticate and check permissions

**Parent topic gap:** No conceptual overview exists. High-impact pre-migration blocker.

---

### Job 6: Look up oc administrator commands
**Category:** Reference | **Persona(s):** Cluster administrator

> When I need to perform administrative operations on my OpenShift cluster, I want to find the right oc adm commands organized by operational purpose, so I can manage nodes, security, and cluster maintenance efficiently from the command line.

**Source content:** OpenShift CLI administrator command reference (administrator-cli-commands.adoc) — ~45 commands, currently alphabetical

**Stages (purpose-grouped):**
1. Manage nodes
2. Manage security and access control
3. Maintain and troubleshoot the cluster

---

### Job 7: Install and use companion CLIs
**Category:** Integrate | **Persona(s):** Developer, Cluster administrator, Operator author

> When I need to manage specific OpenShift platform services from the command line, I want to install and use the purpose-built CLI for that service, so I can perform specialized tasks like pipeline management, serverless deployment, GitOps, Operator catalog building, or hosted cluster provisioning.

**Source content:** 5 companion CLI sections: kn (stub), tkn (3 assemblies), argocd (stub), opm (2 assemblies), hcp (1 assembly)

**Stages:**
1. Pipelines CLI (tkn) — install, configure, reference
2. opm CLI — install, reference
3. Hosted control planes CLI (hcp) — 3 install methods
4. Knative CLI (kn) — stub, redirects to Serverless docs
5. GitOps CLI (argocd) — stub, redirects to GitOps docs

---

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| odo deprecation absorbed into Job 1 | Users evaluating CLI tools should see the deprecation in context |
| oc vs kubectl repositioned into Job 3 | Users encounter the "which binary?" question during configuration |
| CLI Manager release notes removed | Release notes are not a user goal |
| Manual plugins + CLI Manager merged | Both serve the same intent: extending CLI functionality |
| Installation elevated from Getting Started | Installation was buried 2 levels deep |
| Five companion CLIs grouped into one job | Reduces top-level count from 14 to 7 |

---

## Content Gaps

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| No CLI tool comparison matrix | Medium | Add decision guide to Job 1 |
| No developer commands overview | High | Author parent topic for Job 5 |
| No troubleshooting guide | High | Add common CLI error resolution |
| No observability content | Medium | Link to monitoring/logging guides |
| kn/argocd stubs | Low | Evaluate: expand or remove |

---

## Open Questions

1. Should tkn, opm, or hcp be promoted to standalone top-level entries?
2. Should developer + admin command references merge into one job?
3. Should oc vs kubectl live in Discover (Job 1) or Configure (Job 3)?
4. Should the developer commands parent topic be authored before restructuring?
