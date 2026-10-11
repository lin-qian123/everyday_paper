# 每日论文索引 - 2026-10-12

## 今日概览

- 运行日期：2026-10-12
- 新增论文数：6（1 篇 2026-10-09 正式出版记录，对应作者预印本全文；5 篇 2026-10-08 官方 arXiv 预印本）。
- 最新性：官方 arXiv 目标分类最新高相关投稿日期为 2026-10-08；Crossref 对 2026-10-09 至 10-12 做 15 组由宽到窄的主题/标题查询。安装的多来源搜索层对 3 个定向查询返回 0 条，故转用官方 arXiv、Crossref、APS 与 IOP。
- 主题：THz 锁时外注入 LWFA、LM26 磁化靶聚变压缩加热与 Thomson 诊断、XFEL 共振 ICF 混合诊断、PIC 偏振中子，以及面向 Vlasov/漂移动力学的 Lagrangian PINN。
- 去重：按 DOI/arXiv、规范化标题、430 条完成台账、28 条重试队列、来源 URL、正式版—预印本关系、摘要和物理场景检查；LM26 两文共享 LMC-12 炮次但分别报告装置结果和诊断实现，未伪装成独立复现实验。
- PDF / 正文：6 份 PDF 均通过 `%PDF-`、`file`、`pdfinfo`、`pypdf`、SHA-256 与非空 `pdftotext -layout`；共 78 页、23,658,952 字节，人工核查 12 个关键页并解码 6 幅保留图。MinerU 对 6 个公开 URL 均 `parsing failed`，故明确使用已验证本地 PDF、布局文本和渲染回退。
- 重试：IOP 正式论文 `10.1088/1361-6587/aeb280` 的 PDF/DOI/正文路线都返回 HTML/Radware 验证页，未生成笔记，进入结构化重试；队列 `28 → 29`。
- 覆盖边界：定向增量筛选，不宣称穷尽所有期刊、预印本或数据库。

## 论文清单

### 1. Controlling external injection in laser-plasma accelerators with terahertz frequency bunch manipulation

