<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Subagents 指南

subagents 是 Claude Code 里做复杂任务拆分的关键能力。你可以把它理解成“主 Claude 把某个子任务交给一个更专业、上下文更独立的助手去做”。

---

## subagents 是什么

subagent 具备这些特点：

- 有自己的角色定位
- 有自己的上下文窗口
- 可以限制可用工具
- 可以使用单独的 system prompt
- 适合做任务拆分和专业分工

它不是简单的“再开一个对话”，而是 Claude Code 的正式能力机制。

---

## 什么时候值得用 subagents

非常适合：

- 大型代码审查
- 安全审查
- 测试策略分析
- 文档生成
- 调试与根因定位
- 多条线并行处理

不太适合：

- 单文件的小改动
- 简单解释性问题
- 只需要几步就能完成的轻任务

---

## subagents 的核心价值

| 价值 | 说明 |
|------|------|
| 上下文隔离 | 避免主对话被复杂细节污染 |
| 专业分工 | 不同 agent 做不同任务 |
| 工具隔离 | 可以限制某个 agent 能做什么 |
| 可复用 | 适合团队共享常用角色 |

---

## 文件放哪里

| 类型 | 路径 | 作用域 |
|------|------|--------|
| 项目级 | `.claude/agents/` | 当前项目 |
| 用户级 | `~/.claude/agents/` | 所有项目 |
| plugin 自带 | plugin 的 `agents/` 目录 | 随 plugin 启用 |

---

## 文件格式长什么样

subagent 文件通常是：

1. YAML frontmatter
2. 后面跟 Markdown 形式的 system prompt

一个典型结构如下：

```yaml
---
name: code-reviewer
description: Review recent changes for quality issues
tools: Read, Grep, Glob, Bash
model: inherit
---
```

---

## frontmatter 里这些字段不要翻

- `name`
- `description`
- `tools`
- `model`
- `effort`
- `permissionMode`
- `skills`
- `mcpServers`

如果你是做中文本地化，这些字段要保真；可以翻译的是下面真正给人看的 system prompt 正文。

---

## 本目录里的示例 subagents

| 名称 | 文件 | 用途 |
|------|------|------|
| `code-reviewer` | `code-reviewer.md` | 代码审查 |
| `clean-code-reviewer` | `clean-code-reviewer.md` | Clean Code 角度审查 |
| `test-engineer` | `test-engineer.md` | 测试覆盖与测试策略 |
| `documentation-writer` | `documentation-writer.md` | 文档生成 |
| `secure-reviewer` | `secure-reviewer.md` | 安全检查 |
| `implementation-agent` | `implementation-agent.md` | 功能实现 |
| `debugger` | `debugger.md` | 错误调试与根因定位 |
| `data-scientist` | `data-scientist.md` | 数据分析与 SQL 任务 |

---

## 如何安装

```bash
mkdir -p .claude/agents
cp 04-subagents/*.md .claude/agents/
```

或者安装单个：

```bash
cp 04-subagents/code-reviewer.md .claude/agents/
```

---

## 如何决定要不要拆成 subagents

### 推荐拆

- 任务本身可以天然分工
- 某个子任务需要单独工具权限
- 某个子任务需要更专门的 system prompt
- 你希望并行推进多个分析方向

### 不推荐拆

- 任务太小
- 子任务之间高度耦合、必须反复共享细节
- 你自己还没想清楚主任务是什么

---

## 常见坑

### 1. subagent 角色太模糊

如果 description 太空，Claude 就不知道什么时候该委派给它。

### 2. 工具给太多或太少

- 给太多：失去隔离价值
- 给太少：agent 做不了事

### 3. 直接把中文翻译写进字段名

像 `tools`、`model`、`name` 这些不能翻。

---

## 中国用户特别注意

- 如果 subagent 需要调用 shell，先确认 shell 环境。
- 如果某个 agent 依赖 Git、Python、Node、数据库 CLI 等工具，最好在正文里写清依赖。
- Windows 环境下尤其要提前确认路径和命令兼容性。

---

## 推荐下一步

- 想让 Claude 连接外部系统：看 [05-mcp](../05-mcp/)
- 想做自动检查和自动触发：看 [06-hooks](../06-hooks/)
- 想打包成团队工作流：看 [07-plugins](../07-plugins/)
