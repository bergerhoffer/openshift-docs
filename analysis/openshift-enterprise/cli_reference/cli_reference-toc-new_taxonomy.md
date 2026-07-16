# CLI Reference
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals*

---

## Guide Overview

**Purpose:** Help users install, configure, and use the OpenShift CLI tools to manage clusters and applications from the command line.
**Personas:** Cluster administrator, Developer, Operator author
**Main Jobs:** 14 core jobs

## Quick Navigation

**I want to:**
- Decide which CLI tool to use → Job 1
- Install the oc CLI → Job 2
- Log in and run my first commands → Job 3
- Set up tab completion and kubeconfig → Job 4
- Switch between clusters or projects → Job 5
- Write or install CLI plugins → Job 6
- Find the right oc developer command → Job 7
- Find the right oc adm command → Job 8
- Manage plugins with the CLI Manager Operator → Job 9
- Work with serverless resources → Job 10
- Run CI/CD pipelines → Job 11
- Manage GitOps deployments → Job 12
- Build Operator catalogs → Job 13
- Create hosted control plane clusters → Job 14

---

# Table of Contents

### Job 1: Choose the right CLI tool
*When I am new to OpenShift or evaluating which CLI tool fits my task*

**Personas:** Cluster administrator, Developer

→ Lines 2-456: CLI tools overview
  Source: CLI tools overview section
  - oc (OpenShift CLI) — cluster management and application deployment
  - helm — Kubernetes package management
  - opm — Operator catalog management
  - kn — Knative serverless workloads
  - tkn — Tekton CI/CD pipelines

→ Lines 12642-12653: Important update on odo
  Source: odo deprecation notice
  - odo documentation moved to odo.dev
  - Supported under Cooperative Community Support model

**Content gap:** No comparison matrix or decision guide for choosing between tools. A table showing use cases, personas, and when to prefer each tool would help users make faster decisions.

---

### Job 2: Install the OpenShift CLI
*When I need to interact with an OpenShift cluster from my terminal*

**Personas:** Cluster administrator, Developer

#### Choose an installation method

- **Option A: Download from the Customer Portal** (When you have a Red Hat account with an active subscription)
  → Lines 991-1304: Installing by downloading from the Customer Portal
    Source: Installing the OpenShift CLI
  - Covers Linux (line 1054), Windows (line 1159), macOS with arm64 support (line 1257)
  - Warns about version incompatibility with earlier oc versions

- **Option B: Download from the web console** (When you want to match the CLI to your cluster version)
  *Persona: Developer*
  → Lines 1312-1467: Installing by downloading from the web console
    Source: Installing the OpenShift CLI
  - Covers Linux (line 1335), Windows (line 1384), macOS (line 1426)
  - Ensures version compatibility with the target cluster

- **Option C: Install using RPM** (When you want system package management on RHEL 8)
  → Lines 1479-1549: Installing by using an RPM
    Source: Installing the OpenShift CLI
  - Requires root/sudo and subscription-manager registration
  - **Not supported on RHEL 9** — download the binary instead

- **Option D: Install using Homebrew** (When you are on macOS and prefer brew)
  *Persona: Developer*
  → Lines 1562-1589: Installing by using Homebrew
    Source: Installing the OpenShift CLI
  - Single command: `brew install openshift-cli`

---

### Job 3: Get started with the OpenShift CLI
*When I have the CLI installed and need to authenticate and perform basic tasks*

**Personas:** Cluster administrator, Developer
**Requires:** Job 2 (Install the OpenShift CLI)

#### 3.1 Authenticate to the cluster
**Goal:** Establish a session with the OpenShift API server.

- **Option A: Log in with credentials**
  → Lines 1600-1664: Logging in to the OpenShift CLI
    Source: Getting started with the OpenShift CLI
  - Interactive username/password login via `oc login`
  - Supports HTTP proxy via environment variables
  - Tip: copy the login command from the web console to skip interactive prompts

- **Option B: Log in through a web browser**
  → Lines 1675-1737: Logging in using a web browser
    Source: Getting started with the OpenShift CLI
  - Uses `oc login --web` with browser-based identity provider flow
  - **Caution:** Runs a localhost HTTP server — use with care on shared workstations

#### 3.2 Perform basic operations
**Goal:** Create a project, deploy an application, and inspect resources.

