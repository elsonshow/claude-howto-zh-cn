# 测试指南

本项目的测试主要覆盖两类内容：

- Python 脚本与 EPUB 构建
- 本地化校验脚本与相关守护逻辑

## 本地运行

```bash
uv venv
uv pip install -r scripts/requirements-dev.txt
uv run pytest scripts/tests/ -v
uv run python scripts/validate_localization.py
```

## 关注点

- EPUB 是否还能正常构建
- 中文化是否破坏 frontmatter、JSON/YAML、shell 脚本
- 关键受保护标识是否还存在
