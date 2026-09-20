# 每日论文索引 - 2026-09-21

## 今日概览

- 运行日期：2026-09-21
- 新增论文数：3（2 篇 2026-09-18 正式期刊论文，1 篇 2026-09-07 高相关 arXiv 专题候选）
- 最新性：官方 arXiv 目标分类本轮可见的最新批次仍为 2026-09-18，周末没有更晚的新提交批次；因此以 Crossref 2026-09-18 至 2026-09-21 正式出版元数据为主，并补入上轮明确保留、与“聚变中子—医用同位素”应用链直接相关的 `arXiv:2609.19166`。没有把该预印本写成 9 月 21 日新投稿。
- 主题分布：纳秒激光产生高电荷铁等离子体的 EUV 光谱/辐射输运诊断；IFMIF/EVEDA 高流氘束、液态锂靶与聚变材料中子源工程验证；D–T 中子和热中子链制备 `²²⁸Th/²²⁹Th` 发生器母体的 OpenMC 产能情景。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det`、`physics.optics`、`physics.atom-ph`、`nucl-th` 与 `hep-ph` 最新列表，以 Crossref、出版商、DOI 和机构库页面核验 2026-09-18 后正式来源；本地多源搜索器本轮返回 0 条，最终选择不依赖聚合器排序，也不宣称穷尽所有数据库。
- 去重：按 DOI/arXiv identifier、规范化标题、363 条完成台账、17 条旧重试队列和历史 `daily/` 核对。前两篇未入库；第三篇曾在 2026-09-20 索引中明确列为后续专题候选，今天作为 backlog 补入而不是重复处理。
- PDF / 正文：3 份全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；Zhu 与 Parisi 完成 MinerU，IFMIF 文件在 MinerU 两次失败后使用本地文本、嵌图提取与页面渲染 fallback。共保留并逐张查看 14 张关键图。详见 [pdf_validation.json](pdf_validation.json)。
- 来源边界：IFMIF 的正式出版元数据来自 *Nuclear Fusion*，本地可读全文是 QST 机构库的 IAEA 作者/会议稿而不是 IOP VOR；正式 MAST-U ML tomography 论文因 IOP/Radware 只返回 HTML，未从摘要生成笔记，已加入结构化重试队列。

## 论文清单

### 1. Spectral characteristics and plasma state diagnosis of highly charged iron ions in laser-produced plasma

- 标识符：[DOI: 10.1088/2058-6272/ae82da](https://doi.org/10.1088/2058-6272/ae82da)
- 发表日期：2026-09-18
- 期刊 / 平台：*Plasma Science and Technology* **28**, 095501（正式期刊论文）
- 本地 PDF：`daily/2026-09-21/pdfs/Zhu et al. - 2026 - Spectral diagnosis of highly charged iron laser plasma.pdf`
- 中文笔记：[Zhu et al. - 2026 - Highly charged iron plasma spectral diagnosis.md](notes/Zhu%20et%20al.%20-%202026%20-%20Highly%20charged%20iron%20plasma%20spectral%20diagnosis.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：把真实纳秒激光铁等离子体 EUV 谱、Cowan 原子结构、羽流成像和含自吸收的 SpeIma3D 辐射输运连成完整诊断链，并保留了明显拟合残差，适合作为 HEDP 光谱反演的边界案例。
- 一句话总结：`850 mJ, 10 ns, 1064 nm` 激光产生的 `9.5–12 nm` 谱由 `Fe⁸⁺–Fe¹²⁺` 多组跃迁解释，模型反演中心 `Tₑ≈38.4 eV`、`Nion≈5.6×10¹⁹ cm⁻³`、`⟨Z⟩≈8.86`；后三者依赖 LTE、高斯空间分布和单视线路径，并非独立探针直接实测。

### 2. Overview of achievements and outlook of the IFMIF/EVEDA project

- 标识符：[DOI: 10.1088/1741-4326/aea171](https://doi.org/10.1088/1741-4326/aea171)
- 发表日期：2026-09-18
- 期刊 / 平台：*Nuclear Fusion* **66**, 116020（正式开放论文，CC BY 4.0）
- 本地 PDF：`daily/2026-09-21/pdfs/Hasegawa et al. - 2026 - IFMIF EVEDA achievements and outlook.pdf`（QST 作者/会议稿，不是 IOP VOR）
- 中文笔记：[Hasegawa et al. - 2026 - IFMIF EVEDA achievements and outlook.md](notes/Hasegawa%20et%20al.%20-%202026%20-%20IFMIF%20EVEDA%20achievements%20and%20outlook.md)
- 来源影响力分：9/10
- 专业相似度分：8/10
- 推荐理由：给出高流氘束—束损—RFQ 热问题—SRF—液态锂回路—辐射监测的工程状态，能直接约束“聚变中子源可用于材料/核应用”之前还缺哪些装置验证。
- 一句话总结：LIPAc 已在 `5 MeV` 脉冲模式达到约 `119–125 mA`，最终 Phase B+ 为 `8.75% duty`、RFQ 透射约 `90%`，锂回路与远距离表面诊断也有试验结果；目标 `9 MeV, 125 mA, CW`、1.125 MW 长时运行和完整 D–Li 源尚未实现。

### 3. Scalable Production of Lead-212 and Actinium-225 Generators with Fusion Neutrons

- 标识符：[arXiv:2609.19166](https://arxiv.org/abs/2609.19166)；归档 DOI `10.48550/arXiv.2609.19166`
- 提交日期：2026-09-07
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-21/pdfs/Parisi and Rutkowski - 2026 - Fusion neutrons for Pb-212 and Ac-225 generators.pdf`
- 中文笔记：[Parisi and Rutkowski - 2026 - Fusion neutrons for isotope generators.md](notes/Parisi%20and%20Rutkowski%20-%202026%20-%20Fusion%20neutrons%20for%20isotope%20generators.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 D–T 快中子、热中子、钍/镤/镎原料与 `²¹²Pb/²²⁵Ac` 发生器供应连接起来，直接覆盖本仓库扩展的中子—同位素—诊疗应用方向，同时明确关键核截面仍待实验。
- 一句话总结：OpenMC/耗减情景预测 `10 MW` D–T 源照射含 `27% ²³⁰Th` 的吨级钍约 6 个月可积累约 `250 Ci ²²⁹Th`，换算为五百万个年度 `²²⁵Ac` reference dose-equivalents；这是模型供应指标，不是患者数、实际产线或已验证靶产额。

## 未入库候选与取舍

- `10.1088/1361-6587/aea4f2`（*PPCF*）是 MAST-U 稀疏视角软 X 射线机器学习层析正式论文，主题与 ML 诊断高度相关；官方 IOP PDF、DOI 和 Radware 路径仅返回 HTML，未找到合法开放作者稿，因此不从摘要生成笔记，并新增至重试队列。
- `10.1088/1361-6587/aea366` 研究 double-cone ignition 金锥抗压，属于辐射流体/靶设计正式论文；本轮已有一篇激光等离子体实验诊断和一篇中子源工程综述，故暂不挤入当日三篇。
- `10.1088/1361-6587/aea24b` 是强纳秒激光致密等离子体超越自相似阶段的时间分辨研究，相关性高但与本轮 Zhu 的纳秒激光诊断主题重叠，优先保留证据链更完整且全文已验证者。
- `10.1063/5.0352958`（*Physics of Plasmas*）提出 DeepPropNet 预测热等离子体性质，ML 方法质量合格；场景偏热等离子体性质代理，本轮优先更直接的 HEDP 光谱、中子源与医用同位素应用链。

## 当日综合总结

- Zhu 说明高电荷铁 EUV 谱能约束温度/密度/电荷态，但只有把原子结构、空间几何和辐射输运假设一起写出，反演数值才有物理含义。
- Hasegawa 说明聚变中子源的瓶颈不仅是加速器峰值电流，还包括占空比、RF 耦合器热稳定、束损监测、液态锂表面与长期可用率；现有进展不能写成 IFMIF 已完成 9 MeV CW 验收。
- Parisi 把中子源连接到治疗同位素发生器库存，但其醒目产能数字仍是核数据、源强、靶量、冷却和理想回收日程共同决定的场景结果。
- 推荐阅读顺序：先看 Zhu 图 1/3/8c 区分观测与谱反演；再看 IFMIF 图 2、图 4–6、图 11–13 理解工程验证层级；最后看 Parisi 图 2/3/4/9，把反应路径、几何和模型产额联系起来。
