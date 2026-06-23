# 每日论文索引 - 2026-06-23

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 2 条，均为高相关近期 arXiv 预印本。
- 两条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge `Journal of Plasma Physics` / `High Power Laser Science and Engineering` 当前页面以及 arXiv `physics.plasm-ph` / `physics.acc-ph` 最新列表；正式来源没有筛到比 2026-06-21 到 2026-06-22 已入库条目更强、且明确非重复的新候选，因此回退到近一周 arXiv 新稿。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Impact of energetic alpha particles on core turbulence in an ARC-class fusion power plant
- 作者：J. Hall, N.T Howard, P. Rodriguez-Fernandez, R.A. Tinguely, I. Sfiligoi, J. Ruiz-Ruiz, J.C. Hillesheim, A. Creely, E.A. Belli, J. Candy
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.15965
- 真实发表日期：2026-06-18（v2）
- 来源链接：https://arxiv.org/abs/2606.15965
- 与方向关系：直接覆盖仓库已跟踪的“磁约束聚变与 alpha 粒子”支线。文章用线性/非线性 `CGYRO` 研究 ARC 级燃烧等离子体中快 alpha 对核心 ITG 湍流和输运的稳化作用，对反应堆性能预测很关键。

### 2) Quasiparticles and ion cooling by an electron beam in a strong magnetic field
- 作者：D.M. Popov, A.I. Milstein
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.16126
- 真实发表日期：2026-06-15
- 来源链接：https://arxiv.org/abs/2606.16126
- 与方向关系：属于束流-等离子体相互作用与束流品质控制的理论补充。文章把强磁场电子束冷却问题化约为离子与 `Larmor circle` 准粒子的相互作用，可为后续 beam-plasma reduced model 或磁化电子冷却理解提供方法学参考。

## 检索与去重执行记录

- 检索日期：2026-06-23。
- 重点检索方向：激光等离子体、强场 QED、PIC/动理学、机器学习在等离子体中的应用，以及磁约束聚变/快粒子/束流相关扩展主题。
- 优先来源：Cambridge `Journal of Plasma Physics`、`High Power Laser Science and Engineering` 当前页面；随后补扫 arXiv `physics.plasm-ph` 与 `physics.acc-ph` 近一周新稿。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：2 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 2 条候选论文 PDF 下载尝试，详见 `daily/2026-06-23/run_results.json`。
- 结果：2 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 2 份中文结构化笔记：
  - `daily/2026-06-23/notes/J. Hall et al. - 2026 - Impact of energetic alpha particles on core turbulence in an ARC-class fusion power plant.md`
  - `daily/2026-06-23/notes/D.M. Popov et al. - 2026 - Quasiparticles and ion cooling by an electron beam in a strong magnetic field.md`

## 状态更新

- `state/processed_articles.json`：从 130 条增至 132 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天不是纯粹补热门激光题目，而是补了两条“快粒子/束流与输运”方向的近期增量：一条面向燃烧等离子体性能预测，一条面向磁化电子束冷却理论。
- 两条里更值得优先读的是 `10.48550/arXiv.2606.15965`，因为它直接影响 ARC 级装置的核心输运建模，也更容易与仓库里已有的 gyrokinetics、surrogate 和反应堆性能条目串起来。
