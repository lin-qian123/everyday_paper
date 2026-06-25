# 每日论文索引 - 2026-06-25

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条，均为高相关近期 arXiv 预印本。
- 3 条论文均已下载通过 PDF 校验，并已生成中文结构化笔记。
- 今天先复查了 Cambridge `Journal of Plasma Physics` 与 `High Power Laser Science and Engineering` 当前页面，没有筛到比近几日已入库条目更强且明确非重复的正式来源增量；随后转向 arXiv `physics.plasm-ph` / `physics.acc-ph` 近两日列表，补入 3 条更贴合“激光离子束应用、束流-尾场设计、HEDP 诊断”主线的增量。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) Multi-objective Bayesian optimisation of a double-layer target for quasi-monoenergetic TNSA protons
- 作者：Chengqi-Zhang, Yang He, Mamat Ali Bake, Bai-Song Xie
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.23224
- 真实发表日期：2026-06-22
- 来源链接：https://arxiv.org/abs/2606.23224
- 与方向关系：这篇直接对应“激光离子加速束流品质与应用前优化”主线，用多目标贝叶斯优化联动激光参数与双层靶结构，面向准单能 TNSA 质子束设计，对辐照、诊疗和后续核反应应用都很相关。

### 2) Evolution of Quadrupole Wakefield Driven by Transversely Asymmetric Electron Beams in Hollow Plasma Channels
- 作者：Siqin Ding, Jianfei Hua, Fei Li, Shiyu Zhou, Wei Lu
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.24067
- 真实发表日期：2026-06-23
- 来源链接：https://arxiv.org/abs/2606.24067
- 与方向关系：论文研究 hollow plasma channel 中适合正电子加速的 quadrupole wakefield 如何稳定演化，属于先进 wakefield 加速与可用束流设计问题，对正电子方案和装置级束流品质约束都有价值。

### 3) Observation of stopping power reduction at strong ion-plasma coupling
- 作者：Yun Liu, Jieru Ren, Zhigang Deng, Wei Qi, Bubo Ma, Wenqing Wei, Shizheng Zhang, Xuyang Luo, Ziqian Zhao, Mingzhe Yang, Yifang Gao, Xueguang Ren, Jianxing Li, Dieter H. H. Hoffmann, Xing Wang, Zhongfeng Xu, Shaoyi Wang, Quanping Fan, Bo Cui, Weiwu Wang, Sixin Wu, Yue Yang, Zhurong Cao, Zongqing Zhao, Yuqiu Gu, Leifeng Cao, Bin He, Shaoping Zhu, Olga Rosmej, Rui Cheng, Guoqing Xiao, Weimin Zhou, Yongtao Zhao
- 期刊/平台：arXiv 预印本
- DOI：https://doi.org/10.48550/arXiv.2606.23109
- 真实发表日期：2026-06-22
- 来源链接：https://arxiv.org/abs/2606.23109
- 与方向关系：这篇把激光加速准单能碳离子直接用于强耦合致密等离子体 stopping 实验，横跨激光离子束应用、高能量密度物理、ICF 输运基准和实验诊断，是本轮最贴近“束流驱动 HEDP 应用”的条目。

## 检索与去重执行记录

- 检索日期：2026-06-25。
- 重点检索方向：激光离子加速与参数寻优、先进尾场加速束流设计、激光束流驱动的高能量密度物理诊断。
- 优先来源：Cambridge `Journal of Plasma Physics`、`High Power Laser Science and Engineering` 当前页面；随后补扫 arXiv `physics.plasm-ph`、`physics.acc-ph` 近两日列表。
- 去重基线：`state/processed_articles.json` 与 `state/daily_retry_candidates.json`。
- 本次新增候选：3 条，均未命中现有 processed/retry 台账。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-06-25/run_results.json`。
- 结果：3 条候选均通过环境代理路径下载，并通过 PDF 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-06-25/notes/Chengqi-Zhang et al. - 2026 - Multi-objective Bayesian optimisation of a double-layer target for quasi-monoenergetic TNSA protons.md`
  - `daily/2026-06-25/notes/Siqin Ding et al. - 2026 - Evolution of Quadrupole Wakefield Driven by Transversely Asymmetric Electron Beams in Hollow Plasma Channels.md`
  - `daily/2026-06-25/notes/Yun Liu et al. - 2026 - Observation of stopping power reduction at strong ion-plasma coupling.md`

## 状态更新

- `state/processed_articles.json`：从 135 条增至 138 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍为 65 条。

## 当日总结

- 今天的 3 条增量分别补强了三条互相可衔接的主线：激光离子束参数优化、先进等离子体尾场的可用束流结构，以及激光束流驱动的高能量密度 stopping 诊断。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2606.23109`，因为它最直接连接用户扩展关注的“激光离子束应用 + HEDP/ICF 诊断与输运模型基准”。
