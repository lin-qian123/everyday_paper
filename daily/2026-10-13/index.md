# 每日论文索引 - 2026-10-13

## 今日概览

- 运行日期：2026-10-13
- 新增论文数：6（2 篇最新正式出版记录对应作者预印本全文；4 篇 2026-10-09 官方 arXiv 预印本）。
- 最新性：官方 arXiv 目标分类筛得 2026-10-09 的新批次；Crossref 对 2026-10-09 至 10-13 做 8 组主题查询，得到 694 个唯一元数据记录。安装的多来源搜索层对 3 个定向查询返回 0 条，故转用官方 arXiv、Crossref、Optica、IOP 与精确标题核查。
- 主题：束流—多箔靶柱矢量 γ 射线、STEP 全局电磁回旋动理学、物理状态监督 ICF 代理、SpeCyl 自由边界 RWM、bump-on-tail 束流优化，以及 Ni 链 E1—中子俘获率。
- 去重：按 DOI/arXiv、规范化标题、436 条完成台账、29 条重试队列、来源 URL、正式版—作者稿关系、摘要和物理构型检查；Optica 新文与库中 HPL 旋转束单箔文作者/主题相近，但构型、结果和标识不同。
- PDF / 正文：6 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、`pypdf`、SHA-256 与非空 `pdftotext -layout`；共 175 页、14,550,916 字节，人工核查 12 个关键页并解码 6 幅保留图。MinerU 不支持本地路径，6 个公开 URL 又全部 `parsing failed`，故明确使用已验证本地 PDF、布局文本和渲染回退。
- 重试：正式论文 `10.1088/1361-6560/aeaf41` 的 PDF/DOI 路线均返回 IOP/Radware HTML 验证页，未生成摘要笔记，进入结构化重试；队列 `29 → 30`。
- 覆盖边界：定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Generating cylindrical vector γ rays via beam–target interactions: toward structured light at high energies

