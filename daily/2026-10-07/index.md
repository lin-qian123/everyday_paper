# 每日论文索引 - 2026-10-07

## 今日概览

- 运行日期：2026-10-07
- 新增论文数：5（1 篇 Springer 正式 version of record、1 篇 APS accepted paper 对应作者预印本、3 篇官方 arXiv 预印本）
- 版本更新：既有 PHITS AI-agent 条目由 `arXiv:2607.11309` 合并升级为正式 DOI `10.1080/00223131.2026.2742550`，不重复计数；正式 VOR 正文仍不可达，本地全文仍为原作者预印本。
- 最新性：官方 arXiv 目标分类已出现 2026-10-05 投稿；Crossref 对 2026-10-06 至 10-07 的 5 组主题查询得到 240 条去重作品。安装的多来源搜索层对 3 个定向查询返回 0 条，故转用官方 arXiv、Crossref 与出版社来源。
- 主题：相对论量子对等离子体、2 keV 中子低阈探测器标定、等离子体波导过渡层、辛神经网络加速器正规形，以及磁化激波中的辐射反作用。
- 去重：按 DOI/arXiv、规范化标题、415 条完成台账、22 条重试队列、来源 URL、正式版关系、摘要和物理场景检查；5 篇均为新作品，PHITS 只更新原记录。
- PDF / 正文：5 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；共 67 页，人工核查 24 个关键页并解码 5 幅关键图。MinerU 本地路径不受支持，5 个公开 URL 任务均失败，故明确使用已验证本地 PDF、布局文本和渲染回退。
- 重试：HL-3 CXRS `10.1088/1741-4326/aeb037` 复查仍为 HTML；新增 PRE 毛细管等离子体 `10.1103/yrts-62hs` 与 JNST `99Tc(n,γ)` `10.1080/00223131.2026.2729210`，队列 `22 → 24`。
- 覆盖边界：定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Nonlinear excitations in a relativistic pair plasma with quantum corrections

