# CLI Reference — TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-07-15
**JTBD Records:** 55
**Main Jobs:** 14 (rolled up from 55 records)

---

## Current Structure (Feature-Based)

```
CLI tools
├── CLI tools overview
├── OpenShift CLI (oc)
│   ├── Getting started with the OpenShift CLI
│   ├── Configuring the OpenShift CLI
│   ├── Usage of oc and kubectl commands
│   ├── Managing CLI profiles
│   ├── Extending the OpenShift CLI with plugins
│   ├── OpenShift CLI developer command reference
│   └── OpenShift CLI administrator command reference
├── OpenShift CLI Manager
│   ├── OpenShift CLI Manager overview
│   ├── OpenShift CLI Manager release notes
│   ├── Installing the OpenShift CLI Manager
│   ├── Using the OpenShift CLI Manager
│   └── Uninstalling the OpenShift CLI Manager
├── Developer CLI (odo)
├── Knative CLI (kn) for use with OpenShift Serverless
├── Pipelines CLI (tkn)
│   ├── Installing tkn
│   ├── Configuring tkn
│   └── Basic tkn commands
├── GitOps CLI (argocd) for use with OpenShift GitOps
├── opm CLI
│   ├── Installing the opm CLI
│   └── opm CLI reference
└── Hosted control planes CLI
```

**Total top-level sections:** 10
**Total pages/assemblies:** 22
**Organization principle:** Grouped by CLI tool, then by lifecycle (install → configure → reference)

---

## Proposed JTBD-Based Structure

```
CLI Reference
├── Job 1:  Choose the right CLI tool
├── Job 2:  Install the OpenShift CLI
│   ├── Option A: Customer Portal binary
│   ├── Option B: Web console binary
│   ├── Option C: RPM (RHEL 8)
│   └── Option D: Homebrew (macOS)
├── Job 3:  Get started with the OpenShift CLI
│   ├── 3.1 Authenticate to the cluster
│   ├── 3.2 Perform basic operations
│   └── 3.3 Get help and log out
├── Job 4:  Configure the OpenShift CLI
│   ├── 4.1 Enable tab completion
│   ├── 4.2 Export and configure kubeconfig
│   └── 4.3 Understand oc vs kubectl
├── Job 5:  Manage CLI profiles
│   ├── 5.1 Switch between profiles
│   ├── 5.2 Manually configure profiles
│   └── 5.3 Understand load and merge rules
├── Job 6:  Extend the CLI with plugins
│   ├── 6.1 Write a CLI plugin
│   └── 6.2 Install and use a plugin
├── Job 7:  Use developer CLI commands
│   ├── 7.1 Create and deploy applications
│   ├── 7.2 Manage deployment rollouts and scaling
│   ├── 7.3 Inspect, create, modify, and delete resources
│   ├── 7.4 Debug and troubleshoot running applications
│   ├── 7.5 Configure application settings
│   ├── 7.6 Manage container images
│   └── 7.7 Authenticate and check permissions
├── Job 8:  Use administrator CLI commands
│   ├── 8.1 Manage nodes
│   ├── 8.2 Manage security and access control
│   └── 8.3 Maintain and troubleshoot the cluster
├── Job 9:  Manage CLI plugins with the CLI Manager
│   ├── 9.1 Install the CLI Manager Operator
│   ├── 9.2 Use CLI plugins via oc krew
│   └── 9.3 Uninstall the CLI Manager
├── Job 10: Use the Knative CLI for serverless workloads
├── Job 11: Use the Pipelines CLI for CI/CD
│   ├── 11.1 Install the tkn CLI
│   ├── 11.2 Configure tab completion for tkn
│   └── 11.3 Look up tkn commands
├── Job 12: Use the GitOps CLI for application delivery
├── Job 13: Use the opm CLI for Operator catalogs
│   ├── 13.1 Install the opm CLI
│   └── 13.2 Look up opm commands
└── Job 14: Use the hcp CLI for hosted control planes
    ├── Option A: Install from terminal
    ├── Option B: Install from web console
    └── Option C: Install from content gateway
```

