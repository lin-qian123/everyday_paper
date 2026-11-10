# 2026-11-11 每日论文索引

## 今日概览

- 新增**4篇独立作品的全文／中文笔记**：1篇11-10正式VOR、3篇11-10公告的作者预印本；台账**551→555**，原551条完成对象不变。
- **4 PDF／83页**（6＋14＋20＋43），18,637,962字节；通过文件头、类型、SHA-256、pdfinfo／pypdf／PyMuPDF页数及逐页文本校验。目视检查25个关键页，保留9幅经核对的原图／表摘录。PDF和布局文本本地保存，沿用Git忽略规则；本轮未使用MinerU。
- 正式来源优先：Crossref十主题2026-11-09至11-11、每组40行，共400行／346个唯一DOI；初次7组429，顺序重查全部恢复。arXiv十类别11-10最新日期块317行／285个唯一ID，**cs.LG仅前100/509**，属于有限范围检索，不宣称穷尽。
- 锥靶贝叶斯优化中子源aeb708定向重查仍为Radware HTML；新增跨装置剖面机器学习aebb4a全文重试，**63→64**。其余62条旧重试对象不变；没有用摘要代替全文入库。

## 新增论文

| 论文与版本 | 核心内容及限制 | 本地资料 |
|---|---|---|
| Brown等，[PRX Energy正式VOR](https://doi.org/10.1103/hkpv-c3y7)，11-10发表、10-08接收 | Z装置两炮高电感MITL污染对照；负载峰电流17.8／18.0 MA，来自速度测量＋MHD反演。省略燃料、外磁场与预热，没有聚变产额比较 | [笔记](notes/brown-2026-electrode-contamination.md) · [PDF](pdfs/fusion-electrode-contamination.pdf) |
| Maguire等，[2611.12812v1](https://arxiv.org/abs/2611.12812v1)，11-09首投／11-10公告 | 激光—固体多MeV电子单脉冲体外细胞研究；正常与肿瘤均有保护趋势。AG01522-D的RBE10为外推，S1–S5补充缺失；不是临床／正常组织选择性证据 | [笔记](notes/maguire-2026-picosecond-cell-sparing.md) · [PDF](pdfs/maguire-2026-picosecond-cell-sparing.pdf) |
| Shuai等，[2611.12410v1](https://arxiv.org/abs/2611.12410v1)，11-09首投／11-10公告 | 密度坡反射压缩＋磁化群速度分裂；1D 3.53 ps→2.8 fs，2D改用1 ps／120 T。EW／ZW是口径外推，总效率属于两子脉冲 | [笔记](notes/shuai-2026-magnetized-plasma-modulator.md) · [PDF](pdfs/shuai-2026-magnetized-plasma-modulator.pdf) |
| Xia等，[2611.10870v1](https://arxiv.org/abs/2611.10870v1)，11-07首投／11-10公告 | 在线聚合改善1D Vlasov控制；60例配对数值评估，有限时间条件定理。损失归一化、模索引／波数及图轴口径待澄清；未部署到装置 | [笔记](notes/xia-2026-online-plasma-control.md) · [PDF](pdfs/xia-2026-online-plasma-control.pdf) |

三篇预印本的官方元数据无期刊版字段，分别作精确标题Crossref前三项查询，未核实同作品正式版。该限定查询不证明正式版不存在。按DOI、归一化标题、arXiv别名、作者与物理场景去重；相关前作不作为本篇期刊版本替代。

## 全文受限与后续重点

- **aeb708**：[锥靶定向中子源](https://doi.org/10.1088/1741-4326/aeb708)，旧候选定向复查：官方PDF HTTP200、text/html、14,371字节，跳转Radware，无有效PDF。
- **aebb4a**：[跨装置剖面预测与可微优化](https://doi.org/10.1088/1741-4326/aebb4a)，Crossref在线日期11-10、链接同时标注AM／VOR，未取得全文以核实版本，精确接收日期未核实；官方PDF同样返回14,371字节Radware HTML。有限精确标题检索未核实合法替代全文，不写摘要笔记。
- 细胞研究优先补S1–S5、原始膜／克隆数据、同辐射质脉宽扫描与跨批重复；磁化调制器优先查实际宽带输入、真实密度坡／大口径磁场、空间收敛及绝对功率能量账本。
- MITL优先补多炮统计、表面库存及电流反演误差；在线控制优先取得固定代码／种子、解释印刷口径、核对损失与物理范数以及端到端计算成本。
- CoilStellaration 2611.12689仅阅读摘要，TRIMEG++ 2611.12209仅列标题线索；旧tearing／RPC等线索本轮未精读，不计入完成数。

本轮未复跑作者物理、输运、训练、拟合、计时或实验；未新增激光光核核素完整生产链、临床或辐射防护验收。

## 来源与验证记录

- [检索范围](research/discovery.json) · [来源清单](research/sources.jsonl) · [选中文献元数据](research/selected-sources.json) · [期刊版核查](research/version-checks.json)
- [下载记录](download_report.json) · [PDF验证](pdf_validation.json) · [图表核验](research/visual-validation.json) · [补充材料核查](research/supplement-check.json)
- [静态数值／印刷式核对](research/static-checks.json) · [重试检查](research/retry-checks.json) · [未读线索](research/next-leads.json)
- [运行结果](run_results.json) · [最终范围审计](research/verification.json)
