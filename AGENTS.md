# AGENTS

## 项目约束

在本仓库进行开发/维护时，持续维护以下三个核心文件：

- `AGENTS.md`：项目指令与执行约束。
- `README.md`：项目定位、运行方式、目录结构、当前状态与重要说明。
- `TODO.md`：待办、阶段记录、阻塞点、下一步行动与接续线索。

## 执行规则

- 进入项目、推进项目、接续开发或整理状态时，先检查这三个文件是否存在且与当前状态一致。
- 若缺失则先创建；若过期则先更新，再进入代码或数据处理。
- 新项目启动时，先使用 Superpowers 的 brainstorming 流程梳理目标/约束/方案/风险，再开始实现。
- 每次新增论文并更新 `state/processed_articles.json` 后，运行 `python scripts/build_indexes.py` 重建 `papers/`、`categories/`、`daily/README.md` 和根 `INDEX.md`。
- 自动化成功完成后，默认提交并推送到远程 GitHub 仓库的 `origin/master`。
