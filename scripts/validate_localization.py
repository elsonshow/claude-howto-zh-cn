#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# ///
"""Validate localization-sensitive files in the repository."""

from __future__ import annotations

import argparse
import json
import re
import subprocess  # nosec B404
import sys
from pathlib import Path

import yaml

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
ENGLISH_WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z']{2,}\b")

MARKDOWN_IGNORE_PARTS = {
    ".git",
    ".pytest_cache",
    ".venv",
    "node_modules",
    "zh",
    "vi",
    "uk",
}

ALLOWED_ENGLISH_HEADING_RE = [
    re.compile(pattern)
    for pattern in [
        r"^#{1,6}\s+CLAUDE\.md$",
        r"^#{1,6}\s+v\d+\.\d+\.\d+\b.*$",
        r"^#{1,6}\s+CI/CD$",
        r"^#{1,6}\s+`[^`]+`$",
        r"^#{1,6}\s+/[A-Za-z0-9_-]+$",
    ]
]

ALLOWED_ENGLISH_HEADINGS_BY_PATH = {
    Path("README.md"): {
        "## Table of Contents",
        "## Contributing",
        "## License",
    }
}

FORBIDDEN_UNTRANSLATED_SNIPPETS = [
    "## Table of Contents",
    "## Contributing",
    "## License",
    "# Security Policy",
    "# Testing Guide",
    "# Publishing Notes",
    "## Review Template",
    "## Project Information",
    "## Executive Summary",
    "## Pre-Refactoring Checklist",
    "## Identified Code Smells",
    "## Refactoring Phases",
    "| Area | Status |",
    "| Feature Area | Score | Mastery | Status |",
    "This is a TypeScript web application.",
    "Run tests before commit.",
    "Keep API changes documented.",
]
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
    Path("03-skills/code-review-specialist/SKILL.md"),
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
    Path("03-skills/code-review-specialist/SKILL.md"): [
        "name: code-review-specialist",
        "## 审查模板",
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
        # Validate repo-local shell files with `bash -n`.
        result = subprocess.run(  # nosec B603 B607
            ["bash", "-n", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            details = result.stderr.strip() or "bash -n failed"
            errors.append(f"{path}: invalid shell syntax - {details}")
    return errors


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in MARKDOWN_IGNORE_PARTS for part in path.parts)
    )


def is_allowed_english_heading(line: str) -> bool:
    return any(pattern.match(line) for pattern in ALLOWED_ENGLISH_HEADING_RE)


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "", line)


def looks_like_command_or_path(line: str) -> bool:
    stripped = line.strip()
    if stripped.startswith(("[![", "<", "|", "$", "# /", "# -", "- `", "* `")):
        return True
    command_prefixes = (
        "git ",
        "npm ",
        "npx ",
        "uv ",
        "python ",
        "python3 ",
        "bash ",
        "claude ",
        "curl ",
        "docker ",
        "kubectl ",
        "bq ",
        "cp ",
        "mkdir ",
    )
    return stripped.startswith(command_prefixes)


def validate_untranslated_english(root: Path) -> list[str]:
    errors: list[str] = []

    for path in iter_markdown_files(root):
        relative_path = path.relative_to(root)
        allowed_headings = ALLOWED_ENGLISH_HEADINGS_BY_PATH.get(relative_path, set())
        content = read_text(path)
        errors.extend(
            f"{path}: untranslated protected text '{snippet}'"
            for snippet in FORBIDDEN_UNTRANSLATED_SNIPPETS
            if snippet in content and snippet not in allowed_headings
        )

        in_fence = False
        in_frontmatter = False
        first_line = True
        for line_number, raw_line in enumerate(content.splitlines(), 1):
            line = raw_line.strip()
            if first_line and line == "---":
                in_frontmatter = True
                first_line = False
                continue
            first_line = False
            if in_frontmatter:
                if line == "---":
                    in_frontmatter = False
                continue
            if line.startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if in_fence or not line or looks_like_command_or_path(line):
                continue

            if line.startswith("#") and not CJK_RE.search(line):
                if line in allowed_headings:
                    continue
                if ENGLISH_WORD_RE.search(line) and not is_allowed_english_heading(
                    line
                ):
                    errors.append(
                        f"{path}:{line_number}: untranslated heading '{line}'"
                    )
                continue

            text = strip_inline_code(line)
            if CJK_RE.search(text):
                continue
            if len(ENGLISH_WORD_RE.findall(text)) >= 9:
                errors.append(
                    f"{path}:{line_number}: likely untranslated text '{line}'"
                )

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


