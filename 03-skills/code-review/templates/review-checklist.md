# Code Review Checklist / 审查清单

## Security Checklist

- [ ] 没有硬编码 secrets
- [ ] 所有用户输入都有校验
- [ ] 避免 SQL injection
- [ ] 状态修改接口有 CSRF 保护（如适用）
- [ ] 有 XSS 防护
- [ ] 受保护接口有鉴权检查

## Performance Checklist

- [ ] 没有明显 O(n²) 热路径
- [ ] 避免 N+1 查询
- [ ] 缓存策略合理
- [ ] 没有明显内存浪费

## Quality Checklist

- [ ] 命名清晰
- [ ] 函数职责单一
- [ ] 没有明显重复代码
- [ ] 关键逻辑有足够测试
