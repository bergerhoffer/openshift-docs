# CLI Reference --- Consolidation Report

**Document:** cli_reference-combined.adoc
**JTBD Records:** 14 main jobs (no adjustments needed)

---

## Executive Summary

### What's Changing

The CLI Reference documentation is currently organized by CLI tool name. The top-level navigation groups content under ten tool-based sections --- oc, CLI Manager, odo, kn, tkn, argocd, opm, and hcp --- each with its own install/configure/reference lifecycle. Within the oc section, content follows a linear sequence from "Getting started" through "Configuring" to two monolithic alphabetical command references (developer and administrator). This structure requires users to already know which tool they need and then navigate a tool-specific lifecycle to find what they want to accomplish.

This tool-centric organization causes three problems. First, installation procedures for the primary oc CLI are buried inside the "Getting started" assembly, forcing users who simply want to install the CLI to navigate into a multi-topic assembly to find the download instructions. Second, the developer command reference lists approximately 100 commands in alphabetical order, making it difficult for users to find commands by purpose --- a developer debugging a pod must scan from `oc annotate` through `oc whoami` to find `oc debug`, `oc exec`, and `oc logs`. Third, companion CLIs have inconsistent depth: tkn has three pages of install/configure/reference content, while argocd and kn are single-page stubs that redirect elsewhere.

The proposed structure reorganizes the documentation around 14 user goals. Instead of "find the tool, then find the topic," users navigate by asking "What do I want to accomplish?" Each goal is a standalone job with clear prerequisites and labeled approaches. The developer command reference is broken into seven purpose-grouped categories. Installation becomes a first-class job. Companion CLIs receive consistent structure with explicit gap flagging for stub sections.

### Key Improvements

- **Installation elevated to a standalone job:** The four oc installation methods (Customer Portal, web console, RPM, Homebrew) move from inside "Getting started" to Job 2, with a decision guide in the appendix.
- **Developer commands grouped by purpose:** The monolithic alphabetical reference of ~100 commands is reorganized into 7 functional categories (create/deploy, rollouts, CRUD, debug, configure, images, auth).
- **Administrator commands grouped by purpose:** The ~45 `oc adm` commands are reorganized into 3 functional categories (node management, security, maintenance).
- **CLI Manager consolidated from 5 pages to 1 job:** Overview, release notes, install, use, and uninstall pages become 3 user stories under a single goal-oriented job.
- **oc vs kubectl repositioned as configuration context:** The standalone "Usage of oc and kubectl commands" page moves into Job 4 (Configure), where users naturally encounter the question during setup.
- **odo deprecation surfaced in tool selection:** The dead-end odo page is absorbed into Job 1 (Choose the right CLI tool), where users evaluating options will see it.
- **Quick navigation and journey maps added:** Six pre-built user journeys (first-time user, developer, admin, multi-cluster, CI/CD, operator author) provide shortcut paths through the documentation.
- **Stub sections explicitly flagged:** kn and argocd sections are flagged as content gaps rather than appearing as full sections with minimal content.

---

## Current Structure (Feature-Based)

- **CLI tools overview** --- Landing page listing available CLI tools (oc, helm, opm, kn, tkn)
  - List of CLI tools
- **Getting started with the OpenShift CLI** --- Onboarding assembly covering install through first use
  - About the OpenShift CLI
  - Installing the OpenShift CLI (concept)
    - Installing by downloading from the Customer Portal (Linux, Windows, macOS)
    - Installing by downloading from the web console (Linux, Windows, macOS)
    - Installing by using an RPM
    - Installing by using Homebrew
  - Logging in to the OpenShift CLI
  - Logging in to the OpenShift CLI using a web browser
  - Using the OpenShift CLI (7 basic operation procedures)
  - Getting help
  - Logging out of the OpenShift CLI
- **Configuring the OpenShift CLI** --- Post-install shell customization
  - Enabling tab completion for Bash
  - Enabling tab completion for Zsh
  - Accessing kubeconfig by using the oc CLI
- **Usage of oc and kubectl commands** --- Conceptual comparison of the two CLIs
  - The oc binary
  - The kubectl binary
- **Managing CLI profiles** --- Multi-cluster/multi-user configuration
  - About switching between CLI profiles
  - Manually configuring CLI profiles
  - Manual configuration of CLI profiles (reference table)
  - Load and merge rules
