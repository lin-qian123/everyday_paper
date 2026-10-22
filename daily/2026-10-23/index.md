# 每日论文索引：2026-10-23

本轮新增 **4 篇**，台账 **486 → 490**：2 篇 10-22 正式 VOR、1 篇 10-22 新正式 DOI 对应的 2025 作者稿、1 篇 10-20 官方 arXiv v1。覆盖室温聚变靶、成像软件、等离子体量子光学和束流机器学习；定量结果均属数值、软件或设计证据。

## 检索、去重与全文

- 正式来源优先：Crossref 2026-10-22 至 23，10 组主题查询、每组最多 75 条，返回 **677 行、458 个唯一 DOI**，无请求错误。大量 plasma/fusion 等词命中医学和无关工程；这是一轮有界检索。
- arXiv 五类最近 300 条，最新可见提交 **2026-10-21T17:33:40Z**。束流图网络经精确题名 Crossref 前三条检查未核实正式版，不据此断言不存在其他版本。公开来源另核查 APS、IOP、JOSS 和 Qu 作者稿。
- DOI/arXiv 别名、规范化标题、最近似标题、作者及物理场景联合去重。Qu 作者稿与新正式 DOI 只计一个作品；Du 从旧重试恢复，不与完成台账重复；束流图网络与昨日 WARP 谱 PDE 学习不同。
- **4 份 PDF 共 42 页、11,643,290 字节**，通过文件头、文件类型、SHA-256、pdfinfo/pypdf 页数一致、逐页可读文本与布局抽取。14 个身份/关键页、8 幅原图/原表摘录已目视检查；MinerU 三篇成功，IOP 报文件读取失败后使用已验证本地回退。
- PDF、布局文本和成功 MinerU 正文按仓库约定留本地、Git 忽略；笔记、必要原图、元数据、失败原因、核验与索引随 GitHub 发布。

## 新增论文

| 论文与实际阅读版本 | 内容与证据 | 中文笔记 |
|---|---|---|
| [Du 等，Nuclear Fusion，10-22 在线 VOR](https://doi.org/10.1088/1741-4326/aeb1db)；卷期为 67 (2027), 016007 | MULTI-IFE 一维多燃料模块和遗传算法；2.35 MJ→23.93 MJ 是计算靶增益，IFAR<17 不等于多维稳定验证。旧重试已恢复。 | [笔记](notes/Du%20et%20al.%20-%202026%20-%20Room%20temperature%20direct%20drive%20fusion%20targets.md) |
| [Zhang 等，JOSS 11(126), 11132，10-22 VOR](https://doi.org/10.21105/joss.11132) | BM3DORNL 合成中子 sinogram 去条纹；分开处理时间、硬件和 PSNR/SSIM，未测材料反演或剂量。 | [笔记](notes/Zhang%20et%20al.%20-%202026%20-%20BM3DORNL%20neutron%20tomography.md) |
| [Qu、Fisch，PRE，10-22 正式 DOI](https://doi.org/10.1103/c4r9-jsw7)；实际读 [arXiv:2507.12288v1，2025-07-16](https://arxiv.org/abs/2507.12288v1) | Raman/Langmuir 量子压缩理论；VOR 不可达，作者稿的匹配频差、噪声归一化、光子数与滑移疑点显式保留。 | [笔记](notes/Qu%20et%20al.%20-%202026%20-%20Plasma%20wave%20quantum%20squeezing.md) |
| [Zhang 等，arXiv:2610.28250v1，10-20](https://arxiv.org/abs/2610.28250v1) | Pelegant 合成束流与图闭合，结构守恒有独立检查；弱集体区间物理组件未显示精度增益，输出归一化主导训练差异。 | [笔记](notes/Zhang%20et%20al.%20-%202026%20-%20Physics%20constrained%20graph%20linac%20surrogate.md) |

## 全文重试与未入库线索

- **恢复** `10.1088/1741-4326/aeb1db`：Crossref 新 VOR 日期提供复查信号，IOP 官方 PDF 现在可取；正文首页核实 10-22 在线/2027 卷期，已完成笔记并移出队列。
- **新增** `10.1103/79kq-8mpn`（同步离子 surfing、定制密度）和 `10.1103/9237-5stj`（有限脉冲有质动力光栅）：APS harvest 在代理/直连均 404，期刊 PDF 在两模式均 403 “Just a moment” HTML。未取得可验证同篇作者稿，不写 abstract-only 笔记。离子标题初次 arXiv 查询限流；降低频率的作者/题词查询恢复 200、零条目。其余 42 条旧重试不变，队列 **43−1+2=44**。
- Qu 正式全文也受上述 APS 入口限制，但精确作者/题名可匹配官方旧作者稿，故以同作品不同版本入库，不新增第二条完成记录或缺全文重试。VOR 对照仍是后续任务。
- 碰撞无关 FDR、辐射重联、EAST 场景 RL、SiC 检测/波形学习及中子屏蔽复合材料等留为低优先级元数据线索，未精读全文，未计入入库。

## 阅读重点与证据边界

1. Du 的融合能量/激光能量与墙插效率不同；中子仅首碰近似，产氚反馈 5.2% 不是全燃料循环增殖比。相同 LiBD₂T₂ 脉冲的 DT 对照与重新优化 DT 的比较结果不同。图 6 注释与实际坐标不符，按图轴解释。
2. BM3DORNL 的 1900 倍属于 Fourier-SVD，340 倍属于 streak，不能与 multiscale 的较高 SSIM 拼成同一性能点；共有淡蓝差图背景来自缩放偏差。
3. Qu 仅作者稿有核验：式 (9) 方差与前文差因子二；“10¹⁸ 光子”与式 (10)/图不一致，不能作可信产额。正式版是否修正未知。
4. 图网络的反对称消息只保证相应离散空间电荷自力；学生推理不运行该模块。约 7% 是范围内留出模拟设置，未验证实机或强集体区间；0.159 s forward 与 0.378 s 含加载在线时间分开。
5. 本轮未复跑辐射流体、遗传优化、量子模型、图网络或成像 benchmark；未新增强外场 QED 观测、激光转换靶—光核/中子/同位素端到端实测、临床或防护验收。

## 可追溯记录

[PDF 核验](pdf_validation.json) · [下载报告](download_report.json) · [来源与检索范围](research/research-run.json) · [选中/重试原始元数据](research/sources.jsonl) · [候选筛选](research/candidate-screen.json) · [版本查询](research/version-checks.json) · [恢复的旧重试](research/retry-resolved.json) · [MinerU](research/mineru-attempts.json) · [原图/表来源](research/figure-manifest.json) · [本轮运行与验证](run_results.json)
