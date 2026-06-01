#!/usr/bin/env python3
"""JTBD pipeline for merged security + authentication books."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TOPIC_MAP = REPO / "_topic_maps" / "_topic_map.yml"
OUTPUT = REPO / "analysis" / "topicmap" / "security-auth"
BOOKS = ("security", "authentication")
DISTRO = "openshift-enterprise"

# Draft main jobs from plan (stable IDs for parent_job assignment)
MAIN_JOBS = [
    {
        "id": "understand-security-layers",
        "title": "Understand OCP security layers and shared responsibility",
        "job_map_stage": "Plan",
        "patterns": [
            r"security-understanding",
            r"security-hosts-vms",
            r"security-hardening",
            r"security-compliance",
            r"security-platform",
            r"security-storage",
            r"security-monitoring",
            r"security-network",
            r"^security/index",
        ],
    },
    {
        "id": "control-sign-in",
        "title": "Control who can sign in to the cluster",
        "job_map_stage": "Secure",
        "patterns": [
            r"understanding-authentication",
            r"configuring-internal-oauth",
            r"configuring-oauth",
            r"identity_providers/",
            r"understanding-identity-provider",
            r"external-auth",
            r"ldap-syncing",
            r"remove-kubeadmin",
            r"managing-oauth-access",
        ],
    },
    {
        "id": "rbac-permissions",
        "title": "Assign and audit permissions with RBAC",
        "job_map_stage": "Secure",
        "patterns": [r"using-rbac", r"impersonating-system-admin"],
    },
    {
        "id": "workload-identities",
        "title": "Configure workload and automation identities",
        "job_map_stage": "Secure",
        "patterns": [
            r"understanding-and-creating-service-accounts",
            r"using-service-accounts",
            r"bound-service-account-tokens",
            r"tokens-scoping",
        ],
    },
    {
        "id": "pod-security",
        "title": "Enforce what pods are allowed to run",
        "job_map_stage": "Secure",
        "patterns": [
            r"managing-security-context-constraints",
            r"understanding-and-managing-pod-security",
            r"security_profiles_operator/",
            r"seccomp-profiles\.adoc",
        ],
    },
    {
        "id": "supply-chain",
        "title": "Secure the container software supply chain",
        "job_map_stage": "Secure",
        "patterns": [
            r"security-container-signature",
            r"security-container-content",
            r"security-registries",
            r"security-build",
            r"security-deploy",
        ],
    },
    {
        "id": "secrets-credentials",
        "title": "Manage secrets and cloud provider credentials",
        "job_map_stage": "Secure",
        "patterns": [
            r"understanding-secrets-management",
            r"external_secrets_operator/",
            r"zero_trust_workload_identity",
            r"managing_cloud_provider_credentials/",
        ],
    },
    {
        "id": "certificates-tls",
        "title": "Manage certificates and TLS for cluster services",
        "job_map_stage": "Secure",
        "patterns": [
            r"certificates/",
            r"certificate_types_descriptions/",
            r"cert_manager_operator/",
            r"tls-security-profiles",
        ],
    },
    {
        "id": "encrypt-at-rest",
        "title": "Encrypt sensitive data at rest",
        "job_map_stage": "Secure",
        "patterns": [
            r"network_bound_disk_encryption/",
            r"nbde_tang_server_operator/",
            r"nbde-",
        ],
    },
    {
        "id": "compliance",
        "title": "Demonstrate compliance with security profiles",
        "job_map_stage": "Secure",
        "patterns": [r"compliance_operator/", r"oc-compliance"],
    },
    {
        "id": "detect-threats",
        "title": "Detect vulnerabilities and unauthorized file changes",
        "job_map_stage": "Operate",
        "patterns": [r"file_integrity_operator/", r"pod-vulnerability-scan"],
    },
    {
        "id": "audit-investigate",
        "title": "Configure auditing and investigate security events",
        "job_map_stage": "Operate",
        "patterns": [
            r"audit-log-",
            r"allowing-javascript-access",
        ],
    },
]


@dataclass
class Topic:
    name: str
    rel_path: str  # path relative to book dir, e.g. certificates/api-server.adoc
    book: str


def _walk_topics(
    topics: list,
    book: str,
    prefix: str,
    out: list[Topic],
) -> None:
    for entry in topics or []:
        if not isinstance(entry, dict):
            continue
        name = entry.get("Name", "")
        subdir = entry.get("Dir", "")
        path_prefix = prefix
        if subdir:
            path_prefix = f"{prefix}{subdir.strip('/')}/"
        if "File" in entry:
            rel = f"{path_prefix}{entry['File']}.adoc"
            out.append(Topic(name=name, rel_path=rel, book=book))
        if "Topics" in entry:
            _walk_topics(entry["Topics"], book, path_prefix, out)


def parse_topic_map() -> dict[str, list[Topic]]:
    """Parse multi-doc YAML topic map for security and authentication books."""
    import yaml

    books: dict[str, list[Topic]] = {b: [] for b in BOOKS}
    with TOPIC_MAP.open(encoding="utf-8") as f:
        for doc in yaml.safe_load_all(f):
            if not isinstance(doc, dict):
                continue
            book = doc.get("Dir")
            if book not in BOOKS:
                continue
            distros = doc.get("Distros", "")
            if isinstance(distros, str):
                distro_list = [d.strip() for d in distros.split(",")]
            else:
                distro_list = list(distros or [])
            if distro_list and DISTRO not in distro_list and "openshift-origin" not in distro_list:
                continue
            _walk_topics(doc.get("Topics", []), book, "", books[book])
    return books


def assign_main_job(rel_path: str, book: str) -> dict:
    key = f"{book}/{rel_path}"
    # More specific jobs are listed later in MAIN_JOBS; evaluate in reverse order.
    for job in reversed(MAIN_JOBS):
        for pat in job["patterns"]:
            if re.search(pat, key):
                return job
    return MAIN_JOBS[0]


def reduce_assembly(book_dir: Path, rel_path: str, out_path: Path) -> bool:
    src = book_dir / rel_path
    if not src.exists():
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["asciidoctor-reducer", str(src), "-o", str(out_path)],
            cwd=book_dir,
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"WARN reduce failed {rel_path}: {e.stderr[:200] if e.stderr else e}", file=sys.stderr)
        return False


def build_include_graph(book: str, topics: list[Topic]) -> dict:
    assemblies = []
    for t in topics:
        asm_path = REPO / book / t.rel_path
        includes = []
        if asm_path.exists():
            for line in asm_path.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(r"^include::([^[]+)\[", line)
                if m:
                    mod = m.group(1)
                    mtype = "UNKNOWN"
                    if "proc-" in mod or "/proc-" in mod:
                        mtype = "PROCEDURE"
                    elif "con-" in mod or "/con-" in mod:
                        mtype = "CONCEPT"
                    elif "ref-" in mod or "/ref-" in mod:
                        mtype = "REFERENCE"
                    elif "snip-" in mod:
                        mtype = "SNIPPET"
                    includes.append({"module": mod, "type": mtype})
        assemblies.append(
            {
                "file": Path(t.rel_path).name,
                "topic_name": t.name,
                "rel_path": t.rel_path,
                "includes": includes,
            }
        )
    return {"book": book, "assemblies": assemblies}


def extract_sections(combined: str) -> list[dict]:
    """Split combined doc by = assembly titles and == sections."""
    sections = []
    lines = combined.splitlines()
    current_asm = None
    current_sec = None
    sec_start = 0
    asm_start = 0

    for i, line in enumerate(lines):
        if line.startswith("= ") and not line.startswith("== "):
            if current_sec and current_asm:
                sections.append(
                    {
                        "assembly": current_asm,
                        "section": current_sec,
                        "start": sec_start,
                        "end": i,
                    }
                )
            current_asm = line[2:].strip()
            current_sec = None
            asm_start = i
        elif line.startswith("== "):
            if current_sec and current_asm:
                sections.append(
                    {
                        "assembly": current_asm,
                        "section": current_sec,
                        "start": sec_start,
                        "end": i,
                    }
                )
            current_sec = line[3:].strip()
            sec_start = i

    if current_sec and current_asm:
        sections.append(
            {
                "assembly": current_asm,
                "section": current_sec,
                "start": sec_start,
                "end": len(lines),
            }
        )
    return sections


def infer_persona(text: str, book: str) -> str:
    lower = text.lower()
    if "developer" in lower or "application" in lower:
        return "Developer"
    if "compliance" in lower or "audit" in lower:
        return "Security or compliance officer"
    if "namespace" in lower or "project admin" in lower:
        return "Namespace administrator"
    if "service account" in lower:
        return "Platform engineer"
    return "Cluster administrator"


def infer_granularity(section: str, content: str) -> str:
    lower = (section + content[:500]).lower()
    if re.search(r"^(install|uninstall|update|upgrade|configure|create|delete|remove|enable|disable|replacing)", section, re.I):
        return "procedure"
    if "procedure" in lower or re.search(r"^\.\s*Step", content, re.M):
        return "procedure"
    if "understanding" in lower or "about " in lower or "overview" in lower:
        return "user_story"
    return "user_story"


def make_job_statement(section: str, topic_name: str) -> str:
    s = section or topic_name
    return (
        f"When working with {topic_name}, I want to {s.lower()}, "
        f"so I can meet security and access requirements for the cluster."
    )


def make_outcomes(section: str) -> list[str]:
    return [
        f"Minimize the time required to complete {section.lower()}",
        f"Minimize the likelihood of errors during {section.lower()}",
    ]


def extract_records_from_topic(
    topic: Topic, reduced_text: str, line_offset: int, doc_name: str
) -> list[dict]:
    records = []
    parent = assign_main_job(topic.rel_path, topic.book)
    sections = extract_sections(reduced_text)
    if not sections:
        # assembly-level record
        records.append(
            {
                "doc": doc_name,
                "section": topic.name,
                "job_statement": make_job_statement(topic.name, topic.name),
                "job_type": "core",
                "persona": infer_persona(reduced_text, topic.book),
                "job_map_stage": parent["job_map_stage"],
                "granularity": "user_story",
                "parent_job": parent["title"],
                "prerequisites": [],
                "related_jobs": [],
                "desired_outcomes": make_outcomes(topic.name),
                "evidence": f"{doc_name} -> {topic.name}, assembly {topic.rel_path}",
                "notes": f"Book: {topic.book}. Assembly: {topic.rel_path}",
                "validation_status": "pending",
            }
        )
        return records

    for sec in sections:
        if sec["section"].lower() in (
            "additional resources",
            "providing feedback on red hat documentation",
        ):
            continue
        start = sec["start"] + line_offset
        end = sec["end"] + line_offset
        gran = infer_granularity(sec["section"], reduced_text)
        records.append(
            {
                "doc": doc_name,
                "section": sec["section"],
                "job_statement": make_job_statement(sec["section"], topic.name),
                "job_type": "core" if gran != "procedure" else "related",
                "persona": infer_persona(reduced_text, topic.book),
                "job_map_stage": parent["job_map_stage"],
                "granularity": gran,
                "parent_job": parent["title"] if gran != "main_job" else None,
                "prerequisites": [],
                "related_jobs": [],
                "desired_outcomes": make_outcomes(sec["section"]),
                "evidence": f"{doc_name} -> {sec['section']}, lines {start}-{end} [{topic.rel_path}]",
                "notes": f"Assembly: {topic.book}/{topic.rel_path}. Topic: {topic.name}",
                "validation_status": "pending",
            }
        )
    return records


def add_main_job_records(all_records: list[dict]) -> list[dict]:
    """Ensure each of the 12 main jobs exists as main_job granularity."""
    existing = {r.get("section") for r in all_records if r.get("granularity") == "main_job"}
    out = list(all_records)
    for job in MAIN_JOBS:
        if job["title"] in existing:
            continue
        child_count = sum(1 for r in all_records if r.get("parent_job") == job["title"])
        out.insert(
            0,
            {
                "doc": "security-auth-combined.adoc",
                "section": job["title"],
                "job_statement": (
                    f"When securing an OpenShift cluster, I want to {job['title'].lower()}, "
                    "so I can reduce risk and meet organizational security requirements."
                ),
                "job_type": "core",
                "persona": "Cluster administrator",
                "job_map_stage": job["job_map_stage"],
                "granularity": "main_job",
                "parent_job": None,
                "prerequisites": [],
                "related_jobs": [],
                "desired_outcomes": [
                    f"Minimize the time required to {job['title'].lower()}",
                    f"Maximize confidence that {job['title'].lower()} is done correctly",
                ],
                "evidence": f"security-auth-consolidated model; {child_count} child records",
                "notes": f"Consolidated main job id: {job['id']}",
                "validation_status": "consolidated",
            },
        )
    return out


def write_jsonl(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_csv(path: Path, records: list[dict]) -> None:
    cols = [
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
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in records:
            row = dict(r)
            for k in ("prerequisites", "related_jobs", "desired_outcomes"):
                if isinstance(row.get(k), list):
                    row[k] = "; ".join(row[k])
            w.writerow(row)


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    books = parse_topic_map()
    all_topics: list[Topic] = []
    for b in BOOKS:
        all_topics.extend(books.get(b, []))
        print(f"{b}: {len(books.get(b, []))} topics")

    topicmap_out = {
        "name": "Security and authentication (merged)",
        "dirs": list(BOOKS),
        "distro": DISTRO,
        "topics": [
            {"book": t.book, "name": t.name, "rel_path": t.rel_path} for t in all_topics
        ],
    }
    (OUTPUT / "security-auth-topicmap.json").write_text(
        json.dumps(topicmap_out, indent=2), encoding="utf-8"
    )

    include_graph = {"books": [build_include_graph(b, books[b]) for b in BOOKS]}
    (OUTPUT / "security-auth-include-graph.json").write_text(
        json.dumps(include_graph, indent=2), encoding="utf-8"
    )

    combined_parts: list[str] = []
    all_records: list[dict] = []
    line_offset = 1
    doc_name = "security-auth-combined.adoc"
    reduced_index: list[dict] = []

    for t in all_topics:
        book_dir = REPO / t.book
        safe = t.rel_path.replace("/", "--")
        out_reduced = OUTPUT / f"{t.book}--{safe.replace('.adoc', '')}-reduced.adoc"
        if not reduce_assembly(book_dir, t.rel_path, out_reduced):
            continue
        reduced_text = out_reduced.read_text(encoding="utf-8", errors="replace")
        reduced_index.append({"topic": t.name, "book": t.book, "path": t.rel_path, "reduced": str(out_reduced.name)})
        combined_parts.append(f"= {t.name}\n\n{reduced_text}\n\n")
        recs = extract_records_from_topic(t, reduced_text, line_offset, doc_name)
        all_records.extend(recs)
        line_offset += reduced_text.count("\n") + 3

    combined_path = OUTPUT / doc_name
    combined_path.write_text("".join(combined_parts), encoding="utf-8")
    print(f"Combined: {combined_path} ({combined_path.stat().st_size} bytes)")

    all_records = add_main_job_records(all_records)
    jsonl_path = OUTPUT / "security-auth-jtbd.jsonl"
    write_jsonl(jsonl_path, all_records)
    write_csv(OUTPUT / "security-auth-jtbd.csv", all_records)
    (OUTPUT / "security-auth-reduced-index.json").write_text(
        json.dumps(reduced_index, indent=2), encoding="utf-8"
    )

    main_count = sum(1 for r in all_records if r["granularity"] == "main_job")
    print(f"Wrote {len(all_records)} records ({main_count} main_job) -> {jsonl_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
