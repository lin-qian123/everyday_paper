# 每日论文索引 - 2026-07-20

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：3 条 arXiv 高相关预印本。
- 3 条论文均已通过官方 arXiv 来源下载，并通过 `%PDF-` 文件头校验。
- 今天先加载 `processed_articles.json`、`daily_retry_candidates.json` 和历史 daily 索引做硬去重；arXiv API 查询一度超时，因此改用 arXiv 官方近期列表页与单篇页面核对元数据。按台账、重试队列和历史 daily 去重后，优先选择与近表面等离子体控制、机器学习/统计诊断和 Hall-MHD 数值方法相关的未入库条目。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Microwave Resonant Discharges for Spatiotemporally Selective Plasma Breakdown Near Surfaces

- 作者：Arnav Mohapatra; Joshua K. Goodrich; Thomas C. Underwood
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14495
- 真实发表日期：2026-07-16
- 来源链接：https://arxiv.org/abs/2607.14495
- 与方向关系：论文用介质谐振结构和微波脉冲控制近表面局部击穿位置，补充非平衡等离子体源、靶表面能量沉积和实验平台控制方向。

### 2) Automated Outlier-Robust Bayesian Profile Fitting for Magnetically Confined Plasmas with Modified Tanh Profiles and Good-and-Bad Gaussian Mixture Likelihoods

- 作者：Jaewook Kim; Jekil Lee; Laurent Jung; Sang-hee Hahn; Sehyun Kwak
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14142
- 真实发表日期：2026-07-13
- 来源链接：https://arxiv.org/abs/2607.14142
- 与方向关系：论文把 outlier-robust Bayesian fitting、MCMC 和批处理诊断数据管线结合起来，用于 KSTAR 磁约束等离子体剖面生产，补强机器学习/统计推断与等离子体实验诊断交叉方向。

### 3) A structure-preserving Numerical Method for the Compressible Resistive-Hall-MHD System

- 作者：Murtazo Nazarov; Rafael Rodriguez-Velasco; Ignacio Tomas
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14286
- 真实发表日期：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.14286
- 与方向关系：论文构造可压缩电阻 Hall-MHD 的结构保持有限元方法，覆盖正性、能量、散度约束和磁重联 benchmark，补强 PIC/动理学之外的多尺度等离子体数值模拟主线。

## 检索与去重执行记录

- 检索日期：2026-07-20。
- 重点检索方向：近期 HPL/JPP 正式来源可见增量，以及 arXiv `physics.plasm-ph`、`physics.acc-ph`、`nucl-ex` 中与激光等离子体、HEDP、PIC/数值方法、激光加速束流应用、实验诊断和机器学习模拟相关的最新条目。
- 去重基线：`state/processed_articles.json`、`state/daily_retry_candidates.json` 与历史 `daily/` 全文检索。
- 去重结果：`10.48550/arXiv.2607.14495`、`10.48550/arXiv.2607.14142`、`10.48550/arXiv.2607.14286` 均未出现在处理台账、重试队列或历史 daily 中。
- 正式来源复查：本轮没有确认到比上述三条更强且明确非重复的 HPL/JPP 正式来源增量；旧重试队列仍是 12 条明确来源侧限制条目。
- 跳过记录：`10.48550/arXiv.2607.15072`、`10.48550/arXiv.2607.14722` 和 `10.48550/arXiv.2607.14235` 已在 2026-07-18 的备选记录中出现，本轮不作为新增论文重复处理。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-20/*.download_report.json`。
- 结果：3 条候选均通过环境代理路径从官方 arXiv 来源下载成功，并通过 `%PDF-` 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-20/notes/Arnav Mohapatra et al. - 2026 - Microwave resonant discharges.md`
  - `daily/2026-07-20/notes/Jaewook Kim et al. - 2026 - Bayesian profile fitting magnetically confined plasmas.md`
  - `daily/2026-07-20/notes/Murtazo Nazarov et al. - 2026 - Structure-preserving Hall-MHD method.md`

## 状态更新

- `state/processed_articles.json`：从 208 条增至 211 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍需后续专项清理；本轮不扩展旧重试队列。

## 当日总结

- 今天补强了近表面等离子体可控击穿、磁约束等离子体 Bayesian 诊断拟合和 Hall-MHD 结构保持数值方法三条主线。
- 三篇均为 arXiv 预印本，正式发表来源本轮未筛到更强且明确非重复的增量。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2607.14142`，因为它对实验诊断自动化、异常通道鲁棒处理和数据驱动等离子体分析的迁移价值最高。
