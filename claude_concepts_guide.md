# Claude Code 概念总览

这个文件用于把仓库里最容易混淆的几个核心概念放在一起解释。

## 1. Slash Commands（快捷命令）

用户主动输入的快捷命令，适合显式触发某个动作。

## 2. Memory（记忆）

长期自动加载的上下文，适合放项目规则和个人偏好。

## 3. Skills（技能）

可复用、可自动触发的能力，适合沉淀稳定工作流。

`v2.1.206` 这轮同步后，特别值得关注这些 bundled skills、plugin 和排障入口：

- `/run`：启动当前项目，确认改动能真实运行
- `/verify`：构建、运行并观察应用，确认修复不是只停留在测试通过
- `/run-skill-generator`：为项目生成专属 run / verify skill
- `/code-review [effort]`：审查当前 diff 的正确性缺陷
- `/simplify`：清理型审查，关注复用、简化、效率和抽象层级，并应用修复
- `/dataviz`：图表和 dashboard 设计指导，附带可运行的调色板校验器
- `${CLAUDE_PROJECT_DIR}`：在 skill body 和 `allowed-tools` 中引用项目根目录绝对路径
- 一次调用可叠加最多 6 个开头的 slash-skills，重复 skill 内容会去重
- `/reload-skills`：重新扫描 skill 目录，不需要重启当前 session
- `disableBundledSkills` / `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS=1`：隐藏内置 skills、workflows 和 commands
- `claude plugin init <name>`：在 `.claude/skills` 中脚手架本地 plugin，放在该目录的 plugin 会自动加载
- `/plugin list --enabled` / `--disabled`：按启用状态查看 installed plugins
- `/doctor`：诊断安装、配置和 plugin 健康状态；`v2.1.178+` 起界面是 flat tree 布局
- `/bug`：提交反馈；`v2.1.178+` 起必须填写描述
- `/review <pr>`：审查 GitHub PR；`v2.1.186+` 起复用 `/code-review medium` 的 review engine，本地 diff 仍用 `/code-review [effort]`

## 4. Subagents（子代理）

用于复杂任务拆分和专业分工的子代理。

从 `v2.1.172+` 起，subagent 可以再 spawn 子 subagent，最多嵌套 5 层；如果要限制可 spawn 的对象，保留 `Agent(agent_type)` 语法，不要翻译成中文字段。

从 `v2.1.178+` 起，嵌套 `.claude/agents/` 里的同名 agent 会按“离当前工作目录最近者优先”加载；workflow 和 output-style 定义也遵循这个规则。

从 `v2.1.198+` 起，subagents 默认在后台运行，built-in `Explore` 会继承 session 模型（上限 Opus），extended thinking 也会继承。`CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` 可禁用 built-in Explore / Plan，`--append-subagent-system-prompt` 可在 print mode 中追加统一提示。

Agent Teams 的 teammate mode 也新增了 `--teammate-mode iterm2`，可把 teammate 放进 iTerm2 pane；该模式依赖 `it2` CLI。

## 5. MCP（外部工具协议）

让 Claude 连接外部工具和实时数据的协议。

从 `v2.1.186+` 起，`claude mcp login <name>` / `claude mcp logout <name>` 可以直接在 CLI 中处理 MCP server 登录状态；`--no-browser` 适合 SSH 或 headless session。

从 `v2.1.193+` 起，启动时会提示哪些 MCP server 仍需要认证；如果你用 `headersHelper` 提供动态认证头，遇到 HTTP 401 / 403 时会自动刷新。

从 `v2.1.203+` 起，MCP server 可通过 `roots/list` 获得启动目录和 `--add-dir` / `additionalDirectories`，目录变化时会收到 `notifications/roots/list_changed`。未信任 workspace 中的 project MCP 会保持 `Pending approval`，不能靠 `enableAllProjectMcpServers` 自动绕过。

## 6. Hooks（钩子）

在特定事件上自动执行动作的机制。

从 `v2.1.172+` 起，hook handler 可以加 `if` 条件，用 `Edit(src/**)`、`Read(.env)`、`Bash(git push *)` 这类 permission-rule 语法按工具参数继续收窄匹配。

从 `v2.1.178+` 起，permission rule 还可以用 `Tool(param:value)` 形式按工具输入参数匹配。这个语法本身不要翻译。

