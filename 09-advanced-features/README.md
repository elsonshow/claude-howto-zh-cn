<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Advanced Features 指南

当你已经会用 slash commands、memory、skills、MCP、hooks 和 subagents 之后，Claude Code 的高级能力会决定你能不能把它真正用到复杂项目和高自动化工作流里。

这部分不是“你必须一口气全会”，而是你要知道：

- 哪些高级能力最值得先学
- 哪些适合日常开发
- 哪些适合团队和自动化
- 哪些不该在没准备好的情况下乱开

---

## 这部分包含什么

主要包括：

- planning mode
- extended thinking
- Auto Mode
- background tasks
- scheduled tasks
- permission modes
- print mode / headless usage
- session management
- remote / desktop / web sessions
- worktrees
- sandboxing
- configuration

---

## 最推荐先掌握的四项

### 1. planning mode

复杂任务先规划再执行。

### 2. permission modes

明确 Claude 在本地到底能做多少事。

### 3. print mode

把 Claude Code 接进脚本、CI/CD 和自动化流程的关键入口。

### 4. background tasks

让耗时任务后台跑，不阻塞当前会话。

如果你不是重度用户，先掌握这四个就足够产生明显收益。

---

## planning mode

### planning mode 是什么

它是“两阶段工作流”：

1. 先做计划
2. 再按计划执行

适合：

- 多文件重构
- 新功能设计
- 架构调整
- 数据迁移
- 高风险变更

不太适合：

- 小 bug
- 单文件轻改
- 只问一个简单问题

### 常见入口

```text
/plan Implement user authentication system
```

也可以通过权限模式进入只读规划状态：

```bash
claude --permission-mode plan
```

### 一个好的 planning mode 输出应该包含什么

- 分阶段计划
- 预计会改哪些文件
- 风险点
- 验证方式
- 用户需要确认的地方

如果 planning mode 只给你几句空话，那不是好计划。

---

## extended thinking

extended thinking 的价值在于：让 Claude 对复杂问题多想一步，而不是急着下结论。

它特别适合：

- 架构对比
- 技术选型
- 高歧义问题
- 边界条件分析

对中国用户来说，一个实用理解是：  
**不是所有问题都要更长思考，但复杂问题最好别让 Claude 秒答。**

---

## Auto Mode

Auto Mode 属于更偏自动化、也更需要谨慎的能力。

它适合：

- 明确受控的自动化环境
- 已经知道自己在放开什么权限
- 你对项目风险边界比较清楚

它不适合：

- 你还没搞清 permission modes 差异
- 你还不确定项目里哪些操作是危险的

新手建议先不要把 Auto Mode 作为默认。

---

## permission modes

permission modes 决定 Claude 在本地能做什么，以及什么时候会请求你确认。

### 常见模式

- `default`
- `acceptEdits`
- `plan`
- `dontAsk`
- `bypassPermissions`
- `auto`

### 如何理解

| 模式 | 适合什么 |
|------|----------|
| `default` | 日常安全使用 |
| `acceptEdits` | 希望编辑流畅一些 |
| `plan` | 只想分析，不想改 |
| `dontAsk` | 非交互脚本 |
| `bypassPermissions` | 可信环境中的强自动化 |
| `auto` | 有更高自动化诉求、且明确接受风险 |

### 一个常见误区

很多人以为权限模式只是“麻烦不麻烦”。  
其实它决定的是：

- 风险控制
- 自动化强度
- 你是否还能及时拦住错误操作

---

## print mode / headless usage

`claude -p` 是 Claude Code 进入自动化世界的关键入口。

适合：

- shell 脚本
- CI/CD
- 一次性任务
- 管道输入
- 结构化输出

例如：

```bash
claude -p "Run tests and summarize failures"
cat error.log | claude -p "Explain this error"
```

### print mode 使用建议

- 任务尽量清晰明确
- 一开始先用小任务试
- 不要直接上高权限全自动流程
- 需要 JSON 输出时，先确认消费端怎么解析

---

## background tasks 与 scheduled tasks

### background tasks

适合：

- 长时间运行的任务
- 不想阻塞当前对话
- 需要并行推进的工作

### scheduled tasks

适合：

- 周期性检查
- 定时重复 prompt
- 简单提醒或轮询式任务

如果你还没掌握 print mode 和权限模式，先别急着把 scheduled tasks 做复杂。

---

## session management

session 管理能力在任务复杂后会非常重要。

高频场景：

- 恢复之前的工作
- 给当前任务命名
- 从当前 session 分叉实验

常见操作：

- `/resume`
- `/rename`
- `/branch`（较新的主名称，部分环境中 `/fork` 仍可能作为兼容别名出现）
- `claude -c`
- `claude -r "session-name"`

如果你不命名 session，后期会越来越难管理。

---

## remote / web / desktop

这些能力适合：

- 在多台机器间切换
- 在本地和云端之间接力
- 用 desktop 做更好的可视化 diff 或会话管理

对于新手，先知道它们存在即可。  
真正要用时，再重点看网络和权限环境。

---

## worktrees

worktrees 特别适合：

- 多分支并行方案
- 大任务拆成多个实验方向
- 和 planning mode / agent workflows 配合

如果你已经开始同时试两三种实现路线，worktrees 会非常有价值。

---

## sandboxing

sandboxing 的核心不是“更麻烦”，而是“更安全地控制 Claude 的能力范围”。

适合：

- 风险敏感环境
- 企业环境
- 希望限制文件系统或网络访问

不适合：

- 你还没搞清当前工具链本身怎么跑

---

## configuration 与环境变量

高级能力很多都会回到配置层，例如：

- permission mode
- thinking effort
- channels
- auto mode
- plugins
- MCP

所以你最终还是会需要理解：

- settings 文件
- CLI flags
- 环境变量

如果你想长期高效使用 Claude Code，这一步绕不过去。

---

## 中国用户特别注意

### 1. 自动化前先看网络

如果你要用：

- `claude -p`
- remote / web / desktop
- MCP
- plugins

先确认：

- API 访问
- GitHub 连通性
- npm / uv / Python 依赖下载
- 公司代理和证书环境

### 2. 先理解权限，再追求自动化

很多人会一开始就想“全自动”，但权限模式没搞清时，这很容易出事。

### 3. Windows / WSL 差异要提前确认

高级特性里很多命令和脚本默认更贴近 Unix 生态。

---

## 常见坑

### 1. 把 advanced features 全当成“酷炫功能”

它们本质上是控制力、风险边界和自动化能力，不只是花哨选项。

### 2. 还没理解权限就开高自动化

这会让“让 Claude 帮忙”很快变成“让 Claude 瞎动”。

### 3. print mode 用得太重太快

建议从日志解释、测试摘要、静态分析这种低风险任务开始。

### 4. session 不命名

长任务一多，后面很难找回。

---

## Troubleshooting

如果高级功能“看起来有、实际上跑不起来”，优先检查：

1. 权限模式是否合适
2. 当前命令是否应该用交互模式还是 print mode
3. 环境变量是否齐全
4. 远程或外部服务是否可访问
5. 当前是否受网络、代理、公司策略影响

---

## Best Practices

- 先掌握 planning mode、permission modes、print mode、background tasks
- 先小范围试自动化，再逐渐放权
- 高风险任务优先用 plan / checkpoints / worktrees 保护自己
- 中国用户优先排除网络和 shell 环境问题

---

## 推荐下一步

- 想把高级能力接进脚本：看 [10-cli](../10-cli/)
- 想打包团队工作流：看 [07-plugins](../07-plugins/)
- 想理解 checkpoint 和安全试错：看 [08-checkpoints](../08-checkpoints/)