→ Lines 1748-1993: Using the OpenShift CLI
  Source: Getting started with the OpenShift CLI
  - **Task:** Create a project (line 1764)
  - **Task:** Create an application from source (line 1795)
  - **Task:** View pods (line 1830)
  - **Task:** View pod logs (line 1869)
  - **Task:** View current project status (line 1901, 1932)
  - **Task:** List available API resources (line 1970)

#### 3.3 Get help and log out
**Goal:** Find command usage information and end a session.

→ Lines 2005-2089: Getting help
  Source: Getting started with the OpenShift CLI
  - `oc help` — general help
  - `oc <command> --help` — command-specific help
  - `oc explain <resource>` — resource field documentation

→ Lines 2100-2125: Logging out of the OpenShift CLI
  Source: Getting started with the OpenShift CLI
  - `oc logout` deletes the auth token from both server and local config

---

### Job 4: Configure the OpenShift CLI
*When I want to customize my shell environment and manage cluster credentials*

**Personas:** Developer, Cluster administrator
**Requires:** Job 2 (Install the OpenShift CLI)

#### 4.1 Enable tab completion
**Goal:** Auto-complete commands and flags in the shell.

→ Lines 2540-2619: Enabling tab completion
  Source: Configuring the OpenShift CLI
  - **Bash** (line 2553): Requires the `bash-completion` package
  - **Zsh** (line 2591): Self-contained setup

#### 4.2 Export and configure kubeconfig
**Goal:** Persist cluster credentials for cross-session access.

→ Lines 2629-2680: Accessing kubeconfig by using the oc CLI
  Source: Configuring the OpenShift CLI
  - Export kubeconfig for use across sessions and machines
  - **Security:** Store kubeconfig securely; do not commit to source control

#### 4.3 Understand oc vs kubectl
**Goal:** Know when to use oc and when kubectl suffices.

→ Lines 2683-3186: Usage of oc and kubectl commands
  Source: Configuring the OpenShift CLI
  - oc extends kubectl with OpenShift-specific features (DeploymentConfig, BuildConfig, Route, ImageStream, built-in login, new-app, new-project)
  - The kubectl binary is included when installing the OpenShift CLI
  - Version compatibility matrix between oc client and cluster server

---

### Job 5: Manage CLI profiles
*When I work with multiple clusters or user accounts*

**Personas:** Cluster administrator, Developer
**Requires:** Job 3 (Log in at least once)

#### 5.1 Switch between profiles
**Goal:** Change the active cluster or project without editing config files.

→ Lines 3607-3719: About switching between CLI profiles
  Source: Managing CLI profiles
  - kubeconfig structure (clusters, contexts, current-context, users)
  - Switch projects with `oc project`
  - Verify active context with `oc status` and `oc config view`
  - Re-authenticate as system:admin when needed

#### 5.2 Manually configure profiles
**Goal:** Set up custom profiles for complex multi-cluster environments.

→ Lines 3728-3874: Manually configuring CLI profiles
  Source: Managing CLI profiles
  - Advanced usage for users who need fine-grained control
  - **Task:** `oc config set-cluster` — define cluster entries
  - **Task:** `oc config set-context` — define context entries
  - **Task:** `oc config use-context` — switch active context
  - **Task:** `oc config set` / `unset` — modify individual properties
  - **Task:** `oc config view` — display merged config

#### 5.3 Understand load and merge rules
**Goal:** Predict which credentials the CLI will use when multiple config sources exist.

→ Lines 3882-3921: Load and merge rules
  Source: Managing CLI profiles
  - Precedence: `--config` flag > `$KUBECONFIG` env var > `~/.kube/config`
  - `$KUBECONFIG` supports colon-separated paths for multiple files
  - Context resolution: `--context` flag > `current-context` in config > empty
  - Only one auth technique per user entry

---

### Job 6: Extend the CLI with plugins
*When default oc commands do not cover my workflow*

**Personas:** Developer

#### 6.1 Write a CLI plugin
**Goal:** Create a custom command that integrates with the oc CLI.

→ Lines 4353-4401: Writing CLI plugins
  Source: Extending the OpenShift CLI with plugins
  - Naming convention: `oc-` or `kubectl-` prefix (underscores become dashes in commands)
  - Plugins cannot overwrite built-in oc commands
  - Sample Bash plugin provided

#### 6.2 Install and use a plugin
**Goal:** Make a plugin available as an oc subcommand.

→ Lines 4412-4464: Installing and using CLI plugins
  Source: Extending the OpenShift CLI with plugins
  - **Task:** Make the plugin executable (`chmod +x`)
  - **Task:** Place it in `$PATH`
  - **Task:** Verify with `oc plugin list`

