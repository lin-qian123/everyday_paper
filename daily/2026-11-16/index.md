# 2026-11-16 每日论文

新增 **3篇经核验作者全文／中文笔记**，台账 **570→573**：1篇11-13正式发表的PRE记录对应五月作者v2，2篇11-12首投、11-13公告的近期预印本。**本轮未取得出版社VOR。**570个既有完成对象保持，69项重试内容逐字节保持；未全队列重试。

## 新增论文

| 论文与实际版本 | 主要内容与证据边界 | 全文与笔记 |
| --- | --- | --- |
| Gautam等，电容放电中的EBW；[PRE正式记录](https://doi.org/10.1103/cv7h-ghnk)，**11-13发表**；实际[2508.15269v2](https://arxiv.org/abs/2508.15269v2)，05-19修订 | 1D3V显式静电PIC–MCC及色散比较；密度/电离峰分离、第二RF谐波和体加热。磁场–r、Debye网格、FFT角波数及功率分解需澄清；没有新实验。 | [16页PDF](./pdfs/ebw-2026.pdf) · [中文笔记](./notes/gautam-2026-bernstein-discharge.md) |
| Tian等，²²⁸Th–D₂O光中子标定源；[2611.16415v1](https://arxiv.org/abs/2611.16415v1) | 放射性γ驱动的光核源实测；132.3±5.8/h净计数经7.63% MC效率得到1734±76±65/h前端面发射率，非4π源强。BSS谱依赖响应/先验，PandaX的220h千事件为未来MC。 | [25页PDF](./pdfs/photoneutron-2026.pdf) · [中文笔记](./notes/tian-2026-thorium-photoneutron.md) |
| Patel等，无磁化对等离子体受激后散射；[2611.17279v1](https://arxiv.org/abs/2611.17279v1) | 有限泵浦流体涨率、LP奇次谐波、热分布与1D OSIRIS；大泵浦涨率不单调增加，时间/空间问题温度效应不同。已有对等离子体，无QED造对或新实验。 | [25页PDF](./pdfs/pair-2026.pdf) · [中文笔记](./notes/patel-2026-pair-stimulated-scattering.md) |

## 检索、版本和去重

- 正式来源优先：Crossref十主题、在线日期11-13至11-16、相关性前40（光核组19），共 **379行／304 DOI**，十项均HTTP200。覆盖激光等离子体、QED、HEDP/ICF、PIC/ML、转换靶/γ、光核/中子/核素、VHEE、靶/防护和核诊断；返回项含非相关同词论文，未将全部结果视为研究候选。
- 官方arXiv十类recent的最新公告均为 **11-13**，共 **582行／547 ID**；本轮含physics.ins-det，以补核探测器/光中子源，cs.LG该块340条。类别交叉重复合并；这是有界检索，不是全球文献穷尽。
- APS独立页面核实PRE长文与伴随短文均11-13发表；长文实际读五月v2，接收日10-27单列。伴随[短文5hwk-fymz](https://doi.org/10.1103/5hwk-fymz)同作者/近同场景，本轮只收长文，短文未全文精读；PRL L–H阈值rw25-wy15仅未读线索。
- 三篇按DOI、规范化标题、arXiv别名、作者和物理场景去重。Patel引用库内[Tangtartharakul等Bragg完全反射](https://doi.org/10.1103/g27z-2kd3)，但不同作者、独立OSIRIS分析的涨率/谐波/热效应构成不同作品，不算独立实验验证。
- 光中子PDF首页10作者与网页8作者不同，台账依实际全文保留10人及顺序，并记录原始网页差异；不推断正式期刊作者表。两篇新预印本的Crossref精确标题前3项未核实同作品期刊版，这不证明期刊版不存在。

## 全文可用性和验证

EBW普通PDF返回 **403、text/html、5514字节**，官方harvest返回 **401、application/json、57字节**；均不是有效全文。已取得同作品官方作者v2，因此只保留出版社版本边界，没有新增冗余全文重试。既有69项重试未改动，没有摘要代替全文的笔记。

3 PDF共 **66页、11,814,550字节**，文件头、MIME、SHA-256、pdfinfo/pypdf/PyMuPDF页数和逐页非空文本均通过。全文布局文本已读；阅读者实际目视 **38个关键原页**（EBW11、光中子13、对等离子体14），**9幅保留原图均由主代理重开，解码像素与源PDF裁框一致**。PDF与布局文本本地保留、沿用Git忽略；笔记、原图、元数据及核验记录发布到仓库。

MinerU此前认证失效，本轮零请求且未复测，明确采用本地全文/渲染回退。光中子截面修改、MC效率、BSS先验相关性与部署几何的传递分开；对等离子体印刷公式疑点仅作静态核查，不判断作者代码错误。未复跑EDIPIC、OSIRIS、Geant4、MAXED或PandaX，不把新放射源实验写成激光转换靶—光核核素端到端新实验，也没有临床/防护验收。

## 运行证据

- [检索来源](./research/discovery_sources.json) · [候选元数据](./research/discovery_candidates.jsonl) · [选定原始元数据](./research/selected_metadata.json) · [期刊版本核查](./research/journal_version_checks.json)
- [去重](./research/dedup_checks.json) · [EBW阅读](./research/ebw_reading.json) · [光中子阅读](./research/photoneutron_reading.json) · [对等离子体阅读](./research/pair_reading.json)
- [原图来源](./research/figure_provenance.json) · [下载报告](./download_report.json) · [PDF验证](./pdf_validation.json) · [运行结果](./run_results.json) · [最终验证](./research/verification.json)
