# Changelog

> 本文件保留上游版本信息的时间顺序，但用中文补充阅读说明，方便中文用户快速判断“这个仓库最近同步了什么”。

## v2.2.0 — 2026-03-26

### Documentation

- 将全部教程和参考文档同步到 Claude Code `v2.1.84`
  - slash commands 更新为 55+ 个内建命令 + 5 个 bundled skills，并标记 3 个已废弃项
  - hooks 事件从 18 个扩展到 25 个，并新增 `agent` hook type
  - advanced features 新增 Auto Mode、Channels、Voice Dictation
  - `SKILL.md` frontmatter 新增 `effort`、`shell`
  - subagent 字段新增 `initialPrompt`、`disallowedTools`
  - MCP 新增 WebSocket transport、elicitation、2KB tool cap 等说明
  - plugins 新增 LSP、`userConfig`、`${CLAUDE_PLUGIN_DATA}` 相关支持
  - 更新 `CATALOG`、`QUICK_REFERENCE`、`LEARNING-ROADMAP`、`INDEX`
- README 改写为更像 landing page 的结构

### Bug Fixes

- 为 CI 补充缺失的 cSpell 词条和 README 章节
- 在 cSpell 词典中加入 `Sandboxing`

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug Fixes

- 删除导致链接检查失败的无效 marketplace 链接
- 在 cSpell 词典中补充 `sandboxed` 和 `pycache`

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Features

- 新增自适应学习路径、自测和课后测验相关 skills
  - `/self-assessment`：对 10 个能力域做交互式自测并给出个性化学习路径
  - `/lesson-quiz [lesson]`：针对单个模块做 8-10 题知识检查

### Bug Fixes

- 更新失效 URL、已废弃写法和过时引用
- 修复资源文档和自测 skill 里的坏链
- 将概念指南中的嵌套代码块改为波浪线 fence
- 增补 cSpell 词典缺失词条

### Documentation

- 修正文档里的术语、URL 和一致性问题
- 完成缺失能力覆盖与参考文档补齐
- 在 MCP 章节加入 MCPorter 运行时说明
- 补充缺失命令、设置项和特性说明
- 新增风格指南
- 将自测和 lesson-quiz 引入 README 与路线图

### New Contributors

- `@VikalpP` 首次贡献

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Features

- 将文档整体同步到 2026 年 2 月的 Claude Code 能力集
  - 新增 Auto Memory
  - 新增 Remote Control、Web Sessions、Desktop App
  - 新增 Agent Teams（实验性）
  - 新增 MCP OAuth 2.0、Tool Search、Claude.ai Connectors
  - 新增 subagents 的 persistent memory 与 worktree isolation
  - 新增 background subagents、task list、prompt suggestions
  - 新增 sandboxing 与 managed settings
  - 新增 HTTP hooks 和 7 个新事件
  - 新增 plugin settings、LSP、marketplace 相关说明
  - 补充 checkpoints 的 summarize from checkpoint
  - 补充 17 个新 slash commands
  - 补充一批新 CLI flags 和环境变量

### Design

- 重做 logo，改为更简洁的视觉设计

### Bug Fixes / Corrections

- 更新模型名：Sonnet 4.5 → Sonnet 4.6，Opus 4.5 → Opus 4.6
- 修正 permission mode 名称
- 修正 hooks 事件名
- 修正 CLI 写法：`claude-code --headless` → `claude -p`
- 修正 checkpoint 命令示例
- 修正 session 管理命令
- 修正 plugin manifest：`plugin.yaml` → `.claude-plugin/plugin.json`
- 修正 MCP 配置路径
- 修正文档 URL，并删除虚构地址
- 移除多个虚构配置字段

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
