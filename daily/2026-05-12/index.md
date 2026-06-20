# 每日论文索引 - 2026-05-12

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 检索与去重执行记录

- 检索日期：2026-05-12。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在这些方向中的应用。
- 主要检索来源：ScienceDirect（JCP）、Nature 系列主题页、DOI 落地页。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（合计 DOI 键 70 条）。
- 去重命中：`10.1016/j.jcp.2026.114707`（已在历史台账中出现，未重复处理）。
- 今日新增并尝试处理 DOI：
  - `10.1016/j.jcp.2026.114693`
  - `10.1016/j.jcp.2026.114867`
  - `10.1016/j.jcp.2026.114991`

## 下载与校验状态

- 已执行 `scripts/safe_pdf_download.py` 对上述 3 篇新增论文进行 PDF 下载与校验。
- 三篇均下载失败，当前失败模式一致：
  - 代理模式：`URLError: [Errno 1] Operation not permitted`（环境代理端口不可用）。
  - 直连模式：`URLError: [Errno 8] nodename nor servname provided, or not known`（DNS 解析失败）。
- `daily/2026-05-12/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文笔记文件（无新增且校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免重复处理旧论文）。
- `state/daily_retry_candidates.json`：新增 3 条下载失败重试记录：
  - `10.1016/j.jcp.2026.114693`
  - `10.1016/j.jcp.2026.114867`
  - `10.1016/j.jcp.2026.114991`

## 当日总结

- 本轮已完成“正式来源优先 + DOI 去重 + 新增候选下载校验 + 失败入重试队列”的日更闭环。
- 当前主要阻塞仍为本机网络连通性（代理不可达 + 直连 DNS 失败）；网络恢复后可直接按 `daily/2026-05-12/run_results.json` 中命令重试。
