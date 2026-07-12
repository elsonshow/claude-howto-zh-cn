# 资源总览

仓库里的 `resources/` 目录主要存放：

- logo
- icon
- favicon
- 设计系统说明
- 快速使用说明
- 供文档引用的配套资源索引

如果你要把这个中文 fork 发布成独立仓库，也可以在保留来源说明的前提下替换这些资源。

## 2026 年 7 月需要关注的新能力

这轮同步后，中文读者如果只看资源索引，至少要知道这些新入口：

| 能力 | 说明 | 入口 |
|------|------|------|
| `/usage-credits` | 配置额外用量额度；`/extra-usage` 仍可作为 alias（别名） | [Slash Commands](01-slash-commands/) |
| `/run` / `/verify` | bundled skills，用于启动项目并确认改动真实可用 | [Skills Guide](03-skills/) |
| `/run-skill-generator` | 为项目生成专属 run / verify skill | [Skills Guide](03-skills/) |
| `claude agents --json` | 输出机器可读的 Agent View 列表 | [CLI Guide](10-cli/) |
| `/code-review [effort]` | 内置正确性缺陷审查命令，可传入 `/code-review high` | [Skills Guide](03-skills/) |
| `/simplify` | 清理型审查命令，关注复用、简化、效率和抽象层级 | [Skills Guide](03-skills/) |
| `/reload-skills` | 重新扫描 skill 目录，不需要重启当前 session | [Skills Guide](03-skills/) |
| `/workflows` | 查看 dynamic workflows 的运行记录 | [Advanced Features](09-advanced-features/) |
| `/cd <path>` | 切换当前 session 工作目录，并尽量保留 prompt cache | [Slash Commands](01-slash-commands/) |
| `--safe-mode` / `CLAUDE_CODE_SAFE_MODE=1` | 禁用 CLAUDE.md、plugins、skills、hooks、MCP servers，用于排查配置问题 | [Advanced Features](09-advanced-features/) |
| `fallbackModel` | 配置最多三个 fallback models；`--fallback-model` 也适用于交互式 session | [CLI Guide](10-cli/) |
| `disableBundledSkills` | 隐藏内置 skills、workflows 和 commands | [Skills Guide](03-skills/) |
| `/plugin list --enabled` | 按启用状态查看 installed plugins | [Plugins Guide](07-plugins/) |
| `hookSpecificOutput.additionalContext` | Stop / SubagentStop hook 给 Claude 追加上下文并继续当前 turn | [Hooks Guide](06-hooks/) |
| `CLAUDE_CODE_SESSION_ID` | 串联 MCP server、hooks 和 Bash 日志的 session 标识 | [MCP Guide](05-mcp/) |
| `claude plugin init <name>` | 在 `.claude/skills` 中脚手架本地 plugin；该目录下的 plugin 会自动加载 | [Plugins Guide](07-plugins/) |
| `CLAUDE_CODE_ENABLE_AUTO_MODE=1` | 在 Bedrock / Vertex / Foundry 上对 Opus 4.7 / 4.8 显式启用 Auto Mode | [CLI Guide](10-cli/) |
| `EnterWorktree` | 在同一 session 中切换 Claude 管理的 worktree | [Advanced Features](09-advanced-features/) |
| `claude agents` 里的 `Ctrl+T` | 固定后台 session，空闲时优先保留 | [CLI Guide](10-cli/) |
| `allowAllClaudeAiMcps` | 组织级允许加载 claude.ai 云端 MCP connectors 的托管设置 | [MCP Guide](05-mcp/) |
| `Agent(agent_type)` | 限制 subagent 能 spawn 哪些子 subagent；`v2.1.172+` 最多支持 5 层嵌套 | [Subagents Guide](04-subagents/) |
| hook `if` 条件 | 用 permission-rule 语法按工具参数继续收窄 hook 匹配 | [Hooks Guide](06-hooks/) |
| `/plugin` marketplace 搜索栏 | 在 marketplace 浏览界面按名称或关键词过滤 plugin | [Plugins Guide](07-plugins/) |
| `enforceAvailableModels` | 托管策略强制 `availableModels` 也约束 Default model | [Advanced Features](09-advanced-features/) |
| `wheelScrollAccelerationEnabled` | 关闭全屏 renderer 的鼠标滚轮加速 | [CLI Guide](10-cli/) |
| `footerLinksRegexes` | 把匹配正则的链接显示成 footer badges | [CLI Guide](10-cli/) |
| `language` | 设置回复、语音听写和自动 session title 的偏好语言 | [CLI Guide](10-cli/) |
| `/doctor` | 诊断安装、配置和 plugin 健康；`v2.1.178+` 起是 flat tree 布局 | [Slash Commands](01-slash-commands/) |
| `/bug` | 提交反馈；`v2.1.178+` 起必须填写描述 | [Slash Commands](01-slash-commands/) |
| `Tool(param:value)` | permission rule 按工具输入参数继续细化匹配 | [CLI Guide](10-cli/) |
| 嵌套 `.claude/agents/` 最近目录优先 | monorepo 中同名 agent 采用离当前目录最近的定义 | [Subagents Guide](04-subagents/) |
| remote session plugin loading | remote session 里的 plugin 加载性能在 `v2.1.179+` 改进 | [Plugins Guide](07-plugins/) |
| `/review <pr>` | 审查 GitHub PR；本地 diff 仍用 `/code-review [effort]` | [Slash Commands](01-slash-commands/) |
| `claude mcp login/logout` | 在 CLI 中处理 MCP server OAuth 登录状态，`--no-browser` 适合 SSH / headless session | [MCP Guide](05-mcp/) |
| `--teammate-mode iterm2` | 让 teammate 进入 iTerm2 pane，依赖 `it2` CLI | [Subagents Guide](04-subagents/) |
| `respondToBashCommands` | 控制 `!` bash 命令输出后是否自动让 Claude 回复 | [Advanced Features](09-advanced-features/) |
| Auto Mode 内置意图保护 | 默认拦截一批破坏性命令，除非当前 session 明确要求 | [Advanced Features](09-advanced-features/) |
| `sandbox.credentials` | 阻止 sandboxed commands 读取凭证文件和 secret 环境变量 | [Advanced Features](09-advanced-features/) |
| `/config key=value` | 直接从 prompt 设置单个配置项 | [Advanced Features](09-advanced-features/) |
| `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` | 调整 remote MCP tool 无响应 abort 超时 | [CLI Guide](10-cli/) |
| MCP 认证启动提醒 / `headersHelper` 自动刷新 | 启动时提示仍需认证的 MCP server；HTTP 401 / 403 后动态认证头会自动刷新 | [MCP Guide](05-mcp/) |
| hook `matcher` 逗号列表 | `"Write,Edit"` 这类 matcher 会匹配任一列出的工具，并按更精确规则匹配工具名 | [Hooks Guide](06-hooks/) |
| `/plugin` unused plugins 提示 | `/plugin` 会提示不再使用的 plugins；plugin name 和 marketplace entry name 不一致时仍能 enable / disable | [Plugins Guide](07-plugins/) |
| `/rewind` 跨 `/clear` | `/clear` 不再是硬边界，可以回到更早 checkpoint | [Checkpoints Guide](08-checkpoints/) |
| `autoMode.classifyAllShell` | 让所有 Bash / PowerShell 命令都经过 Auto Mode 分类器 | [Advanced Features](09-advanced-features/) |
| `claude_code.assistant_response` | OpenTelemetry log event，用于记录模型回复文本 | [Advanced Features](09-advanced-features/) |
| `!` bash mode 路径自动补全 | 输入 `!` shell 命令时支持 live file-path autocomplete | [Advanced Features](09-advanced-features/) |
| `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` | 禁用 fullscreen mode 的 mouse click / drag / hover，wheel scroll 仍可用 | [CLI Guide](10-cli/) |
| Sonnet 5 / `claude-sonnet-5` | 原生 1M context window；是否作为默认模型取决于订阅档位 | [CLI Guide](10-cli/) |
| `manual` permission mode | `v2.1.200+` 的交互默认名称；旧 `default` 仍作为 alias 可用 | [Advanced Features](09-advanced-features/) |
| `/dataviz` | 图表、dashboard 与调色板设计 bundled skill | [Skills Guide](03-skills/) |
| `${CLAUDE_PROJECT_DIR}` | 在 command / skill 中引用项目根目录绝对路径 | [Skills Guide](03-skills/) |
| subagent 默认后台运行 | `Explore` 继承 session 模型，extended thinking 也会继承 | [Subagents Guide](04-subagents/) |
| MCP `roots/list` | 向 MCP server 暴露启动目录和额外工作目录 | [MCP Guide](05-mcp/) |
| `agent_needs_input` / `agent_completed` | 后台 agent 对应的 `Notification` matcher | [Hooks Guide](06-hooks/) |
| `renames` / `displayName` / `defaultEnabled` | marketplace entry 的迁移、显示和默认启用控制 | [Plugins Guide](07-plugins/) |
| `Summarize up to here` | 压缩所选位置之前的对话，与 `Summarize from here` 组成双向压缩 | [Checkpoints Guide](08-checkpoints/) |
| `askUserQuestionTimeout` / `enableArtifact` | 控制询问超时和 Artifact tool 的个人设置 | [Advanced Features](09-advanced-features/) |
| `CLAUDE_ENABLE_STREAM_WATCHDOG` | streaming 5 分钟无事件时 abort / retry；设为 `0` 可禁用 | [CLI Guide](10-cli/) |

这些名称都是可执行标识或协议字段，不要翻译成中文 key。
