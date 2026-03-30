<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Memory 指南

memory 是 Claude Code 中最容易被低估的一项能力。很多人觉得自己只是“加了个 `CLAUDE.md`”，实际上它影响的是 Claude 在每次进入项目时会自动带上的长期上下文。

---

## memory 是什么

Claude Code 的 memory 主要依赖文件系统中的 `CLAUDE.md` 体系。你可以把它理解成：

- 项目规则入口
- 团队约定入口
- 个人偏好入口
- 某个目录下的局部规则入口

它和“当前对话里的临时上下文”不同，memory 更像是长期生效的规则层。

---

## 什么时候最该先配 memory

以下情况非常值得先配 `CLAUDE.md`：

- 你每次都要重复告诉 Claude 代码风格
- 团队里有固定约定，例如测试要求、命名规范、Git 流程
- 项目目录复杂，希望 Claude 一进来就知道哪些目录干什么
- 你想把一部分项目知识长期保存下来，而不是每次重新解释

---

## 高价值命令

| 命令 / 写法 | 用途 |
|-------------|------|
| `/init` | 初始化项目 memory |
| `/memory` | 查看或编辑 memory |
| `# your rule` | 快速把一句规则写进 memory |
| `# remember this` | 用自然语言追加记忆 |
| `@README.md` | 在 `CLAUDE.md` 中引用外部文档 |

---

## 最快上手方式

### 方法 1：直接复制项目模板

```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
```

### 方法 2：让 Claude 帮你初始化

```text
/init
```

这通常适合新项目起步时使用。

### 方法 3：对话中快速写入一条规则

```text
# Always run tests before commit
```

---

## 常见 memory 类型

### 项目级 memory

位置通常是：

- `./CLAUDE.md`
- 或 `.claude/CLAUDE.md`

适合放：

- 项目背景
- 目录结构
- 技术栈
- 代码规范
- 测试规则
- 提交和 PR 规范

### 个人级 memory

位置通常是：

- `~/.claude/CLAUDE.md`

适合放：

- 你的个人编码偏好
- 你习惯的回答风格
- 常用工具和命令约定

### 目录级 memory

适合大型项目或 monorepo，在局部目录下放更细粒度规则。

---

## 写什么最有价值

新手最容易把 `CLAUDE.md` 写成“泛泛而谈的项目介绍”，这价值并不大。更推荐写这些：

- 哪些目录最重要
- 哪些规则最容易被忽略
- 提交前必须做什么
- 哪些工具是本项目默认用法
- 哪些文件不要乱动
- 测试和验证的最低标准

---

## 一个适合小白的最小模板

```md
# Project Memory

## Project Overview
- This is a TypeScript web application.

## Development Rules
- Run tests before commit.
- Prefer async/await.
- Keep API changes documented.

## Important Paths
- `src/` main application code
- `tests/` automated tests
- `docs/` documentation
```

---

## 哪些内容不适合写进 memory

- 过长、每次都不一定相关的大段背景知识
- 会频繁变化的实时数据
- 明显更适合做成 skill 或 hook 的工作流细节
- 会影响运行的命令名或配置 key 的中文重命名

如果你发现某段内容更像“流程模板”，通常更适合去做 skill，而不是塞进 `CLAUDE.md`。

---

## 中国用户特别注意

- 如果你在 Windows 上工作，路径规则和 shell 说明最好明确写清楚。
- 如果项目依赖 `uv`、`npm`、`pnpm`、`bun` 等特定工具，也建议写入 memory。
- 如果项目所在团队有 GitHub、内网、代理、镜像源要求，也值得写在 memory 里。

---

## 常见坑

### 1. 以为 memory 越长越好

不是。memory 要优先放高价值、长期稳定、对 Claude 行为影响大的规则。

### 2. 把项目规则和个人偏好全混在一起

推荐区分项目级和个人级，这样更方便团队协作。

### 3. 让 `CLAUDE.md` 和实际仓库脱节

如果项目目录或规范已经变了，要及时更新 memory，否则 Claude 会学到过期规则。

---

## 推荐下一步

- 想做可复用工作流：看 [03-skills](../03-skills/)
- 想安全试错：看 [08-checkpoints](../08-checkpoints/)
- 想看完整学习顺序：看 [LEARNING-ROADMAP.md](../LEARNING-ROADMAP.md)
