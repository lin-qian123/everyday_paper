# 2026-11-15 每日论文

新增 **3篇经核验作者全文与中文笔记**，台账 **567→570**：1篇已发表PRC记录对应作者稿、1篇新接收PRApplied记录对应较早作者稿、1篇近期预印本。**未取得出版社VOR。**全部567个既有完成对象保持；新增2项受限全文重试，队列 **67→69**，既有67个重试对象保持。

## 新增论文

| 论文与实际阅读版本 | 主要内容与证据边界 | 全文及笔记 |
| --- | --- | --- |
| Tomin等，束驱动横向偏转诊断；[PRApplied DOI](https://doi.org/10.1103/ttzy-t1wy)，APS **11-13接收**；实际[arXiv:2605.13752v3](https://arxiv.org/abs/2605.13752v3)，05-27修订 | 高Q尾场使相邻RF桶的witness在过零点附近偏转。14 GeV、500 pC driver、6 m的约1.6 fs是估计/跟踪性能，未实测；21 MeV自尾场能损、上游压缩15–25%扰动和标定成本需闭合。未取得11月接收稿。 | [7页PDF](./pdfs/deflector-2026.pdf) · [中文笔记](./notes/tomin-2026-beam-driven-deflector.md) |
| Wantz等，碳中子分道截面；[PRC正式记录](https://doi.org/10.1103/j2m6-v12v)，**09-17发表**；实际[arXiv:2611.16075v1](https://arxiv.org/abs/2611.16075v1)，11-11首投 | LANSCE既有数据新增p2、p3+4、d1、d2分道分析；同一旧实验、相对标准定标与逃逸MC修正，不是激光中子源新实验。主表/补充表6点数值或误差冲突；总截面和的终态/能区需区分。 | [15页含5页补充PDF](./pdfs/carbon-2026.pdf) · [中文笔记](./notes/wantz-2026-carbon-reactions.md) |
| Kushoro等，蓝宝石中子探测器原型；[arXiv:2611.14745v1](https://arxiv.org/abs/2611.14745v1)，11-10首投、11-13公告 | 八个原型完成α源响应和偏压扫描；DT中子谱来自Geant4，2%分辨来自假设展宽，没有中子实测或稳定计数平台。沉积能、载流子收集和触发效率分开。 | [11页PDF](./pdfs/sapphire-2026.pdf) · [中文笔记](./notes/kushoro-2026-sapphire-detectors.md) |

## 检索、状态核查与去重

- 正式来源优先：Crossref十主题按在线日期11-13至11-15，每组相关性前40（光核/中子组17），共 **377行／300个DOI**；5个初始HTTP429均顺序定向恢复为200。筛选词覆盖激光等离子体、QED、HEDP/ICF、PIC/ML、转换靶/γ、光核/中子/核素、VHEE、离子束/防护和核诊断。相关性排序与关键词并不等于全部返回项都相关。
- 官方arXiv十类recent的最新日期块均仍为 **11-13**，共 **579行／543个ID**；本轮cs.LG读该块340条。类别交叉重复已合并，这是有界检索，不是全球穷尽。
- 定向核对APS PRL近期、PRE等离子体近期、PRApplied等离子体主题与接收列表、精确标题。**Crossref published-online不能自动证明VOR已出版**：准分子激光与Tomin记录11-13在APS仍为接收。本轮将接收日期明确单列。
- 三篇按DOI、规范化标题、arXiv别名、作者和物理场景去重；Tomin的正式接收DOI与五月v3只计一篇，不以相关Bazyl PRAB设计标准论文替代其正文。碳论文补收保留9月出版日期，复用旧数据的关系明确，不算新独立实验。
- 蓝宝石精确标题Crossref前3项未核实同作品期刊版。PDF的Al₂O₃及作者Kushoro与网页摘要Al₂O₂、姓名Kushoroa不同，依PDF/机构上标核正，原始元数据保留。
- PRL L–H阈值、两篇近同作者PRE EBW、arXiv pair-scattering2611.17279、AI4Plasma I/II仅为候选/元数据线索，未精读、未写摘要笔记。未做旧队列全量重试。

## 全文受限与重试

- [Excimer lasers as drivers of many stage laser plasma accelerators](https://journals.aps.org/prresearch/accepted/10.1103/78bn-rj6r)：11-13接收，未核实VOR。官方PDF为HTTP403、text/html、5556字节；官方harvest为404、JSON、52字节。
- [Polarized lepton source via target-normal sheath fields](https://journals.aps.org/prapplied/abstract/10.1103/qzlv-8y21)：PRApplied 26,054024、11-09发表。官方PDF为HTTP403、text/html、5553字节；官方harvest为401、JSON、57字节。

两项均经过有界精确标题检索与官方HAL精确标题前5项检查，HAL为200/numFound0，未核实合法替代全文；保留精确失败并进入重试，**没有摘要代替全文的笔记**。Tomin与碳已有同作品作者全文，出版社版本受限只记版本边界，不重复加入完成全文重试。

## 全文与科学核验

3 PDF共 **33页、5,280,087字节**，布局文本 **163,328字节**；文件头、MIME、SHA、pdfinfo/pypdf/PyMuPDF页数和逐页非空文本均通过。阅读者目视27个关键原页（Tomin5、蓝宝石9、碳13），主代理另核碳主/补充表页10、14、15；9幅保留原图/表全部重开，并与源PDF裁框解码像素匹配。PDF/布局文本本地保留并沿用Git忽略；笔记、图像、来源与核验记录随仓库发布。

MinerU此前认证过期，本次零请求且未复测凭据；使用本地全文/原页渲染回退。未复跑作者ECHO/CST/Ocelot、Geant4/Menate_r、TALYS、拟合或实验。碳数据须先澄清表间冲突和协方差；蓝宝石须完成中子场验证；束诊断须补时序/束荷/对准/自尾场联合误差。这些工作没有新增激光光核核素完整实验链、临床或防护验收。

- [检索来源](./research/discovery_sources.json) · [候选元数据](./research/discovery_candidates.jsonl) · [原始选定元数据与版本](./research/selected_metadata.json)
- [精确标题版本核查](./research/journal_version_checks.json) · [替代全文检查](./research/alternate_fulltext_checks.json) · [去重检查](./research/dedup_checks.json)
- [阅读与表间复核](./research/reading_review.json) · [原图来源](./research/figure_provenance.json) · [下载报告](./download_report.json)
- [PDF核验](./pdf_validation.json) · [运行结果](./run_results.json) · [最终验证](./research/verification.json)