- **Extending the OpenShift CLI with plugins** --- Custom plugin development
  - Writing CLI plugins
  - Installing and using CLI plugins
- **OpenShift CLI developer command reference** --- Alphabetical listing of ~100 developer commands
- **OpenShift CLI administrator command reference** --- Alphabetical listing of ~45 `oc adm` commands
- **OpenShift CLI Manager** --- Krew-based plugin distribution (Technology Preview)
  - Overview / About the CLI Manager
  - Release notes (0.1.1, 0.2.0)
  - Installing the CLI Manager (namespace, operator, CliManager resource, Krew index)
  - Using the CLI Manager (search, install, upgrade, uninstall plugins)
  - Uninstalling the CLI Manager
- **Developer CLI (odo)** --- Deprecation redirect to odo.dev
- **Knative CLI (kn)** --- Stub with redirect to Serverless docs
- **Pipelines CLI (tkn)** --- Install, configure, and reference for Tekton CLI
  - Installing tkn (Linux binary, RPM, Windows, macOS)
  - Configuring tkn (Bash tab completion)
  - OpenShift Pipelines tkn reference (10 command groups)
- **GitOps CLI (argocd)** --- Stub with redirect to GitOps docs
- **opm CLI** --- Operator catalog management
  - About the opm CLI
  - Installing the opm CLI
  - opm CLI reference (generate, index, init, migrate, render, serve, validate)
- **Hosted control planes CLI** --- hcp CLI for Day 1 cluster creation
  - Installing from the terminal
  - Installing using the web console
  - Installing using the content gateway

**Total:** 10 top-level tool-based sections, 22 pages/assemblies, ~17,900 source lines, organized by CLI tool name with internal lifecycle ordering (install, configure, use, reference).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Discover**
  - Job 1: Choose the right CLI tool

- **Get Started**
  - Job 2: Install the OpenShift CLI
  - Job 3: Get started with the OpenShift CLI

- **Configure**
  - Job 4: Configure the OpenShift CLI
  - Job 5: Manage CLI profiles

- **Extend**
  - Job 6: Extend the CLI with plugins
  - Job 9: Manage CLI plugins with the CLI Manager

- **Develop**
  - Job 7: Use developer CLI commands

- **Administer**
  - Job 8: Use administrator CLI commands

- **Integrate**
  - Job 10: Use the Knative CLI for serverless workloads
  - Job 11: Use the Pipelines CLI for CI/CD
  - Job 12: Use the GitOps CLI for application delivery
  - Job 13: Use the opm CLI for Operator catalogs
  - Job 14: Use the hcp CLI for hosted control planes

### Detailed Job Descriptions

#### Discover

**Job 1: Choose the right CLI tool**

*When I am new to OpenShift or evaluating CLI options, I want to understand the available CLI tools and their purposes, so I can choose the right tool for my administration or development tasks.*

*Parent topic: CLI tools overview --- provides tool comparison and selection guidance*

Prerequisites: None

- **1.1. Review the CLI tools overview** `[concept]`
  - Lines 2-456: CLI tools overview section (CLI tools overview): Lists oc, helm, opm, kn, tkn with purpose descriptions
  - Context: When first encountering OpenShift and needing to understand which CLI tools are available
- **1.2. Review odo status** `[concept]`
  - Lines 12642-12653: Important update on odo (Developer CLI section): Deprecation notice and redirect to odo.dev
  - Context: When evaluating developer-focused CLI tools and needing to understand odo's current support status

---

#### Get Started

**Job 2: Install the OpenShift CLI**

*When I need to interact with an OpenShift cluster from my terminal, I want to install the OpenShift CLI on my operating system, so I can manage clusters and deploy applications from the command line.*

*Parent topic: Installing the OpenShift CLI --- provides overview of installation methods and version compatibility*

Prerequisites: Access to one of: Red Hat Customer Portal, OpenShift web console, RHEL 8 system, or macOS with Homebrew

- **2.1. Download from the Customer Portal** `[procedure]`
  - Lines 991-1304: Installing by downloading from the Customer Portal (Getting started): OS-specific procedures for Linux, Windows, macOS (arm64 supported)
  - Context: When you have a Red Hat account with an active OpenShift subscription
- **2.2. Download from the web console** `[procedure]`
  - Lines 1312-1467: Installing by downloading from the web console (Getting started): OS-specific procedures for Linux, Windows, macOS
  - Context: When you want to ensure the CLI version matches your cluster version
