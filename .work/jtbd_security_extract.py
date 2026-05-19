#!/usr/bin/env python3
"""Extract JTBD records for security book and write JSONL/CSV."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

OUTPUT = Path("/home/ahoffer/git/openshift-docs/analysis/openshift-enterprise/security")
COMBINED = OUTPUT / "security-combined.adoc"
TOPICMAP = OUTPUT / "security-topicmap.json"
INCLUDE_GRAPH = OUTPUT / "security-include-graph.json"
DOC = "security-combined.adoc"

# main_job_key -> definition
MAIN_JOBS: dict[str, dict] = {
    "landscape": {
        "job_statement": "When I am responsible for cluster security, I want to understand how OpenShift addresses security and compliance across layers, so I can plan controls and assign ownership.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Plan",
        "sections": ["Security and compliance overview"],
    },
    "container_supply_chain": {
        "job_statement": "When I run containerized workloads, I want to secure images, builds, registries, deployment, networking, and storage, so I can reduce supply-chain and runtime risk.",
        "job_type": "core",
        "persona": "Platform engineer",
        "job_map_stage": "Secure",
        "path_prefixes": ["container_security/"],
        "exclude_files": ["security-compliance"],
    },
    "compliance_understanding": {
        "job_statement": "When my organization must meet regulatory or governance requirements, I want to understand compliance concepts and checking options in OpenShift, so I can choose appropriate controls.",
        "job_type": "core",
        "persona": "Compliance officer",
        "job_map_stage": "Plan",
        "sections": ["Understanding compliance"],
    },
    "compliance_operator": {
        "job_statement": "When I need automated compliance assessment, I want to install and run the Compliance Operator with profiles and remediations, so I can demonstrate and improve regulatory posture.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Secure",
        "path_prefixes": ["compliance_operator/"],
    },
    "file_integrity": {
        "job_statement": "When I must detect unauthorized changes on cluster nodes, I want continuous file integrity monitoring, so I can investigate tampering and support audits.",
        "job_type": "core",
        "persona": "Security engineer",
        "job_map_stage": "Monitor",
        "path_prefixes": ["file_integrity_operator/"],
    },
    "security_profiles": {
        "job_statement": "When I need consistent workload isolation, I want to manage seccomp and SELinux profiles for pods, so I can enforce least-privilege execution.",
        "job_type": "core",
        "persona": "Platform engineer",
        "job_map_stage": "Secure",
        "path_prefixes": ["security_profiles_operator/"],
    },
    "platform_certificates": {
        "job_statement": "When cluster components require trusted TLS, I want to replace and manage ingress, API, and service certificates, so I can meet organizational PKI requirements.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Configure",
        "path_prefixes": ["certificates/"],
    },
    "certificate_reference": {
        "job_statement": "When I troubleshoot TLS or plan certificate rotation, I want to understand each certificate type used by the platform, so I can manage lifecycle and trust correctly.",
        "job_type": "related",
        "persona": "Platform engineer",
        "job_map_stage": "Reference",
        "path_prefixes": ["certificate_types_descriptions/"],
    },
    "cert_manager": {
        "job_statement": "When I need automated X.509 certificate issuance and renewal, I want to deploy and configure the cert-manager Operator, so I can reduce manual certificate operations.",
        "job_type": "core",
        "persona": "Platform engineer",
        "job_map_stage": "Configure",
        "path_prefixes": ["cert_manager_operator/"],
    },
    "nbde_encryption": {
        "job_statement": "When I must protect data at rest on nodes, I want network-bound disk encryption with Tang servers, so I can meet encryption requirements without storing keys on nodes.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Secure",
        "path_prefixes": [
            "network_bound_disk_encryption/",
            "nbde_tang_server_operator/",
        ],
    },
    "zero_trust_identity": {
        "job_statement": "When I adopt zero-trust workload identity, I want to deploy SPIFFE/SPIRE and related federation, so I can authenticate workloads without long-lived secrets.",
        "job_type": "core",
        "persona": "Security architect",
        "job_map_stage": "Configure",
        "title_keywords": ["Zero Trust Workload Identity"],
    },
    "external_secrets": {
        "job_statement": "When sensitive values live in external vaults, I want the External Secrets Operator to sync secrets into the cluster, so I can avoid duplicating secret storage.",
        "job_type": "core",
        "persona": "Platform engineer",
        "job_map_stage": "Configure",
        "title_keywords": ["External Secrets Operator", "External Secret Operator"],
        "sections": [
            "Understanding secrets management",
            "Configuring Network Policy for the Operand",
            "Migrating from the community External Secret Operator to the External Secret Operator For Red Hat OpenShift",
        ],
    },
    "audit_monitoring": {
        "job_statement": "When I need accountability for cluster changes, I want to configure audit policy and review audit logs, so I can support investigations and compliance evidence.",
        "job_type": "core",
        "persona": "Security engineer",
        "job_map_stage": "Observe",
        "sections": [
            "Viewing audit logs",
            "Configuring the audit log policy",
            "Monitoring cluster events and logs",
        ],
    },
    "cluster_hardening": {
        "job_statement": "When I harden a production cluster, I want to configure TLS profiles, seccomp defaults, and API access constraints, so I can reduce attack surface.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Secure",
        "sections": [
            "Configuring TLS security profiles",
            "Configuring seccomp profiles",
            "Allowing JavaScript-based access to the API server from additional hosts",
            "Hardening Red Hat Enterprise Linux CoreOS",
            "Understanding host and VM security",
        ],
    },
    "vulnerability_scanning": {
        "job_statement": "When I deploy container images, I want to scan pods for known vulnerabilities, so I can block or remediate risky workloads before production.",
        "job_type": "core",
        "persona": "Cluster administrator",
        "job_map_stage": "Confirm",
        "sections": ["Scanning pods for vulnerabilities"],
    },
}


def load_topics() -> list[dict]:
    return json.loads(TOPICMAP.read_text(encoding="utf-8"))["topics"]


def assembly_line_range(combined: str, name: str) -> tuple[int, int]:
    marker = f"= {name}\n"
    start = combined.find(marker)
    if start == -1:
        return 0, 0
    start_line = combined[:start].count("\n") + 1
    # next assembly marker: find next topic name at column 0
    rest = combined[start + len(marker) :]
    next_m = re.search(r"\n= [^\n]+\n", rest)
    end = start + len(marker) + (next_m.start() if next_m else len(rest))
    end_line = combined[:end].count("\n") + 1
    return start_line, end_line


def classify_topic(topic: dict) -> str | None:
    rel = topic["rel_path"]
    name = topic["name"]
    for key, spec in MAIN_JOBS.items():
        if spec.get("sections") and name in spec["sections"]:
            return key
        for p in spec.get("path_prefixes", []):
            if rel.startswith(p):
                if spec.get("exclude_files"):
                    base = Path(rel).stem
                    if base in spec["exclude_files"]:
                        continue
                return key
        for kw in spec.get("title_keywords", []):
            if kw in name:
                return key
    return None


def graph_for_assembly(rel_path: str, graph: dict) -> dict | None:
    asm_name = Path(rel_path).name
    for a in graph.get("assemblies", []):
        if a.get("rel_path") == rel_path or a.get("file") == asm_name:
            return a
    return None


def evidence_str(start: int, end: int, section: str, mod_note: str = "") -> str:
    base = f"{DOC} -> Section '{section}', lines {start}-{end}"
    if mod_note:
        base += f" [{mod_note}]"
    return base


def statement_from_title(name: str) -> str:
    n = name
    low = n.lower()
    if low.startswith("understanding"):
        return (
            f"When I need context before changing cluster security, I want to understand {n.removeprefix('Understanding ').removeprefix('Understanding the ')}, "
            f"so I can design controls and explain trade-offs to stakeholders."
        )
    if low.startswith("installing"):
        target = n.removeprefix("Installing ").removeprefix("Installing the ")
        return (
            f"When the capability is not yet available on my cluster, I want to install {target}, "
            f"so I can enable the security feature in supported namespaces."
        )
    if low.startswith("configuring"):
        target = n.removeprefix("Configuring ").removeprefix("Configuring the ")
        return (
            f"When default settings do not meet my security requirements, I want to configure {target}, "
            f"so I can align the cluster with organizational policy."
        )
    if low.startswith("updating"):
        return (
            f"When a supported upgrade path is available, I want to update {n.removeprefix('Updating ').removeprefix('Updating the ')}, "
            f"so I can receive fixes without prolonged exposure to known issues."
        )
    if low.startswith("uninstalling"):
        return (
            f"When I decommission a security capability, I want to uninstall {n.removeprefix('Uninstalling ').removeprefix('Uninstalling the ')}, "
            f"so I can remove unused components and reduce attack surface."
        )
    if low.startswith("troubleshooting"):
        return (
            f"When a security component is not behaving as expected, I want to troubleshoot {n.removeprefix('Troubleshooting ').removeprefix('Troubleshooting the ')}, "
            f"so I can restore expected monitoring or enforcement."
        )
    if low.startswith("managing"):
        return (
            f"When ongoing operation is required, I want to manage {n.removeprefix('Managing ').removeprefix('Managing the ')}, "
            f"so I can keep security controls effective over the cluster lifecycle."
        )
    if "release notes" in low:
        return (
            f"When I plan upgrades, I want to review release notes for this component, "
            f"so I can assess impact and schedule compatible cluster changes."
        )
    if low.startswith("viewing") or low.startswith("monitoring"):
        return (
            f"When I need visibility into cluster security events, I want to {low.split()[0]} relevant logs or metrics, "
            f"so I can detect issues and support audits."
        )
    if "scan" in low or "vulnerabilit" in low:
        return (
            f"When I must assess workload risk, I want to run vulnerability scanning as documented, "
            f"so I can identify images or pods that need remediation before production."
        )
    return (
        f"When this security topic applies to my cluster, I want to follow documented guidance for {n.lower()}, "
        f"so I can implement the control without gaps or rework."
    )


def user_story_for_assembly(
    topic: dict,
    parent_label: str,
    combined: str,
    graph: dict,
) -> dict:
    name = topic["name"]
    start, end = assembly_line_range(combined, name)
    section = name
    rel = topic["rel_path"]
    asm = graph_for_assembly(rel, graph)
    mod_note = ""
    notes = f"Assembly: {rel}"
    if asm and asm.get("includes"):
        inc = asm["includes"][0]
        mod_note = f"module: {inc['module']}, type: {inc['type']}"
        notes += f". Source module: {inc['module']} ({inc['type']})"

    job_statement = statement_from_title(name)
    persona = MAIN_JOBS.get(classify_topic(topic) or "", {}).get(
        "persona", "Cluster administrator"
    )

    return {
        "doc": DOC,
        "section": section,
        "job_statement": job_statement,
        "job_type": "related",
        "persona": persona,
        "job_map_stage": MAIN_JOBS.get(classify_topic(topic) or "", {}).get(
            "job_map_stage", "Secure"
        ),
        "granularity": "user_story",
        "parent_job": parent_label,
        "prerequisites": [],
        "related_jobs": [],
        "desired_outcomes": [
            "Minimize time to find accurate steps for this task",
            "Reduce likelihood of misconfiguration during implementation",
        ],
        "evidence": evidence_str(start, end, section, mod_note),
        "notes": notes,
        "validation_status": None,
        "validation_flags": [],
    }


def main():
    topics = load_topics()
    combined = COMBINED.read_text(encoding="utf-8")
    graph = json.loads(INCLUDE_GRAPH.read_text(encoding="utf-8"))

    records: list[dict] = []

    # Main jobs
    for key, spec in MAIN_JOBS.items():
        # pick first matching topic for evidence (wider excerpt)
        ev_start, ev_end = 1, 120
        for t in topics:
            if classify_topic(t) == key:
                ev_start, ev_end = assembly_line_range(combined, t["name"])
                if ev_start:
                    ev_end = min(ev_start + 120, ev_end)
                    break
        parent_label = spec["job_statement"].split(", so I can")[0].replace(
            "When ", ""
        )
        section_title = spec.get("sections", [None])[0] if spec.get("sections") else None
        if not section_title:
            for t in topics:
                if classify_topic(t) == key:
                    section_title = t["name"]
                    break
        section_title = section_title or key.replace("_", " ").title()
        records.append(
            {
                "doc": DOC,
                "section": section_title,
                "job_statement": spec["job_statement"],
                "job_type": spec["job_type"],
                "persona": spec["persona"],
                "job_map_stage": spec["job_map_stage"],
                "granularity": "main_job",
                "parent_job": None,
                "prerequisites": [],
                "related_jobs": [],
                "desired_outcomes": [
                    "Minimize time to implement required security controls",
                    "Reduce likelihood of security gaps in production clusters",
                ],
                "evidence": evidence_str(
                    ev_start, min(ev_end, ev_start + 80), section_title
                ),
                "notes": f"Main job grouping key: {key}",
                "validation_status": None,
                "validation_flags": [],
            }
        )

    # User stories per assembly (skip if unclassified)
    for topic in topics:
        key = classify_topic(topic)
        if not key:
            continue
        parent = MAIN_JOBS[key]["job_statement"]
        records.append(user_story_for_assembly(topic, parent, combined, graph))

    # Validate grounding (mechanical section + evidence resolution)
    for rec in records:
        flags = []
        m = re.search(r"lines (\d+)-(\d+)", rec.get("evidence", ""))
        if m:
            s, e = int(m.group(1)), int(m.group(2))
            if s < 1 or s > len(combined.splitlines()):
                flags.append("evidence start line out of range")
            else:
                window = combined.splitlines()[s - 1 : min(e, s + 200)]
                excerpt = "\n".join(window)
                title = rec["section"]
                if title not in excerpt:
                    # Assembly titles appear as '= Title' after attribute blocks
                    if f"= {title}" not in combined[max(0, s - 5) : s + 800]:
                        flags.append("section heading not found near cited lines")
        else:
            flags.append("could not parse evidence line range")
            rec["validation_status"] = "no_evidence"
            rec["validation_flags"] = flags
            continue
        rec["validation_status"] = "flag" if flags else "pass"
        rec["validation_flags"] = flags

    jsonl_path = OUTPUT / "security-jtbd.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    csv_cols = [
        "doc",
        "section",
        "job_statement",
        "job_type",
        "persona",
        "job_map_stage",
        "granularity",
        "parent_job",
        "prerequisites",
        "related_jobs",
        "desired_outcomes",
        "evidence",
        "notes",
        "validation_status",
        "validation_flags",
    ]
    csv_path = OUTPUT / "security-jtbd.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=csv_cols, extrasaction="ignore")
        w.writeheader()
        for rec in records:
            row = dict(rec)
            for arr in ("prerequisites", "related_jobs", "desired_outcomes", "validation_flags"):
                if isinstance(row.get(arr), list):
                    row[arr] = "; ".join(row[arr])
            if row.get("parent_job") is None:
                row["parent_job"] = ""
            w.writerow(row)

    main_count = sum(1 for r in records if r["granularity"] == "main_job")
    passed = sum(1 for r in records if r["validation_status"] == "pass")
    flagged = sum(1 for r in records if r["validation_status"] == "flag")
    no_ev = sum(1 for r in records if r["validation_status"] == "no_evidence")
    print(f"Records: {len(records)} ({main_count} main_job)")
    print(f"Validation: {passed} pass, {flagged} flagged, {no_ev} no_evidence")
    print(f"Wrote {jsonl_path} and {csv_path}")


if __name__ == "__main__":
    main()
