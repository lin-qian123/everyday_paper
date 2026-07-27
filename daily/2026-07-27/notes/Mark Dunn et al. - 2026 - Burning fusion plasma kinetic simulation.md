# A Multi-Species Reactive-Boltzmann Formulation for Self-Consistent Kinetic Simulation of Burning Fusion Plasmas

## 基本信息

- 作者：Mark Dunn; Jingwei Hu; Uri Shumlak
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.21723
- 发表时间：2026-07-23
- 来源链接：https://arxiv.org/abs/2607.21723
- 本地 PDF：`daily/2026-07-27/pdfs/Mark Dunn et al. - 2026 - Burning fusion plasma kinetic simulation.pdf`

## 研究问题

NIF 燃烧等离子体实验与辐射流体模型的差异，是否可能来自聚变产物碰撞弛豫造成的非 Maxwell 反应离子分布。

## 方法与模型

- 建立多组分反应--弹性动理学框架，反应源汇由速度分布上的 reactive Boltzmann 算子直接计算。
- 用 Landau/Lenard--Bernstein 小角碰撞近似与快速 Fourier 谱离散，在三维速度空间求解 D--D 体系。

## 主要结论

- 聚变产物加热不会在早期弱耦合 D--D 体系中产生显著超热反应离子群。
- 相对于 Maxwell 分布的偏离和聚变反应率变化均较小，为相关简化假设提供动理学检验。

## 与本仓库方向的关系

- 补强 HEDP/ICF、聚变反应率与高阶动理学模拟方法。
- 主题关键词：burning plasma；reactive Boltzmann；fusion reactivity；Landau collision；NIF。
- 相关性评分：4/5。

## 局限与注意事项

数值实验是空间均匀、早期弱耦合 D--D 情形；不能直接外推到完整 NIF 靶、强空间梯度或 D--T 燃烧阶段。