- **2.3. Install using RPM** `[procedure]`
  - Lines 1479-1549: Installing by using an RPM (Getting started): subscription-manager registration and yum install
  - Context: When you are on RHEL 8 and want system package management (not supported on RHEL 9)
- **2.4. Install using Homebrew** `[procedure]`
  - Lines 1562-1589: Installing by using Homebrew (Getting started): Single `brew install openshift-cli` command
  - Context: When you are on macOS and prefer brew-managed installations

---

**Job 3: Get started with the OpenShift CLI**

*When I have the OpenShift CLI installed, I want to learn how to authenticate, perform basic operations, and get help, so I can begin managing my cluster and applications from the terminal.*

*Parent topic: Getting started with the OpenShift CLI --- provides onboarding workflow from login through first commands*

Prerequisites: Job 2 (Install the OpenShift CLI), access to an OpenShift cluster

- **3.1. Log in to the cluster** `[procedure]`
  - Lines 1600-1664: Logging in to the OpenShift CLI (Getting started): Interactive `oc login` with username/password, proxy support
  - Context: When you have cluster credentials and want to authenticate via the terminal
- **3.2. Log in through a web browser** `[procedure]`
  - Lines 1675-1737: Logging in using a web browser (Getting started): `oc login --web` with browser-based identity provider
  - Context: When you want to avoid exposing tokens on the command line or use an external identity provider
- **3.3. Perform basic operations** `[procedure]`
  - Lines 1748-1993: Using the OpenShift CLI (Getting started): Create project, create app, view pods, view logs, view project status, list API resources
  - Context: When verifying your installation works and learning the fundamental CLI workflow
- **3.4. Get help and log out** `[procedure]`
  - Lines 2005-2125: Getting help and Logging out (Getting started): `oc help`, `oc <command> --help`, `oc explain <resource>`, `oc logout`
  - Context: When you need to find command usage information or end your session

---

#### Configure

**Job 4: Configure the OpenShift CLI**

*When I have installed the OpenShift CLI, I want to configure it for my shell environment and cluster access, so I can work efficiently with tab completion, authentication, and persistent settings.*

*Parent topic: Configuring the OpenShift CLI --- provides overview of post-install configuration options*

Prerequisites: Job 2 (Install the OpenShift CLI)

- **4.1. Enable tab completion** `[procedure]`
  - Lines 2540-2619: Enabling tab completion (Configuring the CLI): Bash (requires bash-completion package) and Zsh setup procedures
  - Context: When you want auto-completion for oc commands and flags in your shell
- **4.2. Export and configure kubeconfig** `[procedure]`
  - Lines 2629-2680: Accessing kubeconfig by using the oc CLI (Configuring the CLI): Export kubeconfig for cross-session and cross-machine access
  - Context: When you need to persist credentials across terminal sessions or share cluster access
- **4.3. Understand oc vs kubectl** `[concept]`
  - Lines 2683-3186: Usage of oc and kubectl commands (Configuring the CLI): oc extends kubectl with OpenShift-specific features; version compatibility matrix
  - Context: When deciding which binary to use and understanding OpenShift-specific capabilities

---

**Job 5: Manage CLI profiles**

*When I work with multiple OpenShift clusters or user accounts, I want to manage CLI profiles and contexts, so I can switch between environments without losing configuration or re-entering credentials.*

*Parent topic: Managing CLI profiles --- provides overview of kubeconfig-based profile management*

Prerequisites: Job 3 (Log in to at least one cluster)

- **5.1. Switch between profiles** `[concept]`
  - Lines 3607-3719: About switching between CLI profiles (Managing CLI profiles): kubeconfig structure, `oc project`, `oc status`, `oc config view`
  - Context: When you need to change the active cluster or project without editing config files
- **5.2. Manually configure profiles** `[procedure]`
  - Lines 3728-3874: Manually configuring CLI profiles (Managing CLI profiles): `oc config set-cluster/set-context/use-context/set/unset/view` commands
  - Context: When you need fine-grained control over multi-cluster configurations beyond `oc login` and `oc project`
- **5.3. Understand load and merge rules** `[concept]`
  - Lines 3882-3921: Load and merge rules (Managing CLI profiles): Precedence order (`--config` flag > `$KUBECONFIG` > `~/.kube/config`), context resolution, auth techniques
  - Context: When multiple kubeconfig files exist and you need to predict which credentials the CLI will use

