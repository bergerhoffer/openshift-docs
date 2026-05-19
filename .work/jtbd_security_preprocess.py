#!/usr/bin/env python3
"""Preprocess security book for JTBD analysis (topic map -> reduced + combined)."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/ahoffer/git/openshift-docs")
TOPIC_MAP = REPO / "_topic_maps/_topic_map.yml"
BOOK_DIR = "security"
DISTRO = "openshift-enterprise"
OUTPUT = REPO / "analysis" / DISTRO / BOOK_DIR


def distro_matches(distros: str | list | None, target: str) -> bool:
    if not distros:
        return True
    if isinstance(distros, str):
        parts = [d.strip() for d in distros.split(",")]
    else:
        parts = [str(d).strip() for d in distros]
    return target in parts


def load_book() -> dict:
    with open(TOPIC_MAP, encoding="utf-8") as f:
        docs = list(__import__("yaml").safe_load_all(f))
    for doc in docs:
        if doc and doc.get("Dir") == BOOK_DIR:
            if distro_matches(doc.get("Distros"), DISTRO):
                return doc
    raise SystemExit(f"Book {BOOK_DIR} not found for distro {DISTRO}")


def walk_topics(
    topics: list,
    book_dir: Path,
    subdir: str = "",
    inherited_distros: str | None = None,
) -> list[dict]:
    """Collect leaf topics with File, respecting distro filters."""
    results = []
    for topic in topics or []:
        name = topic.get("Name", "")
        file_base = topic.get("File")
        topic_distros = topic.get("Distros", inherited_distros)
        nested_dir = topic.get("Dir")
        nested_topics = topic.get("Topics")

        if nested_topics:
            new_subdir = f"{subdir}/{nested_dir}" if nested_dir else subdir
            if nested_dir and not file_base:
                # Section group only
                results.extend(
                    walk_topics(nested_topics, book_dir, new_subdir, topic_distros)
                )
            elif nested_dir and file_base:
                # Has both Dir and nested Topics - unusual; handle file if at this level
                pass
            else:
                results.extend(
                    walk_topics(nested_topics, book_dir, subdir, topic_distros)
                )

        if file_base:
            if not distro_matches(topic_distros, DISTRO):
                continue
            rel = f"{subdir}/{file_base}.adoc" if subdir else f"{file_base}.adoc"
            rel = rel.lstrip("/")
            full = book_dir / rel
            results.append(
                {
                    "name": name,
                    "file": file_base,
                    "rel_path": rel,
                    "full_path": str(full),
                }
            )

        if nested_dir and nested_topics and not file_base:
            new_subdir = f"{subdir}/{nested_dir}" if subdir else nested_dir
            results.extend(
                walk_topics(nested_topics, book_dir, new_subdir, topic_distros)
            )

    return results


def walk_topics_v2(
    topics: list,
    book_dir: Path,
    subdir: str = "",
    inherited_distros: str | None = None,
) -> list[dict]:
    """Walk topic tree; collect assemblies with File field."""
    results: list[dict] = []
    for topic in topics or []:
        name = topic.get("Name", "")
        file_base = topic.get("File")
        topic_distros = topic.get("Distros") or inherited_distros
        nested_dir = topic.get("Dir")
        nested_topics = topic.get("Topics")

        if nested_topics:
            child_subdir = subdir
            if nested_dir:
                child_subdir = f"{subdir}/{nested_dir}" if subdir else nested_dir
            results.extend(
                walk_topics_v2(nested_topics, book_dir, child_subdir, topic_distros)
            )
        elif file_base:
            if not distro_matches(topic_distros, DISTRO):
                continue
            rel = f"{subdir}/{file_base}.adoc" if subdir else f"{file_base}.adoc"
            rel = rel.lstrip("/")
            full = book_dir / rel
            results.append(
                {
                    "name": name,
                    "file": file_base,
                    "rel_path": rel,
                    "full_path": str(full),
                }
            )

    return results


def module_type(path: str) -> str:
    p = path.lower()
    if "con-" in p or "/con-" in p:
        return "CONCEPT"
    if "proc-" in p or "/proc-" in p:
        return "PROCEDURE"
    if "ref-" in p or "/ref-" in p:
        return "REFERENCE"
    if "snip-" in p or "/snip-" in p:
        return "SNIPPET"
    return "UNKNOWN"


def parse_includes(assembly_path: Path) -> list[dict]:
    includes = []
    if not assembly_path.exists():
        return includes
    text = assembly_path.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(
        r"include::([^\[]+)\[([^\]]*)\]", text
    ):
        mod = m.group(1).strip()
        opts = m.group(2)
        leveloffset = ""
        if "leveloffset" in opts:
            lo = re.search(r"leveloffset=([^\s,]+)", opts)
            if lo:
                leveloffset = lo.group(1)
        includes.append(
            {
                "module": mod,
                "type": module_type(mod),
                "leveloffset": leveloffset,
            }
        )
    return includes


def reduce_assembly(book_path: Path, rel_path: str, out_path: Path) -> bool:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "asciidoctor-reducer",
        rel_path,
        "-o",
        str(out_path),
    ]
    r = subprocess.run(
        cmd,
        cwd=book_path,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(f"FAIL {rel_path}: {r.stderr[:500]}", file=sys.stderr)
        return False
    return True


def main() -> None:
    import yaml

    book = load_book()
    book_path = REPO / BOOK_DIR
    OUTPUT.mkdir(parents=True, exist_ok=True)

    topics = walk_topics_v2(book.get("Topics", []), book_path)
    # Deduplicate by rel_path (security-hardening appears twice for different distros)
    seen: set[str] = set()
    unique_topics = []
    for t in topics:
        if t["rel_path"] in seen:
            continue
        seen.add(t["rel_path"])
        if Path(t["full_path"]).exists():
            unique_topics.append(t)
        else:
            print(f"MISSING: {t['full_path']}", file=sys.stderr)

    print(f"Assemblies: {len(unique_topics)}")

    include_graph = {
        "book": BOOK_DIR,
        "book_name": book.get("Name"),
        "distro": DISTRO,
        "assemblies": [],
    }

    reduced_paths = []
    for t in unique_topics:
        stem = t["rel_path"].replace("/", "_").replace(".adoc", "")
        out_reduced = OUTPUT / f"{stem}-reduced.adoc"
        ok = reduce_assembly(book_path, t["rel_path"], out_reduced)
        if not ok:
            continue
        reduced_paths.append((t, out_reduced))
        asm_file = Path(t["full_path"]).name
        include_graph["assemblies"].append(
            {
                "file": asm_file,
                "topic_name": t["name"],
                "rel_path": t["rel_path"],
                "includes": parse_includes(Path(t["full_path"])),
            }
        )

    combined_lines = []
    for t, reduced in reduced_paths:
        combined_lines.append(f"= {t['name']}\n")
        combined_lines.append(reduced.read_text(encoding="utf-8", errors="replace"))
        combined_lines.append("\n\n")

    combined_path = OUTPUT / f"{BOOK_DIR}-combined.adoc"
    combined_path.write_text("".join(combined_lines), encoding="utf-8")
    line_count = combined_path.read_text(encoding="utf-8").count("\n") + 1
    print(f"Combined: {combined_path} ({line_count} lines)")

    (OUTPUT / f"{BOOK_DIR}-include-graph.json").write_text(
        json.dumps(include_graph, indent=2), encoding="utf-8"
    )

    topicmap_out = {
        "name": book.get("Name"),
        "dir": BOOK_DIR,
        "distros": book.get("Distros"),
        "distro_filter": DISTRO,
        "topics": [
            {"name": t["name"], "file": t["file"], "rel_path": t["rel_path"]}
            for t, _ in reduced_paths
        ],
    }
    (OUTPUT / f"{BOOK_DIR}-topicmap.json").write_text(
        json.dumps(topicmap_out, indent=2), encoding="utf-8"
    )

    # Verify no includes left
    for _, reduced in reduced_paths:
        content = reduced.read_text(encoding="utf-8")
        bad = [
            ln
            for ln in content.splitlines()
            if ln.strip().startswith("include::")
        ]
        if bad:
            print(f"WARN includes remain in {reduced.name}: {len(bad)}", file=sys.stderr)

    print("DONE", OUTPUT)


if __name__ == "__main__":
    main()
