# 每日论文索引 - 2026-06-03

## 今日新增论文索引

- 今日未发现满足“新增且可完成 PDF 下载校验”的论文入库条目。

## 今日高相关候选（已去重，待重试）

### 1) Explainable tokamak-agnostic forecasting of fusion plasma instability via megahertz turbulent fluctuations
- 作者：Semin Joung, Jaewook Kim, David R. Smith et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02689-2
- 真实发表日期：2026-06-01
- 来源链接：https://www.nature.com/articles/s42005-026-02689-2
- 与方向关系：机器学习用于 fusion plasma diagnostics/control + 可解释机器学习 + 跨装置泛化

### 2) Ultrafast many-body dynamics of dense Rydberg gases and ultracold plasma
- 作者：Mario Grossmann, Jette Heyer, Julian Fiedler et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02674-9
- 真实发表日期：2026-05-14
- 来源链接：https://www.nature.com/articles/s42005-026-02674-9
- 与方向关系：超冷等离子体动力学 + 激光驱动等离子体形成 + 分子动力学模拟

### 3) FusionMAE, a self-supervised pretrained model to optimize and simplify diagnostic and control of fusion plasma
- 作者：Zongyu Yang, Zhenghao Yang, Wenjing Tian et al.
- 期刊/平台：Communications Physics（正式期刊）
- DOI：https://doi.org/10.1038/s42005-026-02626-3
- 真实发表日期：2026-05-01
- 来源链接：https://www.nature.com/articles/s42005-026-02626-3
- 与方向关系：机器学习用于 fusion + 自监督预训练 + 诊断重建与控制接口统一

## 检索与去重执行记录

- 检索日期：2026-06-03。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 机器学习在上述方向中的应用。
- 优先来源：Nature Portfolio 正式论文页面与对应 DOI。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计 79 条）。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。
- 说明：检索过程中剔除了已在历史台账中的旧论文，例如 `10.1038/s42254-026-00935-8` 与 `10.1038/s41586-026-10400-2`，避免重复处理。

## 下载与校验状态

- 当日执行了 3 条正式论文 PDF 下载尝试，详见 `daily/2026-06-03/run_results.json`。
- 结果：三条候选均因本地运行环境网络受限失败，错误模式一致：
  - 走环境代理时返回 `Operation not permitted`
  - 直连时返回 DNS 解析失败 `nodename nor servname provided, or not known`
- `daily/2026-06-03/pdfs/` 无新增可校验 PDF。

## 笔记产出

- 今日无新增中文结构化笔记（无校验通过的 PDF）。

## 状态更新

- `state/processed_articles.json`：无新增（继续避免写入未校验论文）。
- `state/daily_retry_candidates.json`：已追加今日 3 条新增正式论文候选，待网络恢复后重试。

## 当日总结

- 今天成功补入 3 条此前未入库的新正式候选，且继续维持 DOI/标题硬去重，避免重复处理旧论文。
- 当前主阻塞仍是本地运行时的网络出站；网络恢复后应优先重试今天这 3 篇 `Communications Physics` 论文。
