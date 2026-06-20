# 每日论文雷达 - 2026-05-11

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 检索与去重执行记录

- 检索日期：2026-05-11。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在这些方向中的应用。
- 主要检索来源：Nature / Nature Communications、Physical Review 检索入口、ScienceDirect（JCP/CPC）与 DOI 落地页；arXiv 仅作补充。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（合计 DOI 键 70 条）。
- 去重命中：`10.1016/j.cpc.2026.110021`（Full EPIC-GOD）已在历史台账中出现，未重复处理。

## 下载与校验状态

- 尝试下载的新增候选：
  - `10.1016/j.jcp.2026.114867`
  - `10.1016/j.jcp.2026.114991`
- 本地执行 `scripts/safe_pdf_download.py` 失败，失败原因为运行环境缺少 `requests`。
- 尝试在仓库虚拟环境安装依赖时受当前网络/代理限制（`Operation not permitted`）阻塞，导致今日无法完成在线 PDF 抓取。
- `daily/2026-05-11/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文笔记文件（无新增且校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增。
- `state/daily_retry_candidates.json`：无新增（本次阻塞为运行环境问题，非单篇来源特异失败）。

## 当日总结

- 本轮继续遵循“正式来源优先 + DOI 去重 + 仅新增入库”。
- 今日关键阻塞为执行环境依赖与网络权限，待恢复后可直接重试上述两个 DOI 下载并继续入库流程。
