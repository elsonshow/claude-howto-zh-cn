# Checkpoint Examples

下面是一些更贴近真实工作的 checkpoint 用法示例。

> 注意：checkpoints 默认会自动创建。你不需要手动保存，只需要在需要时用 `Esc+Esc` 或 `/rewind` 回退。

## Example 1: 数据库迁移方案对比

- 先尝试直接迁移
- 测试失败后回退
- 再尝试 dual-write 方案
- 对比两种策略后选择更稳妥的实现

## Example 2: 性能优化实验

- 基线 checkpoint
- 尝试缓存
- 回退
- 尝试查询优化
- 再组合方案

## Example 3: UI 方案迭代

- 保存起始状态
- 试 sidebar
- 回退
- 试 top nav
- 回退
- 试 card grid
- 最后组合最佳方案

## Example 4: 调试假设切换

- 锁定一个 bug
- 试第一种假设
- 不成立就回退
- 换第二种假设
- 直到找到根因

## Example 5: API 设计演进

- 从 REST 方案开始
- 回退后切到 GraphQL 方案
- 再比较哪种更适合当前项目
