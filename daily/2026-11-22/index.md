# 2026-11-22 每日论文

新增 **2篇正式已接收／发表研究的全文笔记**，台账 **588→590**；既有纳米线质子论文原位补上期刊接收身份，不重复计数。原74条重试记录逐对象及文件字节保持，未整队重复探测；其余587个旧完成对象保持。

## 本轮论文与阅读顺序

| 实际全文版本 | 主要内容及证据边界 | 本地阅读 |
| --- | --- | --- |
| Karst等，Nature Communications [10.1038/s41467-026-79615-1](https://www.nature.com/articles/s41467-026-79615-1)，11-21最终VOR；10-22接收 | 516 nm、18 fs、20 kHz氦HHG实验，13.5 nm的2%带宽约1.8×10¹¹ photons/s／2.7 μW。最高10⁻⁶效率对应HH33整条线；3 fs、电离／相干空间结构来自模拟。 | [中文笔记](./notes/karst-2026-hhg.md) · [8页正文](./pdfs/hhg-2026-visible.pdf) · [7页补充](./pdfs/karst-2026-hhg-supp.pdf) |
| Ikeya等，Scientific Reports [10.1038/s41598-026-81760-y](https://www.nature.com/articles/s41598-026-81760-y)，11-21在线Article in Press；11-17接收，非最终VOR | ASE图像→DNN增量→SLM的Yb:YAG实机起振。原配置100/100一次成功；三次重装100／98／98初态均两次内成功。有限样本、可见ASE及人工粗对准条件；标量NM与图像DNN并非等信息／等总成本比较。 | [中文笔记](./notes/ikeya-2026-control.md) · [14页正文](./pdfs/ikeya-2026-control.pdf) · [13页补充](./pdfs/ikeya-2026-control-supp.pdf) |

优先读 **HHG图1和补表1**，厘清整线／2%带宽／总谱功率；再读 **DNN图4–5**，区分离线误差、有限重装成功率和完整训练成本。两份笔记按原文顺序解释图、公式与补充。HHG当前原始页面已列Version of record，搜索缓存仍有早期版本提示，按当前PDF和页面为准；DNN实际PDF明确Article in Press。

## 同一作品的期刊接收更新

7月已入库的ELI-NP纳米线质子作品2607.09229，对应新接收PRResearch [10.1103/bvnj-1wmg](https://journals.aps.org/prresearch/accepted/10.1103/bvnj-1wmg)。Crossref accepted为11-21，online同日，最终发表未独立核实，台账publication_date留空。期刊标题去掉nano-structured／ultra-relativistic连字符，23位作者顺序及同一实验摘要匹配。

官方arXiv仍仅v1，重新取得17页PDF与[既有本地PDF](<../2026-07-14/pdfs/Sagar Dam et al. - 2026 - Tens of MeV collimated bright fluxes of protons.pdf>)哈希相同；保留旧processed_date与作者稿证据，[旧笔记](<../2026-07-14/notes/Sagar Dam et al. - 2026 - Tens of MeV collimated bright fluxes of protons.md>)增补状态说明。仅首页身份／哈希及格式检查，**未全文重审物理内容**。APS文章403 HTML5571B、PDF403 HTML5556B、harvest404 JSON52B；同作已有全文，不建重复重试。重复下载副本已清理。

## 检索覆盖、去重与未读线索

正式来源优先，Crossref十主题、journal-article、online11-21至22、每主题相关性前40：返回 **312行／243 DOI**。两次429在有界重试后恢复，最终十查询均200。覆盖激光等离子体、QED、HEDP、PIC、ML、转换靶／伽马、光核／中子／核素、离子靶、屏蔽及核诊断。另通过网页检索发现Crossref这组有界前列未返回的HHG正式论文，回到出版社核验。

arXiv十类最新块仍为11-20，与上轮一致，**347行／327 ID**；无新公告不等于无未读论文，recent亦含旧作跨类。新增两篇在588旧对象中DOI及规范化标题无冲突，近似标题／作者／物理情景复核未见同作。纳米线作品则正确归并为原位身份更新。

- 2611.26402v1软光子正反冲采样：核了官方元数据和34页PDF格式，未读全文；本轮优先两篇正式研究，**未入台账、无笔记**，未使用下载副本已清理。
- 10.1007/s10967-026-11304-1光中子源测Gd浓度：仅正式元数据线索，尚未调查全文可得性或阅读，不计为完成，也不凭空写成下载失败重试。
- 2611.24653核活化数据比较仍为未读接续线索，本轮未下载。原74项来源受限队列保持，没有无变化全量空跑。

本轮是有界增量，不声称穷尽当天领域论文。

## 原文疑点与证据边界

DNN正文写NM成功首达最多32次，补表S2的test3-2列33，笔记同时保留；图2示意三处池化与正文前两层后池化不同，表S1亦未给全声称的simplex偏移。没有自行补造代码参数。离线采样与训练耗时、图像／标量信息量、闭环更新／目标评估次数分开。

HHG模拟谱在HH37处按实验归一化，有效气体密度相对背压估计除4.4，内部强度与3 fs时宽均属模型解释／预测。新结果没有转换靶MeV伽马、光核中子／核素端到端实测或临床／防护验收；本轮未复跑作者模型、训练或实验。

## 文件与索引验证

四份新增科学PDF共 **42页**，两篇正文和科学补充均核内容身份；另验旧质子17页文件，物理阅读范围仍限历史笔记。文件头／MIME／SHA、pdfinfo／pypdf／PyMuPDF页数及逐页文本检查通过。29个新关键源页＋1个历史身份页实际渲染，9个原图表摘录重看／源像素复核。PDF和布局文本保留本地，沿用Git忽略。

MinerU历史401/A0211认证失效未复测、零请求，明确本地文本／渲染回退。台账变化后运行 `python scripts/build_indexes.py`；测试和最终范围、去重、链接、文件哈希检查见下列记录。AGENTS.md原有修改保留、排除本轮提交。

- [检索范围](./research/discovery_sources.json) · [Crossref结果](./research/crossref_discovery.json) · [arXiv结果](./research/arxiv_discovery.json)
- [正式元数据](./research/formal_selected_metadata.json) · [当前版本证据](./research/publisher_status_evidence.json) · [旧作品arXiv身份](./research/dam_arxiv_metadata.json)
- [新增对象](./research/selected_metadata.json) · [原位更新](./research/in_place_updates.json) · [去重](./research/dedup_checks.json)
- [下载记录](./download_report.json) · [PDF验证](./pdf_validation.json) · [阅读范围](./research/reading_summary.json) · [图像来源](./research/visual_validation.json)
- [运行结果](./run_results.json) · [最终核验](./research/verification.json)
