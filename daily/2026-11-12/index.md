# 2026-11-12 每日论文索引

## 今日概览

- 新增 **4篇独立作品全文／中文笔记**，台账 **555→559**：1篇11-11正式出版记录对应作者v2全文、3篇11-11公告的作者v1预印本。**本轮取得的四份全文均为作者稿，没有取得出版社VOR。** 原555条完成对象保持不变。
- **4 PDF／67页**（21＋14＋14＋18），17,128,357字节；通过文件头、类型、SHA-256、pdfinfo／pypdf／PyMuPDF页数及逐页非空文本检查。目视检查 **43关键页／12原图摘录**；四篇正文依原文顺序整理，重要公式附定义、推导及限制。MinerU已知凭据失效，本轮零请求，实际使用本地全文与原页渲染。PDF／385,493字节布局文本本地保留、沿用Git忽略规则。
- 正式来源优先：Crossref出版日期11-10至11-12的十主题，按最近发表和相关性各40行，**800行／594 DOI**；补四主题在线日期检索 **144行／144 DOI**，两者合计 **648 DOI**。arXiv十类别11-11最新日期块 **220行／201 ID**，cs.LG仅读前100/235。检索有范围和截断，不宣称穷尽。
- Scientific Reports的TPF-2早期接收研究PDF入口返回HTML，新增全文重试，**64→65**；原64重试对象均保持，无全队列探测、无摘要替代全文。APS Open Science条目类型未核实，保留为候选线索，没有升格为期刊正式版或完成条目。

## 新增论文

| 论文与实际版本 | 核心内容与证据限制 | 本地资料 |
|---|---|---|
| Kalluri、Hillier，[Phys. Plasmas正式记录](https://doi.org/10.1063/5.0335643)，11-11在线；实际读[2510.27053v2](https://arxiv.org/abs/2510.27053v2)，10-24修订 | 2D／3D非理想MHD比较：二维贯入较强、三维局地混合／耗散较强。二维模式结论限指定磁场取向；缺三维加密序列，功率／累计能量及印刷式口径需澄清。出版社PDF403，未核实与作者稿逐字一致 | [笔记](notes/kalluri-2026-mrti-2d-3d.md) · [PDF](pdfs/kalluri-2026-mrti-2d-3d.pdf) |
| Hessami等，[2611.13436v1](https://arxiv.org/abs/2611.13436v1)，11-10首投 | RF电子双束驱动PWFA＋弱弯转压缩；实测光学辐射7.6±1.3 nJ。2.3 fs／4.8 kA为PUFFIN模拟；谱为多炮扫描拼接且有选炮条件，未给前后发射度成对测量 | [笔记](notes/hessami-2026-plasma-compression.md) · [PDF](pdfs/hessami-2026-plasma-compression.pdf) |
| Wang等，[2611.12994v1](https://arxiv.org/abs/2611.12994v1)，11-08首投 | SLEGS LCS γ束测Tm-169(γ,n)，18展开点／8.27–14.61 MeV；317.08±10.26 mb是12.41 MeV数据。恒星率／逆俘获为TALYS推断，联合拟合复用NewSUBARU数据，χ²/ndf≈8.7；不是激光等离子体核素生产链 | [笔记](notes/wang-2026-thulium-photoneutron.md) · [PDF](pdfs/wang-2026-thulium-photoneutron.pdf) · [表I转录](research/wang-table1-cross-sections.csv) |
| Maslarova等，[2611.14119v1](https://arxiv.org/abs/2611.14119v1)，11-10首投 | HarP＋物理坐标GP／BO重建第23次HHG效率；4D参考集NRMSE约0.044，非逐点4.4%误差。额外确认6.96×10⁻⁶不属于120轮内最佳采样，最优在域边界，无新实验 | [笔记](notes/maslarova-2026-hhg-bayesian.md) · [PDF](pdfs/maslarova-2026-hhg-bayesian.pdf) |

三篇v1的官方元数据没有期刊版字段，分别作有限精确标题Crossref前三项查询，未核实同作品期刊版。Hessami检索命中的五月纵向动力学前作不是本篇实验的正式版本。Tm文与库内NewSUBARU作品按设施、作者、能区和原文引文核实为不同作品，联合分析共享的数据另作说明。DOI、归一化标题与arXiv别名均用于去重。

## 全文受限与接续重点

- [TPF-2](https://www.nature.com/articles/s41598-026-79996-9)：11-11在线、11-04接收，页面明确是等待最终VOR的早期同行评审稿；PDF入口HTTP200，重定向232,044字节HTML，未取得文章PDF。精确标题检索未核实替代全文，不根据摘要生成笔记，已入重试。
- [bi-Kappa装载高能尾](https://doi.org/10.1103/1m87-jy9v)：Crossref容器为 **APS Open Science**，无卷页／全文链接；DOI实际入口403，harvest404/JSON。试探的PRE accepted路径也403，但这不证明它属于PRE。出版类型及全文尚未核实，保留候选、未入完成台账或冒称正式论文。
- MRTI优先取得VOR、求解器／初态与三维加密证据；压缩实验优先补全炮光谱与阈值选择原因、独立束长／前后发射度及色散定义；Tm优先补积分通量、背景计数定义、响应矩阵／协方差和联合拟合张力；HHG优先核验五种子统计、固定物理候选池消融、域边界扩展和实验抖动。
- `2611.13793`仅检查摘要／元数据，未读全文；此前CoilStellaration、TRIMEG、tearing、RPC等未读线索本轮未补读。未复跑作者求解器、PIC、MC、拟合、BO或实验；没有新增激光光核核素完整生产链、临床或防护验收。

## 可追溯记录与验证

- [检索范围与限制](research/discovery_sources.json)、[去重后的来源候选](research/discovery_candidates.jsonl)、[选中来源元数据](research/selected_metadata.json)、[预印本期刊版检查](research/journal_version_checks.json)。在线日期检索首次临时收集遇429，已顺序重查四组成功；HHG标题检查429后重查200，均不把失败响应当有效元数据。
- [下载报告](download_report.json)、[PDF验证](pdf_validation.json)、[图像页码／裁框／SHA](research/figure_provenance.json)、[运行结果](run_results.json)、[最终范围审计](research/verification.json)。原图裁剪均实际打开，且与源PDF裁框解码像素比对。
- 台账变更后运行 `python scripts/build_indexes.py`；`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q`：**7项通过，5.69秒**。最终文件、链接、JSON、去重与提交范围检查见审计记录。
- 提交／推送收据在发布后写入自动化运行记忆；既有用户`AGENTS.md`修改保持并排除于本轮提交。