---

### Job 7: Use developer CLI commands
*When I need to manage applications, resources, and deployments*

**Personas:** Developer

#### 7.1 Create and deploy applications
**Goal:** Go from source code to a running, accessible application.

→ Lines 4467-8017: OpenShift CLI developer command reference
  Source: Developer command reference
  - `oc new-app` — create application from source, image, or template (line 6817)
  - `oc new-build` — create build configuration (line 6872)
  - `oc start-build` — trigger a build (line 7879)
  - `oc new-project` — create a project (line 6927)
  - `oc expose` — expose a service as a route (line 5408)

#### 7.2 Manage deployment rollouts and scaling
**Goal:** Control how and when application updates are delivered.

  - `oc rollout` — manage rollouts with cancel, history, latest, pause, restart, resume, retry, status, undo (line 7235)
  - `oc rollback` — revert to a previous deployment (line 7225)
  - `oc scale` — adjust replica count (line 7464)
  - `oc autoscale` — create a horizontal pod autoscaler
  - `oc set triggers` — configure deployment triggers (line 7813)

#### 7.3 Inspect, create, modify, and delete resources
**Goal:** Manage the desired state of cluster resources efficiently.

  - `oc get` / `oc describe` — query resources (line 5427, 6231)
  - `oc create` / `oc delete` — create and remove resources (line 5585, 6192)
  - `oc edit` / `oc apply` / `oc patch` — modify resources (line 6274, 4968, 6945)
  - `oc annotate` / `oc label` — add metadata (line 4900, 6724)
  - `oc diff` — preview changes before applying (line 6259)

#### 7.4 Debug and troubleshoot running applications
**Goal:** Diagnose and resolve issues in running workloads.

  - `oc debug` — launch a debug pod with the same config (line 6152)
  - `oc logs` — view container logs (line 6791)
  - `oc exec` — run commands inside a container (line 6322)
  - `oc rsh` — open a remote shell (line 7388)
  - `oc rsync` — sync files between local and container (line 7413)
  - `oc port-forward` — forward local ports to a pod (line 7057)
  - `oc events` — view cluster events (line 6298)
  - `oc status` — project overview (line 7908)
  - `oc cp` — copy files to/from containers (line 5551)

#### 7.5 Configure application settings
**Goal:** Update application configuration without manually editing YAML.

  - `oc set env` — environment variables (line 6594)
  - `oc set resources` — CPU and memory limits (line 6736)
  - `oc set volumes` — volume mounts (line 7843)
  - `oc set probe` — liveness and readiness probes (line 6715)
  - `oc set image` — container image (line 6658)
  - `oc set route-backends` — traffic splitting (line 6766)
  - `oc set deployment-hook` / `oc set build-hook` — lifecycle hooks (line 6575)
  - `oc set serviceaccount` / `oc set selector` / `oc set subject` — identity and selectors (line 7763, 7776, 7791)

#### 7.6 Manage container images
**Goal:** Control which images are available for deployments.

  - `oc import-image` — import from an external registry into an image stream (line 6706)
  - `oc tag` — tag images into image streams (line 7926)
  - `oc image mirror` — mirror images between registries (line 6614)
  - `oc image append` / `extract` / `info` — manipulate and inspect images (line 6505, 6544, 6593)
  - `oc registry login` — authenticate to the integrated registry (line 7190)

#### 7.7 Authenticate and check permissions
**Goal:** Manage login sessions and verify authorization.

  - `oc login` / `oc logout` / `oc whoami` — session management (line 6752, 6791, 8003)
  - `oc auth can-i` — check if an action is permitted (line 7067)
  - `oc policy add-role-to-user` — grant roles (line 7002)
  - `oc policy scc-review` — check SCC admission (line 7017)

---

### Job 8: Use administrator CLI commands
*When I need to manage nodes, security policies, and cluster health*

**Personas:** Cluster administrator
**Requires:** cluster-admin permissions

#### 8.1 Manage nodes
**Goal:** Safely perform node maintenance without disrupting workloads.

→ Lines 8535-8854: Node management commands
  Source: Administrator command reference
  - `oc adm cordon` / `uncordon` — mark nodes as unschedulable/schedulable
  - `oc adm drain` — evict pods before maintenance
  - `oc adm taint` — apply scheduling taints
  - `oc adm node-image create` / `monitor` — add nodes to clusters
  - `oc adm node-logs` — view node-level logs
  - `oc adm restart-kubelet` — coordinated kubelet restarts
  - `oc adm reboot-machine-config-pool` / `wait-for-node-reboot` — rolling reboots

