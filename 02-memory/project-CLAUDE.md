# 项目配置

## Project Overview

- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture

@docs/architecture.md  
@docs/api-standards.md  
@docs/database-schema.md

## Development Standards

### Code Style

- 使用 Prettier
- 使用 ESLint + airbnb config
- 最大行长 100
- 2-space indentation

### Naming Conventions

- **Files**: kebab-case
- **Classes**: PascalCase
- **Functions/Variables**: camelCase
- **Constants**: UPPER_SNAKE_CASE
- **Database Tables**: snake_case

### Git Workflow

- 分支命名：`feature/description` 或 `fix/description`
- 提交信息遵循 conventional commits
- 合并前需要 PR
- 所有 CI/CD 检查必须通过
- 至少 1 个 approval

### Testing Requirements

- 最低 80% 覆盖率
- 关键路径必须有测试
- unit tests 用 Jest
- E2E 用 Cypress
- 文件命名：`*.test.ts` 或 `*.spec.ts`

### API Standards

- 使用 RESTful endpoints
- JSON request / response
- 正确使用 HTTP status code
- API 统一带版本：`/api/v1/`
- 所有 endpoint 要有示例文档

### Database

- schema 变更必须走 migration
- 不允许硬编码凭证
- 使用 connection pooling
- 开发环境开启 query logging
- 定期备份

### Deployment

- Docker-based deployment
- Kubernetes orchestration
- blue-green deployment
- 失败自动回滚
- deploy 前先跑数据库迁移

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | 启动开发服务 |
| `npm test` | 运行测试 |
| `npm run lint` | 检查代码风格 |
| `npm run build` | 生产构建 |
| `npm run migrate` | 执行数据库迁移 |

## Team Contacts

- Tech Lead: Sarah Chen (`@sarah.chen`)
- Product Manager: Mike Johnson (`@mike.j`)
- DevOps: Alex Kim (`@alex.k`)

## Known Issues & Workarounds

- PostgreSQL 连接池高峰期限制为 20
- 临时方案：实现 query queuing
- Safari 14 对 async generators 有兼容性问题
- 临时方案：使用 Babel transpiler

## Related Projects

- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
