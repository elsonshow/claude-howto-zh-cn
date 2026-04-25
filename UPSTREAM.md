# 上游与 Fork 说明

## 上游来源

- 上游仓库：[`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto)
- 上游分支：`main`
- 本地化基线 commit：`0ca8c37c81918458e063739425c4740ca92c2db2`
- 最近检查到的上游 commit：`eff5bd29d52cb62461bd76d69468825b1f38f2e4`
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

### 上游同步 — 2026-04-25

- Reviewed upstream range: `d17d515` → `eff5bd2`
- 重点上游变化：
  - 修复 `security-reviewer` agent 中无效的 `diff` 工具配置，改为 `bash`
  - 新增 `scripts/check_cross_references.py` 的 repo-root 边界处理
  - 新增 `scripts/tests/test_check_cross_references.py` 覆盖该脚本边界场景
  - 将 `scripts/requirements.txt` 固定到已验证版本
- Chinese fork actions:
  - 把 agent 工具修正同步到中文仓库
  - 引入交叉引用检查脚本和测试，并修正中文仓库现有断锚，确保脚本能本地通过
  - 固定脚本依赖版本，减少环境差异导致的校验波动
  - 保持中文根目录主线，不引入上游多语言目录结构

### 上游同步 — 2026-04-24

- Reviewed upstream range: `cf92e8e` → `d17d515`
- 重点上游变化：
  - 上游同步到 Claude Code `v2.1.119`
  - slash commands 补充 `/cost` / `/stats` / `/usage` 的新关系，以及 `/doctor`、`/theme`、`/btw` 的新版说明
  - hooks 补充 `mcp_tool`、28 个事件、`duration_ms`、PowerShell auto-approve
  - CLI / advanced features 补充 native binary、docs host 迁移、Opus 4.7 细节、Auto Mode 与 settings 新行为
  - skills / memory / subagents / checkpoints / plugins 文档补充一批配置与行为说明
- Chinese fork actions:
  - 只把影响中文用户理解和实际使用的变化同步到中文根目录主线
  - 保持中文默认入口，不采用上游英文 README 和多语言目录结构
  - 对新增配置和命令做中文解释，同时保留可执行标识原样
  - 本地化校验与测试通过后再推送到 origin/main

### 上游同步 — 2026-04-22

- Reviewed upstream range: `9c224ff` → `cf92e8e`
- 重点上游变化：
  - 上游同步到 Claude Code `v2.1.110` / `v2.1.112`
  - 新增或明确 `/tui`、`/focus`、`/recap`、`/undo`、`/proactive`、`/ultrareview`、`/less-permission-prompts`
  - advanced features 补充了 TUI、session recap、push notifications、Auto Mode 新访问方式
  - CLI / docs 切到 Opus 4.7，并引入 `xhigh` effort
  - plugins 章节新增 background monitors 说明
- Chinese fork actions:
  - 把本轮新增能力同步到中文根目录主线文档
  - 保留中文默认入口，不采用上游英文 README 和 `uk/` / `zh/` 目录结构
  - 更新本地化校验，拦截明显未翻译的英文标题和英文模板段落

### 上游同步 — 2026-04-14

- Reviewed upstream range: `561c6cb` → `9c224ff`
- 重点上游变化：
  - 上游把 `# ...` inline memory 快捷写法标记为 discontinued，推荐改用 `/memory` 或自然语言记忆请求
  - `05-mcp/README.md` 不再继续强调 `WebSocket transport`
  - 新增 `/team-onboarding` 命令说明，并扩充了 `/ultraplan` 的云端起草细节
  - `Monitor Tool` 被明确写进 advanced features，用于替代低效轮询
  - `06-hooks/pre-tool-check.sh` 修复了 block reason 输出和 `rm -rf /tmp/...` 误拦截问题
  - README 补充了乌克兰语入口，但这属于上游多语言分发层变化
- Chinese fork actions:
  - 更新中文 `memory` 文档，移除对 `# ...` 快捷写法的继续推荐
  - 删除中文 `MCP` 文档里已经过时的 `WebSocket transport` 说明
  - 在中文命令目录、Catalog、Quick Reference 中补上 `/team-onboarding`、`/ultraplan` 与 `Monitor Tool`
  - 同步 `pre-tool-check.sh` 的上游修复，并新增回归测试覆盖 block/warn 行为
  - 保持根目录中文主线结构，不引入上游 `uk/` 目录和 README 语言切换入口

### 上游同步 — 2026-04-08

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
### 上游同步 — 2026-04-01

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
## 上游同步 - YYYY-MM-DD

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
