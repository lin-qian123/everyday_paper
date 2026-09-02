# 每日论文索引 - 2026-09-03

## 今日概览

- 运行日期：2026-09-03
- 新增论文数：3
- 重点来源：2 篇正式期刊论文（Scientific Reports、Nature Photonics）与 1 篇官方 arXiv 预印本。
- 主题分布：涂层等离子体镜增强全光学逆康普顿散射、双激光 LWFA–ITS 可调谐 MeV γ 源、强激光—电子束相互作用中的自旋/偏振量子效应。
- 检索范围：复查 Cambridge HPL 最新/accepted manuscripts 与 JPP 当前页；检查官方 arXiv `physics.plasm-ph`、`physics.acc-ph`、`physics.comp-ph`、`nucl-ex`、`physics.ins-det` 最新提交，并定向检索 laser-plasma γ、strong-field QED、光核/中子和激光加速束流应用。
- 去重：按 DOI、规范化标题、历史 daily、重试队列、摘要及物理场景核对 `state/processed_articles.json`；三篇均未入库且不与近期条目构成内容近重复。
- PDF/正文：3 份全文均通过 `%PDF-` 文件头、`file` 类型、`pdfinfo` 页数/元数据、SHA-256、非空 `pdftotext -layout` 和 MinerU Markdown 转换。Hu 等对应的 Nature Photonics 期刊 PDF 在当前环境受 cookie/订阅路径限制，本地保存的是 DOI 关系明确的 Research Square v1 作者预印本；完整校验见 [`pdf_validation.json`](pdf_validation.json)。

## 论文清单

### 1. Enhanced inverse Compton scattering via spontaneous focusing induced by a coated plasma mirror

- DOI：[10.1038/s41566-026-01958-4](https://doi.org/10.1038/s41566-026-01958-4)
- 在线发表：2026-07-23
- 来源：[Nature Photonics 论文页](https://www.nature.com/articles/s41566-026-01958-4)
- 期刊 / 平台：Nature Photonics；本地全文为对应的 Research Square v1 作者预印本，不是出版社排版版
- 本地 PDF：`daily/2026-09-03/pdfs/Hu et al. - 2026 - Enhanced inverse Compton scattering via coated plasma mirror.pdf`
- 中文笔记：[Hu et al. - 2026 - Enhanced inverse Compton scattering via coated plasma mirror.md](notes/Hu%20et%20al.%20-%202026%20-%20Enhanced%20inverse%20Compton%20scattering%20via%20coated%20plasma%20mirror.md)
- 专业相似度分：`5/5`
- 推荐理由：用涂层 PM 的自发凹面聚焦提升反射场强，并以 100 TW/400 TW 实验、EPOCH PIC 和 Geant4 响应反演共同量化 γ 光子数、能谱及能量转换效率。
- 一句话总结：100 TW 下涂层/未涂层 PM 的光子数约为 `7.9×10^7/1.3×10^7`，临界能量约 `39/26 MeV`；400 TW 下涂层 PM 达约 `8×10^9` 个光子、`60 MeV` 临界能量和 `400 MeV` 截止能量，但自发聚焦的细节与谱重建仍含 PIC/响应模型依赖。

### 2. Stable and tunable MeV γ-ray generation via dual-laser inverse Thomson scattering from a laser-plasma accelerator

- DOI：[10.1038/s41598-026-56639-7](https://doi.org/10.1038/s41598-026-56639-7)
- 发表日期：2026-06-16
- 来源：[Scientific Reports 论文页](https://www.nature.com/articles/s41598-026-56639-7)
- 期刊 / 平台：Scientific Reports
- 本地 PDF：`daily/2026-09-03/pdfs/Tsai et al. - 2026 - Stable and tunable MeV gamma-ray generation via dual-laser ITS.pdf`
- 中文笔记：[Tsai et al. - 2026 - Stable and tunable MeV gamma-ray generation via dual-laser ITS.md](notes/Tsai%20et%20al.%20-%202026%20-%20Stable%20and%20tunable%20MeV%20gamma-ray%20generation%20via%20dual-laser%20ITS.md)
- 专业相似度分：`5/5`
- 推荐理由：在独立散射激光的双光束架构中同时给出电子束参数、γ 能谱、光子数、长时稳定性和射线照相，形成较完整的 LWFA–ITS 实验闭环。
- 一句话总结：电子能量调到 `122–204 MeV` 时，γ 特征能量为 `0.28±0.08`、`0.61±0.15` 和 `1.2±0.35 MeV`，光子数最高约 `2×10^7/shot`；近 1000 发运行的 rms 波动为 `5.5%`，但 NRF/光裂变只是应用设想，未在本文实测。

### 3. Polarized quantum effects in countable signals from intense laser - electron beam interactions

- DOI：[10.48550/arXiv.2609.01494](https://doi.org/10.48550/arXiv.2609.01494)
- 提交日期：2026-09-01；稿件日期：2026-09-02
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.01494)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：`daily/2026-09-03/pdfs/Moritaka et al. - 2026 - Polarized quantum effects in countable laser-electron signals.pdf`
- 中文笔记：[Moritaka et al. - 2026 - Polarized quantum effects in countable laser-electron signals.md](notes/Moritaka%20et%20al.%20-%202026%20-%20Polarized%20quantum%20effects%20in%20countable%20laser-electron%20signals.md)
- 专业相似度分：`5/5`
- 推荐理由：把非线性 Compton、Breit–Wheeler、电子自旋和光子偏振纳入可计数信号预测，并以 SLAC E-144 历史实验作 Monte Carlo 基准。
- 一句话总结：ELI-NP 参考工况的 Monte Carlo 预测把高能光子边缘从经典非线性模型的约 `314 MeV` 推到约 `360 MeV`，偏振/自旋使正电子产额降低约 `20–30%`、大角度自旋差异可到约 `12%`；这些是模拟预测，不是 ELI-NP 的实验观测。

## 当日综合总结

- 两篇正式论文互补地展示全光学 γ 源的两条路线：Hu 用单激光 + 涂层 PM 自发聚焦提升场强和高能尾部，Tsai 用独立散射脉冲换取能量调谐、稳定性和成像能力。前者能量更高，后者对运行与应用诊断的闭环更完整。
- Moritaka 从自旋/偏振分辨的 Monte Carlo 角度提醒：当 `χ` 接近量子辐射区时，仅用经典 nonlinear Thomson/Compton 图景会偏移谱边并高估对产生计数，实验设计应同时保留能谱、偏振和角分布。
- 证据边界：Hu、Tsai 的核心 γ 结果是实验，但局部场强、机制和部分能谱依赖 PIC/Geant4/反演；Moritaka 的 ELI-NP 数值完全是预测。三篇都没有测量光核截面、NRF、光裂变、中子/活化产额、剂量或屏蔽性能。
- 对当前研究最值得优先阅读的顺序：若关注高能量与转换效率，先读 Hu；若关注稳定可调谐源和诊断闭环，先读 Tsai；若要设计强场 QED 可辨识量和计数统计，再读 Moritaka。