**Total top-level jobs:** 14
**Total user stories/paths:** 41
**Organization principle:** Grouped by user goal, ordered by workflow progression

---

## Key Differences

### Current Structure (Feature-Based)

| Aspect | Details |
|--------|---------|
| **Organized by** | CLI tool name (oc, tkn, opm, etc.) |
| **Top-level items** | 10 tool-based sections |
| **Navigation model** | Find the right tool section, then browse its pages |
| **User journey** | Implicit — user must know which tool to look under |
| **Command reference** | Two monolithic alphabetical lists (developer, admin) |
| **Installation** | Buried inside "Getting started with the OpenShift CLI" assembly |
| **oc vs kubectl** | Standalone section under OpenShift CLI (oc) |

### Proposed Structure (JTBD-Based)

| Aspect | Details |
|--------|---------|
| **Organized by** | User goals and workflow stages |
| **Top-level items** | 14 goal-oriented jobs |
| **Navigation model** | "What do I want to accomplish?" → find the right job |
| **User journey** | Explicit — Quick Navigation and journey maps guide users |
| **Command reference** | Grouped by purpose (7 functional categories for developer, 3 for admin) |
| **Installation** | Elevated to a standalone Job 2 with decision guide |
| **oc vs kubectl** | Folded into Job 4 (Configure) as context, not a standalone topic |

---

## Structural Changes Detail

### 1. Installation elevated to a first-class job

**Current:** Installation procedures are nested inside "Getting started with the OpenShift CLI," making them hard to find independently.

**Proposed:** Job 2 (Install the OpenShift CLI) is a standalone job with four clearly labeled options and a decision guide in the appendix.

**Benefit:** Users arriving with one question — "How do I install oc?" — find their answer in one click instead of navigating into a getting-started assembly.

### 2. Command references reorganized by purpose

**Current:** The developer command reference is a single monolithic alphabetical list of ~100 commands. Users must scan the full list to find the right command.

**Proposed:** Job 7 breaks the same commands into 7 functional groups (create/deploy, rollouts, CRUD, debug, configure, images, auth). Each group has a goal statement explaining when to use those commands.

**Benefit:** A developer debugging a failing pod goes directly to "7.4 Debug and troubleshoot" instead of scanning an alphabetical list from `oc annotate` to `oc whoami`.

### 3. CLI Manager consolidated from 5 pages to 1 job

**Current:** The CLI Manager has 5 separate pages (overview, release notes, install, use, uninstall) as a standalone section parallel to the oc CLI.

**Proposed:** Job 9 consolidates these into 3 user stories under a single job, positioned after the manual plugin approach (Job 6) for natural progression.

**Benefit:** Users see both plugin approaches (manual and managed) in sequence and can compare them.

### 4. "oc vs kubectl" repositioned as context

**Current:** "Usage of oc and kubectl commands" is a standalone page under the oc CLI section, disconnected from the configuration workflow.

**Proposed:** Folded into Job 4 (Configure the OpenShift CLI) as section 4.3, positioned after tab completion and kubeconfig — where users naturally encounter the question of which binary to use.

**Benefit:** The oc-vs-kubectl decision is surfaced at the moment it matters (during configuration), not as an isolated conceptual page.

### 5. Companion CLIs given consistent structure

**Current:** Companion CLIs (kn, tkn, argocd, opm, hcp) have inconsistent depth — tkn has 3 pages, argocd has 1, hcp has 1.

**Proposed:** Jobs 10-14 give each companion CLI a consistent job-level entry with a clear purpose statement. Stubs (kn, argocd) are explicitly flagged as content gaps rather than silently sparse.

**Benefit:** Users can evaluate whether a companion CLI is documented in-depth or is a redirect to external docs.

### 6. odo deprecation surfaced in context

**Current:** "Developer CLI (odo)" is a standalone top-level section that only contains a deprecation redirect.

**Proposed:** The odo deprecation notice is folded into Job 1 (Choose the right CLI tool), where users evaluating CLI options will naturally encounter it.

