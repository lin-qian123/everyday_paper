# 每日论文雷达 - 2026-06-04

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) A hybrid quantum-classical particle-in-cell method for plasma simulations
- 作者：Pratibha Raghupati Hegde, Paolo Marcandelli, Yuanchun He et al.
- 期刊/平台：Future Generation Computer Systems（正式期刊，Open Access）
- DOI：https://doi.org/10.1016/j.future.2025.108087
- 真实发表日期：2026-02
- 来源链接：https://www.sciencedirect.com/science/article/pii/S0167739X25003814
- 与方向关系：PIC 数值方法 + 混合量子经典求解器 + 物理约束机器学习

### 2) Enhanced plasma heating by interaction with high-contrast laser and cone-shaped target
- 作者：Yuga Karaki, Yoshitaka Mori, Eigo Ebisawa et al.
- 期刊/平台：High Energy Density Physics（正式期刊）
- DOI：https://doi.org/10.1016/j.hedp.2025.101256
- 真实发表日期：2026-03
- 来源链接：https://www.sciencedirect.com/science/article/pii/S1574181825000849
- 与方向关系：高能量密度物理 + 高对比度激光加热 + 快点火/惯性约束聚变相关

### 3) Simulating ultrarelativistic beam-plasma instabilities with a quasistatic particle-in-cell code
- 作者：原页面摘要可确认，作者名单待网络恢复后补全
- 期刊/平台：Computer Physics Communications（正式期刊，Online first）
- DOI：https://doi.org/10.1016/j.cpc.2026.110140
- 真实发表日期：2026-03-25（Available online）
- 来源链接：https://www.sciencedirect.com/science/article/pii/S0010465526001220
- 与方向关系：束流-等离子体不稳定性 + 准静态 PIC + 激光/等离子体尾场加速建模

## 检索与去重执行记录

- 检索日期：2026-06-04。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：ScienceDirect 正式论文页；继续优先正式发表来源，不补重复旧条目。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 82 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。
- 说明：检索过程中继续剔除了历史已处理或已在失败重试台账中的旧论文，不重复下载、不重复分析。

## 下载与校验状态

- 当日执行了 3 条正式论文 PDF 下载尝试，详见 `daily/2026-06-04/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-04/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增正式论文候选，待网络恢复后重试。

## 当日总结

- 今天新增补入了 3 条此前未进入 processed/retry 台账的正式来源论文，继续保持 DOI/标题硬去重。
- 当前主阻塞仍是本地运行时的网络出站；网络恢复后应与 `2026-06-03` 的 3 条候选一起优先重试。
