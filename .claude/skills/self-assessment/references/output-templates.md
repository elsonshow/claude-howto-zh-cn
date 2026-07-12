# 输出模板（Output Templates）

这里保存 assessment results 和 learning path 的空白 Markdown 模板。`SKILL.md` 负责流程与评分，模板文件负责减少主说明里的重复长文本。

## Quick Assessment 结果模板（Step 3A）

```markdown
## Claude Code 自测结果

### 你的等级：Level 1: Beginner / Level 2: Intermediate / Level 3: Advanced

你勾选了 **N/8** 项。

[根据等级给一句具体总结，避免空泛鼓励]

### 你的能力概览

| 能力领域 | 状态 |
|----------|------|
| 基础 CLI 与对话 | [已掌握 / 有短板] |
| CLAUDE.md 与 Memory | [已掌握 / 有短板] |
| Slash Commands（内置命令） | [已掌握 / 有短板] |
| Custom Commands 与 Skills | [已掌握 / 有短板] |
| MCP Servers | [已掌握 / 有短板] |
| Hooks | [已掌握 / 有短板] |
| Subagents | [已掌握 / 有短板] |
| Print Mode 与 CI/CD | [已掌握 / 有短板] |

### 主要短板

[对每个未勾选项，给一行要学什么 + 对应教程链接]

### 你的个性化学习路径

[按 Step 4 输出学习路径]
```

## Deep Assessment 结果模板（Step 3B）

```markdown
## Claude Code 自测结果

### 整体等级：Level 1 / Level 2 / Level 3

**总分：N/19**

[一句基于得分结构的具体总结]

### 你的能力画像

| 功能领域 | 得分 | 掌握程度 | 状态 |
|----------|------|----------|------|
| Slash Commands | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Memory | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Skills | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Hooks | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| MCP | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Subagents | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Checkpoints | N/1 | 未掌握 / 熟练（None / Proficient） | 学习 / 已掌握（Learn / Mastered） |
| Advanced Features | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| Plugins | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |
| CLI | N/2 | 未掌握 / 基础 / 熟练（None / Basic / Proficient） | 学习 / 复习 / 已掌握（Learn / Review / Mastered） |

**掌握程度说明**：0 = None（未掌握），1 = Basic（基础），2 = Proficient（熟练）

### 优势领域

[列出得分满分的主题]

### 优先补齐短板

[列出得分为 0 的主题，并按依赖顺序排列]

### 需要复习的领域

[列出得分为 1 的主题]

### 你的个性化学习路径

[按 Step 4 输出 gap-specific learning path]
```

## 学习路径模板（Step 4）

```markdown
### 你的个性化学习路径

**预计时间**：约 N 小时（已按你当前掌握情况调整）

#### 阶段 1：[阶段名称]（约 N 小时）

**[主题名称]** — [从零学习 / 深入补课]
- 教程：[链接到教程目录]
- 重点关注：[用户需要补的具体章节或概念]
- 关键练习：[一个具体练习]
- 完成标准：[可验证的成功条件]

**[主题名称]** — ...

---

#### 阶段 2：[阶段名称]（约 N 小时）

...

---

### 推荐练习项目

根据你的短板，建议做这些真实小项目来巩固：

1. **[项目名]**：[一句话说明，组合 2-3 个短板主题]
2. **[项目名]**：[一句话说明]
3. **[项目名]**：[一句话说明]
```
