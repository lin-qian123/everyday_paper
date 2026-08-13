# Measurements of Laser-Driven Plasma Expansion into Hohlraum-Relevant Background Gas

## 基本信息

- 作者：S. Hilsabeck；S. Dannhoff；C. A. Walsh；M. Sherlock；G. D. Sutcliffe；E. R. Tubman
- 期刊/平台：*arXiv preprint*（`physics.plasm-ph`）
- DOI：https://doi.org/10.48550/arXiv.2608.11664
- 发表时间：2026-08-12
- 来源链接：https://arxiv.org/abs/2608.11664
- 本地 PDF：`daily/2026-08-14/pdfs/Laser driven plasma expansion hohlraum gas.pdf`

## 研究问题与方法

间接驱动 ICF 中，黑腔壁受激光烧蚀后的等离子体会向 He 气填充膨胀，改变内束传播、能量沉积和 X 射线驱动对称性。本文在 OMEGA EP 用 `2–5 μm` Cu 箔和 He 气体喷嘴构建单个壁吹离泡的替代平台，覆盖 `0.3`、`0.6 mg cm^-3` 等效气体密度。351 nm、约 `4.2–4.3 kJ`、4 ns 驱动（峰值约 `2.5×10^14 W cm^-2`）产生 Cu 等离子体；263 nm 阴影法/Wollaston 干涉和两轴 `≤30 MeV` TNSA 质子照相在 `1–4 ns` 诊断泡边界、密度结构与路径积分电磁场。结果与 Gorgon 扩展 MHD 和 HYDRA 辐射流体模拟比较。

## 主要结论

- 阴影法解析 Cu–He 界面、受激 He 冲击等结构；`0.6 mg cm^-3` 工况可分出三条边界，且 Cu 近靶面和压缩 He 层出现 `10–100 μm` 尺度丝状/湍动结构。
- 两个代码能再现大尺度形貌，却系统性高估膨胀：`0.3 mg cm^-3`、2 ns 时受激 He 前沿实验为 `0.930 mm`，Gorgon 为 `1.170 mm`（+26%），HYDRA 流体与 Biermann 工况分别为 `1.356 mm`（+46%）和 `1.438 mm`（+55%）；`0.6 mg cm^-3`、3 ns 时 Gorgon 为 `1.942 mm`，实验为 `1.412 mm`（+37%）。
- 调低 HYDRA 激光驱动至 70% 会缩小泡尺寸但未消除速度差，表明主因不只是能量标定。实验缺失的 `10–100 μm` 丝状结构和复杂质子通量调制指向自生磁场、磁化/非局域热输运与动理学不稳定性等缺失物理。
- 简化扩散估计给出 Cu–He 界面附近 Cu 离子减速平均自由程约 `0.3–1.1 μm`，`1/3 ns` 扩散尺度约 `7.2/12.5 μm`，不足以单独解释观测的大尺度差异；作者后续将反演质子照相场并扫描 Biermann 抑制、Nernst 平流和非局域热流。

## 与本仓库方向的关系

- 主题关键词：ICF；高能量密度物理；气填充黑腔；激光烧蚀；扩展 MHD；Biermann battery；质子照相；TNSA 诊断。
- 这是与真实高功率激光平台直接对应的实验—代码基准，能约束黑腔气填充、热输运与自生磁场模型；其 TNSA 质子背照明也为激光离子束诊断应用提供具体实验范例。
- 相关性评分：5/5。

## 局限与注意事项

该平台以单个 Cu 箔泡替代完整黑腔，不能直接给出胶囊内爆性能或实际 NIF/OMEGA 黑腔的驱动对称性。质子照相目前仅给出路径积分场/密度调制的定性与结构性约束，定量 E/B 反演仍在进行；Wollaston 干涉在较晚时刻受参考臂也被等离子体扰动的限制。两种模拟的差异提示需要动理学/磁化输运审计，而不能从此直接断言某一种不稳定性已经被唯一确认。