LESSON_DIRS = {
    f"{number:02d}": directory
    for number, directory in enumerate(
        (
            "01-slash-commands",
            "02-memory",
            "03-skills",
            "04-subagents",
            "05-mcp",
            "06-hooks",
            "07-plugins",
            "08-checkpoints",
            "09-advanced-features",
            "10-cli",
        ),
        1,
    )
}

V2_1_206_REQUIRED_SNIPPETS = {
    Path("01-slash-commands/README.md"): ["/dataviz", "${CLAUDE_PROJECT_DIR}"],
    Path("03-skills/README.md"): [
        "/dataviz",
        "${CLAUDE_PROJECT_DIR}",
        "叠加多个 skills",
        '"legacy-context": "name-only"',
        '"deploy": "off"',
    ],
    Path("04-subagents/README.md"): [
        "v2.1.198",
        "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS",
        "--append-subagent-system-prompt",
    ],
    Path("05-mcp/README.md"): [
        "roots/list",
        "Pending approval",
        "enableAllProjectMcpServers",
    ],
    Path("06-hooks/README.md"): [
        "agent_needs_input",
        "agent_completed",
        "prompt_id",
    ],
    Path("07-plugins/README.md"): [
        "renames",
        "displayName",
        "defaultEnabled",
        "first-party-plugins",
        "healthcare",
    ],
    Path("08-checkpoints/README.md"): ["Summarize up to here"],
    Path("09-advanced-features/README.md"): [
        "`manual`",
        "askUserQuestionTimeout",
        "enableArtifact",
    ],
    Path("10-cli/README.md"): [
        "Org default",
        "--append-subagent-system-prompt",
        "CLAUDE_ENABLE_STREAM_WATCHDOG",
        "claude-sonnet-5",
    ],
}

V2_1_212_REQUIRED_SNIPPETS = {
    Path("README.md"): ["v2.1.212", "a645ffe", "8f04517"],
    Path("UPSTREAM.md"): [
        "8f045173d1b1e876d101eb9a94972585f57c4ed1",
        "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS",
    ],
    Path("INDEX.md"): ["v2.1.212", "/fork <directive>", "/branch [name]"],
    Path("claude_concepts_guide.md"): [
        "v2.1.212",
        "4 hops",
        "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS",
    ],
    Path("resources.md"): [
        "claude auto-mode reset",
        "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION",
        "--ax-screen-reader",
    ],
    Path("CATALOG.md"): [
        "2 套机制",
        "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION",
        "--ax-screen-reader",
    ],
    Path("QUICK_REFERENCE.md"): [
        "claude auto-mode reset",
        "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION",
        "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS",
    ],
    Path("01-slash-commands/README.md"): [
        "/fork <directive>",
        "/branch [name]",
        "v2.1.212",
    ],
    Path("02-memory/README.md"): [
        "4 hops",
        "拼接",
        "managed-settings.d/",
        "命令行参数",
    ],
    Path("04-subagents/README.md"): [
        "v2.1.210",
        "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION",
        "xhigh",
        "Task tool",
        "`mode`",
    ],
    Path("05-mcp/README.md"): ["CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS"],
    Path("09-advanced-features/README.md"): [
        "claude auto-mode reset",
        "--ax-screen-reader",
        "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION",
        "disableAutoMode",
    ],
    Path("10-cli/README.md"): [
        "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION",
        "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION",
        "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS",
        "CLAUDE_AX_SCREEN_READER",
    ],
}

V2_1_212_FORBIDDEN_SNIPPETS = {
    Path("02-memory/README.md"): ["当前教程按 8 层理解"],
    Path("09-advanced-features/README.md"): [
        "需要显式设置 `CLAUDE_CODE_ENABLE_AUTO_MODE=1`",
        "较新的主名称",
    ],
    Path("10-cli/README.md"): [
        "需要显式设置 `CLAUDE_CODE_ENABLE_AUTO_MODE=1`",
        "较新的主名称",
    ],
    Path("QUICK_REFERENCE.md"): ["某些版本中 `/fork` 仍可作为兼容别名"],
    Path("resources.md"): [
        "在 Bedrock / Vertex / Foundry 上对 Opus 4.7 / 4.8 显式启用"
    ],
    Path("CATALOG.md"): ["从当前对话分叉\uff08某些版本中 `/fork` 仍可能可用\uff09"],
}


def normalize_heading(value: str) -> str:
    return re.sub(r"[`*_]", "", value).strip().casefold()