- 标识符：[DOI: 10.1140/epjp/s13360-026-08377-y](https://doi.org/10.1140/epjp/s13360-026-08377-y)
- 发表：2026-10-06；*The European Physical Journal Plus* 141, 1143；Springer 正式 version of record
- 本地 PDF：`daily/2026-10-07/pdfs/Imran et al. - 2026 - Quantum relativistic pair plasma nonlinear excitations.pdf`
- 中文笔记：[Imran et al. - 2026 - Quantum relativistic pair plasma nonlinear excitations.md](notes/Imran%20et%20al.%20-%202026%20-%20Quantum%20relativistic%20pair%20plasma%20nonlinear%20excitations.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：把相对论简并、Bohm 势与交换—关联修正放进同一 KdV 约化，可清楚区分幅度与宽度的参数来源。
- 一句话总结：交换—关联项同时改变孤波幅度和宽度，Bohm 项主要增宽；这是归一化量子流体参数扫描，不是激光或天体实验预测。

### 2. Design studies of a pulsed quasimonoenergetic 2-keV neutron source for calibration of low threshold dark matter detectors

- 标识符：[DOI: 10.1103/fqgp-916r](https://doi.org/10.1103/fqgp-916r)
- 版本：APS 2026-10-06 accepted paper；本地全文为同作品 [arXiv:2410.14722v1](https://arxiv.org/abs/2410.14722) 作者预印本，不是 VOR
- 本地 PDF：`daily/2026-10-07/pdfs/Chaplinsky et al. - 2026 - Pulsed 2-keV neutron calibration source.pdf`
- 中文笔记：[Chaplinsky et al. - 2026 - Pulsed 2-keV neutron calibration source.md](notes/Chaplinsky%20et%20al.%20-%202026%20-%20Pulsed%202-keV%20neutron%20calibration%20source.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：把 DT 源、慢化、反共振滤波、复合屏蔽、符合标签与低能核反冲标定连成一条可审计 GEANT4 设计链。
- 一句话总结：最优设计给出约 `50%` 的 2 keV 谱纯度，并在模拟中分辨约 `10 eV` 反冲峰；整机、绝对通量和材料容差尚未由实验闭合。

### 3. Effect of transition layer on wakefield in plasma waveguide

- 标识符：[arXiv:2610.06396](https://arxiv.org/abs/2610.06396)
- 版本：2026-10-05，官方 arXiv v1
- 本地 PDF：`daily/2026-10-07/pdfs/Markov et al. - 2026 - Transition layer in plasma waveguide wakefield.pdf`
- 中文笔记：[Markov et al. - 2026 - Transition layer in plasma waveguide wakefield.md](notes/Markov%20et%20al.%20-%202026%20-%20Transition%20layer%20in%20plasma%20waveguide%20wakefield.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：直接量化实际密度过渡层对正/电子见证束的非对称影响，并给出密度与注入相位两类补偿方案。
- 一句话总结：`100 μm` 过渡层使固定相位正电子增益降低 `3.14×`，但同代码内重新优化可补偿；证据限于冷等离子体 2.5D PIC。

### 4. Reveal normal form structure for nonlinear map in accelerator beam physics with symplectic neural network

- 标识符：[arXiv:2610.05635](https://arxiv.org/abs/2610.05635)
- 版本：2026-10-05，官方 arXiv v1
- 本地 PDF：`daily/2026-10-07/pdfs/He and Hao - 2026 - Symplectic neural network accelerator normal form.pdf`
- 中文笔记：[He and Hao - 2026 - Symplectic neural network accelerator normal form.md](notes/He%20and%20Hao%20-%202026%20-%20Symplectic%20neural%20network%20accelerator%20normal%20form.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：用可逆辛网络提取振幅相关正规形，并把最大振幅下的失真作为明确的失败证据保留下来。
- 一句话总结：小—中振幅轨道的相移标准差约 `1–4×10^-5 rad`，但完整映射只近似辛，尚无真实晶格和同精度性能对照。

### 5. Radiation Reaction in Relativistic Magnetized Shocks of Neutron Star Magnetospheres

- 标识符：[arXiv:2610.05386](https://arxiv.org/abs/2610.05386)
- 版本：2026-10-04，官方 arXiv v1
- 本地 PDF：`daily/2026-10-07/pdfs/Vanthieghem and Levinson - 2026 - Radiation reaction in relativistic magnetized shocks.pdf`
- 中文笔记：[Vanthieghem and Levinson - 2026 - Radiation reaction in relativistic magnetized shocks.md](notes/Vanthieghem%20and%20Levinson%20-%202026%20-%20Radiation%20reaction%20in%20relativistic%20magnetized%20shocks.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：以多流体理论和一维动理学 PIC 同时约束强冷却激波的混沌阈值、谱峰和相干辐射效率。
- 一句话总结：临界 Mach 数近似 `2+12.6τ^0.45`，峰频率按 `τ^(2/7)` 上移；映射到 magnetar/FRB 仍是强模型依赖外推。

## 版本合并

- **Toward AI-Agent-Driven Particle Transport Simulations**：既有 [2026-07-15 中文笔记](../2026-07-15/notes/Tatsuhiko%20Sato%20et%20al.%20-%202026%20-%20Toward%20AI-Agent-Driven%20Particle%20Transport%20Simulations.md) 已补入正式 *Journal of Nuclear Science and Technology* DOI `10.1080/00223131.2026.2742550` 与 2026-10-06 online 状态。正式 PDF 仍受来源访问限制，因此没有把原 arXiv 全文误写为 VOR，也没有新建重复条目。

## 当日综合总结

- 本轮覆盖“理论—设计—数值—机器学习”四类证据，没有新增直接实验论文。量子对等离子体是解析/KdV 参数扫描；中子源是 GEANT4 工程设计；波导与磁化激波分别是 2.5D 和 1D PIC；辛网络只在玩具映射训练。
- 与激光束流应用最接近的是中子源的慢化—滤波—屏蔽—标签链和波导过渡层容差，但前者不包含激光源的宽谱、EMP 与逐发波动，后者也没有三维、束流品质或真实密度测量。
- 辐射反作用论文给出可核验的阈值与频率标度，却不能替代 magnetar 传播和观测响应；PHITS 本轮仅升级出版元数据，没有重新运行输运案例。
- 本轮没有运行 KdV 系数复算、GEANT4/MCNP、SOM、SympNet、Entity 或 PHITS；所有结果均按作者证据及本地全文核读处理。
