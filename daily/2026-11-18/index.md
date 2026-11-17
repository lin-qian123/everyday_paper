# 2026-11-18 每日论文

新增 **3篇经验证全文／中文笔记**，台账 **576→579**：1篇Plasma正式VOR、1篇Scientific Reports出版社Article in Press、1篇近期arXiv作者预印本。已有7月准静态束流论文原位补PRE接收DOI，不重复计数；其余575个完成对象不变。全部70个旧重试对象保持，新增MERGS全文受限候选，队列 **70→71**。

## 新增全文

| 论文与实际版本 | 内容与证据边界 | 本地材料 |
| --- | --- | --- |
| Lee等，[物理引导XFEL成像去伪影](https://doi.org/10.1038/s41598-026-80553-7)，11-17在线／11-09接收，出版社Article in Press | MEC真实成像＋两组合成注入。U-Net保留细丝与长度，但冲击波无独立真值、细丝模型会误删；集成熵不等于校准置信度。原文exp(R²)、平场定义及归一化需代码澄清；非最终VOR。 | [19页PDF](./pdfs/lee-2026-xfel.pdf) · [中文笔记](./notes/lee-2026-xfel.md) |
| Dey，[相对论非麦克斯韦对束流静电不稳定性](https://doi.org/10.3390/plasma9040049)，11-17发表／11-14接收，Plasma VOR | 弱束流线性响应与共振积分；κ/Gaussian均值及RMS匹配，MJ纵向展宽未匹配。主参数近平行、高动量例斜向，有限波矢域及收敛范围明确；不是非线性能损或对产生实测。 | [19页PDF含附录](./pdfs/dey-2026-pair-beams.pdf) · [中文笔记](./notes/dey-2026-pair-beams.md) |
| Kolobov／Arslanbekov，[PAMAR球形探针基准](https://arxiv.org/abs/2611.21466v1)，11-16首投／11-17公告，作者v1 | 球对称静电Euler动理学、轨道参考与模型切换。电子1%仅归一化碰撞趋势；强CX离子hybrid电流高约50%、俘获sensor未实现，大域只准稳窗口、最多11%时间节省。与2611.14820共享框架／部分算例，非独立实验。 | [32页PDF](./pdfs/kolobov-2026-sphere.pdf) · [中文笔记](./notes/kolobov-2026-sphere.md) |

## 原位去重和受限全文

- [准静态束流不稳定性PRE记录](https://doi.org/10.1103/yp1k-gjh9)是7月已收录2607.24234v1，同标题／作者／物理场景。Crossref接收与online字段同为11-17；APS文章／PDF403，harvest404，**未独立核实正式发表**，台账发表日置空、接收日单列。实际仍是7月28日内部日期的作者v1；当前官方字节与本地既有PDF完全一致，只看身份页／SHA，未重新认证旧物理笔记。[旧索引页保留转向](../../papers/arxiv-2607-24234/README.md)。已有全文，不建冗余重试。PRL 6v3g-18gz／2607.24214为不同伴随文，未新增精读。
- Lee的早期2605.01543与正式论文标题略有变化，作者和场景一致，作为同作品别名；Dey的2611.21041也不重复收录。球体论文与已有PAMAR框架文共享部分结果，笔记逐项区分。
- [MERGS伽马—电子转换](https://doi.org/10.1063/5.0350271)：Crossref在线11-17；官方VOR PDF经代理403／HTML 5696字节、直连403／HTML 93字节，均不是全文。HAL精确标题前5项200／numFound0，有界web未核实合法同作品替代。10月电子光学伴随论文不替代此文，**只入重试，不写摘要笔记**。

## 检索范围

Crossref十主题限定online日期11-17至18、各相关性前40（光核组4），共 **364行／295 DOI**；HEDP查询首次429后单次顺序重试200，最终十组均200。主题涵盖激光等离子体、强场QED、HEDP/ICF、PIC、ML、电子转换靶／γ、光核／中子／核素、VHEE、靶／防护和核诊断；返回的同词无关论文未视为主题命中。

官方arXiv十类recent最新日期块均为11-17，**669行／634 ID**：plasm-ph、acc-ph、comp-ph、ins-det、nucl-ex、nucl-th、med-ph、hep-ph、cs.LG、optics。recent含跨类和旧ID新公告，不将其全称为新投稿；先读标题／分类，选定后再取元数据和全文。另检查HPL最新卷及定向APS／γ诊断来源；新增MDPI期刊版通过标题查证补齐。官方CDN成功取得Dey全文，常规入口403不形成冗余重试。

神经control variates 2608.01360、量子FEL启动2611.19878、whistler2611.20809等保留为**未全文精读线索**，未计入完成。未发现本轮可收录且更直接闭合激光束—转换靶—光核／核素产额／防护的完整实验链。这是有界日更筛选，不是全球穷尽检索，也不是全部候选评审。

## 阅读、文件和验证边界

3 PDF共 **70页、12,377,608字节**；文件头、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF页数及逐页非空文本检查通过。全文／附录已读，阅读者共**36个关键原页目视**；主代理另重开全部**12幅保留原图**，逐图与源PDF坐标及解码像素匹配。旧PRE另核1个身份页，不计入新全文精读。

MinerU历史认证失效未复测、本轮零请求，明确本地布局／渲染回退；PDF／文本本地保留并沿用Git忽略，发布笔记、原图、元数据和验证记录。未复跑作者积分、训练、PAMAR求解器或实验，未做γ／光核／中子／剂量、临床或防护验收。

台账变化后已运行 `python scripts/build_indexes.py`，生成579篇／9类索引；7项仓库测试通过。范围内链接、JSON、去重、哈希、保留插图和实际提交文件的检查见下列记录。

## 运行证据

- [检索来源](./research/discovery_sources.json) · [候选元数据](./research/discovery_candidates.jsonl) · [选定元数据](./research/selected_metadata.json) · [版本关系](./research/journal_version_checks.json)
- [来源访问](./research/source_access_checks.json) · [HAL替代检查](./research/alternate_fulltext_checks.json) · [去重及原位升级](./research/dedup_checks.json)
- [Lee阅读](./research/lee_reading.json) · [Dey阅读](./research/dey_reading.json) · [Kolobov阅读](./research/kolobov_reading.json)
- [下载报告](./download_report.json) · [PDF验证](./pdf_validation.json) · [运行结果](./run_results.json) · [最终检查](./research/verification.json)
