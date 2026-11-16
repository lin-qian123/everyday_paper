# 2026-11-17 每日论文

新增 **3篇经核验全文／中文笔记**，台账 **573→576**：1篇出版社Article in Press、2篇近期arXiv预印本；没有取得最终出版社VOR。另将已有太赫兹论文原位补充PRA接收元数据，不重复计数。其余572个旧完成对象、全部69个旧重试对象保持；新增1项全文重试，队列 **69→70**。

## 新增全文

| 论文与版本 | 内容及证据边界 | 本地材料 |
| --- | --- | --- |
| Ghaith等，[LPA电子束的FEL适用性](https://doi.org/10.1038/s41598-026-80539-5)，11-14在线、11-09接收，出版社Article in Press | COXINEL电子束实测输运及ELEGANT/GENESIS预测。Best-shots为跨炮次组合，270 nm扫描与64/41/28 nm预测不算新激光实验；约40%实测传输与60%模型分开。 | [14页PDF](./pdfs/fel-2026.pdf) · [中文笔记](./notes/ghaith-2026-lpa-fel-qualification.md) |
| Kritikos等，[相对论等离子体辐射MD](https://arxiv.org/abs/2611.18332v1)，11-13首投、11-16公告 | 热电子–质子MD、IKP及LW谱；低频LPM抑制不等于总γ效率下降，高密度Θ<1及经典高频端受限，无转换靶实验。PDF内部日期8月25日单列。 | [25页PDF含补充](./pdfs/radiation-2026.pdf) · [中文笔记](./notes/kritikos-2026-relativistic-radiation-md.md) |
| Pamela等，[Fuse-PINN](https://arxiv.org/abs/2611.18409v1)，11-13首投、11-16公告 | 二维HW及静电约化MHD，节点–变量局部网络和ENGD；弱扩展单epoch近恒时，尚无强扩展或统一精度完整求解对比，约千倍成本差距明确。arXiv备注ICLR拒稿，非已接收会议文。 | [27页PDF含附录](./pdfs/fuse-2026.pdf) · [中文笔记](./notes/pamela-2026-fuse-pinn.md) |

## 原位去重与全文重试

- 同标题、同作者的[太赫兹光子减速论文](https://doi.org/10.1103/p838-2l32)已于7月入库为2607.07005v1。Crossref `accepted`与`published-online`均11-16；本轮APS页面/PDF403、harvest404，**只确认出版社提交的接收元数据，尚未独立核实正式发表**。台账发表日置空、接收日单列；实际仍是7月11页作者v1。只检查旧PDF身份页与SHA，没有重新精读旧物理笔记；[旧页保留转向](../../papers/arxiv-2607-07005/README.md)。已有作者全文，不新增冗余重试。
- [宽带激光非均匀等离子体参量不稳定性](https://doi.org/10.1063/5.0352707)：Crossref在线日期11-16；其列明的官方VOR PDF **403、text/html、5696字节**，不是全文。HAL精确标题前5项HTTP200、numFound0，有界web检查未核实合法替代；相关1月论文／会议摘要不能替代本作品。只入重试，不写摘要笔记。

## 检索范围与版本核查

Crossref十主题限定在线日期11-16至17，相关性前40（光核组3），共 **363行／308 DOI**，全部HTTP200；主题覆盖激光等离子体、QED、HEDP/ICF、PIC/ML、电子转换靶／γ、光核／中子／核素、VHEE、靶／防护和核诊断。返回有大量同词无关记录，未当作全部相关论文。另定向查周末正式来源，补收11-14的FEL论文。

官方arXiv九类recent最新均为11-16公告，共 **282行／253 ID**：plasm-ph、acc-ph、comp-ph、ins-det、nucl-ex、nucl-th、hep-ph、med-ph、cs.LG。跨类合并；recent只提供标题／分类，选定后再取单篇元数据和全文。两篇新预印本各做Crossref精确标题前三项核查，未确认同作品期刊版。未选择的AI4Plasma、Poynting一致MHD、阿尔芬流、IOP神经网络等保留为未读线索，不冒充完成。

按DOI、规范化标题、arXiv别名、作者及物理场景去重；对FEL历史实验引用、旧THz作者稿与接收DOI、MD与量子pair理论、Fuse-PINN与已有PIC神经代理分开。这是**有界日更筛选，并非穷尽检索或全部候选全文评审**。

## 文件与阅读验证

3 PDF共 **66页、12,311,853字节**；文件头、MIME、SHA-256、pdfinfo/pypdf/PyMuPDF页数与逐页非空文本通过。布局文本读主文及MD补充／Fuse附录，**19个关键原页目视、9幅原图表逐一重开**，另对FEL公式文本层占位采用渲染页补核。全部裁图与源PDF坐标和解码像素匹配；来源、裁框及哈希留档。PDF／文本本地保留，沿用Git忽略，仓库发布中文笔记、原图及证据记录。

MinerU历史认证过期，本轮零请求且未复测，明确采用本地全文／渲染回退。未复跑作者物理、训练或实验，无新增光核核素端到端实验、辐照剂量或临床／防护验收。

## 运行证据

- [检索来源](./research/discovery_sources.json) · [候选元数据](./research/discovery_candidates.jsonl) · [选定元数据](./research/selected_metadata.json) · [期刊版本／受阻记录](./research/journal_version_checks.json)
- [去重与旧文升级](./research/dedup_checks.json) · [阅读及边界](./research/reading_checks.json) · [原图来源](./research/figure_provenance.json)
- [下载报告](./download_report.json) · [PDF验证](./pdf_validation.json) · [运行结果](./run_results.json) · [最终验证](./research/verification.json)
