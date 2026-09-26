# 每日论文索引 - 2026-09-26

## 今日概览

- 运行日期：2026-09-26
- 新增论文数：4（均为 2026-09-25 官方新论文列表中的高相关 arXiv 预印本）
- 最新性：官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det` 已核对到 2026-09-25 批次；同时检查 Crossref 2026-09-25 至 26 正式元数据与单篇页，未筛得优先级更高且可验证全文的新增正式论文。
- 主题分布：激光尾场电子—铅转换靶—GeV 缪子成像实验；同步辐射/非线性 Breit–Wheeler 的无查表 Monte Carlo；恒星器湍流 GX 代理与闭环优化；暖稠密铝 mDFT 状态方程和输运。
- 去重：按 DOI/arXiv identifier、规范化标题、378 条完成台账、17 条结构化重试队列和历史 `daily/` 核对，4 篇均为新作品。
- PDF / 正文：4 份官方 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；MinerU 四项均报 `parsing failed`，故按规则采用本地布局文本、页面渲染和逐图检查。共保留并人工查看 16 张关键图。
- 覆盖边界：本轮定向覆盖官方目标分类和正式元数据，不宣称穷尽所有期刊或跨学科来源。

## 论文清单

### 1. Imaging with GeV muons produced via laser-wakefield-accelerated electrons

- 标识符：[arXiv:2609.28788](https://arxiv.org/abs/2609.28788)；归档 DOI `10.48550/arXiv.2609.28788`
- 提交日期：2026-09-23（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-26/pdfs/Dobre et al. - 2026 - Laser-driven GeV muon imaging.pdf`
- 中文笔记：[Dobre et al. - 2026 - Laser-driven GeV muon imaging.md](notes/Dobre%20et%20al.%20-%202026%20-%20Laser-driven%20GeV%20muon%20imaging.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：目前最直接闭合 LWFA 电子、厚铅转换靶、复合屏蔽、人工缪子与实际透射成像的实验链，并保留粒种判别依赖 GEANT4 的边界。
- 一句话总结：最高约 `8 GeV` 的实测电子谱驱动铅靶，在 `20/29 m` 得到 `4.51/6.35 m` 的前向信号并用 30 发成像；`86.91%` 缪子沉积占比和几 GeV 能区来自 GEANT4/传播阈值，而非逐事例谱仪。

### 2. Monte Carlo sampling of first-order QED processes in laser and pulsar plasmas

- 标识符：[arXiv:2609.29325](https://arxiv.org/abs/2609.29325)；归档 DOI `10.48550/arXiv.2609.29325`
- 提交日期：2026-09-24（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-26/pdfs/Sarjomaa and Nattila - 2026 - QED Monte Carlo sampling.pdf`
- 中文笔记：[Sarjomaa and Nattila - 2026 - QED Monte Carlo sampling.md](notes/Sarjomaa%20and%20Nattila%20-%202026%20-%20QED%20Monte%20Carlo%20sampling.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：直接针对辐射 PIC 的同步辐射和非线性 Breit–Wheeler 采样瓶颈，给出无查表、无插值、无迭代寻根的闭式实现与全参数误差图。
- 一句话总结：Padé 近似把累积概率反演化为四次方程，单过程抽样谱约百分比精度；尚未接入生产 PIC，故没有可验证的端到端 speedup 或级联误差结论。

### 3. AI-Accelerated Gyrokinetic Predictions of Turbulent Transport for Stellarator Design Optimization and Experimental Planning

- 标识符：[arXiv:2609.28730](https://arxiv.org/abs/2609.28730)；归档 DOI `10.48550/arXiv.2609.28730`
- 提交日期：2026-09-23（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-26/pdfs/Churchill et al. - 2026 - AI gyrokinetic stellarator transport.pdf`
- 中文笔记：[Churchill et al. - 2026 - AI gyrokinetic stellarator transport.md](notes/Churchill%20et%20al.%20-%202026%20-%20AI%20gyrokinetic%20stellarator%20transport.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：不仅报告 >20 万次 GX 训练与 T3D 加速，还公开展示闭环优化怎样利用分布外非物理解产生虚假最优，是 ML—等离子体应用中少见的正反证据并列。
- 一句话总结：CNN ensemble 在特定算例中实现 `72×` 优化和 `45×/720×` T3D wall-clock/GPU-hour 加速；经非线性 GX 验证的温度提升仍为数值结果，最高分解则因 OOD、非嵌套磁面而失效。

### 4. Equation of state and transport coefficients of warm dense aluminum from mixed deterministic-stochastic density functional theory

- 标识符：[arXiv:2609.29435](https://arxiv.org/abs/2609.29435)；归档 DOI `10.48550/arXiv.2609.29435`
- 提交日期：2026-09-24（2026-09-25 官方新论文列表）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-26/pdfs/Li et al. - 2026 - Warm dense aluminum DFT.pdf`
- 中文笔记：[Li et al. - 2026 - Warm dense aluminum DFT.md](notes/Li%20et%20al.%20-%202026%20-%20Warm%20dense%20aluminum%20DFT.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：给出可供 Z-pinch/MagLIF 辐射流体使用的高温高密铝 EOS/输运表，并清楚暴露简化模型在高压 Hugoniot 和强磁横向输运上的分叉。
- 一句话总结：mDFT 覆盖 `10–1000 eV、1–18 g/cm³`，Lee–More 在 `100 eV` 的电/热导偏差可达 `26–63%`；实验主要止于 `<9 g/cm³`，未验证最强高压分歧。

## 未入库候选与取舍

- `arXiv:2609.29514` 的二维 MHD 重联 PINO 报告高分辨率零样本推断和百倍级作者基准，但本轮已有更大训练规模、含闭环失败分析的恒星器代理，故留作后续 ML 专题。
- `arXiv:2609.28604` 在 VAMOS++ MWPPAC 上做物理约束自监督校准，属于真实核探测器实验；与本轮激光转换靶成像和等离子体主线相比关联稍弱，暂不入库。
- `arXiv:2609.29277` 的介质阻挡放电再点火预测与 `2609.29336` 的贝叶斯饱和闭合具有方法价值，但专业相似度低于上述四篇。
- 本轮 Crossref 正式元数据命中未出现可验证全文且优先级高于四篇的新正式论文；因此没有用一般网页结果替代官方增量。

## 当日综合总结

- Dobre 等把此前“观察到激光驱动缪子”推进到实际成像，但粒种分离仍主要靠 GEANT4；最稳妥表述是“实测信号与缪子主导模型一致”。
- Sarjomaa/Nättilä 给出可以移入辐射 PIC 的轻量采样公式，真正性能要等生产代码集成与级联误差测试。
- Churchill 等同时给出代理加速和闭环失效：只有不确定性、几何可行性和真实 GX 回退同时存在，自动优化的高分才可信。
- Li 等指出铝材料表在高密低温与 10 kT 磁场下的模型选择会显著改变输运，但当前实验锚点没有覆盖最强差异区。
- 推荐阅读顺序：先看缪子论文图 1/9/10理解完整实验链，再看 AI-GX 图 8 的失败案例，最后用 QED 和 mDFT 的误差图判断数值方法适用域。
