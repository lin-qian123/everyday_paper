# 每日论文索引 - 2026-09-10

## 今日概览

- 运行日期：2026-09-10
- 新增论文数：5
- 正式来源优先：补入 2026-09-08 接收的 PRL pair-plasma 论文和 2026-09-03 正式发表的 PRX Intelligence ICF-ML 论文；两者本地全文均为对应 arXiv 作者预印本，未冒充 APS 排版版。
- 预印本增量：官方 arXiv 当前批次补入 AWAKE 十米放电源实验、linear Breit–Wheeler 正电子后向压缩 3D QED-PIC 方案和 relativistic laser channel 磁岛二维 PIC 标度。
- 主题分布：强非线性波–对等离子体反射、ICF 非局域热流 ML closure、长尺度 proton-driven PWFA plasma source、强场 QED pair observable、激光通道自生磁结构。
- 检索范围：检查 APS PRL / PRResearch / PRE / PRX Intelligence accepted 与 recent 页面、Cambridge HPLSE accepted / latest、Nature 与 IOP 定向结果、官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.optics`、`nucl-ex`、`hep-ph` 近期 Atom 记录，并定向检索 laser–plasma、PIC、strong-field QED、γ / 光核 / 中子 / 同位素、诊断、radiation protection 与 plasma ML。
- 去重：按正式 DOI / arXiv identifier、规范化标题、历史 daily、重试队列、摘要与物理场景核对 `state/processed_articles.json`。5 篇均未进入 333 条完成台账；Luo 作者稿只在 2026-04-08/09 blocked-day 索引中出现过，未下载、未写笔记、未入完成台账，本轮借正式发表元数据与合法作者稿首次成功入库。
- PDF / 正文：5 份官方 arXiv 作者稿通过 `%PDF-`、`file`、`pdfinfo` 页数、SHA-256 和非空 `pdftotext -layout`。5 篇均使用当前可用 `MINERU_API_KEY` 完成 Markdown / 图件提取；共选取 18 张关键图并逐张解码查看。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Complete reflection of nonlinear electromagnetic waves in underdense pair plasmas enabled by dynamically formed Bragg-like structures

- 正式 DOI：[10.1103/g27z-2kd3](https://doi.org/10.1103/g27z-2kd3)
- PRL 接收日期：2026-09-08
- 正式来源：[APS accepted paper](https://journals.aps.org/prl/accepted/10.1103/g27z-2kd3)
- 作者稿：[arXiv:2509.06230](https://arxiv.org/abs/2509.06230)
- 期刊 / 平台：Physical Review Letters accepted paper；本地全文为作者预印本
- 本地 PDF：`daily/2026-09-10/pdfs/Tangtartharakul et al. - 2026 - Complete reflection in underdense pair plasma.pdf`
- 中文笔记：[Tangtartharakul et al. - 2026 - Complete reflection in underdense pair plasma.md](notes/Tangtartharakul%20et%20al.%20-%202026%20-%20Complete%20reflection%20in%20underdense%20pair%20plasma.md)
- 来源影响力分：10/10
- 专业相似度分：9/10
- 推荐理由：给出一个与 electron–ion RIT 相反的 pair-plasma 机制，并用压缩解析、移动 Bragg grating、reflection-front 动量平衡和 EPOCH 扫描闭合证据链。
- 一句话总结：作者的 1D3V PIC 显示 $a_0=2.5$ 的波可让每物种仅 $0.0125n_{cr}$ 的冷 pair plasma 形成以约 $0.94c$ 移动的 plug 并完全反射；低密极限阈值约 $n_0/n_{cr}>1/(32a_0^2)$。这是理论/PIC 预测，不是实验室对等离子体反射或 FRB 观测。

### 2. Resolution-Robust Machine Learning Heat Flux Closure for Inertial Confinement Fusion Plasmas

- DOI：[10.1103/9l4n-mnz6](https://doi.org/10.1103/9l4n-mnz6)
- 正式发表日期：2026-09-03
- 正式来源：[PRX Intelligence 论文页](https://journals.aps.org/prxintelligence/abstract/10.1103/9l4n-mnz6)
- 作者稿：[arXiv:2604.03439](https://arxiv.org/abs/2604.03439)
- 期刊 / 平台：PRX Intelligence 1, 013017 (2026)；本地全文为作者预印本
- 本地 PDF：`daily/2026-09-10/pdfs/Luo et al. - 2026 - Resolution-robust ML heat flux closure.pdf`
- 中文笔记：[Luo et al. - 2026 - Resolution-robust ML heat flux closure.md](notes/Luo%20et%20al.%20-%202026%20-%20Resolution-robust%20ML%20heat%20flux%20closure.md)
- 来源影响力分：9/10
- 专业相似度分：10/10
- 推荐理由：不是只回归 kinetic 数据，而是把 PIC 训练的 Fourier neural operator 作为 $T_e\mapsto\partial_xq$ 闭合嵌入隐式电子能量求解器，并显式测试粗训练网格到细部署网格。
- 一句话总结：作者在一维固定密度 OSIRIS 热点与 Epperlein–Short 测试中报告多数温度误差低于 `1%`，单 CPU 在线求解约 `20 min` 对 SNB `800 min`；但热点训练不能可靠外推 ES 分布，`40×` 不含 PIC 数据/训练成本，也不是 ICF hydro 整体加速。

### 3. Demonstration of a 10-metre-long discharge plasma source for plasma wakefield acceleration

- DOI：[10.48550/arXiv.2609.08551](https://doi.org/10.48550/arXiv.2609.08551)
- arXiv v1：2026-09-08
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.08551)
- 期刊 / 平台：arXiv 预印本；AWAKE 实验
- 本地 PDF：`daily/2026-09-10/pdfs/Amoedo et al. - 2026 - 10-metre discharge plasma source for AWAKE.pdf`
- 中文笔记：[Amoedo et al. - 2026 - 10-metre discharge plasma source for AWAKE.md](notes/Amoedo%20et%20al.%20-%202026%20-%2010-metre%20discharge%20plasma%20source%20for%20AWAKE.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：把十米 noble-gas pulsed-DC source 的干涉密度、长期放电稳定性与 `400 GeV` 质子束 self-modulation 频率接到同一实验验证链。
- 一句话总结：He/Ar/Xe 峰值密度约为 $0.36/0.87/1.78\times10^{15}\,\mathrm{cm^{-3}}$；Ar 48 发 modulation frequency 为 `235.1±1.5 GHz`，且超过 20,000 次放电后密度保持在不确定度内。`0.63%` 是频率散布，不是全长密度均匀性；本文没有 witness-electron acceleration。

### 4. Self-organized positron reorienting and pinching mechanism for the experimental detection of the linear Breit-Wheeler process

- DOI：[10.48550/arXiv.2609.07584](https://doi.org/10.48550/arXiv.2609.07584)
- arXiv v1：2026-09-07
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.07584)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-10/pdfs/He et al. - 2026 - Self-organized positron reorienting for linear Breit-Wheeler.pdf`
- 中文笔记：[He et al. - 2026 - Self-organized positron reorienting for linear Breit-Wheeler.md](notes/He%20et%20al.%20-%202026%20-%20Self-organized%20positron%20reorienting%20for%20linear%20Breit-Wheeler.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：把 LBW 总产额问题改写成角相空间工程，用 relativistically transparent channel 的自生 $B_\phi$ 将正电子转向后方并压缩，再用双层靶折中光子密度与通道形成。
- 一句话总结：作者的 3D3V EPOCH QED-PIC 给出均匀 $20n_c$ 靶约 $6.2\times10^7$ 对、双层靶约 $5.5\times10^7$ 对，并预测后向 `15°` 内约 $10^6\,\mathrm{MeV^{-1}\,sr^{-1}}$；没有实验、完整材料背景或探测器响应，题名中的 detection 是方案目标。

### 5. Magnetic island structures in relativistic laser-driven plasma channels

- DOI：[10.48550/arXiv.2609.06562](https://doi.org/10.48550/arXiv.2609.06562)
- arXiv v1：2026-09-06
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.06562)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-10/pdfs/Cai et al. - 2026 - Magnetic islands in relativistic laser-driven plasma channels.pdf`
- 中文笔记：[Cai et al. - 2026 - Magnetic islands in relativistic laser-driven plasma channels.md](notes/Cai%20et%20al.%20-%202026%20-%20Magnetic%20islands%20in%20relativistic%20laser-driven%20plasma%20channels.md)
- 来源影响力分：7/10
- 专业相似度分：9/10
- 推荐理由：把 longitudinal channel current 和 wavefront transverse current 产生的两类 $B_z$ 分开，给出 $a_0$–$n_e$ 区域图及磁岛横纵尺度相似标度。
- 一句话总结：作者的二维 EPOCH 扫描得到 $H\propto(a_0/\hat n_e)^{1/4}$、$L\propto(a_0/\hat n_e)^{1/2}$，并以穿透、排空和有限靶长区分 NPT/TSC/DMI/LMI/TCH；这些是带拟合系数的二维模拟/解析结构，未计算电子束、光子或离子源性能。

## 未入库但需保留的候选

- [First experimental evidence of helicon current drive](https://journals.aps.org/prl/accepted/10.1103/mbn4-fd4v) 是 2026-09-08 接收的 DIII-D 正式实验增量，证明价值高；本轮 5 个名额优先覆盖激光/强场/PIC 主线，保留给后续正式全文可用时处理，不能从 accepted abstract 直接扩写完整笔记。
- [Spatiotemporal ionization dynamics in nonthermal copper plasma pumped by femtosecond relativistic laser pulse](https://journals.aps.org/prresearch/accepted/10.1103/sgyf-lrw1)、[Direct observation of saturated heat-flux inhibition by magnetic fields in laser-produced plasmas](https://journals.aps.org/prresearch/accepted/10.1103/2rqf-hq77) 与 [Cone-guided phase-space control of laser-driven proton beams](https://journals.aps.org/pre/accepted/10.1103/d45l-hsgg) 仍高度相关；2026-09-10 用项目安全下载器复查 accepted / DOI 路径，三者仍全部返回 `HTTP 403` HTML，且未检得合法开放作者稿，因此继续只保留候选元数据。
- PRL recent/accepted 与 HPLSE featured 中的 `Achieving High Efficiency And Enhanced Beam Quality In Laser Wakefield Acceleration`、LWFA–FEL start-to-end、helical electron bunch、SINAPSE 等高相关条目已在历史台账，按正式 DOI、标题和场景跳过，不因页面再次出现而重复处理。

## 当日综合总结

- Tangtartharakul 的关键反转是 pair-plasma mass symmetry 消除 charge-separation restoring field；波压缩、微弱反射诱发 pinching、移动 Bragg grating 和反射前沿反馈共同导致欠密 plasma 变得不透明。它是 1D 理论/PIC，不是实验或 FRB 直接解释。
- Luo 证明 operator discretization transfer 可以服务真实求解器接口，但也用热点→ES 的失败说明 resolution robustness 不等于 physics OOD generalization。最有价值的验证对象是能量方程消费的 $\partial_xq$ 和温度演化，不是单个静态网络指标。
- Amoedo 是今天唯一新增的直接 laser/plasma-device 实验链：10 m DPS + interferometry + proton self-modulation。它验证源与驱动束相容性，却尚未闭合全长 `0.25%` 均匀度目标和 witness-electron energy gain。
- He 与 Cai 都是作者 PIC 结果：前者预测 LBW 正电子角相空间重排，后者预测二维激光通道磁拓扑与相似标度。两者都不能升级为已经观测的 pair signal、实验 magnetic island 或次级源产额。
- 推荐阅读顺序：先读 Amoedo 看实验 observable 链，再读 Luo 看 kinetic-to-fluid closure 与 OOD 边界；随后读 Tangtartharakul 的反直觉 transparency 机制，最后把 He/Cai 当作强场与通道物理的候选设计图，而非已验证应用。
