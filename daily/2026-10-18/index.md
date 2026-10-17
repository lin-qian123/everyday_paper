# 每日论文索引 - 2026-10-18

## 今日概览

- 新增 **5 篇作品**，台账 **465 → 470**：2 篇 10 月 16 日正式 VOR、1 篇新 APS 接受稿记录对应的 2025 年作者稿，以及 2 篇 10 月 15 日官方预印本。同作品正式标识和预印本合并记录，不重复计数。
- 全文共 **63 页、6,048,195 字节**，文件头、类型、SHA-256、pdfinfo/pypdf 页数一致、全页文本和 348,027 字节布局文本通过检查。MinerU pipeline **4 成功、1 失败后使用已验证本地回退**；目视检查 17 个首页/关键页，保留 5 幅可读原图/原表。
- 搜索层 1 组查询无结果后，Crossref 10 组查询取得 750 行、545 个唯一 DOI，日期窗 2026-10-16 至 18，每组最多 75 条、按出版日期降序。官方 arXiv 五类最近 300 条最新提交仍为 10 月 15 日；再查具体标题、出版商接受/发表状态和匹配作者稿。覆盖有界，不宣称全球穷尽。
- Wang、Banks 和 Hobmaier 在前次检索记录中曾出现，但未入完成台账、未写笔记，本次是首次全文入库。Banks 属可迁移计算方法补充，尚非等离子体机器学习应用实证。没有为补齐主题而添加新的弱相关 QED 条目。
- 重试队列 **40 → 40**，保留原记录。电子束激波的 VOR 仍不可得，已找到匹配作者稿，作为版本对照待办；没有 abstract-only 笔记。未选出新的激光转换靶—光核/中子端到端实验增量。

## 论文清单

### 1. Hybrid adaptive RSM-GA Monte Carlo optimization method (HRG-MCO) and its application in the design of moderator–collimator systems for accelerator-based thermal neutron radiography

- 标识与来源：[10.1007/s41365-026-02068-0](https://doi.org/10.1007/s41365-026-02068-0)，*Nuclear Science and Techniques* 37, 248，2026-10-16 正式 VOR。
- [中文笔记](notes/Yang%20et%20al.%20-%202026%20-%20Adaptive%20neutron%20moderator%20collimator%20optimization.md)
- 来源影响力分 8/10；专业相似度分 10/10（主观阅读优先级，不是期刊影响因子）。
- 推荐理由：直接连接源能谱、慢化器几何、MC 评价次数和转换屏响应，适合核应用设计审查。
- 一句话结论：约 50–60 次输运调用逼近二维枚举基准；90% 是转换屏热中子诱发光输出份额，此时热中子数仅占通量的 8.2%。

### 2. First-principles electronic transport properties of Ti and Ti-6Al-4V for modeling ultrashort-pulse laser ablation

- 标识与来源：[10.1103/6sn3-ltl4](https://doi.org/10.1103/6sn3-ltl4)，*Physical Review Materials*，2026-10-16 正式 VOR。关联 arXiv:2607.18085 只记为别名。
- [中文笔记](notes/Hobmaier%20et%20al.%20-%202026%20-%20Titanium%20alloy%20electronic%20transport.md)
- 来源影响力分 8/10；专业相似度分 8/10。
- 推荐理由：说明双温材料模型中热导函数形式和参数补偿如何改变预测，适合靶前沿物性研究。
- 一句话结论：合金热导峰值低约 6.4 倍，但特定亚皮秒 TTM 的晶格峰温只差约 1.4%；更换热导函数形式可带来约 19% 偏差，均非新烧蚀实验。

### 3. First observation of dispersive shock waves in an electron beam

- 标识与来源：[10.1103/2hhy-jfcd](https://doi.org/10.1103/2hhy-jfcd)，*Physical Review Accelerators and Beams* **2026-10-16 接受稿记录**；实际全文为 [arXiv:2510.19786v1](https://arxiv.org/abs/2510.19786v1)，2025-10-22。
- [中文笔记](notes/McCright%20et%20al.%20-%202026%20-%20Electron%20beam%20dispersive%20shock%20waves.md)
- 来源影响力分 8/10；专业相似度分 8/10。
- 推荐理由：把束流集体效应的直接电流观测、WARP PIC 和 KdV 标度分层比较。
- 一句话结论：10 keV UMER 束中测得扩展波列；图 4 文字面板标签有交换，时间宽度展开率 s/s 不能当作 m/s 激波速度。

### 4. Aluminum wide-range EOS sensitivity in Z-pinch dynamic-hohlraum liner-foam impact and outgoing radiation

- 标识与来源：[10.48550/arXiv.2610.21107](https://doi.org/10.48550/arXiv.2610.21107)，2026-10-15 官方 v1 预印本。
- [中文笔记](notes/Wang%20et%20al.%20-%202026%20-%20Aluminum%20EOS%20dynamic%20hohlraum%20sensitivity.md)
- 来源影响力分 7/10；专业相似度分 9/10。
- 推荐理由：给出 EOS 路径、撞击时刻、峰值与脉宽之间可量化的敏感性差异。
- 一句话结论：固定输运的一维模型中，撞击时辐射功率可差约 50%，而峰值和热化率不相应提升；原图部分刻度缺失，定量以可读原表为据。

### 5. The importance of tensor handling and implementation of physics-informed DeepONets

- 标识与来源：[10.48550/arXiv.2610.22157](https://doi.org/10.48550/arXiv.2610.22157)，2026-10-15 官方 v1 预印本。
- [中文笔记](notes/Banks%20et%20al.%20-%202026%20-%20Efficient%20physics%20informed%20DeepONet%20tensors.md)
- 来源影响力分 7/10；专业相似度分 7/10，作为可迁移方法补充。
- 推荐理由：在不改变算子映射的前提下复用 Branch 编码，帮助审查代理模型的训练张量组织。
- 一句话结论：A100 上二维线性平流训练扫描最高约 3.75×；3D 基线内存不足，约 580× 属理论预测，且训练轮数有 200k/300k 文内冲突。

## 当日综合总结

优先阅读中子设计和材料输运，两篇正式全文分别约束源—探测器响应链与材料闭合。电子束实验提供集体动力学对照；EOS 和 DeepONet 则用于审查“峰值代表全程”和“理论复杂度代表实际加速”这两类推断。

- **直接实验：** UMER 电流波列是束流实测，实际阅读的作者稿来自 2025 年；不是新激光加速/转换实验。钛输运中的实验对照来自既有文献。
- **数值与代理：** 中子 Geant4 优化、钛 DFT/TTM、动态黑腔辐射 MHD、线性平流 PI-DeepONet 分别保留源归一化、相态、维度与性能口径边界。
- **全文状态：** 四篇 MinerU 成功；Yang 的任务返回 `parsing failed`，使用已验证本地 PDF、布局文本和页面目视回退。APS 接受稿与较早作者稿内容是否与最终 VOR 完全一致尚待核查。
- **本地工作：** 完成来源、PDF、正文、图表、笔记与索引检查；没有运行相关物理求解器、运输模拟、训练或作者性能基准。

## 维护与证据记录

- [PDF 逐篇核验](pdf_validation.json)
- [检索覆盖、去重及正式版关系](research/research-run.json)
- [来源元数据](research/sources.jsonl)与[入库清单](research/import-manifest.json)
- [MinerU 成功/失败记录](research/mineru-attempts.json)
- [原图/原表出处与裁框](research/figure-manifest.json)
- [验证与发布准备记录](run_results.json)

PDF、布局文本和 MinerU 正文按仓库规则只保留本地；笔记、图表摘录、下载报告和索引随 Git 发布。