---

#### Extend

**Job 6: Extend the CLI with plugins**

*When I need CLI functionality that the default oc commands do not provide, I want to extend the OpenShift CLI with custom plugins, so I can perform new and more complex tasks tailored to my workflow.*

*Parent topic: Extending the OpenShift CLI with plugins --- provides overview of the plugin model and naming conventions*

Prerequisites: Job 2 (Install the OpenShift CLI)

- **6.1. Write a CLI plugin** `[procedure]`
  - Lines 4353-4401: Writing CLI plugins (Extending the CLI): Naming conventions (`oc-` or `kubectl-` prefix), sample Bash plugin
  - Context: When you want to create a custom command that integrates with the oc CLI
- **6.2. Install and use a plugin** `[procedure]`
  - Lines 4412-4464: Installing and using CLI plugins (Extending the CLI): `chmod +x`, place in `$PATH`, verify with `oc plugin list`
  - Context: When you have a plugin script ready and want to make it available as an oc subcommand

---

**Job 9: Manage CLI plugins with the CLI Manager**

*When I need to extend OpenShift CLI functionality with plugins, I want to use the CLI Manager Operator to install, update, and manage CLI plugins, so I can provide consistent CLI tooling to cluster users including in disconnected environments.*

*Parent topic: CLI Manager overview --- provides overview of Krew-based plugin distribution (Technology Preview as of OCP 4.22)*

Prerequisites: Job 2 (Install the OpenShift CLI), cluster-admin permissions, Krew installed

- **9.1. Install the CLI Manager Operator** `[procedure]`
  - Lines 10418-11048: Installing the CLI Manager (CLI Manager section): Create namespace, install operator, create CliManager resource, add custom Krew index, add plugins
  - Context: When you want to set up centralized CLI plugin distribution for cluster users
- **9.2. Use CLI plugins via oc krew** `[procedure]`
  - Lines 11050-11668: Using the CLI Manager (CLI Manager section): `oc krew search/info/install/upgrade/uninstall`, server-side plugin upgrades via Plugin resource YAML
  - Context: When you need to discover, install, update, or remove CLI plugins on your workstation
- **9.3. Uninstall the CLI Manager** `[procedure]`
  - Lines 11671-12158: Uninstalling the CLI Manager (CLI Manager section): Uninstall operator via web console, remove namespace and resources
  - Context: When you no longer need centralized plugin management and want to reclaim cluster resources

---

#### Develop

**Job 7: Use developer CLI commands**

*When I am developing and deploying applications on OpenShift, I want to use the oc developer CLI commands to create, build, deploy, debug, and manage my applications, so I can efficiently manage the full application lifecycle from the command line.*

*Parent topic: OpenShift CLI developer command reference --- provides overview of developer-facing oc commands organized by purpose*

Prerequisites: Job 2 (Install the OpenShift CLI), Job 3 (Log in to a cluster)

- **7.1. Create and deploy applications** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc new-app`, `oc new-build`, `oc start-build`, `oc new-project`, `oc expose`
  - Context: When you need to go from source code to a running, accessible application
- **7.2. Manage deployment rollouts and scaling** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc rollout` (cancel/history/latest/pause/restart/resume/retry/status/undo), `oc rollback`, `oc scale`, `oc autoscale`, `oc set triggers`
  - Context: When you need to control how and when application updates are delivered
- **7.3. Inspect, create, modify, and delete resources** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc get/describe/create/delete/edit/apply/patch/replace/annotate/label/diff/explain`
  - Context: When you need to perform CRUD operations on any Kubernetes resource
- **7.4. Debug and troubleshoot running applications** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc debug`, `oc logs`, `oc exec`, `oc rsh`, `oc rsync`, `oc port-forward`, `oc attach`, `oc events`, `oc status`, `oc cp`
  - Context: When your application is not behaving as expected and you need to diagnose the issue
- **7.5. Configure application settings** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc set env/image/image-lookup/probe/resources/route-backends/volumes/data/deployment-hook/serviceaccount/subject/selector`
  - Context: When you need to update application configuration without manually editing YAML
- **7.6. Manage container images** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc import-image`, `oc tag`, `oc image mirror/append/extract/info`, `oc registry login`
  - Context: When you need to control which images are available for deployments
