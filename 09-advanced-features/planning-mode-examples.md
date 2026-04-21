# Planning Mode 示例

这里给一些 planning mode 的典型用法示例，帮助你理解什么时候值得先规划再执行。

## Example 1: 构建 REST API

使用 `/plan` 后，Claude 应该先输出：

- 分阶段计划
- 需要创建哪些文件
- 核心技术选型
- 风险点
- 预计工作量

而不是直接开始写代码。

## Example 2: 数据库迁移

面对 MongoDB → PostgreSQL 这类高风险任务，planning mode 应该先明确：

- 分阶段迁移策略
- dual-write / rollback 方案
- 数据一致性检查
- cutover 节点

## Example 3: 前端大规模重构

例如 class components → hooks，规划里应该先给：

- 组件盘点
- 复杂度分级
- 迁移顺序
- 测试与回退策略
