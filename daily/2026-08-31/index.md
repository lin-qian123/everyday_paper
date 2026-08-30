# 每日论文索引 - 2026-08-31

## 今日概览

- 运行日期：2026-08-31
- 新增论文数：4
- 重点来源：4 篇官方 arXiv 论文页/PDF；其中 `2602.12765` 是 2026-08-27 发布的 v2 修订版。
- 主题分布：kHz LWFA 低发射度与电子衍射、MAST-U 实时神经网络形状控制、CERN 高能重离子电子辐照设施概念设计、XFEL 束流图像 ROI 机器学习诊断。
- 检索范围：复查 Cambridge HPL 最新/accepted manuscripts，并检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex` 最新列表；截至本轮官方列表显示的最新新提交日为 2026-08-28。
- 去重：已按 DOI、规范化标题和历史 daily 核对 `state/processed_articles.json`；12 条已知来源限制重试项未重复空跑。
- PDF/文本：4 份官方 arXiv PDF 均通过 `%PDF-` 文件头、`file` 类型识别、`pdfinfo` 页数/元数据和非空文本提取复核；SHA-256、字节数、页数和 fallback 说明记录于 [`pdf_validation.json`](pdf_validation.json)。本环境未配置 MinerU token，本轮按论文笔记流程使用本地 `pdftotext -layout` fallback，PDF 与提取文本按仓库规则保持本地忽略。

## 论文清单

### 1. Demonstration of ultra-low emittance beams in a kHz laser wakefield accelerator and their application to electron diffraction

- DOI：[10.48550/arXiv.2602.12765](https://doi.org/10.48550/arXiv.2602.12765)
- 发表/修订日期：2026-08-27（v2；原始提交 2026-02-13）
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2602.12765)
- 期刊 / 平台：arXiv preprint v2
- 本地 PDF：`daily/2026-08-31/pdfs/Monzac et al. - 2026 - Ultra-low emittance kHz laser wakefield beams and electron diffraction.pdf`
- 中文笔记：[Monzac et al. - 2026 - Ultra-low emittance kHz laser wakefield beams and electron diffraction.md](notes/Monzac%20et%20al.%20-%202026%20-%20Ultra-low%20emittance%20kHz%20laser%20wakefield%20beams%20and%20electron%20diffraction.md)
- 专业相似度分：`5/5`
- 推荐理由：直接实测 kHz LWFA 低发射度电子束并用于 UED，为激光加速束流的发射度、能散、聚焦和时间展宽提供应用端基线。
- 一句话总结：`2.7 MeV` 发射度测量得到 `124 nm·rad` 归一化发射度；硅纳米膜衍射炮次看到最高约三阶 Bragg 峰，但由 Bragg 反演的该炮次能量约 `500 keV`、电荷约 `25 fC`，尚未实现亚 `10 fs` 时间分辨率。

### 2. Real-time virtual circuits for plasma shape control via neural network emulators: integration and testing in the MAST-U PCS

- DOI：[10.48550/arXiv.2608.26216](https://doi.org/10.48550/arXiv.2608.26216)
- 发表日期：2026-08-26
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.26216)
- 期刊 / 平台：arXiv preprint；submitted to *Fusion Engineering and Design*
- 本地 PDF：`daily/2026-08-31/pdfs/Marshall et al. - 2026 - Real-time neural virtual circuits for MAST-U plasma shape control.pdf`
- 中文笔记：[Marshall et al. - 2026 - Real-time neural virtual circuits for MAST-U plasma shape control.md](notes/Marshall%20et%20al.%20-%202026%20-%20Real-time%20neural%20virtual%20circuits%20for%20MAST-U%20plasma%20shape%20control.md)
- 专业相似度分：`4/5`
- 推荐理由：把神经网络 Jacobian、伪逆 VC、固定内存推理、共享内存通信和真实 MAST-U piggyback 验证连成可复现的实时控制链。
- 一句话总结：8 模型 ensemble 在开发硬件上 p99 端到端延迟约 `0.93 ms`、内存低于 `1.1 GB`，真实炮次 RTVC 请求与参考 emulator 近乎一致；本文重点是软件集成与 commissioning，不是激光/PIC 物理结果。

### 3. A European high-energy heavy-ion facility for electronics irradiation based at CERN: Concept Design Report

- DOI：[10.48550/arXiv.2608.26369](https://doi.org/10.48550/arXiv.2608.26369)
- 发表日期：2026-08-26；报告版本：2026-08-28
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.26369)
- 期刊 / 平台：arXiv preprint；拟提交 CERN Yellow Report
- 本地 PDF：`daily/2026-08-31/pdfs/Cortes Garcia et al. - 2026 - CERN heavy-ion facility concept for electronics irradiation.pdf`
- 中文笔记：[Cortes Garcia et al. - 2026 - CERN heavy-ion facility concept for electronics irradiation.md](notes/Cortes%20Garcia%20et%20al.%20-%202026%20-%20CERN%20heavy-ion%20facility%20concept%20for%20electronics%20irradiation.md)
- 专业相似度分：`4/5`
- 推荐理由：系统给出高能重离子电子辐照的 LET、穿透、均匀化、束流监测、测试站、interlock、屏蔽、资源和风险接口，可作为激光束应用链的系统工程对照。
- 一句话总结：HEARTS@LEIR 概念基线目标为 `20–100 MeV/nucleon`、`0.4–75 MeV·cm²·mg⁻¹` 和约 `1900 h/year` 用户时间；但这是未经最终审查的概念设计，`2034` commissioning、`2035` operation 和 `18.3 MCHF` 均不是已建成能力。

### 4. Machine Learning Based ROI Segmentation for Beam Imaging Diagnostics at Accelerators

- DOI：[10.48550/arXiv.2608.26826](https://doi.org/10.48550/arXiv.2608.26826)
- 发表日期：2026-08-27
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2608.26826)
- 期刊 / 平台：arXiv preprint；prepared for submission to JINST
- 本地 PDF：`daily/2026-08-31/pdfs/Chandratreya et al. - 2026 - Machine learning ROI segmentation for beam imaging diagnostics.pdf`
- 中文笔记：[Chandratreya et al. - 2026 - Machine learning ROI segmentation for beam imaging diagnostics.md](notes/Chandratreya%20et%20al.%20-%202026%20-%20Machine%20learning%20ROI%20segmentation%20for%20beam%20imaging%20diagnostics.md)
- 专业相似度分：`4/5`
- 推荐理由：为复杂束流图像提供 single/multiclass U-Net 与 autoencoder 对照，并把 ROI 分割接入 XFEL 原型在线服务器。
- 一句话总结：single-class U-Net 在合成 held-out 数据上 IoU `0.9625`、accuracy `0.9946`，multiclass U-Net 可分离 faint/bright twin-bunch；模型主要用合成数据训练，真实 XFEL 图像验证仍受 domain gap 限制。

## 当日综合总结

- 共同趋势：本轮从上游激光加速束流（低发射度 LWFA）延伸到控制软件、重离子辐照设施和屏式束流诊断，显示“可用应用束流”需要源、输运、图像/剂量读出与安全系统共同闭环。
- 实验与设计边界：Monzac 是低能 LWFA/UED 实验；Marshall 的真实 MAST-U 部分主要是 RTVC piggyback commissioning；CERN 文档是概念设计；Chandratreya 的主要精度指标来自合成数据，真实图像用于泛化与原型部署。
- 值得跟进的问题：把 kHz LWFA 束流的同时能谱/发射度/到达时间读出补齐；为激光电子/离子束屏式诊断建立真实 PSF、散射、饱和和背景的训练域；评估重离子设施中的均匀化、spill 时间结构和屏蔽假设能否迁移到激光驱动束线。
- 对当前研究最值得优先阅读的论文：先读 Monzac 建立应用端电子束品质基线，再读 Chandratreya 设计图像诊断链；CERN 报告用于辐照设施工程和安全边界对照，Marshall 论文用于 surrogate 控制系统实现方法。