- **7.7. Authenticate and check permissions** `[reference]`
  - Lines 4467-8017: Developer command reference (Developer reference): `oc login/logout/whoami`, `oc auth can-i/reconcile/whoami`, `oc get-token`, `oc policy add-role-to-user/scc-review/scc-subject-review`
  - Context: When you need to manage login sessions or verify you have the required permissions

---

#### Administer

**Job 8: Use administrator CLI commands**

*When I need to perform administrative operations on my OpenShift cluster, I want to use the oc adm CLI commands, so I can configure, maintain, and troubleshoot the cluster efficiently from the command line.*

*Parent topic: OpenShift CLI administrator command reference --- provides overview of oc adm commands organized by operational purpose*

Prerequisites: Job 2 (Install the OpenShift CLI), cluster-admin permissions

- **8.1. Manage nodes** `[reference]`
  - Lines 8535-8854: Node management commands (Administrator reference): `oc adm cordon/uncordon/drain/taint`, `oc adm node-image create/monitor`, `oc adm node-logs`, `oc adm restart-kubelet`, `oc adm reboot-machine-config-pool/wait-for-node-reboot`
  - Context: When you need to safely perform node maintenance without disrupting workloads
- **8.2. Manage security and access control** `[reference]`
  - Lines 8610-9035: Security commands (Administrator reference): `oc adm groups` (add-users/new/prune/remove-users/sync), `oc adm policy` (add/remove cluster-role-to-user/group, add/remove-scc-to-user/group, scc-review, scc-subject-review)
  - Context: When you need to enforce security policies, manage user access, or synchronize LDAP groups
- **8.3. Maintain and troubleshoot the cluster** `[reference]`
  - Lines 9057-9475: Maintenance commands (Administrator reference): `oc adm prune` (builds/deployments/groups/images), `oc adm inspect/must-gather`, `oc adm top` (node/pod/images), `oc adm upgrade`, `oc adm release extract/info/new`, `oc adm wait-for-stable-cluster`
  - Context: When you need to keep the cluster healthy, prune old resources, or troubleshoot issues

---

#### Integrate

**Job 10: Use the Knative CLI for serverless workloads**

*When I need to deploy and manage serverless applications and event-driven architectures, I want to use the Knative CLI to interact with Knative components, so I can perform serverless computing tasks efficiently from the command line.*

*Parent topic: Knative CLI for use with OpenShift Serverless --- provides overview of kn capabilities and link to Serverless documentation*

Prerequisites: OpenShift Serverless Operator installed on the cluster

- **10.1. Review kn capabilities and install** `[concept]`
  - Lines 13060-13084: Knative CLI overview and installation (Knative CLI section): Lists key features (deploy apps, manage Serving/Eventing, autoscaling, plugins); redirects to Serverless docs for installation
  - Context: When evaluating the kn CLI or needing to install it

---

**Job 11: Use the Pipelines CLI for CI/CD**

*When I need to create, run, and manage CI/CD pipelines on OpenShift, I want to use the Pipelines CLI to interact with Tekton pipeline resources, so I can automate build, test, and deployment workflows from the command line.*

*Parent topic: Installing tkn --- provides overview of tkn installation methods and CLI configuration*

Prerequisites: OpenShift Pipelines Operator installed on the cluster

- **11.1. Install the tkn CLI** `[procedure]`
  - Lines 13087-13754: Installing tkn (Pipelines CLI section): Linux binary (x86_64, s390x, ppc64le, arm64), Linux RPM (RHEL 8), Windows, macOS
  - Context: When you need the tkn binary installed on your workstation
- **11.2. Configure tab completion for tkn** `[procedure]`
  - Lines 13757-14208: Configuring tkn (Pipelines CLI section): Bash tab completion setup
  - Context: When you want auto-completion for tkn commands
- **11.3. Look up tkn commands** `[reference]`
  - Lines 14212-15384: OpenShift Pipelines tkn reference (Pipelines CLI section): Utility, pipeline management, pipeline runs, task management, task runs, conditions (deprecated), pipeline resources (deprecated), cluster tasks, triggers, hub interactions
  - Context: When you need the correct syntax for a specific pipeline management operation

---

**Job 12: Use the GitOps CLI for application delivery**

*When I need to manage GitOps-driven application deployments and Argo CD resources, I want to use the argocd CLI to configure and manage OpenShift GitOps, so I can automate application delivery using GitOps principles from the command line.*

