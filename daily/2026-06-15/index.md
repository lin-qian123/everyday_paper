# 每日论文雷达 - 2026-06-15

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 4 条，全部为在正式来源未筛出更强非重复增量后的高相关 arXiv 预印本补充。
- 4 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) High-dimensional inverse design of inertial fusion implosions via differentiable simulation
- 作者：A. J. Crilly, P. Travis, J. P. Brodrick, J. B. Coughlin, A. S. Joglekar
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.08827
- 真实发表日期：2026-06-07（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.08827
- 与方向关系：把可微仿真、自动微分和神经网络参数化用于 ICF implosion 逆向设计，直接覆盖 AI/ML + HEDP/ICF。

### 2) Conservative Charge and Current Deposition on Nonuniform 3D Cylindrical PIC Meshes with Residual Self-Field Diagnostics
- 作者：Zhe Liu, Zhijun Zhou, Yinjian Zhao
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.09168
- 真实发表日期：2026-06-08（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.09168
- 与方向关系：面向非均匀圆柱网格 PIC 的守恒沉积与 residual self-field 诊断，直接对应 PIC 数值方法和柱坐标强梯度等离子体建模。

### 3) Optimization of EUV output by experimentally validated radiation-hydrodynamic simulations across a broad laser parameter space
- 作者：Nozomi Tanaka, Yu Yamamoto, Akira Sasaki, Katsunobu Nishihara, Atsushi Sunahara, Tomoyuki Johzaki, Yuji Takagi, Kentaro Tomita, Shinsuke Fujioka, Masashi Yoshimura
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.05948
- 真实发表日期：2026-06-04（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.05948
- 与方向关系：基于实验校验过的辐射流体模型系统优化激光产等离子体 EUV 源，属于激光-等离子体 / HEDP 参数设计问题的高质量样本。

### 4) Probing kinetic enhancement of fusion reactivity in turbulent hot spots
- 作者：Yao Guo, Dong Wu, Jie Zhang
- 期刊/平台：arXiv 预印本（高相关补充）
- DOI：https://doi.org/10.48550/arXiv.2606.01860
- 真实发表日期：2026-06-01（arXiv submitted）
- 来源链接：https://arxiv.org/abs/2606.01860
- 与方向关系：围绕 ICF 热点中的非 Maxwell 尾分布、Fokker-Planck 与带核反应 PIC，对 fusion reactivity enhancement 做动力学刻画。

## 检索与去重执行记录

- 检索日期：2026-06-15。
- 重点检索方向：激光等离子体、强场 QED、高能量密度物理、PIC，以及 AI/机器学习在上述方向中的应用。
- 优先来源：先检查 Cambridge HPL accepted manuscripts 等正式来源，未筛出比历史基线更强且明确非重复的新条目；随后转到 arXiv `physics.plasm-ph` 与 `physics.acc-ph` 当前列表，筛出 4 条新的高相关预印本。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`（运行前唯一 DOI/标题键合计按既有记法为 218 条）。
- 本次新增候选：4 条，均未命中现有 processed/retry 台账；追加后唯一 DOI/标题键合计按既有记法为 222 条。

## 下载与校验状态

- 当日执行了 4 条候选论文 PDF 下载尝试，详见 `daily/2026-06-15/run_results.json`。
- 结果：4 条 arXiv 预印本均通过环境代理路径下载，并通过 PDF 文件头校验。
- 当前旧重试队列维持 12 条，仍全部属于来源侧限制：
  - 10 条 Elsevier / ScienceDirect `publisher_http_403`
  - 1 条 Nature `publisher_cookie_wall`
  - 1 条 IOP `publisher_bot_wall`

## 笔记产出

- 已生成 4 份中文结构化笔记：
  - `daily/2026-06-15/notes/A. J. Crilly et al. - 2026 - High-dimensional inverse design of inertial fusion implosions via differentiable simulation.md`
  - `daily/2026-06-15/notes/Zhe Liu et al. - 2026 - Conservative Charge and Current Deposition on Nonuniform 3D Cylindrical PIC Meshes with Residual Self-Field Diagnostics.md`
  - `daily/2026-06-15/notes/Nozomi Tanaka et al. - 2026 - Optimization of EUV output by experimentally validated radiation-hydrodynamic simulations across a broad laser parameter space.md`
  - `daily/2026-06-15/notes/Yao Guo et al. - 2026 - Probing kinetic enhancement of fusion reactivity in turbulent hot spots.md`

## 状态更新

- `state/processed_articles.json`：从 105 条增至 109 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 43 条。

## 当日总结

- 今天补入 4 条高相关 arXiv 预印本，主题覆盖 differentiable ICF inverse design、圆柱非均匀网格 PIC 沉积算法、激光产等离子体 EUV 源辐射流体优化，以及热点湍流下的 fusion reactivity kinetic enhancement。
- 当前下载链路保持稳定，说明最近恢复后的环境代理路径对 arXiv 仍然可用；正式来源仍应坚持“优先筛查、没有清晰增量就及时切到高质量预印本补充”的策略。
