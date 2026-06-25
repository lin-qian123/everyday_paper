# 每日论文索引 - 2026-06-26

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，均为高相关近期 arXiv 预印本。
- 3 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面，没有发现比近几日更强且明确非重复的正式来源增量；随后转向 2026-06-24 新提交的 arXiv 条目，补入 3 条更贴合“LPI 热电子源项、PIC 数值可信度、致密等离子体诊断”主线的增量。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Laser-intensity-spike-dominated hot electron generation from two-plasmon decay instability driven by moderate-bandwidth pulses
- 作者：C. Yao, Z. H. Cai, X. Wang, X. C. Wang, H. R. Yin, Z. A. Zhu, C. W. Lian, Y. Ji, X. Jiang, S. M. Xu, Y. Y. Yao, L. Y. Yang, J. N. Zhang, D. Meng, T. Peng, H. Wen, C. Z. Xiao, K. Y. Meng, J. Li, R. Yan, P. Yuan, Z. Zhang, L. Hao, Q. Jia, W. Feng, H. H. An, H. Y. Liu, Z. Y. Xie, P. P. Wang, C. Wang, A. Lei, X. H. Zhao, Z. H. Fang, W. Wang, Y. Q. Gu, Y-K. Ding, J. Zheng
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.26054
- 真实发表日期：2026-06-24
- 来源链接：http://arxiv.org/abs/2606.26054v1
- 与方向关系：这篇直接连到高能量密度物理与激光等离子体相互作用主线，核心是宽带驱动下两等离子体衰变如何增强热电子产生，对直接驱动 ICF 预热控制、LPI 抑制和激光脉冲工程都很关键。

### 2) Numerical thermalization in $n$-D particle-in-cell simulations
- 作者：R. M. Park, C. H. Moore, S. D. Baalrud
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.25528
- 真实发表日期：2026-06-24
- 来源链接：http://arxiv.org/abs/2606.25528v1
- 与方向关系：这篇非常贴合 PIC 与数值方法主线，直接讨论宏粒子权重导致的非物理碰撞性和数值热化时间尺度，对判断某个 PIC 结果到底是物理弛豫还是算法产物很关键。

### 3) Nanosecond-resolved 266 nm Mach-Zehnder interferometry for electron-density measurements of dense plasmas generated in supercritical fluids
- 作者：Kyusang Cho, Juho Lee, Gunsu Yun
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.25327
- 真实发表日期：2026-06-24
- 来源链接：http://arxiv.org/abs/2606.25327v1
- 与方向关系：这篇落在实验平台与诊断主线，虽然不是典型加速论文，但它提供了致密激光等离子体电子密度定量诊断方案，对 HEDP 实验和源区表征都很有参考价值。

## 检索与去重执行记录

- 检索日期：2026-06-26。
- 重点检索方向：激光等离子体不稳定性与热电子、PIC 数值可信度、致密等离子体实验诊断。
- 优先来源：Cambridge `Journal of Plasma Physics`、`High Power Laser Science and Engineering` 当前页面；随后补扫 arXiv `physics.plasm-ph` / `physics.acc-ph` 最新提交列表与关键词检索。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-26/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-26/notes/C. Yao et al. - 2026 - Laser-intensity-spike-dominated hot electron generation from two-plasmon decay instability driven by moderate-bandwidth pulses.md`
  - `daily/2026-06-26/notes/R. M. Park et al. - 2026 - Numerical thermalization in $n$-D particle-in-cell simulations.md`
  - `daily/2026-06-26/notes/Kyusang Cho et al. - 2026 - Nanosecond-resolved 266 nm Mach-Zehnder interferometry for electron-density measurements of dense plasmas generated in supercritical fluids.md`

## 状态更新

- `state/processed_articles.json`：从 138 条增至 141 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天的 3 条增量分别补强了上游激光不稳定性与热电子源项、PIC 长时间演化的数值可信度，以及高密度短寿命等离子体的定量诊断链路。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2606.25528`，因为它对今后阅读和判断几乎所有 PIC 结果都有方法论价值。
