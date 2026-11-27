# 每日论文：2026-11-28

本轮新增 **3篇经全文核验的中文笔记**：2篇出版社最终VOR、1篇出版社Article in Press；论文台账 **605→608**，原605对象保持。1篇受限正式候选新增重试，**81→82**；原81对象保持。工作在现有master，原有AGENTS.md修改保持并排除在本轮提交之外。

| 论文与正式日期 | 实际阅读版本／方法 | 中文笔记与PDF | 关键边界 |
|---|---|---|---|
| [环扇形靶TNSA能量耦合](https://www.nature.com/articles/s41598-026-79975-0)，11-27在线、11-04接收 | Scientific Reports Article in Press，17页＋8页科学补充；二维Smilei PIC | [笔记](./notes/rezaeipandari-2026-annular.md) · [主文](./pdfs/rezaeipandari-2026-annular.pdf) · [补充](./pdfs/rezaeipandari-2026-annular-supplement.pdf) | 0.616是耦合／留存代理量；16.82 MeV是公共阈值截止，不是单粒子最大能量或临床束能；几何会聚未独立隔离能量贡献 |
| [DEMO偏滤器OpenMC–MCNP中子谱](https://www.mdpi.com/2076-3417/16/23/11775)，11-27发表、11-21接收 | Applied Sciences16(23),11775，16页最终VOR含附录A/B；固定源Monte Carlo比较 | [笔记](./notes/openmc-2026-divertor.md) · [PDF](./pdfs/openmc-2026-divertor.pdf) | 参考MCNP不是实验真值；群积分谱与微分谱分开，筛选谱差／无筛选总tally／群误差不同；外置S1–S18入口403，未读 |
| [直／弯放电波导近远场质心诊断](https://doi.org/10.1088/2058-6272/aea103)，11-27发表、09-01接收 | PST28,124004，官方8页最终VOR；CLAPA-I弱探针实验＋解析反演＋作者COMSOL | [笔记](./notes/man-2026-waveguide.md) · [PDF](./pdfs/man-2026-waveguide.pdf) | 两成像分支分发次测；时序0.9与0.75±0.05 μs原文不一致；弯管零点为相对参考，不是高强度电子束或分级加速验收 |

## 检索、去重与获取

- 正式论文优先：Crossref十主题，online日期11-27至28，每主题相关性前40，共400行／326独立DOI；QED和靶诊断查询曾429，已在有界重试中恢复。十个官方arXiv分类当前最新仍11-26，共396行／382独立ID，各日期标题数量与提取条数一致；本轮未新增预印本。检索有界、非穷尽，不宣称全球没有其他新文。
- 对照完成台账、重试、DOI、规范化标题、来源URL及版本／物理对象。环扇形靶早期Research Square标题不同但为同作者同场景线索，不独立计数；波导与库内相对论质心阻尼论文为不同作品，关系仅列related_work。
- Nature采用实际`_reference.pdf`锚点；MDPI主站403、官方静态PDF恢复。波导IOP PDF200是订阅HTML，合作期刊HTTPS证书不匹配；正常HTTP页面提供官方PDF。30／45秒传输不完整、Range不支持后，一次连续直连成功，完整字节／结构／版本核对后入库。未关闭证书验证。
- 阻抗匹配[10.1088/1361-6595/aec323](https://iopscience.iop.org/article/10.1088/1361-6595/aec323) PDF200返回211055字节订阅HTML，HAL精确标题前5结果0；有界网页未获已验证的同作作者PDF。进入结构化重试，未写摘要式笔记、未执行整队下载；只检查新增重试命令构造。

## 阅读与复核边界

4份科学PDF共 **49页／14,299,648字节**，含三主文41页、环扇形靶科学补充8页。已核验PDF签名／MIME／SHA、pdfinfo／pypdf／PyMuPDF页数、逐页文本；49源页总览与关键页面放大，11幅保留原图均实际重开并核对源像素。正文及明示的内置／独立补充已读，参考文献只核结构，OpenMC外置补充未获。

MinerU零请求，历史401未复测；本地布局文本与页面渲染回退。印刷参数的少量算术复核不等于重跑作者程序。本轮未运行Smilei、COMSOL、OpenMC／MCNP或实验，未新增激光光核核素、临床或防护全链验收。主文PDF／布局文本保留于本地daily目录，按仓库规则不由Git跟踪；笔记、11图和来源／验证报告随提交同步。

## 接续重点

优先恢复阻抗匹配全文及OpenMC外置补充；环扇形靶补固定作者输入、完整3D与边界能量账本；OpenMC做同源／同核库／同体积的差异分解及7090能群采样；波导澄清时序、标定／协方差、同发测量和弯管绝对零点。此前B11、冷中子和活化线索本轮未补读。

## 可追溯记录

[检索范围](./research/discovery_sources.json) · [Crossref快照](./research/crossref_discovery.json) · [arXiv快照](./research/arxiv_discovery.json) · [选中正式元数据](./research/selected_formal_crossref.json) · [入库元数据](./research/selected_metadata.json) · [去重](./research/dedup_checks.json) · [未读线索](./research/deferred_candidates.json)

[初次访问](./research/formal_access.json) · [后续访问／恢复](./research/followup_access.json) · [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [原图溯源](./research/figure_provenance.json) · [印刷算术](./research/printed_arithmetic_checks.json) · [重试命令检查](./research/retry_command_check.json)

[运行结果](./run_results.json) · [索引旧修复保留](./research/index_rebuild_preservation.json) · [最终核验](./research/verification.json)
