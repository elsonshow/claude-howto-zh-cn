<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation 插件

这是一个把部署、回滚、状态检查和 incident 响应打包到一起的 DevOps plugin。

## 功能

- 自动部署
- 回滚流程
- 系统健康检查
- incident 响应
- Kubernetes 集成

## 安装

```bash
/plugin install devops-automation
```

## 包含内容

### 命令

- `/deploy`
- `/rollback`
- `/status`
- `/incident`

### 代理

- `deployment-specialist`
- `incident-commander`
- `alert-analyzer`

## 前置要求

- `kubectl`
- 已配置集群访问
- 必要时设置 `KUBECONFIG`

## 最小配置

```bash
export KUBECONFIG=~/.kube/config
kubectl get pods
```

在真正使用 plugin 前，最好先确认 `kubectl` 本身可用、目标集群可连。

## 一个最小使用流程

### 1. 安装 plugin

```text
/plugin install devops-automation
```

### 2. 先从只读状态检查开始

```text
/status
```

### 3. 再尝试更高风险操作

```text
/deploy staging
```

或：

```text
/rollback production
```

## 使用建议

- 先用 `/status` 验证环境
- 再用 staging 做演练
- 最后才考虑 production 级命令

## 常见坑

### 1. 本地 `kubectl` 没配好

插件本身没问题，但底层依赖没通，就会显得“命令无效”。

### 2. 直接在 production 场景试第一把

这不是一个适合“第一次就直接上线试”的 plugin。

### 3. 没写清团队流程

如果团队内部的部署规范、回滚条件、incident 流程不明确，plugin 也很难替你兜底。
