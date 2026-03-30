"""Validate localization-sensitive files in the repository."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LINK_VALIDATION_PATHS = [
    Path("README.md"),
    Path("UPSTREAM.md"),
    Path("LOCALIZATION-STYLE.md"),
    Path("LEARNING-ROADMAP.md"),
    Path("QUICK_REFERENCE.md"),
    Path("CATALOG.md"),
    Path("CHANGELOG.md"),
    Path("02-memory/README.md"),
    Path("03-skills/README.md"),
    Path("05-mcp/README.md"),
    Path("06-hooks/README.md"),
    Path("07-plugins/README.md"),
    Path("08-checkpoints/README.md"),
    Path("09-advanced-features/README.md"),
    Path("10-cli/README.md"),
    Path("scripts/README.md"),
    Path("01-slash-commands"),
    Path("03-skills/code-review/SKILL.md"),
    Path("04-subagents"),
]

PROTECTED_SNIPPETS = {
    Path("README.md"): [
        "## Table of Contents",
        "## Contributing",
        "## License",
        "UPSTREAM.md",
        "LOCALIZATION-STYLE.md",
    ],
    Path("01-slash-commands/pr.md"): [
        "allowed-tools:",
        "Bash(git add:*)",
        "Bash(git status:*)",
        "Bash(git diff:*)",
    ],
    Path("03-skills/code-review/SKILL.md"): [
        "name: code-review-specialist",
        "## Review Template",
    ],
    Path("04-subagents/code-reviewer.md"): [
        "name: code-reviewer",
        "tools: Read, Grep, Glob, Bash",
        "model: inherit",
    ],
    Path("05-mcp/github-mcp.json"): [
        '"mcpServers"',
        '"github"',
        '"GITHUB_TOKEN"',
    ],
    Path("07-plugins/pr-review/.claude-plugin/plugin.json"): [
        '"name": "pr-review"',
        '"version"',
        '"license": "MIT"',
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_link_validation_files(root: Path) -> list[Path]:
    files: set[Path] = set()
    for relative_path in LINK_VALIDATION_PATHS:
        path = root / relative_path
        if not path.exists():
            continue
        if path.is_file():
            files.add(path)
            continue
        files.update(child for child in path.rglob("*.md") if child.is_file())
    return sorted(files)


def validate_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_link_validation_files(root):
        content = read_text(path)
        for raw_target in MARKDOWN_LINK_RE.findall(content):
            target = raw_target.strip()
            if not target or target.startswith("#"):
                continue
            if "://" in target or target.startswith(("mailto:", "javascript:")):
                continue
            target_path = target.split("#", 1)[0]
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(f"{path}: broken relative link '{target}'")
    return errors


def split_frontmatter(content: str) -> str | None:
    if not content.startswith("---\n"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def validate_frontmatter(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.md"):
        if ".venv" in path.parts or "node_modules" in path.parts:
            continue
        frontmatter = split_frontmatter(read_text(path))
        if frontmatter is None:
            continue
        try:
            loaded = yaml.safe_load(frontmatter)
        except yaml.YAMLError as exc:
            errors.append(f"{path}: invalid YAML frontmatter - {exc}")
            continue
        if loaded is not None and not isinstance(loaded, dict):
            errors.append(f"{path}: YAML frontmatter must parse to a mapping")
    return errors


def validate_data_files(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.json"):
        if ".venv" in path.parts or "node_modules" in path.parts:
            continue
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON - {exc}")
    for suffix in ("*.yml", "*.yaml"):
        for path in root.rglob(suffix):
            if ".venv" in path.parts or "node_modules" in path.parts:
                continue
            try:
                yaml.safe_load(read_text(path))
            except yaml.YAMLError as exc:
                errors.append(f"{path}: invalid YAML - {exc}")
    return errors


def validate_shell_scripts(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.sh"):
        if ".venv" in path.parts or "node_modules" in path.parts:
            continue
        result = subprocess.run(
            ["bash", "-n", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            details = result.stderr.strip() or "bash -n failed"
            errors.append(f"{path}: invalid shell syntax - {details}")
    return errors


def validate_protected_snippets(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path, snippets in PROTECTED_SNIPPETS.items():
        path = root / relative_path
        if not path.exists():
            errors.append(f"{relative_path}: required file is missing")
            continue
        content = read_text(path)
        errors.extend(
            f"{relative_path}: missing protected snippet '{snippet}'"
            for snippet in snippets
            if snippet not in content
        )
    return errors


def validate_root(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_markdown_links(root))
    errors.extend(validate_frontmatter(root))
    errors.extend(validate_data_files(root))
    errors.extend(validate_shell_scripts(root))
    errors.extend(validate_protected_snippets(root))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate localization-sensitive content in the repository."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root to validate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = validate_root(root)
    if errors:
        print("Localization validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Localization validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
