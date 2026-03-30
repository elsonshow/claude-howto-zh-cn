<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 构建脚本与本地化校验脚本

这个目录现在主要包含两类脚本：

- `build_epub.py`：把仓库内的 Markdown 文档打包成 EPUB
- `validate_localization.py`：校验中文本土化过程中是否把可执行标识、链接或配置翻坏

---

## `build_epub.py`

用于把整个指南打包成 EPUB 电子书。

### 功能

- 按目录结构组织章节
- 把 Mermaid 图通过 Kroki.io 渲染成图片
- 生成封面
- 处理内部 Markdown 链接
- 在构建失败时明确报错

### 依赖

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 可访问 Kroki.io 的网络环境

### 快速开始

```bash
uv run scripts/build_epub.py
```

### 常见选项

```text
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]
```

```bash
# 查看详细日志
uv run scripts/build_epub.py --verbose

# 自定义输出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 如果遇到速率限制，降低并发
uv run scripts/build_epub.py --max-concurrent 5
```

---

## `validate_localization.py`

用于在中文本土化过程中做“翻译后验活”，避免这些问题：

- 内部 Markdown 链接失效
- YAML frontmatter 被改坏
- JSON / YAML 无法解析
- shell 脚本语法损坏
- 关键命令名、字段名、环境变量名、plugin manifest 标识被误改

### 快速开始

```bash
uv run python scripts/validate_localization.py
```

### 它会检查什么

- Markdown 相对链接
- frontmatter 合法性
- `.json` / `.yml` / `.yaml` 语法
- `*.sh` 的 `bash -n`
- 关键 protected tokens

### 什么时候运行

- 每次大规模翻译或重写之后
- 每次修改 `SKILL.md`、subagent、slash command 或 plugin manifest 之后
- 每次准备提交前
- 每次同步上游变更后

---

## 本地开发

```bash
# 创建虚拟环境
uv venv

# 激活并安装依赖
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# 运行全部测试
pytest scripts/tests/ -v

# 运行本地化校验
uv run python scripts/validate_localization.py

# 构建 EPUB
python scripts/build_epub.py
```

---

## 常见问题

**EPUB 构建失败且提示网络错误**  
先检查网络、代理以及 Kroki.io 是否可访问，可以尝试提高 `--timeout`。

**本地化校验失败**  
优先检查：

- 是否把 `/optimize`、`/pr`、`claude -p` 这类命令改坏了
- 是否把 `allowed-tools`、`tools`、`model`、`env` 这类字段翻译掉了
- 是否删掉了 `GITHUB_TOKEN`、`mcpServers`、`license` 等受保护标识

**中文内容导致拼写检查报错**  
仓库已对中文字符做了忽略处理；如果仍然报错，多半是英文术语或项目名新增了未收录词条。
