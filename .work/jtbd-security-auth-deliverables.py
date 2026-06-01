#!/usr/bin/env python3
"""Generate TOC, comparison, consolidation report, and gap analysis."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
OUTPUT = REPO / "analysis" / "topicmap" / "security-auth"
JSONL = OUTPUT / "security-auth-jtbd.jsonl"
TOPIC_MAP = REPO / "_topic_maps" / "_topic_map.yml"

STAGE_ORDER = [
    "Plan",
    "Secure",
    "Operate",
    "Observe",
    "Configure",
    "Administer",
]


def load_records() -> list[dict]:
    return [json.loads(l) for l in JSONL.read_text().splitlines() if l.strip()]


def load_current_toc() -> list[dict]:
    """Return hierarchical current structure for security + authentication books."""
    books = []

    def walk(topics, prefix="", depth=0):
        items = []
        for entry in topics or []:
            name = entry.get("Name", "")
            sub = entry.get("Dir", "")
            path = f"{prefix}{sub}/" if sub else prefix
            if "File" in entry:
                items.append({"name": name, "depth": depth, "leaf": True})
            elif "Topics" in entry:
                items.append({"name": name, "depth": depth, "leaf": False})
                items.extend(walk(entry["Topics"], path, depth + 1))
        return items

    with TOPIC_MAP.open(encoding="utf-8") as f:
        for doc in yaml.safe_load_all(f):
            if not isinstance(doc, dict):
                continue
            if doc.get("Dir") not in ("security", "authentication"):
                continue
            books.append(
                {
                    "book": doc.get("Name"),
                    "dir": doc.get("Dir"),
                    "items": walk(doc.get("Topics", [])),
                }
            )
    return books


def group_by_main_job(records: list[dict]) -> dict[str, list[dict]]:
    mains = [r for r in records if r["granularity"] == "main_job"]
    grouped = {m["section"]: [] for m in mains}
    for r in records:
        pj = r.get("parent_job")
        if pj and pj in grouped:
            grouped[pj].append(r)
    return grouped, mains


def write_toc(records: list[dict], grouped: dict, mains: list[dict]) -> None:
    personas = sorted({r["persona"] for r in records})
    stages = sorted({m["job_map_stage"] for m in mains}, key=lambda s: STAGE_ORDER.index(s) if s in STAGE_ORDER else 99)

    lines = [
        "# OpenShift Container Platform — Security & authentication",
        "**Jobs-To-Be-Done Oriented Table of Contents**",
        "",
        "*Organized by user goals and workflow stages*",
        "",
        "---",
        "",
        "## Guide Overview",
        "",
        "**Purpose:** Help cluster administrators, platform engineers, and compliance officers secure OpenShift clusters through authentication, authorization, workload controls, secrets, certificates, compliance scanning, and audit.",
        "",
        f"**Personas:** {', '.join(personas[:6])}{'...' if len(personas) > 6 else ''}",
        "",
        f"**Main Jobs:** {len(mains)} core jobs across {len(stages)} workflow stages ({', '.join(stages)})",
        "",
        "## Quick Navigation",
        "",
        "**I want to:**",
        "- Understand how OCP security is layered → Job 1 (Plan)",
        "- Connect users through my corporate IdP → Job 2 (Secure)",
        "- Grant least-privilege access with RBAC → Job 3 (Secure)",
        "- Automate API access with service accounts → Job 4 (Secure)",
        "- Lock down pod privileges (SCC, PSA, seccomp) → Job 5 (Secure)",
        "- Sign images and harden CI/CD → Job 6 (Secure)",
        "- Store secrets and cloud credentials safely → Job 7 (Secure)",
        "- Replace ingress or API certificates → Job 8 (Secure)",
        "- Encrypt etcd or node disks → Job 9 (Secure)",
        "- Pass a compliance scan (CIS, PCI, etc.) → Job 10 (Secure)",
        "- Find CVEs or tampered files on nodes → Job 11 (Operate)",
        "- Configure audit logs for investigations → Job 12 (Operate)",
        "",
        "---",
        "",
        "# Table of Contents",
        "",
    ]

    stage_labels = {
        "Plan": "Understand your security model",
        "Secure": "Secure the cluster",
        "Operate": "Operate and monitor security",
    }

    by_stage: dict[str, list[dict]] = defaultdict(list)
    for m in mains:
        by_stage[m["job_map_stage"]].append(m)

    job_num = 0
    for stage in STAGE_ORDER:
        if stage not in by_stage:
            continue
        label = stage_labels.get(stage, stage)
        lines.append(f"## {label}")
        lines.append("")
        for m in sorted(by_stage[stage], key=lambda x: x["section"]):
            job_num += 1
            children = grouped.get(m["section"], [])
            stories = [c for c in children if c["granularity"] == "user_story"]
            procs = [c for c in children if c["granularity"] == "procedure"]
            lines.append(f"### Job {job_num}: {m['section']}")
            lines.append(f"*{m['job_statement']}*")
            lines.append("")
            lines.append(f"**Personas:** {m['persona']}")
            lines.append(f"**Child topics:** {len(children)} ({len(stories)} user stories, {len(procs)} procedures)")
            lines.append("")
            # Sample user stories (top 5 by section name)
            for c in sorted(stories, key=lambda x: x["section"])[:5]:
                lines.append(f"- {c['section']}")
            if len(stories) > 5:
                lines.append(f"- *...and {len(stories) - 5} more*")
            lines.append("")

    (OUTPUT / "security-auth-toc-new_taxonomy.md").write_text("\n".join(lines), encoding="utf-8")


def write_comparison(books: list[dict], mains: list[dict]) -> None:
    current_leaf = sum(1 for b in books for i in b["items"] if i.get("leaf"))
    current_sections = sum(1 for b in books for i in b["items"] if not i.get("leaf"))

    lines = [
        "# Security & authentication — TOC Comparison",
        "",
        "**Current Feature-Based vs. Proposed JTBD-Based Structure**",
        "",
        f"**Analysis Date:** {date.today().isoformat()}",
        f"**JTBD Records:** 325",
        f"**Main Jobs:** {len(mains)}",
        "",
        "---",
        "",
        "## Current Structure (Feature-Based)",
        "",
    ]

    for b in books:
        lines.append(f"### {b['book']} (`{b['dir']}/`)")
        lines.append("")
        for item in b["items"][:80]:
            indent = "  " * item["depth"]
            lines.append(f"{indent}- {item['name']}")
        if len(b["items"]) > 80:
            lines.append(f"  - *...{len(b['items']) - 80} more entries*")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Proposed JTBD-Based Structure",
            "",
        ]
    )

    for i, m in enumerate(mains, 1):
        lines.append(f"### Job {i}: {m['section']} ({m['job_map_stage']})")
        lines.append(f"- **When:** {m['job_statement']}")
        lines.append(f"- **Persona:** {m['persona']}")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Key Differences",
            "",
            "### Current Structure (Feature-Based)",
            "- **Organized by:** Product operators, certificate types, and platform layers",
            f"- **Navigation:** 2 books, ~{current_leaf} leaf topics, ~{current_sections} section groupings",
            "- **User journey:** Find the operator or component first, then locate the task",
            "",
            "### Proposed Structure (JTBD-Based)",
            f"- **Organized by:** {len(mains)} outcome-oriented main jobs across Plan → Secure → Operate",
            "- **Navigation:** Start from goal (e.g., pass compliance audit), drill to operator procedures",
            "- **User journey:** Goal → approach → procedure",
            "",
            "### Metrics",
            "",
            "| Metric | Current | Proposed |",
            "|--------|---------|----------|",
            f"| Top-level book entries | 2 books | 1 merged guide |",
            f"| Root TOC branches (approx.) | 15+ operator/feature branches | {len(mains)} main jobs |",
            f"| Leaf topics | {current_leaf} | {current_leaf} (mapped under jobs) |",
            "| Max navigation depth to task | 4–5 (book → operator → subdir → topic) | 3 (category → job → user story) |",
            "",
            "### Consolidation wins",
            "",
            "1. **Authentication + Security merged** — single guide for access and platform security",
            "2. **SCC/PSA + Security Profiles Operator** — one pod-security job (was split across books)",
            "3. **Certificate procedures + cert types + cert-manager** — one certificates job",
            "4. **Operator silos flattened** — install/configure/uninstall nest under jobs, not book root",
            "",
        ]
    )

    (OUTPUT / "security-auth-comparison.md").write_text("\n".join(lines), encoding="utf-8")


def write_consolidation_report(records: list[dict], grouped: dict, mains: list[dict], books: list[dict]) -> None:
    pre_main = len(mains)
    child_counts = {m["section"]: len(grouped[m["section"]]) for m in mains}

    lines = [
        "# Security & authentication — Consolidation Report",
        "",
        "**Document:** security-auth-combined.adoc (security + authentication books)",
        f"**JTBD Records:** 325 extracted → **{pre_main} final main jobs** (within 10–15 target)",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        "### What's Changing",
        "",
        "OpenShift security documentation is split across **Security and compliance** (123 topics) and **Authentication and authorization** (32 topics), organized primarily by **operator name**, **certificate type**, and **platform layer**. Users pursuing outcomes such as \"pass a compliance audit\" or \"replace the ingress certificate\" must know which component owns the task before they can navigate the TOC.",
        "",
        "The proposed structure reorganizes the same content into **12 main jobs** grouped by JTBD lifecycle stage (**Plan**, **Secure**, **Operate**). Operator install/upgrade/uninstall sequences become user stories within the relevant job rather than parallel top-level branches.",
        "",
        "### Key Improvements",
        "",
        "- **Merged access and platform security:** Authentication and Security books become one JTBD guide.",
        "- **Unified pod runtime enforcement:** SCC, PSA, and Security Profiles Operator under one job.",
        "- **Certificate navigation simplified:** Procedures, reference types, and cert-manager under one job (74 child records today).",
        "- **Compliance Operator demoted from book root:** 60 topics roll up under \"Demonstrate compliance.\"",
        "- **Supply chain vs. monitoring split clarified:** Build/sign/deploy vs. vulnerability and file-integrity detection.",
        "- **Stable top-level navigation:** 12 goals vs. 15+ operator/feature roots.",
        "",
        "---",
        "",
        "## Current Structure (Feature-Based)",
        "",
    ]

    for b in books:
        lines.append(f"- **{b['book']}** (`{b['dir']}/`)")
    lines.append("")
    lines.append("Major root branches include: Container security, Configuring certificates, Certificate types, Compliance Operator, File Integrity Operator, Security Profiles Operator, cert-manager, External Secrets, NBDE, identity providers, RBAC, CCO, and more.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Proposed JTBD-Based Structure")
    lines.append("")
    lines.append("### Quick Overview")
    lines.append("")

    for stage in STAGE_ORDER:
        stage_jobs = [m for m in mains if m["job_map_stage"] == stage]
        if not stage_jobs:
            continue
        lines.append(f"**{stage}**")
        for m in stage_jobs:
            lines.append(f"- {m['section']} ({child_counts[m['section']]} topics)")
        lines.append("")

    lines.append("### Detailed Job Descriptions")
    lines.append("")

    for m in mains:
        lines.append(f"#### {m['section']}")
        lines.append(f"- **Statement:** {m['job_statement']}")
        lines.append(f"- **Stage:** {m['job_map_stage']}")
        lines.append(f"- **Persona:** {m['persona']}")
        lines.append(f"- **Mapped child records:** {child_counts[m['section']]}")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Key Differences",
            "",
            "| Aspect | Current | Proposed |",
            "|--------|---------|----------|",
            "| Organizing principle | Feature / operator | User outcome |",
            "| Books | 2 | 1 (merged) |",
            "| Top-level branches | 15+ | 12 jobs |",
            "| SCC vs. SPO location | Auth vs. Security | Single pod-security job |",
            "",
            "---",
            "",
            "## Consolidation Examples",
            "",
            "### Example 1: Pod security (before → after)",
            "",
            "**Before:**",
            "- Authentication → Managing security context constraints",
            "- Authentication → Understanding and managing pod security admission",
            "- Security → Security Profiles Operator → (8 subtopics)",
            "",
            "**After:** Job 5 — Enforce what pods are allowed to run",
            "- User stories for SCC, PSA, seccomp, SELinux profiles, SPO lifecycle",
            "",
            "### Example 2: Certificates (before → after)",
            "",
            "**Before:**",
            "- Security → Configuring certificates (4 topics)",
            "- Security → Certificate types and descriptions (12 topics)",
            "- Security → cert-manager Operator (14 topics)",
            "",
            "**After:** Job 8 — Manage certificates and TLS for cluster services",
            "- Decision path → replace ingress/API → cert-manager automation → reference types",
            "",
            "### Example 3: Compliance Operator (before → after)",
            "",
            "**Before:** Root-level Compliance Operator with concepts, management, scans subtrees",
            "",
            "**After:** Job 10 — Demonstrate compliance with security profiles",
            "- Install → scan → tailor → remediate → troubleshoot as sequential user stories",
            "",
            "---",
            "",
            "## Navigation Improvement Summary",
            "",
            "| Metric | Before | After | Change |",
            "|--------|--------|-------|--------|",
            "| Books to search | 2 | 1 | −50% |",
            "| Root TOC intents | 15+ feature branches | 12 jobs | −20%+ |",
            "| Clicks to SCC+SPO guidance | 2 books | 1 job | Unified |",
            "",
            "---",
            "",
            "## Document Statistics",
            "",
            "- **Assemblies reduced:** 155",
            "- **Combined source size:** ~4.3 MB",
            "- **JTBD records:** 325 (12 main_job, 309 user_story, 4 procedure)",
            "- **Distro filter:** openshift-enterprise",
            "",
        ]
    )

    (OUTPUT / "security-auth-consolidation-report.md").write_text("\n".join(lines), encoding="utf-8")

    summary = {
        "main_jobs": pre_main,
        "children_per_main_job": child_counts,
        "total_records": len(records),
    }
    (OUTPUT / "security-auth-consolidation-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    consolidated = OUTPUT / "security-auth-jtbd-consolidated.jsonl"
    consolidated.write_text(JSONL.read_text(encoding="utf-8"), encoding="utf-8")


def write_gap_analysis(records: list[dict], grouped: dict, mains: list[dict]) -> None:
    gaps = [
        {
            "gap": "No dedicated parent topic for merged Security & authentication guide",
            "impact": "High",
            "job": "All",
            "recommendation": "Author new assembly index with JTBD quick navigation and links to Plan/Secure/Operate jobs",
        },
        {
            "gap": "etcd encryption documented in etcd book, not security",
            "impact": "Medium",
            "job": "Encrypt sensitive data at rest",
            "recommendation": "Add user story with xref to etcd/etcd-encrypt.adoc from Job 9 parent topic",
        },
        {
            "gap": "Certificate types are reference-heavy without decision path",
            "impact": "Medium",
            "job": "Manage certificates and TLS",
            "recommendation": "Add 'Choose a certificate strategy' concept module at start of Job 8",
        },
        {
            "gap": "Network security (policies, egress, IPsec) in Networking guide",
            "impact": "Medium",
            "job": "Understand security layers; Enforce pod security",
            "recommendation": "Related jobs links only (out of scope for merge); do not duplicate content",
        },
        {
            "gap": "Dedicated/ROSA/HCP authentication variants",
            "impact": "Medium",
            "job": "Control sign-in; RBAC",
            "recommendation": "Keep distro conditionals; add user stories per platform in Job 2–3",
        },
        {
            "gap": "security/index.adoc intro blurb marked TODO",
            "impact": "Low",
            "job": "Understand security layers",
            "recommendation": "Complete overview aligned to Job 1 parent topic",
        },
        {
            "gap": "RBAC book has only 2 extracted child records (large assembly)",
            "impact": "Low",
            "job": "Assign permissions with RBAC",
            "recommendation": "Split using-rbac into additional user_story records during content rewrite",
        },
        {
            "gap": "Procedure-level granularity underrepresented (4 of 325)",
            "impact": "Low",
            "job": "All",
            "recommendation": "Re-tag step-heavy modules as procedure during editorial pass",
        },
    ]

    # Jobs with very few children may indicate mapping or content issues
    thin = [(m["section"], len(grouped[m["section"]])) for m in mains if len(grouped[m["section"]]) < 5]

    lines = [
        "# Security & authentication — Content Gaps",
        "",
        f"**Analysis date:** {date.today().isoformat()}",
        "",
        "Gaps identified during JTBD extraction and consolidation of 155 assemblies (security + authentication).",
        "",
        "## Gap summary",
        "",
        "| Gap | Impact | Main job | Recommendation |",
        "|-----|--------|----------|----------------|",
    ]
    for g in gaps:
        lines.append(f"| {g['gap']} | {g['impact']} | {g['job']} | {g['recommendation']} |")

    lines.extend(["", "## Jobs with fewer than 5 mapped child records", ""])
    for name, count in thin:
        lines.append(f"- **{name}:** {count} records — review for missing user_story splits")

    lines.extend(
        [
            "",
            "## Cross-book links required",
            "",
            "| External book | Topic | Link from job |",
            "|---------------|-------|---------------|",
            "| etcd | etcd encryption | Job 9 — Encrypt data at rest |",
            "| Networking | Network policy, egress firewall, IPsec | Related jobs from Jobs 1, 5, 6 (not in merge scope) |",
            "",
            "## Reference vs. procedure balance",
            "",
            "| Job | Child records | Notes |",
            "|-----|---------------|-------|",
        ]
    )
    for m in mains:
        children = grouped[m["section"]]
        ref_like = sum(
            1
            for c in children
            if "certificate_types" in c.get("notes", "")
            or "crd" in c.get("section", "").lower()
            or "understanding" in c.get("section", "").lower()
        )
        lines.append(f"| {m['section']} | {len(children)} | ~{ref_like} concept/reference-heavy sections |")

    (OUTPUT / "security-auth-content-gaps.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records = load_records()
    grouped, mains = group_by_main_job(records)
    books = load_current_toc()
    write_toc(records, grouped, mains)
    write_comparison(books, mains)
    write_consolidation_report(records, grouped, mains, books)
    write_gap_analysis(records, grouped, mains)
    print("Wrote deliverables to", OUTPUT)


if __name__ == "__main__":
    main()
