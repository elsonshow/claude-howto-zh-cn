<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review 插件

把安全检查、测试检查、性能检查和 PR 审查打包成一套工作流。

## 功能

- 安全分析
- 测试覆盖检查
- 文档检查
- 代码质量审查
- 性能影响分析

## 安装

```bash
/plugin install pr-review
```

## 包含内容

### 命令

- `/review-pr`
- `/check-security`
- `/check-tests`

### 代理

- `security-reviewer`
- `test-checker`
- `performance-analyzer`

## 前置要求

- Git 仓库
- GitHub 访问
- 必要时设置 `GITHUB_TOKEN`

## 最小配置

```bash
export GITHUB_TOKEN="your_github_token"
```

如果你当前机器无法稳定访问 GitHub，这个 plugin 的体验会明显受影响。

## 一个最小使用流程

### 1. 安装 plugin

```text
/plugin install pr-review
```

### 2. 在代码改动或 PR 场景中执行

```text
/review-pr
```

### 3. Claude 通常会做什么

1. 收集当前改动或 PR 上下文
2. 分别调用安全、测试、性能相关 agents
3. 汇总问题并输出优先级建议

## 什么时候最适合用

- 发 PR 前做一次结构化审查
- 你怀疑改动对安全或测试有影响
- 团队想形成相对固定的审查模板

## 常见坑

### 1. 没有 `GITHUB_TOKEN`

如果你的流程依赖 GitHub 数据，这会直接影响插件能力。

### 2. 以为它会替代人工 review

这个 plugin 更适合作为结构化预审查，而不是替代所有人工判断。

### 3. 当前目录不是 Git 仓库

很多审查能力都默认建立在 Git 工作流之上。
