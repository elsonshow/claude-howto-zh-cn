"""Tests for localization validation utilities."""

from __future__ import annotations

from pathlib import Path

from validate_localization import (
    validate_data_files,
    validate_frontmatter,
    validate_markdown_links,
    validate_protected_snippets,
    validate_shell_scripts,
    validate_untranslated_english,
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
            "UPSTREAM.md\n"
        ),
        "01-slash-commands/pr.md": "allowed-tools:\nBash(git add:*)\n",
        "03-skills/code-review/SKILL.md": "name: code-review-specialist\n## 审查模板\n",
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
    assert any("LOCALIZATION-STYLE.md" in error for error in errors)


def test_validate_untranslated_english_detects_english_heading(
    tmp_path: Path,
) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("# Security Policy\n\n中文说明。\n", encoding="utf-8")

    errors = validate_untranslated_english(tmp_path)

    assert errors
    assert any("Security Policy" in error for error in errors)


def test_validate_untranslated_english_allows_protected_terms(
    tmp_path: Path,
) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Claude Code 中文指南\n\n"
        "## MCP (外部工具协议)\n\n"
        "### `/optimize`\n\n"
        "`GITHUB_TOKEN` 和 `.mcp.json` 这些标识不要翻译。\n",
        encoding="utf-8",
    )

    errors = validate_untranslated_english(tmp_path)

    assert errors == []


def test_validate_untranslated_english_allows_required_root_readme_headings(
    tmp_path: Path,
) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        "## Table of Contents\n\n"
        "中文目录说明。\n\n"
        "## Contributing\n\n"
        "欢迎继续贡献。\n\n"
        "## License\n\n"
        "本项目使用 MIT License。\n",
        encoding="utf-8",
    )

    errors = validate_untranslated_english(tmp_path)

    assert errors == []
