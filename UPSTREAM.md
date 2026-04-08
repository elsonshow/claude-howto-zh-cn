# Upstream & Fork Notes

## 上游来源

- 上游仓库：[`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto)
- 上游分支：`main`
- 本地化基线 commit：`0ca8c37c81918458e063739425c4740ca92c2db2`
- 最近检查到的上游 commit：`561c6cbaa3043aa86f530af75f46ab697304f531`
- 上游许可证：[MIT License](LICENSE)

## 本仓库性质

本仓库是一个 **非官方中文本土化 fork**，目标是面向中国小白用户重写 Claude Code 学习材料，同时尽量保持与上游结构、示例和运行行为兼容。

它不是：

- 官方 Anthropic 文档
- 上游仓库的逐字逐句翻译镜像
- 为中国平台完全重构后的独立产品

## 本仓库做了哪些调整

- 把首页、学习路线、Quick Reference、Catalog 等核心入口文档改成中文主线。
- 用“先讲用途，再讲安装，再讲示例和常见坑”的方式重写表达。
- 保留目录结构、文件路径、命令名、frontmatter key、JSON/YAML key、环境变量、CLI flags 等关键兼容元素。
- 增加中国用户常见障碍说明，例如 GitHub Token、`npm` / `npx` / `uv` / Python 环境、网络与代理、Windows / WSL 差异。
- 增加本地化校验脚本与 CI 护栏，避免翻译把示例和配置改坏。

## 本地化原则

1. **兼容性优先**  
   任何会影响 Claude Code 运行、加载或复制执行的标识，默认不翻。

2. **中文表达优先**  
   给人看的说明文字、学习路径、FAQ、对比表、导语等内容，以中文重写为主。

3. **术语保真**  
   `skills`、`CLI`、`hooks`、`MCP`、`subagents` 这类高频术语保留英文，首次出现补中文解释。

4. **持续同步**  
   本仓库默认采用“跟进上游版本 -> 判定受影响文件 -> 更新中文内容 -> 记录处理结果”的维护方式。

## 推荐同步流程

1. 获取上游新版本或新 commit。
2. 列出上游变更的文件范围。
3. 判断哪些文件影响本仓库的中文文档、示例或校验脚本。
4. 优先同步以下类型的变化：
   - 命令名、字段名、协议名、路径约定
   - 新增或废弃功能
   - 影响复制可运行性的示例变更
5. 更新中文文档后，运行：

```bash
uv run python scripts/validate_localization.py
```

6. 在提交说明或更新日志中记录：
   - 上游变更点
   - 本仓库采取了什么处理
   - 哪些内容暂时未同步

## 最近一次同步记录

### Upstream Sync — 2026-04-08

- Reviewed upstream range: `0ca8c37` → `561c6cb`
- 重点上游变化：
  - 上游在 2026 年 4 月完成一轮更大的文档同步，并发布 `v2.3.0`
  - 新增 `CLAUDE.md`
  - 新增 `04-subagents/performance-optimizer.md`
  - 新增 `06-hooks/pre-tool-check.sh` 与 `06-hooks/dependency-check.sh`
  - 一批 hooks 脚本改为读取 stdin JSON，并补齐 Windows Git Bash 兼容性
  - 文档层面新增 / 修正了 `MCP Apps`、`/ultraplan`、Agent Teams、Channels、`cleanupPeriodDays` 等说明
  - 上游新增 `zh/`、`vi/` 多语言目录，并重构了部分 CI / release 流程
- Chinese fork actions:
  - 将与中文主线直接相关的新增能力和示例同步到根目录中文文档
  - 新增中文 `CLAUDE.md`，适配本仓库自己的校验和本地化工作流
  - 新增 `performance-optimizer` subagent，并更新 `CATALOG.md`
  - 同步高价值 hooks 脚本与新版协议行为
  - 在 `README.md` 中更新最近同步日期与本轮更新说明
  - 未采用上游 `zh/` / `vi/` 目录结构与 README 指标徽章，继续保持“中文主线在根目录”的 fork 结构
### Upstream Sync — 2026-04-01

- Upstream range: `d41b335` → `0ca8c37`
- Affected files:
  - `06-hooks/README.md`
  - `06-hooks/auto-adapt-mode.py`
  - `09-advanced-features/README.md`
  - `09-advanced-features/setup-auto-mode-permissions.py`
  - `README.md`
- Chinese fork actions:
  - 删除旧的 `auto-adapt-mode` hook 文件，不再继续维护“动态记忆批准”方案
  - 新增 `09-advanced-features/setup-auto-mode-permissions.py`，同步上游的一次性权限种子脚本
  - 在中文 `Advanced Features` 和 `Hooks` 文档中补上新的使用方式、适用场景和安全边界
  - 在项目介绍中写明最近同步日期与本次上游更新内容
  - 上游新增的 Trending 徽章未直接照搬，因为它描述的是上游仓库状态，而不是当前中文 fork 的状态

## 建议记录模板

```md
## Upstream Sync - YYYY-MM-DD

- Upstream range: <old>...<new>
- Affected files:
  - README.md
  - 05-mcp/README.md
- Chinese fork actions:
  - 同步了 MCP 章节新增字段说明
  - 保留了命令名与 JSON key 不变
  - 补充了中国用户的安装注意事项
```

## 额外说明

- 如果你未来将本仓库发布到自己的 GitHub 账号下，建议仓库名使用 `claude-howto-zh-cn`。
- 如果需要替换徽章、封面图、仓库 URL，请在保留来源声明的前提下调整。
- 如果某处翻译和可执行性冲突，**优先保留原始标识**，并在正文中补中文解释。
