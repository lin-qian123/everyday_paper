# 每日论文索引 - 2026-06-06

> 补充说明：当天原始运行受限于网络环境。后续集中回填结果见 [`daily/2026-06-06/pdf-backfill.md`](/Volumes/PHILIPS/programs/everyday_paper/daily/2026-06-06/pdf-backfill.md)。

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Enhanced terahertz radiation generation by phase-controlled two-color laser pulses interacting with an under-dense plasma
- 作者：K. P. Anjana, Rohit Kumar Srivastav, Mrityunjay Kundu
- 期刊/平台：Scientific Reports（正式期刊，Open Access）
- DOI：https://doi.org/10.1038/s41598-026-35800-2
- 真实发表日期：2026-02-14
- 来源链接：https://www.nature.com/articles/s41598-026-35800-2
- 与方向关系：两色激光与欠密等离子体相互作用 + THz 产生增强 + 激光等离子体辐射诊断

### 2) Multi-pulse and multi-angle ultrafast X-ray imaging driven by petawatt-class ultrafast laser pulses
- 作者：Hong Zhang, Hang Guo, Hao Wang et al.
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：https://doi.org/10.1017/hpl.2026.10149
- 真实发表日期：2026-05-15（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/multipulse-and-multiangle-ultrafast-xray-imaging-driven-by-petawattclass-ultrafast-laser-pulses/377C4FD30BE9B10679E9462699301DDE
- 与方向关系：拍瓦级超快激光 + 多脉冲多角度超快 X 射线成像 + FBPIC/Geant4 支撑 HED/ICF 诊断

### 3) Dual-picosecond-laser-driven generation of MV/m giant electromagnetic pulses
- 作者：Aihui Niu, Bo Zhang, Wei Qi et al.
- 期刊/平台：High Power Laser Science and Engineering（Accepted manuscript，官方已接收）
- DOI：官方检索结果页当前未直接暴露，先按标题键去重并入重试队列
- 真实发表日期：2026-05-19（Published online by Cambridge University Press）
- 来源链接：https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/dualpicosecondlaserdriven-generation-of-mvm-giant-electromagnetic-pulses/7455A103DE0717CC117130D01914BF65
- 与方向关系：双皮秒激光驱动 EMP 产生 + 热电子扩展关联 + 激光等离子体设施诊断与 PIC 验证

## 检索与去重执行记录

- 检索日期：2026-06-06。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在上述方向中的应用。
- 优先来源：Nature Portfolio 官方论文页、Cambridge Core 官方论文页 / accepted manuscript 页面。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 88 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计 91 条。
- 说明：今天继续剔除了已在现有台账中的旧论文，例如 `10.1038/s42254-026-00935-8`、`10.1038/s41598-026-42431-0` 与 `10.1038/s41598-026-49116-8`。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-06/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-06/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增候选，待网络恢复后重试。

## 当日总结

- 今天补入了 1 条正式论文和 2 条官方 accepted manuscript，继续覆盖欠密等离子体 THz 辐射、拍瓦激光超快 X 射线诊断与高功率激光 EMP 物理。
- 当前主阻塞仍是本地运行时外网出站；网络恢复后应优先把 `2026-06-03` 至 `2026-06-06` 的 12 条积压候选一起完成 PDF 校验与中文笔记。
