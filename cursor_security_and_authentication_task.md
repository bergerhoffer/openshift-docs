# Security and authentication tasks for OCP
_Exported on 5/20/2026 at 14:05:29 EDT from Cursor (3.2.21)_

---

**User**

I'm looking to restructure the security and authentication guides for openshift container platform. can you help me determine what the top jobs or tasks are that users need to know or do related to security for OCP?

---

**Cursor**

Exploring existing security/auth documentation structure and any JTBD analysis already in the repos.


Checking how many topics each book contains and whether prior analysis artifacts exist.


**Scope for security JTBD analysis**

> **How should we scope the restructure for identifying top jobs?**
> - One combined "Security & authentication" guide (merge books, single JTBD TOC) ✔
> - Keep two guides (Security and compliance + Authentication and authorization) but align them to a shared JTBD model
> - Security and compliance book only (exclude authentication/authorization for now)

> **Network security content currently lives under the Networking guide (network policies, egress firewall, IPsec, etc.). Include it in this JTBD model?**
> - Yes — treat network security as a main job in the overall OCP security model (even if content stays in Networking)
> - No — focus on the Security + Authentication books only ✔

Creating a plan for a combined Security & authentication JTBD model, excluding network security per your choices.


---

**User**

Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.

---

**Cursor**

Implementing the JTBD workflow: reading the jtbd-tools skills and scripts, then running extraction for security and authentication.


Creating a pipeline script to reduce assemblies, extract JTBD records, and generate deliverables.


Improving topic-map parsing with PyYAML and running the pipeline.


Fixing job assignment order and generating consolidation, TOC, comparison, and gap-analysis deliverables.


The JTBD plan is implemented. All artifacts are under [`analysis/topicmap/security-auth/`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/).

## What was produced

| Artifact | Purpose |
|----------|---------|
| [`security-auth-jtbd.jsonl`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-jtbd.jsonl) | 325 JTBD records from 155 assemblies |
| [`security-auth-jtbd.csv`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-jtbd.csv) | Spreadsheet-friendly export |
| [`security-auth-combined.adoc`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-combined.adoc) | Reduced, concatenated source (~4.3 MB) |
| [`security-auth-toc-new_taxonomy.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md) | Proposed JTBD TOC |
| [`security-auth-comparison.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-comparison.md) | Current vs. proposed structure |
| [`security-auth-consolidation-report.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-consolidation-report.md) | Stakeholder consolidation report |
| [`security-auth-content-gaps.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-content-gaps.md) | Gap analysis and recommendations |

Pipeline scripts (for reruns): [`.work/jtbd-security-auth-pipeline.py`](file:///home/ahoffer/git/openshift-docs/.work/jtbd-security-auth-pipeline.py), [`.work/jtbd-security-auth-deliverables.py`](file:///home/ahoffer/git/openshift-docs/.work/jtbd-security-auth-deliverables.py)

## 12 consolidated main jobs

| # | Main job | Stage | Mapped topics |
|---|----------|-------|---------------|
| 1 | Understand OCP security layers and shared responsibility | Plan | 23 |
| 2 | Control who can sign in to the cluster | Secure | 24 |
| 3 | Assign and audit permissions with RBAC | Secure | 2 |
| 4 | Configure workload and automation identities | Secure | 7 |
| 5 | Enforce what pods are allowed to run | Secure | 37 |
| 6 | Secure the container software supply chain | Secure | 8 |
| 7 | Manage secrets and cloud provider credentials | Secure | 40 |
| 8 | Manage certificates and TLS for cluster services | Secure | 74 |
| 9 | Encrypt sensitive data at rest | Secure | 8 |
| 10 | Demonstrate compliance with security profiles | Secure | 60 |
| 11 | Detect vulnerabilities and unauthorized file changes | Operate | 28 |
| 12 | Configure auditing and investigate security events | Operate | 2 |

This matches the plan’s 12-job model (within the 10–15 target). Largest consolidation opportunities: **certificates (74)**, **compliance (60)**, and **secrets/credentials (40)**.

## Gaps to address in the restructure

Highlights from [`security-auth-content-gaps.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-content-gaps.md):

- **New merged guide index** — no parent assembly yet for the combined book
- **etcd encryption** — cross-link from Job 9 to the etcd book
- **Certificate decision path** — reference-heavy; needs a “start here” user story in Job 8
- **RBAC** — only 2 child records; `using-rbac` should split into more user stories during rewrite
- **Network security** — stays in Networking; link as related jobs only (per your scope)

## Next steps for writers

1. Review [`security-auth-toc-new_taxonomy.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md) and [`security-auth-consolidation-report.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-consolidation-report.md) with stakeholders.
2. Update `_topic_map.yml` to reflect the merged, job-oriented hierarchy.
3. Author Job 1 and Job 8 parent topics first (highest structural gaps).

Re-run extraction after topic map changes:

```bash
python3 .work/jtbd-security-auth-pipeline.py
python3 .work/jtbd-security-auth-deliverables.py
```