**Benefit:** Users evaluating CLI tools learn about odo's status without navigating to a dead-end page.

### 7. Quick navigation and journey maps added

**Current:** No navigation aids beyond the TOC tree. Users must know the tool-based hierarchy.

**Proposed:** Quick Navigation section lets users jump to any job by goal. Navigation Guide provides 6 pre-built user journeys (first-time user, developer, admin, multi-cluster, CI/CD, operator author).

**Benefit:** Users with a specific goal can bypass the entire hierarchy and go directly to relevant content.

---

## Navigation Improvement

| Metric | Current | Proposed | Change |
|--------|---------|----------|--------|
| **Top-level sections** | 10 | 14 jobs | +4 (more granular, but goal-labeled) |
| **Clicks to find "how to install oc"** | 3 (CLI tools → OpenShift CLI → Getting started) | 1 (Job 2) | -67% |
| **Clicks to find "how to debug a pod"** | 3+ (CLI tools → OpenShift CLI → Developer command reference → scan list) | 2 (Job 7 → 7.4 Debug) | -33% |
| **Clicks to find "which CLI tool to use"** | 1 (CLI tools overview) | 1 (Job 1) | Same |
| **Clicks to find "how to install tkn"** | 2 (Pipelines CLI → Installing tkn) | 2 (Job 11 → 11.1) | Same |
| **User journey guidance** | None | 6 pre-built journeys | New |
| **Decision guides** | None | 2 (installation method, CLI tool comparison) | New |

**Key insight:** The biggest navigation wins are for the oc CLI itself (Jobs 1-8), where the current structure buries content under tool-centric groupings. Companion CLIs (Jobs 10-14) already have reasonable depth in the current structure.

---

## Content Mapping: Current → Proposed

| Current Location | Proposed Location | Change Type |
|------------------|-------------------|-------------|
| CLI tools overview | Job 1: Choose the right CLI tool | Renamed, enhanced with decision guide |
| Getting started → Install sections | Job 2: Install the OpenShift CLI | Elevated to standalone job |
| Getting started → Login, Using, Help, Logout | Job 3: Get started with the OpenShift CLI | Restructured into 3 themed groups |
| Configuring the OpenShift CLI | Job 4: Configure the OpenShift CLI | Restructured, oc-vs-kubectl absorbed |
| Usage of oc and kubectl commands | Job 4.3: Understand oc vs kubectl | Demoted from standalone to subsection |
| Managing CLI profiles | Job 5: Manage CLI profiles | Restructured into 3 themed groups |
| Extending the OpenShift CLI with plugins | Job 6: Extend the CLI with plugins | Streamlined |
| Developer command reference | Job 7: Use developer CLI commands | Broken into 7 functional categories |
| Administrator command reference | Job 8: Use administrator CLI commands | Broken into 3 functional categories |
| CLI Manager (5 pages) | Job 9: Manage CLI plugins with the CLI Manager | Consolidated to 3 user stories |
| Developer CLI (odo) | Job 1 (deprecation note) | Absorbed into tool overview |
| Knative CLI (kn) | Job 10: Use the Knative CLI | Flagged as stub |
| Pipelines CLI (tkn, 3 pages) | Job 11: Use the Pipelines CLI for CI/CD | Restructured |
| GitOps CLI (argocd) | Job 12: Use the GitOps CLI | Flagged as stub |
| opm CLI (2 pages) | Job 13: Use the opm CLI | Restructured with deprecated vs current split |
| Hosted control planes CLI | Job 14: Use the hcp CLI | Enhanced with 3 installation options |
| CLI Manager release notes | *Removed from TOC* | Release notes are not a user goal |

---

## Workflow Coverage Comparison

