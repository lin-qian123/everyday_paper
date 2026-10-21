# 每日论文索引：2026-10-22

本轮新增 **4 篇**：1 篇 10-21 PRAB 正式 VOR、3 篇 10-19 官方 arXiv v1；台账 **482 → 486**。覆盖阿秒 XFEL 设计、质子照相验证、等离子体谱方法学习和辐射 PIC 离子加热。

## 检索、去重与全文

- 正式来源优先：Crossref 2026-10-21 至 22 的 10 组主题查询，每组最多 75 条，合计 **705 行、490 个唯一 DOI**；2 组初始 HTTP 429 经降低频率顺序补查恢复。宽泛关键词带来大量离题命中，本轮为有界检索。
- 官方 arXiv 五分类最近 300 条，最新可见提交 **2026-10-20T16:46:32Z**。三篇入选预印本经精确题名 Crossref 前三条检查，未核实同篇正式版；不据此断言不存在其他版本。
- DOI/arXiv 别名、规范化题名、最近似旧题名、作者和物理场景联合去重。PRIORA 与既有激光质子场/密度反演不同；含对辐射湍流与既有电子自旋极化、轻子各向异性论文不同；XFEL 新扫描与昨天 corrugated 整形实验不同。
- **4 份 PDF 共 72 页、47,134,658 字节**，通过文件头、文件类型、SHA-256、pdfinfo/pypdf 页数一致、逐页可读文本及非空布局文本核验。337,889 字节布局正文及四篇成功 MinerU pipeline 正文留本地；19 个身份/关键页与 8 幅原图摘录完成人工目视核查；正式 PDF 首页纠正了 MinerU 漏掉的一名作者。
- PDF 与全文抽取按仓库约定本地保留、Git 忽略；中文笔记、关键原图摘录、来源/裁框/哈希、下载与运行报告随仓库发布。

## 新增论文

| 论文与版本 | 核心内容及证据 | 中文笔记 |
|---|---|---|
| [Xu 等，PRAB 29, 103406，10-21 正式 VOR](https://link.aps.org/doi/10.1103/hqjn-r9k9) | GENESIS 三维时域扫描：后饱和超辐射、峰功率与单峰概率权衡；代表性高功率发不能代替全部发统计。 | [笔记](notes/Xu%20et%20al.%20-%202026%20-%20High%20power%20attosecond%20XFEL.md) |
| [Varentsov 等，arXiv:2610.26121v1，10-19](https://arxiv.org/abs/2610.26121v1) | GSI 2/4 GeV 质子照相数据对 PRIORA 的实验核验；有效响应含束靶运动，非激光质子实测。 | [笔记](notes/Varentsov%20et%20al.%20-%202026%20-%20PRIORA%20proton%20radiography%20verification.md) |
| [Chen 与 Kaptanoglu，arXiv:2610.27317v1，10-19](https://arxiv.org/abs/2610.27317v1) | WARP 弱形式与多步 rollout 学习谱 PDE 求解器；同算子库 FD 基线、已知库与模拟数据条件。 | [笔记](notes/Chen%20et%20al.%20-%202026%20-%20WARP%20spectral%20PDE%20solvers.md) |
| [Wang 等，arXiv:2610.26731v1，10-19](https://arxiv.org/abs/2610.26731v1) | 三维辐射 PIC 的含对湍流离子加热；天体数值模型，阈值、量纲和符号疑点保留。 | [笔记](notes/Wang%20et%20al.%20-%202026%20-%20Radiative%20pair%20loaded%20PIC%20ion%20heating.md) |

## 重试与未入库线索

- 新增 **10.1364/ome.606574**，*Enhanced Shock Pressure via Teflon Tape Confinement: A Soft Conformable Tamper for Laser-Driven Shock Applications*。Optica 页面/DOI 跳转为 **Site Maintenance HTML**（含 osamaintenance.azurewebsites.net），代理与直连都未返回 PDF；维护页未给 PDF 链接。精确题名 arXiv 无匹配，有限 web 检索未找到合法同篇作者稿。只保存元数据与失败记录，不写 abstract-only 笔记。队列 **42 → 43**，旧 42 条不变。
- 核质量可解释 AI、linac 图网络闭合、驱动重联辐射变光和 EAST 场景 RL 留作较低优先级线索，均未精读全文或计入入库。本轮没有新的可获取信号支持重复探测旧订阅/禁运来源。

## 阅读重点与证据边界

1. XFEL 的约 1 TW/66 as 是代表性单发；650 as 电子束出口单峰仅 37/200，整体平均与筛选子集不同。理想束扫描和 cw 设施概念不能写成已建成光源；谱宽反算只是参考。
2. PRIORA 115±6 μm 为联合反演的有效靶平面响应，包含探测与多发运动；4 GeV 裸靶无法唯一分开离焦和模糊，仍有约 15% 的极端材料带宽度残差。
3. WARP 的比较主要在已知正确算子库内，不是未知物理自动发现；低噪 Burgers 存在 FD 更好的情况。含对湍流的阈值选择、无量纲约定及图文符号疑点均保留。
4. 本轮未运行作者的 GENESIS、PRIORA/LADA、谱求解器训练或辐射 PIC。未新增激光转换靶—光核中子/同位素端到端实测，也未报告临床、防护验收或强外场 QED 观测。

## 可追溯记录

[PDF 核验](pdf_validation.json) · [来源与有界检索](research/research-run.json) · [原始选中元数据](research/sources.jsonl) · [版本查询](research/version-checks.json) · [MinerU](research/mineru-attempts.json) · [原图裁框与哈希](research/figure-manifest.json) · [本轮运行与验证](run_results.json)
