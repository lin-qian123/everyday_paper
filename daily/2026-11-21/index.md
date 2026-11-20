# 2026-11-21 每日论文

本轮新增 **2篇作者全文／中文笔记**，台账 **586→588**；另将既有DPF模型原位升级为出版社最终版，不重复计数。新增2项受限全文重试，队列 **72→74**，原72项对象保持，未整队重复下载。其余585个已完成对象保持。

## 新增论文与优先阅读

| 实际版本 | 主要发现与证据边界 | 笔记／本地PDF |
| --- | --- | --- |
| Pukhov，[2611.26032v1](https://arxiv.org/abs/2611.26032v1)，29页，11-19首投／11-20公告 | 解析设计＋GEM-PIC-RZ。频率与横模匹配降低尾场失相；175 mJ／10 mm测试增益208 MeV，9.8 mJ／30 mm为169 MeV但相位累计约1.5 rad；真实2 pC两级束能100→265 MeV、能散18.5%，手动重启第二级，非kHz实验。 | [中文笔记](./notes/pukhov-2026-comb.md)／[PDF](./pdfs/pukhov-2026-comb.pdf) |
| Takizawa等，[2611.25552v1](https://arxiv.org/abs/2611.25552v1)，11页，11-19首投／11-20公告 | LFEX球遮挡实测＋径向反演。全功率泵浦、低种子能量2.7–12.9 J压缩前测量；H2 D50对准34→102 μm。2.2×10¹⁸ W/cm²按250 J、1.3 ps换算，非同发瞬时强度直接读数；四束全功率联合焦斑待测。 | [中文笔记](./notes/takizawa-2026-focus.md)／[PDF](./pdfs/takizawa-2026-focus.pdf) |

两篇均未核实期刊接收或发表；Crossref各标题前3项无同作，未把PDF内11-20日期替代11-19首投。去相位方案与库内Palastro 2606.20298的关系已说明：沿用导波去相位思路、采用ωp共振频差和弱皮秒驱动，是不同作品；不重复收录同一物理研究。

**当前优先读LFEX诊断**：它直接影响PIC输入的焦斑、晕环与强度定义。Pukhov适合跟踪低能高重复率束源设计，但需先闭合真实束载、残余相位和后向散射，再谈转换靶应用。

## 既有作品的最终版升级

[DPF混合PIC—流体模型10.1088/1741-4326/aebda4](https://iopscience.iop.org/article/10.1088/1741-4326/aebda4)恢复23页官方VOR（封面＋22正文页）。出版社页面与正文首页一致：**11-04接收、11-20发表**；卷期为 *Nuclear Fusion* 67 (2027) 026002，2027卷年与2026在线日分开。原台账对象和[原笔记](<../2026-11-06/notes/Zhao et al. - 2026 - Hybrid PIC fluid dense plasma focus accepted.md>)更新，保留最初processed_date、作者稿和接收稿来源；[本地最终PDF](./pdfs/zhao-2026-dpf-vor.pdf)。

本轮核标题、五作者、摘要、日期和格式，目检封面／首页，**未全文重读VOR物理内容，未逐式逐图比对两版**。原笔记标为11-06接收稿阅读，旧页码及印刷式疑点不自动升级为VOR审计结论。台账总数不因版本升级增加。

## 正式候选的全文限制与重试

- PRC **10.1103/l8lx-jr9h**，100Mo至98mNb光核产额：Crossref记录11-20接收，online同日，未独立核实最终发表。文章页403 HTML5550字节、PDF403 HTML5514字节、官方harvest404 JSON52字节。arXiv有界题名／作者检索无解析结果、HAL作者题名组合numFound=0，网页检索找到旧95Nb研究及会议摘要，不能替代同作全文。新入重试，**无摘要笔记**。
- JRR **10.1093/jrr/rrag102**，NCEPT微剂量学／RBE评估：Crossref online11-20，期刊网页的检索服务能提供正文片段，但当前直接文章页403 HTML5613字节、PDF403 HTML5685字节，直接网络传输亦403 HTML93字节；Europe PMC DOI查询hitCount=0。未取得可验证PDF，**未入完成台账、未生成全文笔记**。

精确来源／HTTP证据见[访问记录](./research/source_access_checks.json)和[替代来源](./research/alternate_source_checks.json)。原72项重试对象保持，不向受限端点反复空跑。

## 检索覆盖及未读线索

正式来源优先：Crossref十主题、journal-article、online日期11-20至21、各相关性前40，共 **400行／344个DOI**，十次均HTTP200。覆盖激光等离子体、QED、HEDP、PIC、ML、电子转换靶／伽马、光核／核素、离子靶、屏蔽与核诊断；同词医学血浆／泛数据融合等剔除。既有DPF最终版恢复优先于补录旧预印本。

官方arXiv十类最新11-20块，共 **347行／327个ID**：plasm-ph、acc-ph、comp-ph、optics、ins-det、nucl-ex、nucl-th、hep-ph、med-ph、cs.LG；按标题／类别初筛，选定两篇才全文阅读。recent含较旧ID的跨类公告，不等于全部当天首投。有界检索，不能据此声称该领域当天无其他新作。

PRE 10.1103/tp7s-lzc3的11-20接收状态及2609.07732v2别名已核元数据，但未读全文；AVS量子计算等离子体综述10.1116/5.0338793仅标题线索；旧2611.24653活化核数据本轮未补读。没有把这些线索计为已完成。

## 阅读与验证

2篇新文40页，阅读正文／方法／补充；新取得DPF最终版23页仅身份／日期核验。三PDF共 **63页／6,267,081字节**，文件头、MIME、SHA、pdfinfo／pypdf／PyMuPDF页数一致、逐页文本非空。新文24个关键源页及DPF2个身份页实际渲染目检，11幅原图表裁剪复看并与源PDF矩形渲染逐像素匹配。

MinerU历史认证过期未复测、零请求，明确本地布局文本／渲染回退；PDF／文本保留本地，沿用Git忽略。没有运行作者PIC、FLASH、贝叶斯拟合或实验，没有新增激光束—转换靶—光核中子／核素全链实测或临床／防护验收。

台账变化后运行 `python scripts/build_indexes.py`。测试、链接／去重／文件范围检查见[运行结果](./run_results.json)与[最终核验](./research/verification.json)。原AGENTS.md改动保留并排除本次提交。

## 运行证据

- [检索范围](./research/discovery_sources.json) · [Crossref候选](./research/crossref_discovery.json) · [arXiv候选](./research/arxiv_discovery.json)
- [正式元数据](./research/formal_selected_metadata.json) · [预印本元数据](./research/arxiv_selected_metadata.json) · [期刊标题检查](./research/preprint_journal_checks.json)
- [新增记录](./research/selected_metadata.json) · [原位版本更新](./research/in_place_updates.json) · [去重](./research/dedup_checks.json) · [出版社日期](./research/publisher_status_evidence.json)
- [下载报告](./download_report.json) · [PDF验证](./pdf_validation.json) · [阅读记录](./research/reading_summary.json) · [视觉来源](./research/visual_validation.json)
