# 每日论文索引 - 2026-09-08

## 今日概览

- 运行日期：2026-09-08
- 新增论文数：3
- 重点来源：2 篇 High Power Laser Science and Engineering 正式开放 accepted manuscripts，1 篇官方 arXiv 最新预印本。
- 主题分布：LWFA–FEL 的 FBPIC–束线–GENESIS 端到端优化、light-spring 驱动的螺旋 OAM 电子束、阻止本领反馈下的激光 pitcher–catcher 质子–硼聚变。
- 检索范围：检查 HPLSE accepted manuscripts / latest volume、APS PRL / PRResearch / PRE / PRApplied accepted 增量、官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`physics.optics`、`nucl-ex` 和 `hep-ph`，并定向检索 laser–plasma、PIC、strong-field QED、γ / 光核 / 中子 / 同位素、材料辐照、诊断与 radiation protection。官方 arXiv 最新可用批次到 2026-09-04，`2609.04987` 是今天检出的直接相关新增。
- 去重：按 DOI / arXiv identifier、规范化标题、历史 daily、重试队列、摘要与物理场景核对 `state/processed_articles.json`；三篇均未入库。HPLSE 两篇是上一轮已校验全文但因实验论文优先而暂缓的高相关正式稿，本轮没有重复下载旧条目。
- PDF / 正文：3 份官方全文通过 PDF 文件头、`file` 类型、`pdfinfo` 页数 / 元数据、SHA-256 和非空 `pdftotext -layout`。当前环境没有 `MINERU_TOKEN`，因此未声称完成 MinerU 转换；9 个关键 PDF 页面已渲染、解码并人工查看。完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Start-to-end optimization framework for free-electron lasers driven by laser wakefield accelerators

