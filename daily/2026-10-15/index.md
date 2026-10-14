# 每日论文索引 - 2026-10-15

## 今日概览

- 运行日期：2026-10-15
- 新增论文数：6（1 篇 2026-10-14 正式 VOR，5 篇高相关官方 arXiv 预印本）。
- 最新性：官方 arXiv 目标分类最近 300 条的最新可见提交日期为 2026-10-13；Crossref 对 2026-10-13 至 15 执行 10 组主题查询，得到 1,000 条返回、720 个唯一 DOI，并用出版商页面与精确标题补核。安装的多来源搜索层 3 个定向查询均返回 0，故没有把其空结果解释为“无新论文”。
- 主题：硼氢离子电子碰撞、强场 QED-PIC、自旋/偏振正电子、激光质子靶多目标优化、等离子体多模态重建、束流/尾场生成代理，以及非均匀径向网格准静态 PIC。
- 去重：按 DOI/arXiv identifier、规范化标题、447 条完成台账、35 条重试队列、来源 URL、摘要与物理场景检查；6 篇均为未入库作品。
- PDF / 正文：6 份全文均通过 `%PDF-`、`file`、`pdfinfo`、`pypdf`、SHA-256 与非空 `pdftotext -layout`；共 122 页、56,246,645 字节，人工核查 6 个关键页并解码 6 幅保留图。MinerU 对 6 个公开 URL 均失败，明确使用已验证本地 PDF、695,741 字节布局文本和页面渲染回退。
- 重试：APS `10.1103/k2ht-nnz6` 与 Optica `10.1364/oe.612925` 的文章全文因 Cloudflare/404 或 HTML 验证页不可达；未从摘要生成笔记，队列 `35 → 37`。
- 覆盖边界：这是定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Low-energy electron collisions with BH+

