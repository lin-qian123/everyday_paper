# 每日论文索引 - 2026-06-28

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，其中 1 条为正式期刊论文，2 条为高相关 arXiv 预印本。
- 3 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面；高相关 HPL 候选多数已在库，JPP 当前页仍有 1 条强场传播理论增量可补入。随后继续从近期未入库 arXiv 中补入 2 条与“激光驱动中子/光核应用”直接相关的高价值预印本。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Relativistically strong electromagnetic waves in magnetised plasmas
- 作者：Maxim Lyutikov
- 期刊/平台：Journal of Plasma Physics（正式期刊）
- DOI：https://doi.org/10.1017/S0022377826101342
- 真实发表日期：2026-06
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/relativistically-strong-electromagnetic-waves-in-magnetised-plasmas/F0F5A8BFDE9503870BE5FB640878E44B
- 与方向关系：这篇偏强场理论，但它直接讨论相对论强波在磁化等离子体中的传播边界，对强场传播、磁化高能量密度等离子体和极端场波动问题有基础参考价值。

### 2) Laser-Wakefield-Driven Photonuclear and Laser-Driven DD Fusion Neutron Sources for Fast Neutron Capture: A Start-to-End Simulation Study
- 作者：Ou Z. Labun et al.
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2605.18968
- 真实发表日期：2026-05-18
- 来源链接：http://arxiv.org/abs/2605.18968v1
- 与方向关系：这篇几乎正中仓库新增关注的“电子束/离子束驱动中子与光核应用”主线，系统比较了 LWFA 光核源和激光驱动 DD 融合中子源在快中子俘获与核应用端的优劣。

### 3) Laser-driven Ion and Neutron Sources from Medium Repetition Ultrashort PW Laser
- 作者：X. Jiao et al.
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2605.18969
- 真实发表日期：2026-05-18
- 来源链接：http://arxiv.org/abs/2605.18969v1
- 与方向关系：这篇给出了激光离子加速到次级中子源的实验链路，覆盖靶厚优化、离子能谱标度、转换靶次级中子谱和产额，是当前应用方向里很实用的实验基线。

## 检索与去重执行记录

- 检索日期：2026-06-28。
- 重点检索方向：强场传播理论、激光驱动中子源、光核与快中子俘获应用、离子束-转换靶实验链路。
- 优先来源：Cambridge `Journal of Plasma Physics`、`High Power Laser Science and Engineering` 当前页面；随后补查近期未入库的高相关 arXiv 条目。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-28/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-28/notes/Maxim Lyutikov - 2026 - Relativistically strong electromagnetic waves in magnetised plasmas.md`
  - `daily/2026-06-28/notes/Ou Z. Labun et al. - 2026 - Laser-Wakefield-Driven Photonuclear and Laser-Driven DD Fusion Neutron Sources for Fast Neutron Capture A Start-to-End Simulation Study.md`
  - `daily/2026-06-28/notes/X. Jiao et al. - 2026 - Laser-driven Ion and Neutron Sources from Medium Repetition Ultrashort PW Laser.md`

## 状态更新

- `state/processed_articles.json`：从 144 条增至 147 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天的 3 条增量把“强场传播理论”、“激光驱动中子源系统级比较”和“离子束-转换靶实验基线”三条线同时补齐。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2605.18968`，因为它直接把激光源区、转换靶输运和快中子应用端连成了一条完整设计链。
