# 每日论文索引 - 2026-10-01

## 今日概览

- 运行日期：2026-10-01
- 新增论文数：5（4 篇为 2026-09-29 投稿、2026-09-30 官方公告批次；1 篇为上一批次补充收录的中子诊断预印本）
- 最新性：核对官方 arXiv Atom/API 的目标分类，最新可用增量为 2026-09-29 投稿批次；同时检查 Crossref 2026-09-29 至 10-01 正式元数据，没有找到主题更强、可验证全文且未重复的正式论文。
- 主题分布：直接驱动 ICF 的宽带 CBET 抑制实验；可调通道 LWFA 再相位实验；偏振依赖的 betatron X 射线/PIC；KSTAR 传感器失效下扩散先验重建；便携式 `4π` 中子散射相机。
- 去重：按 DOI/arXiv identifier、规范化标题、393 条完成台账、20 条重试队列、历史 `daily/`、摘要和物理场景检查；5 篇均为独立作品。
- PDF / 正文：5 份官方 arXiv PDF 均通过 `%PDF-`、`file`、`pdfinfo`、SHA-256 与非空 `pdftotext -layout`；共 20 个选定页面完成渲染和人工查看。
- 重试：20 条既有来源受限记录不变；未重复空跑 Elsevier、Nature、IOP/Radware 和 APS 阻塞项。
- 覆盖边界：多来源搜索层返回 0 条可用结果，后续使用官方 arXiv、Crossref 与单篇全文；这是定向增量筛选，不宣称穷尽全部期刊或数据库。

## 论文清单

### 1. Experimental demonstration of broadband-laser suppression of cross-beam energy transfer

