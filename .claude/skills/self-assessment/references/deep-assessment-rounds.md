# Deep Assessment 题目轮次

这里保存 Deep Assessment 的 5 轮题目。每轮使用一次 AskUserQuestion，多选，最多 4 个选项；每轮覆盖 2 个能力域。除第 4 轮按 1/3 个选项分配外，其余各轮每个能力域对应 2 个选项。评分映射也保留在 `SKILL.md` 的 Step 2B，方便不重新读取本文件也能计算结果。

---

## 第 1 轮：Slash Commands 与 Memory

Header: `命令`

Prompt: `下面哪些操作你做过？请选择所有符合的选项。`

Options:

1. `创建过 slash command 或 skill` — 写过带 frontmatter 的 `SKILL.md`，或创建过 `.claude/commands/` 文件
2. `在 command 中使用过动态上下文` — 用过 `$ARGUMENTS`、`$0` / `$1`、反引号 `!command` 语法，或 `@file` 引用
3. `同时配置过项目和个人 memory` — 同时创建过项目级 `CLAUDE.md` 和个人级 `~/.claude/CLAUDE.md`（或 `CLAUDE.local.md`）
4. `使用过 memory 层级功能` — 理解 8 层优先级，用过 `.claude/rules/`、path-specific rules 或 `@import`

Scoring: 选项 1-2 记到 **Slash Commands**（0-2）；选项 3-4 记到 **Memory**（0-2）。

---

## 第 2 轮：Skills 与 Hooks

Header: `自动化`

Prompt: `下面哪些操作你做过？请选择所有符合的选项。`

Options:

1. `安装并使用过自动触发的 skill` — 用过会根据 `description` 自动触发的 skill，而不是只能手动 `/command` 调用
2. `控制过 skill 调用方式` — 在 `SKILL.md` frontmatter 里用过 `disable-model-invocation`、`user-invocable` 或 `context: fork` + `agent`
3. `设置过 PreToolUse 或 PostToolUse hook` — 配置过工具执行前后运行的 hook，例如命令校验或自动格式化
4. `使用过进阶 hook 功能` — 配置过 prompt-type hooks、component-scoped hooks、HTTP hooks，或带 `updatedInput` / `systemMessage` 的自定义 JSON output

Scoring: 选项 1-2 记到 **Skills**（0-2）；选项 3-4 记到 **Hooks**（0-2）。

---

## 第 3 轮：MCP 与 Subagents

Header: `集成`

Prompt: `下面哪些操作你做过？请选择所有符合的选项。`

Options:

1. `连接过 MCP server 并使用其工具` — 例如 GitHub MCP、database MCP 或其他外部数据源
2. `使用过进阶 MCP 功能` — 用过 project-scope `.mcp.json`、OAuth、MCP resources `@mentions`、Tool Search 或 `claude mcp serve`
3. `创建或配置过自定义 subagents` — 在 `.claude/agents/` 中定义过带 tools、model 或 permissions 的 agent
4. `使用过进阶 subagent 功能` — 用过 worktree isolation、persistent memory、`Ctrl+B` background tasks、`Task(agent_name)` allowlists 或 agent teams

Scoring: 选项 1-2 记到 **MCP**（0-2）；选项 3-4 记到 **Subagents**（0-2）。

---

## 第 4 轮：Checkpoints 与 Advanced Features

Header: `高级`

Prompt: `下面哪些操作你做过？请选择所有符合的选项。`

Options:

1. `用 checkpoints 做过安全试验` — 创建过 checkpoints，用过 `Esc+Esc` 或 `/rewind`，恢复过 code / conversation，或用过 Summarize
2. `使用过 planning mode 或 extended thinking` — 通过 `/plan`、`Shift+Tab` 或 `--permission-mode plan` 进入 planning；或用 `Alt+T` / `Option+T` 切换 extended thinking
3. `配置过 permission modes` — 通过 CLI flags、快捷键或 settings 用过 `acceptEdits`、`plan`、`dontAsk` 或 `bypassPermissions`
4. `使用过 remote / desktop / web 功能` — 用过 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop` 或 `claude -w`

Scoring: 选项 1 记到 **Checkpoints**（0-1）；选项 2-4 记到 **Advanced Features**（0-3，最多计 2）。

---

## 第 5 轮：Plugins 与 CLI

Header: `综合`

Prompt: `下面哪些操作你做过？请选择所有符合的选项。`

Options:

1. `安装或创建过 plugin` — 安装过 marketplace plugin，或创建过带 `plugin.json` manifest 的 `.claude-plugin/` 目录
2. `使用过 plugin 进阶功能` — 用过 plugin hooks、plugin MCP servers、LSP configuration、plugin namespaced commands 或 `--plugin-dir`
3. `在脚本或 CI/CD 中使用过 print mode` — 用过 `claude -p`、`--output-format json`、`--max-turns`、piped input，或集成到 GitHub Actions / CI
4. `使用过进阶 CLI 功能` — 用过 session resumption（`-c` / `-r`）、`--agents`、`--json-schema`、`--fallback-model`、`--from-pr` 或 batch processing loops

Scoring: 选项 1-2 记到 **Plugins**（0-2）；选项 3-4 记到 **CLI**（0-2）。
