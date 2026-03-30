# 我的开发偏好

## About Me

- **Experience Level**: 8 年全栈开发经验
- **Preferred Languages**: TypeScript、Python
- **Communication Style**: 直接、清晰、带例子
- **Learning Style**: 喜欢图示和代码结合

## Code Preferences

### Error Handling

偏好显式错误处理，尽量使用清晰的 `try-catch` 和有意义的错误信息。  
避免过于泛化的错误；排查时尽量保留日志上下文。

### Comments

注释优先解释 **WHY**，不要只是重复代码在做什么。  
更适合解释业务逻辑或不明显的决策。

### Testing

偏好 TDD。  
尽量先写测试，再实现。  
测试关注行为，而不是实现细节。

### Architecture

偏好模块化、低耦合设计。  
重视可测试性和职责分离。

## Debugging Preferences

- `console.log` 建议带 `[DEBUG]` 前缀
- 日志包含函数名和关键变量
- 能给 stack trace 时尽量给
- 日志里尽量保留时间戳

## Communication

- 复杂概念先给例子再讲理论
- 需要时提供 before / after 代码片段
- 长回答最后给一个简要总结

## Project Organization

我常用的项目结构：

```text
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling

- **IDE**: VS Code + vim keybindings
- **Terminal**: Zsh + Oh-My-Zsh
- **Format**: Prettier（100 字符换行）
- **Linter**: ESLint + airbnb config
- **Test Framework**: Jest + React Testing Library