#### 8.2 Manage security and access control
**Goal:** Enforce security policies and manage user access.

→ Lines 8610-9035: Security and access control commands
  Source: Administrator command reference
  - `oc adm groups` — manage groups (add-users, new, prune, remove-users, sync)
  - `oc adm policy` — manage cluster roles and SCCs
  - LDAP group synchronization via `oc adm groups sync`
  - SCC review commands for checking pod admission

#### 8.3 Maintain and troubleshoot the cluster
**Goal:** Keep the cluster healthy and resolve problems.

→ Lines 9057-9475: Cluster maintenance and troubleshooting commands
  Source: Administrator command reference
  - **Pruning:** `oc adm prune` builds, deployments, groups, images (supports dry-run without `--confirm`)
  - **Diagnostics:** `oc adm inspect`, `oc adm must-gather` (supports multiple plugin images)
  - **Monitoring:** `oc adm top` node, pod, images, imagestreams, PVCs
  - **Upgrades:** `oc adm upgrade`, `oc adm release extract` / `info` / `new`
  - **Cluster stability:** `oc adm wait-for-stable-cluster`

---

### Job 9: Manage CLI plugins with the CLI Manager
*When I want centralized plugin distribution for cluster users*

**Personas:** Cluster administrator, Developer
**Why:** Technology Preview feature as of OCP 4.22. Provides Krew-based plugin management including disconnected environments.

#### 9.1 Install the CLI Manager Operator
**Goal:** Set up centralized CLI plugin infrastructure.

→ Lines 10418-11048: Installing the CLI Manager Operator
  Source: CLI Manager install
  - **Task:** Create the `openshift-cli-manager-operator` namespace
  - **Task:** Install the operator via the web console
  - **Task:** Create a CliManager resource
  - **Task:** Add the custom index to Krew (required for CLI Manager to function)
  - Self-signed certificates must be marked as trusted for Krew

#### 9.2 Use CLI plugins via oc krew
**Goal:** Discover, install, and update CLI plugins from the command line.

*Persona: Developer*
→ Lines 11050-11668: Using the OpenShift CLI Manager
  Source: CLI Manager usage
  - `oc krew search` — discover available plugins
  - `oc krew info` — plugin details
  - `oc krew install` / `upgrade` / `uninstall` — lifecycle management
  - Cluster administrators can upgrade plugins server-side via Plugin resource YAML

#### 9.3 Uninstall the CLI Manager
**Goal:** Remove the operator and clean up resources.

→ Lines 11671-12158: Uninstalling the OpenShift CLI Manager
  Source: CLI Manager uninstall
  - **Task:** Uninstall the operator via the web console
  - **Task:** Remove the `openshift-cli-manager-operator` namespace

---

### Job 10: Use the Knative CLI for serverless workloads
*When I need to deploy and manage serverless applications and event-driven architectures*

**Personas:** Developer
**Requires:** OpenShift Serverless Operator installed on the cluster

→ Lines 13060-13084: Knative CLI overview
  Source: Knative CLI section
  - Deploy serverless applications
  - Manage Knative Serving resources (services, revisions, traffic splitting)
  - Manage Knative Eventing components (event sources, triggers)
  - Configure autoscaling parameters
  - Plugin architecture for extensibility

→ Lines 13081-13084: Installing the Knative CLI
  Source: Knative CLI section
  - Redirects to OpenShift Serverless documentation for installation and detailed usage

**Content gap:** This section is a stub. All kn CLI procedures and reference content live in the Serverless product documentation.

---

### Job 11: Use the Pipelines CLI for CI/CD
*When I need to create, run, and manage Tekton pipelines*

**Personas:** Developer
**Requires:** OpenShift Pipelines Operator installed on the cluster

#### 11.1 Install the tkn CLI
**Goal:** Get the tkn binary installed on my workstation.

→ Lines 13087-13754: Installing tkn
  Source: Pipelines CLI section
  - **Linux binary download** (line 13553): supports x86_64, s390x, ppc64le, arm64
  - **Linux RPM** (line 13603): RHEL 8 only, requires subscription-manager
  - **Windows** (line 13728): zip download
  - **macOS** (line 13729): tar.gz download
  - Also installs `tkn-pac` and `opc` binaries

