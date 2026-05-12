#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT.parent / "wiki"
CONTENT = ROOT / "content"

PUBLIC_DIRS = ["entities", "concepts", "summaries", "comparisons", "queries"]
SKIP_EMPTY_DIRS = {"comparisons", "queries"}


def clean_content() -> None:
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True, exist_ok=True)


def copy_tree(name: str) -> None:
    src = VAULT / name
    if not src.exists():
        return
    md_files = list(src.rglob("*.md"))
    if name in SKIP_EMPTY_DIRS and not md_files:
        return
    shutil.copytree(src, CONTENT / name, dirs_exist_ok=True)


def strip_leading_title(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def read_text(rel_path: str) -> str:
    return (VAULT / rel_path).read_text(encoding="utf-8")


def write_note(rel_path: str, content: str) -> None:
    path = CONTENT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_homepage() -> str:
    return """---
title: Equity Research Wiki
publish: true
tags: [public-equities, thesis]
---

## Overview
This public site is generated from an Obsidian-style research vault focused on public-equity themes, recurring company pages, and memo-derived investment frameworks.

## Start here
- [[catalog]] — full note catalog across entities, concepts, and summaries
- [[about-this-wiki]] — scope, schema, and note conventions
- [[change-log]] — append-only changelog of wiki evolution

## Main sections
- [[entities/nvidia]]
- [[concepts/agentic-utilities]]
- [[concepts/photonics-cpo-supply-chain]]
- [[summaries/26-trades-for-2026]]

## Publishing policy
- Public site includes curated knowledge pages and generated index material.
- Raw source archives under `raw/` stay local and are not published here.
"""


def main() -> None:
    clean_content()

    for folder in PUBLIC_DIRS:
        copy_tree(folder)

    index_body = strip_leading_title(read_text("index.md"))
    schema_body = strip_leading_title(read_text("SCHEMA.md"))
    log_body = strip_leading_title(read_text("log.md"))

    write_note("index.md", build_homepage())
    write_note(
        "catalog.md",
        f"---\ntitle: Catalog\npublish: true\n---\n\n# Catalog\n\n{index_body}",
    )
    write_note(
        "about-this-wiki.md",
        f"---\ntitle: About This Wiki\npublish: true\n---\n\n# About This Wiki\n\n{schema_body}",
    )
    write_note(
        "change-log.md",
        f"---\ntitle: Change Log\npublish: true\n---\n\n# Change Log\n\n{log_body}",
    )

    assets_src = VAULT / "raw" / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, CONTENT / "assets", dirs_exist_ok=True)

    print(f"Synced vault from {VAULT} to {CONTENT}")


if __name__ == "__main__":
    main()
