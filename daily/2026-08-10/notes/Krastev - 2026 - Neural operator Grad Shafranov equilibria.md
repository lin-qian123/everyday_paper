# Millisecond-Scale Neural Operator Surrogates for Double-Null Free-Boundary Grad--Shafranov Equilibria

## 基本信息

- 作者：Plamen G. Krastev
- 期刊/平台：arXiv preprint（physics.plasm-ph；nucl-ex；physics.comp-ph）
- DOI：https://doi.org/10.48550/arXiv.2608.05555
- 发表时间：2026-08-06
- 来源链接：https://arxiv.org/abs/2608.05555
- 本地 PDF：`daily/2026-08-10/pdfs/Krastev - 2026 - Neural operator Grad Shafranov equilibria.pdf`

## 研究问题与方法

自由边界 Grad--Shafranov (GS) 平衡在控制、优化和数字孪生中需反复调用，但 Picard 迭代有样本相关延迟。作者以 FreeGS 为单一装置几何、双零位拓扑生成 6000 个受约束样本，训练几何条件 Fourier Neural Operator：输入空间坐标、`P_axis`、`I_p`、`f_vac` 与指定 X 点坐标，输出 `65×65` 极向磁通 `ψ(R,Z)`。验证除相对 L2 误差外，还检查分离面、X/O 点、边界通量和独立有限差分 GS 残差。

## 主要结论

- 在 500 个测试平衡上，最佳模型平均相对 L2 误差为 0.052%，物理 RMSE 为 `1.54×10^-5 Wb`；两个 X 点定位优于 0.2 cm，O 点误差 0.031 cm，平均最近点分离面偏差 0.072 cm。
- GPU/CPU 单平衡推理分别为 2.77/25.6 ms，相对本文配置下的 FreeGS 报告约 640 倍/69 倍加速；延迟 `p95/median=1.01`，低于迭代求解的 1.13。
- 预测场的有限差分归一化 GS 残差均值为 2.29，与 FreeGS 标签在同一离散诊断下的 `2.29±0.06` 不可区分；随训练样本数的测试误差近似 `N^-0.68` 缩放。

## 与本仓库方向的关系

- 主题关键词：Grad--Shafranov；tokamak；free boundary；Fourier Neural Operator；surrogate；fusion control；numerical simulation。
- 是机器学习加速等离子体数值求解的清晰案例：既量化场误差，又量化几何约束与离散 PDE 残差，适合作为 PIC 代理或多物理优化中“物理量--几何--延迟”三重验证的参照。
- 可服务于磁约束聚变控制与大参数扫描；其显式 X 点条件化也提示，设计代理不应被误写为从真实诊断或执行器直接重建平衡。
- 相关性评分：4/5。

## 局限与注意事项

所有训练和测试仅限一个壁面几何、一个受控双零位拓扑和固定 `65×65` 网格，未证明跨装置、跨拓扑或跨分辨率泛化。X 点是输入而不是预测量，模型并非从线圈/诊断信号出发的执行器级或反演级求解器；报告加速比也只相对本文 FreeGS 配置，不能外推到优化后的生产 C/Fortran 求解器或 warm-start 迭代。代码和数据仅称可向作者合理请求。
