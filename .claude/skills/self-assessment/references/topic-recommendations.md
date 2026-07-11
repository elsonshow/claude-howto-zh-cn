# 按主题给出的学习建议

当某个主题是短板时，按这里生成具体建议。路径相对于本文件所在目录（`.claude/skills/self-assessment/references/`）。

**Slash Commands（score 0）**:
- Tutorial: [01-slash-commands/](../../../../01-slash-commands/)
- Focus on: built-in commands reference、创建第一个 `SKILL.md`、`$ARGUMENTS` syntax
- Key exercise: 创建一个 `/optimize` command 并测试
- Done when: 你能创建带 arguments 和 dynamic context 的 custom skill

**Slash Commands（score 1 — review）**:
- Focus on: 通过反引号 `!command` 注入 dynamic context、`@file` references、`disable-model-invocation` 与 `user-invocable` 的调用控制差异
- Done when: 你能创建一个会注入 live command output、并控制自身触发方式的 skill

**Memory（score 0）**:
- Tutorial: [02-memory/](../../../../02-memory/)
- Focus on: 创建 `CLAUDE.md`、`/init` 和 `/memory` commands、长期规则与一次性上下文的边界
- Key exercise: 创建一个写有编码规范的项目级 `CLAUDE.md`
- Done when: Claude 能跨 session 记住你的项目偏好

**Memory（score 1 — review）**:
- Focus on: 7-level hierarchy 与 priority order、带 path-specific rules 的 `.claude/rules/` 目录、`@import` syntax（max depth 5）、Auto Memory 的 `MEMORY.md`（200-line limit）
- Done when: 你有按目录拆分的 modular rules，并理解完整层级

**Skills（score 0）**:
- Tutorial: [03-skills/](../../../../03-skills/)
- Focus on: `SKILL.md` format、通过 `description` 自动触发、progressive disclosure（三层加载）
- Key exercise: 安装 `code-review` skill 并验证它会自动触发
- Done when: skill 能根据对话场景自动激活

**Skills（score 1 — review）**:
- Focus on: `context: fork` 搭配 `agent` field 让 skill 在 subagent 执行、`disable-model-invocation` 与 `user-invocable`、2% context budget、bundled resources（`scripts/`、`references/`、`assets/`）
- Done when: 你能创建一个在 forked context 的 subagent 中运行的 skill

**Hooks（score 0）**:
- Tutorial: [06-hooks/](../../../../06-hooks/)
- Focus on: hooks 配置结构（`matcher` + hooks array）、`PreToolUse` / `PostToolUse` events、exit codes（0=success, 2=block）、JSON input/output format
- Key exercise: 创建一个能校验 Bash commands 的 `PreToolUse` hook
- Done when: hook 能在执行前阻止危险命令

**Hooks（score 1 — review）**:
- Focus on: 25 个 hook events（包括 `PostToolUseFailure`、`StopFailure`、`TaskCreated`、`CwdChanged`、`FileChanged`、`PostCompact`、`Elicitation`、`ElicitationResult`）、hook types（`command`、`http`、`prompt`、`agent`）、`SKILL.md` frontmatter 里的 component-scoped hooks、带 `allowedEnvVars` 的 HTTP hooks、`SessionStart` / `CwdChanged` / `FileChanged` 可用的 `CLAUDE_ENV_FILE`
- Done when: 你能创建一个 prompt-based `Stop` hook，以及一个 skill 内的 component-scoped hook

**MCP（score 0）**:
- Tutorial: [05-mcp/](../../../../05-mcp/)
- Focus on: `claude mcp add` command、transport types（HTTP recommended）、GitHub MCP 配置、environment variable expansion
- Key exercise: 添加 GitHub MCP server 并查询 PRs
- Done when: 你能通过 MCP 查询外部服务的 live data

**MCP（score 1 — review）**:
- Focus on: project-scope `.mcp.json`（需要团队 approval）、OAuth 2.0 auth、带 `@server:resource` mentions 的 MCP resources、Tool Search（`ENABLE_TOOL_SEARCH`）、`claude mcp serve`、output limits（10k / 25k / 50k）
- Done when: 你有 project `.mcp.json`，并理解 Tool Search auto mode

**Subagents（score 0）**:
- Tutorial: [04-subagents/](../../../../04-subagents/)
- Focus on: agent file format（`.claude/agents/*.md`）、built-in agents（`general-purpose`、`Plan`、`Explore`）、`tools` / `model` / `permissionMode` config
- Key exercise: 创建一个 `code-reviewer` subagent 并测试 delegation
- Done when: Claude 能把 code review 委派给你的 custom agent

**Subagents（score 1 — review）**:
- Focus on: worktree isolation（`isolation: worktree`）、persistent agent memory（带 scopes 的 `memory` field）、background agents（`Ctrl+B` / `Ctrl+F`）、`Task(agent_name)` allowlists、agent teams（`--teammate-mode`）
- Done when: 你有一个带 persistent memory、并运行在 worktree isolation 中的 subagent

**Checkpoints（score 0）**:
- Tutorial: [08-checkpoints/](../../../../08-checkpoints/)
- Focus on: `Esc+Esc` 和 `/rewind` 入口、5 种 rewind options（restore code+conversation、restore conversation、restore code、summarize、cancel）、限制（bash filesystem ops 不被追踪）
- Key exercise: 做一组实验性改动，然后 rewind 恢复
- Done when: 你能放心实验，并知道如何回退

**Advanced Features（score 0）**:
- Tutorial: [09-advanced-features/](../../../../09-advanced-features/)
- Focus on: planning mode（`/plan` 或 `Shift+Tab`）、permission modes、extended thinking（`Alt+T` toggle）
- Key exercise: 用 planning mode 设计一个功能，再执行实现
- Done when: 你能在 planning 和 implementation 之间自然切换

**Advanced Features（score 1 — review）**:
- Focus on: remote control（`claude remote-control`）、web sessions（`claude --remote`）、desktop handoff（`/desktop`）、worktrees（`claude -w`）、task lists（`Ctrl+T`）、enterprise managed settings 的使用场景
- Done when: 你能在 CLI、web 和 desktop 之间交接 session

**Plugins（score 0）**:
- Tutorial: [07-plugins/](../../../../07-plugins/)
- Focus on: plugin structure（`.claude-plugin/plugin.json`）、plugin 能打包什么（commands、agents、MCP、hooks、settings）、marketplace installation
- Key exercise: 安装一个 plugin 并查看它包含哪些组件
- Done when: 你知道什么时候该用 plugin，而不是 standalone components

**Plugins（score 1 — review）**:
- Focus on: 创建 `plugin.json` manifest、plugin hooks（`hooks/hooks.json`）、LSP configuration（`.lsp.json`）、`${CLAUDE_PLUGIN_ROOT}` variable、`--plugin-dir` testing、marketplace publishing
- Done when: 你能为团队创建并测试一个 plugin

**CLI（score 0）**:
- Tutorial: [10-cli/](../../../../10-cli/)
- Focus on: interactive vs print mode、`claude -p` with piping、`--output-format json`、session management（`-c` / `-r`）
- Key exercise: 把文件 pipe 给 `claude -p` 并获得 JSON output
- Done when: 你能在脚本中非交互式使用 Claude

**CLI（score 1 — review）**:
- Focus on: 带 JSON config 的 `--agents` flag、`--json-schema` structured output、`--fallback-model`、`--from-pr`、`--strict-mcp-config`、for loops batch processing、`claude mcp serve`
- Done when: 你有一个使用 Claude 并输出 structured JSON 的 CI/CD script
