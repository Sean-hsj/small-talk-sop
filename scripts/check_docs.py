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
    "assets/illustrations/README.md",
    "docs/cross-cultural-guide.md",
    "docs/review-loop.md",
    "docs/review-report-v1.0.md",
    "docs/review-report-v1.1.md",
    "docs/review-report-v1.2.md",
    "docs/review-report-v1.3.md",
    "docs/review-report-v1.4.md",
    "docs/en/sop.md",
    "docs/en/role-scenario-matrix.md",
    "docs/en/manager-style-addon.md",
    "docs/en/quick-reference.md",
    "docs/en/scenarios.md",
    "docs/zh-CN/sop.md",
    "docs/zh-CN/role-scenario-matrix.md",
    "docs/zh-CN/manager-style-addon.md",
    "docs/zh-CN/quick-reference.md",
    "docs/zh-CN/scenarios.md",
]
REQUIRED_ASSETS = [
    "assets/illustrations/coffee-hello.png",
    "assets/illustrations/lunch-easy-exit.png",
    "assets/illustrations/manager-calibration.png",
]
MAX_ASSET_BYTES = 1_200_000
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MARKDOWN_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r'<a\b[^>]*\bhref="([^"]+)"[^>]*>', re.IGNORECASE)
HTML_IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
HTML_SRC_RE = re.compile(r'\bsrc="([^"]+)"', re.IGNORECASE)
HTML_ALT_RE = re.compile(r'\balt="([^"]*)"', re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
SCENARIO_RE = re.compile(r"^## (\d+)\.\s+", re.MULTILINE)


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

    for relative in REQUIRED_ASSETS:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required asset: {relative}")
            continue
        if path.stat().st_size > MAX_ASSET_BYTES:
            errors.append(f"{relative}: asset exceeds {MAX_ASSET_BYTES} bytes")
        if path.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"{relative}: required asset is not a valid PNG")

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
        for alt, target in MARKDOWN_IMG_RE.findall(text):
            if not alt.strip():
                errors.append(f"{path.relative_to(ROOT)}: Markdown image is missing alt text")
            issue = check_internal_link(path, target)
            if issue:
                errors.append(issue)
        for target in HTML_LINK_RE.findall(text):
            if target.startswith("#"):
                continue
            issue = check_internal_link(path, target)
            if issue:
                errors.append(issue)
        for tag in HTML_IMG_RE.findall(text):
            alt_match = HTML_ALT_RE.search(tag)
            if not alt_match or not alt_match.group(1).strip():
                errors.append(f"{path.relative_to(ROOT)}: HTML image is missing alt text")
            src_match = HTML_SRC_RE.search(tag)
            if not src_match:
                errors.append(f"{path.relative_to(ROOT)}: HTML image is missing src")
                continue
            target = src_match.group(1)
            if target.startswith(("http://", "https://")):
                continue
            issue = check_internal_link(path, target)
            if issue:
                errors.append(issue)

    required_phrases = {
        "README.md": ["English track", "中文入口", "English exercise", "中文小练习", "Version 1.4.0", "<details>"],
        "assets/illustrations/README.md": ["pure white", "Prompt set", "1.2 MB"],
        "docs/en/sop.md": ["Scan", "Ask lightly", "Exit cleanly", "Manager add-on"],
        "docs/zh-CN/sop.md": ["看场", "开口", "接球", "收尾", "管理者沟通偏好附加章"],
        "docs/review-loop.md": ["90/100", "Critical safety gates"],
        "docs/review-report-v1.0.md": ["97/100", "8/8", "44/44", "Final decision"],
        "docs/review-report-v1.1.md": ["97/100", "Role coverage", "16/16", "Final decision"],
        "docs/review-report-v1.2.md": ["97", "14/14", "10/10", "Final decision"],
        "docs/review-report-v1.3.md": ["97", "14/14", "GitHub rendering", "Final decision"],
        "docs/review-report-v1.4.md": ["97", "12/12", "translationese", "Final decision"],
        "docs/en/role-scenario-matrix.md": ["Manager +1 or +2", "Gender and identity", "Meal size and purpose"],
        "docs/zh-CN/role-scenario-matrix.md": ["加一或加二", "性别：不按男女分话题", "聚餐人数与性质"],
        "docs/en/manager-style-addon.md": ["OHAIR", "Unsafe behavior is not a style", "Add-on release gates"],
        "docs/zh-CN/manager-style-addon.md": ["观—猜—问—试—校", "不安全行为不是性格", "附加章发布闸门"],
        "SOURCES.md": ["2026-08-18", "legal advice", "Personality and Leadership", "psychometric instrument"],
    }
    for relative, phrases in required_phrases.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: missing required phrase: {phrase}")

    for relative in ["docs/en/scenarios.md", "docs/zh-CN/scenarios.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        numbers = [int(value) for value in SCENARIO_RE.findall(text)]
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(f"{relative}: scenario numbers are not sequential")

    refined_files = [
        "README.md",
        "docs/en/role-scenario-matrix.md",
        "docs/zh-CN/role-scenario-matrix.md",
        "docs/review-report-v1.1.md",
        "docs/en/manager-style-addon.md",
        "docs/zh-CN/manager-style-addon.md",
        "docs/review-report-v1.2.md",
        "docs/review-report-v1.3.md",
        "docs/review-report-v1.4.md",
    ]
    for relative in refined_files:
        for line_number, line in enumerate(
            (ROOT / relative).read_text(encoding="utf-8").splitlines(), start=1
        ):
            if len(line) > 240:
                errors.append(
                    f"{relative}:{line_number}: refined paragraph exceeds 240 characters"
                )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    stale_homepage_phrases = [
        "寒暄不是表演，也不是套隐私",
        "它只传递一个简短信号",
        "自愿才算自愿",
        "中性默认",
        "社交带宽",
        "重新校准",
    ]
    for phrase in stale_homepage_phrases:
        if phrase in readme:
            errors.append(f"README.md: stale translationese phrase: {phrase}")
    if readme.count("<details>") != 4 or readme.count("<summary>") != 4:
        errors.append("README.md: expected four complete interactive examples")
    for heading in HEADING_RE.findall(readme):
        if " / " in heading:
            errors.append(f"README.md: bilingual heading still paired inline: {heading}")

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
