# 2026-11-24 每日论文

新增 **4篇经全文验证的中文结构化笔记**，台账 **592→596**。一篇11-23在线的出版社Article in Press，三篇11-20首投／11-23公告的arXiv v1；没有取得新的最终VOR。592个旧完成对象保持，新增2项正式论文的全文重试，队列 **75→77**，旧75项保持。

## 今日论文与阅读重点

| 论文／实际版本 | 主要结果及证据限制 | 本地全文与笔记 |
| --- | --- | --- |
| Xu等，Scientific Reports，[10.1038/s41598-026-81462-5](https://doi.org/10.1038/s41598-026-81462-5)，11-16接收、11-23在线Article in Press | 100 nC、10 GeV电子打5 mm Pb，Geant4产生分布交给二维PIC，50 mm后反μ子最高15.7 GeV、留42 fC；三维只核局部近出界场，未完成加速实验。 | [中文笔记](./notes/xu-2026-antimuon.md) · [12页PDF](./pdfs/xu-2026-antimuon.pdf) |
| Han等，[2611.27772v1](https://arxiv.org/abs/2611.27772v1)，同作期刊未核实 | 铅箔谐振声学探测常规脉冲电子韧致X射线，约1–40 mGy(Si)、六点每点一发；R²=0.9998是固定配置离线标定，重复性、总不确定度及在线全链延迟未建立。 | [中文笔记](./notes/han-2026-acoustic.md) · [17页PDF](./pdfs/han-2026-acoustic.pdf) |
| Starodubtseva等，[2611.27857v1](https://arxiv.org/abs/2611.27857v1)，同作期刊未核实 | 准三维两级DLA，最高能约94→225 MeV；超过5 MeV的首级／次级来源电荷6.04→4.55 nC，另有次级自注入1.14 nC。阈值比不等于捕获率，需计入双激光总成本。 | [中文笔记](./notes/starodubtseva-2026-staged-dla.md) · [9页PDF](./pdfs/starodubtseva-2026-staged-dla.pdf) |
| Xie等，[2611.27027v1](https://arxiv.org/abs/2611.27027v1)，同作期刊未核实 | 94能级锂CR压缩为10维神经ODE；解码正归一化、1480留出轨迹电荷比例MAE中位0.0042。76 μs依赖参考弧长网格和大批次；可部署两遍153 μs仍非端到端延迟，存在末态漂移与重启失败。 | [中文笔记](./notes/xie-2026-latent-cr.md) · [32页PDF](./pdfs/xie-2026-latent-cr.pdf) |

建议先看声学实验的同发TLD与误差定义，再看两级DLA的密度／转交阈值和驱动成本。反μ子关注转换靶产额与CTR加载折中；ML重点读可部署网格、同批次基线与失败例，避免把吞吐数字直接当本地CR求解器的加速比。

## 正式候选全文重试

- Lan等，Applied Physics Letters，[10.1063/5.0352710](https://doi.org/10.1063/5.0352710)，11-06接收、11-23发表，楔形改造气靶准直DLA电子。官方文章403 HTML 5757字节，Crossref给出的实际VOR PDF403 HTML 5696字节；HAL精确标题前5返回0，有界网页检索没有核实同作合法作者PDF。
- Shaheen等，Kerntechnik，[10.1515/kern-2026-0085](https://doi.org/10.1515/kern-2026-0085)，11-09接收、11-23在线，400 MeV碳离子铁靶／冷却剂FLUKA活化。官方HTML、PDF、德语PDF以及公开检索找到的open-access参数PDF在本地均返回202、text/html、0字节。网页工具能索引官方正文／PDF片段，但没有取得可验证本地PDF；HAL精确标题前5返回0。

两项都未进完成台账、未写摘要式全文笔记。没有订阅或付费操作，也没有整队重复下载75个历史失败候选。

## 检索覆盖与去重

Crossref按十主题、journal-article、在线日期11-23至24、每主题相关性前40，最终 **400行／353个不同DOI**；两主题在429后经有界顺序请求恢复，最终均200。主题覆盖激光等离子体、QED、HEDP、PIC、ML、电子转换靶伽马、光核核素、中子诊断、离子辐照与屏蔽。最初一次arXiv页面标题结构解析失败，修复后只以保存成功的完整快照统计检索行数；全部请求不是新增论文计数。

官方arXiv十类最新公告块为11-23，**277行／260 ID**，包含跨类条目。DOI、规范化标题、别名及最近似标题结合作者、摘要和物理情景复核；四新作没有同作冲突。CR论文承接作者flow-map前作但有新的连续向量场及对照；两级DLA与仓库luminal模阶梯尾场方案机制不同。论文正式状态与实际阅读版本单独记录，不按版本重复计数。

ICF热层点火[2611.27760](https://arxiv.org/abs/2611.27760)只核官方元数据／摘要，未下载／精读；新51V低能光核10.1140/epjp/s13360-026-08565-w仅Crossref线索，全文可得性未调查。旧活化2611.24653仍未读。此轮为有界日更，不是领域穷尽检索。

## 原文疑点与证据边界

反μ子MC使用10⁴产生偏置因子，须权重还原；局部峰值、两端最大能差／距离及全粒子能量账不同，583 J谱损失与453 J做功未闭合。声学mGy(Si)不是局域铅剂量；同记录相位替换和独立幅值归一不能算绝对预测验收。

DLA原子密度与电离电子密度、转交pₓ>5mc与能谱5 MeV切选分别说明；原文相速方向、式(4)分量、225／228.8 MeV差异保留。CR主参考网格包含测试轨迹时间结构，末态Jacobian／超窗和清零时钟重启失败明确；密度单位、时间跨度和守恒末位数字冲突未擅自修正。

没有复跑作者MC、PIC、训练或声学程序／实验，也没有新增临床、完整光核核素链或防护验收。

## 文件与索引核验

四PDF共 **70页／12,630,527字节**，通过PDF签名、MIME、SHA-256、pdfinfo／pypdf／PyMuPDF页数一致及逐页非空文本检查。阅读者实际目视42个不同源页；18幅保留原图表由主代理重开，并按源PDF裁框／倍率重新渲染比对像素。PDF／布局文本保留本地，沿用Git忽略；笔记、图表摘录、元数据和检查记录纳入本轮提交。

MinerU历史401/A0211认证失效本次未复测、零请求，明确本地文本／渲染回退。台账变化后运行`python scripts/build_indexes.py`，同步相关README、TODO和索引；原有AGENTS.md修改保留且排除提交。测试、精确提交范围和最终发布流程见运行／核验记录，最终提交号与实时远端一致性记入自动化记忆。

- [检索范围](./research/discovery_sources.json) · [Crossref快照](./research/crossref_discovery.json) · [arXiv快照](./research/arxiv_discovery.json)
- [候选元数据／访问](./research/candidate_metadata_access.json) · [正式版状态](./research/publisher_status_evidence.json) · [全文访问失败](./research/source_access_checks.json) · [作者库检索](./research/author_repository_checks.json)
- [新增对象](./research/selected_metadata.json) · [去重核对](./research/dedup_checks.json) · [未读线索](./research/deferred_candidates.json)
- [下载报告](./download_report.json) · [PDF核验](./pdf_validation.json) · [运行结果](./run_results.json) · [最终核验](./research/verification.json)
- [反μ子图源](./research/xu-2026-antimuon-reading.json) · [声学图源](./research/han-2026-acoustic-reading.json) · [DLA图源](./research/staged_dla_reading.json) · [CR图源](./research/latent_cr_reading.json)