- 标识符：[arXiv:2609.36528](https://arxiv.org/abs/2609.36528)；归档 DOI `10.48550/arXiv.2609.36528`
- 提交日期：2026-09-29（2026-09-30 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-01/pdfs/Xu et al. - 2026 - Broadband laser CBET suppression.pdf`
- 中文笔记：[Xu et al. - 2026 - Broadband laser CBET suppression.md](notes/Xu%20et%20al.%20-%202026%20-%20Broadband%20laser%20CBET%20suppression.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：以最高约 `550 J` 的双束真实实验把宽带抑制从单束 LPI 推进到 CBET 增强返光，并用非对称几何分离 SBS 与镜面反射方向。
- 一句话总结：`0.6%` 宽带把对称总返光从 `7.57%` 降到 `4.64%`，非对称 SBS 主导通道从 `3.75%` 降到 `0.46%`；CBET 份额的解释仍依赖固定背景的二维射线模型。

### 2. Electron Rephasing in a Truncated Tunable Plasma Channel

- 标识符：[arXiv:2609.36964](https://arxiv.org/abs/2609.36964)；归档 DOI `10.48550/arXiv.2609.36964`
- 提交日期：2026-09-29（2026-09-30 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-01/pdfs/Mohanty et al. - 2026 - Electron rephasing in plasma channel.pdf`
- 中文笔记：[Mohanty et al. - 2026 - Electron rephasing in plasma channel.md](notes/Mohanty%20et%20al.%20-%202026%20-%20Electron%20rephasing%20in%20plasma%20channel.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：真实测量把有限通道出口变成可调相位控制元件，并用 106 发数据量化 GeV 谱的重复性。
- 一句话总结：`12 mm` 通道在 `15 mm` 气靶中得到 `(1450±42) MeV` 平均截止与 `223±20 pC` 高能电荷；“气泡收缩—再相位”机制来自 EPOCH/FLASH/FBPIC 链，不是直接成像。

### 3. Laser-Polarization Dependence of Betatron X-Ray Production and Angular Collection in Laser-Wakefield Acceleration

- 标识符：[arXiv:2609.37228](https://arxiv.org/abs/2609.37228)；归档 DOI `10.48550/arXiv.2609.37228`
- 提交日期：2026-09-29（2026-09-30 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-01/pdfs/Berceanu et al. - 2026 - Polarization dependent betatron x rays.pdf`
- 中文笔记：[Berceanu et al. - 2026 - Polarization dependent betatron x rays.md](notes/Berceanu%20et%20al.%20-%202026%20-%20Polarization%20dependent%20betatron%20x%20rays.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把偏振、传播阶段、X 射线角接受度和下游电子输运放在同一模拟链中，直接揭示“总产额”和“可收集产额”的差异。
- 一句话总结：后期线偏振未选角 `20–60 keV` 产额可达圆偏振的 `1.91` 倍，但 `±5 mrad` 内近乎相等；全程 PIC/ImpactX 结果，未做成像或剂量实验。

### 4. Diffusion prior for KSTAR equilibrium reconstruction under sensor dropout

- 标识符：[arXiv:2609.36536](https://arxiv.org/abs/2609.36536)；归档 DOI `10.48550/arXiv.2609.36536`
- 提交日期：2026-09-29（2026-09-30 官方公告批次）
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-10-01/pdfs/Nam and Seo - 2026 - KSTAR diffusion prior reconstruction.pdf`
- 中文笔记：[Nam and Seo - 2026 - KSTAR diffusion prior reconstruction.md](notes/Nam%20and%20Seo%20-%202026%20-%20KSTAR%20diffusion%20prior%20reconstruction.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：用真实 KSTAR 信号和最多 `90%` 随机通道遮挡检验物理前向算子约束的生成式先验，并主动报告先验主导与不确定度失准。
- 一句话总结：扩散法的 `Jφ` 标签距离保持 `3.22–4.07%`，同 mask LIUQE 在 `90%` dropout 达 `11.89%`；标签本身是全传感器 LIUQE，单帧约 `1.1 s`，不是实时真值验证。

### 5. A portable neutron scatter camera with isotropic sensitivity

- 标识符：[arXiv:2609.36342](https://arxiv.org/abs/2609.36342)；归档 DOI `10.48550/arXiv.2609.36342`
- 提交日期：2026-09-28（上一公告批次补充收录）
- 期刊 / 平台：arXiv 预印本（标注 submitted to Elsevier）
- 本地 PDF：`daily/2026-10-01/pdfs/Yoon et al. - 2026 - Portable neutron scatter camera.pdf`
- 中文笔记：[Yoon et al. - 2026 - Portable neutron scatter camera.md](notes/Yoon%20et%20al.%20-%202026%20-%20Portable%20neutron%20scatter%20camera.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：对核诊断、装置本底和屏蔽选址有直接方法学价值，并以 Cf-252 完成全 `4π` 定位与远场弱源验证。
- 一句话总结：14 个近场方向的热点约在 `3°` 内重建，远场 `0.003 n cm⁻² s⁻¹` 也可定位；ESS 事件率与高能响应仍是模拟外推，不是现场测量。

## 未入库候选与取舍

- `arXiv:2609.37609` 的 PHASE 多工况 MHD 神经算子与主题相关，但本轮优先保留真实 KSTAR 信号上的 dropout benchmark；PHASE 目前仍是二维不可压 MHD 数值数据验证。
- `arXiv:2609.37856` 使用 Parker Solar Probe、Solar Orbiter 与 WIND 研究太阳风湍流，数据质量高但偏空间等离子体，距离激光/HEDP/核应用主线较远。
- `arXiv:2609.37409` 的超辐射 chorus 全局相锁属于磁层动力学；`arXiv:2609.37257` 的等离子体活性物质发动机偏软凝聚态应用，本轮不收录。
- `arXiv:2609.36533` 的超导加速器慢正电子束为 Geant4 加扩散理论计算，没有激光等离子体源或实测束流，优先级低于本轮直接束流与诊断工作。
- 20 条既有来源受限记录没有新的合法全文线索，继续保留重试状态，不从摘要生成笔记。

## 当日综合总结

- 最强实验增量是昆吾宽带双束 CBET 返光示范和通道出口再相位 LWFA；两者都把关键控制量落到装置测量，但机制分解仍需作者模型。
- betatron 论文提醒应用端不能只报光子总数：滤片、角孔径、传播阶段和电子输运接受度会改变偏振优劣。
- KSTAR 扩散先验在大比例通道遮挡下有明显 benchmark 优势，同时给出两个重要负面结果：全传感器 LIUQE 不是物理真值，扩散样本散布不是可靠误差条。
- 中子相机补齐“源位置—能量—通量”诊断链的一部分，但当前直接校准是 Cf-252；ESS 高能场与多源分解仍需现场部署。
- 推荐阅读顺序：宽带 CBET 实验 → 通道 LWFA 实验 → betatron PIC/输运 → KSTAR dropout 反演 → 中子相机，依次比较直接实验、模型辅助机制、纯模拟设计、数据驱动重建和核诊断标定五种证据层级。
