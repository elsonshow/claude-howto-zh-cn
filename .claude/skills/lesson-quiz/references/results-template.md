# 结果报告模板（Results Report Template）

这是 Step 5（评分并展示结果）的输出模板。使用时填充方括号里的占位符；标题、表格列和段落结构保持一致，正文用中文说明，关键英文术语保留。

```markdown
## Lesson Quiz Results: [Lesson Name]

**Score: N/10** — [Grade label]
**Quiz timing**: [Before / During / After] the lesson
**Question breakdown**: 概念题正确 N 道，实践题正确 N 道

### 单题结果

| # | 类型 | 问题摘要 | 你的回答 | 结果 |
|---|------|----------|----------|------|
| 1 | Conceptual | [简写问题] | [用户选择] | [Correct / Incorrect] |
| 2 | Practical | ... | ... | ... |
| ... | ... | ... | ... | ... |

### Incorrect Answers — Review These

[每道错题都按下面结构展开：]

**Q[N]: [完整问题]**
- Your answer: [用户选择]
- Correct answer: [正确选项]
- Explanation: [为什么正确]
- Review: [建议回看的 lesson README 具体小节]

### 按测验时机给出的反馈

[如果是 pre-test]:
**Pre-test score: N/10.** 这是学习前基线。重点学习上面错题对应的主题；完成本课后，建议再测一次看提升。

[如果是 during]:
**Progress check: N/10.** 如果 7 分及以上，说明进度不错，可以继续学；如果 4-6 分，先回看错题主题再往后走；如果低于 4 分，建议从本课开头重新梳理。

[如果是 after]:
**Mastery check: N/10.** 如果 9-10 分，说明本课已掌握，可以进入下一课；如果 7-8 分，回看错题主题后重测；如果低于 7 分，建议重点复习上面标出的章节。

### Recommended Next Steps

- [如果已掌握]: 进入路线图里的下一课：[next lesson link]
- [如果基本熟练]: 回看这些具体小节后再测：[list sections]
- [如果仍在 Developing 或更低]: 重新阅读完整 lesson：[lesson link]，重点关注：[list weak categories]
- [Offer]: "Would you like to retake this quiz, try a different lesson, or get help with a specific topic?"
```
