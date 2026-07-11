# Deep Assessment 题目轮次

这里保存 Deep Assessment 的 5 轮题目。每轮使用一次 AskUserQuestion，多选，最多 4 个选项；每轮覆盖 2 个能力域，每个能力域对应 2 个选项。评分映射也保留在 `SKILL.md` 的 Step 2B，方便不重新读取本文件也能计算结果。

---

## 第 1 轮：Slash Commands 与 Memory

Header: `Commands`

Prompt: `Which of these have you done? Select all that apply.`

Options:

1. `Created a custom slash command or skill` — 写过带 frontmatter 的 `SKILL.md`，或创建过 `.claude/commands/` 文件
2. `Used dynamic context in commands` — 用过 `$ARGUMENTS`、`$0` / `$1`、反引号 `!command` 语法，或 `@file` 引用
3. `Set up project + personal memory` — 同时创建过项目级 `CLAUDE.md` 和个人级 `~/.claude/CLAUDE.md`（或 `CLAUDE.local.md`）
4. `Used memory hierarchy features` — 理解 7 层优先级，用过 `.claude/rules/`、path-specific rules 或 `@import`

Scoring: 选项 1-2 记到 **Slash Commands**（0-2）；选项 3-4 记到 **Memory**（0-2）。

---

## 第 2 轮：Skills 与 Hooks

Header: `Automation`

Prompt: `Which of these have you done? Select all that apply.`

Options:

1. `Installed and used an auto-invoked skill` — 用过会根据 `description` 自动触发的 skill，而不是只能手动 `/command` 调用
2. `Controlled skill invocation behavior` — 在 `SKILL.md` frontmatter 里用过 `disable-model-invocation`、`user-invocable` 或 `context: fork` + `agent`
3. `Set up a PreToolUse or PostToolUse hook` — 配置过工具执行前后运行的 hook，例如命令校验或自动格式化
4. `Used advanced hook features` — 配置过 prompt-type hooks、component-scoped hooks、HTTP hooks，或带 `updatedInput` / `systemMessage` 的自定义 JSON output

Scoring: 选项 1-2 记到 **Skills**（0-2）；选项 3-4 记到 **Hooks**（0-2）。

---

## 第 3 轮：MCP 与 Subagents

Header: `Integration`

Prompt: `Which of these have you done? Select all that apply.`

Options:

1. `Connected an MCP server and used its tools` — 例如 GitHub MCP、database MCP 或其他外部数据源
2. `Used advanced MCP features` — 用过 project-scope `.mcp.json`、OAuth、MCP resources `@mentions`、Tool Search 或 `claude mcp serve`
3. `Created or configured custom subagents` — 在 `.claude/agents/` 中定义过带 tools、model 或 permissions 的 agent
4. `Used advanced subagent features` — 用过 worktree isolation、persistent memory、`Ctrl+B` background tasks、`Task(agent_name)` allowlists 或 agent teams

Scoring: 选项 1-2 记到 **MCP**（0-2）；选项 3-4 记到 **Subagents**（0-2）。

---

## 第 4 轮：Checkpoints 与 Advanced Features

Header: `Power User`

Prompt: `Which of these have you done? Select all that apply.`

Options:

1. `Used checkpoints for safe experimentation` — 创建过 checkpoints，用过 `Esc+Esc` 或 `/rewind`，恢复过 code / conversation，或用过 Summarize
2. `Used planning mode or extended thinking` — 通过 `/plan`、`Shift+Tab` 或 `--permission-mode plan` 进入 planning；或用 `Alt+T` / `Option+T` 切换 extended thinking
3. `Configured permission modes` — 通过 CLI flags、快捷键或 settings 用过 `acceptEdits`、`plan`、`dontAsk` 或 `bypassPermissions`
4. `Used remote/desktop/web features` — 用过 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop` 或 `claude -w`

Scoring: 选项 1 记到 **Checkpoints**（0-1）；选项 2-4 记到 **Advanced Features**（0-3，最多计 2）。

---

## 第 5 轮：Plugins 与 CLI

Header: `Mastery`

Prompt: `Which of these have you done? Select all that apply.`

Options:

1. `Installed or created a plugin` — 安装过 marketplace plugin，或创建过带 `plugin.json` manifest 的 `.claude-plugin/` 目录
2. `Used plugin advanced features` — 用过 plugin hooks、plugin MCP servers、LSP configuration、plugin namespaced commands 或 `--plugin-dir`
3. `Used print mode in scripts or CI/CD` — 用过 `claude -p`、`--output-format json`、`--max-turns`、piped input，或集成到 GitHub Actions / CI
4. `Used advanced CLI features` — 用过 session resumption（`-c` / `-r`）、`--agents`、`--json-schema`、`--fallback-model`、`--from-pr` 或 batch processing loops

Scoring: 选项 1-2 记到 **Plugins**（0-2）；选项 3-4 记到 **CLI**（0-2）。
