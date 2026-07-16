# 每日论文索引 - 2026-07-17

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 4 条：1 条 JPP 正式开放论文，3 条 arXiv 高相关预印本。
- 4 条论文均已通过官方来源下载，并通过 PDF 文件头校验。
- 今天先复查 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 可见页面，再使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重后，优先选择与大振幅等离子体波动理学、激光质子加速靶设计、激光驱动 D-D 中子源应用、以及 PIC 框架扩展直接相关的高价值条目。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) On the evolution of a large-amplitude, weakly collisional electron plasma wave

- 作者：Archis Joglekar; Alec Thomas
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101986
- 真实发表日期：2026-07-13
- 来源链接：https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/on-the-evolution-of-a-largeamplitude-weakly-collisional-electron-plasma-wave/1F4DFC13829B9865B135E39E08FD57AE
- 与方向关系：论文用 VPFP 模拟分析大振幅弱碰撞电子等离子体波的俘获、退俘获和 Landau 阻尼阶段，补强激光等离子体基础波动、尾场模拟和动理学 benchmark 主线。

### 2) Dual-pulse micronozzle acceleration of sub-GeV-class protons

- 作者：D. Pan; M. Murakami
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.13672
- 真实发表日期：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.13672
- 与方向关系：论文提出双脉冲微喷嘴相位锁定质子加速方案，在 `10^21 W/cm^2` 量级下获得 sub-GeV 质子和高转换效率，直接关联激光离子加速、靶设计、束流品质和次级粒子应用。

### 3) Neutron-source fidelity for laser-driven D--D lithium-blanket tritium-breeding tests

- 作者：Chengqi Zhang et al.
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.13585
- 真实发表日期：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.13585
- 与方向关系：论文耦合 PIC、厚靶 D-D 中子源模型和 Monte Carlo 输运，量化真实激光驱动中子源谱/角分布对锂包层产氚测试的影响，直接覆盖激光离子加速核反应应用和源项保真度。

### 4) λPIC: A callback-centric particle-in-cell framework

- 作者：Xuesong Geng et al.
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.13507
- 真实发表日期：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.13507
- 与方向关系：论文提出面向自定义物理、诊断和原位分析的 callback-centric PIC 框架，特别关注强激光-等离子体相互作用，补强 PIC 代码架构、动态负载均衡和可扩展模拟工作流。

## 检索与去重执行记录

- 检索日期：2026-07-17。
- 重点检索方向：近期 HPL/JPP 正式来源，以及 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det` 中与激光等离子体、HEDP、先进加速、强场辐射、PIC、束流应用、实验诊断、核反应应用和机器学习模拟相关的最新条目。
- 去重基线：`state/processed_articles.json`、`state/daily_retry_candidates.json` 与历史 `daily/` 全文检索。
- 去重结果：`10.1017/S0022377826101986`、`10.48550/arXiv.2607.13672`、`10.48550/arXiv.2607.13585`、`10.48550/arXiv.2607.13507` 均未出现在处理台账、重试队列或历史 daily 中。
- 正式来源复查：Cambridge JPP 当前 issue 已出现 2026-07-13 到 2026-07-14 的正式开放条目；其中 `10.1017/S0022377826101986` 与大振幅电子等离子体波和 VPFP 动理学直接相关，优先入库。Cambridge HPL 可见新增 accepted manuscripts 仍以激光器件/光学系统为主，未筛到比本轮 arXiv 应用条目更贴近扩展主题的非重复正式论文。
- 备选未入库候选包括 `10.48550/arXiv.2607.13791`（Schottky 谱 betatron tune 机器学习诊断）、`10.48550/arXiv.2607.12682`（STEP 电磁湍流大通量转变）、`10.48550/arXiv.2607.12512`（helicon wave heating/current drive reduced model）和 `10.1017/S0022377826101962`（有限振幅单色波中 Maxwellian tail bump 的弱碰撞共振问题）。本轮优先选择正式 JPP 动理学条目和三条更贴近激光加速/中子源/PIC 框架的最新预印本。

## 下载与校验状态

- 当日执行了 4 条候选论文 PDF 下载尝试，详见 `daily/2026-07-17/*.download_report.json`。
- 结果：4 条候选均通过环境代理路径从官方来源下载成功，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 4 份中文结构化笔记：
  - `daily/2026-07-17/notes/Archis Joglekar and Alec Thomas - 2026 - Large-amplitude weakly collisional electron plasma wave.md`
  - `daily/2026-07-17/notes/D. Pan and M. Murakami - 2026 - Dual-pulse micronozzle acceleration.md`
  - `daily/2026-07-17/notes/Chengqi-Zhang et al. - 2026 - Neutron-source fidelity.md`
  - `daily/2026-07-17/notes/Xuesong Geng et al. - 2026 - lambdaPIC callback-centric PIC framework.md`

## 状态更新

- `state/processed_articles.json`：从 201 条增至 205 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍需后续专项清理；本轮不扩展旧重试队列。

## 当日总结

- 今天补强了正式 JPP 等离子体波动理学、激光驱动 sub-GeV 质子靶设计、激光 D-D 中子源产氚应用和 PIC 框架扩展四条主线。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2607.13585`，因为它直接连接激光离子加速、D-D 中子源、锂包层核反应应用和 PIC-Monte Carlo 多物理模拟，是扩展应用方向中最完整的一篇。
