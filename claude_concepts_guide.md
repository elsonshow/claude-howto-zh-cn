# Claude Code 概念总览

这个文件用于把仓库里最容易混淆的几个核心概念放在一起解释。

## 1. Slash Commands

用户主动输入的快捷命令，适合显式触发某个动作。

## 2. Memory

长期自动加载的上下文，适合放项目规则和个人偏好。

## 3. Skills

可复用、可自动触发的能力，适合沉淀稳定工作流。

## 4. Subagents

用于复杂任务拆分和专业分工的子代理。

## 5. MCP

让 Claude 连接外部工具和实时数据的协议。

## 6. Hooks

在特定事件上自动执行动作的机制。

## 7. Plugins

把 commands、skills、MCP、hooks、subagents 打包成整套方案。

## 8. Checkpoints

用于安全试错和回退。

## 9. CLI

Claude Code 的核心使用入口，也是自动化、脚本化和 CI/CD 的关键接口。
