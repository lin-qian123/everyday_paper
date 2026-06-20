# 每日论文雷达 - 2026-06-18

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，均为高相关 arXiv 预印本补充。
- 3 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge HPL accepted manuscripts / latest volume；页面可访问，但没有筛到比当前基线更强且明确非重复的正式来源增量，因此继续转向 arXiv 新稿与近几日相关预印本。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Latent Residual-Closure Fourier Neural Operator for Robust Multi-Field Solving in Particle-in-Cell Simulations
- 作者：Jianhua Lyu, Linlin Zhong
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.17733
- 真实发表日期：2026-06-16（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.17733
- 与方向关系：直接命中 AI/ML + PIC。论文把 PIC 场求解写成 residual-closure FNO 问题，在 SOL 与 two-stream 等基准上兼顾闭环物理一致性和场求解加速。

### 2) An Energy-Conserving Unstaggered Electromagnetic-Potential Particle-in-Cell Method, Part I: Non-relativistic Generalized-Momentum Formulation
- 作者：Andrew J. Christlieb, Luis Chacon, Sining Gong
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.15035
- 真实发表日期：2026-06-13（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.15035
- 与方向关系：直接覆盖 PIC 基础数值方法。工作重点是同时保持 Lorenz gauge / Gauss 定律和离散总能量守恒，对长时间激光等离子体与强场模拟都很关键。

### 3) Ultrashort Pulse Train Generation on a 100TW Laser Beamline Using a Delay Mask After the Final Focusing Optics
- 作者：David Gregocki, Federica Baffigi, Lorenzo Fulgentini, Luca Labate, Leonida A. Gizzi
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.13183
- 真实发表日期：2026-06-11（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.13183
- 与方向关系：直接关联激光尾场加速实验。作者验证了可用于 ReMPI 的超短脉冲列生成方案，属于高功率 LWFA 前端技术准备。

## 检索与去重执行记录

- 检索日期：2026-06-18。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI / 机器学习在上述方向中的应用。
- 优先来源：先检查 Cambridge HPL accepted manuscripts 与 latest volume；确认页面可访问，但未筛出比当前基线更强的非重复正式来源增量。随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 新稿及近几日相关 PIC/LWFA 检索结果。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-18/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py --source-family all`，因为旧重试队列仍是已明确的来源侧限制，继续全量跑只会在无效来源上耗时。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-18/notes/Jianhua Lyu and Linlin Zhong - 2026 - Latent Residual-Closure Fourier Neural Operator for Robust Multi-Field Solving in Particle-in-Cell Simulations.md`
  - `daily/2026-06-18/notes/Andrew J. Christlieb et al. - 2026 - An Energy-Conserving Unstaggered Electromagnetic-Potential Particle-in-Cell Method, Part I Non-relativistic Generalized-Momentum Formulation.md`
  - `daily/2026-06-18/notes/David Gregocki et al. - 2026 - Ultrashort Pulse Train Generation on a 100TW Laser Beamline Using a Delay Mask After the Final Focusing Optics.md`

## 状态更新

- `state/processed_articles.json`：从 116 条增至 119 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 43 条。

## 当日总结

- 今天补入 3 条高相关论文，覆盖了 AI 驱动的 PIC 场求解加速、结构保持/能量守恒 PIC 新格式，以及面向 ReMPI 的 LWFA 脉冲列实验准备。
- 这轮正式来源仍未提供足够强的新增量，继续保持“正式来源优先，但一旦增量质量不足就快速切回高价值 arXiv”的策略仍然合理。
