#!/usr/bin/env python3
"""Dependency-free structural checks for the Small Talk SOP."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "SOURCES.md",
    "docs/cross-cultural-guide.md",
    "docs/review-loop.md",
    "docs/review-report-v1.0.md",
    "docs/en/sop.md",
    "docs/en/quick-reference.md",
    "docs/en/scenarios.md",
    "docs/zh-CN/sop.md",
    "docs/zh-CN/quick-reference.md",
    "docs/zh-CN/scenarios.md",
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)


def slugify(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[\*_~]", "", heading)
    heading = heading.strip().lower().replace(" ", "-")
    heading = re.sub(r"[^\w\-\u4e00-\u9fff]", "", heading)
    return re.sub(r"-+", "-", heading)


def check_internal_link(source: Path, raw_target: str) -> str | None:
    target = raw_target.strip().strip("<>")
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    if target.startswith("#"):
        destination = source
        anchor = target[1:]
    else:
        path_part, separator, anchor = target.partition("#")
        destination = (source.parent / unquote(path_part)).resolve()
        if not str(destination).startswith(str(ROOT.resolve())):
            return f"{source.relative_to(ROOT)}: link escapes repository: {target}"
        if not destination.exists():
            return f"{source.relative_to(ROOT)}: missing link target: {target}"
        if destination.is_dir():
            destination = destination / "README.md"
            if not destination.exists():
                return f"{source.relative_to(ROOT)}: directory has no README: {target}"
        if not separator:
            return None

    if anchor and destination.suffix.lower() == ".md":
        headings = {
            slugify(heading)
            for heading in HEADING_RE.findall(destination.read_text(encoding="utf-8"))
        }
        if unquote(anchor).lower() not in headings:
            return (
                f"{source.relative_to(ROOT)}: missing anchor "
                f"#{anchor} in {destination.relative_to(ROOT)}"
            )
    return None


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if PLACEHOLDER_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: unresolved placeholder")
        for target in LINK_RE.findall(text):
            issue = check_internal_link(path, target)
            if issue:
                errors.append(issue)

    required_phrases = {
        "README.md": ["English SOP", "中文版 SOP", "Version: 1.0.0"],
        "docs/en/sop.md": ["Scan", "Ask lightly", "Exit cleanly", "manager"],
        "docs/zh-CN/sop.md": ["看场", "开口", "接球", "收尾", "管理者"],
        "docs/review-loop.md": ["90/100", "Critical safety gates"],
        "docs/review-report-v1.0.md": ["97/100", "8/8", "44/44", "Final decision"],
        "SOURCES.md": ["2026-08-18", "legal advice"],
    }
    for relative, phrases in required_phrases.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: missing required phrase: {phrase}")

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Documentation checks passed: {len(markdown_files)} Markdown files, "
        f"{len(REQUIRED)} required files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