- 标识符：[DOI: 10.1103/wb14-xvj2](https://doi.org/10.1103/wb14-xvj2)
- 发表：2026-10-09，*Physical Review Research* 正式记录；全文核读使用对应 [arXiv:2604.16059v1](https://arxiv.org/abs/2604.16059) 作者预印本，不冒充 APS VOR
- 中文笔记：[Amini et al. - 2026 - THz-controlled external injection for LWFA.md](notes/Amini%20et%20al.%20-%202026%20-%20THz-controlled%20external%20injection%20for%20LWFA.md)
- 来源影响力分：9/10；专业相似度分：10/10
- 推荐理由：把太赫兹锁时、束团压缩、横向匹配和 FBPIC 等离子体段连成逐发束质稳定性链。
- 一句话总结：100 次 S2E 模拟把 GeV 级能量抖动从 `13.5%` 降到 `1.5%`；理想高斯束的 `0.2%` 仍是优化模拟。

### 2. Compressional heating above 1 keV on the LM26 magnetized target fusion machine

- 标识符：[arXiv:2610.11890](https://arxiv.org/abs/2610.11890)
- 版本：2026-10-08，官方 arXiv v1
- 中文笔记：[Howard et al. - 2026 - LM26 compressional heating above 1 keV.md](notes/Howard%20et%20al.%20-%202026%20-%20LM26%20compressional%20heating%20above%201%20keV.md)
- 来源影响力分：8/10；专业相似度分：9/10
- 推荐理由：给出大型锂内衬压缩的多诊断 HEDP/磁化靶聚变实验，并把直接量与模型反演分开。
- 一句话总结：AXUV/Thomson 支持 `1180±65/1090±40 eV` 电子温度；`459±33 eV` 离子温度依赖中子产额、热化与燃料比例假设。

### 3. Thomson Scattering Measurement of 1 keV Electron Temperature on Lawson Machine 26

- 标识符：[arXiv:2610.11769](https://arxiv.org/abs/2610.11769)
- 版本：2026-10-08，官方 arXiv v1；与上一条共享 LMC-12 炮次
- 中文笔记：[Carle et al. - 2026 - LM26 Thomson scattering at 1 keV.md](notes/Carle%20et%20al.%20-%202026%20-%20LM26%20Thomson%20scattering%20at%201%20keV.md)
- 来源影响力分：8/10；专业相似度分：9/10
- 推荐理由：详细量化狭窄前向散射、角度误差、背景光和内衬遮挡下的 1 keV Thomson 诊断实现。
- 一句话总结：双视线八时刻系统测得 `1090±40 eV`，第 8 脉冲因击中内衬而不可用；不是第二次独立压缩实验。

### 4. Imaging ablator-fuel mix of hot spot in inertial confinement fusion via resonant X-ray absorption using an X-ray free electron laser

- 标识符：[arXiv:2610.11603](https://arxiv.org/abs/2610.11603)
- 版本：2026-10-08，官方 arXiv v1
- 中文笔记：[Huang et al. - 2026 - Resonant X-ray imaging of ICF mix.md](notes/Huang%20et%20al.%20-%202026%20-%20Resonant%20X-ray%20imaging%20of%20ICF%20mix.md)
- 来源影响力分：8/10；专业相似度分：10/10
- 推荐理由：把铜丝共振 XFEL 实验与 Cu/W 掺杂 ICF 壳层合成诊断连接，同时明确烧蚀层混合的实验—设计边界。
- 一句话总结：`8.21 keV` 铜丝实验验证电荷态敏感吸收；球形 ICF 混合和烧蚀阶段仍是二维 FLASH/原子模型预测。

### 5. Beam filamentation instability drives deuterium-tritium fusion with polarized neutron emission

- 标识符：[arXiv:2610.11061](https://arxiv.org/abs/2610.11061)
- 版本：2026-10-08，官方 arXiv v1
- 中文笔记：[Qiu et al. - 2026 - Beam filamentation driven DT fusion.md](notes/Qiu%20et%20al.%20-%202026%20-%20Beam%20filamentation%20driven%20DT%20fusion.md)
- 来源影响力分：7/10；专业相似度分：10/10
- 推荐理由：提供电子丝化—离子加速—D–T 反应—中子偏振的自洽二维 PIC 机制链。
- 一句话总结：模型在 `p₀=100m_ec` 给出 `6.4×10^4` 中子计数和约 `60%` 角向偏振；无限束和理想预偏振靶限制绝对源强外推。

### 6. A neural characteristic mapping method: Lagrangian PINNs based on flow maps for transport-dominated problems

- 标识符：[arXiv:2610.12395](https://arxiv.org/abs/2610.12395)
- 版本：2026-10-08，官方 arXiv v1
- 中文笔记：[Campos Pinto et al. - 2026 - Neural characteristic maps for kinetic transport.md](notes/Campos%20Pinto%20et%20al.%20-%202026%20-%20Neural%20characteristic%20maps%20for%20kinetic%20transport.md)
- 来源影响力分：7/10；专业相似度分：8/10
- 推荐理由：用流映射而非分布函数承载相空间细丝化，并在 Vlasov 和简化 tokamak 漂移动力学上给出守恒/误差基准。
- 一句话总结：SympNet 在 Landau/双流测试明显优于普通 PINN，漂移动力学频率误差约 `0.5%`；低维成本仍不及网格法。

## 当日综合总结

- 本轮直接实验主要是 LM26 的同一 LMC-12 压缩炮次、其 Thomson 诊断，以及 Huang 等的铜丝 XFEL proof-of-principle；Amini、Qiu、Campos Pinto 的关键性能均为数值结果。
- LM26 两篇是互补报告，不把同一炮次重复包装成独立复现；AXUV、Thomson、中子反演和 ISM 的证据等级也分别保留。
- Huang 等没有在球形点火壳层上实测混合，Qiu 等没有激光到偏振中子实验，Amini 等没有实机外注入闭环；不能把设计性能升级成装置成绩。
- 本轮没有运行 ASTRA/GPT/ELEGANT/FBPIC、ISM/BPR/MCNP、FLASH/SCFLY/FLYCHK、PIC 自旋反应模块、GYSELA 或 PINN 训练。
