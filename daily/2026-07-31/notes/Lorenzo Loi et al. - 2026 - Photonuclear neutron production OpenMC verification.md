# Photonuclear Neutron Production in OpenMC: Verification Against MCNPX, FLUKA, and a First-Collision Analytical Solution

## 基本信息

- 作者：Lorenzo Loi; Andrea Missaglia; Carolina Introini 等
- 期刊/平台：arXiv preprint（physics.app-ph；投稿 Nuclear Science and Engineering）
- DOI：https://doi.org/10.48550/arXiv.2607.26045
- 发表时间：2026-07-28
- 来源链接：https://arxiv.org/abs/2607.26045
- 本地 PDF：`daily/2026-07-31/pdfs/A. Rahman et al. - 2026 - Photonuclear neutron production OpenMC verification.pdf`

## 研究问题

面向高能光子转换靶、中子源、屏蔽和医学物理，尚未进入官方发行版的 OpenMC 光核模块能否在受控基准中正确给出光中子总产额？

## 方法与模型

- 构造六个单次碰撞（broomstick）基准：`²H`、`⁹Be`、`²³⁸U` 靶，分别受 `5 MeV`、`15 MeV` 单能光子和 `1--20 MeV` LINAC 代表谱照射。
- 在相同 ENDF7u 光核数据库下对照 OpenMC 开发分支与 MCNPX；另以 FLUKA 原生模型、首碰撞解析解和 IAEA/PD-2019 数据库做交叉比较。
- 同时报出积分中子产额与能谱，避免只以总产额判断二次粒子运动学正确性。

## 主要结论

- 在共同 ENDF7u 数据下，OpenMC 与 MCNPX 在六例积分中子产额上符合至 `0.7%` 内。
- 更换到 IAEA/PD-2019 后，相对 ENDF7u 解析参考的偏差最高约 `11.3%`；数据评价差异可大于同库代码差异。
- FLUKA 对单能例的积分产额差异约 `6--9%`，连续谱例不超过约 `4%`；即使总产额接近，`²H`、`⁹Be` 等例的中子谱仍可明显不同。

## 与本仓库方向的关系

- 为“激光加速电子束--转换靶韧致辐射--光核中子/活化”链条中的末端输运与屏蔽建模提供可追溯验证基线。
- 强调应把代码实现、核数据库和末态运动学三类不确定度分开；对中子诊断、剂量和辐射防护尤其重要。
- 主题关键词：photonuclear；photoneutron；OpenMC；MCNPX；FLUKA；nuclear data；shielding。
- 相关性评分：5/5。

## 局限与注意事项

这是非官方 OpenMC 开发分支的数值验证，不是对真实激光转换靶或实验产额的通用验证。几何刻意抑制多次相互作用与二次输运；用于工程靶、角分布、剂量或探测器响应前，仍需相应几何和实验基准。
