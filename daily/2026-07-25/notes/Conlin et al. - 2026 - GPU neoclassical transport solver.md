# yancc: A GPU-accelerated, differentiable solver for neoclassical transport in tokamaks and stellarators

## 基本信息

- 作者：Rory Conlin; Matt Landreman
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.20861
- 发表时间：2026-07-23
- 来源链接：https://arxiv.org/abs/2607.20861
- 本地 PDF：`daily/2026-07-25/pdfs/Conlin et al. - 2026 - GPU neoclassical transport solver.pdf`

## 研究问题

Tokamak 与 stellarator 的新经典输运计算需要反复求解高维、强对流和各向异性的漂移动理学方程；全物理模型昂贵、内存占用高，限制装置优化与不确定度扫描。本文提出兼顾物理保真度和 GPU 效率的可微求解器。

## 方法与模型

- `yancc` 求解保留速度相关碰撞、能量散射和完整种间耦合的四维漂移动理学方程，并提供单能约化形式。
- 在速度用 Maxwell 多项式配点、在俯仰角和磁通面坐标用有限差分；以改进迎风模板、multigrid 预条件 Krylov 法提升高 Péclet 数收敛性。
- 使用 JAX 实现自动微分，和 MONKES、SFINCS 在多碰撞率、几何与多组分案例比较。

## 主要结论

- 相对 MONKES 与 SFINCS 的基准比较在所示范围内一致到 1% 以内。
- 每个参数扫描的速度约为 SFINCS 的一个数量级，同时内存约低一个数量级，且跨碰撞率的运行时间近似平坦。
- 自动微分使梯度优化、伴随灵敏度、stellarator 优化和输运系数不确定度分析可直接接入。

## 与本仓库方向的关系

- 该工作补强 PIC/动理学数值方法与磁约束聚变的交叉能力，尤其适合高通量扫描和数据驱动输运模型的物理基线构建。
- 主题关键词：drift kinetic equation；neoclassical transport；GPU；JAX；multigrid；tokamak；stellarator。
- 相关性评分：4/5。

## 局限与注意事项

模型在小归一化回旋半径近似下忽略径向耦合，不能直接覆盖全轨道宽度或全局输运效应；论文所报性能也需在目标 GPU、分辨率和实际几何上复现评估。
