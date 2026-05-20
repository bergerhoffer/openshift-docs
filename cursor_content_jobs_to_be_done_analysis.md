# Content jobs to be done analysis
_Exported on 5/20/2026 at 12:44:33 EDT from Cursor (3.2.21)_

---

**User**

@redhat-docs-agent-tools/plugins/jtbd-tools/skills/jtbd-analyze-topicmap/SKILL.md  Help me analyze content jobs to be done. The topic map is located at "_topic_maps/_topic_map.yml". I'd like to evaluate jobs to be done for the security book (called "Security and compliance") and auth book ("Authentication and authorization"). these are related concepts, so the content should be analyzed together. do not separate the job list out by book. some jobs might include content from both books.

---

**Cursor**

I'll read the JTBD analyze-topicmap skill and locate the topic map for the Security and Authentication books.


Checking for automation scripts and whether asciidoctor-reducer is available; these books are large.


Building the pipeline: parsing both books from the topic map, reducing assemblies, then performing unified JTBD analysis.


Combined content is ~4.3MB. Extracting structure and sampling key sections for unified JTBD analysis.


Extracting topic digests and reading key sections across both books for grounded JTBD analysis.


Writing unified JTBD records grounded in the reduced content and saving outputs per the skill.


Completed a unified JTBD analysis of **Security and compliance** (`security/`, 123 assemblies) and **Authentication and authorization** (`authentication/`, 32 assemblies) from `_topic_maps/_topic_map.yml`. Both books are treated as one job map — records are not split by book.

## Processing summary

| Step | Result |
|------|--------|
| Topic map parse | 155 assemblies in topic-map order |
| Reduction | All 155 reduced with `asciidoctor-reducer` |
| Combined source | `security-auth-combined.adoc` (~108k lines) |
| JTBD extraction | **14 main jobs** + **10 user stories** (unified list) |
| Validation | 24 pass, 0 flagged |

## Unified main jobs (14)

These span both books where the work naturally overlaps (for example RBAC/multitenancy, OAuth, audit):

1. **Establish a secure container supply chain** — images, builds, registries, signatures (`security`)
2. **Harden cluster infrastructure** — host/VM and RHCOS/FCOS hardening (`security`)
3. **Authenticate users and API clients to the cluster** — OAuth, users, API auth (`authentication` + `security-platform`)
4. **Integrate enterprise identity sources with the cluster** — IdPs, LDAP sync (`authentication`)
5. **Define and enforce access permissions on cluster resources** — RBAC, multitenancy (`authentication` + `security`)
6. **Constrain workload security context and admission** — PSA, SCC, admission (`authentication` + `security`)
7. **Manage machine identities for applications and automation** — service accounts, tokens, CCO (`authentication`)
8. **Manage platform and ingress TLS certificates** — cluster PKI (`security`)
9. **Operate certificate and secrets management operators** — cert-manager, External Secrets (`security`)
10. **Demonstrate and maintain regulatory compliance posture** — compliance concepts + Compliance Operator (`security`)
11. **Monitor and investigate security-relevant cluster activity** — audit logs, monitoring, FIO (`security`)
12. **Enforce seccomp, SELinux, and related runtime controls** — SPO, TLS/seccomp profiles (`security`)
13. **Protect data at rest** — NBDE/Tang (`security`)
14. **Segment and protect workload networking and storage** — network/storage security (`security`)

**Sample user stories** (implementation paths under those jobs): image signature verification, LDAP/OIDC IdP setup, SCC management, Compliance Operator scans, File Integrity Operator, OAuth server config, kubeadmin removal, CCO credential modes, admission plugin tuning.

## Cross-book links called out in the analysis

- **Access control**: RBAC (`authentication`) ↔ multitenancy and project isolation (`security/container_security/security-platform.adoc`)
- **Identity**: OAuth/IdP (`authentication`) ↔ “Authentication and authorization” in the container security guide
- **Workload policy**: PSA/SCC (`authentication`) ↔ admission plugins (`security`)
- **Auditability**: API audit logs (`security`) depend on authenticated identities (`authentication`)

## Output files

All artifacts are under `analysis/topicmap/security-auth/`:

