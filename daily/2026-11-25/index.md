# 2026-11-25 每日论文

新增 **4篇经全文核验的中文结构化笔记**，台账 **596→600**：2篇11-24出版社最终VOR、1篇RMP接收登记对应的作者v2综述、1篇11-23首投／11-24公告的作者v1。596个旧完成对象保持；Athena靶制造全文受限新增1项重试，队列 **77→78**，原77项保持。

## 今日论文与阅读重点

| 论文／实际全文版本 | 主要内容及证据限制 | 本地全文与笔记 |
| --- | --- | --- |
| Bilbao等，PRL **137,225001**，[10.1103/k67h-dvxp](https://doi.org/10.1103/k67h-dvxp)，10-30接收、11-24发表，最终VOR | 经典betatron冷却导致横向幅度分布成环，继而在分段解析／二维PIC链中放大ICL；约50%为局部粒子条件占比。13组半径对照的5–9%使用同次PIC平均能史，不是实验或全先验预测。 | [中文笔记](./notes/bilbao-2026-betatron-cooling.md) · [9页PDF含End Matter](./pdfs/bilbao-2026-betatron-cooling.pdf) |
| Neuroth等，PSST **35,115019**，[10.1088/1361-6595/aebfc4](https://doi.org/10.1088/1361-6595/aebfc4)，11-09接收、11-24发表，最终VOR | CF₄放电实验与1d3v PIC/MCC多诊断比较；离子弹性／非弹性截面×3／×10，5 Pa调参、30 Pa冻结参数检查。绝对离子通量不作定量验证，部分电子密度仍相差约2倍，中性化学未闭环。 | [中文笔记](./notes/neuroth-2026-cf4-pic-validation.md) · [26页PDF含1页下载封面](./pdfs/neuroth-2026-cf4-pic-validation.pdf) |
| Shrock等，RMP DOI [10.1103/mw87-cjg8](https://doi.org/10.1103/mw87-cjg8)，Crossref11-24接收登记；实际作者[2512.08690v2](https://arxiv.org/abs/2512.08690v2)，11-03修订 | 综述模耦合、泄漏、OFI／毛细管、长气靶与诊断。9.8 m是按剖面计算的衰减长度；米级气靶、10 GeV端点、nC电荷、kHz造通道须按不同工作点引用。正式发表日未核实、留空。 | [中文笔记](./notes/shrock-2026-plasma-waveguides.md) · [113页作者PDF](./pdfs/shrock-2026-plasma-waveguides.pdf) |
| Zhang等，[2611.30084v1](https://arxiv.org/abs/2611.30084v1)，同作期刊未核实 | 固体表面pump–probe二维EPOCH＋Floquet约化；频率／角度选择律与增能对照。单／双pump约0.83%／1.68%仅为指定累计增能差；J/m是二维每出平面长度，非三维总能量和全输入转换效率。 | [中文笔记](./notes/zhang-2026-plasma-crystals.md) · [13页PDF含4页Supplement](./pdfs/zhang-2026-plasma-crystals.pdf) |

建议先读CF₄的“调参后相合”与绝对诊断边界，再读betatron从单粒子映射到分布正梯度和ICL的分段证据。波导综述可作为模拟输入／诊断检查手册；SPPC关注同一频率—角度通道与能量账是否同时成立。

## 正式状态与全文版本

RMP的Crossref同时把accepted和published-online填为11-24，尚无卷页。官方文章403 HTML 5550字节、PDF403 HTML 5514字节、harvest404 JSON52字节；网页工具的接收列表缓存也未包含这一新登记，不能据缓存否认接收，也不能据Crossref同日字段宣布正式发表。实际采用113页作者v2，初稿2025-12-09、修订2026-11-03；身份以标题、四作者、摘要和版本核对。未将作者稿称作出版社接受稿。

PRL普通文章／PDF也403，但官方harvest返回9页最终VOR，首页正式日期清楚；没有重复收录同作2510.24567。其额外在线Supplement入口403，未取得该补充；最终PDF内End Matter A–C已全部读。PSST实际PDF为最终排版版，封面后的文章首页确认发表日，覆盖正文及反应表。SPPC按作者v1阅读，Crossref精确标题相关性前3无同作期刊，不作穷尽断言。

## 新增全文重试

Athena惯性聚变靶批量制造，Fusion Science and Technology，[10.1080/15361055.2026.2752318](https://doi.org/10.1080/15361055.2026.2752318)，Crossref在线日期11-24。官方PDF返回 **403／text/html／5617字节**，提示JavaScript与cookie；HAL精确标题前5返回0，有界网页检索未找到可核实同作合法作者PDF。因此只进入重试，未进完成台账、未写摘要式笔记；PDF未得，0.25 Hz等标题信息不升级为已验证产能。

没有订阅、付费或凭据操作，也没有整队重复请求77项历史候选。RMP已有同作可验证作者全文，未为同一作品再建冗余下载重试。

## 检索范围与去重

Crossref十主题，以journal-article和在线日期11-24至25筛选，每主题相关性前40，最终 **400行／344不同DOI**，均200。覆盖激光等离子体、强场QED、HEDP、PIC、ML、电子转换靶伽马、光核核素、中子诊断、离子辐照和防护；噪声结果按题目／摘要与物理对象排除。

官方arXiv十类最新公告均为11-24，最终 **667行／623不同ID**，包括跨类。第一次解析误取日期标题之后的下一个dl，混入旧块；现已改用标题所在dl，十类条目数均与其最新标题标示相符，只用修正后快照统计。一次候选显示因历史null DOI失败，已改用空值安全比较，保存的检索结果未损坏。

以DOI、arXiv自有标识／正式别名、规范化标题、最相近旧题目结合作者、摘要、物理场景去重。新四作均无完成台账同作；综述引用的原始研究不重计，CF₄前作条纹／氩验证与新多诊断校准分别辨识。所有旧完成／重试对象保留；没有把related_work中的别篇论文错计为本篇身份别名。

本轮未读线索包括B-11厚靶共振2611.30439、冷中子多靶2611.30086、等离子体轴子2611.30098、ML锁模2611.28266；LoKI-GM、stellarator启动和EAST快离子论文仅元数据，其全文可得性未调查。旧热层ICF27760、51V光核08565-w、活化24653继续标为未读。本轮是有界日更，不能声明覆盖所有新论文。

## 阅读与核验边界

四PDF共 **161页／20,281,248字节**，通过签名、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF页数一致及逐页非空文本检查。113页综述的科学正文I–VI完整读取、参考文献仅核结构；两位阅读者分段后主代理完整读合并笔记并复核图源。其余正文、End Matter和已内附补充按实际取得的文件读取。阅读者与主代理共目视69个不同源页，30幅保留图由主代理重开且按源裁框像素检查；具体清单见各阅读记录。

MinerU本次一次请求返回401、user token expired，停止后续提交；明确本地布局文本／渲染回退。未执行作者PIC、MCC、流体、传输矩阵或新实验。没有新增光核／核素、临床或辐射防护的完整链验收。

## 运行资产

PDF／布局文本保留本地并沿用Git忽略；笔记、有效图表、元数据、索引和核验记录提交。台账变化后重建索引，同步README／TODO；原有AGENTS.md编辑保持且排除本轮提交。最终提交与远端一致性记录在自动化记忆。

- [检索范围](./research/discovery_sources.json) · [Crossref快照](./research/crossref_discovery.json) · [arXiv快照](./research/arxiv_discovery.json)
- [正式元数据](./research/selected_formal_crossref.json) · [实际版本](./research/publisher_status_evidence.json) · [作者稿元数据](./research/author_metadata_access.json) · [SPPC期刊核查](./research/sppc_journal_check.json)
- [新增对象](./research/selected_metadata.json) · [去重核对](./research/dedup_checks.json) · [未读线索](./research/deferred_candidates.json)
- [APS访问](./research/formal_access.json) · [其他正式全文访问](./research/other_formal_access.json) · [Athena作者库检索](./research/athena_author_repository.json) · [重试命令构造检查](./research/retry_command_check.json)
- [主代理图源与目视汇总](./research/primary_reading_verification.json) · [索引重建与保留](./research/index_rebuild_preservation.json)
- [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [运行结果](./run_results.json) · [最终核验](./research/verification.json)
- [波导前半图源](./research/waveguides_early_reading.json) · [后半图源](./research/waveguides_late_reading.json) · [betatron图源](./research/betatron_reading.json) · [betatron补充访问](./research/betatron_supplement_access.json) · [CF₄图源](./research/cf4_reading.json) · [SPPC图源](./research/crystal_reading.json)