*Parent topic: GitOps CLI for use with OpenShift GitOps --- provides overview and link to GitOps documentation*

Prerequisites: OpenShift GitOps Operator installed on the cluster

- **12.1. Review argocd CLI and install** `[concept]`
  - Lines 15386-15811: GitOps CLI overview and installation (GitOps CLI section): One-paragraph description; redirects to GitOps docs for installation and usage
  - Context: When evaluating the argocd CLI or needing to install it

---

**Job 13: Use the opm CLI for Operator catalogs**

*When I need to create, maintain, and distribute Operator catalogs for my cluster, I want to use the opm CLI to manage catalog images from Operator bundles, so I can build and serve custom Operator catalogs that can be consumed by OLM on my cluster.*

*Parent topic: About the opm CLI --- provides overview of catalog creation from bundles and the file-based vs SQLite format distinction*

Prerequisites: Understanding of the Operator Framework bundle format; for RHEL 9: podman 1.9.3+ and glibc 2.28+

- **13.1. Install the opm CLI** `[procedure]`
  - Lines 16254-16325: Installing the opm CLI (opm CLI section): Download from OpenShift mirror, extract, add to PATH
  - Context: When you need the opm binary installed on your workstation
- **13.2. Look up opm commands** `[reference]`
  - Lines 16334-17297: opm CLI reference (opm CLI section): File-based catalog commands (generate dockerfile, init, render, serve, validate) and deprecated SQLite commands (index add/prune/prune-stranded/rm, migrate)
  - Context: When you need the correct syntax for catalog management operations

---

**Job 14: Use the hcp CLI for hosted control planes**

*When I need to create and manage hosted control plane clusters, I want to install and use the hcp CLI, so I can provision hosted clusters on supported platforms from the command line.*

*Parent topic: Hosted control planes CLI --- provides overview of hcp as a Day 1 tool and supported platforms (AWS, agent, kubevirt)*

Prerequisites: multicluster engine for Kubernetes Operator 2.5+ installed on the cluster

- **14.1. Install from the terminal** `[procedure]`
  - Lines 17720-17784: Installing from the terminal (hcp CLI section): Uses `oc get ConsoleCLIDownload` to discover download URL; ensures version compatibility
  - Context: When you have oc CLI access to the cluster and want version-matched hcp binary
- **14.2. Install from the web console** `[procedure]`
  - Lines 17793-17844: Installing using the web console (hcp CLI section): Navigate to Help > Command Line Tools to download
  - Context: When you prefer a graphical download workflow
- **14.3. Install from the content gateway** `[procedure]`
  - Lines 17854-17902: Installing using the content gateway (hcp CLI section): Download from developers.redhat.com; requires multicluster engine 2.7+
  - Context: When you need the CLI before connecting to a cluster (only method that does not require existing cluster access)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By CLI tool name, then lifecycle (install, configure, reference) | By user goal, ordered by workflow progression |
| **Top-level items** | 10 tool-based sections | 14 goal-oriented jobs grouped by CCS use-case category |
| **Navigation model** | "Which tool do I need?" then browse its pages | "What do I want to accomplish?" then find the job |
| **oc installation** | Buried inside "Getting started" assembly | Elevated to standalone Job 2 with decision guide |
| **Developer command reference** | 1 monolithic alphabetical list (~100 commands) | 7 purpose-grouped categories under Job 7 |
| **Administrator command reference** | 1 monolithic alphabetical list (~45 commands) | 3 purpose-grouped categories under Job 8 |
| **CLI Manager** | 5 separate pages (overview, release notes, install, use, uninstall) | 1 job with 3 user stories (install, use, uninstall) |
| **oc vs kubectl** | Standalone page under OpenShift CLI (oc) | Subsection 4.3 under Configure, positioned where users encounter the question |
| **odo** | Standalone dead-end page with deprecation redirect | Absorbed into Job 1 as a deprecation note during tool evaluation |
| **User journey guidance** | None | 6 pre-built journeys and Quick Navigation |

### Job List Adjustments from Suggested Input

The suggested 14 main jobs required **no consolidation adjustments**. The 14 jobs from the JTBD analysis map cleanly to 14 jobs in the proposed structure:

