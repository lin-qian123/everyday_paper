# 2026-11-20 每日论文

本轮新增 **4篇经验证全文／中文结构化笔记**，台账 **582→586**；其中1篇11-19正式出版社VOR，3篇11-18首投／11-19公告的作者预印本。另2项既有作品原位补期刊元数据，不重复计数；其余580个既有完成对象保持。**72项重试的字节和对象均保持**，没有整队重复探测。

## 新增全文

| 论文与实际版本 | 证据与关键结论 | 中文笔记／本地PDF |
| --- | --- | --- |
| Xin等，硬件补偿波形与光纤SBS；[HPL 10.1017/hpl.2026.10195](https://doi.org/10.1017/hpl.2026.10195)，11-19在线、8-04接收，12页正式VOR | RF模型、真实电压闭环、OSA和MOPA实验。七阶谱补偿前后2269→3562 W约57%，RMS6.99→7.25 GHz；一阶→七阶约20.5%，不能混用基线，RMS定义不明不转FWHM。不是等离子体SBS实验。 | [笔记](./notes/xin-2026-sbs.md)／[PDF](./pdfs/xin-2026-sbs.pdf) |
| McMillen等，外部散斑增强束喷散；[2611.24914v1](https://arxiv.org/abs/2611.24914v1)，7页作者稿，投稿PRL未核实接收 | OMEGA真实透射／Thomson测量及稳态非局域模型。95%收集角33.8 mrad，相对真空12.7 mrad约2.7倍；之后18.5 mrad是另一背景。18%密度扰动是模型量，不是直接测量。 | [笔记](./notes/mcmillen-2026-beam-spray.md)／[PDF](./pdfs/mcmillen-2026-beam-spray.pdf) |
| Wu等，人字靶准静态磁场与偏振正电子；[2611.24069v1](https://arxiv.org/abs/2611.24069v1)，11页作者稿 | 无碰撞3D自旋QED-PIC，3.4 PW激光另需10 GeV电子。总数目比0.0288；5°两支合计约0.00708但自旋相反，各支约0.00369／0.00339，不是单束63%产额。近90%对应更低产额。 | [笔记](./notes/wu-2026-herringbone.md)／[PDF](./pdfs/wu-2026-herringbone.pdf) |
| Pérez de Rada Fiol等，NFS快中子液闪响应；[2611.24118v1](https://arxiv.org/abs/2611.24118v1)，9页作者稿，投稿NIM A未核实接收 | 40 MeV氘打Be的TOF实验＋Geant4／PHITS响应。MONSTER实测至40 MeV、阈值180 keVee；sTED至20 MeV、80 keVee，受本次PMT非线性限制。积分效率吻合不等于局部谱形已验证；未测激光源产额。 | [笔记](./notes/perez-2026-neutron-response.md)／[PDF](./pdfs/perez-2026-neutron-response.pdf) |

三篇预印本的Crossref标题前3项未核实同作期刊版；网页“submitted”不升级为接收／发表，媒体报道也不替代期刊证据。NFS按PDF与citation元数据13作者，未采网页自动的错误作者计数。

## 既有条目的原位维护

- **BORAY-3D**：8月2608.05667关联[10.1088/2058-6272/aec41f](https://doi.org/10.1088/2058-6272/aec41f)。IOP页面明确“Accepted Manuscript online 19 November 2026”，**不是最终VOR**；PDF端点HTTP200却返回文章HTML 84,395字节。原[笔记](<../2026-08-10/notes/Wang et al. - 2026 - BORAY 3D ray tracing code.md>)新增版本说明，实际仍是8-06作者v1、12页。
- **AWAKE十米放电源**：9月2609.08551关联[PRResearch 10.1103/33h4-lf1m](https://doi.org/10.1103/33h4-lf1m)，Crossref接收11-19，online同日未独立核实为发表。APS接收页／PDF403，PDF为HTML 5,556字节；官方harvest404／JSON52字节。原[笔记](<../2026-09-10/notes/Amoedo et al. - 2026 - 10-metre discharge plasma source for AWAKE.md>)补版本说明，实际仍为9-08作者v1、10页。

两份旧PDF的当前官方v1均与现有文件逐字节相同，另目检2个身份页、比对标题／作者／摘要和物理场景。**只核身份与哈希，未重新验收旧物理笔记。**已存在同作作者全文，不为期刊PDF不可得增加冗余重试；旧论文索引保留转向新DOI页的入口，旧路径不失效。

## 检索覆盖与未完成线索

Crossref十主题限定online日期2026-11-19至20，journal-article、各组相关性前40；共 **400行／351 DOI**，详见[检索范围](./research/discovery_sources.json)。涵盖激光等离子体、QED、HEDP、PIC、ML、电子转换靶／韧致辐射、光核／中子／核素、离子靶、屏蔽与核诊断；返回的医学血浆、泛材料／数据融合同词命中已筛除。十个发现查询均HTTP200；后续正式DOI元数据初次并行批遇429，改为顺序请求后四项全部200，没有把失败当作无结果。

官方arXiv十类recent最新11-19块：plasm-ph、acc-ph、comp-ph、optics、ins-det、nucl-ex、nucl-th、hep-ph、med-ph、cs.LG，共 **351行／330 ID**。只筛标题／分类，选定后取得元数据与全文；recent也包含较旧ID的新跨类公告，不等于全是11-18首投。最新块取自实际包裹的dl，未重复此前解析错误。

11-19新闻提及的GNN Poisson论文10.1007/s44205-026-00191-z实际4-03发表，未误记为新发表。2611.24653聚变活化核数据、2611.23319形式化Vlasov证明、PRD新接收10.1103/zh5q-4hp9、AIP 10.1063/5.0352852仅保留未精读线索；AIP页面403，没有开展该文PDF／替代全文调查，不将其写作已读或已完成重试。**有界非穷尽日更**，未新增激光束—转换靶—光核中子／核素全链实验、临床或防护验收。

## 阅读、图像与本地验证

4份新科学PDF共 **39页／6,636,301字节**，文件头、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF三路页数及逐页非空文本通过；布局文本265,222字节。长文按research-paper-explainer技能分工；主代理读两篇实验文并审阅全部四篇交付笔记。阅读者实际目检 **30个新文关键源页**，主代理另重开全部 **19幅保留裁图**并与源PDF矩形渲染逐像素核验。旧文2个身份页单独记录。

MinerU历史认证失效未复测，本轮零请求；明确采用本地布局文本／渲染回退。四PDF与文本保留本地并沿用既有Git忽略；GitHub发布笔记、原图、元数据、下载／阅读／校验证据及索引。未运行作者控制程序、谱拟合、QED-PIC、MC输运或实验；笔记中的算术和公式检查属于静态核对。

台账变化后运行 `python scripts/build_indexes.py`；测试与最终范围核验见[运行结果](./run_results.json)与[最终检查](./research/verification.json)。已有AGENTS.md修改保留，排除本次提交。

## 运行证据

- [Crossref候选](./research/crossref_discovery.json) · [arXiv候选](./research/arxiv_discovery.json) · [检索覆盖](./research/discovery_sources.json)
- [正式元数据](./research/formal_selected_metadata.json) · [arXiv版本](./research/arxiv_selected_metadata.json) · [新增台账](./research/selected_metadata.json) · [期刊标题检查](./research/preprint_journal_checks.json)
- [出版社状态](./research/publisher_status_evidence.json) · [期刊PDF访问](./research/journal_version_checks.json) · [旧文身份](./research/old_work_identity.json) · [原位更新](./research/in_place_updates.json) · [去重](./research/dedup_checks.json)
- [HPL阅读](./research/xin_reading.json) · [束喷散阅读](./research/mcmillen_reading.json) · [QED阅读](./research/wu_reading.json) · [中子阅读](./research/perez_reading.json)
- [下载报告](./download_report.json) · [PDF校验](./pdf_validation.json) · [运行结果](./run_results.json) · [最终检查](./research/verification.json)
