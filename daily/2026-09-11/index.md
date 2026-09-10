# 每日论文索引 - 2026-09-11

## 今日概览

- 运行日期：2026-09-11
- 新增论文数：3
- 正式来源优先：补入 2026-09-10 接收的 Physical Review E 非局域输运论文；本地全文明确使用对应作者预印本 arXiv:2508.17309，不是 APS 排版版。
- 预印本增量：官方 arXiv 当前批次补入纳米线靶偏振正电子二维 QED-PIC 方案和覆盖 collisionless / relativistic / electromagnetic / collisional plasma 的广义相似理论。
- 主题分布：磁化 ICF 非局域热输运与 Biermann/Nernst 修正、强场 QED positron angle–spin correlation、PIC/fluid 缩比相似律。
- 检索范围：检查 APS PRL / PRE accepted 页面，并通过官方 arXiv Atom API 扫描 `physics.plasm-ph`、`physics.acc-ph`、`physics.ins-det`、`physics.med-ph`、`nucl-ex` 等近期记录；随后按强场 QED、激光尾场、PIC、HEDP 和束流应用定向核对全文来源。搜索聚合器本轮没有返回可用结果，因此候选发现以官方 APS/arXiv 来源为主，不宣称覆盖全部数据库。
- 去重：按正式 DOI / arXiv identifier、规范化标题、历史 daily、完成台账、重试队列、摘要与物理场景核对 `state/processed_articles.json`。3 篇均未进入 338 条完成台账；Zhang 的 nonlinear Breit–Wheeler 纳米线角偏振与昨日 linear Breit–Wheeler 后向压缩反应通道不同；Fu 是通用 Boltzmann–Maxwell 相似理论，不等同于已有单装置 scaling；Chen 首次以正式接收元数据和合法作者稿入库。
- PDF / 正文：3 份官方 arXiv PDF/作者稿均通过 `%PDF-`、`file`、`pdfinfo` 页数、SHA-256 和非空 `pdftotext -layout`；3 篇均使用当前可用 `MINERU_API_KEY` 完成 Markdown / 图件提取，共选取 14 张关键图并逐张解码查看。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. An improved nonlocal electron heat transport model for magnetized plasmas

