<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation 插件

用于把 API 文档、README 生成、文档同步和文档校验打包成一套方案。

## Features

- API 文档生成
- README 创建与更新
- 文档同步
- 代码注释改进
- 示例生成

## Installation

```bash
/plugin install documentation
```

## What's Included

### Commands

- `/generate-api-docs`
- `/generate-readme`
- `/sync-docs`
- `/validate-docs`

### Agents

- `api-documenter`
- `code-commentator`
- `example-generator`

## 适合什么项目

- API 或 SDK 项目
- README 常年落后的项目
- 示例代码和实际实现经常不同步的项目

## 最小使用流程

### 1. 安装 plugin

```text
/plugin install documentation
```

### 2. 从一个具体入口开始

例如：

```text
/generate-api-docs
```

或者：

```text
/generate-readme
```

### 3. Claude 通常会做什么

1. 扫描代码结构
2. 分配给相关文档 agents
3. 生成或更新文档
4. 检查链接、示例与结构是否一致

## 常见坑

### 1. 以为它能自动理解一切上下文

如果代码结构混乱、注释缺失，这个 plugin 也需要更多人工引导。

### 2. 文档生成后不做验证

生成不等于正确，最好配合 `/validate-docs` 使用。

### 3. 只更新 README，不更新 API 文档

文档类 plugin 的核心价值之一，就是帮助你保持多个文档入口的一致性。
