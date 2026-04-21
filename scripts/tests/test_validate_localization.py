"""Tests for localization validation utilities."""

from __future__ import annotations

from pathlib import Path

from validate_localization import (
    validate_data_files,
    validate_frontmatter,
    validate_markdown_links,
    validate_protected_snippets,
    validate_shell_scripts,
)


def test_validate_markdown_links_detects_missing_file(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("[Broken](missing.md)\n", encoding="utf-8")

    errors = validate_markdown_links(tmp_path)

    assert len(errors) == 1
    assert "broken relative link" in errors[0]


def test_validate_frontmatter_accepts_valid_mapping(tmp_path: Path) -> None:
    skill = tmp_path / "skill.md"
    skill.write_text(
        "---\nname: sample\ndescription: demo\n---\n# Title\n",
        encoding="utf-8",
    )

    errors = validate_frontmatter(tmp_path)

    assert errors == []


def test_validate_data_files_detects_bad_json(tmp_path: Path) -> None:
    config = tmp_path / "broken.json"
    config.write_text("{bad json}\n", encoding="utf-8")

    errors = validate_data_files(tmp_path)

    assert len(errors) == 1
    assert "invalid JSON" in errors[0]


def test_validate_shell_scripts_detects_syntax_error(tmp_path: Path) -> None:
    script = tmp_path / "broken.sh"
    script.write_text("if then\n", encoding="utf-8")

    errors = validate_shell_scripts(tmp_path)

    assert len(errors) == 1
    assert "invalid shell syntax" in errors[0]


def test_validate_protected_snippets_detects_missing_tokens(tmp_path: Path) -> None:
    files = {
        "README.md": (
            "## Table of Contents\n"
            "## Contributing\n"
            "## License\n"
            "Language / Ngôn ngữ / 语言 / Мова\n"
            "[中文](zh/README.md)\n"
        ),
        "zh/README.md": ("## 目录\n## 许可证\n[English](../README.md)\n"),
        "01-slash-commands/pr.md": "allowed-tools:\nBash(git add:*)\n",
        "03-skills/code-review/SKILL.md": "name: code-review-specialist\n",
        "04-subagents/code-reviewer.md": "name: code-reviewer\n",
        "05-mcp/github-mcp.json": '{"mcpServers": {"github": {}}}\n',
        "07-plugins/pr-review/.claude-plugin/plugin.json": '{"name": "pr-review"}\n',
    }
    for relative_path, content in files.items():
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    errors = validate_protected_snippets(tmp_path)

    assert errors
    assert any("[中文](README.md)" in error for error in errors)
