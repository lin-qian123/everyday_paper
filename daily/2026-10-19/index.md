# 每日论文索引 - 2026-10-19

## 今日概览

- 新增 **3 篇去重作品**，台账 **470 → 473**：1 篇 10 月 16 日正式 VOR、2 篇 10 月 12—13 日官方作者预印本，分别覆盖微聚束相干辐射、隐式 PIC–MCC 与磁几何/湍流验证。
- 3 份 PDF 共 **49 页、5,259,781 字节**，通过文件头、类型、SHA-256、pdfinfo/pypdf 页数一致和全页文本检查；275,238 字节布局文本保留本地。MinerU pipeline **2 成功、1 失败后本地验证回退**，目视核查 10 个首页/关键页，保留 6 幅原图摘录（其中一幅包含原文 Figs. 4、5）。
- 搜索层 1 组查询无返回；Crossref 10 组近期查询得到 750 行、543 个唯一 DOI，再以较宽日期窗的 4 组相关性查询得到 280 行、256 个 DOI。两组计数各自去重，不能相加称为唯一论文数。官方 arXiv 五类最近 300 条最新可见投稿仍为 10 月 15 日。覆盖有界，不宣称全球穷尽。
- 重试队列 **40 → 42**：新增两篇温稠密物质候选。Ghosh 正式论文需订阅，harvest 返回 401，官方注明 CHORUS 作者稿 2027-10-13 开放；Rajai 目前是 10-15 接受记录，harvest 返回 404。精确标题未找到可用合法作者稿，未生成摘要替代笔记。既有相位锁定 LWFA 项复查仍为 404，记录本次真实重试时间。
- 本次没有选出新的激光转换靶—光核/中子端到端实测增量或强场 QED 全文。未为补齐主题而加入弱相关条目。

## 论文清单

### 1. Generation of mode-locked EUV and soft X-ray radiation via coherent Thomson scattering from a density-modulated electron bunch

- [DOI](https://doi.org/10.1007/s41365-026-02075-1)，*Nuclear Science and Techniques* 37, 250，2026-10-16 正式 VOR。
- [中文笔记](notes/Wang%20et%20al.%20-%202026%20-%20Mode%20locked%20coherent%20Thomson%20radiation.md)
- 来源影响力分 8/10；专业相似度分 9/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：直接连接束流纵向微结构、相干场叠加、谱齿间距与时间脉冲列，并明确极端发射度限制。
- 一句话结论：约 124 eV 的计算频梳齿距由种子设定为 1.55/3.10/6.20 eV，约 0.3 fs 是理想模型脉冲列宽度，尚非源实验或绝对通量结果。

### 2. Implicit PIC Simulations of Hydrogen Plasmas with Intense Negative Ion Production

- [官方 arXiv v1](https://arxiv.org/abs/2610.16257v1)，2026-10-12，作者预印本，未核实同篇正式版。
- [中文笔记](notes/Eremin%20-%202026%20-%20Implicit%20PIC%20hydrogen%20negative%20ions.md)
- 来源影响力分 7/10；专业相似度分 8/10。
- 推荐理由：守恒 PIC–MCC、振动分子壁面闭合与负离子损失共同决定离子源模型结果，避免只看平均温度或密度峰值。
- 一句话结论：5 Pa 数值放电中，surfatron 的峰密度比 nH⁻/ne≈0.23，CCP 体区接近 2；这是局域密度而非提取束流或能效。

### 3. Validation of geometric proxies using negative and positive triangularity plasmas with varying elongation on TCV and multi-machine gyrokinetic simulations

- [官方 arXiv v1](https://arxiv.org/abs/2610.17974v1)，2026-10-13，作者预印本，PDF 仍为 IOP 投稿模板。
- [中文笔记](notes/Balestri%20et%20al.%20-%202026%20-%20Geometric%20proxies%20for%20negative%20triangularity.md)
- 来源影响力分 8/10；专业相似度分 8/10。
- 推荐理由：用可解释几何量做趋势预判，再以实验和非线性模型检验，并保留无法稳定到达的低拉长比区域。
- 一句话结论：TCV 高拉长比下约 1.5 倍的 βN/H98y2 改善有配对实测支持，低 κ 的反转及 DIII-D/AUG/JET 热通量倍数仍属模拟。

## 当日综合总结

优先阅读 Thomson 论文中相干求和的条件与图 5、6；它与既有激光脉冲列硬 X 射线频梳是不同作品，不能互借光子产额或束长条件。PIC 笔记适合检查离子源的化学闭合与守恒算法；磁几何工作提供实验与人工系数交换如何相互支持的案例。

- **直接实验：** TCV 配对放电支持高、低拉长比的趋势差别；未直接实现 κ≲0.75 的预测反转，也不能把 1.5 倍约束指标当作聚变增益。
- **计算：** 辐射计算为理想逐电子经典模型；负离子为 PIC–MCC 加 RLM 振动态闭合；多装置磁湍流热通量为固定剖面的局域 GENE 结果。没有本地复跑这些模型。
- **全文：** 三篇均取得真实 PDF。MinerU 两篇预印本成功，正式 Thomson 论文返回解析失败，已通过本地正文和原页回退核验。
- **未闭合项：** 真实束流相干容差、绝对光子数、负离子提取与化学不确定性、低 κ 实验/偏滤器/杂质效应；两篇温稠密物质候选只保留来源与重试证据。

## 维护与证据记录

- [PDF 逐篇核验](pdf_validation.json)
- [检索覆盖、去重及选择](research/research-run.json)
- [正式版与精确标题检查](research/version-checks.json)
- [原始来源元数据](research/sources.jsonl)与[入库清单](research/import-manifest.json)
- [MinerU 成功/失败记录](research/mineru-attempts.json)
- [原图来源、裁框与哈希](research/figure-manifest.json)
- [验证与发布准备记录](run_results.json)

PDF、布局文本和 MinerU 正文按现有规则保留本地并由 Git 忽略；中文笔记、原图摘录、元数据、下载报告和索引随 Git 发布。
