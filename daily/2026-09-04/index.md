# 每日论文索引 - 2026-09-04

## 今日概览

- 运行日期：2026-09-04
- 新增论文数：3
- 重点来源：1 篇 Nature Photonics 正式开放论文、2 篇官方 arXiv 预印本；其中 diffusion-surrogate 稿件注明已被 Nature Communications 接收，但本轮尚未检得正式 DOI 页面。
- 主题分布：实验 laser–plasma Raman amplification、非均匀等离子体中的 chirped-pulse forward Raman PIC 方案、物理方差锚定的生成式 diffusion plasma-transport surrogate。
- 检索范围：复查 Cambridge HPL 最新/accepted manuscripts、Nature Photonics 2026 年 9 月卷期；检查官方 arXiv physics.plasm-ph、physics.acc-ph、physics.comp-ph、nucl-ex 与 physics.ins-det 的 2026-09-03 新发布列表，并定向检查 strong-field QED、laser-driven γ/光核/中子与 particle-in-cell 关键词。
- 去重：按 DOI、规范化标题、历史 daily、重试队列、摘要和物理场景核对 state/processed_articles.json；三篇均未入库。Shaw 是正式期刊卷期新发现的 8 月漏项，Lei 与 Reichherzer 是 9 月 3 日新发布。
- PDF/正文：3 份全文均通过 PDF 文件头、file 类型、pdfinfo 页数/元数据、SHA-256、非空 pdftotext -layout 和 MinerU Markdown 转换；完整校验见 [pdf_validation.json](pdf_validation.json)。

## 论文清单

### 1. Laser–plasma amplification of an ultrabroadband laser pulse to 0.3 TW

- DOI：[10.1038/s41566-026-01977-1](https://doi.org/10.1038/s41566-026-01977-1)
- 在线发表：2026-08-03；2026 年 9 月卷期收录
- 来源：[Nature Photonics 正式开放论文](https://www.nature.com/articles/s41566-026-01977-1)
- 期刊 / 平台：Nature Photonics
- 本地 PDF：daily/2026-09-04/pdfs/Shaw et al. - 2026 - Laser-plasma amplification of an ultrabroadband pulse to 0.3 TW.pdf
- 中文笔记：[Shaw et al. - 2026 - Laser-plasma amplification of an ultrabroadband pulse to 0.3 TW.md](notes/Shaw%20et%20al.%20-%202026%20-%20Laser-plasma%20amplification%20of%20an%20ultrabroadband%20pulse%20to%200.3%20TW.md)
- 专业相似度分：5/5
- 推荐理由：以 heater–pump–seed 三束激光和 single-shot SPIDER 完成宽带 Raman 放大实验，并用 OSIRIS PIC 解释 nonlinear pump depletion 与 wave breaking 限制。
- 一句话总结：直接测得 seed 从 130 fs 压缩到 64 fs、输出约 0.31 TW，最高时间重叠修正效率 8.7%；另一个炮次净传能 222.8 ± 17.2 mJ、能量放大约 30 倍，但其超过 1.8 TW 的功率只是在无可用 SPIDER 情况下假定脉宽不变的估算。

### 2. Chirped-Pulse Forward Raman Amplification in Nonuniform Plasmas

- DOI：[10.48550/arXiv.2609.02326](https://doi.org/10.48550/arXiv.2609.02326)
- 提交日期：2026-09-02；arXiv 新发布：2026-09-03
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.02326)
- 期刊 / 平台：arXiv preprint
- 本地 PDF：daily/2026-09-04/pdfs/Lei et al. - 2026 - Chirped-Pulse Forward Raman Amplification in Nonuniform Plasmas.pdf
- 中文笔记：[Lei et al. - 2026 - Chirped-Pulse Forward Raman Amplification in Nonuniform Plasmas.md](notes/Lei%20et%20al.%20-%202026%20-%20Chirped-Pulse%20Forward%20Raman%20Amplification%20in%20Nonuniform%20Plasmas.md)
- 专业相似度分：5/5
- 推荐理由：把 density-gradient detuning 与正啁啾 seed 的频率序列配对，给出含失谐三波模型、实验参数窗及 EPOCH 1D/2D/3D PIC 验证。
- 一句话总结：有效增长条件为失谐小于两倍理想 FRA 增长率；基准 PIC 在不足 400 μm、约 1.8 ps 内预测约 10⁷ 倍强度增益和近单周期输出，二维示例达约 4 PW，但这些均不是实验测量。

### 3. Generative Diffusion Surrogates with Analytical Variance Schedule

- DOI：[10.48550/arXiv.2609.01705](https://doi.org/10.48550/arXiv.2609.01705)
- 提交日期：2026-09-01；arXiv 新发布：2026-09-03
- 来源：[arXiv 摘要页](https://arxiv.org/abs/2609.01705)
- 期刊 / 平台：arXiv preprint；作者注明 accepted for Nature Communications
- 本地 PDF：daily/2026-09-04/pdfs/Reichherzer et al. - 2026 - Generative Diffusion Surrogates with Analytical Variance Schedule.pdf
- 中文笔记：[Reichherzer et al. - 2026 - Generative Diffusion Surrogates with Analytical Variance Schedule.md](notes/Reichherzer%20et%20al.%20-%202026%20-%20Generative%20Diffusion%20Surrogates%20with%20Analytical%20Variance%20Schedule.md)
- 专业相似度分：4.5/5
- 推荐理由：只改 VE diffusion model 的 scalar noise schedule，就把 ballistic-to-diffusive variance law 写进生成时间，并对磁湍流粒子输运、test-particle simulation 与既有 proton-radiography 数据作联合验证。
- 一句话总结：telegraph-anchored schedule 在相同训练预算下重现规定的方差与入口 kurtosis 松弛，并在 diffusive regime 把模拟 kurtosis 残差控制在约 0.20 ± 0.05；但物理时间只在二阶矩层面校准，本文也没有运行新的等离子体实验。

## 当日综合总结

- Shaw 和 Lei 形成一组必须区分证据等级的 active plasma optics 对照：前者是 counter-propagating Raman 实验，后者是 co-propagating cFRA 理论/PIC 方案。实验已经证明 0.31 TW、64 fs 与最高 8.7% 修正效率，multi-PW 和近单周期 cFRA 尚是预测。
- Reichherzer 把已知 variance law 变成 diffusion model 的物理时钟，降低对中间时刻训练数据的需求；它适合分布级 transport inference，不替代逐粒子轨迹、完整 PIC/MHD 或 non-Gaussian memory model。
- 本轮定向检索未发现可同时闭合 laser-accelerated beam、converter γ 谱、光核/中子/活化产额、剂量和 shielding 的新实验论文。三篇都不能写成强场 QED 观测、粒子束应用或核产额实测。
- 推荐阅读顺序：先读 Shaw 建立实验可达基线，再读 Lei 比较 density-gradient/chirp 如何改变 Raman 增益窗口，最后读 Reichherzer 评估稀疏诊断下的 physics-anchored generative surrogate。
