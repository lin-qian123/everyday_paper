# Parameter Scan of Multi-Fluid Equilibria in Rotating p-11B Plasmas: Effects on Fusion Power and Bremsstrahlung Losses

## 基本信息

- 作者：Xingyu Li; Huasheng Xie; Lai Wei; Zhengxiong Wang
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.14496
- 发表时间：2026-07-16
- 来源链接：https://arxiv.org/abs/2607.14496
- 本地 PDF：`daily/2026-07-18/pdfs/Xingyu Li et al. - 2026 - Rotating p-11B bremsstrahlung losses.pdf`

## 研究问题

p-11B 聚变具有中子少的吸引力，但需要很高离子能量，同时电子韧致辐射损失严重。论文关注的问题是：在球形 tokamak 型旋转多流体平衡中，质子和硼离子的同转/差分环向旋转如何共同影响密度重分布、聚变功率和韧致辐射功率。

## 方法与模型

- 提出 `VEQ-MF` 快速谱参数扫描框架，用于二维轴对称、多物种、给定物种依赖环向旋转的平衡计算。
- 模型耦合广义 Boltzmann 密度响应、准中性静电极化和广义 Grad-Shafranov 方程。
- 在 EHL-2 和 EHL-3B 几何中扫描质子与硼的旋转频率。
- 后处理阶段用 drift-Maxwellian 反应率系数估算聚变功率，并用解析辐射模型计算韧致辐射损失。

## 主要结论

- 同转情况下，重硼离子向外侧聚集会提高体积分的 `n_e^2`，使聚变功率与韧致辐射功率比随旋转增强而下降。
- 物种差分旋转会削弱离心极化、降低韧致辐射，同时相对环向流可提高 drift-Maxwellian 反应率系数。
- 在固定扫描设定下，EHL-3B 案例中功率比可从同转时约 `0.18` 增至最大差分环向流附近约 `1.3`。
- 论文强调该工作是参数扫描和诊断分解 benchmark，不等同于 p-11B 反应堆可行性评估。

## 与本仓库方向的关系

- 论文直接涉及聚变等离子体、韧致辐射损失、多流体平衡和参数扫描工具。
- 对扩展主题中的核反应应用、辐射损失评估、束流/等离子体能量分配和 p-11B 高能量密度路线有参考价值。
- 主题关键词：p-11B fusion；bremsstrahlung loss；multi-fluid equilibrium；toroidal rotation；parameter scan；fusion power。
- 相关性评分：4/5。

## 阅读价值

适合关注 p-11B、韧致辐射损失和旋转多物种等离子体平衡的人阅读。它的主要价值在于把密度重叠项和反应率系数项拆开诊断，有助于避免只看总功率比而误判物理来源。

## 局限与注意事项

模型把旋转、温度和剖面作为给定控制参数，没有自洽计算维持差分旋转所需的动量交换功率、摩擦热化和工程约束。因此结果更适合作为机制分解与代码 benchmark，而不是直接的能量增益结论。
