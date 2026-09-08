# 每日论文索引 - 2026-09-09

## 今日概览

- 运行日期：2026-09-09
- 新增论文数：3
- 重点来源：3 篇官方 arXiv 最新预印本；正式来源增量优先复查后，没有发现比当前候选更直接、可获取且非重复的论文。
- 主题分布：电子束–强激光碰撞搜寻 millicharged particles、MRX 半碰撞电子电流片的真实质量比动理学模拟、DIII-D/MAST 无磁诊断平衡重建机器学习挑战。
- 检索范围：检查 HPLSE accepted manuscripts / latest volume、APS PRL / PRResearch / PRE / PRApplied accepted 页面、官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.optics`、`nucl-ex` 和 `hep-ph`，并定向检索 laser–plasma、PIC、strong-field QED、γ / 光核 / 中子 / 同位素、材料辐照、诊断、radiation protection 与 plasma ML。官方 arXiv 当前最新可用批次仍到 2026-09-04。
- 去重：按 DOI / arXiv identifier、规范化标题、历史 daily、重试队列、摘要与物理场景核对 `state/processed_articles.json`。三篇均未入库；其中 Fusion Equilibrium Challenge 是跨装置公开基准，不是此前 MAST-U neural virtual circuit 的重复条目。
- PDF / 正文：3 份官方 arXiv PDF 通过 `%PDF-`、`file` 类型、`pdfinfo` 页数 / 元数据、SHA-256 和非空 `pdftotext -layout`。当前环境没有 `MINERU_TOKEN`，因此未声称完成 MinerU 转换；9 个关键 PDF 页面已渲染、解码并人工查看。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Exploring millicharged particles in laboratory and astrophysical strong-field regimes

- DOI：[10.48550/arXiv.2609.03399](https://doi.org/10.48550/arXiv.2609.03399)
- arXiv v1：2026-09-03
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.03399)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-09/pdfs/Jiang et al. - 2026 - Millicharged particles in strong-field regimes.pdf`
- 中文笔记：[Jiang et al. - 2026 - Millicharged particles in strong-field regimes.md](notes/Jiang%20et%20al.%20-%202026%20-%20Millicharged%20particles%20in%20strong-field%20regimes.md)
- 来源影响力分：7/10
- 专业相似度分：8/10
- 推荐理由：把 Furry picture / Volkov dressed states 下的 electron–laser trident 过程与 magnetar polar-gap Schwinger production 放进同一 millicharged-particle 参数平面，并显式估算不可约 neutrino background。
- 一句话总结：作者投影 LUXE 参数下实验室灵敏度可到 $\epsilon\sim10^{-8}$，强度参数 $\eta=10$ 时约 $3\times10^{-9}$；magnetar energy-loss 约束对 $m_\chi\lesssim10^{-2}\,\mathrm{eV}$ 可到 $\epsilon\sim10^{-9}$。这些都是理想平面波、计数与极区模型上的理论投影，不是 LUXE 或 magnetar 的 MCP 观测。

### 2. Revisiting the MRX Electron Current Sheet Width with Semi-Collisional Kinetic Simulations at Hydrogen Mass Ratio