#### 11.2 Configure tab completion for tkn
**Goal:** Enable auto-completion for tkn commands.

→ Lines 13757-14208: Configuring the OpenShift Pipelines tkn CLI
  Source: Pipelines CLI section
  - Bash tab completion setup
  - Requires `bash-completion` package
  - **Content gap:** No Zsh or Fish configuration documented despite the completion command supporting Zsh

#### 11.3 Look up tkn commands
**Goal:** Find the correct syntax for pipeline management operations.

→ Lines 14212-15384: OpenShift Pipelines tkn reference
  Source: Pipelines CLI section
  - Utility commands (line 14639)
  - Pipeline management (line 14678) and pipeline runs (line 14745)
  - Task management (line 14830) and task runs (line 14898)
  - Condition management (line 14971) — deprecated
  - Pipeline resource management (line 15019) — deprecated
  - Cluster task management (line 15076)
  - Trigger management (line 15137)
  - Hub interaction commands (line 15296) — discover and install reusable tasks from Tekton Hub

---

### Job 12: Use the GitOps CLI for application delivery
*When I need to manage GitOps-driven deployments with Argo CD*

**Personas:** Cluster administrator
**Requires:** OpenShift GitOps Operator installed on the cluster

→ Lines 15386-15811: GitOps CLI overview
  Source: GitOps CLI section
  - Configure and manage OpenShift GitOps and Argo CD resources

→ Lines 15802-15808: Installing the GitOps CLI
  Source: GitOps CLI section
  - Redirects to OpenShift GitOps documentation for installation and detailed usage

**Content gap:** This section is a stub. No argocd commands, syntax, or reference content are included. All substantive content lives in the GitOps product documentation.

---

### Job 13: Use the opm CLI for Operator catalogs
*When I need to create, maintain, and distribute Operator catalogs*

**Personas:** Operator author

#### 13.1 Install the opm CLI
**Goal:** Get the opm binary installed on my workstation.

→ Lines 16254-16325: Installing the opm CLI
  Source: opm CLI section
  - Download from OpenShift mirror site, extract, add to PATH
  - Covers Linux, macOS, and Windows
  - **Requires:** podman 1.9.3+ and glibc 2.28+ on RHEL 9+

#### 13.2 Look up opm commands
**Goal:** Find the correct syntax for catalog management operations.

→ Lines 16334-17297: opm CLI reference
  Source: opm CLI section

  **File-based catalog commands (current):**
  - `opm generate dockerfile` — generate Dockerfile for declarative config (line 16794)
  - `opm init` — initialize a package declaration (line 17116)
  - `opm render` — generate declarative config blobs from bundles (line 17201)
  - `opm serve` — run a GRPC catalog server (line 17231)
  - `opm validate` — validate declarative config files (line 17287)

  **SQLite-format commands (deprecated):**
  - `opm index add` / `prune` / `prune-stranded` / `rm` (line 16873)
  - `opm migrate` — convert SQLite to file-based catalog (line 17155)

---

### Job 14: Use the hcp CLI for hosted control planes
*When I need to create and manage hosted control plane clusters*

**Personas:** Cluster administrator
**Requires:** multicluster engine for Kubernetes Operator 2.5+
**Why:** The hcp CLI is a Day 1 tool for initial cluster creation. Day 2 operations use GitOps or other automation.

#### Choose an installation method

- **Option A: Install from the terminal** (When you have oc CLI access to the cluster)
  → Lines 17720-17784: Installing from the terminal
    Source: Hosted control planes CLI section
  - Uses `oc get ConsoleCLIDownload` to discover the download URL
  - Ensures version compatibility with the installed multicluster engine
  - Includes macOS note about security settings for unsigned binaries

- **Option B: Install from the web console** (When you prefer a graphical workflow)
  → Lines 17793-17844: Installing using the web console
    Source: Hosted control planes CLI section
  - Navigate to Help > Command Line Tools to download

- **Option C: Install from the content gateway** (When you need the CLI before connecting to a cluster)
  → Lines 17854-17902: Installing using the content gateway
    Source: Hosted control planes CLI section
  - Download from developers.redhat.com
  - **Requires:** multicluster engine 2.7+ (stricter than other methods)
  - Only method that does not require existing cluster access

**Supported platforms:** AWS, agent, kubevirt

---

## Appendices

### A. CLI Installation Method Decision Guide

