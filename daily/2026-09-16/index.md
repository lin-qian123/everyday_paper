# 每日论文索引 - 2026-09-16

## 今日概览

- 运行日期：2026-09-16
- 新增论文数：3
- 最新性：官方 arXiv 目标分类在本轮可见的最新批次为 2026-09-15；新增两篇 2026-09-14 提交的预印本，并从同批次交叉列表补入一篇 2026-07-06 已正式发表于 *Physical Review E*、此前未入库的论文。
- 主题分布：高电荷 LWFA 束团出口 electron shedding 的 FREM 实验—FBPIC 机制链；ICP 中分布式感应/电容反馈的 phasor–PIC/MCC 算法；Fe/Ni 不透明度的 CNN–MLP–FiLM 代理。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`physics.med-ph`、`nucl-ex`、`physics.app-ph`、`physics.optics`、`astro-ph.HE`、`physics.atom-ph` 与 `physics.flu-dyn` 新增/交叉列表，并定向搜索激光等离子体、强场 QED、HEDP、PIC、等离子体 ML 和激光加速束应用。多源聚合器本轮返回 0 条可用记录，因此以官方分类页、arXiv 文章页和正式 DOI 元数据核验，不宣称穷尽所有数据库。
- 去重：按正式 DOI/arXiv identifier、规范化标题、历史 `daily/`、351 条完成台账、16 条重试队列、摘要和物理场景核对；三篇均未入库，重试队列不变。
- PDF / 正文：三份官方 arXiv 全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；全部完成 MinerU 正文/图件转换，保留并逐张查看 12 张关键图。完整记录见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Direct observation of electron shedding from a laser-plasma accelerator

- 标识符：[arXiv:2609.15968](https://arxiv.org/abs/2609.15968)；归档 DOI `10.48550/arXiv.2609.15968`
- 提交日期：2026-09-14；正文日期：2026-09-15
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-16/pdfs/Tata et al. - 2026 - Electron shedding from a laser-plasma accelerator.pdf`
- 中文笔记：[Tata et al. - 2026 - Electron shedding from a laser-plasma accelerator.md](notes/Tata%20et%20al.%20-%202026%20-%20Electron%20shedding%20from%20a%20laser-plasma%20accelerator.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：把高电荷 LWFA、沿出口位置扫描的飞秒相对论电子显微镜、准圆柱 FBPIC、合成诊断和头—尾能量账本接成同一机制链，直接指向束流提取区长期被低估的纵向相空间演化。
- 一句话总结：FREM 看到约 `550 pC` 高能束在下降沿延伸到数百微米并逐步丢失电子；作者 PIC 将其解释为激光失焦后束流接管尾场、头部向尾部转移约 `0.1 J` 并引发低能尾部脱落，但近 `20%` 主束能量损失、`2 MeV` 重建阈值和机制分解均是模拟/前向诊断量，不是逐电子直接测量。

### 2. A self-consistent phasor–PIC algorithm for bidirectional inductive–capacitive coupling in ICPs

- 标识符：[arXiv:2609.15043](https://arxiv.org/abs/2609.15043)；归档 DOI `10.48550/arXiv.2609.15043`
- 提交日期：2026-09-14
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-16/pdfs/Chen et al. - 2026 - Self-consistent phasor-PIC algorithm for ICPs.pdf`
- 中文笔记：[Chen et al. - 2026 - Self-consistent phasor-PIC algorithm for ICPs.md](notes/Chen%20et%20al.%20-%202026%20-%20Self-consistent%20phasor-PIC%20algorithm%20for%20ICPs.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：在离散层面统一每匝真空互阻抗、等离子体反电动势、Poisson 面通量表面电荷和分布式复数网络，并给出制造解、真空电感、历史 GEC 密度剖面和端口功率闭合的分层验证。
- 一句话总结：算法以 `2N+1` 个复数未知量逐 RF 周期更新线圈和电位，GEC 算例的功率不平衡约 `0.409–0.505%`；但高精度制造解主要是无粒子线性基准，实际算例仍是二维轴对称、基频、一周期延迟的作者 PIC/MCC，与历史探针数据的功率口径也不完全一致。

### 3. Opacity predictions in plasmas under stellar conditions using deep learning

- DOI：[10.1103/f237-bqz2](https://doi.org/10.1103/f237-bqz2)
- 正式发表：2026-07-06；作者稿 [arXiv:2609.13252](https://arxiv.org/abs/2609.13252) 于 2026-09-05 提交，并在 2026-09-15 的目标分类交叉列出
- 期刊 / 平台：*Physical Review E* **114**, 015204；本地保存 arXiv 作者稿
- 本地 PDF：`daily/2026-09-16/pdfs/Benredjem and Pain - 2026 - Deep-learning opacity predictions in stellar plasmas.pdf`
- 中文笔记：[Benredjem and Pain - 2026 - Deep-learning opacity predictions in stellar plasmas.md](notes/Benredjem%20and%20Pain%20-%202026%20-%20Deep-learning%20opacity%20predictions%20in%20stellar%20plasmas.md)
- 来源影响力分：8/10
- 专业相似度分：8/10
- 推荐理由：把 ILIade 超组态/统计跃迁数据、光谱代理、Rosseland/Planck 平均量和 FiLM 条件调制放在同一工作流中，并明确暴露 Ni 高温 L/M 壳层的困难区，适合作为 HEDP 原子物理 surrogate 的边界案例。
- 一句话总结：模型在指定 Fe/Ni 温密度网格内通常以 $10^{-3}$ 量级 MARE 复现 ILIade 平均不透明度，但 Ni Rosseland 最坏相对误差可接近 `8.98%`；结果是对单一原子代码的插值，没有跨代码、实验、OOD 或包含训练数据生成成本的端到端速度验证。

## 未入库候选与取舍

- `arXiv:2609.13554` 是氢/氘同位素对 H/L 转换影响的 50 页专题综述，覆盖面广但本轮原创结果密度低于三篇入选工作，保留作后续综述检索线索。
- `arXiv:2609.15101` 讨论晶体波荡器 γ 辐射，主要是器件/轨迹模拟，与当前激光等离子体—强场 QED—激光加速束应用主线的直接联系弱于入选论文，未用来扩充数量。
- 本批次未发现同时闭合“激光加速电子/离子束 → 转换靶/捕获器 → γ/中子/光核或活化产额 → 剂量/屏蔽”的新实验论文；仍不以仅有束流、仅有辐射模拟或相邻核物理主题替代端到端证据。
- PRE 不透明度论文并非 9 月新发表；本轮入库理由是正式 DOI 高相关、目标分类交叉列表首次暴露且历史台账无重复。索引同时保留正式发表日和作者稿日期，避免把交叉列出误写成新出版。

## 当日综合总结

- 三篇共同强调“耦合不能被过度压缩”：LWFA 出口仍有束—等离子体反馈，ICP 负载不能只写成固定线圈电流或一个集中阻抗，温密度条件对光谱代理也不能只靠无条件卷积。
- 最强的实验增量来自 electron shedding 的 FREM 扫描，但完整机制依赖合成诊断和 PIC；另两篇分别是算法验证和单一代码数据上的机器学习代理，均不是新实验发现。
- 推荐阅读顺序：先看 Tata 图 5 区分实验图样与合成诊断；再看 Chen 图 1 与功率表理解离散闭合；最后看 Benredjem 图 9、11、13、16，对比光谱峰、平均量和条件网络各自能证明什么。
