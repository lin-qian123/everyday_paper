# Electromagnetically Driven Thermal Dissipation Scaling in Plasma Centrifuges for Mass Separation

## 基本信息

- 作者：Drue P. Hood-McFadden；Shreyas Kotla；Thomas C. Underwood
- 期刊/平台：arXiv preprint（physics.plasm-ph）
- DOI：https://doi.org/10.48550/arXiv.2607.28208
- 发表时间：2026-07-30
- 来源链接：https://arxiv.org/abs/2607.28208
- 本地 PDF：`daily/2026-08-01/pdfs/Hood-McFadden et al. - 2026 - Plasma centrifuge mass separation.pdf`

## 研究问题

电磁驱动等离子体离心机（EMDC）的洛伦兹力旋转会同时引起加热；如何用可检验的标度判断几何、磁场和电流密度何时有利于质量/同位素分离？

## 方法与模型

- 建立简化双温 MHD 模型，跟踪径向几何中转动与热耗散的耦合演化。
- 用离心参数 `λ = m Vθ²/(2 kB T)` 表示定向转动能相对热混合的强度。
- 以 Ar 与 Ar/Kr 实验标定：电流密度最高 `15 kA/m²`、磁场最高 `0.57 T`、压强 `0.5–3 Torr`、环隙尺度 `1–5 cm`；再模拟 `40Ar/36Ar`。

## 主要结论

- 体积式 `J×B` 驱动虽然峰值 `λ` 可低于壁面剪切离心机，却能在更大的径向体积维持较高 `λ`，提高积分分离效果。
- 联合优化电磁力与几何后，模型中 EMDC 的分离性能可超过受材料速度限制的剪切驱动离心机。
- 结果反驳“黏性耗散必然使弱电离等离子体离心机 `λ < 1`”的绝对判断；关键是扩展 `λ` 的径向分布，而非只提高峰值或面积平均值。

## 与本仓库方向的关系

- 直接覆盖同位素/质量分离这一束流与核技术邻近应用，也点名聚变偏滤器排气中的 D/T 选择性回收。
- 为等离子体装置中热输运、磁场/电流设计和分离效率之间的权衡提供可量化框架。
- 主题关键词：plasma centrifuge；mass separation；isotope；two-temperature MHD；Lorentz force；thermal dissipation。
- 相关性评分：4/5。

## 局限与注意事项

实验基准为 Ar 与 Ar/Kr，小规模、弱电离环隙装置；`40Ar/36Ar` 和聚变 D/T 的结论来自模型外推，尚不是实际核燃料循环或工业同位素系统的性能验证。
