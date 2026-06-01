#!/usr/bin/env python3
"""Reassign parent jobs and write consolidation artifacts."""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import importlib.util

spec = importlib.util.spec_from_file_location(
    "pipeline",
    Path(__file__).parent / "jtbd-security-auth-pipeline.py",
)
pipeline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pipeline)

OUTPUT = Path(__file__).resolve().parents[1] / "analysis" / "topicmap" / "security-auth"
JSONL = OUTPUT / "security-auth-jtbd.jsonl"


def reassign(rec: dict) -> dict:
    if rec.get("granularity") == "main_job":
        return rec
    notes = rec.get("notes", "")
    m = None
    if "Assembly:" in notes:
        asm = notes.split("Assembly:", 1)[1].strip().split(".", 1)[0]
        if "/" in asm:
            book, rel = asm.split("/", 1)
            rel = rel + ".adoc" if not rel.endswith(".adoc") else rel
            job = pipeline.assign_main_job(rel, book)
            rec["parent_job"] = job["title"]
            rec["job_map_stage"] = job["job_map_stage"]
    return rec


def main() -> None:
    records = [json.loads(l) for l in JSONL.read_text().splitlines() if l.strip()]
    for r in records:
        reassign(r)

    # Update main_job child counts in evidence
    counts = Counter(r.get("parent_job") for r in records if r.get("parent_job"))
    for r in records:
        if r.get("granularity") == "main_job":
            c = counts.get(r["section"], 0)
            r["evidence"] = f"security-auth-consolidated model; {c} child records"
            r["validation_status"] = "consolidated"

    out = OUTPUT / "security-auth-jtbd-consolidated.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    summary = {
        "main_jobs": len([r for r in records if r["granularity"] == "main_job"]),
        "user_stories": len([r for r in records if r["granularity"] == "user_story"]),
        "procedures": len([r for r in records if r["granularity"] == "procedure"]),
        "children_per_main_job": dict(counts),
        "merge_notes": [
            "12 main jobs retained (within 10-15 target)",
            "Operator install/upgrade/uninstall topics remain as user stories under parent jobs",
            "SCC/PSA (authentication) and SPO (security) unified under pod-security job",
            "Certificate types reference nested under certificates-tls job",
        ],
    }
    (OUTPUT / "security-auth-consolidation-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    JSONL.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
