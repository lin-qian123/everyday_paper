# 每日论文索引 - 2026-07-18

## 今日新增论文索引

- 今日新增并完成 PDF 校验入库 3 条：3 条 arXiv 高相关预印本。
- 3 条论文均已通过官方 arXiv 来源下载，并通过 PDF 文件头校验。
- 今天先复查正式来源可见检索结果，再使用 arXiv 官方 API 检索近期 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 与 `physics.ins-det` 条目；按台账、重试队列和历史 daily 去重后，优先选择与多尺度等离子体模拟、p-11B 聚变韧致辐射损失、以及弱非线性动理学等离子体先进算法相关的高价值条目。

## 今日高相关候选（已去重，已完成 PDF 与笔记）

### 1) An asymptotic-preserving five-moment two-species plasma model coupled to an external magnetohydrodynamic solver

- 作者：Magnus Deisenhofer; Aleksandr Mustonen; Simon Lautenbach; Rainer Grauer
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.15019
- 真实发表日期：2026-07-16
- 来源链接：https://arxiv.org/abs/2607.15019
- 与方向关系：论文提出 AP 五矩两物种流体到理想 MHD 的耦合策略，服务于从 Vlasov/PIC 级动理学区域到全局 MHD 区域的多尺度模拟，补强 PIC/动理学/流体层级耦合主线。

### 2) Parameter Scan of Multi-Fluid Equilibria in Rotating p-11B Plasmas: Effects on Fusion Power and Bremsstrahlung Losses

- 作者：Xingyu Li; Huasheng Xie; Lai Wei; Zhengxiong Wang
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14496
- 真实发表日期：2026-07-16
- 来源链接：https://arxiv.org/abs/2607.14496
- 与方向关系：论文用多流体平衡参数扫描分解 p-11B 旋转等离子体中的聚变功率和韧致辐射损失，直接关联核反应应用、辐射损失、能量转换效率和高能量密度聚变路线评估。

### 3) An end-to-end quantum algorithm for weakly nonlinear plasma physics with superquadratic speedup

- 作者：Bjorn K. Berntson; David Jennings; Matteo Lostaglio; Scott Parker
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14308
- 真实发表日期：2026-07-15
- 来源链接：https://arxiv.org/abs/2607.14308
- 与方向关系：论文为弱非线性动理学等离子体模型构造端到端量子算法，覆盖 Vlasov-Poisson、Fourier-Hermite 截断、Carleman 嵌入和复杂度分析，补充先进算法与等离子体模拟交叉方向。

## 检索与去重执行记录

- 检索日期：2026-07-18。
- 重点检索方向：近期 HPL/JPP 正式来源，以及 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det` 中与激光等离子体、HEDP、先进加速、强场辐射、PIC、束流应用、实验诊断、核反应应用和机器学习/先进算法相关的最新条目。
- 去重基线：`state/processed_articles.json`、`state/daily_retry_candidates.json` 与历史 `daily/` 全文检索。
- 去重结果：`10.48550/arXiv.2607.15019`、`10.48550/arXiv.2607.14496`、`10.48550/arXiv.2607.14308` 均未出现在处理台账、重试队列或历史 daily 中。
- 正式来源复查：公开搜索未筛到比本轮 arXiv 候选更强且明确非重复的 HPL/JPP 正式论文增量；本轮用 arXiv 官方 API 补入 2026-07-15 到 2026-07-16 的高相关新稿。
- 备选未入库候选包括 `10.48550/arXiv.2607.15072`（total-f gyrokinetic turbulence 初始化瞬态抑制）、`10.48550/arXiv.2607.14235`（相对论无碰撞激波长时 PIC 模拟）和 `10.48550/arXiv.2607.14722`（HSX/W7-X 边界巨岛构型计算）。本轮优先选择更贴近多尺度模拟接口、韧致辐射损失和先进算法主线的三篇。

## 下载与校验状态

- 当日执行了 3 条候选论文 PDF 下载尝试，详见 `daily/2026-07-18/*.download_report.json`。
- 结果：3 条候选均通过环境代理路径从官方 arXiv 来源下载成功，并通过 `%PDF-` 文件头校验。
- 今日没有重新运行 `scripts/retry_download_queue.py`，因为旧重试队列仍是 12 条明确来源侧限制条目，继续全量重试收益很低。

## 笔记产出

- 已生成 3 份中文结构化笔记：
  - `daily/2026-07-18/notes/Magnus Deisenhofer et al. - 2026 - AP five-moment plasma MHD coupling.md`
  - `daily/2026-07-18/notes/Xingyu Li et al. - 2026 - Rotating p-11B bremsstrahlung losses.md`
  - `daily/2026-07-18/notes/Bjorn Berntson et al. - 2026 - Quantum algorithm for weakly nonlinear plasma.md`

## 状态更新

- `state/processed_articles.json`：从 205 条增至 208 条。
- `state/daily_retry_candidates.json`：保持 12 条，无新增来源失败重试记录。
- 当前“已补回 PDF 但尚无中文结构化笔记”的历史条目仍需后续专项清理；本轮不扩展旧重试队列。

## 当日总结

- 今天补强了多尺度等离子体模拟接口、p-11B 聚变韧致辐射损失评估和弱非线性动理学等离子体量子算法三条主线。
- 如果只优先读一篇，建议先看 `10.48550/arXiv.2607.14496`，因为它直接连接核反应应用、韧致辐射损失和参数扫描诊断，对扩展应用方向最贴近。
