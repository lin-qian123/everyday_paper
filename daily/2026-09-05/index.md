# 每日论文索引 - 2026-09-05

## 今日概览

- 运行日期：2026-09-05
- 新增论文数：4
- 重点来源：1 篇 2026-09-04 被 Physical Review E 接收的理论论文（本地全文为对应 arXiv v2 author preprint），以及 3 篇 2026-09-04 新发布的官方 arXiv 预印本。
- 主题分布：EPOCH quasi-cylindrical X-dispersionless PIC、GTC hybrid spectral gyrokinetic PIF、standing-wave cavity 中的 QED vacuum nonlinearity，以及密度梯度中 SRS/SBS 的多维 Noether conservation laws。
- 检索范围：检查 APS Physical Review E accepted papers 与 Crossref 2026-09-04 更新；检查官方 arXiv physics.plasm-ph、physics.acc-ph、physics.comp-ph、hep-ph、quant-ph 与相关交叉列表的 2026-09-04 新发布；定向检查 laser–plasma、PIC、gyrokinetics、strong-field/QED、γ/光核/中子和诊断关键词。
- 去重：按 DOI / arXiv identifier、规范化标题、历史 daily、重试队列、摘要和物理场景核对 state/processed_articles.json；4 篇均未入库。
- PDF/正文：4 份全文均通过 PDF 文件头、file 类型、pdfinfo 页数/元数据、SHA-256、非空 pdftotext -layout 和 MinerU Markdown 转换；完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. X-dispersionless solver for electromagnetic and axion fields in a cylindrical particle-in-cell code

- DOI：[10.48550/arXiv.2609.03550](https://doi.org/10.48550/arXiv.2609.03550)
- 提交日期：2026-09-03；arXiv 新发布：2026-09-04
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.03550)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：daily/2026-09-05/pdfs/An et al. - 2026 - X-dispersionless cylindrical PIC solver for electromagnetic and axion fields.pdf
- 中文笔记：[An et al. - 2026 - X-dispersionless cylindrical PIC solver for electromagnetic and axion fields.md](notes/An%20et%20al.%20-%202026%20-%20X-dispersionless%20cylindrical%20PIC%20solver%20for%20electromagnetic%20and%20axion%20fields.md)
- 专业相似度分：5/5
- 推荐理由：把 direction-splitting 无色散推进推广到 EPOCH quasi-cylindrical 模式，并用 vacuum、LWFA 与两色激光 axion phase-matching 三类 benchmark 检查累计相位误差。
- 一句话总结：在 $c\Delta t=\Delta x$ 下，横向输运变量沿轴向每步精确移动一格；作者报告粗网格群速度误差 $2.61\times10^{-4}$ 接近有限腰斑理论值 $2.53\times10^{-4}$，但本轮未做源码审计、编译或本地复现。

### 2. Minute-Scale High-Fidelity Gyrokinetic Simulations with Portability from Laptop to Supercomputer

- DOI：[10.48550/arXiv.2609.03354](https://doi.org/10.48550/arXiv.2609.03354)
- 提交日期：2026-09-03；稿件日期 / arXiv 新发布：2026-09-04
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.03354)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：daily/2026-09-05/pdfs/Bao et al. - 2026 - Minute-scale high-fidelity gyrokinetic simulations.pdf
- 中文笔记：[Bao et al. - 2026 - Minute-scale high-fidelity gyrokinetic simulations.md](notes/Bao%20et%20al.%20-%202026%20-%20Minute-scale%20high-fidelity%20gyrokinetic%20simulations.md)
- 专业相似度分：4.5/5
- 推荐理由：将二维 poloidal particle coupling、radial finite differences 与截断 $m$ harmonics 组合进 GTC electrostatic gyrokinetics，同时给出 laptop 和 A100 的分项 timing。
- 一句话总结：作者在 ITG 指标上把 effective problem size 降低 48×，单 $n$、2000-step、约 2 million markers 的 laptop RTX 4090 算例为 78.2 s；1→16 A100 总体仅 8.66×，约 30 s 的单 rank Poisson 解已成为瓶颈。

### 3. Quantum Vacuum Nonlinearities in Laser Interferometers