def validate_curriculum_consistency(root: Path) -> list[str]:  # noqa: PLR0912
    """Check cross-document facts that syntax and link checks cannot catch."""

    errors: list[str] = []
    required_paths = [
        Path(".claude/skills/lesson-quiz/SKILL.md"),
        Path(".claude/skills/lesson-quiz/references/question-bank.md"),
        Path(".claude/skills/lesson-quiz/references/results-template.md"),
        Path(".claude/skills/self-assessment/SKILL.md"),
        Path(".claude/skills/self-assessment/references/deep-assessment-rounds.md"),
        Path(".claude/skills/self-assessment/references/output-templates.md"),
        Path(".claude/skills/self-assessment/references/topic-recommendations.md"),
        Path("06-hooks/README.md"),
    ]
    missing = [path for path in required_paths if not (root / path).is_file()]
    if missing:
        return [f"{path}: required curriculum file is missing" for path in missing]

    lesson_skill_path = root / required_paths[0]
    question_bank_path = root / required_paths[1]
    results_template_path = root / required_paths[2]
    assessment_skill_path = root / required_paths[3]
    deep_rounds_path = root / required_paths[4]
    assessment_template_path = root / required_paths[5]
    topic_recommendations_path = root / required_paths[6]
    hooks_path = root / required_paths[7]

    lesson_skill = read_text(lesson_skill_path)
    question_bank = read_text(question_bank_path)
    results_template = read_text(results_template_path)
    assessment_skill = read_text(assessment_skill_path)
    deep_rounds = read_text(deep_rounds_path)
    assessment_template = read_text(assessment_template_path)
    topic_recommendations = read_text(topic_recommendations_path)
    hooks = read_text(hooks_path)

    if (
        "每轮 2 题，共 5 轮" not in lesson_skill  # noqa: RUF001
        or "所有 4 轮" in lesson_skill
    ):
        errors.append(
            f"{lesson_skill_path}: lesson quiz must consistently use 5 rounds"
        )

    frontmatter = split_frontmatter(lesson_skill)
    loaded = yaml.safe_load(frontmatter) if frontmatter else {}
    metadata = loaded.get("metadata", {}) if isinstance(loaded, dict) else {}
    if not isinstance(metadata, dict) or metadata.get("version") != "1.1.0":
        errors.append(
            f"{lesson_skill_path}: version 1.1.0 must be stored as metadata.version"
        )
    if isinstance(loaded, dict) and "version" in loaded:
        errors.append(f"{lesson_skill_path}: top-level version key is stale")
    raw_description = loaded.get("description", "") if isinstance(loaded, dict) else ""
    description = raw_description if isinstance(raw_description, str) else ""
    if "整套教程" not in description or "解释" not in description:
        errors.append(
            f"{lesson_skill_path}: description must include negative trigger boundaries"
        )

    lesson_questions: dict[str, list[dict[str, str]]] = {}
    current_lesson = ""
    current_question: dict[str, str] | None = None
    for line in question_bank.splitlines():
        lesson_match = re.match(r"^## Lesson (\d{2})", line)
        if lesson_match:
            current_lesson = lesson_match.group(1)
            lesson_questions[current_lesson] = []
            current_question = None
            continue
        question_match = re.match(r"^### Q(\d+)$", line)
        if question_match and current_lesson:
            current_question = {"number": question_match.group(1)}
            lesson_questions[current_lesson].append(current_question)
            continue
        if current_question is None:
            continue
        field_match = re.match(r"^- \*\*(Category|Correct|Review)\*\*: (.+)$", line)
        if field_match:
            current_question[field_match.group(1).lower()] = field_match.group(2)
        if line.startswith("- **Options**: "):
            current_question["options"] = line.removeprefix("- **Options**: ")
        if line.startswith("- **Explanation**: "):
            current_question["explanation"] = line.removeprefix("- **Explanation**: ")

    for lesson_number, lesson_dir in LESSON_DIRS.items():
        questions = lesson_questions.get(lesson_number, [])
        if [item.get("number") for item in questions] != [str(i) for i in range(1, 11)]:
            errors.append(
                f"{question_bank_path}: lesson {lesson_number} must contain Q1-Q10"
            )
            continue
        categories = [item.get("category") for item in questions]
        if categories.count("conceptual") != 5 or categories.count("practical") != 5:
            errors.append(
                f"{question_bank_path}: lesson {lesson_number} must have 5 conceptual and 5 practical questions"
            )

        lesson_readme = root / lesson_dir / "README.md"
        if not lesson_readme.is_file():
            errors.append(f"{lesson_readme}: required lesson README is missing")
            continue
        headings = {
            normalize_heading(match.group(1))
            for line in read_text(lesson_readme).splitlines()
            if (match := re.match(r"^#{2,6}\s+(.+)$", line))
        }
        for question in questions[8:10]:
            review = question.get("review", "")
            if normalize_heading(review) not in headings:
                errors.append(
                    f"{question_bank_path}: lesson {lesson_number} Q{question.get('number')} review pointer '{review}' does not match a localized heading"
                )

    hook_summary = re.search(r"\*\*(\d+) 个 hook 事件、(\d+) 种 hook 类型\*\*", hooks)
    if not hook_summary:
        errors.append(f"{hooks_path}: missing hook event/type summary")
    else:
        event_count, type_count = map(int, hook_summary.groups())
        hook_questions = lesson_questions.get("06", [])
        if len(hook_questions) < 9:
            errors.append(f"{question_bank_path}: Hooks Q9 is missing")
            hook_q9: dict[str, str] = {}
        else:
            hook_q9 = hook_questions[8]
        option_values = {
            letter: int(value)
            for letter, value in re.findall(
                r"([A-D])\)\s*(\d+)", hook_q9.get("options", "")
            )
        }
        correct = hook_q9.get("correct", "")
        if option_values.get(correct) != event_count:
            errors.append(
                f"{question_bank_path}: Hooks Q9 correct answer must match {event_count} events"
            )
        if f"{event_count} 个 hook 事件" not in hook_q9.get("explanation", ""):
            errors.append(
                f"{question_bank_path}: Hooks Q9 explanation must use {event_count} events"
            )
        if (
            f"{event_count} 个 hook 事件" not in topic_recommendations
            or f"{type_count} 种 hook 类型" not in topic_recommendations
        ):
            errors.append(
                f"{topic_recommendations_path}: hook recommendation must match {event_count} events and {type_count} types"
            )

    english_output_fragments = (
        "Lesson Quiz Results:",
        "Quiz timing",
        "Question breakdown",
        "Incorrect Answers — Review These",
        "Your answer:",
        "Correct answer:",
        "Pre-test score:",
        "Progress check:",
        "Mastery check:",
        "Recommended Next Steps",
        "Would you like to retake this quiz",
        "[next lesson link]",
        "[list sections]",
    )
    errors.extend(
        f"{results_template_path}: untranslated user-facing text '{fragment}'"
        for fragment in english_output_fragments
        if fragment in results_template
    )

    if "N/20" in assessment_skill or "N/20" in assessment_template:
        errors.append(f"{assessment_skill_path}: Deep Assessment maximum is 19, not 20")
    if "N/19" not in assessment_skill or "N/19" not in assessment_template:
        errors.append(
            f"{assessment_template_path}: Deep Assessment output must use N/19"
        )
    if "8 个问题" in assessment_skill:
        errors.append(
            f"{assessment_skill_path}: Quick Assessment has 8 items across 2 questions"
        )
    if (
        "每轮覆盖 2 个能力域，每个能力域对应 2 个选项"  # noqa: RUF001
        in deep_rounds
    ):
        errors.append(f"{deep_rounds_path}: round 4 uses a 1/3 option split, not 2/2")

    untranslated_assessment_fragments = (
        "Which of these have you done? Select all that apply.",
        "Created a custom slash command or skill",
        "Installed and used an auto-invoked skill",
        "Connected an MCP server and used its tools",
        "Used checkpoints for safe experimentation",
        "Installed or created a plugin",
        "- Tutorial:",
        "- Focus on:",
        "- Key exercise:",
        "- Done when:",
    )
    for path, content in (
        (deep_rounds_path, deep_rounds),
        (topic_recommendations_path, topic_recommendations),
    ):
        errors.extend(
            f"{path}: untranslated assessment text '{fragment}'"
            for fragment in untranslated_assessment_fragments
            if fragment in content
        )
    if "2% context budget" in topic_recommendations:
        errors.append(
            f"{topic_recommendations_path}: skill description budget must be 1%"
        )

    for version, required_snippets in (
        ("v2.1.206", V2_1_206_REQUIRED_SNIPPETS),
        ("v2.1.212", V2_1_212_REQUIRED_SNIPPETS),
    ):
        for relative_path, snippets in required_snippets.items():
            path = root / relative_path
            if not path.is_file():
                errors.append(
                    f"{relative_path}: required {version} document is missing"
                )
                continue
            content = read_text(path)
            errors.extend(
                f"{relative_path}: missing {version} content '{snippet}'"
                for snippet in snippets
                if snippet not in content
            )

    for relative_path, snippets in V2_1_212_FORBIDDEN_SNIPPETS.items():
        path = root / relative_path
        if not path.is_file():
            continue
        content = read_text(path)
        errors.extend(
            f"{relative_path}: stale v2.1.212 content '{snippet}'"
            for snippet in snippets
            if snippet in content
        )

    return errors


def validate_root(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_markdown_links(root))
    errors.extend(validate_frontmatter(root))
    errors.extend(validate_data_files(root))
    errors.extend(validate_shell_scripts(root))
    errors.extend(validate_untranslated_english(root))
    errors.extend(validate_protected_snippets(root))
    errors.extend(validate_curriculum_consistency(root))
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
