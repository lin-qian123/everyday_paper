# 2026-11-19 每日论文

新增 **3篇经验证主文／中文笔记**，台账 **579→582**。2项11-18正式期刊记录分别实际读出版社Article in Press及2025年作者v1，另1项近期arXiv预印本；**本轮未取得最终VOR**。6月细丝化论文原位补PRE接收DOI，不重复计数；其余578个完成对象保持。全部71个旧重试对象保持，新增Be-WDM阻止本领受限候选，队列 **71→72**。

## 新增全文

| 论文与实际阅读版本 | 内容和证据边界 | 本地材料 |
| --- | --- | --- |
| Asghari等，[D–T源BNCT束流整形](https://doi.org/10.1038/s41598-026-80838-x)，11-18在线／11-11接收，出版社Article in Press | MCNPX保留参考＋受控敏感性，假设源率10¹² n/s。参考快剂量／超热通量高所用历史值20%；材料点谱、参考面通量和孔径比较分开；CUT能／热谱、NPS及几何待澄清，非实验或临床资格。 | [30页PDF](./pdfs/asghari-2026-bnct.pdf) · [中文笔记](./notes/asghari-2026-bnct.md) |
| Alexopoulou，[TNSA能量／散角／电荷态标度](https://doi.org/10.1140/epjp/s13360-026-08572-x)，11-18正式VOR记录，实际2512.21279v1 | 1700→1002→517个筛选模型样本，非517组实验。能量CV R²71／69／69%，C／O测试84／79%；“>95%”为前作声称，未本篇重证。当前全文是2025-12-24作者稿，未核期刊最终式。 | [24页作者PDF](./pdfs/alexopoulou-2026-tnsa.pdf) · [中文笔记](./notes/alexopoulou-2026-tnsa.md) |
| Zhang等，[相似性降维离子动理学初始化](https://arxiv.org/abs/2611.22165v1)，11-17首投／11-18公告，作者v1 | 1D3V氩CCP、81基尺度训练工况，解析缩放＋ML＋PIC/MCC修正。中位27.7倍／最大56.8倍是收敛RF周期比；误差范数、正性／归一化、稳态判据与完整成本需补，不代表相对论激光PIC或真机验证。 | [6页PDF](./pdfs/zhang-2026-ion-kinetics.pdf) · [中文笔记](./notes/zhang-2026-ion-kinetics.md) |

## 去重、版本与全文缺口

- [PRE细丝化接收记录](https://journals.aps.org/pre/accepted/10.1103/gg1s-rxrg)改题名，但作者、摘要及模型与6月已收2606.21221v1一致，原位合并。官方接收页为11-18，Crossref的online字段同日；**发表未独立核实，发表日为空，接收日单列**。APS PDF403／HTML5514字节、harvest404／JSON52字节；仍用既有10页作者v1，当前官方字节与本地SHA相同。此次只核身份页／哈希，未重读或重新认证旧物理笔记。[旧论文页保留转向](../../papers/arxiv-2606-21221/README.md)。已有同作全文，未新建冗余重试。
- TNSA正式标题增加laser-driven，作者及摘要场景与2512.21279相同，列为同作别名；出版社历史明确11-18 VOR，但PDF入口HTTP200实际重定向HTML。**同作作者稿已获，不增加冗余重试；不假定最终稿的式、数据和问题与v1完全相同。**
- [Be-WDM束缚／自由电子阻止本领](https://journals.aps.org/pre/accepted/10.1103/yx13-bzgg)：11-18接收，发表未核实。官方PDF403／HTML5514字节，harvest404／JSON52字节；HAL精确标题前5项HTTP200／numFound0，有界精确web检索没有核实合法同作全文。**仅入重试，不写摘要笔记。**
- BNCT网页所链6页“Supplementary Information”是无关行政表单，**不是科学补充**；识别类型后删除本地表单PDF／文本，不转载其个人信息、签名或图像。下载及类型误配留证，但不计入科学阅读或入库PDF页数；实际仍缺完整MCNPX输入和科学补充。

## 检索覆盖

Crossref十主题限定online日期2026-11-18至19，journal-article、每组相关性前40，共 **362行／287 DOI**。四个查询最初429，各单次顺序重试均200；包含激光等离子体、强场QED、HEDP、PIC、ML、电子转换靶／韧致辐射、光核／中子／核素、离子靶、防护／诊断和聚变核诊断。返回同词医学、材料等无关结果，未将它们全部算作领域命中；APS接收日期不作已发表数量。

官方arXiv十类recent最新日期块均11-18，**341行／328 ID**：plasm-ph、acc-ph、comp-ph、optics、ins-det、nucl-ex、nucl-th、hep-ph、med-ph、cs.LG。med-ph最新块为空；cs.LG211项已取全。初次脚本误按h3在dl外解析而失败，已改为在实际包裹列表内按日期边界读取；没有把解析失败当无论文。recent包含旧ID跨类公告，只先筛标题／分类，选定后获取元数据与全文。

另查定向APS接收页与出版社版本历史。10.1103/qnp8-g1zm热电子角分布、2611.21899密度极限、2611.21902 FACET-II不确定性、2611.23084 Vlasov积分等仅未全文精读线索，未计完成。未对72项队列做整队重复探测。本轮为有界非穷尽日更，未新增激光束—转换靶—光核中子／核素产额完整实验链、临床或防护验收。

## 阅读和验证范围

3主文PDF **60页／7,489,694字节**，通过文件头、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF三路页数与逐页非空文本。两篇长文按research-paper-explainer技能分工，主代理读CCP并审阅全部交付笔记；阅读者合计 **33个关键原页目视**，主代理另重开全部 **12幅保留原图**并对源PDF矩形裁图逐像素核验。另有旧CFI1个身份页，不计新科学全文。

MinerU历史认证失效未复测，本轮零请求；本地全文／布局文本／渲染回退明确记录。三个主文及文本留本地并沿用Git忽略；发布中文笔记、12原图、元数据、下载／验证及索引。无关6页表单虽PDF格式有效，但内容不匹配，已删除；格式有效不等于科学补充有效。

本轮未复跑作者MCNPX、解析前向模型、统计拟合、ASTRA、神经训练或实验。本文的公式／计数静态核对与作者性能声称分开。台账变化后运行 `python scripts/build_indexes.py` 重建582篇／9类索引；仓库7项测试及范围内JSON、链接、去重、哈希与图像检查通过。

## 运行证据

- [检索范围及状态](./research/discovery_sources.json) · [Crossref候选](./research/crossref_discovery.json) · [arXiv候选](./research/arxiv_discovery.json)
- [选定台账元数据](./research/selected_metadata.json) · [arXiv版本元数据](./research/arxiv_selected_metadata.json) · [TNSA出版社历史](./research/tnsa_publisher_metadata.json) · [版本边界](./research/journal_version_checks.json)
- [下载报告](./download_report.json) · [APS备用端点](./research/aps_harvest_checks.json) · [合法替代及期刊检查](./research/alternate_and_journal_checks.json) · [旧CFI身份](./research/old_cfi_identity.json) · [去重](./research/dedup_checks.json)
- [BNCT阅读](./research/asghari_reading.json) · [TNSA阅读](./research/alexopoulou_reading.json) · [CCP阅读](./research/zhang_reading.json)
- [PDF校验及内容误配](./pdf_validation.json) · [运行结果](./run_results.json) · [最终检查](./research/verification.json)