1. **Job 1 (CLI tools overview)** absorbed the odo deprecation notice (JSONL record 40, user_story level) from the separate "Developer CLI (odo)" section, consolidating tool evaluation content into a single entry point.
2. **Job 4 (Configure the OpenShift CLI)** absorbed the "Usage of oc and kubectl commands" content (JSONL record 16, user_story level) from its standalone section, repositioning it as configuration context rather than a standalone conceptual page.
3. **Job 9 (CLI Manager)** consolidated the 5-page CLI Manager section into 3 user stories, removing the release notes page (release notes are not a user goal) and folding the overview into the job's parent topic.

No merges, promotions, or dissolutions of main jobs were required because the 14 JTBD records already represented distinct, non-overlapping user goals with clear boundaries between them.

---

## Consolidation Examples

### Example 1: Developer Command Reference (1 alphabetical list -> 7 purpose-grouped categories)

**Current (Fragmented):**
- Lines 4893-8017: OpenShift CLI (oc) developer commands --- Single alphabetical list of ~100 commands from `oc annotate` to `oc whoami`
- Users must scan the entire list to find commands related to their task
- Debugging commands (`oc debug`, `oc exec`, `oc logs`, `oc rsh`) are scattered between `oc delete` and `oc set`

A developer troubleshooting a failing pod must scan through dozens of unrelated commands to find the debugging tools. There is no grouping by purpose, so users cannot browse by task.

**Proposed (Consolidated):**
- **Job 7: Use developer CLI commands**
  - 7.1. Create and deploy applications (5 commands)
  - 7.2. Manage deployment rollouts and scaling (5 commands)
  - 7.3. Inspect, create, modify, and delete resources (11 commands)
  - 7.4. Debug and troubleshoot running applications (10 commands)
  - 7.5. Configure application settings (12 `oc set` subcommands)
  - 7.6. Manage container images (7 commands)
  - 7.7. Authenticate and check permissions (10 commands)

**Benefit:** A developer debugging a pod goes directly to "7.4 Debug and troubleshoot" and finds `oc debug`, `oc logs`, `oc exec`, `oc rsh`, and `oc port-forward` together --- instead of scanning an alphabetical list of 100 commands to find them scattered between `oc delete` and `oc edit`.

---

### Example 2: CLI Manager (5 pages -> 1 job with 3 user stories)

**Current (Fragmented):**
- Lines 9480-9928: OpenShift CLI Manager overview --- About page
- Lines 9928-10418: OpenShift CLI Manager release notes --- Version 0.1.1 and 0.2.0 release notes
- Lines 10418-11048: Installing the OpenShift CLI Manager --- Namespace, operator, CliManager, Krew index
- Lines 11050-11668: Using the OpenShift CLI Manager --- `oc krew` commands
- Lines 11671-12158: Uninstalling the OpenShift CLI Manager --- Operator removal and cleanup

The CLI Manager content is spread across 5 separate navigation entries. The release notes page is not a user goal and interrupts the install-use-uninstall flow. Users evaluating the CLI Manager must visit 2-3 pages to understand and begin using it.

**Proposed (Consolidated):**
- **Job 9: Manage CLI plugins with the CLI Manager**
  - 9.1. Install the CLI Manager Operator
  - 9.2. Use CLI plugins via oc krew
  - 9.3. Uninstall the CLI Manager

**Benefit:** Overview content becomes the job's introductory context (parent topic). Release notes are removed from navigation (they are not a user goal). The install/use/uninstall sequence is preserved under one goal-oriented entry point, reducing the number of navigation targets from 5 to 1 job with 3 clear user stories.

---

### Example 3: Installation Procedures (buried in Getting Started -> standalone job with decision guide)

**Current (Fragmented):**
- Lines 459-2125: Getting started with the OpenShift CLI --- Monolithic assembly containing installation, login, basic operations, help, and logout
- Installation procedures (lines 978-1589) are nested 2 levels deep inside the getting-started assembly
- No guidance on which installation method to prefer

Users arriving with one question --- "How do I install oc?" --- must navigate into the getting-started assembly and then find the installation sub-section among login, usage, and help content.

**Proposed (Consolidated):**
- **Job 2: Install the OpenShift CLI**
  - 2.1. Download from the Customer Portal
  - 2.2. Download from the web console
  - 2.3. Install using RPM (RHEL 8)
  - 2.4. Install using Homebrew (macOS)
  - Appendix: Installation Method Decision Guide

