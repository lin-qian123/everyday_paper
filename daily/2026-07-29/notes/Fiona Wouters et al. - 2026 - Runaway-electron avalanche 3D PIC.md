# Implementation and verification of the avalanche source in a 3D full-f particle-in-cell model of relativistic electrons for studies of tokamak disruptions

## 基本信息

- 作者：F. Wouters; H. Bergström; M. Hoelzl; G. T. A. Huijsmans; J. van Dijk; JOREK team
- 期刊/平台：arXiv preprint
- DOI：https://doi.org/10.48550/arXiv.2607.24602
- 发表时间：2026-07-27
- 来源链接：https://arxiv.org/abs/2607.24602
- 本地 PDF：`daily/2026-07-29/pdfs/Fiona Wouters et al. - 2026 - Runaway-electron avalanche 3D PIC.pdf`

## 研究问题

托卡马克破裂中，敲出碰撞引发的 runaway-electron（RE）雪崩会形成多 MA 束流；已有三维 MHD 场中的 RE 模拟需要同时描述雪崩源、相空间输运和标记粒子数的指数增长。

## 方法与模型

- 在 JOREK 的三维非线性 MHD--相对论 full-f PIC 混合模型中实现能量、动量守恒的二体 knock-on 碰撞算子。
- 使用导引中心五维 `(R,Z,φ,p∥,μ)` 重采样控制标记粒子数，并以文献解析增长率验证。
- 在 JET-like 终止场景测试三维 MHD 活跃条件下的再雪崩。

## 主要结论

- 碰撞算子可保留高 pitch-angle、受困及逆电场传播的二次 RE，从而给出比简化源项更完整的相空间描述。
- 重采样显著减少标记数，仍保留三维结构；全局能量、动量守恒表现良好，但不等同于逐局域严格守恒。
- JET-like 案例显示，再雪崩优先出现在 RE 密度与平行电场都高的区域；考虑 RE 电流对电场的反馈后仍可见 RE 增长。

## 与本仓库方向的关系

- 连接 PIC、磁约束聚变、逃逸电子与反应堆壁面/热负荷风险。
- 主题关键词：runaway electron；tokamak disruption；full-f PIC；knock-on collision；JOREK。
- 相关性评分：4/5。

## 局限与注意事项

本文是预印本且案例为 JET-like 终止；长时间尺度、ITER 周期性终止与再雪崩仍需加速 HPC 和更完整的自洽 MHD--RE 反馈验证。