| Method | Best For | OS Support | Prerequisites | Package Management |
|--------|----------|------------|---------------|--------------------|
| Customer Portal binary | Production environments | Linux, Windows, macOS | Red Hat account + subscription | Manual |
| Web console binary | Matching CLI to cluster version | Linux, Windows, macOS | Web console access | Manual |
| RPM | System package management | RHEL 8 only | root/sudo + subscription | yum |
| Homebrew | macOS convenience | macOS only | Homebrew installed | brew |

### B. CLI Tools Comparison

| Tool | Primary Persona | Purpose | Included with oc? |
|------|----------------|---------|-------------------|
| oc | Cluster admin, Developer | Full cluster and app management | — |
| kubectl | Developer | Standard Kubernetes operations | Yes |
| helm | Developer | Package management (charts) | No |
| tkn | Developer | Tekton CI/CD pipelines | No |
| kn | Developer | Knative serverless workloads | No |
| argocd | Cluster admin | GitOps application delivery | No |
| opm | Operator author | Operator catalog management | No |
| hcp | Cluster admin | Hosted control plane provisioning | No |

### C. Category Coverage Analysis

| Category | Coverage | Jobs | Notes |
|----------|----------|------|-------|
| Discover | ✅ | Job 1 | CLI tools overview |
| Get Started | ✅ | Jobs 2, 3 | Installation, login, basic operations |
| Configure | ✅ | Jobs 4, 5 | Shell config, profiles, kubeconfig |
| Extend | ✅ | Jobs 6, 9 | Custom plugins and CLI Manager |
| Use | ✅ | Jobs 7, 8, 10-14 | Developer and admin command references, companion CLIs |
| Observe | ❌ | — | No observability content |
| Troubleshoot | ⚠️ Limited | Job 7 (7.4), Job 8 (8.3) | Debug/inspect commands exist but no troubleshooting guide |
| Upgrade | ⚠️ Limited | Job 8 (8.3) | `oc adm upgrade` exists but no upgrade procedures |
| Migrate | ❌ | — | No migration content |

### Gaps Identified

| Category | Gap | Recommendation |
|----------|-----|----------------|
| Discover | No comparison matrix for choosing between CLI tools | Add decision guide table to Job 1 |
| Observe | No dedicated observability content | Link to monitoring/logging guides |
| Troubleshoot | No structured troubleshooting guide | Add common CLI error resolution section |
| Migrate | No migration content | Add version migration guidance if applicable |
| Knative CLI | Stub section with no procedures | Evaluate whether to expand or remove redirect |
| GitOps CLI | Stub section with no procedures | Evaluate whether to expand or remove redirect |

---

## Navigation Guide

### By User Journey

**First-time CLI user:**
1. Job 1: Choose the right CLI tool
2. Job 2: Install the OpenShift CLI
3. Job 3: Get started (log in, run basic commands)
4. Job 4: Configure tab completion and kubeconfig

**Developer building applications:**
1. Job 7 (7.1): Create and deploy applications
2. Job 7 (7.2): Manage rollouts and scaling
3. Job 7 (7.4): Debug and troubleshoot

**Cluster administrator managing infrastructure:**
1. Job 8 (8.1): Manage nodes
2. Job 8 (8.2): Manage security and access control
3. Job 8 (8.3): Maintain and troubleshoot the cluster

**Multi-cluster operator:**
1. Job 4 (4.2): Export kubeconfig
2. Job 5 (5.1): Switch between profiles
3. Job 5 (5.2): Manually configure profiles

**CI/CD pipeline developer:**
1. Job 11 (11.1): Install tkn
2. Job 11 (11.3): Look up tkn commands
3. Job 7 (7.1): Create and deploy applications

**Operator author building catalogs:**
1. Job 13 (13.1): Install opm
2. Job 13 (13.2): Look up opm commands

---

## Document Statistics

**Main Jobs:** 14
**User Stories/Paths:** 41
**Source Line Range:** Lines 2-17905
**CLI Tools Covered:** 8 (oc, kubectl, kn, tkn, argocd, opm, hcp, helm)
**Personas:** 3 (Cluster administrator, Developer, Operator author)

**Content Distribution:**
- Getting started and configuration: Jobs 1-5 (lines 2-3930)
- Extending the CLI: Job 6 (lines 3931-4464)
- Developer command reference: Job 7 (lines 4467-8017)
- Administrator command reference: Job 8 (lines 8018-9478)
- CLI Manager: Job 9 (lines 9480-12158)
- Companion CLIs: Jobs 10-14 (lines 12642-17905)
