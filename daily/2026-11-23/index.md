# 2026-11-23 每日论文

新增 **2篇全文与中文结构化笔记**，台账 **590→592**：一篇11-22在线的出版社Article in Press、一篇11-19首投／11-20公告的arXiv v1。没有取得新的最终VOR。全部590个既有完成对象保持；Gd光中子诊断新增1条受限全文重试，队列 **74→75**，旧74对象保持，未整队重复探测。

## 本轮论文与阅读重点

| 实际全文版本 | 主要内容与证据边界 | 本地阅读 |
| --- | --- | --- |
| Giakoumakis等，Scientific Reports [10.1038/s41598-026-78588-x](https://www.nature.com/articles/s41598-026-78588-x)，10-27接收、11-22在线Article in Press | 100 Hz、17.48 keV Mo Kα源与单棋盘光栅的静态PMMA相衬成像实测。4 mJ小源斑在等480 s累计曝光下优于12 mJ大源斑；最高0.922±0.008是1920 s配置的y方向相关系数，不能视为单发／绝对相位标定。 | [中文笔记](./notes/giakoumakis-2026-phase.md) · [21页出版社早期全文](./pdfs/giakoumakis-2026-phase.pdf) |
| Elkina、Pukhov，[arXiv:2611.26402v1](https://arxiv.org/abs/2611.26402v1)，11-19首投、11-20公告；未核实同作期刊接收／发表 | 用零损失原子＋正Gamma聚合软光子反冲，匹配局部无发射概率和前两矩；磁场／离子通道／激光场解析与轨迹数值测试。正支持不保证损失小于可用能量，停止轨迹及谱后处理边界明确；不是实验或完整自洽PIC验证。 | [中文笔记](./notes/elkina-2026-recoil.md) · [34页作者全文含两补充](./pdfs/elkina-2026-recoil.pdf) |

先读成像笔记的三配置表与原图2／7，区分近似等光子计数和等时间；再读反冲构造、过度损失风险及状态更新基线。两份全文共 **55页**，PDF与布局文本保留本地，沿用Git忽略；笔记、有效图摘录及来源／核验记录纳入Git。

## 正式候选的全文重试

Zong等，Journal of Radioanalytical and Nuclear Chemistry [10.1007/s10967-026-11304-1](https://link.springer.com/article/10.1007/s10967-026-11304-1)，11-21发表，比较e-LINAC光中子源的中子寿命／透射法测Gd浓度。上轮仅元数据，本轮首次调查全文：文章HTTP200为订阅预览HTML343794B；官方PDF入口HTTP200重定向到文章HTML343760B，非PDF。HAL精确标题前5查询200／numFound0，有界网页检索未找到核实的同作合法作者稿。新增精确失败重试，**未入完成台账、未写摘要式笔记**，没有订阅／付费操作。

## 检索覆盖与去重

Crossref十主题、journal-article、在线日期11-22至23、每主题相关性前40，返回 **232行／185 DOI**；十请求均200。覆盖激光等离子体、QED、HEDP、PIC、ML、转换靶与伽马、光核中子与核素、离子靶、屏蔽及核诊断。标题、期刊、DOI及人工相关性复核后，选择最新成像正式研究，其余大量“plasma／fusion”等词义无关条目未入库。

arXiv十类最新块仍是11-20，**347行／327 ID**，与上轮集合一致，包含旧作跨类。没有新公告不代表没有未读高质量论文，因此本轮续读已发现的软反冲方法。两新作品与590旧对象按DOI、规范化标题、最近似标题及作者／摘要／物理情景去重，无同作冲突；未以预印本与期刊状态拆成重复条目。

[2611.24653活化核数据报告](https://arxiv.org/abs/2611.24653)本轮只更新官方元数据／摘要检查，未下载／精读，继续列未读；Crossref新发现400 MeV碳离子铁靶／冷却剂活化FLUKA论文10.1515/kern-2026-0085仅元数据，未调查全文可得性，不虚构下载失败。以上为有界日更，非领域穷尽检索。

## 原文疑点与证据边界

成像早期PDF的球投影厚度印刷式缺整球弦长因子2；图2／7的“2π rad”单位／约146数值与正文球径、折射率的绝对相位未闭合。正文消色差距离1.78 m与表4的187.42 m冲突；仅做窄带算术复核，未替作者修订。最高相关系数主要反映形状，并且±值由球径公差传播；Confidence Map是梯度闭合自一致性，不覆盖共同可积偏差。单光栅实验实际需仅样品、样品＋光栅、仅光栅三种采集，飞秒驱动不代表飞秒单发成像。

反冲方法需分开冻结核与状态更新、磁冷却与分辨轨道、初始总体与幸存轨迹、动力学计时与谱重建成本。Gamma有正支持但仍有上尾越界风险，不能因没有能量增益就认为所有轨迹合法。本文未复跑作者程序／实验，未新增临床、光核核素完整链或防护验收。

## 文件与索引验证

两PDF通过文件头／MIME／SHA、pdfinfo／pypdf／PyMuPDF页数及逐页非空文本检查；原页与裁图实际查看，裁框与源像素一致性另行记录。MinerU历史401/A0211认证失效本次未复测、零请求，明确本地全文／渲染回退。

台账变更后运行 `python scripts/build_indexes.py`，同步根／分类／每日／单篇索引及README、TODO。AGENTS.md原有修改保留、排除本次提交。测试及精确提交范围的检查结果见运行和核验记录。

- [检索范围](./research/discovery_sources.json) · [Crossref候选](./research/crossref_discovery.json) · [arXiv候选](./research/arxiv_discovery.json)
- [成像正式元数据](./research/imaging-crossref.json) · [Gd正式元数据](./research/gd-crossref.json) · [版本证据](./research/publisher_status_evidence.json)
- [新增对象](./research/selected_metadata.json) · [去重检查](./research/dedup_checks.json) · [来源受限记录](./research/source_access_checks.json) · [未读线索](./research/deferred_candidates.json)
- [下载记录](./download_report.json) · [PDF验证](./pdf_validation.json) · [成像阅读与图来源](./research/imaging_reading.json) · [反冲阅读与图来源](./research/recoil_reading.json)
- [运行结果](./run_results.json) · [最终核验](./research/verification.json)
