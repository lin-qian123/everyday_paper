# 每日论文索引 - 2026-09-06

## 今日概览

- 运行日期：2026-09-06
- 新增论文数：3
- 重点来源：1 篇 2026-09-03 正式发表的 Physical Review Letters 开放论文、1 篇 2026-09-05 被 Physical Review Research 接收且有对应开放作者预印本的论文、1 篇官方 arXiv 预印本。
- 主题分布：LWFA 耗尽长度后的高通量 betatron X 射线、低电荷 neutron–γ 深度学习判别与可解释性、锥形通道 LWFA 的 2D3V WarpX 参数扫描。
- 检索范围：检查 APS Physical Review Letters / Physical Review Research recent 与 accepted 增量；检查官方 arXiv physics.plasm-ph、physics.acc-ph、physics.comp-ph、physics.ins-det 及相关交叉列表；定向检查 laser–plasma、PIC、ML、strong-field QED、γ / 光核 / 中子、诊断与 radiation protection 关键词。
- 去重：按 DOI / arXiv identifier、规范化标题、历史 daily、重试队列、摘要和物理场景核对 `state/processed_articles.json`；3 篇均未入库。
- PDF / 正文：3 份全文均通过 PDF 文件头、`file` 类型、`pdfinfo` 页数 / 元数据、SHA-256、非空 `pdftotext -layout` 和 MinerU Markdown 转换；完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. High-Flux X-Ray Emission due to Injection into a Laser-Wakefield Accelerator beyond Its Depletion Length

