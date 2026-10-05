# 2026-10-06 定向论文研究报告

## 检索覆盖

安装的多来源搜索层对 3 个定向查询没有返回可用结果。官方 arXiv Atom API 已显示 2026-10-02 的新投稿，覆盖 plasma physics、accelerator physics、instrumentation、computational physics、nuclear experiment、medical physics 和 applied physics；从中筛出 5 篇高相关全文。Crossref 对 2026-10-05 至 10-06 的 6 组查询读取 568 条元数据、473 条去重作品；AIP 最新期补入激光 X 射线照相正式论文。覆盖是定向的，不宣称穷尽全部期刊或数据库。

## 选择逻辑

- **正式实验优先：** 两篇 RSI VOR 分别闭合激光背光源“产额—谱—分辨率”和 Titan 热致密等离子体多谱仪平台。
- **PIC 机制与数值误差分开：** 3D 重联论文研究物理加速通道；带宽论文研究降噪对线性模的扰动，避免把算法改进与物理结论混为一谈。
- **前沿方法保留但降级口径：** 张量网络稿是能力原型，不是成熟 PIC 替代；NeutronGym 是 McStas/RL 软件实验，不是上机仪器设计。
- **全文门槛：** HL-3 CXRS 正式论文高度相关，但官方 IOP 路径只返回 HTML 验证页，进入重试而不生成摘要型笔记。

## 共同证据边界

Benkadoum 和 Fairchild 含直接激光实验，但双 Maxwellian、GEANT4、PrismSPECT、MERL 以及温度/密度解释均为模型辅助。Karavola、Agrawal、Connor 与 NeutronGym 均是数值或软件证据；其中 Connor 只有短篇原型，NeutronGym 的训练多数为单 seed 且固定布局。没有在本地运行任何 PIC、原子物理、输运、张量网络、McStas 或 RL 计算。

## PDF 与解析

6 份 PDF 共 97 页，通过 `%PDF-`、`file`、字节数、SHA-256、`pdfinfo` 和非空 `pdftotext -layout`。人工核查 36 个关键页，并保留 6 幅可追溯图。MinerU 的本地路径入口不受支持，6 个公开 URL 任务也全部失败；因此按规则采用本地全文、布局文本和渲染回退，未把解析失败写成 PDF 失败。