- DOI：[10.48550/arXiv.2609.03314](https://doi.org/10.48550/arXiv.2609.03314)
- 提交日期：2026-09-03；稿件日期 / arXiv 新发布：2026-09-04
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.03314)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：daily/2026-09-05/pdfs/Mehdi et al. - 2026 - Quantum vacuum nonlinearities in laser interferometers.pdf
- 中文笔记：[Mehdi et al. - 2026 - Quantum vacuum nonlinearities in laser interferometers.md](notes/Mehdi%20et%20al.%20-%202026%20-%20Quantum%20vacuum%20nonlinearities%20in%20laser%20interferometers.md)
- 专业相似度分：4.5/5
- 推荐理由：把 Euler–Heisenberg forward scattering 映射到 standing-wave Fabry–Pérot cavity 的单模 phase shift 与双模 polarization differential readout，并明确给出功率、finesse、squeezing 和积分时间缩放。
- 一句话总结：作者预测 $\mathcal F=7\times10^5$、1 W 输入、约 700 kW circulating power 时，shot-noise-limited 单模 SNR 可在一天接近 1；这是依赖最小 mode volume 和完整噪声抑制的理论方案，不是已观测的真空双折射。

### 4. Generalized multi-dimensional conservation laws for stimulated Raman and Brillouin scattering in a density gradient

- 正式 DOI：[10.1103/hdkp-2mpm](https://doi.org/10.1103/hdkp-2mpm)
- 接收日期：2026-09-04
- 来源：[APS accepted papers 页面](https://journals.aps.org/pre/accepted/10.1103/hdkp-2mpm)
- 期刊 / 平台：Physical Review E accepted paper；本地全文为对应 [arXiv:2604.00295v2](https://arxiv.org/abs/2604.00295v2) author preprint
- 本地 PDF：daily/2026-09-05/pdfs/Patel et al. - 2026 - Generalized multidimensional conservation laws for SRS and SBS.pdf
- 中文笔记：[Patel et al. - 2026 - Generalized multidimensional conservation laws for SRS and SBS.md](notes/Patel%20et%20al.%20-%202026%20-%20Generalized%20multidimensional%20conservation%20laws%20for%20SRS%20and%20SBS.md)
- 专业相似度分：5/5
- 推荐理由：从三波 paraxial Lagrangian 系统导出 density-gradient 中 action、energy、momentum 和 OAM 的多维局域守恒式，并给 pF3D 类代码留下可实现的 residual checks。
- 一句话总结：phase symmetries 给出含横向通量的多维 Manley–Rowe，真实 $z$ translation 因 $\phi'(z)$ 失配产生动量源项；effective OAM index matching 只在各 index 沿传播不变时成立。

## 未入库但需保留的候选

- [Cone-guided phase-space control of laser-driven proton beams](https://journals.aps.org/pre/accepted/10.1103/d45l-hsgg)（DOI：10.1103/d45l-hsgg）于 2026-09-04 被 Physical Review E 接收，摘要与 laser-driven proton beam 高度相关；但 APS PDF 与 DOI PDF 本轮均返回 HTTP 403，且未找到对应开放预印本，因此没有把摘要扩写成全文笔记，也没有写入 processed ledger。
- arXiv:2609.03479 的 conical plasma-channel LWFA 与 arXiv:2609.03768 的 physics-informed high-order mixed derivative 方法均完成摘要筛选；相较本轮 4 篇，它们对 PIC 算法、可量化性能或当前 QED/laser–plasma 证据链的新增价值较低，留待后续去重检索。

## 当日综合总结

- An 与 Bao 都在降低高维粒子模拟成本，但压缩维度不同：前者保留有限 azimuthal modes 并修正主轴 Maxwell dispersion，后者在 gyrokinetic ITG 中截断 toroidal/poloidal harmonics；二者都不能泛化为任意三维物理无损。
- Patel 为三波 envelope code 提供守恒诊断基准：多维边界通量、damping sinks 和 density-gradient momentum source 必须一起计入。它可用于数值审计，不代表新的 SRS/SBS 实验或 PIC 结果。
- Mehdi 的低能 QED 路线依赖相位相干积累，与强激光产生高能 photon/pair 的诊断链不同；“一天可达”是理想 shot-noise 估算，下一步首先应补齐工程 noise budget。
- 本轮未找到可同时闭合 laser-accelerated beam、converter γ 谱、光核/中子/活化产额、剂量和 shielding 的新实验全文；不得把数值 axion source、理论 cavity SNR 或 gyrokinetic benchmark 写成实验观测。
- 推荐阅读顺序：先读 An 抓住累计数值色散，再读 Patel 建立三波守恒校验，再读 Bao 比较物理截断与性能收益，最后读 Mehdi 审查理想 QED signal 对工程噪声的依赖。
