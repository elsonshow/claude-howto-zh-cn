# Upstream & Fork Notes

## 上游来源

- 上游仓库：[`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto)
- 上游分支：`main`
- 本地化基线 commit：`d41b335cbc40832d83656184c5a67ca4952bad4f`
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
