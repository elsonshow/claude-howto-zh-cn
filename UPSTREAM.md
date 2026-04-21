# Upstream & Fork Notes

## 上游来源

- 上游仓库：[`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto)
- 上游分支：`main`
- 最近同步到的上游 commit：`cf92e8e4f8e1e98e2ee26f5c8227f9029e85b2f7`
- 上游版本标签：`v2.1.112`
- 上游许可证：[MIT License](LICENSE)

## 当前结构

本仓库现在采用和上游一致的多语言结构：

- 根目录保持英文主线，尽量与 `upstream/main` 一致。
- `zh/` 目录保存中文版本，用于和英文根目录对照阅读。
- `vi/`、`uk/` 目录跟随上游保留，避免后续同步时反复制造删除差异。
- `LOCALIZATION-STYLE.md` 和本文件是本 fork 的维护说明，不属于上游主线内容。

这次调整替代了早期“根目录中文主线”的维护方式。后续同步时，优先保证英文根目录能干净跟进上游，再检查 `zh/` 目录是否需要补齐中文表达或链接入口。

## 本仓库性质

本仓库是一个非官方中文对照 fork，目标是让中文用户可以对照英文原文学习 Claude Code，同时尽量保持上游示例、脚本、目录结构和运行行为一致。

它不是：

- 官方 Anthropic 文档
- 上游仓库的独立重写版本
- 为中国平台完全重构后的独立产品

## 本地化原则

1. **英文主线先同步**
   根目录文档、脚本、CI 和资源文件默认跟随 `upstream/main`，避免中英内容混杂。

2. **中文对照放在 `zh/`**
   中文版本集中维护在 `zh/`，尽量与英文路径一一对应，方便用户在英文原文和中文说明之间切换。

3. **运行标识不翻译**
   目录名、文件名、frontmatter key、JSON/YAML key、CLI flags、环境变量、slash command 名称、skill/subagent/plugin 名称默认保持英文。

4. **中文表达可以本土化**
   说明性文字、学习路线、FAQ、导读和常见坑可以按中文用户习惯改写，但不能改坏可复制运行的示例。

## 推荐同步流程

1. `git fetch --all --prune`
2. 合并 `upstream/main` 到本 fork 的 `main`。
3. 对上游已存在的文件，优先恢复为 `upstream/main` 内容，避免自动合并造成中英文段落混杂。
4. 检查 `README.md` 和 `zh/README.md` 的语言入口。
5. 检查 `zh/` 是否和英文根目录保持可对照结构。
6. 运行本仓库可用的校验命令，至少包括：

```bash
git diff --check
python -m pytest scripts/tests/test_build_epub.py
```

如继续维护本 fork 的旧本地化校验脚本，也可以额外运行：

```bash
uv run python scripts/validate_localization.py
```

## 最近一次同步记录

### Upstream Sync - 2026-04-21

- Reviewed upstream range: `9c224ff` -> `cf92e8e`
- 重点上游变化：
  - 上游发布 `v2.1.112`
  - 同步 Claude Code `v2.1.110` 相关文档更新
  - 根目录 README 保持英文主线，并提供 English / Vietnamese / Chinese / Ukrainian 语言入口
  - 上游已经维护 `zh/` 中文目录
- Chinese fork actions:
  - 合并 `upstream/main`
  - 将上游已有文件恢复为英文主线内容
  - 保留 `zh/` 作为中文对照目录
  - 在中文 README 顶部补充语言切换入口，方便从中文版本返回英文原文
  - 更新本文件和 `LOCALIZATION-STYLE.md`，记录新的中英文对照维护策略

### Earlier Sync History

本 fork 早期曾使用“根目录中文主线”的方式维护，并手工同步过 2026-04-01、2026-04-08、2026-04-14 的上游变化。自 2026-04-21 起，维护策略改为“英文根目录 + `zh/` 中文对照目录”，以降低后续与上游合并时的冲突和混排风险。

## 额外说明

- 如果 GitHub About 仍强调中文版本，建议描述为“Claude Code 中文对照指南，基于 luongnv89/claude-howto 同步维护”。
- 如果需要补充中国用户常见安装、网络或环境说明，优先放在 `zh/` 对应文档里。
- 如果某处翻译和可执行性冲突，优先保留原始标识，并在中文正文中补充解释。