| File | Purpose |
|------|---------|
| `security-auth-jtbd.jsonl` | JTBD records (primary) |
| `security-auth-jtbd.csv` | Spreadsheet-friendly export |
| `security-auth-combined.adoc` | Reduced, concatenated source |
| `security-auth-include-graph.json` | Module include graph |
| `security-auth-topicmap.json` | Parsed topic structure |
| `*-reduced.adoc` | Per-assembly reduced files |

Example record (cross-book authentication job):

```3:3:analysis/topicmap/security-auth/security-auth-jtbd.jsonl
{"doc": "security-auth-combined.adoc", "section": "Understanding authentication", "job_statement": "When users and automation interact with the cluster API, I want reliable authentication that identifies every caller, so I can enforce authorization and maintain an accurate audit trail.", ...
```

## Scope note

With 155 assemblies, the skill’s target is ~10–15 **stable main jobs**, not one record per topic. The 10 user stories cover major implementation paths; operators (Compliance, FIO, SPO, cert-manager, etc.) are grouped under the main jobs above. I can expand with more user stories per operator or run `docs-tools:jtbd-toc` on this output if you want a TOC or gap analysis next.

---

**User**

please run jtbd-toc on this next

---

**Cursor**

Generating the JTBD-oriented TOC from the records and writing it to the analysis directory.


Generated the JTBD-oriented TOC from `security-auth-jtbd.jsonl`.

**Output:** [`analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-toc-new_taxonomy.md)

### What's in it

- **14 sequentially numbered main jobs** (unified across both books), grouped by workflow:
  - Getting Started → Secure Your Environment → Set Up & Configure → Confirm & Comply → Track & Investigate
- **10 user stories** nested under their parent jobs (LDAP, OIDC, image signatures, SCC, Compliance scans, FIO, OAuth, kubeadmin, CCO, admission plugins)
- **Quick navigation** (“I want to…” → job links)
- **Appendices:** operator map, IdP selection guide, workflow coverage (✅/⚠️/❌), cross-book dependency diagram
- **Persona-based journeys** (platform admin, cluster admin, compliance officer, security admin)
- Line references using `→ Lines X-Y: Section` from the combined source

### Coverage highlights

| Stage | Status |
|-------|--------|
| Secure, Configure, Operate, Confirm, Monitor | ✅ Covered |
| Troubleshoot | ⚠️ Partial (operator topics only) |
| Migrate / Upgrade | ❌ or ⚠️ Partial |

If you want a structural comparison against the current book TOCs, the next step is `jtbd-compare` on this analysis directory.

---

**User**

yes, jtbd-compare next please

---

**Cursor**

Building the comparison from the topic-map structure and JTBD outputs.


The JTBD comparison is ready.

**Output:** [`analysis/topicmap/security-auth/security-auth-comparison.md`](file:///home/ahoffer/git/openshift-docs/analysis/topicmap/security-auth/security-auth-comparison.md)

### Headline metrics

| | Current (topic map) | Proposed (JTBD) |
|--|---------------------|-----------------|
| Books | 2 separate | 1 unified job map |
| Top-level navigation | **39** sections (19 + 20) | **14** main jobs |
| Leaf assemblies | 155 | 14 jobs + 10 user stories |
| Top-level reduction | — | **~64% fewer** choices |

### Main findings

1. **Book boundary friction** — RBAC, multitenancy, OAuth, and admission content is split between *Security and compliance* and *Authentication and authorization*. The proposed **Jobs 6–9** merge those into one access-control path.

2. **Operator silos** — Compliance, FIO, SPO, cert-manager, and ESO each repeat install/configure/uninstall at the top level. The JTBD map groups them under goals (e.g. **Job 13** compliance, **Job 12** cert/secrets automation).

3. **Strong consolidations** — Nine IdP topics → **Job 7** with LDAP/OIDC options; 17 certificate topics → **Job 11** (procedural + reference nested).

4. **Gaps in both structures** — Cross-operator **troubleshooting**, unified **upgrade**, and **Zero Trust Workload Identity Manager** are not represented as main jobs in the current JTBD set.

### Recommendations in the doc

- Add a unified landing page with the 14-job quick nav while keeping both books on disk  
- Cross-link Jobs 8–9 between books  
- Add an IdP decision table to the auth overview  
- Consider extending JTBD with ZTWI Manager and a troubleshooting job

If you want to go further, options include updating the JTBD records for the gaps above or generating a stakeholder slide outline from this comparison.