从 `v2.1.191+` 起，`matcher` 支持 `"Write,Edit"` 这类逗号列表；从 `v2.1.195+` 起，工具名匹配更精确，带连字符的 MCP tool name 不会再因为子串重叠误触发。

这轮同步移除了上一版里关于 `Stop` / `SubagentStop` 可读取 `background_tasks`、`session_crons` 的说明；当前官方 hooks reference 没有列出这两个字段，写 hook 时不要依赖它们。

`Notification` matcher 新增 `agent_needs_input` 和 `agent_completed`；hook 输入新增 `prompt_id`，可与 OpenTelemetry `prompt.id` 对齐。

## 7. Plugins（插件）

把 commands、skills、MCP、hooks、subagents 打包成整套方案。

从 `v2.1.187+` 起，`/plugin` 会提示 unused plugins；从 `v2.1.195+` 起，plugin 的 `plugin.json` `name` 和 marketplace entry name 不一致时，enable / disable 仍能正确工作。

marketplace entry 还支持 `renames`、`displayName`、`defaultEnabled`；`first-party-plugins` 和 `healthcare` 是官方保留的 marketplace 名称。

## 8. Checkpoints（检查点）

用于安全试错和回退。

从 `v2.1.191+` 起，`/clear` 不再是 `/rewind` 的硬边界。需要时可以回到 `/clear` 之前创建的 checkpoint。

`Summarize up to here` 可以压缩所选位置之前的对话，与 `Summarize from here` 组成双向定点压缩。

## 9. CLI（命令行）

Claude Code 的核心使用入口，也是自动化、脚本化和 CI/CD 的关键接口。

`claude agents --json` 可以把 Agent View 列表输出为机器可读 JSON，适合接状态栏、脚本巡检或自定义 session picker。

在 `claude agents` 视图里，`Ctrl+T` 可以固定后台 session。已固定的 session 空闲时会被优先保留，升级 Claude Code 时也会在原位重启，只有内存压力较大时才会在未固定 session 之后被清理。

`/usage` 的成本页现在会按 skills、subagents、plugins、MCP server 等类别拆分，排查“钱花在哪里”会更直观。

`v2.1.174+` 的 VSCode Account & usage 视图还会显示 cache miss、long-context cost、subagents，以及 per-skill / per-agent / per-plugin / per-MCP 归因。

`/workflows` 可以查看 dynamic workflows 的运行记录，适合大规模审查、迁移、全仓扫描这类需要多代理编排的任务。

`v2.1.160` 起，dynamic workflows 的触发关键词是 `ultracode`；裸词 `workflow` 不再触发运行。

`/model` 的默认行为也要注意：`v2.1.153+` 起选择模型会保存为后续 session 默认值；如果只想作用于当前 session，选中后按 `s`。

`--safe-mode` / `CLAUDE_CODE_SAFE_MODE=1` 适合排查自定义配置问题；`fallbackModel` 适合给主模型不可用时准备有序 fallback。

`wheelScrollAccelerationEnabled`、`footerLinksRegexes`、`language` 是 settings.json 里的 key，说明文字可以中文化，但 key 本身不要翻译。

`respondToBashCommands` 控制 `!` bash 命令输出后是否自动让 Claude 回复；默认 `true`，设为 `false` 可回到只把输出放进上下文的旧行为。

交互 permission mode 从 `v2.1.200+` 起显示为 `manual`，旧 `default` 仍是 alias。`askUserQuestionTimeout`、`enableArtifact`、`CLAUDE_ENABLE_STREAM_WATCHDOG` 和 Sonnet 5 的 `claude-sonnet-5` 都已进入当前口径。

从 `v2.1.193+` 起，`!` bash mode 支持 live file-path autocomplete。`autoMode.classifyAllShell` 可以让所有 Bash / PowerShell 命令都过 Auto Mode 分类器，`claude_code.assistant_response` 可把模型回复文本写进 OpenTelemetry log event。

`CLAUDE_CLIENT_PRESENCE_FILE`、`CLAUDE_CODE_MAX_RETRIES`、`CLAUDE_CODE_RETRY_WATCHDOG`、`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`、`CLAUDE_CODE_DISABLE_MOUSE_CLICKS` 是环境变量标识，不要翻译。`sandbox.credentials`、`sandbox.allowAppleEvents`、`autoMode.classifyAllShell` 和 `/config key=value` 属于配置 / 命令口径，也要保持原文。