- 标识符：[DOI: 10.1364/optica.612330](https://doi.org/10.1364/optica.612330)
- 发表：2026-10-09，*Optica* 正式记录；全文核读使用对应 [arXiv:2508.16220v1](https://arxiv.org/abs/2508.16220) 作者预印本，不冒充 Optica VOR
- 中文笔记：[Cao et al. - 2026 - Cylindrical vector gamma rays.md](notes/Cao%20et%20al.%20-%202026%20-%20Cylindrical%20vector%20gamma%20rays.md)
- 来源影响力分：9/10；专业相似度分：10/10
- 推荐理由：直接覆盖相对论电子束—多箔转换靶、非线性 Compton γ 源、偏振与后续正电子产生。
- 一句话总结：三维 QED-PIC 给出约 `57%` 径向 γ 偏振、约 `400 MeV` 截止与 `38 pC` 正电子示例，但均是理想束靶模拟。

### 2. Global gyrokinetic simulations of electromagnetic turbulence in STEP

- 标识符：[DOI: 10.1088/1741-4326/aeaaf4](https://doi.org/10.1088/1741-4326/aeaaf4)
- 发表：2026-10-12，*Nuclear Fusion* CC BY 正式记录；全文核读使用对应 [arXiv:2609.02803v1](https://arxiv.org/abs/2609.02803) 作者预印本，不冒充 IOP VOR
- 中文笔记：[Kennedy et al. - 2026 - Global gyrokinetic STEP turbulence.md](notes/Kennedy%20et%20al.%20-%202026%20-%20Global%20gyrokinetic%20STEP%20turbulence.md)
- 来源影响力分：9/10；专业相似度分：8/10
- 推荐理由：用全局电磁 GENE 检验局部 STEP hKBM 极端输运是否被有限 `ρ*` 效应消除。
- 一句话总结：全局热流仍约 `295–1400 MW/m²`，远高于 `1.5–1.7 MW/m²` 源平衡；参考剖面非稳态，但可行状态尚需通量驱动证明。

### 3. Physical-state supervision for design-only Gaussian process surrogates of implosion simulations

- 标识符：[arXiv:2610.13822](https://arxiv.org/abs/2610.13822)
- 版本：2026-10-09，官方 arXiv v1
- 中文笔记：[Liu et al. - 2026 - Physical-state GP implosion surrogates.md](notes/Liu%20et%20al.%20-%202026%20-%20Physical-state%20GP%20implosion%20surrogates.md)
- 来源影响力分：8/10；专业相似度分：10/10
- 推荐理由：同时覆盖 ICF 设计、可解释物理状态表示、有限数据代理和严格负对照。
- 一句话总结：CH 数据随机/OOD MSE 降 `60.25%/52.98%`，但 Be/Cocktail 外推收益接近零，MoE 在部分条件下反而退化。

### 4. Implementation and verification of a new free boundary module for Resistive Wall Modes simulations with the nonlinear 3D full MHD code SpeCyl

- 标识符：[arXiv:2610.13428](https://arxiv.org/abs/2610.13428)
- 版本：2026-10-09，官方 arXiv v1
- 中文笔记：[Galeazzi et al. - 2026 - SpeCyl free-boundary RWM module.md](notes/Galeazzi%20et%20al.%20-%202026%20-%20SpeCyl%20free-boundary%20RWM%20module.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：给出自由边界、双电阻薄壳与 RWM/外扭曲模阈值的可量化代码验证。
- 一句话总结：增长率平均相对误差约 `6%`、RWM 区约 `3–4%`；这是解析/既有建模基准，不是新装置观测。

### 5. Global optimization of beam profiles for suppressing the bump-on-tail instability

- 标识符：[arXiv:2610.13391](https://arxiv.org/abs/2610.13391)
- 版本：2026-10-09，官方 arXiv v1
- 中文笔记：[Mignelli and Einkemmer - 2026 - Optimized beam profiles for bump-on-tail suppression.md](notes/Mignelli%20and%20Einkemmer%20-%202026%20-%20Optimized%20beam%20profiles%20for%20bump-on-tail%20suppression.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：把束流调制、Vlasov–Poisson 与高维全局优化连成可复算 benchmark。
- 一句话总结：15 周期二值束 `FOM=0.189`，比均匀束低 `81.1%`；一维静电模型尚未包含实际注入器与横向物理。

### 6. Impact of ab initio E1 strength on neutron capture rates along the nickel isotopic chain

- 标识符：[arXiv:2610.13868](https://arxiv.org/abs/2610.13868)
- 版本：2026-10-09，官方 arXiv v1
- 中文笔记：[Bonaiti and Sobczyk - 2026 - Ab initio E1 neutron capture rates.md](notes/Bonaiti%20and%20Sobczyk%20-%202026%20-%20Ab%20initio%20E1%20neutron%20capture%20rates.md)
- 来源影响力分：8/10；专业相似度分：8/10
- 推荐理由：补强光核/中子反应输入、Ni 同位素和 TALYS 反应率的不确定性链。
- 一句话总结：低能 E1 强度在 `3–10 GK` 增强形成 `68–78Ni` 的俘获率，`80Ni` 效应约从 `0.5 GK` 起；不是新截面实验。

## 当日综合总结

- 两篇正式记录都通过对应作者预印本核读，出版社元数据与本地全文 provenance 分开；其余四篇均为新 arXiv 预印本。
- Optica γ 源、STEP、SpeCyl、束流优化和 Ni 俘获率都是理论/数值证据；ICF 代理来自一维模拟数据库。本轮没有新增直接实验。
- Optica 新文与既有 HPL `10.1017/hpl.2026.10121` 是相近作者团队的互补方案，不把它们当重复，也不把任一模拟性能升级成已建成光源。
- 本轮没有运行 SLIPs/其他 QED-PIC、GENE、内爆数据库、SpeCyl、Vlasov 优化、LIT-CC 或 TALYS。
