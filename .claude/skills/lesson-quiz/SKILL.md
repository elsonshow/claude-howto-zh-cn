---
name: lesson-quiz
version: 1.1.0
description: 针对单个 Claude Code tutorial lesson（01-10）进行 10 题互动测验，评分并标出薄弱点。Use when asked to "quiz me on hooks", "test my knowledge of lesson 3", "lesson quiz", "practice quiz for MCP", "do I understand skills", or similar Chinese requests.
effort: high
metadata:
  author: Luong NGUYEN
---

# 课程测验（Lesson Quiz）

这是一个针对单个 Claude Code lesson 的完整互动测验 skill，用于检查用户对某一课的理解程度。它只测一个 lesson，不用于整套教程的水平评估；整套评估请使用 `self-assessment`。

## 前置条件与护栏

本 skill 需要能读取教程仓库中的 `01-slash-commands/` 到 `10-cli/` 目录，以及本 skill 自带的 `references/question-bank.md`。

- 先确认目标 lesson 的 `README.md` 存在；如果不存在，停止并提醒用户检查仓库结构。
- **不要临时编题。** 只使用 `references/question-bank.md` 中该 lesson 的预置题；如果题库缺失，直接说明并停止。
- **准确计分。** 每题选项会随机打乱，必须记录正确选项在打乱后的新位置，再据此判分。
- **先确认测验时机。** `Before` / `During` / `After` 会影响结果解释，不能跳过。

## 使用说明

### Step 1: 确认 lesson

如果用户提供了参数，就映射到 lesson 目录：

- `01` / `slash-commands` / `commands` → `01-slash-commands`
- `02` / `memory` → `02-memory`
- `03` / `skills` → `03-skills`
- `04` / `subagents` / `agents` → `04-subagents`
- `05` / `mcp` → `05-mcp`
- `06` / `hooks` → `06-hooks`
- `07` / `plugins` → `07-plugins`
- `08` / `checkpoints` / `checkpoint` → `08-checkpoints`
- `09` / `advanced` / `advanced-features` → `09-advanced-features`
- `10` / `cli` → `10-cli`

如果用户没提供参数，使用 AskUserQuestion 分 2-3 轮让用户选择 lesson。

---

### Step 2: 读取 lesson 与题库

先读取：

- `<lesson-directory>/README.md`
- `references/question-bank.md`

只读取当前选中 lesson 的 `README.md`，不要为了测一个 lesson 一次性加载全部 10 个 lesson。题库中每个 lesson 应有 10 道预置题；如果该 lesson 题目不足，停止并报告题库需要维护，不要根据 README 临时补题。

---

### Step 3: 询问测验时机

用 AskUserQuestion 询问用户当前是在：

1. `Before (pre-test)`
2. `During (progress check)`
3. `After (mastery check)`

不同 timing 会影响结果解读。

---

### Step 4: 出题

- 每次固定 10 题
- 每轮 2 题，共 5 轮
- 混合概念题和实践题
- 每题使用 AskUserQuestion，提供 3-4 个选项
- 每轮用户答完后，立即给出本轮逐题反馈：是否答对；如果答错，给出正确答案和简短解释
- 每题展示前必须随机打乱选项顺序，不要照搬题库里的 A/B/C/D 顺序，也不要固定把正确答案放在第一项
- 打乱后要记录正确答案对应的新位置，最终评分按打乱后的真实答案判定

每题必须包含这些信息：

- `category`
- `question`
- `options`
- `correct`
- `explanation`
- `review`

记录用户答案；每轮反馈不替代最终结果，所有 4 轮结束后仍要统一评分。

---

### Step 5: 评分与结果输出

每题答对记 1 分，总分 10 分。

等级：

- 9-10：Mastered
- 7-8：Proficient
- 5-6：Developing
- 3-4：Beginning
- 0-2：Not yet

输出格式使用 `references/results-template.md`。填充模板里的占位符，保留分数行、单题结果表、错题复盘、按时机给出的反馈和推荐下一步。

---

### Step 6: 根据 timing 解释结果

#### 如果是学前测验

- 把成绩解释为“学习前基线”
- 强调用户接下来应重点关注哪些主题

#### 如果是学习中检查

- 把成绩解释为“阶段性进度检查”
- 明确哪些点已经掌握、哪些点要补

#### 如果是学后测验

- 把成绩解释为“lesson mastery check（课程掌握度检查）”
- 如果分数高，建议进入下一课
- 如果分数一般，列出明确回看点

---

### Step 7: 提供后续动作

最后再用 AskUserQuestion 让用户选择：

1. `Retake this quiz`
2. `Quiz another lesson`
3. `Explain a topic I missed`
4. `Done`

如果选第三项，先问错题编号，再读取该 lesson README 的相关部分，用中文解释并给例子。

## 验收标准

一次完整测验必须满足：

- 已解析且只解析了一个 lesson（01-10）
- 已通过 AskUserQuestion 获取 `Before` / `During` / `After` 测验时机
- 已从 `references/question-bank.md` 取出该 lesson 的 10 道题
- 已按 5 轮、每轮 2 题展示，并对每题选项随机打乱
- 已按打乱后的真实正确位置计分，最终分数为 0-10 的整数
- 最终报告包含 `Score: N/10`、10 行单题结果、每道错题的正确答案与复习建议
- 已提供 `Retake this quiz` / `Quiz another lesson` / `Explain a topic I missed` / `Done` 后续选择

## 边界情况

- 无效 lesson 参数：展示可用 lesson 列表并让用户重新选择。
- 用户中途退出：给出已答题目的部分结果，分母用已答题数，不要写成 10 分满分。
- 目标 `README.md` 不存在：停止并提示检查仓库结构。
- 题库缺失：停止并说明缺少该 lesson 的题目，不要编造题目。

## 输出要求

- 中文表达清晰
- 保留关键英文术语
- 错题解释必须具体
- 复习建议要明确到 lesson 或章节
- 不要把测验做成泛泛聊天