**Benefit:** Installation becomes a first-class job accessible in one click from the top-level TOC. The four methods are labeled as options with clear "when to use" context. A decision guide table in the appendix helps users choose the right method based on their OS, prerequisites, and preferences.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No CLI tool comparison/decision matrix | Job 1 | Tools listed with brief descriptions but no comparison table | **Medium** --- Users can read individual descriptions but lack a quick-reference table to compare tool capabilities, personas, and use cases |
| No structured CLI troubleshooting guide | Jobs 7, 8 | Debug commands exist in reference but no troubleshooting guide for common CLI errors | **High** --- Users encountering `oc login` failures, certificate errors, or timeout issues have no guided resolution path; likely causes support tickets |
| No observability content | None | No CLI-specific monitoring or logging guidance | **Medium** --- Users must find observability docs outside the CLI reference; `oc adm top` exists but is not connected to a monitoring workflow |
| Knative CLI (kn) is a stub | Job 10 | Single paragraph plus redirect to Serverless docs | **Low** --- Content exists in the Serverless documentation; the gap is about discoverability, not missing information |
| GitOps CLI (argocd) is a stub | Job 12 | Single paragraph plus redirect to GitOps docs | **Low** --- Content exists in the GitOps documentation; the gap is about discoverability, not missing information |
| No CLI version migration guidance | None | No content on upgrading or migrating between oc versions | **Medium** --- Users upgrading clusters need to know if their oc version is compatible and how to upgrade it |
| Missing Zsh/Fish completion for tkn | Job 11 | Only Bash tab completion documented; `tkn completion` supports Zsh | **Low** --- Users can run `tkn completion zsh` independently, but documentation gap may cause confusion |
| No parent topic for Job 7 (developer commands) | Job 7 | Auto-generated reference with no conceptual overview | **High** --- Pre-migration blocker: a parent topic explaining how the ~100 developer commands are organized by purpose must be created before restructuring |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 10 tool-based sections | 14 goal-oriented jobs | More granular, but each item is goal-labeled and self-describing |
| Clicks to find "how to install oc" | 3 (CLI tools > OpenShift CLI > Getting started > Install sections) | 1 (Job 2: Install the OpenShift CLI) | 67% reduction |
| Clicks to find "how to debug a pod" | 3+ (CLI tools > OpenShift CLI > Developer reference > scan alphabetical list) | 2 (Job 7 > 7.4 Debug and troubleshoot) | 33% reduction |
| Sections to browse for debugging commands | ~100 commands in alphabetical list | 10 commands in "Debug and troubleshoot" category | ~90% reduction in browsing scope |
| Clicks to find "how to install tkn" | 2 (Pipelines CLI > Installing tkn) | 2 (Job 11 > 11.1 Install tkn) | No change (already well-structured) |
| Clicks to find "oc vs kubectl" | 2 (OpenShift CLI > Usage of oc and kubectl) | 2 (Job 4 > 4.3 Understand oc vs kubectl) | No change, but better positioned in configuration workflow |
| CLI Manager pages to navigate | 5 separate pages | 1 job with 3 user stories | 60% reduction in navigation targets |
| User journey guidance | None | 6 pre-built journeys (first-time user, developer, admin, multi-cluster, CI/CD, operator author) | New capability |
| Decision guides | None | 2 (installation method, CLI tool comparison) | New capability |

**Final job count: 14** (same as suggested). The 14 JTBD records mapped directly to 14 non-overlapping jobs. Internal consolidation occurred at the user-story level: odo deprecation was absorbed into Job 1, oc-vs-kubectl was repositioned under Job 4, and CLI Manager release notes were removed from navigation. The primary structural improvements come from reorganizing the flat command references into purpose-grouped categories and elevating buried content to first-class jobs.

---

## Document Statistics

| Dimension | Value |
|-----------|-------|
| **Main jobs** | 14 |
| **User stories/approaches** | 41 |
| **Source line range** | Lines 2-17,905 |
| **CLI tools covered** | 8 (oc, kubectl, kn, tkn, argocd, opm, hcp, helm) |
| **Personas** | 3 (Cluster administrator, Developer, Operator author) |
| **CCS categories with coverage** | 7 (Discover, Get Started, Configure, Extend, Develop, Administer, Integrate) |
| **CCS categories with gaps** | 3 (Observe, Troubleshoot, Migrate) |
| **Content distribution** | Getting started and configuration: Jobs 1-5; Extending: Jobs 6, 9; Developer reference: Job 7; Admin reference: Job 8; Companion CLIs: Jobs 10-14 |