| Category | Current | Proposed | Status |
|----------|---------|----------|--------|
| Discover | ✅ CLI tools overview page | ✅ Job 1 + decision guide | Enhanced |
| Get Started | ✅ Getting started assembly | ✅ Jobs 2, 3 | Split into clearer steps |
| Configure | ✅ Configuring + Profiles pages | ✅ Jobs 4, 5 | Reorganized by goal |
| Extend | ⚠️ Plugins page + CLI Manager section | ✅ Jobs 6, 9 | Better progression |
| Use (Dev) | ✅ Developer command reference | ✅ Job 7 (7 categories) | Reorganized by purpose |
| Use (Admin) | ✅ Administrator command reference | ✅ Job 8 (3 categories) | Reorganized by purpose |
| Use (Companion) | ⚠️ Inconsistent depth across 5 tools | ✅ Jobs 10-14 | Consistent structure, gaps flagged |
| Observe | ❌ No content | ❌ No content | Gap remains |
| Troubleshoot | ⚠️ Debug commands exist in reference | ⚠️ Job 7.4 + Job 8.3 | Elevated but no dedicated guide |
| Upgrade | ⚠️ `oc adm upgrade` in reference | ⚠️ Job 8.3 | No change |
| Migrate | ❌ No content | ❌ No content | Gap remains |

### Gaps Identified

| Category | Gap | Recommendation |
|----------|-----|----------------|
| Discover | No comparison matrix for CLI tools | Add decision table to Job 1 |
| Observe | No observability content in CLI reference | Link to monitoring/logging guides |
| Troubleshoot | No structured troubleshooting guide | Add common CLI errors and resolutions section |
| Migrate | No version migration content | Add oc version upgrade guidance if applicable |
| kn/argocd | Stub sections with no procedures | Evaluate: expand in-place or remove redirects |
| Release notes | CLI Manager release notes not mapped to a job | Keep as reference appendix or move to product release notes |

---

## Example: Content Consolidation

### Developer Command Reference

**Current (Alphabetical, Monolithic):**
```
OpenShift CLI developer command reference
  oc annotate
  oc apply
  oc attach
  oc auth can-i
  ...
  oc whoami
  (~100 commands in alphabetical order)
```

**Proposed (Purpose-Grouped):**
```
Job 7: Use developer CLI commands
  7.1 Create and deploy applications (5 commands)
  7.2 Manage deployment rollouts and scaling (5 commands)
  7.3 Inspect, create, modify, and delete resources (11 commands)
  7.4 Debug and troubleshoot running applications (10 commands)
  7.5 Configure application settings (12 oc set subcommands)
  7.6 Manage container images (7 commands)
  7.7 Authenticate and check permissions (10 commands)
```

**Benefit:** Users searching for "how do I debug my app" go to 7.4 and find `oc debug`, `oc logs`, `oc exec`, `oc rsh`, and `oc port-forward` together — instead of finding them scattered across the alphabet between `oc delete` and `oc edit`.

### CLI Manager Section

**Current (Lifecycle-Based, 5 Pages):**
```
OpenShift CLI Manager
  ├── Overview
  ├── Release notes
  ├── Installing
  ├── Using
  └── Uninstalling
```

**Proposed (Goal-Based, 1 Job):**
```
Job 9: Manage CLI plugins with the CLI Manager
  ├── 9.1 Install the CLI Manager Operator
  ├── 9.2 Use CLI plugins via oc krew
  └── 9.3 Uninstall the CLI Manager
```

**Benefit:** Overview content becomes the job's introductory context. Release notes are removed as a navigation target (they are not a user goal). The install/use/uninstall sequence is preserved but consolidated under one goal-oriented entry point.

---

## Summary of Improvements

| Dimension | Improvement |
|-----------|-------------|
| **Findability** | Quick navigation and journey maps reduce "where is it?" friction |
| **Command reference** | Purpose-grouped commands vs alphabetical scan |
| **Decision support** | Installation method and CLI tool decision guides added |
| **Content gaps** | Stub sections (kn, argocd) explicitly flagged for action |
| **Consistency** | All 14 jobs follow the same structure (goal, personas, user stories) |
| **Deprecation visibility** | odo status surfaced in context rather than as a dead-end page |
| **Release notes** | Removed from navigation hierarchy (not a user goal) |
| **User journeys** | 6 pre-built journeys for common personas |