- DOI：[10.1103/krsl-322s](https://doi.org/10.1103/krsl-322s)
- 接收 / 发表日期：2026-07-09 / 2026-09-03
- 来源：[APS 论文页](https://journals.aps.org/prl/abstract/10.1103/krsl-322s)
- 期刊 / 平台：Physical Review Letters 137, 105001 (2026)
- 本地 PDF：daily/2026-09-06/pdfs/Wood et al. - 2026 - High-flux X-ray emission beyond LWFA depletion length.pdf
- 中文笔记：[Wood et al. - 2026 - High-flux X-ray emission beyond LWFA depletion length.md](notes/Wood%20et%20al.%20-%202026%20-%20High-flux%20X-ray%20emission%20beyond%20LWFA%20depletion%20length.md)
- 来源影响力分：10/10
- 专业相似度分：10/10
- 推荐理由：用长度扫描把电子谱、绝对电荷和 betatron X 射线联系起来，直接展示超过 pump-depletion length 后第二注入带来的谱通量增益，并用 FBPIC 解释激光压缩和 bubble 扩张。
- 一句话总结：110 TW 激光驱动的第一束团超过 2 GeV，而耗尽长度后出现的 140–360 pC、约 0.7 GeV 第二束团产生 $>5\times10^{10}$ photons/shot 和 $(7.0\pm0.8)\times10^4$ photons/mrad²/0.1%BW；$r_\beta$ 与峰值亮度含反演 / 模拟假设。

### 2. SINAPSE: A lightweight deep learning framework for accurate and explainable neutron-γ discrimination

- 正式 DOI：[10.1103/qd3v-7j5p](https://doi.org/10.1103/qd3v-7j5p)
- 接收日期：2026-09-05
- 来源：[APS accepted papers 页面](https://journals.aps.org/prresearch/accepted/10.1103/qd3v-7j5p)
- 期刊 / 平台：Physical Review Research accepted paper；本地全文为对应 [arXiv:2605.13627v2](https://arxiv.org/abs/2605.13627v2) author preprint
- 本地 PDF：daily/2026-09-06/pdfs/Carreau et al. - 2026 - SINAPSE neutron-gamma discrimination.pdf
- 中文笔记：[Carreau et al. - 2026 - SINAPSE neutron-gamma discrimination.md](notes/Carreau%20et%20al.%20-%202026%20-%20SINAPSE%20neutron-gamma%20discrimination.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：将大规模真实 EJ-309 波形、低 SNR augmentation、共享 denoising encoder、概率校准、SHAP 和 ONNX / nptool 部署放进同一可审计链，直接关联中子诊断与 radiation protection。
- 一句话总结：校准 FC 模型在 78,596 条独立 prompt-γ 波形上达到 92.3% accuracy；低电荷区 99.9% 置信下覆盖 63.1% 而 graphical cuts 为 55.5%，但 0.981 precision / recall 主要相对 PSD 标签，尚不能当作跨仪器真值误差率。

### 3. Dependence of self-injected bunch parameters on the plasma density gradient and laser pulse amplitude at LWFA in a conical plasma channel

- DOI：[10.48550/arXiv.2609.03479](https://doi.org/10.48550/arXiv.2609.03479)
- 提交日期：2026-09-03
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.03479)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：daily/2026-09-06/pdfs/Bondar et al. - 2026 - Self-injected LWFA bunches in a conical plasma channel.pdf
- 中文笔记：[Bondar et al. - 2026 - Self-injected LWFA bunches in a conical plasma channel.md](notes/Bondar%20et%20al.%20-%202026%20-%20Self-injected%20LWFA%20bunches%20in%20a%20conical%20plasma%20channel.md)
- 来源影响力分：5/10
- 专业相似度分：9/10
- 推荐理由：给出 conical-channel geometry、密度梯度和 $a_0$ 的显式有限扫描，可作为 WarpX 自注入 / taper input design 的候选参数图谱，同时暴露过强梯度破坏 bubble 的上限。
- 一句话总结：作者的 2D3V WarpX 扫描在 $a_0=3.6$、出口 $3n_e$ 时得到 $p_z=111.9m_ec$、$Q=32.1\ \mu$C/m 和 $\epsilon_x=1.6\times10^{-2}$ mm·mrad；$Q$ 是二维线电荷，且本轮没有输入卡、收敛证据或本地复现。

## 未入库但需保留的候选

- [Spatiotemporal ionization dynamics in nonthermal copper plasma pumped by femtosecond relativistic laser pulse](https://journals.aps.org/prresearch/accepted/10.1103/sgyf-lrw1)（DOI：10.1103/sgyf-lrw1）于 2026-09-05 被 Physical Review Research 接收，主题与强激光驱动非热 HED plasma 高度相关；本轮只找到摘要，未找到可合法获取的开放全文，因此没有从摘要扩写笔记或写入台账。
- Physical Review Research accepted paper `10.1103/2rqf-hq77` 的 heat-flux inhibition 与 laser plasma 相关，但本轮同样没有找到可合法获取全文，仅保留元数据候选。
- arXiv:2609.03822 的 Geant4 rare-event shielding importance sampling 与辐射防护相关，arXiv:2609.03768 的高阶 mixed-derivative PINN 与计算方法相关；相较今日三篇，它们对当前 laser-driven source / neutron diagnostic / PIC 证据链的直接增量较低，留待后续去重检索。

## 当日综合总结

- Wood 和 Bondar 都涉及 LWFA self-injection，但证据等级不同：Wood 是带电子 / X 射线诊断的实验并用 FBPIC 支撑机制；Bondar 是单一读取时刻的 2D3V WarpX 扫描。前者的峰值亮度仍含模拟脉宽，后者的 μC/m 不能转成实验束团电荷。
- SINAPSE 展示了低电荷 neutron–γ 判别中比分类头更关键的两点：概率需要 beta calibration，弱信号允许 abstention；VBLL 在该数据集上既未改善 MCE，又妨碍 ONNX export。
- 三篇分别覆盖光源、诊断算法和电子束数值设计，但没有任何一篇闭合“激光加速束流 → 转换靶 γ 谱 → 光核 / 中子 / 活化产额 → 剂量 / shielding”的完整实验链。
- 推荐阅读顺序：先读 Wood 掌握耗尽长度后第二注入的实验事实与模型边界，再读 Carreau 建立 neutron–γ 置信度 / 校准框架，最后读 Bondar，把锥形通道参数当作需要三维收敛验证的候选设计而非最终结论。