- 标识符：[DOI: 10.1063/5.0354874](https://doi.org/10.1063/5.0354874)
- 发表：2026-10-14，*The Journal of Chemical Physics* 正式 VOR
- 中文笔记：[Mezlini et al. - 2026 - Low-energy electron collisions with BH plus.md](notes/Mezlini%20et%20al.%20-%202026%20-%20Low-energy%20electron%20collisions%20with%20BH%20plus.md)
- 来源影响力分：8/10；专业相似度分：8/10
- 推荐理由：给出硼化层受氢同位素等离子体侵蚀后关键分子离子的低能电子碰撞数据库，可服务边界等离子体组分与能量平衡建模。
- 一句话总结：MRCI、complex-Kohn 与 MQDT 共同预测低温 DR/VdE 占优、升温后 VE 增强及明显同位素效应；全文是理论计算，不是 ITER 边界等离子体测量。

### 2. SPIRE: Spin-Resolved Particle-in-Cell with Radiative Corrections for Extreme Laser--Plasma Interactions

- 标识符：[arXiv:2610.14664](https://arxiv.org/abs/2610.14664)
- 发表：2026-10-10，官方 arXiv 作者预印本
- 中文笔记：[Wu et al. - 2026 - SPIRE spin-resolved QED PIC.md](notes/Wu%20et%20al.%20-%202026%20-%20SPIRE%20spin-resolved%20QED%20PIC.md)
- 来源影响力分：8/10；专业相似度分：10/10
- 推荐理由：将经典 PIC、非线性 Compton/Breit–Wheeler、自旋进动、光子偏振与真空双折射/二色性合入同一验证框架。
- 一句话总结：多个模块与 SMILEI/既有论文算例一致，并复现锥靶偏振正电子方案；但源码位置未给出，且数值基准不能替代实验确认。

### 3. Multi-Objective Design of C-Shaped Targets for Energy--Divergence Control in Laser-Driven Proton Acceleration

- 标识符：[arXiv:2610.14824](https://arxiv.org/abs/2610.14824)
- 发表：2026-10-10，官方 arXiv 作者预印本
- 中文笔记：[Rezaei-Pandari et al. - 2026 - C-shaped laser proton targets.md](notes/Rezaei-Pandari%20et%20al.%20-%202026%20-%20C-shaped%20laser%20proton%20targets.md)
- 来源影响力分：7/10；专业相似度分：10/10
- 推荐理由：把二维 Smilei 与约束多目标贝叶斯优化结合，直接量化靶几何、能量、发散角和质子能量效率的冲突。
- 一句话总结：82 个设计中 60 个满足 `η_H≥9%`，15 点 Pareto 前沿覆盖 `28.64 MeV/52.51°` 到 `11.47 MeV/11.13°`；二维固定时刻结果不是实验靶最优解。

### 4. Toward a Multimodal Foundation Model for Plasma State Reconstruction

- 标识符：[arXiv:2610.15076](https://arxiv.org/abs/2610.15076)
- 发表：2026-10-10，NeurIPS 2026 Physical World AI workshop 官方 arXiv 预印本
- 中文笔记：[Xia et al. - 2026 - Multimodal plasma reconstruction.md](notes/Xia%20et%20al.%20-%202026%20-%20Multimodal%20plasma%20reconstruction.md)
- 来源影响力分：8/10；专业相似度分：9/10
- 推荐理由：用一个掩码时空网络统一处理等离子体稀疏诊断、跨模态补全、超分辨与时间缺失。
- 一句话总结：在 250 次固定 `βₑ₀=0.2` 的 VPIC 模拟上，`0.1%` 磁场可见率把隐藏密度的中位 NRMSE 约从 `0.9` 降至 `0.1`；尚无真实诊断或 sim-to-real 验证。

### 5. Learn the Dynamics, Enforce the Physics: Generative Latent Operators for High-Dimensional Beam Evolution

- 标识符：[arXiv:2610.14537](https://arxiv.org/abs/2610.14537)
- 发表：2026-10-10，官方 arXiv under-review 预印本
- 中文笔记：[Zou et al. - 2026 - GLOBE beam evolution.md](notes/Zou%20et%20al.%20-%202026%20-%20GLOBE%20beam%20evolution.md)
- 来源影响力分：8/10；专业相似度分：9/10
- 推荐理由：把生成式潜空间预测与无参数 Poisson/Maxwell 投影组合，直接面向三维束流与 PWFA 快速演化。
- 一句话总结：在两个 WarpX 数据集上相对强基线把相对 `L₂` 误差降低 `9%/13%`、报告 `102×/189×` rollout 加速，并把场约束残差压到 `10⁻⁷`；训练成本与跨代码/实机误差不在该速度比内。

### 6. QUARZ: a quasi-static particle-in-cell code with non-uniform radial grids for plasma wakefields

- 标识符：[arXiv:2610.16910](https://arxiv.org/abs/2610.16910)
- 发表：2026-10-12，官方 arXiv 作者预印本
- 中文笔记：[Pukhov and Wilson - 2026 - QUARZ plasma wakefields.md](notes/Pukhov%20and%20Wilson%20-%202026%20-%20QUARZ%20plasma%20wakefields.md)
- 来源影响力分：8/10；专业相似度分：10/10
- 推荐理由：为准静态尾场 PIC 提供守恒非均匀径向网格，并给出近轴强聚焦与 AWAKE 基准。
- 一句话总结：512 单元拉伸网格用约 `1/30` 的网格量达到 16000 单元均匀网格的近轴精度，单次 sweep `1.4 s` 对 `36.6 s`；收益来自特定多尺度案例且模型仍受准静态/低方位模限制。

## 当日综合总结

- 本轮唯一正式 VOR 是原子分子碰撞理论；其余五篇均为作者预印本，分别属于代码/模型验证、二维设计优化与合成模拟代理，不应写成独立实验发现。
- GLOBE 的场投影保证单帧约束而非全轨迹守恒；SPIRE/QUARZ 的模块或跨代码基准证明实现一致性，不构成源码审计或装置验收。
- C 形靶的 Pareto 解、Xia 的跨模态消融以及 GLOBE 的速度比分别受二维固定时刻、同分布 VPIC 数据与不计训练/数据生成成本限制。
- 本地没有运行 MRCI/Kohn/MQDT、SPIRE/SMILEI、Smilei 优化、VPIC/神经网络、WarpX/GLOBE 或 QUARZ/HiPACE++；只核验全文、图表、来源与结构化证据边界。
