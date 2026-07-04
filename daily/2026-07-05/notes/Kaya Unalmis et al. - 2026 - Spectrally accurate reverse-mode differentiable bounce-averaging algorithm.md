# Spectrally accurate, reverse-mode differentiable bounce-averaging algorithm and its applications

## 基本信息

- 作者：Kaya Unalmis; Rahul Gaur; Rory Conlin; Dario Panici; Egemen Kolemen
- 期刊/平台：Journal of Plasma Physics
- DOI：https://doi.org/10.1017/S0022377826101652
- 发表时间：2026-06
- 本地 PDF：`daily/2026-07-05/pdfs/Kaya Unalmis et al. - 2026 - Spectrally accurate reverse-mode differentiable bounce-averaging algorithm.pdf`

## 研究问题

Bounce averaging 常用于简化磁约束等离子体中的 kinetic models，尤其是低碰撞率 regime 下的 trapped-particle 动力学和 neoclassical transport 估计。问题在于传统实现往往难以同时满足高精度、高效率和可微优化需求。

## 方法与模型

- 提出快速、谱精度的 bounce-averaging 算法。
- 算法支持自动微分，尤其是 reverse-mode differentiation，便于处理包含大量设计变量的优化问题。
- 将实现嵌入 DESC stellarator optimization suite。
- 应用目标包括 effective ripple、低碰撞率 neoclassical transport 相关指标，以及 energetic particle confinement 代理量。

## 主要结论

- 该算法在精度上达到谱收敛特征，适合对 trapped-particle 轨道平均量做高精度计算。
- Reverse-mode differentiability 使其可直接进入 stellarator 形状优化和多目标优化流程。
- 论文展示了 kinetic model simplification 与 differentiable physics / optimization workflow 的实际结合路径。

## 与本仓库方向的关系

- 属于磁约束聚变、动理学建模、可微物理计算和先进算法交叉方向。
- 虽然不是激光等离子体论文，但与 PIC/kinetic simulation、机器学习/自动微分在等离子体物理中的应用高度相关。
- 对 stellarator 优化、energetic particle confinement 和 neoclassical transport 方向有方法参考价值。

## 阅读价值

- 适合关注 stellarator optimization、DESC、自动微分物理算法和 kinetic model reduction 的读者。
- 如果后续要整理“机器学习/可微计算在等离子体设计优化中的应用”，这篇是正式来源中的高价值方法论文。

## 局限与注意事项

- 算法主要针对 bounce-averaged kinetic quantities，并不直接替代全轨道或全分布函数动理学模拟。
- 工程设计结论依赖于 DESC 中的几何、目标函数和代理指标定义，跨代码复现时应关注实现细节。
