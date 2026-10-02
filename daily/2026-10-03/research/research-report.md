# 2026-10-03 定向论文研究报告

## 检索覆盖

本轮先运行安装的多来源搜索层，4 个定向查询没有返回可用结果；随后核对官方 arXiv `/new` 页面中 `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.ins-det`、`physics.optics`、`physics.med-ph`、`physics.data-an`、`nucl-ex`、`nucl-th`、`hep-ph`、`hep-ex`、`cs.LG` 与 `cond-mat.mtrl-sci` 的 2026-10-02 公告批次，并用 Crossref 核对 2026-10-01 至 10-03 的正式元数据。覆盖是定向的，不宣称穷尽全部期刊。

## 选择逻辑

- **诊断与可解释 ML：** `2610.01485` 直接使用既有 AWAKE schlieren 实验图像，并用模拟信号训练可审计解析式；半径结果较稳健，鞘宽跨密度迁移受限。
- **PIC 守恒：** `2610.01429` 针对有限 β 磁化等离子体跨越电子回旋/Debye 尺度的问题，在离散层面同时闭合能量和电荷守恒。
- **PIC 稳定性：** `2610.02052` 从无网格相互作用推导 MCP/ECP 的离散谱，量化网格 aliasing、形函数和 `N_ppc` 的关系。
- **实时部署：** `2610.00845` 把十个聚变 AI 模型的 CPU/GPU 延迟与 DIII-D/ITER 毫秒控制预算对齐，但没有反应堆闭环验证。
- **核反应与应用：** `2610.01719` 有近阈值厚靶中子的直接实验计数，并把 TALYS/SRIM 外推与核医学、地下本底及核合成应用分层；本地版本为已接收作者稿，不是 VOR。

## 共同证据边界

五篇中只有 Demeter 和 Meisel 使用直接实验材料：前者重新分析既有 AWAKE 图像，后者直接测量近阈值厚靶中子产额。Morozov 是算法推导与数值测试，Finn/Evstatiev 是一维静电冷等离子体理论与 PIC 验证，Chen 是异构硬件上的离线推理基准。本地只做 PDF、正文、公式和图表核验，没有重跑符号回归、xpic、PIC 本征模、AI 部署或 TALYS/SRIM。解析公式不等于跨仪器泛化，守恒不等于所有物理统计量收敛，冷一维稳定性不等于生产 PIC 稳定，平均 latency 不等于闭环最坏时延，模型外推活度也不等于同位素生产实测。

## PDF 与解析

5 份官方 arXiv PDF 都通过文件头、类型、字节数、SHA-256、页数和非空布局文本检查，共 20 个抽样页完成渲染和人工查看。本地路径不被 MinerU 当前工作流支持；改用官方 URL 后任务被接受，但在限定 5 分钟内保持 `pending`，因此按技能 fallback 使用 `pdftotext -layout` 与页面渲染，未把 MinerU 写成成功。
