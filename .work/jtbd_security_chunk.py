#!/usr/bin/env python3
"""Split security-combined.adoc into chunks at assembly boundaries only."""

import json
import re
from pathlib import Path

OUTPUT = Path("/home/ahoffer/git/openshift-docs/analysis/openshift-enterprise/security")
COMBINED = OUTPUT / "security-combined.adoc"
TOPICMAP = OUTPUT / "security-topicmap.json"
CHUNKS_DIR = OUTPUT / "chunks"
CHUNK_SIZE = 4


def main():
    topicmap = json.loads(TOPICMAP.read_text(encoding="utf-8"))
    topic_names = [t["name"] for t in topicmap["topics"]]
    text = COMBINED.read_text(encoding="utf-8")

    # Split only on assembly boundary headings from topic map
    pattern = "|".join(re.escape(f"= {name}\n") for name in topic_names)
    # Build sections in topic map order
    assemblies = []
    pos = 0
    for name in topic_names:
        marker = f"= {name}\n"
        idx = text.find(marker, pos)
        if idx == -1:
            print(f"WARN: marker not found: {name[:60]}")
            continue
        if assemblies:
            assemblies[-1]["content"] = text[pos:idx]
        assemblies.append({"name": name, "start": idx, "content": ""})
        pos = idx
    if assemblies:
        assemblies[-1]["content"] = text[pos:]

    print(f"Split into {len(assemblies)} assemblies")

    CHUNKS_DIR.mkdir(exist_ok=True)
    # Clear old chunks
    for old in CHUNKS_DIR.glob("chunk-*.adoc"):
        old.unlink()

    chunks_meta = []
    for i in range(0, len(assemblies), CHUNK_SIZE):
        batch = assemblies[i : i + CHUNK_SIZE]
        chunk_num = i // CHUNK_SIZE + 1
        content = "\n\n".join(a["content"] for a in batch)
        path = CHUNKS_DIR / f"chunk-{chunk_num:03d}.adoc"
        path.write_text(content, encoding="utf-8")
        titles = [a["name"] for a in batch]
        chunks_meta.append(
            {
                "num": chunk_num,
                "path": str(path),
                "titles": titles,
                "lines": content.count("\n"),
            }
        )
        print(
            f"  chunk-{chunk_num:03d}: {len(titles)} assemblies, "
            f"{chunks_meta[-1]['lines']} lines"
        )

    (OUTPUT / "chunk-manifest.json").write_text(
        json.dumps(chunks_meta, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(chunks_meta)} chunks")


if __name__ == "__main__":
    main()
