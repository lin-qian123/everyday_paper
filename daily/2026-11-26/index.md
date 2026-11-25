# 2026-11-26 每日论文

新增 **2篇正式最终版全文／中文结构化笔记**，均于11月25日发表，台账 **600→602**。600个旧完成对象保持；机器学习诊断配置与¹⁸⁵Ta光核制备全文受限，新增2项重试，队列 **78→80**，原78项保持。

## 今日论文

| 正式论文与实际全文 | 阅读重点与限制 | 本地资产 |
| --- | --- | --- |
| Pogorelsky，Frontiers in Physics **14:1969078**，[10.3389/fphy.2026.1969078](https://doi.org/10.3389/fphy.2026.1969078)，10-29接收、11-25发表，9页最终VOR | LWIR平台综述：相似缩放降低强度／密度需求，改善电子、离子与通道诊断。已有2 ps／5 TW与计划100 fs／25–40 TW分开；既有图像不构成新点火或重离子结果。 | [中文笔记](./notes/pogorelsky-2026-lwir.md) · [PDF](./pdfs/pogorelsky-2026-lwir.pdf) |
| Arnold等，PRL **137,221603**，[10.1103/rk4d-45t9](https://doi.org/10.1103/rk4d-45t9)，10-06接收、11-25发表，7页最终VOR含End Matter | 对产生与韧致辐射形成过程重叠可削弱LPM抑制；新文纳入电子／介质光子质量。计算量是合并通道的电子能损微分率，非靶后光子谱；均匀厚介质与有限靶预期分开。 | [中文笔记](./notes/arnold-2026-bremsstrahlung.md) · [PDF](./pdfs/arnold-2026-bremsstrahlung.pdf) |

建议优先读LWIR的“现有／计划能力”和逐图诊断边界，再读PRL中BH、LPM与LPM⁺三种归一化以及能损率／逸出光子数的区别。两文均未新增转换靶光核、核素、临床或防护的完整实验链。

## 状态与版本核验

Frontiers网页搜索缓存仍停留在接收阶段，但本轮直接访问的官方全文页面、PDF与Crossref一致给出11-25发表，实际采用最终排版9页版。PRL从APS官方harvest取得7页最终版，末尾两页完整公式与LogGamma分支说明已读；不是作者预印本替代稿。

PRL同作预印本2604.18685作为身份别名去重，只收一个作品；同日PRD伴随长文10.1103/8rg8-tmgg／2605.03002是不同论文，38页文件只核首页／结构、未精读，未另入库，临时PDF和布局已清理。前作JHEP质量可忽略极限也未当作本篇新结果。没有为已有可验证全文的PRL建立重复下载重试。

## 新增全文重试

- **机器学习指导下一发诊断配置**，RSI [10.1063/5.0350254](https://doi.org/10.1063/5.0350254)：Crossref官方PDF **403／HTML／5696字节**，已校正的官方文章入口 **403／HTML／5739字节**。初始文章路径含未核实ID，已标明不作为判断依据。HAL精确标题前5返回0；OSTI带引号精确标题返回200、61字节空XML记录。未找到可核实同作作者PDF。
- **无载体¹⁸⁵Ta光核制备与快速化学分离**，JRNC [10.1007/s10967-026-10928-7](https://doi.org/10.1007/s10967-026-10928-7)：PDF入口 **200但重定向订阅HTML／325915字节**，不满足PDF签名。HAL精确标题前5返回0；OSTI同样返回空XML记录。有界网页检索未找到可核实同作作者全文，专利等相关材料不替代论文。

这两项仅进入重试台账，未写摘要式笔记。OSTI初始非引号宽检索只作线索；后续XML响应曾触发JSON专用解析异常，现保留原始格式／空记录证据，未把异常本身当作无结果。未整队重试历史78项，也未进行订阅、付费或凭据操作。

## 检索与去重范围

Crossref十主题，在线日期11-25至11-26、journal-article、每主题相关性前40，返回 **400行／353不同DOI**。覆盖激光等离子体、强场QED、HEDP、PIC、ML、电子转换靶、光核核素、中子、离子辐照与防护；排除血液plasma、一般激光加工、天体和无关机器学习结果。

官方arXiv十类取11-25最新公告块，从日期标题所在dl解析，并逐类核对标题标示数量；共 **365行／348不同ID**。通用网页工具返回的arXiv缓存仍可能停留11-23，因此未据该旧缓存宣布没有新稿。正式全文优先，本轮没有新增预印本。新的Hall-thruster PIC、等离子体涡旋／闭合／detachment等仅存未读线索；前日B-11、冷中子、轴子、ML锁模及更早ICF／光核／活化线索未在本轮补读。

去重检查DOI、规范化标题、同作arXiv标识、最近旧题目及作者／摘要／物理场景。综述引用的旧实验不重复计数，PRL内部的同作预印本和伴随论文区别处理；related_work不作为本篇身份别名。检索有界、非穷尽。

## 阅读、核验与本地资产

两份正式PDF共 **16页／3,245,483字节**，通过签名、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF三路页数与逐页非空文本检查。正文及PRL的End Matter完整读取，参考文献只核结构；16页实际总览，关键单页加看，10幅保留裁图逐一重开并核源裁框像素。

MinerU本轮零请求，前轮401未复测；明确使用本地布局文本与渲染回退。没有复跑作者模型／程序／实验，没有把平台方案或解析预测升级为已完成应用。

PDF和布局文本保留本地、沿用Git忽略；中文笔记、10幅有效图、来源、台账和索引提交。README／TODO同步当前进度；既有AGENTS.md修改保留并排除本次提交。最终提交及远端一致性记录在自动化记忆。

## 运行记录

- [检索范围](./research/discovery_sources.json) · [Crossref快照](./research/crossref_discovery.json) · [arXiv快照](./research/arxiv_discovery.json)
- [正式元数据](./research/selected_formal_crossref.json) · [新增台账对象](./research/selected_metadata.json) · [去重检查](./research/dedup_checks.json) · [PRL作者稿身份](./research/arnold_arxiv_identity.json)
- [正式来源访问](./research/formal_access.json) · [APS／校正AIP访问](./research/followup_access.json) · [精确OSTI查询](./research/osti_exact_queries.json) · [RSI HAL](./research/mariscal-hal.json) · [Ta HAL](./research/snow-hal.json)
- [RSI宽检索OSTI](./research/mariscal-osti.json) · [Ta宽检索OSTI](./research/snow-osti.json) · [重试命令构造](./research/retry_command_check.json)
- [伴随文未读记录](./research/companion_deferred.json) · [其他未读线索](./research/deferred_candidates.json) · [图源与阅读范围](./research/figure_provenance.json)
- [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [运行结果](./run_results.json) · [索引保留检查](./research/index_rebuild_preservation.json) · [最终核验](./research/verification.json)
