---
name: blog-draft
description: 根据想法和资料起草博客文章。Use when users want to draft a blog post, write an article from research, or turn notes/resources into a structured post.
---

# Blog Draft / 博客草稿生成

## 用户输入

```text
$ARGUMENTS
```

用户最好提供：

- 主题 / 想法
- 参考资料（URL、文件、笔记）
- 目标读者
- 语气风格

如果用户是在修改已有草稿，直接从“迭代草稿”阶段开始。

## 执行流程

### Step 1: 创建文章目录

目录格式：

```text
blog-posts/
└── YYYY-MM-DD-short-topic-name/
    └── resources/
```

### Step 2: 整理资料

对每个资料生成摘要文件，至少包含：

- 关键观点
- 可引用的数据或句子
- 与主题的关联

### Step 3: 明确文章方向

整理并向用户确认：

- 主要观点
- 可选角度
- 核心论点
- 信息缺口

### Step 4: 先产出大纲

生成 `OUTLINE.md`，包含：

- 目标读者
- 语气
- 目标篇幅
- 核心 takeaway
- 文章结构
- 计划引用的资料

### Step 5: 写草稿

按大纲生成 `draft-v0.1.md`，要求：

- 有吸引人的开头
- 结构清晰
- 有证据和例子
- 重要事实带引用
- 结尾有总结或行动建议

### Step 6: 迭代

如果用户要求修改：

- 记录反馈
- 递增版本号
- 保存为 `draft-v0.2.md`、`draft-v0.3.md`

## 输出要求

- 先给结构，再写全文
- 引用要清楚
- 表达可以中文化，但文件和目录命名保持可管理
