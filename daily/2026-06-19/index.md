# 每日论文雷达 - 2026-06-19

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 4 条，均为高相关 arXiv 预印本补充。
- 4 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge HPL / JPP 近期正式来源，但没有筛到比当前基线更强且明确非重复的增量，因此继续转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近一周新稿。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Wake Perturbations in Laser- and Beam-Driven Plasma Wakefield Accelerators: A Symmetry-Based Multipole Classification
- 作者：Andrei C. Berceanu, Alessio Del Dotto
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.18845
- 真实发表日期：2026-06-17（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.18845
- 与方向关系：直接命中激光等离子体加速主线。工作把 LWFA / PWFA 的束质退化机制统一映射到多极对称性通道，便于后续把 beam loading、hosing 和优化问题放到同一语言下理解。

### 2) Ionization-Induced Electrostatic Hose Instability in Electron-Beam-Sustained Plasmas
- 作者：Jia-Hong Chen, Yi Yu, Jian Chen, Zhi-Bin Wang
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.12127
- 真实发表日期：2026-06-15（arXiv v2）
- 来源链接：https://arxiv.org/abs/2606.12127
- 与方向关系：虽然场景偏 beam-sustained plasma，但论文提出的新型 electrostatic hose 机制与束流-等离子体耦合、尾场加速稳定性和 PIC 验证方法直接相通。

### 3) Hierarchical Framework of Runaway Electrons using Deep Learning
- 作者：Tyler Mark, Christopher J. McDevitt
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.12567
- 真实发表日期：2026-06-10（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.12567
- 与方向关系：直接覆盖 AI / 机器学习在等离子体动理学中的代理建模。工作把伴随公式和 PINN 结合起来，加速 runaway electron 电流、平均能量和能谱预测。

### 4) Mixed Hermite-Legendre spectral method for kinetic plasma simulations
- 作者：Opal Issan, Gian Luca Delzanno, Vadim Roytershteyn
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.12322
- 真实发表日期：2026-06-10（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.12322
- 与方向关系：偏基础算法，但和 kinetic plasma simulation 直接相关；它补的是非 PIC 的低噪声谱方法路线，适合和近期多篇 PIC 数值方法条目并读。

## 检索与去重执行记录

- 检索日期：2026-06-19。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI / 机器学习在上述方向中的应用。
- 优先来源：先复查 Cambridge HPL latest volume 与 JPP 近期页面；确认页面可访问，但 2026-06-19 这轮没有筛出比当前基线更强的非重复正式来源增量。随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近一周列表与相关检索结果。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：4 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 4 条候选论文 PDF 下载尝试，详见 `daily/2026-06-19/run_results.json`。
- 结果：4 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py --source-family all`，因为旧重试队列仍是已明确的来源侧限制，继续全量跑只会在无效来源上耗时。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 4 份中文结构化笔记：
  - `daily/2026-06-19/notes/Andrei C. Berceanu et al. - 2026 - Wake Perturbations in Laser- and Beam-Driven Plasma Wakefield Accelerators A Symmetry-Based Multipole Classification.md`
  - `daily/2026-06-19/notes/Jia-Hong Chen et al. - 2026 - Ionization-Induced Electrostatic Hose Instability in Electron-Beam-Sustained Plasmas.md`
  - `daily/2026-06-19/notes/Tyler Mark et al. - 2026 - Hierarchical Framework of Runaway Electrons using Deep Learning.md`
  - `daily/2026-06-19/notes/Opal Issan et al. - 2026 - Mixed Hermite-Legendre spectral method for kinetic plasma simulations.md`

## 状态更新

- `state/processed_articles.json`：从 119 条增至 123 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目为 65 条。

## 当日总结

- 今天补入 4 条高相关论文，分别覆盖了激光/束驱尾场加速的束质统一理论、束流诱导等离子体中的新型 hose 不稳定性、AI 驱动的 runaway electron 动理学代理，以及 kinetic plasma 的低噪声谱方法。
- 今天最值得优先读的是 `2606.18845`，因为它把 LWFA / PWFA 里一批原本分散的稳定性和束质问题收拢到统一的多极分类框架，对后续做实验设计、仿真诊断和 Bayesian optimization 都有组织价值。
