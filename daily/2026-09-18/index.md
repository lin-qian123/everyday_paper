# 每日论文索引 - 2026-09-18

## 今日概览

- 运行日期：2026-09-18
- 新增论文数：3（1 篇正式开放论文，2 篇高相关 arXiv 预印本）
- 最新性：官方 arXiv 目标分类本轮可见的最新批次为 2026-09-17；两篇预印本均于 2026-09-16 提交。另补入 2026-03-02 正式发表但此前未入库的 DLA—MeV 光子—光中子端到端实验论文，不把它描述为“今日新发表”。
- 主题分布：过临界泡沫 DLA 电子与高 Z 转换靶的实验应用链；千焦 PW DLA 驱动 pair/muon 的 PIC—Geant4 可行性；Ti K 壳层 NLTE 光谱对 ICF SRS 热电子的历史数据再分析。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`、`physics.optics`、`physics.atom-ph`、`astro-ph.HE`、`nucl-th` 与 `hep-ph` 新增/交叉列表，并用 Crossref、APS、IOP 和期刊文章页复查正式来源。本地多源聚合器返回 0 条可用记录，因此采用官方分类页、DOI 元数据和文章页核验，不宣称穷尽所有数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、357 条完成台账、16 条重试队列和历史 `daily/` 核对；三篇入选稿均未入库。其余候选按物理场景、证据强度和近期主题重复度取舍。
- PDF / 正文：3 份官方 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；全部完成 MinerU 转换，保留并逐张查看 16 张关键图。正式 IOP 纯氘低温层靶论文因出版商返回 HTML/Radware 页面而未入库，进入结构化重试队列。详见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Ultrahigh flux of direct laser-accelerated electrons, MeV photons, and neutrons from overdense polymer foams

- 标识符：[DOI: 10.1103/5mpy-2jw5](https://doi.org/10.1103/5mpy-2jw5)
- 发表日期：2026-03-02
- 期刊 / 平台：*Physical Review Applied* **25**, 034003（正式论文，CC BY 4.0）
- 本地 PDF：`daily/2026-09-18/pdfs/Tavana et al. - 2026 - Ultrahigh-flux DLA electrons photons and neutrons.pdf`
- 中文笔记：[Tavana et al. - 2026 - Ultrahigh-flux DLA electrons photons and neutrons.md](notes/Tavana%20et%20al.%20-%202026%20-%20Ultrahigh-flux%20DLA%20electrons%20photons%20and%20neutrons.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：完整覆盖“预电离泡沫 DLA 电子 → Ta/Au 转换靶 → MeV 韧致辐射 → Au/Ta 光核活化 → 光中子”链条，同时给出束荷、角分布、光谱、转换效率和 GEANT4 靶厚扫描，是近期扩展应用主题中证据最完整的实验条目。
- 一句话总结：`60±4 J` PHELIX 主脉冲得到约 `300 nC` 的 `>1.5 MeV` 电子和 `20–30 nC` 的前向 `>7.5 MeV` 电子，实验反演 `>7 MeV` 光子约 `(2.07±1.08)×10¹¹ sr⁻¹`、激光到光子效率 `1.23±0.23%`，泡泡探测器对应约 `2×10⁹` 中子/发；最优光子/正电子/中子靶厚分别约 `3–4/5/>20 mm` 则来自作者 GEANT4，不是实验扫描。

### 2. Kilojoule-scale laser acceleration enabling efficient generation of electron-positron and muon beams

- 标识符：[arXiv:2609.18775](https://arxiv.org/abs/2609.18775)；归档 DOI `10.48550/arXiv.2609.18775`
- 提交日期：2026-09-16；正文日期：2026-09-17
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-18/pdfs/Babjak et al. - 2026 - Kilojoule DLA positron and muon beams.pdf`
- 中文笔记：[Babjak et al. - 2026 - Kilojoule DLA positron and muon beams.md](notes/Babjak%20et%20al.%20-%202026%20-%20Kilojoule%20DLA%20positron%20and%20muon%20beams.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把准三维 DLA 电子源、Pb 中的 pair/muon 输运、缪子解析标度和 pair beam 电流成丝串成统一设计链，并明确揭示固定束能下“总电荷/总能量比单电子截止能更重要”的工程规律。
- 一句话总结：作者模拟的 `1 PW/110 J` 与 `10 PW/1.125 kJ` 工作点分别产生 `35 nC >100 MeV` 和 `74 nC >400 MeV` 电子，GEANT4 预言最高约 `3×10¹²` 个正电子以及 `3.6×10⁴/6.5×10⁵` 个缪子；二维 OSIRIS 在传播约 `150 ps/45 mm` 后出现成丝，但全部是作者模拟，窄带正电子电荷和三维实验可观测性尚未达到“已验证注入源”。

### 3. K-shell x-ray spectroscopy: A reliable probe for stimulated Raman scattering in inertial confinement fusion

- 标识符：[arXiv:2609.18423](https://arxiv.org/abs/2609.18423)；归档 DOI `10.48550/arXiv.2609.18423`
- 提交日期：2026-09-16；正文日期：2026-09-17
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-18/pdfs/Luo et al. - 2026 - K-shell SRS spectroscopy.pdf`
- 中文笔记：[Luo et al. - 2026 - K-shell SRS spectroscopy.md](notes/Luo%20et%20al.%20-%202026%20-%20K-shell%20SRS%20spectroscopy.md)
- 来源影响力分：6/10
- 专业相似度分：8/10
- 推荐理由：把双 Maxwell 热尾如何改变 Ti 电荷态、K 壳层主线/卫星线以及历史 Nova 光谱拟合按原子动力学链条说明清楚，可作为 ICF 中 SRS 光学诊断的局域互补手段。
- 一句话总结：固定 `ne=10²¹ cm⁻³`、`Thot=19 keV` 的 NLTE 模型在 `Te≈1–2 keV` 对热电子比例最敏感，重新拟合 Nova 四时刻得到 `f=2%、9%、4%、5%` 并跟随独立 SRS loss 的主趋势；这是历史数据的模型再分析，局域热电子数分数不能等同于全局 SRS 能量损失。

## 未入库候选与取舍

- `10.1088/1741-4326/ae9edc`（*Nuclear Fusion*，2026-09-17 online）报告 Shenguang 间接驱动纯氘低温层靶实验，摘要给出 `9.6×10¹⁰` 中子产额、`30 Gbar` 热点压力和 `19%` clean yield，主题和来源都很强；但 IOP PDF、DOI 与文章页均返回 HTML/Radware 验证页，且本轮未找到合法开放作者稿。已新增到 `state/daily_retry_candidates.json`，不根据摘要生成全文笔记。
- `arXiv:2609.17661` 用一维 PIC 研究 magnetar 级强场中的 pair cascade 与回旋吸收，强场相关但天体场景和一维模型与本轮两篇二级源应用重合度低，保留为后续强场专题候选。
- `arXiv:2609.18517` 讨论重离子束驱动的等离子体尾场，属于相邻束流加速方向；本轮优先 DLA—转换靶—pair/muon 的完整应用链。
- `arXiv:2609.17751`（W7-X pellet）与 `arXiv:2609.17938`（Landau damping）分别偏磁约束实验和基础理论，质量合格，但当前主题优先级低于激光加速束应用与 ICF 诊断。
- 形式化来源复查没有发现与三篇入选稿重复的既有台账记录；正式 Tavana 论文虽发表于 3 月，但此前未收录，作为扩展应用方向的历史遗漏补入并明确标注日期。

## 当日综合总结

- 今天最强实验增量是 Tavana：一次电子束、光核活化、角分布和中子剂量都来自实际 PHELIX shots；其谱反演和峰值通量带模型/时间假设，正电子及最优厚度是 GEANT4。
- Babjak 把同类 DLA 驱动束外推到 pair plasma、加速器注入与缪子源，是可行性数值设计，不得与 Tavana 的实验结果合并成“千焦 pair/muon 已实现”。
- Luo 给出诊断方法增量：K 壳层光谱通过原子动力学间接看 SRS 热电子。它和背散射损失相关，但不是相同 observable。
- 推荐阅读顺序：先看 Tavana 图 1/2/8/10 闭合实验链；再看 Babjak 图 3/4c/6 理解转换厚度、能量预算和集体效应；最后看 Luo 图 1/3/4 区分谱线敏感性、历史拟合和 SRS 代理边界。
