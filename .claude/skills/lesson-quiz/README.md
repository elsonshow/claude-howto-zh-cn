# Lesson Quiz

> 针对单个 Claude Code lesson 的互动测验 skill。它不只是随便出几道题，而是会按 lesson 组织题面、给出评分、错题解释、复习建议和后续动作。

## Highlights

- 每次固定 8 题
- 覆盖 10 个 lesson
- 支持学前、学中、学后三种测验时机
- 每道错题都会给出解释和建议回看的章节
- 会给出总分、等级判断和下一步建议

## 什么时候用

| 你可以这样说 | 它会做什么 |
|---|---|
| “帮我测一下 hooks” | 做一轮 `06-hooks` 相关测验 |
| “我会不会 MCP” | 测 `05-mcp` 的理解程度 |
| “来个 lesson quiz” | 让你先选 lesson，再开始测 |
| “测试我对 skills 的理解” | 直接进入 `03-skills` 测验 |

## 使用方式

```text
/lesson-quiz [lesson-name-or-number]
```

例如：

```text
/lesson-quiz hooks
/lesson-quiz 03
/lesson-quiz advanced-features
/lesson-quiz
```

## 输出内容

### 1. 总分与等级

- 例如 `7/8 — Proficient`

### 2. 每题结果

- 哪些答对
- 哪些答错
- 概念题 / 实践题表现如何

### 3. 错题解释

对每个答错的问题，给出：

- 你选了什么
- 正确答案是什么
- 为什么正确答案更合理
- 建议回看 lesson 的哪一节

### 4. 后续动作

测完后可以继续：

- 重测当前 lesson
- 切到另一课
- 让 Claude 详细解释某道错题