- DOI：[10.1017/hpl.2026.10191](https://doi.org/10.1017/hpl.2026.10191)
- 在线日期：2026-07-30
- 来源：[Cambridge Core 论文页](https://www.cambridge.org/core/product/6C0FD5325CF26134016413B750D7C3CC)
- 期刊 / 平台：High Power Laser Science and Engineering accepted manuscript
- 本地 PDF：`daily/2026-09-08/pdfs/Ge et al. - 2026 - LWFA-driven FEL start-to-end optimization.pdf`
- 中文笔记：[Ge et al. - 2026 - LWFA-driven FEL start-to-end optimization.md](notes/Ge%20et%20al.%20-%202026%20-%20LWFA-driven%20FEL%20start-to-end%20optimization.md)
- 来源影响力分：8/10
- 专业相似度分：10/10
- 推荐理由：把 FBPIC、ELEGANT/OCELOT、GENESIS 和 CMA-ES 接成两阶段闭环，用下游 FEL 输出反向筛选上游 LWFA，而不是只优化等离子体出口束流。
- 一句话总结：作者的 start-to-end 数值最优解给出约 `500 MeV / 34 pC / 0.4%` 电子束与 `13.5 nm / 9 μJ / 3.3 GW` FEL；这些是模拟输出，附录 500-seed 检查还显示约 `5.8 μJ` 均值与 `43%–46%` 波动，不能写成实验装置指标。

### 2. Energetic helical electron-bunch generation driven by a light spring wakefield

- DOI：[10.1017/hpl.2026.10192](https://doi.org/10.1017/hpl.2026.10192)
- 在线日期：2026-07-30
- 来源：[Cambridge Core 论文页](https://www.cambridge.org/core/product/6A6B7447A1D44D743B4D93CD64E0A57E)
- 期刊 / 平台：High Power Laser Science and Engineering accepted manuscript
- 本地 PDF：`daily/2026-09-08/pdfs/Liu et al. - 2026 - Light-spring helical electron bunch.pdf`
- 中文笔记：[Liu et al. - 2026 - Light-spring helical electron bunch.md](notes/Liu%20et%20al.%20-%202026%20-%20Light-spring%20helical%20electron%20bunch.md)
- 来源影响力分：8/10
- 专业相似度分：9/10
- 推荐理由：用 3D EPOCH 展示由 7 个频率—拓扑荷相关 LG 子束合成的 light spring 如何把光学手性编码进 helical bubble、电子轨迹与 OAM。
- 一句话总结：论文报告模拟束团约 `9.53 nC`、最高 `103 MeV`、OAM 转换效率 `12.78%`；单组理想 PIC 尚未证明实验可实现性、长距离束运或 OAM betatron 辐射性能。

### 3. Impact of ion-beam stopping power on proton-boron fusion yield in the pitcher-catcher scheme driven by ultra-intense laser

- DOI：[10.48550/arXiv.2609.04987](https://doi.org/10.48550/arXiv.2609.04987)
- arXiv v1：2026-09-04；稿件首页日期：2026-09-07
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.04987)
- 期刊 / 平台：arXiv 预印本
- 本地 PDF：`daily/2026-09-08/pdfs/Hua et al. - 2026 - Stopping power in proton-boron pitcher-catcher fusion.pdf`
- 中文笔记：[Hua et al. - 2026 - Stopping power in proton-boron pitcher-catcher fusion.md](notes/Hua%20et%20al.%20-%202026%20-%20Stopping%20power%20in%20proton-boron%20pitcher-catcher%20fusion.md)
- 来源影响力分：7/10
- 专业相似度分：10/10
- 推荐理由：直接把 laser-driven proton beam、boron catcher、集体阻止本领、电子温度反馈和 $p{}^{11}\mathrm B$ 反应率接成理论—PIC—MC 链，紧贴激光束流核应用主线。
- 一句话总结：在论文给定 1D 密度/厚度与 `25%` 能散下，考虑 stopping feedback 后最优入射能量从 `672 keV` 移到约 `900 keV`；没有新的直接 $\alpha$ 实验、绝对单发产额或净能量增益。

## 未入库但需保留的候选

- [Spatiotemporal ionization dynamics in nonthermal copper plasma pumped by femtosecond relativistic laser pulse](https://journals.aps.org/prresearch/accepted/10.1103/sgyf-lrw1)、[Direct observation of saturated heat-flux inhibition by magnetic fields in laser-produced plasmas](https://journals.aps.org/prresearch/accepted/10.1103/2rqf-hq77) 和 [Cone-guided phase-space control of laser-driven proton beams](https://journals.aps.org/pre/accepted/10.1103/d45l-hsgg) 仍高度相关；本轮直接重试 APS PDF，三者均为 `HTTP 403` HTML，且未检得合法开放作者稿，因此不从摘要扩写笔记。
- [Sub-2-Cycle, Terawatt Pulses via Double-Stage Multi-Pass Cell Compression of an Yb Laser](https://arxiv.org/abs/2609.04989) 是同批次 `kHz / 1.4 TW / 6.2 fs` 激光技术新稿，面向未来 LWFA，但尚未给出等离子体加速结果，本轮优先核应用与直接 PIC/FEL 主题。
- `arXiv:2609.04421` 的 HELIX 将 differentiable optimization 接入 hadron-linac PIC，方法价值较高，但与本仓库激光—等离子体主线较间接，暂不挤占当日三篇额度。

## 当日综合总结

- Ge 的贡献是优化层级：先用便宜的 gain-length proxy 扩大搜索，再用含空间电荷和随机种子的辐射能量精化；最关键边界是它仍是作者运行的数值链，并且主结果与 500-seed 附录的 `9/5.8 μJ` 口径需要进一步解释。
- Liu 的贡献是结构编码：LS 的非轴对称场同时提供纵向加速、径向聚焦与方位角加速；但 `103 MeV / 9.53 nC / 12.78%` 来自单组 3D PIC，应用到辐射源还缺光子端计算和实验容差。
- Hua 的贡献是把“截面峰值”改写为“沿减速路径积分截面”：对足够厚密的 catcher，`900 keV` 质子先穿过宽平台再扫过 `672 keV` 共振，前沿加热又减弱尾部 stopping；这不是普适最优能量，更不是实验产额或净增益。
- 推荐阅读顺序：先读 Hua 看 beam–catcher 核反应反馈，再读 Ge 理解如何把多代码链变成可优化的端到端系统，最后读 Liu 看结构光如何新增电子束 OAM 自由度。