- 正式 DOI：[10.1103/mwjc-s21x](https://doi.org/10.1103/mwjc-s21x)
- PRE 接收日期：2026-09-10
- 正式来源：[APS accepted paper](https://journals.aps.org/pre/accepted/10.1103/mwjc-s21x)
- 作者稿：[arXiv:2508.17309](https://arxiv.org/abs/2508.17309)
- 期刊 / 平台：Physical Review E accepted paper；本地全文为作者预印本
- 本地 PDF：`daily/2026-09-11/pdfs/Chen et al. - 2026 - Improved nonlocal electron heat transport in magnetized plasmas.pdf`
- 中文笔记：[Chen et al. - 2026 - Improved nonlocal electron heat transport in magnetized plasmas.md](notes/Chen%20et%20al.%20-%202026%20-%20Improved%20nonlocal%20electron%20heat%20transport%20in%20magnetized%20plasmas.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：把 magnetized SNB 多群热流、含密度扰动的 Biermann 电场、nonlocal Nernst 与 Righi–Leduc 离散稳定性接成一条可嵌入 FLASH 的模型链。
- 一句话总结：作者模型在 He/Zr 温度坡面、$Z=1$ Biermann 抑制和简化 Be laser-solid 测试中复现多项 K2 VFP 趋势，并显示非局域模型把峰值温度由约 1.8 keV 改为约 2.1 keV且重排约 1.3 MG 磁场；这些是作者模型/VFP benchmark，不是实验或本地 FLASH 复现。

### 2. High-charge, highly polarized positron beams generated from a laser-driven nanowire-array target

- DOI：[10.48550/arXiv.2609.09908](https://doi.org/10.48550/arXiv.2609.09908)
- arXiv v1：2026-09-09
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.09908)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-11/pdfs/Zhang et al. - 2026 - High-charge polarized positrons from nanowire target.pdf`
- 中文笔记：[Zhang et al. - 2026 - High-charge polarized positrons from nanowire target.md](notes/Zhang%20et%20al.%20-%202026%20-%20High-charge%20polarized%20positrons%20from%20nanowire%20target.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把 NBW 出生时 $B_z$–$S_z$ 统计相关与后续 transverse Lorentz impulse 接起来，明确解释纳米线怎样减少角 bin 内的相反自旋抵消。
- 一句话总结：作者的二维 spin-resolved QED-PIC 在 $a_0=1500$、$n_e=200n_c$ 纳米线参考算例中给出最大 $|\bar S_z|\approx0.46$，满足 $|\bar S_z(\theta)|>0.3$ 的角选择电荷约 308 nC；这是极端理想条件下的二维模拟，不是已产生或可直接输运的实验束团。

### 3. Generalized Similarity Theory for Plasmas

- DOI：[10.48550/arXiv.2609.08413](https://doi.org/10.48550/arXiv.2609.08413)
- arXiv v1：2026-09-08
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.08413)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-11/pdfs/Fu - 2026 - Generalized similarity theory for plasmas.pdf`
- 中文笔记：[Fu - 2026 - Generalized similarity theory for plasmas.md](notes/Fu%20-%202026%20-%20Generalized%20similarity%20theory%20for%20plasmas.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：从 Boltzmann 加完整 Maxwell 方程给出统一 scaling exponents，并用两流、相对论二极管、RF 驻波与跨电离区放电展示相似条件和破坏项。
- 一句话总结：作者推导长度/时间同缩放、速度不变、场随逆长度缩放的变换，并以 PIC/fluid 模拟展示无碰撞密度 $k^2$、强电离碰撞密度 $k$ 的不同极限；相似性依赖初始、边界、碰撞和驱动共同缩放，不是任意真实等离子体都可无损缩小。

## 未入库但需保留的候选

- [Nuclear polarization by intense laser pulses](https://journals.aps.org/prl/accepted/10.1103/p7k8-mjn7) 是 2026-09-09 接收的 PRL 理论/数值方案；accepted abstract 报告单脉冲可超过 10% 并设想脉冲序列接近完全极化，但本轮项目安全下载器对 accepted 和 DOI 路径均得到 `HTTP 403` HTML，未找到合法开放全文。已加入结构化重试队列，不能从摘要扩写完整笔记，也不能把预测写成已实现核极化。
- [Nonthermal electron acceleration and transition probability density in turbulent wakefields driven by an intense laser pulse](https://journals.aps.org/pre/accepted/10.1103/nc7w-yr34) 是 2026-09-10 接收的 PRE 1D PIC / stochastic-transport 工作；摘要给出低能 Brownian+Lévy、中能 Lorentzian TPD 和高能 ballistic 分区。本轮 accepted / DOI 下载同样为 `HTTP 403`，已加入重试队列；没有全文时不把 $\gamma^{-2}$ 尾部机制扩写成已复核结论。
- [First experimental evidence of helicon current drive](https://journals.aps.org/prl/accepted/10.1103/mbn4-fd4v) 仍是高价值 DIII-D 实验候选；本轮 exact-title arXiv 核对未发现对应作者稿，继续只保留 accepted metadata，等待合法全文。
- `10.1103/sgyf-lrw1`、`10.1103/2rqf-hq77` 与 `10.1103/d45l-hsgg` 保留在上一轮的 APS blocked 候选记录；本轮没有重复触发下载，不能把旧的 2026-09-10 `HTTP 403` 记录冒充今天的新复查。

## 当日综合总结

- Chen 的价值在于把非局域热流与磁场生成/搬运统一到同一分布函数扰动：热流、Biermann 和 Nernst 不是三个可独立调 limiter 的旋钮。密度扰动决定强非局域 Biermann 抑制能否合理，横向热流又对离散稳定性提出额外要求。
- Zhang 说明偏振束流优化应以 angle-resolved usable charge 而非总 pair yield 为目标。0.46 和 308 nC 均是二维 QED-PIC 预测；真正实验链仍缺三维、预等离子体、制造容差、传输、背景和 polarimeter 接受度。
- Fu 提供的是受控缩比的方程级检查表。最应保留的是 prototype/downscaled 下标方向，以及 weakly ionized $k^2$ 与 highly ionized $k$ 两种密度极限；过渡区温度修正的证据强度低于无碰撞对称性推导。
- 推荐阅读顺序：先读 Chen 看 kinetic-to-MHD 闭包如何影响 observable，再读 Zhang 看 strong-field QED 的 angle–spin correlation；最后用 Fu 的 scaling checklist 检查计划缩小的 PIC 或放电算例是否真的保持全部无量纲条件。
