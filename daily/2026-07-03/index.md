# 每日论文索引 - 2026-07-03

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：均为 Cambridge `Journal of Plasma Physics` 正式开放论文。
- 3 条论文均已下载通过 PDF 文件头校验，并已生成中文结构化笔记。
- 今天先复查 Cambridge `Journal of Plasma Physics` 最新 listing 与 `High Power Laser Science and Engineering` accepted/latest 页面；HPL 当前增量多偏激光器件，JPP 当前期仍有与开放磁约束、中性束和磁喷管等离子体流相关的未入库条目，因此优先补入正式来源。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Overview of GOL-NB experiments in 2025
- 作者：Vladimir V. Postupaev et al.
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101895
- 真实发表日期：2026-06-29
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/overview-of-golnb-experiments-in-2025/453D0204938A5C1B86FE8F21B7582569
- 与方向关系：GOL-NB 是开放磁阱/多镜约束实验平台，论文集中讨论 1 MW 中性束注入、快离子谱、MHD 稳定性、多镜与长螺线管配置对比，以及降低中性气体密度等问题，能补强本仓库对中性束、束流-等离子体耦合和开放磁约束实验诊断的跟踪。

### 2) Plugging of multi-mirror machines by a travelling rotating magnetic field
- 作者：Tal Miller et al.
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101834
- 真实发表日期：2026-06-26
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/plugging-of-multimirror-machines-by-a-travelling-rotating-magnetic-field/40C5B4742CD8067448891DFD0736CB05
- 与方向关系：论文研究开放端多镜约束中的轴向损失抑制，提出 travelling rotating magnetic field 端塞方案，与聚变等离子体约束、单粒子模拟、半动理学率方程和束流相空间控制相关。

### 3) Plasma flow and equilibrium in the magnetic nozzle
- 作者：Andrei Smolyakov et al.
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101718
- 真实发表日期：2026-06-22
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/plasma-flow-and-equilibrium-in-the-magnetic-nozzle/226AD10EC31323F91112BA15F221D4DA
- 与方向关系：磁喷管与开放磁镜、等离子体推进、先进 divertor 和线性聚变装置相关，论文给出 transonic plasma flow、惯性力与 Grad-Shafranov 平衡耦合的解析/数值结果，对束流传输和磁场导引等离子体流有参考价值。

## 检索与去重执行记录

- 检索日期：2026-07-03。
- 重点检索方向：Journal of Plasma Physics 最新条目、High Power Laser Science and Engineering accepted/latest、开放磁约束、多镜端塞、中性束加热、磁喷管等离子体流。
- 优先来源：Cambridge `Journal of Plasma Physics`；随后补查 Cambridge HPL accepted/latest 与近期 arXiv API。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。
- arXiv API 本轮出现 timeout / HTTP 429；由于正式来源已筛到足够高质量增量，未继续扩大预印本抓取。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-03/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-03/notes/Vladimir V. Postupaev et al. - 2026 - Overview of GOL-NB experiments in 2025.md`
  - `daily/2026-07-03/notes/Tal Miller et al. - 2026 - Plugging of multi-mirror machines by a travelling rotating magnetic field.md`
  - `daily/2026-07-03/notes/Andrei Smolyakov et al. - 2026 - Plasma flow and equilibrium in the magnetic nozzle.md`

## 状态更新

- `state/processed_articles.json`：从 159 条增至 162 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天补强了开放磁约束与中性束方向：GOL-NB 实验进展提供平台和诊断基线，travelling rotating magnetic field 端塞论文提供端部损失控制模型，magnetic nozzle 论文提供开放磁场等离子体流和平衡背景。
- 如果只优先读一篇，建议先看 `10.1017/S0022377826101895`，因为它最接近实验平台、1 MW 中性束、快离子谱和多镜约束的综合状态。