- DOI：[10.48550/arXiv.2609.01793](https://doi.org/10.48550/arXiv.2609.01793)
- arXiv v1：2026-09-01
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.01793)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-09/pdfs/Son et al. - 2026 - MRX electron current sheet width.pdf`
- 中文笔记：[Son et al. - 2026 - MRX electron current sheet width.md](notes/Son%20et%20al.%20-%202026%20-%20MRX%20electron%20current%20sheet%20width.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：用含二元 Coulomb 碰撞的 2D VPIC、圆柱 MRX 几何和真实氢质量比，正面复查持续十八年的电子片宽与非理想电场力平衡差异，并把实验探针采样链纳入模拟比较。
- 一句话总结：模拟给出 $\delta_{BT}=0.744\pm0.054\,\mathrm{cm}=6.26\pm0.45\,d_e$，落入 MRX 的 `5.5–7.5 d_e` 范围；压力张量散度约支撑 `76%`、碰撞摩擦补足其余，`3 cm` 轴向采样可重现历史缺口。但 $\rho_e$ 归一化宽度仍相差约 `3–6` 倍，这不是对三维异常耗散已被排除的通用证明。

### 3. The Fusion Equilibrium Challenge: Inferring Magnetic Geometry Without Magnetic Diagnostics

- DOI：[10.48550/arXiv.2609.01750](https://doi.org/10.48550/arXiv.2609.01750)
- arXiv v1：2026-09-01
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.01750)
- 期刊 / 平台：arXiv 预印本 / NeurIPS Competition Track challenge proposal
- 本地 PDF：`daily/2026-09-09/pdfs/Nakkina et al. - 2026 - Fusion Equilibrium Challenge.pdf`
- 中文笔记：[Nakkina et al. - 2026 - Fusion Equilibrium Challenge.md](notes/Nakkina%20et%20al.%20-%202026%20-%20Fusion%20Equilibrium%20Challenge.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把外部 PF coil currents 与 Thomson $T_e/n_e$ 映射为二维 $\psi(R,Z)$，并用 DIII-D 到 MAST 的拓扑迁移、shot-level split 和从预测通量图派生标量的 consistency score 约束数据泄漏与“只拟合标量”捷径。
- 一句话总结：正文的公开 release 为 `8,794` 个 DIII-D shots、`2,414` 个 MAST shots、约 `133 GB`，而摘要仍写 `9,113/2,416`；naive transfer 的 SSIM 从 DIII-D `0.83` 跌到 MAST `0.10`。这是一套挑战、数据集、基线与评分协议，不是已在反应堆运行的无磁传感器平衡控制器。

## 未入库但需保留的候选

- [Spatiotemporal ionization dynamics in nonthermal copper plasma pumped by femtosecond relativistic laser pulse](https://journals.aps.org/prresearch/accepted/10.1103/sgyf-lrw1)、[Direct observation of saturated heat-flux inhibition by magnetic fields in laser-produced plasmas](https://journals.aps.org/prresearch/accepted/10.1103/2rqf-hq77) 与 [Cone-guided phase-space control of laser-driven proton beams](https://journals.aps.org/pre/accepted/10.1103/d45l-hsgg) 仍高度相关；本轮 APS accepted 页面和 PDF 路径均落到 block / `HTTP 403` HTML，且未检得合法开放作者稿，因此不从摘要扩写笔记。
- [Sub-2-Cycle, Terawatt Pulses via Double-Stage Multi-Pass Cell Compression of an Yb Laser](https://arxiv.org/abs/2609.04989) 实验实现 `12.5 mJ / 6.2 fs / 1 kHz / a_0≈3` 的驱动光，但尚未给出 plasma acceleration 或次级源结果，继续作为激光技术候选。
- [HELIX](https://arxiv.org/abs/2609.04421) 的 differentiable hadron-linac PIC 与 [MGKDB](https://arxiv.org/abs/2609.03132) 的 IMAS-aligned fusion turbulence database 均有方法价值；今天优先选择对 MRX 实验差异有直接解释力的动理学工作，以及带明确跨装置泛化压力测试的 fusion-ML challenge。

## 当日综合总结

- Jiang 将实验室电子–激光 missing-energy 搜寻与 magnetar 极区能损放在互补的 $(m_\chi,\epsilon)$ 区域中；关键边界是平面波、亮度、背景与 polar-gap 假设决定灵敏度，论文没有分析真实探测器接受度和系统误差，也没有报告新数据。
- Son 的贡献是把数值分辨率、真实质量比、碰撞、圆柱几何与“按实验探针采样模拟”接到同一证据链；它显著削弱了用 force-balance deficit 直接推断 anomalous dissipation 的必要性，但没有消除 $\rho_e$ 标度、热力学状态或三维输运问题。
- Nakkina 等把 plasma ML 的评估对象从单装置像素误差扩展为 flux fidelity、LCFS、derived-scalar consistency 与 cross-machine retention；它提供可研究资产和比赛协议，但当前 baseline 表现不能写成 reactor-ready 控制性能。
- 推荐阅读顺序：先读 Son 看模拟—实验分辨率如何改变物理解释，再读 Nakkina 看数据泄漏与跨装置泛化如何被写进评分，最后读 Jiang 区分强场理论灵敏度与真实可观测事件链。
