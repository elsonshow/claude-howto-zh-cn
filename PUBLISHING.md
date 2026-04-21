# Publishing Notes

## 推荐 commit message

### 单行版本

```text
docs: sync upstream and keep Chinese-English parallel docs
```

### 带正文版本

```text
docs: sync upstream and keep Chinese-English parallel docs

- merge the latest upstream Claude How To content
- keep the English source in the repository root
- keep Chinese documentation under zh/ for side-by-side reading
- preserve fork maintenance notes for future localization syncs
```

## 推荐仓库描述（GitHub About）

```text
Claude Code 中文对照指南。基于 luongnv89/claude-howto 同步维护，根目录保留英文原文，zh/ 提供中文版本，方便中英文对照学习。
```

## 推荐 GitHub 首页摘要

```text
这是一个基于 luongnv89/claude-howto 的非官方中文对照 fork。根目录保留上游英文主线，zh/ 目录提供中文版本，方便用户在英文原文和中文说明之间对照学习。

你可以从 README、学习路线图和速查卡开始，再逐步进入 slash commands、memory、skills、MCP、hooks、subagents、plugins、CLI 等模块。中文文档会保留关键可执行标识，尽量避免“中文化后示例不可用”的问题。
```

## 推荐首版 Release 标题

```text
v1.1.0 - 中英文对照同步版
```

## 推荐首版 Release 摘要

```text
同步上游主线内容，并调整为英文根目录 + zh/ 中文目录的中英文对照结构。

本版保留上游英文原文，补齐中文入口，方便后续继续跟随主仓库更新。
```

## 发布前建议核对

- 仓库默认分支是否正确
- `UPSTREAM.md` 中的来源说明是否保留
- GitHub 仓库 About 文案是否与 README 首段一致
- Release 标题、tag 和 `RELEASE_NOTES.md` 是否统一
