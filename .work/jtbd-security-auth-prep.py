#!/usr/bin/env python3
"""Prepare combined reduced content for security + authentication JTBD analysis."""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path("/home/ahoffer/git/openshift-docs")
TOPIC_MAP = REPO / "_topic_maps/_topic_map.yml"
OUTPUT = REPO / "analysis/topicmap/security-auth"
BOOK_DIRS = ("security", "authentication")
COMBINED_NAME = "security-auth"


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


def walk_topics(topics, book_dir, sub_dirs=None):
    sub_dirs = sub_dirs or []
    assemblies = []
    for t in topics or []:
        if "Topics" in t:
            new_sub = list(sub_dirs)
            if "Dir" in t:
                new_sub.append(t["Dir"])
            assemblies.extend(walk_topics(t["Topics"], book_dir, new_sub))
        elif "File" in t:
            rel = Path(*sub_dirs) / f"{t['File']}.adoc" if sub_dirs else Path(f"{t['File']}.adoc")
            assemblies.append(
                {
                    "name": t.get("Name", ""),
                    "rel_path": str(rel),
                    "book_dir": book_dir,
                    "book_name": None,
                }
            )
    return assemblies


def parse_include_graph(assembly_path: Path, rel_path: str, topic_name: str, book_dir: str):
    text = assembly_path.read_text(encoding="utf-8", errors="replace")
    includes = []
    for m in re.finditer(
        r"include::([^\[]+)\[(?:[^\]]*,)?\s*leveloffset\s*=\s*([^\],]+)",
        text,
    ):
        mod = m.group(1).strip()
        includes.append(
            {
                "module": mod,
                "type": module_type(mod),
                "leveloffset": m.group(2).strip(),
            }
        )
    for m in re.finditer(r"include::([^\[]+)\[\]", text):
        mod = m.group(1).strip()
        if not any(i["module"] == mod for i in includes):
            includes.append({"module": mod, "type": module_type(mod), "leveloffset": ""})
    return {
        "file": assembly_path.name,
        "rel_path": rel_path,
        "topic_name": topic_name,
        "book_dir": book_dir,
        "includes": includes,
    }


def reduce_assembly(book_dir: str, rel_path: str, out_path: Path) -> bool:
    src = REPO / book_dir / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cwd = REPO / book_dir
    cmd = [
        "asciidoctor-reducer",
        rel_path,
        "-o",
        str(out_path),
    ]
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL {rel_path}: {r.stderr[:200]}", file=sys.stderr)
        return False
    content = out_path.read_text(encoding="utf-8", errors="replace")
    if re.search(r"^include::", content, re.MULTILINE):
        print(f"WARN includes remain in {out_path.name}", file=sys.stderr)
    return True


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    all_assemblies = []
    books_meta = []

    with open(TOPIC_MAP) as f:
        for doc in yaml.safe_load_all(f):
            if not doc or doc.get("Dir") not in BOOK_DIRS:
                continue
            book_dir = doc["Dir"]
            book_name = doc["Name"]
            assemblies = walk_topics(doc.get("Topics", []), book_dir)
            for a in assemblies:
                a["book_name"] = book_name
            all_assemblies.extend(assemblies)
            books_meta.append(
                {
                    "name": book_name,
                    "dir": book_dir,
                    "distros": doc.get("Distros", ""),
                    "topic_count": len(assemblies),
                }
            )

    print(f"Reducing {len(all_assemblies)} assemblies...")
    failed = []
    graph_assemblies = []
    for i, a in enumerate(all_assemblies, 1):
        stem = Path(a["rel_path"]).stem
        out_name = f"{a['book_dir']}--{stem}-reduced.adoc"
        out_path = OUTPUT / out_name
        src = REPO / a["book_dir"] / a["rel_path"]
        if not src.exists():
            failed.append(a["rel_path"])
            continue
        if (i % 20) == 0:
            print(f"  {i}/{len(all_assemblies)}")
        if not reduce_assembly(a["book_dir"], a["rel_path"], out_path):
            failed.append(a["rel_path"])
            continue
        graph_assemblies.append(
            parse_include_graph(src, a["rel_path"], a["name"], a["book_dir"])
        )

    combined_path = OUTPUT / f"{COMBINED_NAME}-combined.adoc"
    lines = []
    for a in all_assemblies:
        stem = Path(a["rel_path"]).stem
        reduced = OUTPUT / f"{a['book_dir']}--{stem}-reduced.adoc"
        if not reduced.exists():
            continue
        lines.append(f"= {a['name']}")
        lines.append(f"// source: {a['book_dir']}/{a['rel_path']}")
        lines.append(reduced.read_text(encoding="utf-8", errors="replace").strip())
        lines.append("")
    combined_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    line_count = len(lines)

    include_graph = {
        "books": books_meta,
        "combined_doc": f"{COMBINED_NAME}-combined.adoc",
        "assemblies": graph_assemblies,
    }
    (OUTPUT / f"{COMBINED_NAME}-include-graph.json").write_text(
        json.dumps(include_graph, indent=2), encoding="utf-8"
    )

    topicmap = {
        "name": "Security and compliance + Authentication and authorization",
        "dirs": list(BOOK_DIRS),
        "books": books_meta,
        "topics": [
            {"name": a["name"], "file": Path(a["rel_path"]).stem, "book_dir": a["book_dir"]}
            for a in all_assemblies
        ],
    }
    (OUTPUT / f"{COMBINED_NAME}-topicmap.json").write_text(
        json.dumps(topicmap, indent=2), encoding="utf-8"
    )

    print(f"Combined: {combined_path} ({combined_path.stat().st_size} bytes)")
    print(f"Assemblies reduced: {len(graph_assemblies)}, failed: {len(failed)}")
    if failed:
        print("Failed:", failed[:10])


if __name__ == "__main__":
    main()
