# 每日论文索引 - 2026-09-15

## 今日概览

- 运行日期：2026-09-15
- 新增论文数：2
- 最新性：周二早间运行时，官方 arXiv 目标分类的最新可见增量是 2026-09-14（周一）批次；本轮收录其中一篇已经正式接收、此前受 APS `HTTP 403` 阻塞但现有合法作者稿的 PRL，并补入 2026-09-11 正式发表的 HPLSE 实验论文。
- 主题分布：DIII-D helicon 电流驱动实验，以及低密度泡沫靶冲击的时间分辨 X 射线照相—MULTI/FLASH 流体模拟链。
- 检索范围：检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`physics.med-ph`、`nucl-ex`、`physics.app-ph`、`physics.optics` 与 `astro-ph.HE` 新增列表，并复查 APS、Cambridge HPLSE 及激光等离子体、PIC、强场 QED、HEDP、等离子体 ML、核诊断和激光加速束应用定向结果。多源聚合器没有返回可用记录，arXiv Atom API 又遇到 `HTTP 429`，因此使用官方分类页与文章页核验，不宣称覆盖全部数据库。
- 去重：按正式 DOI/arXiv identifier、规范化标题、历史 `daily/`、349 条完成台账、17 条重试队列、摘要和物理场景核对；两篇均不在完成台账。helicon 条目成功补回后从重试队列移除，队列降至 16 条。
- PDF / 正文：两份开放全文均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 和非空 `pdftotext -layout`；两篇均完成 MinerU 正文/图件转换，保留并逐张查看 17 张关键图。完整记录见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. First Experimental Evidence of Helicon Current Drive

- DOI：[10.1103/mbn4-fd4v](https://doi.org/10.1103/mbn4-fd4v)
- 正式接收：2026-09-08；作者稿 arXiv v1：2026-09-14
- 开放全文：[arXiv 摘要页](https://arxiv.org/abs/2609.12474)
- 期刊 / 平台：*Physical Review Letters* 接收稿；本地保存作者稿
- 本地 PDF：`daily/2026-09-15/pdfs/Lestz et al. - 2026 - First experimental evidence of helicon current drive.pdf`
- 中文笔记：[Lestz et al. - 2026 - First experimental evidence of helicon current drive.md](notes/Lestz%20et%20al.%20-%202026%20-%20First%20experimental%20evidence%20of%20helicon%20current%20drive.md)
- 来源影响力分：10/10
- 专业相似度分：9/10
- 推荐理由：把 476 MHz 行波天线、调制 ECE 沉积、电子比压扫描、ECH 加热匹配对照、MSE/EFIT q 剖面和 GENRAY/TRANSP 电流分解接成同一证据链，是磁约束射频电流驱动中少见的实验机制闭合。
- 一句话总结：DIII-D 在核心得到 `20 ± 10 kA` 的残差电流，与 GENRAY 在同一区域约 `21 kA` 的首程预测一致；但这是平衡重建减去模型化欧姆/bootstrap/NBI/ECCD 电流后的结果，单侧天线尚未完成传播方向反转，低比压 L 模结果也不能直接外推为反应堆效率。

### 2. Laser-driven shock wave propagation in low-density foam targets investigated by time-resolved X-ray radiography and hydrodynamic simulations

- DOI：[10.1017/hpl.2026.10174](https://doi.org/10.1017/hpl.2026.10174)
- 正式发表：2026-09-11
- 来源：[Cambridge Core 文章页](https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/laserdriven-shock-wave-propagation-in-lowdensity-foam-targets-investigated-by-timeresolved-xray-radiography-and-hydrodynamic-simulations/A816C3577E537869C352798728AEF660)
- 期刊 / 平台：*High Power Laser Science and Engineering* 14, e77
- 本地 PDF：`daily/2026-09-15/pdfs/Turianska et al. - 2026 - Laser-driven shock propagation in low-density foam.pdf`
- 中文笔记：[Turianska et al. - 2026 - Laser-driven shock propagation in low-density foam.md](notes/Turianska%20et%20al.%20-%202026%20-%20Laser-driven%20shock%20propagation%20in%20low-density%20foam.md)
- 来源影响力分：9/10
- 专业相似度分：9/10
- 推荐理由：将 `15/25/35 ns` X 射线照相、靶内推动层轨迹、空间分辨率标定、一维/二维 MULTI、FLASH 交叉比较和合成照相放在统一框架中，适合作为 HEDP 泡沫靶诊断—模拟证据边界范例。
- 一句话总结：Ti 推动层在 `0.1 g/cm³` TMPTA 泡沫中的平均速度为 `18.5 ± 2 km/s`，模拟以 `(3–5)×10¹³ W/cm²` 有效强度复现实验量级并支持中心轴准一维动力学；该强度是模型匹配参数，`~1 Mbar` 也是模拟量，不能写成独立测得的耦合效率或压力。

## 未入库候选与取舍

- 同一 arXiv 批次的 `2609.12479` 研究栅控电子沟道中的非均匀流体等离子体波不稳定性，属于 InGaAs/GaAs 理论模型，与仓库的激光等离子体、HEDP、PIC 和束流应用主线距离较远，未用来扩充数量。
- 多个目标分类的 2026-09-14 批次没有发现新的、可获取且证据链更直接的强场 QED、激光束—转换靶—光核/中子、剂量或屏蔽论文。本轮仍不以相邻主题替代端到端应用证据。
- helicon 论文不是把 APS 摘要升级为全文结论：作者于 2026-09-14 发布的 arXiv 全文通过了 PDF 与正文核验，正式 DOI、接收日期和作者稿来源分别保留；相应旧阻塞项才从重试队列移除。

## 当日综合总结

- 两篇论文都把“直接观测”和“模型反演”分开：helicon 的 ECE、MSE 与锯齿是观测，独立电流分量来自 EFIT/TRANSP/GENRAY 分解；泡沫靶的透射图和推动层位置是观测，有效强度、压力及完整密度场来自流体模型。
- 最值得复用的实验设计思想是对照与合成诊断：前者用加热匹配排除纯温升解释，后者把模拟密度场经衰减与成像几何投影后再与图像比较。
- 推荐阅读顺序：先看 helicon 的图 1–3，理解功率沉积和电流残差的不同推断层级；再看泡沫靶的图 6–9 与图 13，比较实验定位、一维标度、二维效应和跨代码一致性各自能证明到哪里。
